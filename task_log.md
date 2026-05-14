# 🧠 TASK LOG — SIMRP Refactor & Fitur Baru

> **Last Updated:** 2026-05-14
> **Status:** IN_PROGRESS
> **Checkpoint Terakhir:** Batch 3 selesai — menunggu Batch 4 Modularisasi Backend Lanjutan

---

## 🚨 INSTRUKSI UNTUK AI — BACA INI DULU SEBELUM NGAPA-NGAPA

1. **Kamu adalah AI agent yang melanjutkan pekerjaan sebelumnya.**
2. **BACA SELURUH FILE INI dulu dari atas ke bawah.** Pahami konteks, arsitektur, dan progress.
3. **Lihat bagian PROGRESS TRACKING di bawah.** Cari item dengan `[ ]` (belum selesai).
4. **Kerjakan SATU item `[ ]` pertama yang lo temukan.**
5. **Setelah SELESAI mengerjakan 1 item:**
   - Ubah `[ ]` jadi `[x]` di checklist.
   - Update **Checkpoint Terakhir** di atas.
   - Tambah changelog singkat di bagian CHANGELOG.
   - JANGAN kerjakan item berikutnya sebelum update file ini.
6. **Jika ada kendala, error, atau kebingungan:** TULIS di bagian NOTES / KENDALA, lalu berhenti. JANGAN MENGASUMSI.
7. **JANGAN MENGUBAH ARSITEKTUR** kecuali diminta di item checklist.
8. **JANGAN MENGHAPUS KODE YANG SUDAH ADA.** Hanya tambah atau pindahkan.

---

## 📐 ARSITEKTUR PROYEK SAAT INI

```
server/
├── main.py              ← Runtime utama (ThreadingHTTPServer, ~1570 baris)
├── main_test.py          ← Versi test backend
├── api/                  ← Modul API (auth, events, reports, dll.)
│   ├── __init__.py       ← Gabungan route
│   ├── auth.py
│   ├── events.py
│   ├── reports.py
│   ├── collaboration.py
│   ├── geographic.py
│   ├── xp.py
│   ├── admin.py
│   ├── notifications.py
│   ├── certificates.py
│   ├── rewards.py
│   ├── users.py
│   └── rate_limiter.py
├── core/                 ← Konfigurasi & helper
│   ├── config.py
│   ├── database.py
│   └── security.py
src/
├── app/
│   ├── App.tsx           ← SPA Router (state-based)
│   └── components/       ← Semua halaman & UI
├── lib/api.ts            ← API Client
├── types/index.ts        ← TypeScript types
└── data/                 ← Data statis (geographic, leveling, badges)
```

---

## ✅ YANG SUDAH BERES (JANGAN DIUBAH)

- [x] Auth system (login, signup, session, RBAC)
- [x] Event CRUD (create draft, approve/reject, join, complete)
- [x] Report system (submit wizard, verify, XP apply)
- [x] Leaderboard & XP (kelurahan, pillar)
- [x] Collaboration/Mitra (public form, review)
- [x] Notification system (in-app bell, polling)
- [x] Certificate record (tabel ada, record dibuat)
- [x] Voucher/Redeem (tabel ada, catalog & redeem)
- [x] Radar chart 4 pilar (komponen FE)
- [x] Audit trail (log_audit helper)
- [x] Rate limiting, security headers, CORS
- [x] FE Error pages (404, 429, 500)

---

## 📋 PROGRESS TRACKING — Yang Harus Dikerjakan

### Batch 1: Refactor Endpoint ke Modul
- [x] Pindahkan endpoint `/auth/*` dari main.py ke api/auth.py
- [x] Pindahkan endpoint `/events/*` dari main.py ke api/events.py
- [x] Pindahkan endpoint `/reports/*` dari main.py ke api/reports.py
- [x] Pindahkan endpoint `/collaboration-requests/*` dari main.py ke api/collaboration.py
- [x] Pindahkan endpoint `/geo/*`, `/kodepos/*`, `/kampung/*` dari main.py ke api/geographic.py
- [x] Pindahkan endpoint `/admin/*` dari main.py ke api/admin.py
- [x] Pindahkan endpoint `/notifications/*` dari main.py ke api/notifications.py (file baru)
- [x] Pindahkan endpoint `/certificates/*` dari main.py ke api/certificates.py (file baru)
- [x] Pindahkan endpoint `/rewards/*` dari main.py ke api/rewards.py (file baru)
- [x] Pindahkan endpoint `/users/*`, `/recommendations`, `/health` dari main.py ke api/users.py (file baru)

### Batch 2: Fitur Baru (Backend)
- [x] PUBLISH GATE: Tambah endpoint `POST /events/:id/publish` (status approved → published)
- [x] STATUS UNDER_REVIEW: Tambah transisi `pending` → `under_review` di laporan
- [x] PDF SERTIFIKAT: Tambah endpoint `GET /certificates/:id/download` (generate PDF)
- [x] EMAIL MITRA: Tambah stub email di approve mitra

### Batch 3: Perbaikan Hasil Audit (KRITIS sebelum Frontend)
- [x] Samakan nama env admin password (.env.example vs main.py)
- [x] Batasi endpoint /users, /reports, /events untuk user biasa (RBAC filter)
- [x] FIX CRITICAL: Migration error di event_reports_legacy (main.py:754-771). Bikin transaksi eksplisit, PRAGMA foreign_key_check, pastikan server bisa start ulang dengan DB existing.
- [x] FIX CRITICAL: Tutup celah RBAC verify laporan. Moderator T2 harus dicek scope wilayahnya (join ke events), bukan cuma role.
- [x] FIX CRITICAL: Tambah UI tombol "Publish" di ModeratorDashboard untuk event status "approved", panggil POST /events/:id/publish.
- [x] FIX CRITICAL: Hapus database/backups/*.db dan database/backups/*.sql dari repo. Tambah ke .gitignore. Kalau perlu, rotasi password demo.
- [x] Perbaiki start_server.bat (path ke server/main.py) atau hapus jika tidak terpakai.
- [x] Perbaiki backup_database.bat (path database) atau hapus jika tidak terpakai.
- [x] Perbaiki smoketest.py (sesuaikan endpoint), atau nonaktifkan dengan komentar jika belum sempat.

### Batch 4: Backend Modularisasi Lanjutan
- [ ] Batch 4.1 — Update arsitektur task_log berdasarkan audit terbaru: `main.py` ~1570 baris, modul API aktif/legacy diperjelas
- [ ] Batch 4.2 — Extract pure helpers dari `server/main.py` ke `server/core/*` tanpa ubah behavior
- [ ] Batch 4.3 — Extract schema, migration, dan seed dari `server/main.py` ke `server/db/*`
- [ ] Batch 4.4 — Extract service logic ke `server/services/*`: auth/session, audit, notifications, XP, geography, dev credentials, temporary adjustments
- [ ] Batch 4.5 — Kurangi dependency dictionary di `server/main.py` secara bertahap setelah helper/service aktif
- [ ] Batch 4.6 — Bersihkan duplicate/dead code: route-dict legacy, `server/api/xp.py`, `server/api/rate_limiter.py`, `server/main_test.py`, setelah usage dicek
- [ ] Batch 4.7 — Final backend smoke test: health, auth, event approve/publish, join, attendance, complete, report review/verify, certificate, reward, notifications

### Batch 5: Frontend Completeness
- [ ] Halaman "Event Saya" di UserDashboard (riwayat partisipasi)
- [ ] Timeline status laporan di detail report
- [ ] Rank card di profil/halaman dashboard
- [ ] Tambah tombol/download flow untuk certificate download jika UI belum expose endpoint `/certificates/:id/download`

### Batch 6: Frontend Professional Refactor
- [ ] Split `ModeratorDashboard.tsx` menjadi module kecil: event management, report review, collaboration review, geo/data hooks
- [ ] Split `UserDashboard.tsx` menjadi module kecil: events, reports, certificates, rewards, attendance, leaderboard
- [ ] Extract shared notification hook dari DesktopNavbar dan MobileNavbar
- [ ] Sinkronkan `src/types/index.ts` dengan payload backend aktif
- [ ] Pastikan semua API call dashboard lewat helper/hook yang konsisten

### Batch 7: Documentation & Release Readiness
- [ ] Update README agar sesuai runtime aktual: `main.py` ~1570 baris sekarang, admin env yang benar, endpoint aktif
- [ ] Update DEMO_ACCOUNTS sesuai sistem credential lokal terbaru
- [ ] Update CONTRIBUTOR_SETUP_GUIDE sesuai start/backup script terbaru
- [ ] Jalankan final validation: `npm run build`, `python -m py_compile`, smoketest end-to-end

---

## 📝 CATATAN / KENDALA

- (isi kalau ada masalah, error, atau hal yang perlu diketahui agent berikutnya)
- Batch 4 harus dikerjakan bertahap satu item per session agar aman dari context window limit.
- Jangan gabungkan Batch 4.1 dengan schema/migration/seed.
- Jangan sentuh frontend sebelum Batch 4 minimal selesai Batch 4.1 atau user minta.
- Jangan hapus legacy code sebelum usage dicek.
- 2026-05-11: Runtime smoke test endpoint RBAC tidak tuntas karena startup existing DB gagal di migrasi `event_reports_legacy` (`sqlite3.IntegrityError: FOREIGN KEY constraint failed`). Verifikasi sintaks in-memory tetap OK.

---

## 📝 CHANGELOG

### 2026-05-14 — Reprioritization: Backend Modularization Before Frontend
- Menambahkan Batch 4 Modularisasi Backend Lanjutan berdasarkan audit terbaru.
- Batch frontend dipindah menjadi Batch 5.
- Arsitektur diperbarui: `server/main.py` saat ini sekitar 1570 baris dan masih memegang banyak helper/service non-route.

### 2026-05-14 — Batch 3 Item 9: smoketest.py
- Menulis ulang `smoketest.py` agar sesuai endpoint aktif: `/geo/options`, `/geo/stats`, `/rewards/catalog`, `/rewards/redeem`, dan endpoint admin yang tersedia.
- Smoketest kini membaca base URL/password dari env, fallback ke `database/runtime/dev_credentials.txt`, serta memilih ID kelurahan dari `/geo/options` alih-alih hardcode ID.
- Verifikasi: `python -m py_compile smoketest.py` dan smoke run end-to-end via server temporer/DB temporer (`59 PASS`, `0 FAIL`).

### 2026-05-14 — Batch 3 Item 8: backup_database.bat
- Memperbaiki backup database dengan entry point root `backup_database.bat` dan `scripts/backup_database.bat` yang menjalankan `scripts/backup_database.py`.
- Backup kini memakai path default `database/runtime/database.db`, mendukung `SIMRP_DB_PATH`/`SIMRP_BACKUP_DIR`, dan menyimpan hasil ke `database/backups` yang sudah di-ignore.
- Verifikasi: `python -m py_compile scripts/backup_database.py`, `cmd /c backup_database.bat --check`, dan backup/restore read test dengan database temporer.

### 2026-05-14 — Batch 3 Item 7: start_server.bat
- Menambahkan `start_server.bat` yang menjalankan `server\main.py` dari root repo, memvalidasi path entrypoint, dan fallback dari `python` ke `py -3`.
- Verifikasi: `cmd /c start_server.bat --check`, `python -m py_compile server/main.py`, dan smoke run `/health` via batch dengan DB temporer.

### 2026-05-13 — Batch 3 Item 6: Backup DB Cleanup & Demo Password Rotation
- Menghapus tracked backup `database/backups/*.db` dan `database/backups/*.sql`, lalu mengubah `.gitignore` agar backup database tidak masuk repo lagi.
- Menghapus fallback demo password statis (`password123`/`admin`) dari runtime aktif/test, menggantinya dengan secret lokal generated di `database/runtime/dev_credentials.txt` atau env eksplisit.
- Verifikasi: `python -m py_compile server/main.py server/main_test.py server/api/auth.py`, `npm run build`, dan smoke run schema dengan DB temporer.

### 2026-05-11 — Batch 3 Item 5: Publish Button ModeratorDashboard
- Menambahkan action publish event di ModeratorDashboard untuk status approved.
- Verifikasi: `npm run build`.

### 2026-05-11 — Batch 3 Item 4: RBAC Verify Report Scope
- Menambahkan validasi scope wilayah untuk moderator tier 2 (lurah/camat) saat review/verify laporan berdasarkan event.
- Verifikasi: `python -m py_compile server/api/reports.py`.

### 2026-05-11 — Batch 3 Item 3: Fix Migration event_reports_legacy
- Membuat transaksi eksplisit dengan matikan `PRAGMA foreign_keys = OFF` dan commit/rollback pattern di `server/main.py`.
- Menambahkan pemeriksaan `PRAGMA foreign_key_check` untuk mendeteksi pelanggaran relasi.
- Verifikasi: server `main.py` berhasil di-*start* dengan koneksi dan migrasi ke *database existing* berstatus `OK` tanpa *IntegrityError*.

### 2026-05-11 — Batch 3 Item 2: RBAC Filter Endpoint
- `GET /users`: user biasa hanya menerima data dirinya sendiri; KSH hanya menerima relawan/KSH di kelurahannya.
- `GET /reports`: user/KSH hanya menerima laporan miliknya sendiri, meskipun query `userId` dikirim berbeda.
- `GET /events`: user/KSH hanya menerima event `published`/`completed` yang sesuai kelurahan/kecamatan area mereka.
- Verifikasi: compile in-memory `server/api/users.py`, `server/api/reports.py`, `server/api/events.py`, dan `server/main.py` → SYNTAX OK.

### 2026-05-11 — Batch 3 Item 1: Env Admin Password
- `.env.example` disamakan dengan runtime `server/main.py`: admin password kini memakai `SIMRP_ADMIN_LOGIN_PASSWORD`.
- `server/core/config.py` ikut diselaraskan agar export `ADMIN_LOGIN_PASSWORD` membaca env yang sama.
- Verifikasi: compile in-memory `server/core/config.py` dan `server/main.py` → SYNTAX OK.

### 2026-05-06 — Batch 2 Item 4: EMAIL MITRA
- Ditambahkan fungsi `_send_approval_email_stub()` di `server/api/collaboration.py`.
- Stub dipanggil saat approve/reject mitra di handler `/collaboration-requests/:id/approval`.
- Stub: log ke stdout dengan payload lengkap (to, subject, body, smtp_host).
- Fail gracefully: exception email tidak rollback transaksi approval (try/except terpisah).
- Semua konfigurasi SMTP via env var (`SIMRP_SMTP_HOST`, `SIMRP_EMAIL_FROM`, dll.) — tidak ada hardcode sesuai .ai_rules 2.3.
- Query SELECT diperluas untuk mengambil `email`, `pic_name`, `support_type`, `support_description`.
- Verifikasi: `python -m py_compile` → SYNTAX OK.

### 2026-05-06 — Batch 2 Item 3: PDF SERTIFIKAT
- Ditambahkan endpoint `GET /certificates/:id/download` di `server/api/certificates.py`.
- Menggunakan stdlib Python `html` (escape) — tanpa dependensi eksternal (no reportlab/weasyprint).
- Generate HTML sertifikat bergaya (Playfair Display + Inter) yang bisa dicetak sebagai PDF dari browser (Ctrl+P → Save as PDF).
- Security: requires auth, RBAC ownership check (pemilik atau admin), semua output di-escape XSS, header security standar.
- `_generate_certificate_html()` me-escape semua field user/event via `html.escape()`.
- Filename dibersihkan dari karakter berbahaya (`/`, `\`).
- Verifikasi: `python -m py_compile` → SYNTAX OK.

### 2026-05-06 — Batch 2 Item 2: STATUS UNDER_REVIEW
- Ditambahkan endpoint `POST /reports/:id/review` di `server/api/reports.py` (transisi `pending` → `under_review`).
- DB schema `event_reports` di `server/main.py` diupdate: CHECK constraint diperluas ke `('pending','under_review','verified','rejected')`.
- Migration otomatis ditambahkan di `migrate_schema()` untuk DB yang sudah ada: recreate tabel dengan constraint baru (pola sama dengan migrasi events).
- Handler `/verify` diupdate: kini menerima laporan berstatus `pending` ATAU `under_review`.
- Audit trail dan notifikasi tersedia di semua transisi.
- Verifikasi: `python -m py_compile` → SYNTAX OK.

### 2026-05-06 — Batch 2 Item 1: PUBLISH GATE
- Ditambahkan endpoint `POST /events/:id/publish` di `server/api/events.py`.
- Flow baru: `draft` → `/approval` → `approved` → `/publish` → `published`.
- Handler `/approval` kini hanya set status ke `approved` (bukan langsung `published`).
- Guard ditambahkan: hanya event berstatus `draft` yang bisa di-review; hanya event `approved` yang bisa dipublish.
- RBAC tetap: moderator_t2 (lurah/camat sesuai area) atau admin.
- Audit trail dan notifikasi ditambahkan pada kedua langkah.
- Verifikasi: `python -m py_compile` → SYNTAX OK.

### 2026-05-03 — Batch 1 Langkah 1
- Endpoint `/auth/*` dipindahkan dari `server/main.py` ke `server/api/auth.py` dengan delegasi handler GET/POST/DELETE.
- Verifikasi: `python -m py_compile server/main.py server/api/auth.py` dan smoke test lokal login/me/logout berhasil.

### 2026-05-03 — Batch 1 Langkah 2
- Endpoint `/events/*` dipindahkan dari `server/main.py` ke `server/api/events.py` dengan delegasi handler GET/POST/PUT.
- `server/main.py` kini mendelegasikan rute event ke modul `events_api`.

### 2026-05-03 — Batch 1 Langkah 3
- Endpoint `/reports/*` dipindahkan dari `server/main.py` ke `server/api/reports.py` dengan delegasi handler GET/POST.
- `server/main.py` kini mendelegasikan rute report ke modul `reports_api`.

### 2026-05-03 — Batch 1 Langkah 4
- Endpoint `/collaboration-requests/*` dipindahkan dari `server/main.py` ke `server/api/collaboration.py` dengan delegasi handler GET/POST.
- `server/main.py` kini mendelegasikan rute kolaborasi ke modul `collaboration_api`.

### 2026-05-06 — Batch 1 Langkah 5
- Endpoint `/geo/*`, `/kodepos/*`, `/kampung/*` sudah ditangani di `server/api/geographic.py` dan didelegasikan dari `server/main.py`.

### 2026-05-06 — Batch 1 Langkah 6
- Endpoint `/admin/*` dipindahkan dari `server/main.py` ke `server/api/admin.py` dengan delegasi handler GET/POST.

### 2026-05-06 — Batch 1 Langkah 7
- Endpoint `/notifications/*` dipindahkan dari `server/main.py` ke `server/api/notifications.py` dengan delegasi handler GET/POST.

### 2026-05-06 — Batch 1 Langkah 8
- Endpoint `/certificates/*` dipindahkan dari `server/main.py` ke `server/api/certificates.py` dengan delegasi handler GET.

### 2026-05-06 — Batch 1 Langkah 10
- Endpoint `/users/*` (GET list, GET me/participations, PUT update), `/recommendations` (GET/POST stub), `/health` (GET), dan `/landing/leaderboard` (GET) dipindahkan dari `server/main.py` ke `server/api/users.py`.
- Ditambahkan `users_dependencies()` di `main.py` dan delegasi `users_api.handle_get/post/put` pada `do_GET`, `do_POST`, `do_PUT`.
- Verifikasi: `python -m py_compile server/main.py server/api/users.py` → SYNTAX OK.

### 2026-05-06 — Batch 1 Langkah 9
- Endpoint `/rewards/*` dipindahkan dari `server/main.py` ke `server/api/rewards.py` dengan delegasi handler GET/POST.

### 2026-05-03 — Inisialisasi TASK_LOG
- Template dibuat, siap diisi.
```
