"""
SIMRP Authentication Module.

The active runtime still owns the database connection and shared helpers in
server/main.py. These handlers receive those dependencies explicitly so auth
routing can be moved out of main.py without changing security behavior.
"""
import hmac
import uuid


def _json(deps, handler, status, payload):
  deps["write_json"](handler, status, payload)
  return True


def _auth_header(handler):
  return handler.headers.get("Authorization")


def _bearer_token(handler):
  auth = _auth_header(handler)
  if not auth or not auth.startswith("Bearer "):
    return None
  return auth.split(" ", 1)[1].strip()


def handle_get(handler, conn, path, deps):
  """Handle GET /auth/* routes. Returns True when a route was handled."""
  api_prefix = deps["API_PREFIX"]

  if path == f"{api_prefix}/auth/me":
    user = deps["user_from_token"](conn, _auth_header(handler))
    if not user:
      return _json(deps, handler, 401, {"error": "Unauthorized"})
    return _json(deps, handler, 200, {"user": deps["get_user_payload"](conn, user)})

  return False


def handle_post(handler, conn, path, body, deps):
  """Handle POST /auth/* routes. Returns True when a route was handled."""
  api_prefix = deps["API_PREFIX"]
  write_json = lambda target, status, payload: _json(deps, target, status, payload)
  execute = deps["execute"]

  if path == f"{api_prefix}/auth/signup":
    if deps["rate_limited"](handler, "auth-signup", deps["RATE_LIMIT_AUTH_MAX"], deps["RATE_LIMIT_WINDOW_SECONDS"]):
      return write_json(handler, 429, {"error": "Terlalu banyak percobaan signup, coba lagi nanti"})
    if not body.get("email") or not body.get("password") or not body.get("name"):
      return write_json(handler, 400, {"error": "Email, password, name wajib"})
    email = str(body.get("email")).strip().lower()
    if not deps["valid_email"](email):
      return write_json(handler, 400, {"error": "Format email tidak valid"})
    if not deps["valid_password"](body.get("password")):
      return write_json(handler, 400, {"error": "Password minimal 8 karakter dan kombinasi huruf-angka"})
    name = deps["bounded_text"](body.get("name"), 120)
    nik = deps["bounded_text"](body.get("nik", ""), 32)
    rw = deps["bounded_text"](body.get("rw", ""), 16)
    if conn.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone():
      return write_json(handler, 400, {"error": "Email sudah terdaftar"})
    kel_name = deps["bounded_text"](body.get("kelurahan"), 120)
    kel = conn.execute(
      """
      SELECT kelurahan.id AS id, kecamatan.id AS kec_id
      FROM kelurahan JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
      WHERE kelurahan.name = ? LIMIT 1
      """,
      (kel_name,),
    ).fetchone()
    if not kel:
      return write_json(handler, 400, {"error": "Kelurahan tidak ditemukan"})
    user_id = str(uuid.uuid4())
    now = deps["utc_now_iso"]()
    execute(
      conn,
      """
      INSERT INTO users(
        id, name, email, password_hash, nik, rw, role_code, is_ksh, moderator_tier, email_verified,
        kelurahan_id, kecamatan_id, points, badges_json, created_at, updated_at
      )
      VALUES(?, ?, ?, ?, ?, ?, 'user', 0, NULL, 1, ?, ?, 0, '[]', ?, ?)
      """,
      (
        user_id,
        name,
        email,
        deps["hash_password"](body.get("password")),
        nik,
        rw,
        kel["id"],
        kel["kec_id"],
        now,
        now,
      ),
    )
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    token = deps["create_session"](conn, user_id)
    return write_json(handler, 200, {"success": True, "token": token, "user": deps["get_user_payload"](conn, user)})

  if path == f"{api_prefix}/auth/login":
    if deps["rate_limited"](handler, "auth-login", deps["RATE_LIMIT_AUTH_MAX"], deps["RATE_LIMIT_WINDOW_SECONDS"]):
      return write_json(handler, 429, {"error": "Terlalu banyak percobaan login, coba lagi nanti"})
    email = str(body.get("email", "")).strip().lower()
    if not deps["valid_email"](email):
      return write_json(handler, 400, {"error": "Format email tidak valid"})
    password = str(body.get("password", ""))
    user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    if not user or not deps["verify_password"](password, user["password_hash"]):
      return write_json(handler, 401, {"error": "Email/password salah"})
    token = deps["create_session"](conn, user["id"])
    return write_json(handler, 200, {"success": True, "token": token, "user": deps["get_user_payload"](conn, user)})

  if path == f"{api_prefix}/auth/admin-login":
    if deps["rate_limited"](handler, "auth-admin-login", deps["RATE_LIMIT_AUTH_MAX"], deps["RATE_LIMIT_WINDOW_SECONDS"]):
      return write_json(handler, 429, {"error": "Terlalu banyak percobaan login admin, coba lagi nanti"})
    if not deps["ADMIN_LOGIN_USERNAME"] or not deps["ADMIN_LOGIN_PASSWORD"]:
      return write_json(handler, 403, {"error": "Admin login tidak dikonfigurasi"})
    username = str(body.get("username", "")).strip()
    password = str(body.get("password", ""))
    expected_username = deps["ADMIN_LOGIN_USERNAME"]
    expected_password = deps["ADMIN_LOGIN_PASSWORD"]
    valid_user = hmac.compare_digest(username, expected_username)
    valid_pass = hmac.compare_digest(password, expected_password)
    if not valid_user or not valid_pass:
      return write_json(handler, 401, {"error": "Invalid credentials"})
    admin = conn.execute("SELECT * FROM users WHERE role_code = 'admin' LIMIT 1").fetchone()
    if not admin:
      return write_json(handler, 500, {"error": "Akun admin tidak ditemukan"})
    token = deps["create_session"](conn, admin["id"])
    return write_json(handler, 200, {"success": True, "token": token, "user": deps["get_user_payload"](conn, admin)})

  if path == f"{api_prefix}/auth/logout":
    token = _bearer_token(handler)
    if not token:
      return write_json(handler, 401, {"error": "Unauthorized"})
    execute(conn, "DELETE FROM sessions WHERE token = ?", (token,))
    return write_json(handler, 200, {"success": True})

  return False


def handle_delete(handler, conn, path, deps):
  """Handle DELETE /auth/* routes. Returns True when a route was handled."""
  api_prefix = deps["API_PREFIX"]

  if path == f"{api_prefix}/auth/logout":
    actor = deps["user_from_token"](conn, _auth_header(handler))
    if not actor:
      return _json(deps, handler, 401, {"error": "Unauthorized"})
    token = _bearer_token(handler)
    if not token:
      return _json(deps, handler, 401, {"error": "Unauthorized"})
    deps["execute"](conn, "DELETE FROM sessions WHERE token = ?", (token,))
    return _json(deps, handler, 200, {"success": True})

  return False


auth_routes = {
  "GET": ("/auth/me",),
  "POST": ("/auth/signup", "/auth/login", "/auth/admin-login", "/auth/logout"),
  "DELETE": ("/auth/logout",),
}
