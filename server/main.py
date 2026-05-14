import json
import os
import re
import sqlite3
import uuid
import hmac
import secrets
import hashlib
import sys
import threading
import time
from datetime import datetime, timedelta, timezone
from hashlib import pbkdf2_hmac
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_DIR = ROOT_DIR / "database"
DB_PATH = Path(os.environ.get("SIMRP_DB_PATH", str(DB_DIR / "runtime" / "database.db")))
GEO_PATH = ROOT_DIR / "src" / "data" / "geographicData.ts"
API_PREFIX = "/make-server-32aa5c5c"
DEV_CREDENTIALS_PATH = DB_PATH.parent / "dev_credentials.txt"
_DEV_CREDENTIAL_NOTES = []


def generate_runtime_secret():
  return secrets.token_urlsafe(24)


def record_dev_credential(label, identifier, env_name, secret):
  if IS_PRODUCTION:
    return
  _DEV_CREDENTIAL_NOTES.append({
    "label": label,
    "identifier": identifier,
    "env_name": env_name,
    "secret": secret,
  })


def write_dev_credentials_file():
  if IS_PRODUCTION or not _DEV_CREDENTIAL_NOTES:
    return
  lines = [
    "SIMRP local development credentials",
    "Generated because one or more demo credential environment variables were not set.",
    "This file is under database/runtime/ and must stay ignored by Git.",
    "",
  ]
  for item in _DEV_CREDENTIAL_NOTES:
    lines.extend([
      f"[{item['label']}]",
      item["identifier"],
      f"{item['env_name']}={item['secret']}",
      "",
    ])
  DEV_CREDENTIALS_PATH.parent.mkdir(parents=True, exist_ok=True)
  DEV_CREDENTIALS_PATH.write_text("\n".join(lines), encoding="utf-8")
  print(f"[SECURITY] Local development credentials file: {DEV_CREDENTIALS_PATH}")

if str(ROOT_DIR) not in sys.path:
  sys.path.insert(0, str(ROOT_DIR))

from api import auth as auth_api
from api import events as events_api
from api import reports as reports_api
from api import collaboration as collaboration_api
from api import geographic as geographic_api
from api import admin as admin_api
from api import notifications as notifications_api
from api import certificates as certificates_api
from api import rewards as rewards_api
from api import users as users_api


def env_flag(name, default=False):
  raw = os.environ.get(name)
  if raw is None:
    return default
  value = str(raw).strip().lower()
  return value in ("1", "true", "yes", "on", "y")

APP_ENV = str(os.environ.get("SIMRP_ENV", "development")).strip().lower()
IS_PRODUCTION = APP_ENV in ("prod", "production")
PBKDF2_ITERATIONS = int(os.environ.get("SIMRP_PBKDF2_ITERATIONS", "210000"))
MAX_BODY_BYTES = int(os.environ.get("SIMRP_MAX_BODY_BYTES", str(8 * 1024 * 1024)))
SESSION_TTL_HOURS = int(os.environ.get("SIMRP_SESSION_TTL_HOURS", "24" if IS_PRODUCTION else "168"))
RATE_LIMIT_WINDOW_SECONDS = int(os.environ.get("SIMRP_RATE_LIMIT_WINDOW_SECONDS", "60"))
RATE_LIMIT_AUTH_MAX = int(os.environ.get("SIMRP_RATE_LIMIT_AUTH_MAX", "10"))
RATE_LIMIT_MUTATION_MAX = int(os.environ.get("SIMRP_RATE_LIMIT_MUTATION_MAX", "120"))
HOST = str(os.environ.get("SIMRP_HOST", "0.0.0.0" if IS_PRODUCTION else "127.0.0.1")).strip()
PORT = int(os.environ.get("SIMRP_PORT", "8000"))
ENABLE_DEMO_SEED = env_flag("SIMRP_ENABLE_DEMO_SEED", not IS_PRODUCTION)
DEMO_PASSWORD = str(os.environ.get("SIMRP_DEMO_PASSWORD", "")).strip()

DEV_ALLOWED_ORIGINS = {
  "http://localhost:5173",
  "http://127.0.0.1:5173",
}
raw_allowed_origins = str(os.environ.get("SIMRP_ALLOWED_ORIGINS", "")).strip()
ALLOWED_ORIGINS = {item.strip() for item in raw_allowed_origins.split(",") if item.strip()}

ADMIN_LOGIN_USERNAME = str(os.environ.get("SIMRP_ADMIN_LOGIN_USERNAME", "")).strip()
ADMIN_LOGIN_PASSWORD = str(os.environ.get("SIMRP_ADMIN_LOGIN_PASSWORD", "")).strip()
if not ADMIN_LOGIN_USERNAME and not IS_PRODUCTION:
  ADMIN_LOGIN_USERNAME = "admin"
if not ADMIN_LOGIN_PASSWORD and not IS_PRODUCTION:
  ADMIN_LOGIN_PASSWORD = generate_runtime_secret()
  record_dev_credential("Admin portal", f"username={ADMIN_LOGIN_USERNAME}", "SIMRP_ADMIN_LOGIN_PASSWORD", ADMIN_LOGIN_PASSWORD)
if ENABLE_DEMO_SEED and not DEMO_PASSWORD:
  if IS_PRODUCTION:
    raise RuntimeError("SIMRP_DEMO_PASSWORD is required when SIMRP_ENABLE_DEMO_SEED=true in production")
  DEMO_PASSWORD = generate_runtime_secret()
  record_dev_credential(
    "Demo user accounts",
    "emails=relawan.demo@simrp.app, moderator1.demo@simrp.app, ksh.demo@simrp.app, ...",
    "SIMRP_DEMO_PASSWORD",
    DEMO_PASSWORD,
  )

_rate_lock = threading.Lock()
_rate_hits = {}

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def utc_now_iso():
  return datetime.now(timezone.utc).isoformat()


def hash_password(password):
  salt = os.urandom(16)
  digest = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, PBKDF2_ITERATIONS)
  return f"{salt.hex()}:{digest.hex()}"


def verify_password(password, encoded):
  try:
    salt_hex, digest_hex = encoded.split(":", 1)
    salt = bytes.fromhex(salt_hex)
    expected = bytes.fromhex(digest_hex)
  except Exception:
    return False
  got = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, PBKDF2_ITERATIONS)
  return hmac.compare_digest(got, expected)


def valid_email(email):
  return bool(EMAIL_PATTERN.match(str(email or "").strip()))


def valid_password(password):
  s = str(password or "")
  if len(s) < 8:
    return False
  has_alpha = any(ch.isalpha() for ch in s)
  has_digit = any(ch.isdigit() for ch in s)
  return has_alpha and has_digit


def bounded_text(value, max_len):
  text = str(value or "").strip()
  if len(text) > max_len:
    raise ValueError(f"Input terlalu panjang (maksimal {max_len} karakter)")
  return text


def client_ip(handler):
  forwarded = str(handler.headers.get("X-Forwarded-For", "")).strip()
  if forwarded:
    return forwarded.split(",")[0].strip()
  return str(handler.client_address[0] if handler.client_address else "unknown")


def resolve_cors_origin(handler):
  origin = str(handler.headers.get("Origin", "")).strip()
  if not origin:
    return None
  if origin in ALLOWED_ORIGINS:
    return origin
  if not IS_PRODUCTION and origin in DEV_ALLOWED_ORIGINS:
    return origin
  return None


def add_common_headers(handler):
  handler.send_header("X-Content-Type-Options", "nosniff")
  handler.send_header("X-Frame-Options", "DENY")
  handler.send_header("Referrer-Policy", "no-referrer")
  handler.send_header("Permissions-Policy", "geolocation=(), microphone=(), camera=()")
  handler.send_header("Cache-Control", "no-store")
  if IS_PRODUCTION:
    handler.send_header("Strict-Transport-Security", "max-age=63072000; includeSubDomains; preload")
    handler.send_header(
      "Content-Security-Policy",
      "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self'",
    )
  origin = resolve_cors_origin(handler)
  if origin:
    handler.send_header("Access-Control-Allow-Origin", origin)
    handler.send_header("Vary", "Origin")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
    handler.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")


def rate_limited(handler, bucket, limit, window_seconds):
  now = time.time()
  key = f"{bucket}:{client_ip(handler)}"
  with _rate_lock:
    hits = _rate_hits.get(key, [])
    threshold = now - window_seconds
    hits = [item for item in hits if item >= threshold]
    if len(hits) >= limit:
      _rate_hits[key] = hits
      return True
    hits.append(now)
    _rate_hits[key] = hits
  return False


def open_sqlite(path):
  conn = sqlite3.connect(str(path), timeout=30)
  conn.row_factory = sqlite3.Row
  # Use WAL journaling in production for better concurrency; fallback to MEMORY
  # for environments where file journals may be blocked.
  if IS_PRODUCTION:
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
  else:
    conn.execute("PRAGMA journal_mode = MEMORY")
    conn.execute("PRAGMA synchronous = NORMAL")
  conn.execute("PRAGMA temp_store = MEMORY")
  conn.execute("PRAGMA foreign_keys = ON")
  return conn


def connect_db():
  return open_sqlite(DB_PATH)


def execute(conn, sql, params=()):
  cur = conn.execute(sql, params)
  return cur


def log_audit(conn, actor_id, action, entity_type, entity_id, payload=None):
  safe_payload = payload if isinstance(payload, dict) else {"value": payload}
  execute(
    conn,
    """
    INSERT INTO audit_logs(actor_user_id, action, entity_type, entity_id, payload_json, created_at)
    VALUES(?, ?, ?, ?, ?, ?)
    """,
    (
      actor_id,
      bounded_text(action, 120),
      bounded_text(entity_type, 120),
      str(entity_id) if entity_id is not None else None,
      json.dumps(safe_payload or {}, ensure_ascii=True),
      utc_now_iso(),
    ),
  )


def create_notification(conn, user_id, notif_type, title, message, entity_type=None, entity_id=None):
  if not user_id:
    return None
  cur = execute(
    conn,
    """
    INSERT INTO notifications(user_id, type, title, message, is_read, entity_type, entity_id, created_at)
    VALUES(?, ?, ?, ?, 0, ?, ?, ?)
    """,
    (
      user_id,
      bounded_text(notif_type, 80),
      bounded_text(title, 180),
      bounded_text(message, 2000),
      bounded_text(entity_type, 120) if entity_type else None,
      str(entity_id) if entity_id is not None else None,
      utc_now_iso(),
    ),
  )
  return int(cur.lastrowid)


def parse_geo_data():
  content = GEO_PATH.read_text(encoding="utf-8")
  rows = []
  current = None
  in_kelurahan_block = False

  kec_code_pattern = re.compile(r"kode:\s*'(\d{7})'")
  kec_name_pattern = re.compile(r"nama:\s*'([^']+)'")
  kel_pattern = re.compile(
    r"\{\s*kode:\s*'(\d{10})'\s*,\s*nama:\s*'([^']+)'\s*,\s*kodepos:\s*\[([^\]]*)\]"
  )
  code_pattern = re.compile(r"'(\d{5})'")

  for raw_line in content.splitlines():
    line = raw_line.strip()
    if not line or line.startswith("//"):
      continue

    if current is None:
      code_match = kec_code_pattern.search(line)
      if code_match:
        current = {"kode": code_match.group(1), "nama": "", "kelurahan": []}
      continue

    if "kelurahan:" in line and "[" in line:
      in_kelurahan_block = True
      continue

    if in_kelurahan_block:
      if line.startswith("]"):
        in_kelurahan_block = False
        continue
      kel_match = kel_pattern.search(line)
      if kel_match:
        kel_code, kel_name, code_block = kel_match.groups()
        current["kelurahan"].append(
          {"kode": kel_code, "nama": kel_name, "kodepos": code_pattern.findall(code_block)}
        )
      continue

    if not current["nama"]:
      name_match = kec_name_pattern.search(line)
      if name_match:
        current["nama"] = name_match.group(1)
      continue

    if line.startswith("},") or line.startswith("}"):
      if current["kode"] and current["nama"]:
        rows.append(current)
      current = None
      in_kelurahan_block = False

  if current and current["kode"] and current["nama"]:
    rows.append(current)
  return rows


def get_geo_stats():
  parsed = parse_geo_data()
  kecamatan_total = len(parsed)
  kelurahan_total = sum(len(kec.get("kelurahan", [])) for kec in parsed)
  postal_codes = {
    code
    for kec in parsed
    for kel in kec.get("kelurahan", [])
    for code in kel.get("kodepos", [])
    if isinstance(code, str) and len(code) == 5
  }
  return {
    "kecamatan": kecamatan_total,
    "kelurahan": kelurahan_total,
    "kodepos": len(postal_codes),
  }


def write_json(handler, code, payload):
  body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
  handler.send_response(code)
  handler.send_header("Content-Type", "application/json")
  handler.send_header("Content-Length", str(len(body)))
  add_common_headers(handler)
  handler.end_headers()
  handler.wfile.write(body)


def parse_json_body(handler):
  length = int(handler.headers.get("Content-Length", "0"))
  if length <= 0:
    return {}
  if length > MAX_BODY_BYTES:
    raise ValueError("Payload terlalu besar")
  content_type = str(handler.headers.get("Content-Type", "")).lower()
  if content_type and "application/json" not in content_type:
    raise ValueError("Content-Type harus application/json")
  raw = handler.rfile.read(length).decode("utf-8")
  if not raw:
    return {}
  try:
    return json.loads(raw)
  except json.JSONDecodeError as exc:
    raise ValueError("Format JSON tidak valid") from exc


def create_session(conn, user_id):
  token = secrets.token_urlsafe(48)
  now = utc_now_iso()
  expires = (datetime.now(timezone.utc) + timedelta(hours=SESSION_TTL_HOURS)).isoformat()
  execute(
    conn,
    "INSERT INTO sessions(token, user_id, expires_at, created_at) VALUES(?, ?, ?, ?)",
    (token, user_id, expires, now),
  )
  return token


def user_from_token(conn, auth_header):
  if not auth_header or not auth_header.startswith("Bearer "):
    return None
  token = auth_header.split(" ", 1)[1].strip()
  return conn.execute(
    """
    SELECT users.*
    FROM sessions
    JOIN users ON users.id = sessions.user_id
    WHERE sessions.token = ? AND sessions.expires_at > ?
    """,
    (token, utc_now_iso()),
  ).fetchone()


def init_schema():
  DB_PATH.parent.mkdir(parents=True, exist_ok=True)
  conn = connect_db()
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS roles (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      code TEXT NOT NULL UNIQUE,
      name TEXT NOT NULL
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS role_attributes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      role_id INTEGER NOT NULL,
      attribute_key TEXT NOT NULL,
      attribute_value TEXT NOT NULL,
      FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS kecamatan (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      code TEXT NOT NULL UNIQUE,
      name TEXT NOT NULL UNIQUE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS kelurahan (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      code TEXT NOT NULL UNIQUE,
      kecamatan_id INTEGER NOT NULL,
      name TEXT NOT NULL,
      FOREIGN KEY (kecamatan_id) REFERENCES kecamatan(id) ON DELETE CASCADE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS postal_codes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      code TEXT NOT NULL UNIQUE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS kampung_mapping (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      kelurahan_id INTEGER NOT NULL,
      postal_code_id INTEGER NOT NULL,
      UNIQUE(kelurahan_id, postal_code_id),
      FOREIGN KEY (kelurahan_id) REFERENCES kelurahan(id) ON DELETE CASCADE,
      FOREIGN KEY (postal_code_id) REFERENCES postal_codes(id) ON DELETE CASCADE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS users (
      id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      password_hash TEXT NOT NULL,
      nik TEXT,
      rw TEXT,
      role_code TEXT NOT NULL,
      is_ksh INTEGER NOT NULL DEFAULT 0,
      moderator_tier INTEGER,
      tier2_badge TEXT,
      email_verified INTEGER NOT NULL DEFAULT 1,
      kelurahan_id INTEGER,
      kecamatan_id INTEGER,
      points INTEGER NOT NULL DEFAULT 0,
      badges_json TEXT NOT NULL DEFAULT '[]',
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      FOREIGN KEY (kelurahan_id) REFERENCES kelurahan(id),
      FOREIGN KEY (kecamatan_id) REFERENCES kecamatan(id)
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS events (
      id TEXT PRIMARY KEY,
      title TEXT NOT NULL,
      description TEXT,
      pillar INTEGER NOT NULL,
      event_date TEXT NOT NULL,
      event_time TEXT,
      location TEXT,
      quota INTEGER NOT NULL DEFAULT 0,
      scope_type TEXT NOT NULL CHECK(scope_type IN ('kelurahan','kecamatan')),
      kecamatan_id INTEGER NOT NULL,
      kelurahan_id INTEGER,
      created_by_user_id TEXT NOT NULL,
      status TEXT NOT NULL CHECK(status IN ('draft','approved','published','completed')),
      output_summary TEXT,
      published_at TEXT,
      completed_at TEXT,
      completed_by_user_id TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      FOREIGN KEY (kecamatan_id) REFERENCES kecamatan(id),
      FOREIGN KEY (kelurahan_id) REFERENCES kelurahan(id),
      FOREIGN KEY (created_by_user_id) REFERENCES users(id)
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS event_participation (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      event_id TEXT NOT NULL,
      user_id TEXT NOT NULL,
      status TEXT NOT NULL CHECK(status IN ('registered','attended','reported')),
      checklist_done INTEGER NOT NULL DEFAULT 0,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      UNIQUE(event_id, user_id),
      FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
      FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS event_reports (
      id TEXT PRIMARY KEY,
      event_id TEXT NOT NULL,
      user_id TEXT NOT NULL,
      participants INTEGER NOT NULL,
      checklist_json TEXT NOT NULL,
      outcome_tags_json TEXT NOT NULL,
      photo_url TEXT,
      status TEXT NOT NULL CHECK(status IN ('pending','under_review','verified','rejected')),
      points_awarded INTEGER NOT NULL DEFAULT 0,
      verified_by_user_id TEXT,
      verified_at TEXT,
      reject_reason TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
      FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS xp_kelurahan (
      kelurahan_id INTEGER PRIMARY KEY,
      total_xp INTEGER NOT NULL DEFAULT 0,
      updated_at TEXT NOT NULL,
      FOREIGN KEY (kelurahan_id) REFERENCES kelurahan(id) ON DELETE CASCADE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS xp_pillar (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      kelurahan_id INTEGER NOT NULL,
      pillar INTEGER NOT NULL,
      xp INTEGER NOT NULL DEFAULT 0,
      updated_at TEXT NOT NULL,
      UNIQUE(kelurahan_id, pillar),
      FOREIGN KEY (kelurahan_id) REFERENCES kelurahan(id) ON DELETE CASCADE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS audit_logs (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      actor_user_id TEXT,
      action TEXT NOT NULL,
      entity_type TEXT NOT NULL,
      entity_id TEXT,
      payload_json TEXT NOT NULL DEFAULT '{}',
      created_at TEXT NOT NULL
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS collaboration_requests (
      id TEXT PRIMARY KEY,
      organization_name TEXT NOT NULL,
      pic_name TEXT NOT NULL,
      email TEXT NOT NULL,
      support_type TEXT NOT NULL CHECK(support_type IN ('dana','konsumsi','peralatan','media_partner','lainnya')),
      contribution_scope TEXT NOT NULL DEFAULT 'kota' CHECK(contribution_scope IN ('kota','kecamatan','kelurahan')),
      scope_kecamatan_id INTEGER,
      scope_kelurahan_id INTEGER,
      support_description TEXT NOT NULL,
      submitted_by_user_id TEXT,
      status TEXT NOT NULL CHECK(status IN ('pending','approved','rejected')),
      reviewed_by_user_id TEXT,
      reviewed_at TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      FOREIGN KEY (submitted_by_user_id) REFERENCES users(id),
      FOREIGN KEY (reviewed_by_user_id) REFERENCES users(id),
      FOREIGN KEY (scope_kecamatan_id) REFERENCES kecamatan(id),
      FOREIGN KEY (scope_kelurahan_id) REFERENCES kelurahan(id)
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS notifications (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id TEXT NOT NULL,
      type TEXT NOT NULL,
      title TEXT NOT NULL,
      message TEXT NOT NULL,
      is_read INTEGER NOT NULL DEFAULT 0,
      entity_type TEXT,
      entity_id TEXT,
      created_at TEXT NOT NULL,
      FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS certificates (
      id TEXT PRIMARY KEY,
      user_id TEXT NOT NULL,
      event_id TEXT NOT NULL,
      report_id TEXT NOT NULL,
      certificate_hash TEXT NOT NULL,
      issued_at TEXT NOT NULL,
      UNIQUE(user_id, event_id),
      FOREIGN KEY (user_id) REFERENCES users(id),
      FOREIGN KEY (event_id) REFERENCES events(id),
      FOREIGN KEY (report_id) REFERENCES event_reports(id)
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS voucher_catalog (
      id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      description TEXT,
      xp_cost INTEGER NOT NULL,
      stock INTEGER NOT NULL DEFAULT 0,
      is_active INTEGER NOT NULL DEFAULT 1,
      created_at TEXT NOT NULL
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS voucher_redemptions (
      id TEXT PRIMARY KEY,
      user_id TEXT NOT NULL,
      voucher_id TEXT NOT NULL,
      xp_spent INTEGER NOT NULL,
      voucher_code TEXT NOT NULL,
      redeemed_at TEXT NOT NULL,
      expires_at TEXT NOT NULL,
      FOREIGN KEY (user_id) REFERENCES users(id),
      FOREIGN KEY (voucher_id) REFERENCES voucher_catalog(id)
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS sessions (
      token TEXT PRIMARY KEY,
      user_id TEXT NOT NULL,
      expires_at TEXT NOT NULL,
      created_at TEXT NOT NULL,
      FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """,
  )
  execute(
    conn,
    """
    CREATE TABLE IF NOT EXISTS temporary_adjustments (
      id TEXT PRIMARY KEY,
      user_id TEXT NOT NULL,
      adjustment_type TEXT NOT NULL CHECK(adjustment_type IN ('points','badge','role')),
      value_json TEXT NOT NULL,
      reason TEXT NOT NULL,
      expires_at TEXT NOT NULL,
      created_at TEXT NOT NULL,
      FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """,
  )
  migrate_schema(conn)
  seed_roles(conn)
  seed_geography(conn)
  if ENABLE_DEMO_SEED:
    if IS_PRODUCTION:
      print("[SECURITY] WARNING: Demo seed is enabled in production (SIMRP_ENABLE_DEMO_SEED=true)")
    seed_demo(conn)
  conn.commit()
  conn.close()


def migrate_schema(conn):
  user_cols = {row["name"] for row in conn.execute("PRAGMA table_info(users)").fetchall()}
  if "tier2_badge" not in user_cols:
    execute(conn, "ALTER TABLE users ADD COLUMN tier2_badge TEXT")

  collab_cols = {row["name"] for row in conn.execute("PRAGMA table_info(collaboration_requests)").fetchall()}
  if "contribution_scope" not in collab_cols:
    execute(conn, "ALTER TABLE collaboration_requests ADD COLUMN contribution_scope TEXT NOT NULL DEFAULT 'kota'")
  if "scope_kecamatan_id" not in collab_cols:
    execute(conn, "ALTER TABLE collaboration_requests ADD COLUMN scope_kecamatan_id INTEGER")
  if "scope_kelurahan_id" not in collab_cols:
    execute(conn, "ALTER TABLE collaboration_requests ADD COLUMN scope_kelurahan_id INTEGER")
  if "submitted_by_user_id" not in collab_cols:
    execute(conn, "ALTER TABLE collaboration_requests ADD COLUMN submitted_by_user_id TEXT")

  report_cols = {row["name"] for row in conn.execute("PRAGMA table_info(event_reports)").fetchall()}
  if "reject_reason" not in report_cols:
    execute(conn, "ALTER TABLE event_reports ADD COLUMN reject_reason TEXT")

  # Migrasi CHECK constraint event_reports: tambah 'under_review' ke status yang valid.
  # Deteksi dengan mencoba SELECT yang pasti gagal jika constraint lama masih aktif.
  report_constraint_ok = False
  try:
    # Cara paling andal: cek sql teks di sqlite_master
    schema_row = conn.execute(
      "SELECT sql FROM sqlite_master WHERE type='table' AND name='event_reports'"
    ).fetchone()
    if schema_row and "under_review" in (schema_row["sql"] or ""):
      report_constraint_ok = True
  except Exception:
    pass

  if not report_constraint_ok:
    # Recreate tabel dengan constraint baru mengikuti pola migrasi events.
    conn.commit()  # Ensure no pending transaction before changing pragmas
    conn.execute("PRAGMA foreign_keys = OFF")
    conn.execute("BEGIN TRANSACTION")
    try:
      conn.execute("ALTER TABLE event_reports RENAME TO event_reports_legacy")
      conn.execute(
        """
        CREATE TABLE event_reports (
          id TEXT PRIMARY KEY,
          event_id TEXT NOT NULL,
          user_id TEXT NOT NULL,
          participants INTEGER NOT NULL,
          checklist_json TEXT NOT NULL,
          outcome_tags_json TEXT NOT NULL,
          photo_url TEXT,
          status TEXT NOT NULL CHECK(status IN ('pending','under_review','verified','rejected')),
          points_awarded INTEGER NOT NULL DEFAULT 0,
          verified_by_user_id TEXT,
          verified_at TEXT,
          reject_reason TEXT,
          created_at TEXT NOT NULL,
          updated_at TEXT NOT NULL,
          FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
          FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        """
      )
      legacy_report_cols = {row["name"] for row in conn.execute("PRAGMA table_info(event_reports_legacy)").fetchall()}
      reject_reason_expr = "reject_reason" if "reject_reason" in legacy_report_cols else "NULL"
      conn.execute(
        f"""
        INSERT INTO event_reports(
          id, event_id, user_id, participants, checklist_json, outcome_tags_json,
          photo_url, status, points_awarded, verified_by_user_id, verified_at,
          reject_reason, created_at, updated_at
        )
        SELECT
          id, event_id, user_id, participants, checklist_json, outcome_tags_json,
          photo_url, status, points_awarded, verified_by_user_id, verified_at,
          {reject_reason_expr}, created_at, updated_at
        FROM event_reports_legacy
        """
      )
      conn.execute("DROP TABLE event_reports_legacy")

      fk_violations = conn.execute("PRAGMA foreign_key_check(event_reports)").fetchall()
      if fk_violations:
        raise ValueError(f"Foreign key constraint failed after migration: {fk_violations}")

      conn.commit()
    except Exception:
      conn.rollback()
      raise
    finally:
      conn.execute("PRAGMA foreign_keys = ON")

  event_cols = conn.execute("PRAGMA table_info(events)").fetchall()
  names = {row["name"] for row in event_cols}
  kel_notnull = 1
  for row in event_cols:
    if row["name"] == "kelurahan_id":
      kel_notnull = int(row["notnull"])
      break
  needs_event_migration = (
    "scope_type" not in names or
    "kecamatan_id" not in names or
    kel_notnull == 1
  )
  if not needs_event_migration:
    return

  execute(conn, "ALTER TABLE events RENAME TO events_legacy")
  execute(
    conn,
    """
    CREATE TABLE events (
      id TEXT PRIMARY KEY,
      title TEXT NOT NULL,
      description TEXT,
      pillar INTEGER NOT NULL,
      event_date TEXT NOT NULL,
      event_time TEXT,
      location TEXT,
      quota INTEGER NOT NULL DEFAULT 0,
      scope_type TEXT NOT NULL CHECK(scope_type IN ('kelurahan','kecamatan')),
      kecamatan_id INTEGER NOT NULL,
      kelurahan_id INTEGER,
      created_by_user_id TEXT NOT NULL,
      status TEXT NOT NULL CHECK(status IN ('draft','approved','published','completed')),
      output_summary TEXT,
      published_at TEXT,
      completed_at TEXT,
      completed_by_user_id TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      FOREIGN KEY (kecamatan_id) REFERENCES kecamatan(id),
      FOREIGN KEY (kelurahan_id) REFERENCES kelurahan(id),
      FOREIGN KEY (created_by_user_id) REFERENCES users(id)
    )
    """,
  )
  legacy_cols = {row["name"] for row in conn.execute("PRAGMA table_info(events_legacy)").fetchall()}
  if "kecamatan_id" in legacy_cols:
    kec_expr = "COALESCE(events_legacy.kecamatan_id, (SELECT kecamatan_id FROM kelurahan WHERE id = events_legacy.kelurahan_id))"
  else:
    kec_expr = "(SELECT kecamatan_id FROM kelurahan WHERE id = events_legacy.kelurahan_id)"
  execute(
    conn,
    f"""
    INSERT INTO events(
      id, title, description, pillar, event_date, event_time, location, quota,
      scope_type, kecamatan_id, kelurahan_id, created_by_user_id, status,
      output_summary, published_at, completed_at, completed_by_user_id, created_at, updated_at
    )
    SELECT
      events_legacy.id,
      events_legacy.title,
      events_legacy.description,
      events_legacy.pillar,
      events_legacy.event_date,
      events_legacy.event_time,
      events_legacy.location,
      events_legacy.quota,
      'kelurahan',
      {kec_expr},
      events_legacy.kelurahan_id,
      events_legacy.created_by_user_id,
      CASE WHEN events_legacy.status = 'rejected' THEN 'draft' ELSE events_legacy.status END,
      events_legacy.output_summary,
      events_legacy.published_at,
      events_legacy.completed_at,
      events_legacy.completed_by_user_id,
      events_legacy.created_at,
      events_legacy.updated_at
    FROM events_legacy
    """,
  )
  execute(conn, "DROP TABLE events_legacy")


def seed_roles(conn):
  roles = [
    ("user", "Relawan"),
    ("ksh", "Verified KSH"),
    ("moderator_t1", "Moderator Tier 1"),
    ("moderator_t2", "Moderator Tier 2"),
    ("moderator_t3", "Moderator Tier 3"),
    ("admin", "Administrator"),
  ]
  for code, name in roles:
    execute(conn, "INSERT OR IGNORE INTO roles(code, name) VALUES(?, ?)", (code, name))


def seed_geography(conn):
  # Keep DB in-sync with src/data/geographicData.ts by code (not by existing names).
  # This repairs legacy demo DBs where kelurahan names/kodepos mappings were shifted.
  # IMPORTANT: do not recreate rows to preserve foreign-key references from users/events.
  parsed = parse_geo_data()
  valid_kel_codes = set()
  for kec in parsed:
    execute(conn, "INSERT OR IGNORE INTO kecamatan(code, name) VALUES(?, ?)", (kec["kode"], kec["nama"]))
    execute(conn, "UPDATE kecamatan SET name = ? WHERE code = ?", (kec["nama"], kec["kode"]))
    kec_id = conn.execute("SELECT id FROM kecamatan WHERE code = ?", (kec["kode"],)).fetchone()["id"]

    for kel in kec["kelurahan"]:
      valid_kel_codes.add(kel["kode"])
      execute(
        conn,
        "INSERT OR IGNORE INTO kelurahan(code, kecamatan_id, name) VALUES(?, ?, ?)",
        (kel["kode"], kec_id, kel["nama"]),
      )
      execute(
        conn,
        "UPDATE kelurahan SET name = ?, kecamatan_id = ? WHERE code = ?",
        (kel["nama"], kec_id, kel["kode"]),
      )
      kel_id = conn.execute("SELECT id FROM kelurahan WHERE code = ?", (kel["kode"],)).fetchone()["id"]

      # Replace mapping for this kelurahan with exact mapping from geographicData.ts.
      execute(conn, "DELETE FROM kampung_mapping WHERE kelurahan_id = ?", (kel_id,))
      for code in kel["kodepos"]:
        execute(conn, "INSERT OR IGNORE INTO postal_codes(code) VALUES(?)", (code,))
        p_id = conn.execute("SELECT id FROM postal_codes WHERE code = ?", (code,)).fetchone()["id"]
        execute(conn, "INSERT OR IGNORE INTO kampung_mapping(kelurahan_id, postal_code_id) VALUES(?, ?)", (kel_id, p_id))

      execute(conn, "INSERT OR IGNORE INTO xp_kelurahan(kelurahan_id, total_xp, updated_at) VALUES(?, 0, ?)", (kel_id, utc_now_iso()))
      for pillar in (1, 2, 3, 4):
        execute(
          conn,
          "INSERT OR IGNORE INTO xp_pillar(kelurahan_id, pillar, xp, updated_at) VALUES(?, ?, 0, ?)",
          (kel_id, pillar, utc_now_iso()),
        )

  # Remove stale postcode links from deprecated kelurahan rows so `/kodepos/*`
  # always follows canonical mapping from geographicData.ts.
  if valid_kel_codes:
    placeholders = ",".join(["?"] * len(valid_kel_codes))
    execute(
      conn,
      f"""
      DELETE FROM kampung_mapping
      WHERE kelurahan_id IN (
        SELECT id FROM kelurahan WHERE code NOT IN ({placeholders})
      )
      """,
      tuple(sorted(valid_kel_codes)),
    )


def insert_user(conn, name, email, password, role_code, *, is_ksh=0, tier=None, tier2_badge=None, kelurahan_name=None, sync_existing=False):
  existing = conn.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
  if existing and not sync_existing:
    return existing["id"]
  kel = None
  if kelurahan_name:
    kel = conn.execute(
      """
      SELECT kelurahan.id AS id, kecamatan.id AS kec_id
      FROM kelurahan JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
      WHERE kelurahan.name = ? LIMIT 1
      """,
      (kelurahan_name,),
    ).fetchone()
  now = utc_now_iso()
  if existing:
    execute(
      conn,
      """
      UPDATE users
      SET name = ?, password_hash = ?, role_code = ?, is_ksh = ?, moderator_tier = ?, tier2_badge = ?,
          kelurahan_id = ?, kecamatan_id = ?, updated_at = ?
      WHERE id = ?
      """,
      (
        name,
        hash_password(password),
        role_code,
        1 if is_ksh else 0,
        tier,
        tier2_badge,
        kel["id"] if kel else None,
        kel["kec_id"] if kel else None,
        now,
        existing["id"],
      ),
    )
    return existing["id"]

  user_id = str(uuid.uuid4())
  execute(
    conn,
    """
    INSERT INTO users(
      id, name, email, password_hash, role_code, is_ksh, moderator_tier,
      tier2_badge, kelurahan_id, kecamatan_id, created_at, updated_at
    )
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
      user_id,
      name,
      email,
      hash_password(password),
      role_code,
      1 if is_ksh else 0,
      tier,
      tier2_badge,
      kel["id"] if kel else None,
      kel["kec_id"] if kel else None,
      now,
      now,
    ),
  )
  return user_id


def seed_demo(conn):
  admin_seed_password = str(os.environ.get("SIMRP_SEED_ADMIN_PASSWORD", "")).strip()
  if not admin_seed_password:
    if IS_PRODUCTION:
      raise RuntimeError("SIMRP_SEED_ADMIN_PASSWORD is required when SIMRP_ENABLE_DEMO_SEED=true in production")
    admin_seed_password = generate_runtime_secret()
    record_dev_credential("Seed admin account", "email=admin@simrp.local", "SIMRP_SEED_ADMIN_PASSWORD", admin_seed_password)
  insert_user(conn, "Administrator", "admin@simrp.local", admin_seed_password, "admin", kelurahan_name="Keputih", sync_existing=True)
  insert_user(conn, "Andi Relawan", "relawan.demo@simrp.app", DEMO_PASSWORD, "user", kelurahan_name="Bulak", sync_existing=True)
  insert_user(conn, "Nia Relawan", "relawan2.demo@simrp.app", DEMO_PASSWORD, "user", kelurahan_name="Keputih", sync_existing=True)
  insert_user(conn, "Budi Relawan", "relawan3.demo@simrp.app", DEMO_PASSWORD, "user", kelurahan_name="Wonorejo", sync_existing=True)
  insert_user(conn, "Kak Esa", "ksh.demo@simrp.app", DEMO_PASSWORD, "ksh", is_ksh=1, kelurahan_name="Keputih", sync_existing=True)
  insert_user(conn, "Pak Raka ASN", "moderator1.demo@simrp.app", DEMO_PASSWORD, "moderator_t1", tier=1, kelurahan_name="Keputih", sync_existing=True)
  insert_user(conn, "Bu Sinta Lurah", "moderator2.demo@simrp.app", DEMO_PASSWORD, "moderator_t2", tier=2, tier2_badge="lurah", kelurahan_name="Keputih", sync_existing=True)
  insert_user(conn, "Pak Dimas Camat", "moderator2.camat@simrp.app", DEMO_PASSWORD, "moderator_t2", tier=2, tier2_badge="camat", kelurahan_name="Keputih", sync_existing=True)
  insert_user(conn, "Pak Arif", "moderator3.demo@simrp.app", DEMO_PASSWORD, "moderator_t3", tier=3, kelurahan_name="Keputih", sync_existing=True)
  execute(
    conn,
    "UPDATE users SET tier2_badge = 'lurah' WHERE role_code = 'moderator_t2' AND (tier2_badge IS NULL OR tier2_badge = '')",
  )

  creator = conn.execute("SELECT id FROM users WHERE role_code = 'moderator_t1' LIMIT 1").fetchone()
  keputih = conn.execute("SELECT id FROM kelurahan WHERE name = 'Keputih' LIMIT 1").fetchone()
  bulak = conn.execute("SELECT id FROM kelurahan WHERE name = 'Bulak' LIMIT 1").fetchone()
  wonorejo = conn.execute("SELECT id FROM kelurahan WHERE name = 'Wonorejo' LIMIT 1").fetchone()
  if not creator or not keputih or not bulak or not wonorejo:
    return
  keputih_kec = conn.execute("SELECT kecamatan_id FROM kelurahan WHERE id = ?", (keputih["id"],)).fetchone()["kecamatan_id"]
  wonorejo_kec = conn.execute("SELECT kecamatan_id FROM kelurahan WHERE id = ?", (wonorejo["id"],)).fetchone()["kecamatan_id"]
  bulak_kec = conn.execute("SELECT kecamatan_id FROM kelurahan WHERE id = ?", (bulak["id"],)).fetchone()["kecamatan_id"]
  events = [
    ("event-seed-1", "Aksi Bersih Taman Kampung", "Pembersihan area publik.", 1, "2026-02-20", "07:00", "Balai RW Keputih", 40, "kelurahan", keputih_kec, keputih["id"], "published"),
    ("event-seed-2", "Pelatihan UMKM Digital", "Pendampingan UMKM kampung.", 2, "2026-02-22", "13:00", "Aula Kelurahan", 30, "kelurahan", keputih_kec, keputih["id"], "published"),
    ("event-seed-3", "Forum Guyub Warga", "Forum sosial antar warga.", 3, "2026-02-25", "19:00", "Pendopo Wonorejo", 50, "kecamatan", wonorejo_kec, None, "published"),
    ("event-seed-4", "Festival Seni Kampung", "Kegiatan budaya lokal.", 4, "2026-02-27", "18:00", "Lapangan Bulak", 60, "kelurahan", bulak_kec, bulak["id"], "draft"),
  ]
  for event in events:
    execute(
      conn,
      """
      INSERT OR IGNORE INTO events(
        id, title, description, pillar, event_date, event_time, location, quota,
        scope_type, kecamatan_id, kelurahan_id, created_by_user_id, status, created_at, updated_at, published_at
      )
      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
      """,
      (
        event[0], event[1], event[2], event[3], event[4], event[5], event[6], event[7],
        event[8], event[9], event[10], creator["id"], event[11], utc_now_iso(), utc_now_iso(), utc_now_iso() if event[11] == "published" else None
      ),
    )

  requests = [
    (
      "collab-seed-1",
      "Komunitas Hijau Surabaya",
      "Rina Putri",
      "rina@hijausby.id",
      "peralatan",
      "Dukungan alat kebersihan untuk 3 kegiatan lingkungan di kelurahan.",
      "pending",
    ),
    (
      "collab-seed-2",
      "PT Sejahtera Pangan",
      "Dedi Saputra",
      "dedi@sejahterapangan.co.id",
      "konsumsi",
      "Penyediaan konsumsi relawan pada kegiatan kemasyarakatan bulanan.",
      "pending",
    ),
  ]
  for req in requests:
    execute(
      conn,
      """
      INSERT OR IGNORE INTO collaboration_requests(
        id, organization_name, pic_name, email, support_type, support_description,
        status, reviewed_by_user_id, reviewed_at, created_at, updated_at
      )
      VALUES(?, ?, ?, ?, ?, ?, ?, NULL, NULL, ?, ?)
      """,
      (req[0], req[1], req[2], req[3], req[4], req[5], req[6], utc_now_iso(), utc_now_iso()),
    )

  vouchers = [
    ("voucher-10000", "Voucher Rp 10.000", "Voucher demo SIMRP nominal Rp 10.000", 100, 50, 1),
    ("voucher-25000", "Voucher Rp 25.000", "Voucher demo SIMRP nominal Rp 25.000", 200, 20, 1),
  ]
  for voucher in vouchers:
    execute(
      conn,
      """
      INSERT OR IGNORE INTO voucher_catalog(id, name, description, xp_cost, stock, is_active, created_at)
      VALUES(?, ?, ?, ?, ?, ?, ?)
      """,
      (voucher[0], voucher[1], voucher[2], voucher[3], voucher[4], voucher[5], utc_now_iso()),
    )


def cleanup_adjustments(conn):
  now = utc_now_iso()
  rows = conn.execute("SELECT * FROM temporary_adjustments WHERE expires_at <= ?", (now,)).fetchall()
  for row in rows:
    if row["adjustment_type"] == "points":
      value = json.loads(row["value_json"])
      execute(conn, "UPDATE users SET points = points - ? WHERE id = ?", (int(value.get("points", 0)), row["user_id"]))
    if row["adjustment_type"] == "badge":
      value = json.loads(row["value_json"])
      user = conn.execute("SELECT badges_json FROM users WHERE id = ?", (row["user_id"],)).fetchone()
      badges = json.loads(user["badges_json"] or "[]")
      badge_id = value.get("badgeId")
      badges = [item for item in badges if item.get("id") != badge_id]
      execute(conn, "UPDATE users SET badges_json = ? WHERE id = ?", (json.dumps(badges), row["user_id"]))
  execute(conn, "DELETE FROM temporary_adjustments WHERE expires_at <= ?", (now,))


def get_user_payload(conn, user_row):
  kel = None
  kampung = None
  if user_row["kelurahan_id"]:
    kel = conn.execute(
      """
      SELECT kelurahan.id AS id, kelurahan.name AS kel_name, kecamatan.name AS kec_name
      FROM kelurahan JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
      WHERE kelurahan.id = ?
      """,
      (user_row["kelurahan_id"],),
    ).fetchone()
    total = conn.execute("SELECT total_xp FROM xp_kelurahan WHERE kelurahan_id = ?", (kel["id"],)).fetchone()
    volunteers = conn.execute(
      "SELECT COUNT(*) AS c FROM users WHERE kelurahan_id = ? AND role_code IN ('user','ksh')",
      (kel["id"],),
    ).fetchone()["c"]
    kampung = {
      "id": kel["id"],
      "name": kel["kel_name"],
      "kecamatan": kel["kec_name"],
      "xp": int(total["total_xp"]) if total else 0,
      "volunteers": int(volunteers),
    }

  pending = conn.execute(
    """
    SELECT COUNT(*) AS c
    FROM event_participation ep
    JOIN events e ON e.id = ep.event_id
    WHERE ep.user_id = ? AND ep.status = 'attended' AND ep.checklist_done = 0 AND e.status = 'completed'
    """,
    (user_row["id"],),
  ).fetchone()["c"]

  return {
    "id": user_row["id"],
    "name": user_row["name"],
    "email": user_row["email"],
    "role": "admin" if user_row["role_code"] == "admin" else ("moderator" if str(user_row["role_code"]).startswith("moderator_t") else "user"),
    "roleCode": user_row["role_code"],
    "isKsh": bool(user_row["is_ksh"]),
    "moderatorTier": user_row["moderator_tier"],
    "tier2Badge": user_row["tier2_badge"],
    "kelurahan": kel["kel_name"] if kel else None,
    "kecamatan": kel["kec_name"] if kel else None,
    "kampungId": kel["id"] if kel else None,
    "kampung": kampung,
    "points": int(user_row["points"]),
    "badges": json.loads(user_row["badges_json"] or "[]"),
    "hasPendingReport": bool(pending),
    "developerNote": "Definition of Kampung may shift in future (RW vs Kelurahan). Logic must stay flexible.",
  }


def can_create_event(user):
  return user["role_code"] in ("moderator_t1", "admin")


def can_approve_event(user):
  return user["role_code"] in ("moderator_t2", "admin")


def can_verify_report(user):
  return user["role_code"] in ("moderator_t2", "admin")


def auth_dependencies():
  return {
    "API_PREFIX": API_PREFIX,
    "ADMIN_LOGIN_PASSWORD": ADMIN_LOGIN_PASSWORD,
    "ADMIN_LOGIN_USERNAME": ADMIN_LOGIN_USERNAME,
    "IS_PRODUCTION": IS_PRODUCTION,
    "RATE_LIMIT_AUTH_MAX": RATE_LIMIT_AUTH_MAX,
    "RATE_LIMIT_WINDOW_SECONDS": RATE_LIMIT_WINDOW_SECONDS,
    "bounded_text": bounded_text,
    "create_session": create_session,
    "execute": execute,
    "get_user_payload": get_user_payload,
    "hash_password": hash_password,
    "rate_limited": rate_limited,
    "user_from_token": user_from_token,
    "utc_now_iso": utc_now_iso,
    "valid_email": valid_email,
    "valid_password": valid_password,
    "verify_password": verify_password,
    "write_json": write_json,
  }


def events_dependencies():
  return {
    "API_PREFIX": API_PREFIX,
    "bounded_text": bounded_text,
    "can_approve_event": can_approve_event,
    "can_create_event": can_create_event,
    "create_notification": create_notification,
    "execute": execute,
    "log_audit": log_audit,
    "user_from_token": user_from_token,
    "utc_now_iso": utc_now_iso,
    "write_json": write_json,
  }


def reports_dependencies():
  return {
    "API_PREFIX": API_PREFIX,
    "apply_xp": apply_xp,
    "bounded_text": bounded_text,
    "can_verify_report": can_verify_report,
    "create_notification": create_notification,
    "execute": execute,
    "log_audit": log_audit,
    "user_from_token": user_from_token,
    "utc_now_iso": utc_now_iso,
    "write_json": write_json,
  }


def collaboration_dependencies():
  return {
    "API_PREFIX": API_PREFIX,
    "bounded_text": bounded_text,
    "create_notification": create_notification,
    "execute": execute,
    "log_audit": log_audit,
    "user_from_token": user_from_token,
    "utc_now_iso": utc_now_iso,
    "valid_email": valid_email,
    "write_json": write_json,
  }


def geographic_dependencies():
  return {
    "API_PREFIX": API_PREFIX,
    "get_geo_stats": get_geo_stats,
    "user_from_token": user_from_token,
    "write_json": write_json,
  }


def admin_dependencies():
  return {
    "API_PREFIX": API_PREFIX,
    "bounded_text": bounded_text,
    "execute": execute,
    "log_audit": log_audit,
    "user_from_token": user_from_token,
    "utc_now_iso": utc_now_iso,
    "write_json": write_json,
  }


def notifications_dependencies():
  return {
    "API_PREFIX": API_PREFIX,
    "execute": execute,
    "user_from_token": user_from_token,
    "write_json": write_json,
  }


def certificates_dependencies():
  return {
    "API_PREFIX": API_PREFIX,
    "user_from_token": user_from_token,
    "write_json": write_json,
  }


def rewards_dependencies():
  return {
    "API_PREFIX": API_PREFIX,
    "bounded_text": bounded_text,
    "create_notification": create_notification,
    "execute": execute,
    "log_audit": log_audit,
    "user_from_token": user_from_token,
    "utc_now_iso": utc_now_iso,
    "write_json": write_json,
  }


def users_dependencies():
  return {
    "API_PREFIX": API_PREFIX,
    "bounded_text": bounded_text,
    "execute": execute,
    "get_user_payload": get_user_payload,
    "user_from_token": user_from_token,
    "utc_now_iso": utc_now_iso,
    "write_json": write_json,
  }


def apply_xp(conn, event_row, participants):
  kelurahan_id = event_row["kelurahan_id"]
  pillar = int(event_row["pillar"])
  base = 20 + (participants * 2)
  rows = conn.execute("SELECT pillar, xp FROM xp_pillar WHERE kelurahan_id = ?", (kelurahan_id,)).fetchall()
  pillar_map = {int(r["pillar"]): int(r["xp"]) for r in rows}
  total = sum(pillar_map.values())
  avg = total / 4 if total else 0
  p_value = pillar_map.get(pillar, 0)
  multiplier = 1.0
  if total > 0 and p_value > avg * 1.2:
    multiplier = 0.7
  elif total > 0 and p_value < avg * 0.8:
    multiplier = 1.3
  gained = int(round(base * multiplier))
  now = utc_now_iso()
  execute(
    conn,
    "UPDATE xp_pillar SET xp = xp + ?, updated_at = ? WHERE kelurahan_id = ? AND pillar = ?",
    (gained, now, kelurahan_id, pillar),
  )
  execute(
    conn,
    "UPDATE xp_kelurahan SET total_xp = total_xp + ?, updated_at = ? WHERE kelurahan_id = ?",
    (gained, now, kelurahan_id),
  )
  return gained


class Handler(BaseHTTPRequestHandler):
  def do_OPTIONS(self):
    write_json(self, 200, {"ok": True})

  def do_GET(self):
    conn = connect_db()
    cleanup_adjustments(conn)
    try:
      parsed = urlparse(self.path)
      path = parsed.path
      query = parse_qs(parsed.query)

      if auth_api.handle_get(self, conn, path, auth_dependencies()):
        return

      if events_api.handle_get(self, conn, path, query, events_dependencies()):
        return

      if reports_api.handle_get(self, conn, path, query, reports_dependencies()):
        return

      if collaboration_api.handle_get(self, conn, path, query, collaboration_dependencies()):
        return

      if geographic_api.handle_get(self, conn, path, geographic_dependencies()):
        return

      if admin_api.handle_get(self, conn, path, admin_dependencies()):
        return

      if notifications_api.handle_get(self, conn, path, notifications_dependencies()):
        return

      if certificates_api.handle_get(self, conn, path, certificates_dependencies()):
        return

      if rewards_api.handle_get(self, conn, path, rewards_dependencies()):
        return

      if users_api.handle_get(self, conn, path, query, users_dependencies()):
        return

      return write_json(self, 404, {"error": "Not found"})
    except ValueError as exc:
      return write_json(self, 400, {"error": str(exc)})
    except Exception as exc:
      print(f"[GET] error path={self.path}: {exc}")
      if IS_PRODUCTION:
        return write_json(self, 500, {"error": "Internal server error"})
      return write_json(self, 500, {"error": str(exc)})
    finally:
      conn.commit()
      conn.close()

  def do_POST(self):
    conn = connect_db()
    cleanup_adjustments(conn)
    try:
      path = urlparse(self.path).path
      if rate_limited(self, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS):
        return write_json(self, 429, {"error": "Terlalu banyak permintaan, coba lagi sebentar"})
      body = parse_json_body(self)

      if auth_api.handle_post(self, conn, path, body, auth_dependencies()):
        return

      if events_api.handle_post(self, conn, path, body, events_dependencies()):
        return

      if reports_api.handle_post(self, conn, path, body, reports_dependencies()):
        return

      if collaboration_api.handle_post(self, conn, path, body, collaboration_dependencies()):
        return

      if admin_api.handle_post(self, conn, path, body, admin_dependencies()):
        return

      if notifications_api.handle_post(self, conn, path, body, notifications_dependencies()):
        return

      if rewards_api.handle_post(self, conn, path, body, rewards_dependencies()):
        return

      actor = user_from_token(conn, self.headers.get("Authorization"))
      if not actor:
        return write_json(self, 401, {"error": "Unauthorized"})

      if users_api.handle_post(self, conn, path, body, users_dependencies()):
        return

      return write_json(self, 404, {"error": "Not found"})
    except ValueError as exc:
      return write_json(self, 400, {"error": str(exc)})
    except Exception as exc:
      print(f"[POST] error path={self.path}: {exc}")
      if IS_PRODUCTION:
        return write_json(self, 500, {"error": "Internal server error"})
      return write_json(self, 500, {"error": str(exc)})
    finally:
      conn.commit()
      conn.close()

  def do_DELETE(self):
    conn = connect_db()
    try:
      path = urlparse(self.path).path
      if rate_limited(self, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS):
        return write_json(self, 429, {"error": "Terlalu banyak permintaan, coba lagi sebentar"})
      if auth_api.handle_delete(self, conn, path, auth_dependencies()):
        return
      actor = user_from_token(conn, self.headers.get("Authorization"))
      if not actor:
        return write_json(self, 401, {"error": "Unauthorized"})
      return write_json(self, 404, {"error": "Not found"})
    except Exception as exc:
      print(f"[DELETE] error path={self.path}: {exc}")
      if IS_PRODUCTION:
        return write_json(self, 500, {"error": "Internal server error"})
      return write_json(self, 500, {"error": str(exc)})
    finally:
      conn.commit()
      conn.close()

  def do_PUT(self):
    conn = connect_db()
    try:
      path = urlparse(self.path).path
      if rate_limited(self, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS):
        return write_json(self, 429, {"error": "Terlalu banyak permintaan, coba lagi sebentar"})
      actor = user_from_token(conn, self.headers.get("Authorization"))
      if not actor:
        return write_json(self, 401, {"error": "Unauthorized"})

      body = parse_json_body(self)

      if events_api.handle_put(self, conn, path, body, events_dependencies()):
        return

      if users_api.handle_put(self, conn, path, body, actor, users_dependencies()):
        return

      return write_json(self, 404, {"error": "Not found"})
    except ValueError as exc:
      return write_json(self, 400, {"error": str(exc)})
    except Exception as exc:
      print(f"[PUT] error path={self.path}: {exc}")
      if IS_PRODUCTION:
        return write_json(self, 500, {"error": "Internal server error"})
      return write_json(self, 500, {"error": str(exc)})
    finally:
      conn.commit()
      conn.close()


def main():
  init_schema()
  write_dev_credentials_file()
  display_host = "127.0.0.1" if HOST in ("0.0.0.0", "::") else HOST
  print(f"SIMRP API: http://{display_host}:{PORT}{API_PREFIX}")
  print(f"Bind: {HOST}:{PORT}")
  print(f"DB: {DB_PATH}")
  print(f"Mode: {APP_ENV} | demo-seed={'on' if ENABLE_DEMO_SEED else 'off'}")
  server = ThreadingHTTPServer((HOST, PORT), Handler)
  server.serve_forever()


if __name__ == "__main__":
  main()
