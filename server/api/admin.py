"""
SIMRP Admin Module
Admin-only operations: user management, temporary adjustments.
"""
from core import execute, commit, generate_entity_id, utc_now_iso, MIN_TEMP_POINTS, MAX_TEMP_POINTS
from datetime import datetime, timezone, timedelta
import json


def get_admin_stats(handler, body, client_ip):
    """Get admin dashboard statistics."""
    user = handler.get_current_user()
    if not user or user["roleCode"] != "admin":
        return handler.send_json(403, {"error": "Admin only"})
    
    stats = {
        "users": {"total": execute("SELECT COUNT(*) as c FROM users").fetchone()["c"]},
        "events": {"total": execute("SELECT COUNT(*) as c FROM events").fetchone()["c"]},
        "reports": {"pending": execute("SELECT COUNT(*) as c FROM event_reports WHERE status = 'pending'").fetchone()["c"]},
    }
    return handler.send_json(200, stats)


def get_temporary_adjustments(handler, body, client_ip):
    """Get all temporary adjustments."""
    user = handler.get_current_user()
    if not user or user["roleCode"] != "admin":
        return handler.send_json(403, {"error": "Admin only"})
    
    rows = execute("""
        SELECT temporary_adjustments.*, users.name AS user_name
        FROM temporary_adjustments JOIN users ON users.id = temporary_adjustments.user_id
        ORDER BY temporary_adjustments.created_at DESC
    """).fetchall()
    
    adjustments = []
    for r in rows:
        value = json.loads(r["value_json"])
        adjustments.append({
            "id": r["id"], "type": r["adjustment_type"],
            "value": value.get("points") if r["adjustment_type"] == "points" else value.get("badgeId", ""),
            "reason": r["reason"], "grantedAt": r["created_at"], "expiresAt": r["expires_at"],
            "targetUserName": r["user_name"],
        })
    return handler.send_json(200, {"adjustments": adjustments})


def add_temporary_points(handler, body, client_ip):
    """Add temporary points to user."""
    user = handler.get_current_user()
    if not user or user["roleCode"] != "admin":
        return handler.send_json(403, {"error": "Admin only"})
    
    points = int(body.get("points", 0))
    if points < MIN_TEMP_POINTS or points > MAX_TEMP_POINTS:
        return handler.send_json(400, {"error": f"Penyesuaian poin maksimal {MIN_TEMP_POINTS} sampai {MAX_TEMP_POINTS}"})
    
    now = utc_now_iso()
    execute("UPDATE users SET points = points + ?, updated_at = ? WHERE id = ?", (points, now, body.get("userId")))
    execute("INSERT INTO temporary_adjustments(id, user_id, adjustment_type, value_json, reason, expires_at, created_at) VALUES(?, ?, 'points', ?, ?, ?, ?)",
            (generate_entity_id("adjust"), body.get("userId"), json.dumps({"points": points}), body.get("reason", "admin points"), 
             (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat(), now))
    commit()
    return handler.send_json(200, {"success": True})


admin_routes = {
    "GET": {"/admin/stats": get_admin_stats, "/admin/temporary-adjustments": get_temporary_adjustments},
    "POST": {"/admin/add-temporary-points": add_temporary_points},
}
