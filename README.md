# SIMRP - Sistem Informasi Manajemen Rekap Partisipatif

SIMRP adalah aplikasi partisipasi warga berbasis React + Vite, Python native HTTP server, dan SQLite. Project ini dipakai untuk alur relawan/KSH, moderator, admin, kegiatan kampung, laporan kegiatan, XP/leaderboard, sertifikat, reward voucher, notifikasi, dan kolaborasi mitra.

Status saat ini: backend sudah partial modular. Banyak endpoint runtime sudah pindah ke `server/api/*`, tetapi `server/main.py` masih menjadi entrypoint utama dan masih memegang banyak logic non-route.

## Status Project Saat Ini

- Frontend: React 18 + Vite 6 + TypeScript-style TSX components.
- Backend: Python stdlib `http.server.ThreadingHTTPServer`, tanpa Flask/FastAPI/Django.
- Database: SQLite di `database/runtime/database.db` secara default.
- Runtime utama: `server/main.py`.
- Ukuran `server/main.py` saat ini sekitar 1570 baris.
- API prefix runtime: `/make-server-32aa5c5c`.
- Branch kerja lokal saat README ini diperbarui: `update`.
- Remote deploy yang relevan: `https://github.com/lustresense/samlekom-wok.git`.

## Arsitektur Ringkas

```text
server/
  main.py              Runtime utama HTTP server
  main_test.py         Copy/test backend lama
  api/
    auth.py            Auth, signup, login, admin-login, logout
    events.py          Event create/edit/approve/publish/join/attendance/complete
    reports.py         Report submit/review/verify/reject, XP, certificate trigger
    collaboration.py   Public mitra request dan approval moderator/admin
    geographic.py      Geo options, kodepos, kampung, pillar XP
    admin.py           Admin role dan temporary adjustment
    notifications.py   Notification list/count/read
    certificates.py    Certificate list/verify/download HTML
    rewards.py         Reward catalog dan voucher redeem
    users.py           Users, health, participations, landing leaderboard
    xp.py              Legacy/partial leaderboard module
    rate_limiter.py    Legacy/support rate limiter
  core/
    config.py
    database.py
    security.py

src/
  app/App.tsx
  app/components/
    UserDashboard.tsx
    ModeratorDashboard.tsx
    AdminDashboard.tsx
    ReportingWizard.tsx
    EventList.tsx
    UserProfile.tsx
    PillarRadarChart.tsx
    ui/
    landing/
  lib/api.ts
  types/index.ts
  data/
```

## Kondisi Backend

`server/main.py` masih memegang:

- konfigurasi env dan path runtime;
- koneksi SQLite dan wrapper `execute`;
- schema/init DB;
- migration;
- seed geography/demo data;
- auth/session helper;
- response/json helper;
- RBAC helper;
- audit log helper;
- notification helper;
- XP calculation;
- geography parser dari `src/data/geographicData.ts`;
- dependency dictionary untuk modul API;
- lifecycle `BaseHTTPRequestHandler`.

Target refactor berikutnya adalah modularisasi backend lanjutan supaya `server/main.py` turun bertahap menjadi entrypoint tipis sekitar 200-300 baris.

Prioritas refactor berikutnya:

1. Extract pure helpers dari `server/main.py` ke `server/core/*`.
2. Extract schema, migration, dan seed ke `server/db/*`.
3. Extract service logic ke `server/services/*`.
4. Kurangi dependency dictionary di `server/main.py`.
5. Bersihkan duplicate/dead code setelah usage dicek dengan search.
6. Validasi final backend dengan `py_compile` dan smoke test endpoint utama.

## Fitur Aktif

- Auth user: signup, login, logout, session token.
- Admin login terpisah via credential env.
- RBAC user, KSH, moderator tier, admin.
- Event flow: draft, approval, publish, join, attendance checklist, complete.
- Report flow: submit, under review, verify/reject.
- XP kampung dan XP pillar.
- Leaderboard landing dan leaderboard kampung.
- Collaboration/mitra request dan approval.
- In-app notifications.
- Certificate record, public verify, dan HTML download untuk print/PDF.
- Reward catalog dan voucher redemption.
- Admin temporary points/badges dan role assignment.
- Backup database helper.
- Smoke test script untuk API lokal.

## API Runtime Aktual

Base URL default:

```text
http://127.0.0.1:8000/make-server-32aa5c5c
```

Endpoint utama:

| Area | Endpoint |
|---|---|
| Health | `GET /health` |
| Auth | `GET /auth/me`, `POST /auth/signup`, `POST /auth/login`, `POST /auth/admin-login`, `POST /auth/logout`, `DELETE /auth/logout` |
| Users | `GET /users`, `PUT /users/{id}`, `GET /users/me/participations` |
| Events | `GET /events`, `POST /events`, `PUT /events/{id}`, `POST /events/{id}/approval`, `POST /events/{id}/publish`, `POST /events/{id}/join`, `POST /events/{id}/attendance`, `POST /events/{id}/complete` |
| Reports | `GET /reports`, `POST /reports`, `POST /reports/{id}/review`, `POST /reports/{id}/verify` |
| Collaboration | `GET /collaboration-requests`, `POST /collaboration-requests`, `POST /collaboration-requests/{id}/approval` |
| Notifications | `GET /notifications/count`, `GET /notifications`, `POST /notifications/{id}/read` |
| Certificates | `GET /certificates`, `GET /certificates/{id}/verify`, `GET /certificates/{id}/download` |
| Rewards | `GET /rewards/catalog`, `POST /rewards/redeem` |
| Geographic | `GET /geo/options`, `GET /geo/stats`, `GET /kodepos/{code}` |
| Kampung/XP | `GET /landing/leaderboard`, `GET /kampung`, `GET /kampung/{id}/pillars` |
| Recommendations | `GET /recommendations`, `POST /recommendations` return 410/off-system |

## Database

Default DB path:

```text
database/runtime/database.db
```

Override path:

```bash
SIMRP_DB_PATH=./database/runtime/database.db
```

Tabel runtime utama:

- `roles`
- `role_attributes`
- `kecamatan`
- `kelurahan`
- `postal_codes`
- `kampung_mapping`
- `users`
- `events`
- `event_participation`
- `event_reports`
- `xp_kelurahan`
- `xp_pillar`
- `audit_logs`
- `collaboration_requests`
- `notifications`
- `certificates`
- `voucher_catalog`
- `voucher_redemptions`
- `sessions`
- `temporary_adjustments`

Database runtime dan backup tidak boleh masuk Git. `.gitignore` sudah mengecualikan `database/runtime/`, `database/*.db`, dan `database/backups/*.db|*.sql`.

## Quickstart Lokal

```bash
npm install
npm run dev
```

Perintah `npm run dev` menjalankan:

- Python API dari `server/main.py`;
- Vite frontend dari `npm run dev:web`.

URL lokal:

- Frontend: `http://localhost:5173`
- Admin page: `http://localhost:5173/admin`
- Backend API: `http://127.0.0.1:8000/make-server-32aa5c5c`

Development credential:

- Jika `SIMRP_ADMIN_LOGIN_PASSWORD`, `SIMRP_DEMO_PASSWORD`, atau `SIMRP_SEED_ADMIN_PASSWORD` tidak diset di development, runtime membuat credential acak dan menulisnya ke `database/runtime/dev_credentials.txt`.
- Jangan commit file credential runtime.

## Environment Penting

Contoh lengkap ada di `.env.example`.

| Env | Fungsi |
|---|---|
| `SIMRP_ENV` | `development` atau `production` |
| `SIMRP_DB_PATH` | Path SQLite runtime |
| `SIMRP_HOST` | Bind host backend |
| `SIMRP_PORT` | Port backend |
| `SIMRP_ADMIN_LOGIN_USERNAME` | Username admin portal |
| `SIMRP_ADMIN_LOGIN_PASSWORD` | Password admin portal |
| `SIMRP_ENABLE_DEMO_SEED` | Enable/disable seed demo |
| `SIMRP_DEMO_PASSWORD` | Password akun demo |
| `SIMRP_SEED_ADMIN_PASSWORD` | Password seeded admin user |
| `SIMRP_ALLOWED_ORIGINS` | Allowlist CORS production |
| `SIMRP_PBKDF2_ITERATIONS` | Iterasi PBKDF2 password hashing |
| `SIMRP_SESSION_TTL_HOURS` | TTL session token |
| `SIMRP_MAX_BODY_BYTES` | Batas body JSON |
| `VITE_API_BASE_URL` | Base URL API untuk frontend |

## Script Penting

```bash
npm run dev
npm run dev:web
npm run api
npm run build
```

Windows helper:

```bat
start_server.bat --check
backup_database.bat --check
```

Smoke test:

```bash
python smoketest.py
```

Smoke test membaca:

- `SIMRP_SMOKE_BASE`
- `SIMRP_SMOKE_DEMO_PASSWORD`
- fallback credential dari `database/runtime/dev_credentials.txt`

## Catatan Frontend

Komponen utama:

- `src/app/App.tsx`: state-based routing, session bootstrap, dashboard switching.
- `src/lib/api.ts`: centralized API client.
- `UserDashboard.tsx`: event user, reports, kampung, certificates, rewards, attendance KSH.
- `ModeratorDashboard.tsx`: report moderation, event create/edit/approval/publish, collaboration review.
- `AdminDashboard.tsx`: overview admin dan akses ke `AdminGodMode`.
- `ReportingWizard.tsx`: report submission wizard.
- `PillarRadarChart.tsx`: radar chart XP empat pilar.

Catatan teknis:

- `src/types/index.ts` masih perlu diselaraskan dengan payload backend aktual.
- Notification logic masih terduplikasi di desktop/mobile navbar.
- Certificate download endpoint sudah ada, tetapi UI saat ini baru menampilkan detail/hash.

## Validasi yang Disarankan Sebelum Push

```bash
python -m py_compile server/main.py server/api/auth.py server/api/events.py server/api/reports.py
npm run build
python smoketest.py
```

Untuk perubahan backup script:

```bat
backup_database.bat --check
```

## Production Checklist

- Set `SIMRP_ENV=production`.
- Set `SIMRP_ADMIN_LOGIN_USERNAME` dan `SIMRP_ADMIN_LOGIN_PASSWORD` dengan credential kuat.
- Set `SIMRP_ENABLE_DEMO_SEED=false`, kecuali demo seed memang diperlukan.
- Jika demo seed production aktif, set `SIMRP_DEMO_PASSWORD` dan `SIMRP_SEED_ADMIN_PASSWORD`.
- Naikkan `SIMRP_PBKDF2_ITERATIONS` sesuai kapasitas server.
- Set `SIMRP_ALLOWED_ORIGINS` ke domain frontend resmi.
- Jangan expose database runtime, backup, `.env`, atau `dev_credentials.txt`.
- Jalankan backend di belakang reverse proxy TLS jika dipublish ke internet.

## File yang Sengaja Tidak Dipush

Local AI/editor instruction mirrors, audit handoff reports, runtime DB, backup DB, logs, dan env lokal di-ignore supaya tidak ikut `git add .`.

Contoh:

- `.ai_rules`
- `.ai_security_manifesto.md`
- `.github/copilot-instructions.md`
- `AGENTS.md`
- `AI_HANDOFF_REPORT.md`
- `PROJECT_STRUCTURE_AUDIT.md`
- `database/runtime/`
- `database/backups/*.db`
- `database/backups/*.sql`
