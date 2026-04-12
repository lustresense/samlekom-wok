"""
SIMRP Authentication Module
Handles login, register, admin-login, logout, and session management.
"""
import re
from core import (
    execute, commit, get_db,
    hash_password, verify_password, generate_token,
    EMAIL_PATTERN, SESSION_TTL_HOURS, RATE_LIMIT_AUTH_MAX,
)
from api.rate_limiter import check_rate_limit
from datetime import datetime, timezone, timedelta
import uuid


def utc_now_iso():
    """Get current UTC time in ISO format."""
    return datetime.now(timezone.utc).isoformat()


def valid_email(email):
    """Validate email format."""
    return bool(re.match(EMAIL_PATTERN, str(email).strip()))


def valid_password(password):
    """Validate password strength."""
    s = str(password or "")
    if len(s) < 8:
        return False
    has_alpha = any(c.isalpha() for c in s)
    has_digit = any(c.isdigit() for c in s)
    return has_alpha and has_digit


def get_user_from_token(token):
    """Get user data from session token."""
    now = utc_now_iso()
    row = execute(
        "SELECT users.* FROM sessions JOIN users ON users.id = sessions.user_id WHERE sessions.token = ? AND sessions.expires_at > ?",
        (token, now)
    ).fetchone()
    return row


def create_session(user_id, ttl_hours=SESSION_TTL_HOURS):
    """Create a new session for user."""
    token = generate_token()
    now = utc_now_iso()
    expires = (datetime.now(timezone.utc) + timedelta(hours=ttl_hours)).isoformat()
    execute("INSERT INTO sessions(token, user_id, expires_at, created_at) VALUES(?, ?, ?, ?)", 
            (token, user_id, expires, now))
    commit()
    return token


def get_user_payload(user):
    """Convert user database row to API payload."""
    kel = execute(
        "SELECT kelurahan.name AS kel_name, kecamatan.name AS kec_name FROM kelurahan JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id WHERE kelurahan.id = ?",
        (user["kelurahan_id"],)
    ).fetchone() if user["kelurahan_id"] else None
    
    total_xp = execute("SELECT total_xp FROM xp_kelurahan WHERE kelurahan_id = ?", 
                       (user["kelurahan_id"],)).fetchone() if user["kelurahan_id"] else None
    volunteers = execute("SELECT COUNT(*) AS c FROM users WHERE kelurahan_id = ? AND role_code IN ('user', 'ksh')", 
                         (user["kelurahan_id"],)).fetchone()["c"] if user["kelurahan_id"] else 0
    
    import json
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "role": "admin" if user["role_code"] == "admin" else ("moderator" if user["role_code"].startswith("moderator_t") else "user"),
        "roleCode": user["role_code"],
        "isKsh": bool(user["is_ksh"]),
        "moderatorTier": user["moderator_tier"],
        "tier2Badge": user["tier2_badge"],
        "kelurahan": kel["kel_name"] if kel else None,
        "kecamatan": kel["kec_name"] if kel else None,
        "kampungId": user["kelurahan_id"],
        "kampung": {
            "id": user["kelurahan_id"],
            "name": kel["kel_name"],
            "kecamatan": kel["kec_name"],
            "xp": int(total_xp["total_xp"]) if total_xp else 0,
            "volunteers": volunteers
        } if kel else None,
        "points": int(user["points"]),
        "badges": json.loads(user["badges_json"] or "[]"),
        "hasPendingReport": False,
    }


def handle_login(handler, body, client_ip):
    """Handle user login endpoint."""
    if check_rate_limit("auth-login", client_ip, RATE_LIMIT_AUTH_MAX):
        return handler.send_json(429, {"error": "Terlalu banyak percobaan login"})
    
    email = str(body.get("email", "")).strip().lower()
    password = str(body.get("password", ""))
    
    if not valid_email(email):
        return handler.send_json(400, {"error": "Format email tidak valid"})
    
    user = execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    if not user or not verify_password(password, user["password_hash"]):
        return handler.send_json(401, {"error": "Email/password salah"})
    
    token = create_session(user["id"])
    return handler.send_json(200, {"success": True, "token": token, "user": get_user_payload(user)})


def handle_admin_login(handler, body, client_ip):
    """Handle admin login endpoint."""
    if check_rate_limit("auth-admin-login", client_ip, RATE_LIMIT_AUTH_MAX):
        return handler.send_json(429, {"error": "Terlalu banyak percobaan login admin"})
    
    username = str(body.get("username", "")).strip()
    password = str(body.get("password", ""))
    
    admin = execute("SELECT * FROM users WHERE role_code = 'admin' LIMIT 1").fetchone()
    if not admin or not verify_password(password, admin["password_hash"]):
        return handler.send_json(401, {"error": "Invalid credentials"})
    
    token = create_session(admin["id"])
    return handler.send_json(200, {"success": True, "token": token, "user": get_user_payload(admin)})


def handle_signup(handler, body, client_ip):
    """Handle user registration endpoint."""
    if check_rate_limit("auth-signup", client_ip, RATE_LIMIT_AUTH_MAX):
        return handler.send_json(429, {"error": "Terlalu banyak percobaan signup"})
    
    if not all([body.get("email"), body.get("password"), body.get("name")]):
        return handler.send_json(400, {"error": "Email, password, name wajib"})
    
    email = str(body.get("email")).strip().lower()
    password = body.get("password")
    name = str(body.get("name")).strip()[:120]
    
    if not valid_email(email):
        return handler.send_json(400, {"error": "Format email tidak valid"})
    
    if not valid_password(password):
        return handler.send_json(400, {"error": "Password minimal 8 karakter dan kombinasi huruf-angka"})
    
    if execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone():
        return handler.send_json(400, {"error": "Email sudah terdaftar"})
    
    kelurahan_name = str(body.get("kelurahan", "")).strip()
    kel = execute(
        "SELECT kelurahan.id AS id, kecamatan.id AS kec_id FROM kelurahan JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id WHERE kelurahan.name = ? LIMIT 1",
        (kelurahan_name,)
    ).fetchone()
    
    if not kel:
        return handler.send_json(400, {"error": "Kelurahan tidak ditemukan"})
    
    user_id = str(uuid.uuid4())
    now = utc_now_iso()
    
    execute(
        """INSERT INTO users(id, name, email, password_hash, role_code, is_ksh, email_verified,
           kelurahan_id, kecamatan_id, points, badges_json, created_at, updated_at)
           VALUES(?, ?, ?, ?, 'user', 0, 1, ?, ?, 0, '[]', ?, ?)""",
        (user_id, name, email, hash_password(password), kel["id"], kel["kec_id"], now, now)
    )
    commit()
    
    token = create_session(user_id)
    user = execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    return handler.send_json(200, {"success": True, "token": token, "user": get_user_payload(user)})


def handle_logout(handler, token):
    """Handle logout endpoint."""
    execute("DELETE FROM sessions WHERE token = ?", (token,))
    commit()
    return handler.send_json(200, {"success": True})


def handle_get_me(handler, token):
    """Handle get current user endpoint."""
    user = get_user_from_token(token)
    if not user:
        return handler.send_json(401, {"error": "Unauthorized"})
    return handler.send_json(200, {"user": get_user_payload(user)})


# Routes dictionary for main.py
auth_routes = {
    "POST": {
        "/auth/login": handle_login,
        "/auth/admin-login": handle_admin_login,
        "/auth/signup": handle_signup,
        "/auth/logout": lambda h, b, ip: handle_logout(h, h.headers.get("Authorization", "").replace("Bearer ", "")),
    },
    "GET": {
        "/auth/me": lambda h, b, ip: handle_get_me(h, h.headers.get("Authorization", "").replace("Bearer ", "")),
    },
}
