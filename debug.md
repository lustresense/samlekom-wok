# 🔍 SIMRP AUDIT & IMPLEMENTATION PLAN

> **Last Updated:** 2026-05-02  
> **Author:** AI Audit (Antigravity)  
> **Purpose:** Gap analysis D26–D100 + actionable implementation plan untuk AI berikutnya.  
> **Status:** AUDIT COMPLETE ✅ — IMPLEMENTATION COMPLETE ✅

---

## 🚨 INSTRUKSI UNTUK AI BERIKUTNYA — BACA INI DULU

1. **Backend runtime = `server/main.py`** (1911 baris, monolith). File `server/api/*.py` dan `server/core/*.py` adalah **DEAD CODE** — tidak di-import oleh runtime. Jangan edit file itu kecuali memang mau refactor arsitektur.
2. **Frontend = SPA di `src/app/App.tsx`** — routing via React state, BUKAN React Router.
3. **Database = SQLite** di `database/runtime/database.db`, schema di `init_schema()` `main.py:296-554`.
4. **Run**: `npm run dev` — jalanin Vite FE + Python server via `scripts/dev-local.mjs`.
5. **Jangan refactor arsitektur** kecuali user minta. Tambah fitur di `main.py` inline handler.
6. **Setelah implement**, update status di bagian bawah file ini.

---

## 📐 ARSITEKTUR SAAT INI

```
server/main.py          ← SATU-SATUNYA backend runtime (BaseHTTPRequestHandler + SQLite)
  - init_schema()       ← 12 tabel: roles, users, sessions, events, event_participation,
                          event_reports, xp_kelurahan, xp_pillar, audit_logs,
                          collaboration_requests, temporary_adjustments, postal_codes, dll
  - Handler.do_GET()    ← GET endpoints inline
  - Handler.do_POST()   ← POST endpoints inline
  - Handler.do_PUT()    ← PUT /users/:id
  - Handler.do_DELETE() ← DELETE /auth/logout
  - apply_xp()          ← XP formula: base=20+(n*2), multiplier 0.7-1.3
  - rate_limited()      ← Per-IP rate limiting
  - add_common_headers()← Security headers (CORS, CSP, HSTS, X-Frame)

src/app/App.tsx          ← SPA router, state: Page = landing|login|register|...
src/app/components/      ← Semua halaman FE
src/lib/api.ts           ← Fetch wrapper (apiGet, apiPost, apiPut, apiPublicPost, apiPublicGet)
src/types/index.ts       ← TypeScript types (sebagian outdated)
```

---

## ✅ YANG SUDAH IMPLEMENTED (Sudah Bener, Jangan Ganggu)

### Auth (M2)
- ✅ Signup: email validation, password 8 char + alpha+digit, kelurahan lookup
- ✅ Login: email/password, session token, rate limit 10/min
- ✅ Admin login: HMAC compare, separate endpoint
- ✅ Session: create_session(), user_from_token(), /auth/me, /auth/logout
- ✅ RBAC: can_create_event(), can_approve_event(), can_verify_report()
- ✅ FE: LoginPage, RegisterPage, AdminLoginPage, route guard, role-based view switching

### Events (M3) — Partial
- ✅ Create event draft: Mod T1/Admin, title/pillar/scope/quota/date/time/location
- ✅ Approve/reject: Mod T2/Admin, scope validation (lurah hanya kelurahan, camat hanya kecamatan)
- ✅ FE: Create form (ModeratorDashboard), draft table, approve/reject buttons, status badges

### Participation (M4) — Partial
- ✅ Join event: cek published, kuota, pending report block
- ✅ Complete event: KSH only, scope check, output summary required, batch attendance update
- ✅ FE: Join button (EventList), "Tandai Selesai" (UserDashboard KSH mode)

### Reporting (M5) — Partial
- ✅ Submit report: 2-step wizard (bukti + dampak), guard conditions (event completed, user participated)
- ✅ Report list: GET /reports with userId filter
- ✅ FE: ReportingWizard (2-step), photo preview, outcome tags

### Verification (M6) — Partial
- ✅ Verify endpoint: approve → apply_xp + user points +5, reject
- ✅ XP formula: apply_xp() with pillar variance multiplier (0.7-1.3)
- ✅ FE: ModeratorDashboard verify tab (Mod T2)

### Gamification (M7) — Partial
- ✅ Leaderboard: `/landing/leaderboard` (public, top 7), `/kampung` (auth, top 100)
- ✅ xp_kelurahan + xp_pillar tables, updated on report verify
- ✅ FE: LeaderboardSection (landing), leaderboards tab (UserDashboard)

### Mitra (M9)
- ✅ Public form: POST /collaboration-requests (tanpa auth), scope kota/kecamatan/kelurahan
- ✅ Review: Mod T2/Admin approve/reject
- ✅ FE: CollaborationPage (public), ModeratorDashboard collab tab

### Security (M10) — Partial
- ✅ Rate limiting: auth 10/min, mutation 120/min per IP
- ✅ Input validation: bounded_text(), email regex, password rules
- ✅ Security headers: X-Content-Type-Options, X-Frame-Options, HSTS, CSP, Referrer-Policy
- ✅ CORS: allow-list based, production whitelist

### Docs
- ✅ Architecture docs: 5 files di `docs/architecture/`
- ✅ Security docs: 3 files di `docs/security/`
- ✅ Logbook: 8 files di `docs/logbook/`
- ✅ README, DEMO_ACCOUNTS, CONTRIBUTOR_SETUP_GUIDE

---

## ❌ IMPLEMENTATION PLAN — Yang Harus Dikerjakan

### PRIORITY 1 — Backend Fixes (Kritis, Endpoint Existing yang Kurang)

#### 1.1 Audit Trail — INSERT ke audit_logs
**File:** `server/main.py`  
**Problem:** Tabel `audit_logs` sudah ada (line 487-496) tapi **TIDAK PERNAH ada INSERT**. Nol baris.  
**Action:**  
Tambah helper function `log_audit(conn, actor_id, action, entity_type, entity_id, payload)` lalu panggil di:
- `POST /reports` → action: `"report.submit"`, entity: report
- `POST /reports/:id/verify` → action: `"report.verify"` atau `"report.reject"`, entity: report
- `POST /events/:id/approval` → action: `"event.approve"` atau `"event.reject"`, entity: event
- `POST /events/:id/complete` → action: `"event.complete"`, entity: event
- `POST /collaboration-requests/:id/approval` → action: `"collab.approve"` atau `"collab.reject"`
- `POST /admin/assign-role`, `/admin/remove-role`, `/admin/add-temporary-points`, `/admin/add-temporary-badge`

**Contoh implementation:**
```python
def log_audit(conn, actor_id, action, entity_type, entity_id, payload=None):
    execute(conn, """
        INSERT INTO audit_logs(actor_user_id, action, entity_type, entity_id, payload_json, created_at)
        VALUES(?, ?, ?, ?, ?, ?)
    """, (actor_id, action, entity_type, entity_id, json.dumps(payload or {}), utc_now_iso()))
```

---

#### 1.2 Reject Reason — Simpan Alasan Reject
**File:** `server/main.py`  
**Problem:** Saat reject event atau report, alasan TIDAK disimpan.  
**Action:**
1. ALTER TABLE `event_reports` ADD COLUMN `reject_reason TEXT` — tambah di `migrate_schema()` (cek kolom, kalau belum ada tambah)
2. ALTER TABLE `events` — tidak perlu kolom reject_reason karena reject event = kembalikan ke draft
3. Di handler verify report (`main.py ~line 1736`), ambil `body.get("reason", "")` dan simpan ke reject_reason
4. Di FE `ModeratorDashboard.tsx`, saat reject:
   - Tampilkan dialog/prompt untuk isi alasan
   - Kirim `{ approved: false, reason: "..." }` ke API
5. Di FE report history, tampilkan reject_reason jika status rejected

**Backend change (line ~1736-1741):**
```python
# current:
execute(conn, "UPDATE event_reports SET status = 'rejected', verified_by_user_id = ?, verified_at = ?, updated_at = ? WHERE id = ?", ...)

# change to:
reject_reason = bounded_text(body.get("reason", ""), 500)
execute(conn, "UPDATE event_reports SET status = 'rejected', reject_reason = ?, verified_by_user_id = ?, verified_at = ?, updated_at = ? WHERE id = ?",
    (reject_reason, actor["id"], now, now, report_id))
```

---

#### 1.3 Edit Draft Event — PUT /events/:id
**File:** `server/main.py` di `do_PUT()`  
**Problem:** Tidak ada endpoint untuk edit event draft. KSH/Mod harus bisa edit sebelum di-approve.  
**Action:** Tambah handler di `do_PUT()` (setelah line 1865):
```python
if path.startswith(f"{API_PREFIX}/events/") and not path.endswith("/"):
    event_id = path.split("/")[-1]
    event = conn.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
    if not event:
        return write_json(self, 404, {"error": "Event tidak ditemukan"})
    if event["status"] != "draft":
        return write_json(self, 400, {"error": "Hanya event draft yang bisa diedit"})
    if event["created_by_user_id"] != actor["id"] and actor["role_code"] != "admin":
        return write_json(self, 403, {"error": "Hanya pembuat event yang bisa edit"})
    body = parse_json_body(self)
    # Update fields...
    # (title, description, pillar, date, time, location, quota, scopeType, kecamatanId, kelurahanId)
```
**FE:** Tambah tombol "Edit" di draft event list → buka form pre-filled.

---

#### 1.4 Duplicate Report Prevention
**File:** `server/main.py`  
**Problem:** User bisa submit report berkali-kali untuk event yang sama.  
**Action:** Di handler `POST /reports` (line ~1658), tambah check:
```python
existing = conn.execute(
    "SELECT id FROM event_reports WHERE event_id = ? AND user_id = ?",
    (event_id, actor["id"])
).fetchone()
if existing:
    return write_json(self, 400, {"error": "Kamu sudah pernah mengirim laporan untuk event ini"})
```

---

### PRIORITY 2 — Modul Baru yang Belum Ada Sama Sekali

#### 2.1 Notification System
**Backend (`server/main.py`):**
1. Tambah tabel `notifications` di `init_schema()`:
```sql
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
```
2. Tambah helper `create_notification(conn, user_id, type, title, message, entity_type=None, entity_id=None)`
3. Panggil di:
   - Report verified → notif ke reporter: "Laporanmu disetujui! +X XP"
   - Report rejected → notif ke reporter: "Laporanmu ditolak: [reason]"
   - Event approved → notif ke event creator
   - Collaboration approved/rejected → notif ke submitter (kalau punya user_id)
4. Endpoint: `GET /notifications` (auth required) — return user's notifications
5. Endpoint: `POST /notifications/:id/read` — mark as read
6. Endpoint: `GET /notifications/count` — return unread count

**Frontend:**
1. Tambah notification bell icon di `FloatingNavbar` dengan badge unread count
2. Dropdown/page untuk list notifikasi
3. Polling setiap 30 detik untuk unread count

---

#### 2.2 Certificate System (Sertifikat Digital)
**Backend (`server/main.py`):**
1. Tambah tabel `certificates` di `init_schema()`:
```sql
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
```
2. Saat report di-verify (approve), otomatis buat entry certificate:
```python
cert_id = f"cert-{uuid.uuid4().hex[:12]}"
cert_hash = hashlib.sha256(f"{cert_id}:{report['user_id']}:{report['event_id']}:{now}".encode()).hexdigest()[:16]
execute(conn, "INSERT OR IGNORE INTO certificates(...) VALUES(...)")
```
3. Endpoint: `GET /certificates` (auth) — return user's certificates
4. Endpoint: `GET /certificates/:id/verify` (public) — verify certificate hash

**Frontend:**
1. Tambah tab "Sertifikat" di `UserDashboard` atau di `UserProfile`
2. List sertifikat dengan tombol "Lihat" → modal/page detail
3. Detail menampilkan: nama peserta, nama kegiatan, tanggal, hash verifikasi
4. **TIDAK perlu generate PDF** untuk MVP — cukup tampilkan data di UI

---

#### 2.3 Reward/Voucher System
**Backend (`server/main.py`):**
1. Tambah tabel:
```sql
CREATE TABLE IF NOT EXISTS voucher_catalog (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    xp_cost INTEGER NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    is_active INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL
)

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
```
2. Seed beberapa voucher demo di `seed_demo()`:
   - "Voucher Rp 10.000" — 100 XP, stok 50
   - "Voucher Rp 25.000" — 200 XP, stok 20
3. Endpoints:
   - `GET /rewards/catalog` (auth) → return catalog
   - `POST /rewards/redeem` (auth) → body: { voucherId } → cek XP cukup, kurangi XP user, buat entry, return voucher_code
4. Guard: XP cukup, stok tersedia, user punya XP di `users.points`

**Frontend:**
1. Tambah halaman/tab "Reward" di `UserDashboard`
2. Tampilkan catalog: nama, deskripsi, XP cost, stok
3. Tombol "Tukar" → dialog konfirmasi → call redeem → tampilkan kode voucher
4. Tampilkan XP user saat ini sebagai indikator

---

#### 2.4 Radar Chart Empat Pilar
**Backend (`server/main.py`):**
1. Endpoint: `GET /kampung/:id/pillars` (auth) → return 4 pillar XP data:
```python
if path.startswith(f"{API_PREFIX}/kampung/") and path.endswith("/pillars"):
    kel_id = path.split("/")[-2]
    rows = conn.execute("SELECT pillar, xp FROM xp_pillar WHERE kelurahan_id = ?", (int(kel_id),)).fetchall()
    pillars = {int(r["pillar"]): int(r["xp"]) for r in rows}
    return write_json(self, 200, {"pillars": {
        "lingkungan": pillars.get(1, 0),
        "ekonomi": pillars.get(2, 0),
        "kemasyarakatan": pillars.get(3, 0),
        "sosialBudaya": pillars.get(4, 0)
    }})
```

**Frontend:**
1. Buat komponen `PillarRadarChart.tsx` — bisa pakai library ringan seperti `recharts` (sudah ada?) atau pure SVG
2. Tampilkan di `UserDashboard` home tab, di bawah kampung card
3. Fetch data dari `/kampung/:id/pillars` saat komponen mount
4. Fallback jika data kosong: tampilkan placeholder "Belum ada data pilar"

---

### PRIORITY 3 — Polish & Completeness

#### 3.1 Attendance Checklist UI
**Problem:** Saat complete event, semua peserta otomatis ditandai hadir. Harusnya KSH bisa pilih per-peserta.  
**Backend:** Tambah endpoint `POST /events/:id/attendance` yang menerima `{ userIds: [...] }` — update hanya user tersebut jadi "attended".  
**Frontend:** Modal checklist di `UserDashboard` KSH mode — list peserta event, checkbox per-orang, submit.

#### 3.2 FE Error Pages (404, 429, 500)
**File:** `src/lib/api.ts` dan `App.tsx`
- Di `api.ts`: Sudah handle 401. Tambah handling 429 (show toast "Terlalu banyak permintaan, coba lagi nanti").
- Di `App.tsx`: Tambah fallback component jika `currentPage` tidak match — tampilkan halaman 404 sederhana.

#### 3.3 Event Status: Separate Approved & Published
**Problem:** Approve langsung set "published". Requirement: draft → approved → published.
**Action:** SKIP — ini perubahan besar yang mungkin break existing flow. Kecuali user minta, tinggalkan.

#### 3.4 Participation History Endpoint
**Backend:** Tambah `GET /users/me/participations` yang return events yang pernah diikuti user beserta status partisipasinya (registered, attended, reported).
```python
if path == f"{API_PREFIX}/users/me/participations":
    rows = conn.execute("""
        SELECT ep.*, e.title, e.event_date, e.status AS event_status
        FROM event_participation ep
        JOIN events e ON e.id = ep.event_id
        WHERE ep.user_id = ?
        ORDER BY e.event_date DESC
    """, (actor["id"],)).fetchall()
```

---

## 📁 KEY FILE LOCATIONS

| File | Lines | Purpose |
|------|-------|---------|
| `server/main.py` | 1911 | Backend runtime (SATU-SATUNYA) |
| `src/app/App.tsx` | 315 | SPA router |
| `src/app/components/UserDashboard.tsx` | 407 | Warga/KSH dashboard |
| `src/app/components/ModeratorDashboard.tsx` | 862 | Moderator dashboard |
| `src/app/components/AdminDashboard.tsx` | ~500 | Admin dashboard |
| `src/app/components/ReportingWizard.tsx` | 324 | 2-step report form |
| `src/app/components/EventList.tsx` | ~250 | Event cards + join |
| `src/app/components/CollaborationPage.tsx` | ~500 | Public mitra form |
| `src/app/components/UserProfile.tsx` | ~300 | Profile page |
| `src/lib/api.ts` | 85 | API client |
| `src/types/index.ts` | 132 | TypeScript types (sebagian outdated) |

---

## 📊 EFFORT ESTIMATE

| Task | Priority | Effort | Files Changed |
|------|----------|--------|---------------|
| 1.1 Audit Trail | P1 | Kecil | main.py |
| 1.2 Reject Reason | P1 | Kecil | main.py, ModeratorDashboard.tsx |
| 1.3 Edit Draft Event | P1 | Sedang | main.py, ModeratorDashboard.tsx |
| 1.4 Duplicate Report Check | P1 | Kecil | main.py |
| 2.1 Notification System | P2 | Besar | main.py, FloatingNavbar.tsx, App.tsx |
| 2.2 Certificate System | P2 | Sedang | main.py, UserDashboard.tsx / UserProfile.tsx |
| 2.3 Voucher/Redeem | P2 | Besar | main.py, UserDashboard.tsx (new tab/page) |
| 2.4 Radar Chart | P2 | Sedang | main.py, UserDashboard.tsx (new component) |
| 3.1 Attendance Checklist | P3 | Sedang | main.py, UserDashboard.tsx |
| 3.2 FE Error Pages | P3 | Kecil | api.ts, App.tsx |
| 3.4 Participation History | P3 | Kecil | main.py |

---

## 📝 PROGRESS TRACKING

Setiap AI yang implement, **update checklist ini:**

- [x] 1.1 Audit Trail
- [x] 1.2 Reject Reason
- [x] 1.3 Edit Draft Event
- [x] 1.4 Duplicate Report Prevention
- [x] 2.1 Notification System
- [x] 2.2 Certificate System
- [x] 2.3 Voucher/Redeem System
- [x] 2.4 Radar Chart Empat Pilar
- [x] 3.1 Attendance Checklist UI
- [x] 3.2 FE Error Pages
- [x] 3.4 Participation History Endpoint

---

## 📝 CHANGELOG

### 2026-05-02 — Demo Seed Sync + Production Readiness (Codex)
- Fixed demo account persistence by syncing/upserting demo users on startup (prevents moderator login mismatch after DB drift).
- Added env toggles:
  - `SIMRP_ENABLE_DEMO_SEED` (default on in development, off in production)
  - `SIMRP_DEMO_PASSWORD` (default `password123`)
  - `SIMRP_HOST` + `SIMRP_PORT` for VPS binding
- Enabled `seed_geography()` to keep DB mapping in sync with `src/data/geographicData.ts`.
- Updated [DEMO_ACCOUNTS.md](DEMO_ACCOUNTS.md) to match actual auth flow and env vars.
- Live auth verification (local API): moderator/login + user login OK after forced password corruption + restart (seed sync repaired).

### 2026-05-02 — CRUD Smoke Test (Codex)
- End-to-end flow OK on local API using demo accounts: create event (moderator1) → approve (moderator2/lurah) → join (relawan2) → attendance + complete (KSH) → report submit (relawan2) → verify (moderator2).
- Sample artifacts: event `event-99a4eca8d2`, report `report-fb0aeaf2b659`.

### 2026-04-24 — Validation Refresh (Codex)
- Re-validated runtime and frontend after previous implementation batch.
- Validation results:
  - `f:/codes/Figmasimrp/.venv/Scripts/python.exe -m py_compile server/main.py` passed
  - `npm run build` passed (Vite build success, dist generated)
- Status check:
  - No TypeScript/Python diagnostics reported in edited files.
  - Checklist 1.1–3.4 remains complete and consistent with code state.

### 2026-04-23 — Live File-by-File Update (Codex, completed)
- Updated `server/main.py`:
  - Added schema for `notifications`, `certificates`, `voucher_catalog`, `voucher_redemptions`
  - Added migration for `collaboration_requests.submitted_by_user_id`
  - Added backend endpoints: notifications (`GET /notifications`, `GET /notifications/count`, `POST /notifications/:id/read`), certificates (`GET /certificates`, `GET /certificates/:id/verify`), rewards (`GET /rewards/catalog`, `POST /rewards/redeem`), pillar radar (`GET /kampung/:id/pillars`), participation history (`GET /users/me/participations`), attendance (`POST /events/:id/attendance`)
  - Added notification triggers on report verify/reject, event approval, collaboration approval, reward redeem
  - Added certificate issuance on approved reports
  - Updated report submission guard to require participant status `attended`
- Updated `src/app/components/ui/_types.ts`:
  - Added optional `authToken` prop in `FloatingNavbarProps`
- Updated `src/app/components/ui/DesktopNavbar.tsx`:
  - Added notification bell, unread badge, dropdown list, mark-as-read action, and 30-second polling
- Updated `src/app/components/ui/MobileNavbar.tsx`:
  - Added notification bell, unread badge, dropdown list, mark-as-read action, and 30-second polling
  - Cleaned unused icon imports after notification UI merge
- Updated `src/lib/api.ts`:
  - Added global toast handling for HTTP `429` (rate limit)
  - Added global toast handling for server errors (`5xx`)
- Updated `src/app/App.tsx`:
  - Added explicit `not-found` route state and 404 fallback page UI
  - Unknown URL path now routes to in-app 404 screen instead of silently falling back
- Updated `src/app/components/UserDashboard.tsx`:
  - Rebuilt dashboard flow to include tabs `certificates` + `rewards`
  - Added KSH attendance checklist modal flow before event completion
  - Integrated certificate listing and reward redemption UI
  - Integrated pillar radar chart placement in Home tab
- Added `src/app/components/PillarRadarChart.tsx`:
  - New radar chart component using `recharts` for 4-pillar XP visualization
  - Fetches `/kampung/:id/pillars` with loading + empty-data fallback states
- Updated `src/app/components/ModeratorDashboard.tsx`:
  - Added draft event edit flow (prefill + PUT update)
  - Added reject reason prompt on report rejection
- Updated `src/app/components/AdminDashboard.tsx`:
  - Added reject reason prompt on report rejection
- Updated `src/app/components/UserProfile.tsx`:
  - Added reject reason display in report history
- Validation:
  - `python -m py_compile server/main.py` passed
  - `npm run build` passed
  - Re-run after final UI merge: both checks still passed
- Progress tracking:
  - All checklist items 1.1–3.4 marked complete

### 2026-04-23 — Batch A Implementation (Codex)
- Implemented audit trail helper `log_audit(...)` + inserts on report submit/verify, event approve/reject/complete, collaboration approval, and all admin temporary/role mutations
- Added `event_reports.reject_reason` migration + backend reject validation + FE reject reason prompt (Moderator/Admin) + reject reason rendering in user report history
- Added `PUT /events/:id` draft editing endpoint with validation + ownership check, and integrated draft edit UI in Moderator Tier 1
- Added duplicate report guard for same `event_id + user_id` on `POST /reports`
- Verification: `python -m py_compile server/main.py` and `npm run build` both passed

### 2026-04-23 — Initial Audit + Plan (Antigravity)
- Full codebase audit completed against D26–D100
- Identified 11 implementation gaps across 3 priority tiers
- Created detailed implementation plan with code snippets
- Every gap has: problem statement, file location, exact action steps
