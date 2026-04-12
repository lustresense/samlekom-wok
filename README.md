# 🚀 SIMRP - Sistem Informasi Manajemen Rekap Partisipatif

<div align="center">

**Platform digital untuk masyarakat Surabaya melaporkan kegiatan sosial, bergabung event, dan mendapat reward dengan sistem level & badge**

[🚀 Quick Start](#-quick-start---mulai-dalam-3-langkah-mudah) • [🎮 Demo Accounts](#-demo-accounts) • [📋 Fitur](#-fitur-utama) • [🏗️ Arsitektur](#-arsitektur)

</div>
ne
---

## 🚀 QUICK START - Mulai Dalam 3 Langkah Mudah

> **Untuk kontributor yang baru**: Jangan pusing, tiga langkah ini aja. Sisanya akan otomatis.

### ✅ Langkah 1: Setup Komputer (Cek Sekali Doang)

Buka **Command Prompt** atau **Terminal**, salin dan jalankan satu persatu:

```bash
node --version
npm --version
python --version
```

**Hasil yang **BENAR**:**
- Node: `v18.0.0` atau lebih tinggi (misal: `v20.10.0`) ✅
- NPM: `8.0.0` atau lebih tinggi ✅
- Python: `3.10` atau lebih tinggi (misal: `3.11.8`) ✅

**Kalau ada yang error atau nggak keluar versi?**
- **Node belum install** → Download di https://nodejs.org (pilih button hijau besar "LTS") → Install → Restart komputer
- **Python belum install** → Download di https://www.python.org → **PENTING: Centang "Add Python to PATH" saat install** → Restart komputer

---

### ✅ Langkah 2: Download & Setup Project (5 Menit)

**A. Kalau dapat link GitHub:**
```bash
git clone <PASTE_LINK_GITHUB_DI_SINI>
cd Figmasimrp
```

**B. Kalau dapat file ZIP:**
1. Extract ZIP ke folder (misalnya: `C:\Users\YourName\Documents\Figmasimrp`)
2. Buka **Command Prompt**, ketik:
```bash
cd C:\Users\YourName\Documents\Figmasimrp
```
*(ganti path sesuai folder kamu)*

**C. Setelah folder terbuka di terminal, ketik:**
```bash
npm install
```

**Tunggu sampai selesai.** Terminal akan terlihat sibuk beberapa menit. Ini normal. ⏳
- Kalau muncul tulisan `added XXX packages in XXX` → ✅ BERHASIL
- Kalau ada error yang berwarna merah:
  - Cek koneksi internet (harus stabil dan kuat)
  - Ulangi lagi perintah `npm install`

---

### ✅ Langkah 3: Jalankan & Buka Browser (Selesai!)

Masih di terminal folder yang sama, ketik:
```bash
npm run dev
```

**Tunggu sampai muncul:**
```
VITE v6.3.5  ready in XXX ms

➜  Local:   http://localhost:5173/
```

**JANGAN TUTUP TERMINAL INI.** Biarkan terus terbuka.

Sekarang buka **browser** (Chrome, Firefox, Edge, Safari), pergi ke:
```
http://localhost:5173
```

**Jreeng! 🎉 Aplikasi sudah jalan.**

---

## 🎯 Sehari-Hari Ngoding

Setiap kali mau develop:

1. **Buka folder project di terminal** (atau buka terminal baru dan `cd` ke folder)
2. **Ketik satu perintah:**
```bash
npm run dev
```
3. **Browser otomatis buka** atau manual buka `http://localhost:5173`
4. **Ubah-ubah file** (React/CSS/JavaScript) → **Otomatis refresh di browser** ✨

Untuk **berhenti/stop**, tekan **`Ctrl + C`** di terminal (atau tutup terminal).

---

## ❓ Masalah Umum & Solusi

| Masalah | Apa yang terjadi | Solusi |
|---------|-----------------|--------|
| **"command not found: npm"** | Terminal nggak kenal npm | Restart komputer, ulangi `npm --version` |
| **"Python not found"** | Terminal nggak kenal python | Restart komputer, cek "Add Python to PATH" saat install |
| **Terminal error pas jalan `npm install`** | Ada error berwarna merah | Ulangi `npm install`, pastikan internet kuat |
| **"Port 5173 already in use"** | Port sudah dipakai aplikasi lain | Tutup aplikasi lain, atau ganti port di `vite.config.ts` |
| **"Database error" atau blank page** | Database rusak | Ketik di terminal: `rm -rf database/runtime` lalu `npm run dev` lagi |
| **Browser blank / error di console** | Terminal dev masih berjalan tapi error JavaScript | Cek terminal, ada error berwarna merah? Scroll up, baca error-nya |
| **Perubahan file nggak muncul di browser** | File belum di-save atau code error | Pastikan file udah di-save (Ctrl+S), refresh browser (Ctrl+R) |

**Masalah tidak tercantum di atas?**
- Screenshot error di terminal → tanya di #dev-help
- Cek internet stabil
- Coba restart terminal + restart browser

---

## 👥 Demo Accounts - Langsung Login Aja Pakai Ini

**Aplikasi sudah punya akun-akun siap pakai.** Cukup login pakai email & password di bawah. **SEMUA akun pakai password yang sama:** `password123`

### 👤 Regular Volunteer (Relawan Biasa)
```
Email: relawan.demo@simrp.app
Password: password123
```
**Bisa apa**: Lihat event, ikut event, submit laporan, lihat ranking

**Test apa**: 
1. Login
2. Klik tab "Event"
3. Pilih salah satu event, klik "Ikuti"
4. Lihat poin & level naik

---

### 🏘️ KSH - Kepala Lingkungan (Verified Authority)
```
Email: ksh.demo@simrp.app
Password: password123
```
**Bisa apa**: Semua yang relawan + Buat event baru + Tandai event selesai

**Test apa**:
1. Login
2. Buka menu (hamburger ☰ icon)
3. Coba "Buat Event"
4. Lihat badge KSH di profil

---

### 🛡️ Moderator Tier 1 (ASN / Pegawai Negeri)
```
Email: moderator1.demo@simrp.app
Password: password123
```
**Bisa apa**: Bikin draft event proposal

---

### 🛡️ Moderator Tier 2 (Lurah / Kelurahan Head)
```
Email: moderator2.demo@simrp.app
Password: password123
```
**Bisa apa**: Approve/tolak event + Verifikasi laporan dari relawan + Kasih poin XP

**Test apa**:
1. Login
2. Buka menu (hamburger ☰) → "Dashboard"
3. Cek tab "Event Pending"
4. Klik approve/reject
5. Cek tab "Laporan" untuk verifikasi

---

### 🛡️ Moderator Tier 3 (Kota Level / City Admin)
```
Email: moderator3.demo@simrp.app
Password: password123
```
**Bisa apa**: Review kolaborasi mitra kota + Approve event level kota + Lihat report dari moderator lain

---

### ⚙️ Admin (FULL ACCESS - GOD MODE)
**Akses di**: `http://localhost:5173/admin`
```
Username: admin
Password: admin
```
**Bisa apa**: SEMUA - Manage user + Ubah poin/badge sesuka + Lihat audit log + Testing mode lengkap

**Test apa**:
1. Login ke admin page
2. Cek "God Mode" tab
3. Coba buat user custom atau ubah point
4. Lihat "Tasks" tab (fitur baru task explorer)

---

**💡 Tips**: Buka 2 browser tab / Incognito mode untuk test beda role sekaligus



## 🎯 FITUR UTAMA - Apa Aja yang Bisa Dilakukan

### 👥 Sistem Role (Siapa Lakukan Apa)
- **Relawan**: User biasa, bisa ikut event dan buat laporan
- **KSH**: Community leader dengan badge khusus, bisa bikin event sendiri
- **Moderator Tier 1-3**: Verifikator & approver dengan hak berbeda
- **Admin**: Full control, bikin user baru atau ubah apapun

### 🎮 Gamification System (Game + Reward)
- **Level**: Mulai dari level 1, naik terus seiring dapat poin dari aktivitas
- **XP Points**: Dapat poin dari ikut event & submit laporan
- **Badges**: Kumpulin badge dari aktivitas di area geografis (kelurahan/kecamatan)
- **Leaderboard**: Lihat ranking top relawan per wilayah

### 📅 Event Management (Bikin & Manage Event)
- **Lifecycle**: Event dibuat → Diapprove moderator → Publish → Relawan ikut → Selesai & beri report
- **Scope**: Event bisa untuk level kelurahan atau kecamatan
- **Registration**: Event punya kuota, relawan daftar sesuai kapasitas
- **Report System**: Setelah selesai, relawan upload foto + laporan

### 📊 Verification & Rewards (Validasi & Beri Poin)
- **Report Verification**: Moderator cek laporan, approve atau tolak
- **XP Award**: Laporan yang diapprove dapat poin XP
- **Leaderboard Update**: Poin langsung update di ranking

### 🎨 UI/UX Baru (April 2026)
- **Animated Navbar**: Floating navbar yang smooth dan indah pas buka/tutup
- **Task Explorer**: Admin bisa lihat daftar tasks dengan sorting & detail modal
- **Responsive Design**: Jalan sempurna di desktop, tablet, & mobile

---

## 🏗️ TEKNOLOGI - Tech Stack Apa Aja

### Frontend (Yang kamu lihat di browser)
```
React 18          - Framework JavaScript
TypeScript        - Supaya code lebih aman
Vite 6            - Fast build tool (kecepatan kilat)
Tailwind CSS 4    - Styling CSS yang cepat
Radix UI          - Accessible UI components
Framer Motion     - Smooth animations
Lucide Icons      - Icon library
```

### Backend (Server yang ngurus database)
```
Python 3.10+      - Bahasa programming
SQLite            - Database (file storage)
PBKDF2            - Secure password hashing
Rate Limiting     - Anti spam/attack
```

### Database (Penyimpanan data)
Semua data disimpan dalam file SQLite (database.db):
- `users` - Semua akun user
- `events` - Daftar event
- `event_participation` - Siapa join event apa
- `event_reports` - Laporan dari relawan
- `collaboration_requests` - Request kolaborasi dari partner
- `sessions` - Session data login
- `audit_logs` - Log siapa ngapain (untuk security)

---

## 📁 FOLDER STRUCTURE - Kemana File-File Disimpan

```
Figmasimrp/
├─ src/                          📱 Frontend React (Tampilan & Logic)
│  ├─ app/
│  │  ├─ App.tsx                # Halaman utama
│  │  └─ components/            # Semua komponen (pages & UI)
│  │     ├─ AdminDashboard.tsx        # Page: Admin dashboard
│  │     ├─ UserDashboard.tsx         # Page: User dashboard
│  │     ├─ ModeratorDashboard.tsx    # Page: Moderator dashboard
│  │     ├─ ui/                       # Reusable UI components
│  │     │  ├─ FloatingNavbar.tsx     # 🎯 Smart navbar (desktop/mobile)
│  │     │  ├─ DesktopNavbar.tsx      # Desktop navbar (hanya di desktop)
│  │     │  ├─ MobileNavbar.tsx       # Mobile navbar (hanya di mobile)
│  │     │  └─ button.tsx, card.tsx   # Other UI blocks
│  │     └─ landing/            # Landing page components
│  │
│  ├─ data/                     # Static data
│  │  ├─ levelingSystem.ts      # Level & XP progression
│  │  ├─ geographicData.ts      # Kelurahan/kecamatan data
│  │  └─ validatedBadges.ts     # Badge definitions
│  │
│  ├─ lib/                      # Utility functions
│  │  └─ api.ts                 # API client ke backend
│  │
│  ├─ types/                    # TypeScript types
│  │  └─ index.ts               # All type definitions
│  │
│  ├─ styles/                   # CSS styling
│  │  ├─ tailwind.css           # Tailwind config
│  │  └─ theme.css              # Custom theme
│  │
│  └─ main.tsx                  # Entry point (jangan diubah)
│
├─ server/                      🐍 Backend Python (Logic & Database)
│  ├─ main.py                  # Server utama (handles semua request)
│  ├─ api/                     # API endpoints (modular)
│  │  ├─ auth.py               # Login & register
│  │  ├─ events.py             # Event CRUD operations
│  │  ├─ reports.py            # Report submission & verification
│  │  ├─ xp.py                 # XP & leveling logic
│  │  └─ ...
│  ├─ core/                    # Core utilities
│  │  ├─ config.py             # Settings
│  │  ├─ database.py           # Database manager
│  │  ├─ security.py           # Password hashing
│  │  └─ rate_limiter.py       # Anti spam
│  └─ models/                  # Data models (optional)
│
├─ database/                    💾 Data Storage
│  ├─ database.db              # Live SQLite database (di-generate otomatis)
│  └─ backups/                 # Backup files
│
├─ docs/                        📚 Documentation lengkap
│  ├─ guides/                   # Tutorial & panduan
│  │  ├─ QUICKSTART.md          # Quick start guide
│  │  └─ DEPLOYMENT.md          # Deployment guide
│  └─ architecture/             # Architecture docs
│
├─ scripts/                     🔧 Helper scripts
│  ├─ dev-local.mjs             # Script untuk `npm run dev`
│  └─ ...
│
├─ package.json                 # NPM configuration (list dependency)
├─ vite.config.ts               # Vite configuration (build settings)
├─ tailwind.config.ts           # Tailwind configuration
└─ tsconfig.json                # TypeScript configuration
```

**Yang perlu kamu perhatian:**
- ✅ Ubah file di `src/` → langsung refresh di browser
- ✅ Ubah file di `server/main.py` → perlu restart terminal
- ❌ JANGAN ubah: `package.json`, `vite.config.ts`, `tsconfig.json` (kecuali tahu apa yang dilakukan)

---

## 🧪 TESTING FITUR - Test Setiap Role

> **Tip**: Buka 2 browser tab (atau incognito mode) untuk test beda role tanpa logout/login terus-menerus

### 1️⃣ Test Sebagai Relawan (Regular User)
1. Login pakai email: `relawan.demo@simrp.app` password: `password123`
2. Klik tab "Event" di navbar
3. Cari event yang tersedia
4. Klik tombol "Ikuti Event" atau "Join"
5. Lihat profil → score/poin harus naik

### 2️⃣ Test Sebagai Moderator
1. Login pakai email: `moderator2.demo@simrp.app` password: `password123`
2. Klik menu hamburger (☰) → "Dashboard"
3. Lihat tab "Event Pending"
4. Klik salah satu event → tombol "Approve" atau "Reject"
5. Cek tab "Laporan" untuk verifikasi laporan dari relawan

### 3️⃣ Test Sebagai Admin (Full Control)
1. Buka `http://localhost:5173/admin`
2. Login: username `admin`, password `admin`
3. Di halaman admin bisa:
   - Tab **Overview**: Lihat statistik keseluruhan
   - Tab **Users**: Manage user (buat baru / edit / delete)
   - Tab **God Mode**: Ubah poin siapapun, assign moderator
   - Tab **Audit Log**: Lihat history semua aksi
   - Tab **Tasks** (Baru): List tasks dengan sorting, click untuk detail

### 4️⃣ Test Navbar Animation (Fitur Baru April 2026) ✨
**Ini adalah fitur paling important yang baru diperbaiki:**
1. Login akun manapun
2. Lihat navbar di atas halaman (bentuk "pill" rounded)
3. Desktop (layar lebar) → navbar tetap di atas fixed
4. Mobile/tablet (layar sempit) → navbar tetap di atas tapi bentuk compact
5. **PENTING**: Klik menu button (hamburger ☰) atau pill → perhatikan animasi
   - ✅ Harus: Smooth morphing dari pill ke expanded modal
   - ✅ Harus: Konten menu fade in/out tanpa stretching
   - ✅ Tidak boleh: Distorsi, melar, atau jittery animation
6. Clik X atau area outside modal → tutup dengan animasi smooth

**Kalau animasi kelihatan jelek/melar:**
- Buka browser console (F12)
- Cek error message di tab Console
- Screenshot error → tanyakan di #dev-help

---

## 🛠️ DEVELOPER COMMANDS - Perintah Sehari-Hari

**Semua perintah dijalankan di terminal di folder project root** (folder Figmasimrp)

| Perintah | Fungsi | Kapan Pakai |
|----------|--------|-----------|
| `npm run dev` | ✨ **Jalankan frontend + backend selamanya** | ✅ **Setiap hari** - Paling penting! |
| `npm run dev:web` | Jalankan hanya frontend (tidak backend) | Jarang - kalau backend error |
| `npm run api` | Jalankan hanya backend (tidak frontend) | Jarang - debugging backend aja |
| `npm run build` | Build project untuk production/deploy | Deploy saja, bukan development |
| `npm install` | Download/install semua library | Pertama kali setup atau ada library baru |

**Yang paling penting: `npm run dev`** - cukup satu perintah ini aja setiap hari.

---

## ⚡ TIPS & TRICKS SEHARI-HARI

### 💡 Debugging Kalau Ada Error

**Kalau ada error di browser:**
1. Buka browser **Console** (tekan **F12** → cari tab **Console**)
2. Baca error message (biasanya ada line number)
3. Buka file itu di code editor (biasanya di folder `src/`)
4. Baca line yang error → pahami apa salahnya
5. Screenshot console → tanyakan di #dev-help dengan konteks

### 📝 Test Beda Role Cepat (Pro Tip)

**Gunakan Incognito/Private Window:**
1. Window normal: Login sebagai relawan
2. Tab Incognito baru: Login sebagai moderator
3. Sekarang bisa test 2 role sekaligus tanpa logout/login = lebih cepat!

### 🔄 Auto-Refresh Ketika Code Berubah

- **Frontend code** (file `.tsx` / `.css` di `src/`): Otomatis refresh di browser setelah save ✨ (magic!)
- **Backend code** (file `.py` di `server/`): Perlu restart terminal (Ctrl+C, terus `npm run dev` lagi)

### 🗑️ Reset Database ke Kondisi Bersih

Kalau database rusak atau mau mulai fresh dari awal:
```bash
rm -rf database/runtime
npm run dev
```
Database akan di-generate ulang otomatis dengan akun demo siap pakai.

### 🔍 Cari Tahu Dimana Bug Itu

**Browser DevTools** (tekan F12):
- Tab **Console**: Error messages
- Tab **Network**: Request ke server (loading/error)
- Tab **Elements**: HTML struktur halaman
- Tab **Sources**: Debug JavaScript step-by-step
- Tab **Application**: Local storage, cookies, sessions

---

## 📊 ROLE PERMISSIONS - Tabel Siapa Bisa Apa

| Fitur | Relawan | KSH | Mod T1 | Mod T2 | Mod T3 | Admin |
|-------|:-------:|:---:|:------:|:------:|:------:|:-----:|
| Lihat Event | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Join Event | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Submit Laporan | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Bikin Event Baru | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ |
| Approve Event | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Verifikasi Laporan | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Review Partnership | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Manage User | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## 🔐 SECURITY - Data Protection

Aman kok, data kamu protected dengan:
- **PBKDF2**: Password di-hash dengan super aman (210,000 encryption rounds)
- **Session Auth**: Login expires otomatis dalam 24 jam
- **Rate Limiting**: API dibatasi 10-120 request per menit (prevent spam/attack)
- **Query Validation**: Semua form di-validasi sebelum process
- **Database Backup**: Otomatis backup setiap hari

---

## 🏆 MENJADI KONTRIBUTOR

### Untuk yang baru pertama kali contribute:

1. **Fork repository** di GitHub (buat copy pribadi)
2. **Clone** ke komputer:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Figmasimrp.git
   cd Figmasimrp
   ```
3. **Install & jalankan**:
   ```bash
   npm install
   npm run dev
   ```
4. **Buat branch baru** (jangan di main):
   ```bash
   git checkout -b feature-nama-fitur-kamu
   ```
5. **Code** fitur kamu (test dengan `npm run dev`)
6. **Commit** dengan pesan jelas:
   ```bash
   git commit -m "Add: navbar animation fix for mobile responsiveness"
   ```
7. **Push** ke GitHub:
   ```bash
   git push origin feature-nama-fitur-kamu
   ```
8. **Buat Pull Request** (PR) dengan deskripsi detail apa yang berubah

### Aturan Kontribusi:
- ✅ Test 100% sebelum push
- ✅ Commit message harus clear & descriptive
- ✅ Jangan push langsung ke main branch
- ✅ PR harus di-review sebelum merge
- ✅ Node version harus 18+, Python 3.10+
- ❌ Jangan ubah `package-lock.json` tanpa alasan
- ❌ Jangan commit `.env` files

---

## 📞 HELP & SUPPORT

**Ada yang nggak jelas atau ada error?**

1. **Cek troubleshooting** (section di atas "Masalah Umum & Solusi")
2. **Google errornya** - baik banget untuk learning
3. **Tanyakan di #dev-help** dengan:
   - Screenshot terminal (error message)
   - Apa yang kamu lakukan sebelum error
   - Step demi step yang sudah dicoba

---

## 📅 CHANGELOG - Update Terbaru (April 2026)

### ✨ Fitur Baru
- **FloatingNavbar Refactor**: Split jadi 3 komponen terpisah untuk clean architecture
- **layoutId Animation Fix**: Smooth pill-to-modal transition tanpa visual distortion
- **Inner Content Fading**: Counter-scale technique eliminate stretching artifacts
- **Conditional Rendering**: Hanya 1 navbar di DOM sekaligus (desktop XOR mobile)
- **Responsive Architecture**: React state-based breakpoint (bukan CSS media queries)

### 🧹 Code Quality
- ✅ Removed redundant DOM elements (both navbars rendering simultaneously)
- ✅ Simplified component tree dan render logic
- ✅ Better separation of concerns (Desktop/Mobile/Float wrapper)
- ✅ QWEN Zero-Redundancy Mode compliance

### 🐛 Bug Fixes (Critical)
- 🔧 ~~Navbar distortion on animation~~ → FIXED ✅
- 🔧 ~~DOM reflow conflicts~~ → FIXED ✅
- 🔧 ~~Tailwind media query interference~~ → FIXED ✅
- 🔧 ~~Modal content stretching~~ → FIXED ✅

---

## 🚀 NEXT STEPS

- Review & test navbar animation di semua device (desktop/tablet/mobile)
- Collect feedback from team setelah deployment
- Plan next performance optimizations
- Consider accessibility improvements (a11y audit)

---

**Happy Coding! Ship fast, break things responsibly! 🚀**
9. **Buat Pull Request** di GitHub

### Aturan Commit Message
```
feat(scope): deskripsi fitur
fix(scope): deskripsi bugfix
docs(scope): update dokumentasi
refactor(scope): refactor code
```

Contoh:
- `feat(admin): tambah task explorer dengan sorting`
- `fix(auth): fix session expiration bug`
- `docs(readme): update instalasi guide`

---

## 📚 DOKUMENTASI LENGKAP

| Dokumen | Lokasi |
|---------|--------|
| User Flow & Use Case | `USER_FLOW_USECASE.md` |
| Architecture Details | `docs/architecture/` |
| Security Guide | `docs/security/` |
| Deployment Guide | `docs/guides/DEPLOYMENT.md` |
| Quick Start | `docs/guides/QUICKSTART.md` |
| Demo Accounts | `DEMO_ACCOUNTS.md` |

---

## 🎯 FITUR BARU (APRIL 2026)

### ✨ Task Explorer (Admin)
**Lokasi**: Admin Dashboard → Tab "Tasks"

**Fitur**:
- ✅ Sorting by Date/Time:
  - Newest First
  - Oldest First
  - Nearest Deadline
  - Farthest Deadline
- ✅ Clickable Rows:
  - Cursor pointer pas hover
  - Click untuk buka modal detail
  - Keyboard accessible (Enter/Space)
- ✅ Task Detail Modal:
  - Title, description, expected output
  - Delivery format, impact
  - Base tier, deadline, status
  - Revision count, created date

**Files**:
- `src/app/components/TaskExplorer.tsx`
- `src/app/components/shared/TaskDetailModal.tsx`

---

### 🎨 Animated Floating Navbar
**Lokasi**: Semua dashboard (user, moderator, admin)

**Fitur**:
- ✅ Smooth spring animations (Framer Motion)
- ✅ AnimatePresence untuk mount/unmount
- ✅ Layout prop untuk counter-scale (tidak stretched)
- ✅ Icon rotation animation (menu ↔ close)
- ✅ Smooth backdrop fade

**Konfigurasi Spring**:
```typescript
{
  type: 'spring',
  damping: 20,
  stiffness: 100,
  mass: 0.5
}
```

**Files**:
- `src/app/components/ui/FloatingNavbar.tsx`

---

## 📞 NEED HELP?

- **Technical Docs**: Cek folder `docs/`
- **User Manual**: `docs/guides/PETUNJUK_PENGGUNAAN.md`
- **Issues**: Buat GitHub issue dengan reproduction steps
- **Questions**: Baca docs dulu, baru tanya

---

**Built for Kota Surabaya** 🇮🇩  
**© 2026 Dinas Komunikasi dan Informatika Kota Surabaya**

**Version**: 3.0.0 - April 2026  
**Status**: ✅ Active Development
