"""
SIMRP Event Module
Event CRUD, approval, joining, and completion.
"""
from core import execute, commit, generate_entity_id, utc_now_iso, VALID_PILLARS, VALID_SCOPE_TYPES, RATE_LIMIT_MUTATION_MAX
from api.rate_limiter import check_rate_limit


def get_events(handler, body, client_ip, query_params=None):
    """Get all events with optional filters."""
    user = handler.get_current_user()
    if not user:
        return handler.send_json(401, {"error": "Unauthorized"})
    
    status_filter = query_params.get("status", [None])[0] if query_params else None
    sql = "SELECT * FROM events WHERE 1=1"
    params = []
    
    if status_filter:
        sql += " AND status = ?"
        params.append(status_filter)
    sql += " ORDER BY event_date ASC"
    
    rows = execute(sql, tuple(params)).fetchall()
    events = []
    for r in rows:
        parts = execute("SELECT user_id FROM event_participation WHERE event_id = ?", (r["id"],)).fetchall()
        events.append({
            "id": r["id"], "title": r["title"], "description": r["description"],
            "pillar": r["pillar"], "date": r["event_date"], "time": r["event_time"],
            "location": r["location"], "quota": r["quota"], "scopeType": r["scope_type"],
            "status": r["status"], "participants": [p["user_id"] for p in parts]
        })
    return handler.send_json(200, {"events": events})


def create_event(handler, body, client_ip):
    """Create new event."""
    if check_rate_limit("mutation", client_ip, RATE_LIMIT_MUTATION_MAX):
        return handler.send_json(429, {"error": "Terlalu banyak permintaan"})
    
    user = handler.get_current_user()
    if not user or user["roleCode"] not in ("moderator_t1", "admin"):
        return handler.send_json(403, {"error": "Hanya ASN Tier 1/Admin yang boleh input kegiatan"})
    
    title = str(body.get("title", "")).strip()[:200]
    if not title:
        return handler.send_json(400, {"error": "Judul wajib diisi"})
    
    pillar = int(body.get("pillar", 1))
    if pillar not in VALID_PILLARS:
        return handler.send_json(400, {"error": "Pilar harus 1-4"})
    
    scope_type = str(body.get("scopeType", "kelurahan")).strip().lower()
    if scope_type not in VALID_SCOPE_TYPES:
        return handler.send_json(400, {"error": "Skala kegiatan harus kelurahan atau kecamatan"})
    
    kecamatan_id = int(body.get("kecamatanId"))
    kelurahan_id = int(body["kelurahanId"]) if body.get("kelurahanId") and scope_type == "kelurahan" else None
    
    event_id = generate_entity_id("event")
    now = utc_now_iso()
    
    execute(
        """INSERT INTO events(id, title, description, pillar, event_date, event_time, location, quota,
           scope_type, kecamatan_id, kelurahan_id, created_by_user_id, status, created_at, updated_at)
           VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'draft', ?, ?)""",
        (event_id, title, body.get("description", ""), pillar, body.get("date"), 
         body.get("time", ""), body.get("location", ""), int(body.get("quota", 0)),
         scope_type, kecamatan_id, kelurahan_id, user["id"], now, now)
    )
    commit()
    return handler.send_json(200, {"success": True, "event": {"id": event_id}})


def join_event(handler, body, client_ip, event_id):
    """Join an event."""
    if check_rate_limit("mutation", client_ip, RATE_LIMIT_MUTATION_MAX):
        return handler.send_json(429, {"error": "Terlalu banyak permintaan"})
    
    user = handler.get_current_user()
    if not user or user["roleCode"] not in ("user", "ksh"):
        return handler.send_json(403, {"error": "Hanya relawan/KSH yang dapat mendaftar"})
    
    event = execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
    if not event or event["status"] != "published":
        return handler.send_json(400, {"error": "Event belum dipublish"})
    
    if event["quota"] > 0:
        count = execute("SELECT COUNT(*) AS c FROM event_participation WHERE event_id = ?", (event_id,)).fetchone()["c"]
        if count >= event["quota"]:
            return handler.send_json(400, {"error": "Kuota penuh"})
    
    now = utc_now_iso()
    execute("INSERT OR IGNORE INTO event_participation(event_id, user_id, status, checklist_done, created_at, updated_at) VALUES(?, ?, 'registered', 0, ?, ?)",
            (event_id, user["id"], now, now))
    commit()
    return handler.send_json(200, {"success": True})


def approve_event(handler, body, client_ip, event_id):
    """Approve/reject event."""
    user = handler.get_current_user()
    if not user or user["roleCode"] not in ("moderator_t2", "admin"):
        return handler.send_json(403, {"error": "Hanya Moderator Tier 2/Admin yang boleh approve"})
    
    event = execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
    if not event:
        return handler.send_json(404, {"error": "Event tidak ditemukan"})
    
    approved = bool(body.get("approved", False))
    status = "published" if approved else "draft"
    published_at = utc_now_iso() if approved else None
    
    execute("UPDATE events SET status = ?, published_at = COALESCE(published_at, ?), updated_at = ? WHERE id = ?",
            (status, published_at, utc_now_iso(), event_id))
    commit()
    return handler.send_json(200, {"success": True})


def complete_event(handler, body, client_ip, event_id):
    """Mark event as completed."""
    user = handler.get_current_user()
    if not user or not user["isKsh"]:
        return handler.send_json(403, {"error": "Hanya KSH yang bisa menandai selesai"})
    
    event = execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
    if not event or event["status"] != "published":
        return handler.send_json(400, {"error": "Event harus published sebelum completed"})
    
    output_summary = str(body.get("outputSummary", "")).strip()
    if not output_summary:
        return handler.send_json(400, {"error": "Output summary wajib diisi"})
    
    now = utc_now_iso()
    execute("UPDATE events SET status = 'completed', output_summary = ?, completed_at = ?, completed_by_user_id = ?, updated_at = ? WHERE id = ?",
            (output_summary, now, user["id"], now, event_id))
    execute("UPDATE event_participation SET status = 'attended', updated_at = ? WHERE event_id = ?", (now, event_id))
    commit()
    return handler.send_json(200, {"success": True})


event_routes = {
    "GET": {"/events": get_events},
    "POST": {
        "/events": create_event,
        "/events/{id}/join": join_event,
        "/events/{id}/approval": approve_event,
        "/events/{id}/complete": complete_event,
    },
}
