# Day 15 Draft Artefak Kerja

## Konteks
- Proyek: SIMRP
- Fokus hari ini: Sprint planning, task breakdown, dan daftar API prioritas
- Matkul terkait: MPPL

## Sprint Goal
Menetapkan backlog prioritas untuk alur inti sistem (auth, event, report, approval) agar implementasi mingguan terarah dan terukur.

## Prioritas Sprint (MVP Flow)
1. Login sesuai role (`user`, `moderator`, `admin`)
2. Lifecycle event (`draft -> approval -> published -> completed`)
3. Pelaporan kegiatan oleh relawan
4. Verifikasi laporan oleh moderator/admin
5. Dashboard ringkasan per role

## Task Breakdown
| Task ID | Modul | Task | Prioritas | Estimasi | Dependency | Output |
|---|---|---|---|---|---|---|
| SP-01 | Auth | Validasi login per role dan session handling | High | 3 jam | API auth | Alur login role-based stabil |
| SP-02 | Event | Input draft event (tier 1) + approval (tier 2) | High | 4 jam | SP-01 | Event status lifecycle berjalan |
| SP-03 | Event | Publish, join event, quota check | High | 3 jam | SP-02 | Join event tervalidasi |
| SP-04 | Report | Wizard laporan (foto, peserta, outcome) | High | 4 jam | SP-03 | Submit laporan berhasil |
| SP-05 | Verification | Approve/reject report + feedback status | High | 3 jam | SP-04 | Verifikasi laporan end-to-end |
| SP-06 | Dashboard | Sinkron summary user/moderator/admin | Medium | 3 jam | SP-01..SP-05 | KPI dasar tampil per role |
| SP-07 | QA | Uji skenario utama dan catat bug | High | 2 jam | SP-01..SP-06 | Checklist test + temuan |

## Daftar API Prioritas
| Domain | Method | Endpoint | Fungsi |
|---|---|---|---|
| Auth | POST | `/auth/login` | Login user/moderator |
| Auth | POST | `/auth/signup` | Registrasi relawan |
| Auth | POST | `/auth/admin-login` | Login admin |
| Users | GET | `/users` | Ambil data user (admin/moderator) |
| Geo | GET | `/geo/options` | Opsi kecamatan/kelurahan |
| Geo | GET | `/kodepos/:kodepos` | Validasi wilayah dari kode pos |
| Events | GET | `/events` | List event |
| Events | POST | `/events` | Buat draft event |
| Events | POST | `/events/:id/approval` | Approve/reject event draft |
| Events | POST | `/events/:id/join` | Join event |
| Events | POST | `/events/:id/complete` | Tandai event selesai |
| Reports | GET | `/reports` | List laporan |
| Reports | POST | `/reports` | Submit laporan |
| Reports | POST | `/reports/:id/verify` | Verifikasi laporan |
| Kampung | GET | `/kampung` | Leaderboard/rekap kampung |
| Admin | GET | `/admin/temporary-adjustments` | List adjustment sementara |
| Admin | POST | `/admin/assign-role` | Assign moderator |
| Admin | POST | `/admin/remove-role` | Remove moderator |
| Admin | POST | `/admin/add-temporary-points` | Tambah poin sementara |
| Admin | POST | `/admin/add-temporary-badge` | Tambah badge sementara |

## Definisi Selesai (DoD) Singkat
1. Endpoint prioritas bisa diakses sesuai role.
2. Tidak ada blocker di alur auth -> event -> report -> verify.
3. Minimal 1 skenario uji lolos per role.
4. Bug kritikal dicatat dengan status tindak lanjut.

## Risiko dan Mitigasi
- Risiko: inkonsistensi role access antar UI dan API.
  Mitigasi: validasi akses di backend + smoke test per role.
- Risiko: data event/report ganda.
  Mitigasi: cek idempotency dan validasi status sebelum submit/approve.
- Risiko: scope wilayah tidak sinkron.
  Mitigasi: enforce rule `scope_type` vs `kecamatan/kelurahan`.

## Catatan Eksekusi Hari Ini
- Backlog prioritas sudah disusun.
- Task breakdown dan estimasi awal sudah ditetapkan.
- API list prioritas sudah dipetakan untuk eksekusi sprint.
