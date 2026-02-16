# SIMRP - Sitemap dan Information Architecture (IA)

## Status Validasi
Sitemap dari Gemini **sebagian besar sudah benar** dan sesuai struktur aplikasi saat ini.

## Koreksi Minor yang Perlu Dicatat
1. `Lapor` di User View adalah **modal wizard**, bukan halaman full route.
2. `Protected App Shell` sebenarnya hanya di route `/app`, sedangkan isi layar dikendalikan oleh state internal (`view`, `tab`, `page`, `tier`).
3. `POV Switcher` muncul di konteks admin; bukan navigasi global untuk semua role.
4. Tier moderator memang punya `overview`, tapi default awalnya mengikuti tier:
   Tier 1 ke `monitor`, Tier 2 ke `verify`, Tier 3 ke `aggregate`.

## IA Final 
### 1) Zona Aplikasi
1. Public Zone
2. Auth Gate
3. Protected App Shell
4. Role-Based Workspaces
5. Cross-Cutting Navigation

### 2) Prinsip Struktur
1. URL minimal, state-driven UI di dalam `/app`.
2. Akses fitur berbasis role (`User`, `Moderator Tier 1/2/3`, `Admin`).
3. Alur utama User: lihat event -> ikut event -> submit laporan.
4. Alur utama Moderator: monitoring/approval/verifikasi.
5. Alur utama Admin: governance, monitoring global, dan temporary override via God Mode.

## Sitemap Ringkas (Human Readable)
### Public Zone
1. Landing Page (`/`)
2. Login Page (`/login`) - tab Relawan, tab Moderator
3. Register Page (`/register`)
4. Admin Login Page (`/admin`)

### Protected App Shell
1. Container Dashboard (`/app`)
2. View User
3. View Moderator (Tiered)
4. View Admin

### User View
1. Home
2. Event
3. Lapor (Modal Wizard)
4. Profil

### Moderator View
1. Tier 1: Monitor, Rekom, Overview
2. Tier 2: Verify, Events, Overview
3. Tier 3: Aggregate, Insight, Overview

### Admin View
1. Overview
2. Users
3. Events
4. Reports
5. God Mode: Roles, Adjustments, History

## Sitemap Tree ASCII 1 (Visual)
SIMRP Application
|-- Public Zone
|   |-- Landing Page
|   |-- Login Page
|   |   |-- Tab: Relawan
|   |   `-- Tab: Moderator
|   |-- Register Page
|   `-- Admin Login Page
`-- Protected App Shell
    |-- Overlay dan Navigasi
    |   |-- Floating Menu
    |   |   |-- Profil Saya
    |   |   `-- Keluar
    |   |-- Admin Mobile Menu (Switch Context)
    |   `-- POV Switcher (Admin)
    |
    |-- View: User
    |   |-- Home
    |   |-- Event
    |   |   |-- Tab: Mendatang
    |   |   |-- Tab: Selesai
    |   |   |-- Filter Pilar (Lingkungan, Ekonomi, Kemasyarakatan, Sosial Budaya)
    |   |   `-- Action: Gabung Event / Tandai Selesai (mode KSH)
    |   |-- Lapor (Modal Wizard)
    |   |   |-- Step 1: Pilih Event + Foto + Jumlah Peserta
    |   |   `-- Step 2: Pilih Dampak + Kirim Laporan
    |   `-- Profil
    |
    |-- View: Moderator
    |   |-- Tier 1
    |   |   |-- Monitor
    |   |   |-- Rekom
    |   |   `-- Overview
    |   |-- Tier 2
    |   |   |-- Verify
    |   |   |-- Events
    |   |   `-- Overview
    |   `-- Tier 3
    |       |-- Aggregate
    |       |-- Insight
    |       `-- Overview
    |
    `-- View: Admin
        |-- Tab: Overview
        |-- Tab: Users
        |-- Tab: Events
        |-- Tab: Reports
        `-- Tab: God Mode
            |-- Sub-tab: Roles
            |-- Sub-tab: Adjustments
            `-- Sub-tab: History

## Sitemap Tree ASCII 2 (Full Technical)
SIMRP Application
|-- Public Zone
|   |-- Landing Page (/)
|   |-- Login Page (/login)
|   |   |-- Tab: Relawan
|   |   `-- Tab: Moderator
|   |-- Register Page (/register)
|   `-- Admin Login Page (/admin)
`-- Protected App Shell (/app)
    |-- Overlay dan Navigasi
    |   |-- Floating Menu
    |   |   |-- Profil Saya
    |   |   `-- Keluar
    |   |-- Admin Mobile Menu (Switch Context)
    |   `-- POV Switcher (Admin)
    |
    |-- View: User (/app?view=user)
    |   |-- Home (/app?view=user&page=home)
    |   |-- Event (/app?view=user&page=events)
    |   |   |-- Tab: Mendatang
    |   |   |-- Tab: Selesai
    |   |   |-- Filter Pilar (Lingkungan, Ekonomi, Kemasyarakatan, Sosial Budaya)
    |   |   `-- Action: Gabung Event / Tandai Selesai (mode KSH)
    |   |-- Lapor (Modal Wizard)
    |   |   |-- Step 1: Pilih Event + Foto + Jumlah Peserta
    |   |   `-- Step 2: Pilih Dampak + Kirim Laporan
    |   `-- Profil (/app?view=user&page=profile)
    |
    |-- View: Moderator (/app?view=moderator)
    |   |-- Tier 1
    |   |   |-- Monitor (/app?view=moderator&tier=1&page=monitor)
    |   |   |-- Rekom (/app?view=moderator&tier=1&page=rekom)
    |   |   `-- Overview (/app?view=moderator&tier=1&page=overview)
    |   |-- Tier 2
    |   |   |-- Verify (/app?view=moderator&tier=2&page=verify)
    |   |   |-- Events (/app?view=moderator&tier=2&page=events)
    |   |   `-- Overview (/app?view=moderator&tier=2&page=overview)
    |   `-- Tier 3
    |       |-- Aggregate (/app?view=moderator&tier=3&page=aggregate)
    |       |-- Insight (/app?view=moderator&tier=3&page=insight)
    |       `-- Overview (/app?view=moderator&tier=3&page=overview)
    |
    `-- View: Admin (/app?view=admin)
        |-- Tab: Overview (/app?view=admin&tab=overview)
        |-- Tab: Users (/app?view=admin&tab=users)
        |-- Tab: Events (/app?view=admin&tab=events)
        |-- Tab: Reports (/app?view=admin&tab=reports)
        `-- Tab: God Mode (/app?view=admin&tab=godmode)
            |-- Sub-tab: Roles (/app?view=admin&tab=godmode&subtab=roles)
            |-- Sub-tab: Adjustments (/app?view=admin&tab=godmode&subtab=adjustments)
            `-- Sub-tab: History (/app?view=admin&tab=godmode&subtab=history)

## Sitemap Detail (Spreadsheet Ready)
| ID | Parent_ID | Level | Page_Name | URL_or_State | Type | Role_Access | Goal | Key_Actions | Notes |
|---|---|---:|---|---|---|---|---|---|---|
| SIMRP | - | 0 | SIMRP App | / | Screen | Public | Entry sistem | - | Root |
| PUB | SIMRP | 1 | Public Zone | / | Screen | Public | Akses publik | - | Zona umum |
| PUB-LANDING | PUB | 2 | Landing Page | / | Screen | Public | CTA masuk/daftar | Masuk, Daftar | Halaman utama |
| PUB-LOGIN | PUB | 2 | Login Page | /login | Screen | Public | Autentikasi user/moderator | Submit login | Punya tab internal |
| PUB-LOGIN-REL | PUB-LOGIN | 3 | Tab Relawan | /login?tab=user | Tab | Public | Login relawan | Submit kredensial | Role check user |
| PUB-LOGIN-MOD | PUB-LOGIN | 3 | Tab Moderator | /login?tab=moderator | Tab | Public | Login moderator | Submit kredensial | Role check moderator |
| PUB-REGISTER | PUB | 2 | Register Page | /register | Screen | Public | Registrasi relawan | Isi form, submit | Geo validation kodepos |
| PUB-ADMIN-LOGIN | PUB | 2 | Admin Login Page | /admin | Screen | Public | Login admin | Submit admin credentials | Admin-only auth |
| APP | SIMRP | 1 | Protected App Shell | /app | Screen | User, Moderator-T1, Moderator-T2, Moderator-T3, Admin | Workspace utama | Navigate by state | State-driven UI |
| APP-NAV | APP | 2 | Floating Menu | /app?overlay=floating-menu | Overlay | User, Moderator-T1, Moderator-T2, Moderator-T3, Admin | Aksi cepat akun | Profil Saya, Keluar | Admin punya switch context tambahan |
| APP-POV | APP | 2 | POV Switcher | /app?overlay=pov-switcher | Overlay | Admin | Pindah perspektif view | Switch user/moderator/admin | Untuk admin |
| USER | APP | 2 | User View | /app?view=user | Screen | User, Admin | Aktivitas relawan | Navigate page | View berbasis role |
| USER-HOME | USER | 3 | Home | /app?view=user&page=home | Screen | User, Admin | Ringkasan kampung | Lihat leaderboard | Default user page |
| USER-EVENTS | USER | 3 | Event | /app?view=user&page=events | Screen | User, Admin | Cari dan ikut kegiatan | Filter, gabung event | Bisa mode KSH untuk tandai selesai |
| USER-EVENTS-UP | USER-EVENTS | 4 | Tab Mendatang | /app?view=user&page=events&tab=upcoming | Tab | User, Admin | Ikut event aktif | Gabung event | Dengan filter pilar |
| USER-EVENTS-DONE | USER-EVENTS | 4 | Tab Selesai | /app?view=user&page=events&tab=completed | Tab | User, Admin | Lihat event selesai | Lihat riwayat | Read only |
| USER-REPORT | USER | 3 | Lapor Kegiatan | /app?view=user&modal=reporting-wizard | Modal | User, Admin | Submit laporan kegiatan | Buka wizard | Modal 2 langkah |
| USER-REPORT-S1 | USER-REPORT | 4 | Step 1 Bukti Kegiatan | /app?view=user&modal=reporting-wizard&step=1 | Step | User, Admin | Input bukti awal | Pilih event, upload foto, isi peserta | Wajib diisi |
| USER-REPORT-S2 | USER-REPORT | 4 | Step 2 Dampak | /app?view=user&modal=reporting-wizard&step=2 | Step | User, Admin | Finalisasi laporan | Pilih dampak, kirim | Submit report |
| USER-PROFILE | USER | 3 | Profil | /app?view=user&page=profile | Screen | User, Admin | Lihat data profil dan aktivitas | Lihat badge, riwayat | Statistik laporan |
| MOD | APP | 2 | Moderator View | /app?view=moderator | Screen | Moderator-T1, Moderator-T2, Moderator-T3, Admin | Supervisi wilayah | Navigate by tier/page | Tier-based |
| MOD-T1-MON | MOD | 3 | Tier 1 Monitor | /app?view=moderator&tier=1&page=monitor | Screen | Moderator-T1, Admin | Monitoring kampung binaan | Pantau data | Default Tier 1 |
| MOD-T1-REKOM | MOD | 3 | Tier 1 Rekom | /app?view=moderator&tier=1&page=rekom | Screen | Moderator-T1, Admin | Input draft kegiatan | Simpan draft event | Input kegiatan |
| MOD-T1-OV | MOD | 3 | Tier 1 Overview | /app?view=moderator&tier=1&page=overview | Screen | Moderator-T1, Admin | Ringkasan tier | Lihat summary | Informasi umum |
| MOD-T2-VER | MOD | 3 | Tier 2 Verify | /app?view=moderator&tier=2&page=verify | Screen | Moderator-T2, Admin | Verifikasi laporan | Approve/Reject report | Default Tier 2 |
| MOD-T2-EVT | MOD | 3 | Tier 2 Events | /app?view=moderator&tier=2&page=events | Screen | Moderator-T2, Admin | Approval event draft | Approve/Reject event | Approval flow |
| MOD-T2-OV | MOD | 3 | Tier 2 Overview | /app?view=moderator&tier=2&page=overview | Screen | Moderator-T2, Admin | Ringkasan tier | Lihat summary | Informasi umum |
| MOD-T3-AGG | MOD | 3 | Tier 3 Aggregate | /app?view=moderator&tier=3&page=aggregate | Screen | Moderator-T3, Admin | Monitoring agregat kota | Lihat agregat | Default Tier 3 |
| MOD-T3-INS | MOD | 3 | Tier 3 Insight | /app?view=moderator&tier=3&page=insight | Screen | Moderator-T3, Admin | Insight program | Lihat tren | Analisis kebijakan |
| MOD-T3-OV | MOD | 3 | Tier 3 Overview | /app?view=moderator&tier=3&page=overview | Screen | Moderator-T3, Admin | Ringkasan tier | Lihat summary | Informasi umum |
| ADM | APP | 2 | Admin View | /app?view=admin | Screen | Admin | Kontrol penuh sistem | Navigate tab | Dashboard admin |
| ADM-OV | ADM | 3 | Admin Overview | /app?view=admin&tab=overview | Tab | Admin | Snapshot KPI sistem | Lihat statistik | Tab utama |
| ADM-USR | ADM | 3 | Admin Users | /app?view=admin&tab=users | Tab | Admin | Manajemen pengguna | Lihat user list | Governance |
| ADM-EVT | ADM | 3 | Admin Events | /app?view=admin&tab=events | Tab | Admin | Monitoring event | Review event | Global |
| ADM-RPT | ADM | 3 | Admin Reports | /app?view=admin&tab=reports | Tab | Admin | Verifikasi laporan global | Approve/Reject report | Mirip moderator, scope global |
| ADM-GOD | ADM | 3 | Admin God Mode | /app?view=admin&tab=godmode | Tab | Admin | Intervensi administratif | Buka sub-tab | High privilege |
| ADM-GOD-ROLE | ADM-GOD | 4 | God Mode Roles | /app?view=admin&tab=godmode&subtab=roles | Tab | Admin | Role assignment | Assign/Remove moderator | Role control |
| ADM-GOD-ADJ | ADM-GOD | 4 | God Mode Adjustments | /app?view=admin&tab=godmode&subtab=adjustments | Tab | Admin | Temporary adjustment | Add points/badge sementara | Expire 24h |
| ADM-GOD-HIS | ADM-GOD | 4 | God Mode History | /app?view=admin&tab=godmode&subtab=history | Tab | Admin | Audit temporary action | Lihat history | Audit trail |

## Kesimpulan
Sitemap Gemini lo sudah tepat sebagai baseline. Dokumen ini versi final yang lebih operasional untuk IA, UX flow, dan pengisian spreadsheet.
