"""
SIMRP Report Module
Report creation and verification.
"""
import json
from core import execute, commit, generate_entity_id, utc_now_iso, RATE_LIMIT_MUTATION_MAX
from api.rate_limiter import check_rate_limit


def get_reports(handler, body, client_ip, query_params=None):
    """Get all reports with filters."""
    user = handler.get_current_user()
    if not user:
        return handler.send_json(401, {"error": "Unauthorized"})
    
    status_filter = query_params.get("status", [None])[0] if query_params else None
    sql = "SELECT * FROM event_reports WHERE 1=1"
    params = []
    
    if status_filter:
        sql += " AND status = ?"
        params.append(status_filter)
    sql += " ORDER BY created_at DESC"
    
    rows = execute(sql, tuple(params)).fetchall()
    reports = [{
        "id": r["id"], "eventId": r["event_id"], "userId": r["user_id"],
        "participants": int(r["participants"]), "status": r["status"],
        "points": int(r["points_awarded"]), "createdAt": r["created_at"],
    } for r in rows]
    return handler.send_json(200, {"reports": reports})


def create_report(handler, body, client_ip):
    """Create new report."""
    if check_rate_limit("mutation", client_ip, RATE_LIMIT_MUTATION_MAX):
        return handler.send_json(429, {"error": "Terlalu banyak permintaan"})
    
    user = handler.get_current_user()
    if not user or user["roleCode"] not in ("user", "ksh"):
        return handler.send_json(403, {"error": "Hanya relawan/KSH yang dapat lapor"})
    
    event_id = body.get("eventId")
    if not event_id:
        return handler.send_json(400, {"error": "Event ID wajib diisi"})
    
    event = execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
    if not event or event["status"] != "completed":
        return handler.send_json(400, {"error": "Laporan hanya setelah event selesai"})
    
    try:
        participants = int(body.get("participants", 1))
        if participants < 1 or participants > 10000:
            raise ValueError()
    except:
        return handler.send_json(400, {"error": "Jumlah peserta harus 1-10000"})
    
    outcome_tags = body.get("outcomeTags", [])
    if not isinstance(outcome_tags, list) or len(outcome_tags) > 20:
        return handler.send_json(400, {"error": "Outcome tags harus array (max 20)"})
    
    report_id = generate_entity_id("report")
    now = utc_now_iso()
    
    execute(
        """INSERT INTO event_reports(id, event_id, user_id, participants, checklist_json, outcome_tags_json, photo_url, status, points_awarded, created_at, updated_at)
           VALUES(?, ?, ?, ?, ?, ?, ?, 'pending', 0, ?, ?)""",
        (report_id, event_id, user["id"], participants, json.dumps({"attendance": True}), json.dumps(outcome_tags), body.get("photoUrl"), now, now)
    )
    commit()
    return handler.send_json(200, {"success": True, "report": {"id": report_id}})


def verify_report(handler, body, client_ip, report_id):
    """Verify (approve/reject) report."""
    user = handler.get_current_user()
    if not user or user["roleCode"] not in ("moderator_t2", "admin"):
        return handler.send_json(403, {"error": "Hanya Moderator Tier 2/Admin yang boleh verifikasi"})
    
    report = execute("SELECT * FROM event_reports WHERE id = ?", (report_id,)).fetchone()
    if not report or report["status"] != "pending":
        return handler.send_json(404, {"error": "Report tidak ditemukan atau sudah diproses"})
    
    approved = bool(body.get("approved", False))
    now = utc_now_iso()
    
    if approved:
        event = execute("SELECT * FROM events WHERE id = ?", (report["event_id"],)).fetchone()
        base_xp = 20 + (int(report["participants"]) * 2)
        gained_xp = base_xp  # Simplified - full XP calculation in production
        
        execute("UPDATE xp_kelurahan SET total_xp = total_xp + ?, updated_at = ? WHERE kelurahan_id = ?",
                (gained_xp, now, event["kelurahan_id"]))
        execute("UPDATE users SET points = points + 5, updated_at = ? WHERE id = ?", (now, report["user_id"]))
        execute("UPDATE event_reports SET status = 'verified', points_awarded = ?, verified_by_user_id = ?, verified_at = ?, updated_at = ? WHERE id = ?",
                (gained_xp, user["id"], now, now, report_id))
    else:
        execute("UPDATE event_reports SET status = 'rejected', verified_by_user_id = ?, verified_at = ?, updated_at = ? WHERE id = ?",
                (user["id"], now, now, report_id))
    
    commit()
    return handler.send_json(200, {"success": True})


report_routes = {
    "GET": {"/reports": get_reports},
    "POST": {"/reports": create_report, "/reports/{id}/verify": verify_report},
}
