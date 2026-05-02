# 🚀 SIMRP - Sistem Informasi Manajemen Rekap Partisipatif

<div align="center">
  <img src="./src/assets/logos/logo.svg" alt="SIMRP Logo" width="120" />
</div>

<p align="center">
  <b>Platform digital cerdas berbasis gamifikasi untuk kolaborasi warga dan pemerintah Kota Surabaya.</b>
</p>

---

## 📑 Daftar Isi

1. [Latar Belakang & Visi](#-latar-belakang--visi)
2. [Fitur & Modul Utama](#-fitur--modul-utama)
3. [Hierarki Moderasi (Multi-Tier)](#%EF%B8%8F-hierarki-moderasi-multi-tier)
4. [Alur Sistem (User Flow)](#-alur-sistem-user-flow)
5. [Arsitektur Backend (Native Python)](#%EF%B8%8F-arsitektur-backend-native-python)
6. [Arsitektur Database (SQLite3)](#%EF%B8%8F-arsitektur-database-sqlite3)
7. [Keamanan & Enkripsi (Security)](#-keamanan--enkripsi-security)
8. [Arsitektur Frontend (React + Vite)](#%EF%B8%8F-arsitektur-frontend-react--vite)
9. [Struktur API Endpoints](#-struktur-api-endpoints)
10. [Panduan Mulai Cepat (Quickstart)](#-panduan-mulai-cepat-quickstart)
11. [Checklist Deployment Production](#-checklist-deployment-production)

---

## 📝 Latar Belakang & Visi

**SIMRP** adalah manifestasi dari visi "Surabaya Hebat" yang mengedepankan sinergi tingkat bawah (grassroots) antara warga, Kader Surabaya Hebat (KSH), dan pemangku kebijakan. Sistem ini **tidak dibangun dengan *framework* *bloated***, melainkan dirancang khusus secara *native* agar sangat efisien, tangguh, dan dapat dijalankan di infrastruktur *on-premise* dengan konsumsi sumber daya seminimal mungkin tanpa mengorbankan keamanan.

---

## ✨ Fitur & Modul Utama

- **Gamifikasi Partisipasi & Radar Chart**: Warga mendapatkan XP (*Experience Points*) setiap kali menyelesaikan dan melaporkan kegiatan gotong royong. Poin ini dibagi ke dalam **4 Pilar Utama** (Lingkungan, Sosial, Ekonomi, Kesehatan) yang divisualisasikan secara interaktif menggunakan *Recharts* dalam wujud Radar Chart personal.
- **Pencapaian (Badges System)**: Algoritma *backend* akan menganalisa distribusi pilar XP dan memberikan gelar/badge otomatis secara *real-time* (contoh: *Eco Champion*, *KSH Verified*).
- **Ruang Kolaborasi (Crowdsourcing)**: Warga dapat memprakarsai kegiatan (Proposal Acara Warga). Jika *upvote* dari masyarakat tinggi, sistem otomatis meneruskan *draft* tersebut ke tingkat kecamatan untuk ditinjau pendanaannya.
- **Voucher & Reward Catalog**: Sistem inventori berbasis *Redemption* untuk menukarkan *Points* warga dengan insentif nyata dari pemerintah kota.

---

## ⚖️ Hierarki Moderasi (Multi-Tier)

Sistem *Role-Based Access Control (RBAC)* SIMRP sangat granular dan disesuaikan dengan hierarki Pemkot Surabaya:

| Role Code | Nama Peran | Hak Akses & Yurisdiksi |
| :--- | :--- | :--- |
| `user` | **Relawan Biasa** | Akses publik dasar. Hanya dapat *join* acara, *submit* laporan partisipasi (foto), dan melihat *Leaderboard*. |
| `ksh` | **Kader Surabaya Hebat**| Diverifikasi secara khusus. Dapat membuat inisiatif/draft acara di skala *Kelurahan*. |
| `moderator_t1`| **Moderator RW / Lurah** | Melakukan verifikasi *Tier 1* atas laporan warga di kelurahan yurisdiksinya. |
| `moderator_t2`| **Moderator Camat** | Menyetujui *publish* event skala *Kecamatan* dan memvalidasi pendanaan/kolaborasi eksternal. |
| `moderator_t3`| **Moderator Pemkot** | Akses ke dasbor analitik global tingkat Kota Surabaya. |
| `admin` | **Super Administrator**| Portal *God-Mode* rahasia untuk Seed DB, Manajemen Voucher, dan Audit Log transaksi sistem. |

---

## 🔄 Alur Sistem (User Flow)

1. **Registrasi Auto-Mapping**: Pengguna cukup mendaftar dengan memasukkan kode pos. Modul geografis (`/geographic/*`) otomatis mencari irisan kelurahan dan kecamatan secara presisi dari relasi *Database* 3NF statik (`geographicData.ts`).
2. **Penemuan Acara**: Pengguna dapat melihat daftar *Event* terdekat berdasarkan yurisdiksi domisilinya. Data disaring dinamis menurut 4 Pilar.
3. **Validasi Pelaksanaan**: Pengguna menekan tombol "Hadir". Saat kegiatan selesai, warga melaporkan partisipasi dengan *upload* foto bukti fisik (diproses lewat *Base64 string*) dan sistem menangkap lokasi GPS secara lokal.
4. **Verifikasi Berjenjang**: Moderator di *dashboard*-nya mengecek, lalu menyetujui (*Approve*) atau menolak (*Reject*) laporan tersebut (yang disertai alasan penolakan).
5. **Kalkulasi Reward**: Jika disetujui, modul `xp.py` akan langsung mengeksekusi penambahan XP Kelurahan, XP Pilar Individu, dan *Points* penukaran warga.

---

## ⚙️ Arsitektur Backend (Native Python)

Untuk menjamin performa *Cold-Boot* kilat dan independensi tinggi di server *on-premise*, backend ini **sama sekali tidak menggunakan framework** pihak ketiga seperti Django, Flask, atau FastAPI. 

Inti server HTTP ada di `server/main.py` (~2700 baris kode murni) yang memperluas `http.server.ThreadingHTTPServer`.

- **Modular Native Routing**: *Router* HTTP memecah request berdasarkan *path URL* ke spesifik modul fungsional di `server/api/`:
  - `auth.py`: Autentikasi dan Manajer *Session Token*.
  - `events.py`: Siklus hidup pembuatan kegiatan dan agregasi laporan publik.
  - `reports.py`: Penerimaan data form, pengolahan gambar *base64*, dan kontrol status laporan.
  - `admin.py`: Penanganan pergerakan admin darurat, termasuk auto-migration DB.
  - `rate_limiter.py`: In-memory *Sliding Window Bucket* anti-spam & proteksi *brute-force*.
- **Custom Middleware**: Parser JSON kustom membatasi ukuran *payload* (*MAX_BODY_BYTES*) untuk mencegah serangan DoS (Denial of Service).

---

## 🗄️ Arsitektur Database (SQLite3)

SIMRP membuang ketergantungan *setup* PostgreSQL/MySQL yang berat. Backend mengeksploitasi **SQLite3 WAL Mode (Write-Ahead Logging)** yang terkonfigurasi dengan pragma optimasi konkurensi, memungkinkan operasi *Thread-Locking* yang aman (*Thread-Safe*) dan sepenuhnya *ACID-compliant*.

Struktur *Schema Entity* (*Auto-Migrated on boot*):
- `users`, `roles`, `sessions` untuk Auth.
- `kecamatan`, `kelurahan`, `postal_codes`, `kampung_mapping` untuk relasi pemetaan Geografis yang ketat.
- `events`, `event_participation`, `event_reports` untuk mengikat warga dengan acara mereka.
- `xp_kelurahan`, `xp_pillar` untuk agregasi data papan klasemen (*Leaderboard*) super cepat.
- `audit_logs` untuk mencatat log audit permanen (siapa, merubah apa, dan kapan).

---

## 🔒 Keamanan & Enkripsi (Security)

- **Native PBKDF2 HMAC**: *Hashing* sandi warga dilakukan murni dengan algoritma HMAC-SHA256 (`pbkdf2_hmac`). Menggunakan iterasi minimum `210000` di tingkat *Development* dan siap diskalakan di atas `600000` via *environment variable* `SIMRP_PBKDF2_ITERATIONS` untuk produksi.
- **Session-based JWT-less**: Menolak kelemahan token JWT yang tidak dapat ditarik (*revoked*) secara instan. Menggunakan Token Hex 48-byte acak aman yang harus tervalidasi ke tabel memori `sessions` dengan *TTL (Time-To-Live)* ketat.
- **Rate Limiting Engine**: Perlindungan absolut di API level (terutama pada `/auth/*`) berbasis IP *Client* untuk mencegah eksploitasi skrip otomatis.
- **CSP & CORS**: Disertai penerapan *Strict-Transport-Security (HSTS)*, perlindungan *X-Frame-Options*, dan validasi asal *Cross-Origin Resource Sharing* eksplisit via variabel lingkungan `SIMRP_ALLOWED_ORIGINS`.

---

## 🖥️ Arsitektur Frontend (React + Vite)

Aplikasi klien (*Frontend*) dibangun dengan standar struktur *Enterprise-Grade*:
- **Core Stack**: React 18, Vite 6, TypeScript yang sangat efisien.
- **Styling Sistem**: *Tailwind CSS V4* dikolaborasikan sempurna dengan ribuan komponen UI dari ekosistem `shadcn/ui` (Radix Primitives) yang dikustomisasi di direktori `src/app/components/ui/`. Termasuk pemisahan cerdas antara `DesktopNavbar.tsx` dan `MobileNavbar.tsx`.
- **Motion & Animasi**: Pemanfaatan *Framer Motion* (`motion`) untuk micro-interaction interaktif dan transisi mulus *POV Switcher* (peralihan dasbor antara `UserDashboard`, `ModeratorDashboard`, `AdminDashboard`).
- **Validasi Mutlak**: Mengawinkan `react-hook-form` dengan validasi skema `zod` di sisi klien sebelum divalidasi ulang oleh Python backend.
- **Data Visualizer**: Penggunaan `recharts` secara *deep-level* pada komponen `LevelProgressionCard.tsx` dan `PillarRadarChart.tsx` untuk visualisasi performa relawan kota.

---

## 🔌 Struktur API Endpoints

Semua modul bersandar pada URI utama `/make-server-32aa5c5c`:

- **Auth** (`POST /auth/login`, `POST /auth/signup`, `GET /auth/me`): Pintu gerbang sesi.
- **Events** (`GET /events`, `POST /events/join`, `PUT /events/:id/status`): Sinkronisasi kuota acara real-time.
- **Reports** (`POST /reports/submit`, `PUT /reports/verify`): Moderasi warga.
- **Geographic** (`GET /geographic/kecamatan`): Resolusi wilayah Surabaya.
- **Admin** (`POST /admin/seed`): Eksekusi populasi 1000+ data historikal statis (dummy test).

---

## 🚀 Panduan Mulai Cepat (Quickstart)

Konsepnya adalah *Zero-Config Setup*—seluruh database SQLite dan server Python akan dibentuk dan dijalankan serentak hanya lewat satu skrip Node.

```bash
# 1. Klon repositori
git clone https://github.com/lustresense/samlekom-wok.git
cd Figmasimrp

# 2. Instal seluruh dependensi ekosistem NodeJS Frontend
npm install

# 3. Jalankan server pembangunan gabungan (Vite + Python Backend)
npm run dev
```

> **Akses Portal Development**:
> - Antarmuka Publik Klien: `http://localhost:5173`
> - Portal Super Admin Rahasia: `http://localhost:5173/admin` (User: `admin` | Pass: `admin`)
> - Backend REST Raw: `http://localhost:8000/make-server-32aa5c5c`

---

## 🛑 Checklist Deployment Production

Sebelum kode ini di- *push* dan dijalankan pada infrastruktur server (*bare-metal* atau VPS) resmi Pemerintah Kota Surabaya, pastikan parameter `.env.local` Anda disetel secara ketat:

- [ ] Pastikan `SIMRP_ENV=production` (*Triggers* Strict CSP, SQLite WAL Mode, menolak akses Origin sembarangan, menonaktifkan *Demo Seeding*).
- [ ] Ganti `SIMRP_ADMIN_PASSWORD` ke sandi super administrator dengan entalpi ekstrem (>16 karakter acak).
- [ ] Naikkan profil beban server `SIMRP_PBKDF2_ITERATIONS=600000`.
- [ ] Perlindungan pencurian cookie dengan menurunkan `SIMRP_SESSION_TTL_HOURS=24`.
- [ ] Enforce domain dengan mendaftarkan `SIMRP_ALLOWED_ORIGINS=https://simrp.surabaya.go.id`.
- [ ] Disarankan menyembunyikan port 8000 dari internet publik dan merutekannya (Reverse-Proxy) di belakang *Nginx* berlapis SSL/TLS.

---

<p align="center">
  <b>© 2026 SIMRP - Dinas Komunikasi dan Informatika Kota Surabaya</b><br>
  <i>"Berdaya dari Warga, Untuk Surabaya Hebat!"</i>
</p>
