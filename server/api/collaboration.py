"""
SIMRP Collaboration Module
Collaboration request management.
"""
from core import execute, commit, generate_entity_id, utc_now_iso, VALID_SUPPORT_TYPES, VALID_CONTRIBUTION_SCOPES


def get_collaboration_requests(handler, body, client_ip, query_params=None):
    """Get all collaboration requests."""
    user = handler.get_current_user()
    if not user or user["roleCode"] not in ("moderator_t2", "admin"):
        return handler.send_json(403, {"error": "Hanya Moderator Tier 2/Admin"})
    
    status_filter = query_params.get("status", [None])[0] if query_params else None
    sql = "SELECT * FROM collaboration_requests WHERE 1=1"
    params = []
    
    if status_filter in ("pending", "approved", "rejected"):
        sql += " AND status = ?"
        params.append(status_filter)
    sql += " ORDER BY created_at DESC"
    
    rows = execute(sql, tuple(params)).fetchall()
    requests = [dict(r) for r in rows]
    return handler.send_json(200, {"requests": requests})


def create_collaboration_request(handler, body, client_ip):
    """Create new collaboration request."""
    required = ["organizationName", "picName", "email", "supportType", "supportDescription"]
    for field in required:
        if not body.get(field):
            return handler.send_json(400, {"error": f"{field} wajib diisi"})
    
    support_type = str(body.get("supportType")).strip().lower()
    if support_type not in VALID_SUPPORT_TYPES:
        return handler.send_json(400, {"error": "Jenis dukungan tidak valid"})
    
    contribution_scope = str(body.get("contributionScope", "kota")).strip().lower()
    if contribution_scope not in VALID_CONTRIBUTION_SCOPES:
        return handler.send_json(400, {"error": "Skala kontribusi tidak valid"})
    
    request_id = generate_entity_id("collab")
    now = utc_now_iso()
    
    execute(
        """INSERT INTO collaboration_requests(id, organization_name, pic_name, email, support_type, contribution_scope, support_description, status, reviewed_by_user_id, reviewed_at, created_at, updated_at)
           VALUES(?, ?, ?, ?, ?, ?, ?, 'pending', NULL, NULL, ?, ?)""",
        (request_id, body.get("organizationName"), body.get("picName"), body.get("email"), 
         support_type, contribution_scope, body.get("supportDescription"), now, now)
    )
    commit()
    return handler.send_json(200, {"success": True, "request": {"id": request_id}})


def review_collaboration_request(handler, body, client_ip, request_id):
    """Review (approve/reject) collaboration request."""
    user = handler.get_current_user()
    if not user or user["roleCode"] not in ("moderator_t2", "admin"):
        return handler.send_json(403, {"error": "Hanya Moderator Tier 2/Admin yang boleh approve"})
    
    request = execute("SELECT id, status FROM collaboration_requests WHERE id = ?", (request_id,)).fetchone()
    if not request:
        return handler.send_json(404, {"error": "Permintaan tidak ditemukan"})
    if request["status"] != "pending":
        return handler.send_json(400, {"error": "Permintaan sudah diproses"})
    
    approved = bool(body.get("approved", False))
    now = utc_now_iso()
    
    execute("UPDATE collaboration_requests SET status = ?, reviewed_by_user_id = ?, reviewed_at = ?, updated_at = ? WHERE id = ?",
            ("approved" if approved else "rejected", user["id"], now, now, request_id))
    commit()
    return handler.send_json(200, {"success": True})


collaboration_routes = {
    "GET": {"/collaboration-requests": get_collaboration_requests},
    "POST": {"/collaboration-requests": create_collaboration_request, "/collaboration-requests/{id}/approval": review_collaboration_request},
}
