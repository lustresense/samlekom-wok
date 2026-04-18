# 🚀 SIMRP - Sistem Informasi Manajemen Rekap Partisipatif

<div align="center">

**Platform digital modern untuk warga Surabaya melaporkan kegiatan sosial, berpartisipasi dalam event kota, dan mendapatkan reward melalui sistem gamifikasi yang canggih.**

[🚀 Mulai Cepat](#-mulai-cepat) • [👤 Akun Demo](#-akun-demo) • [🏗️ Arsitektur](#-arsitektur) • [🛡️ Fitur](#-fitur-utama)

</div>

---

## 🚀 MULAI CEPAT

Ikuti langkah mudah berikut untuk menjalankan project di lingkungan lokal Anda.

### 1. Persiapan Lingkungan
Pastikan Anda sudah menginstal:
- **Node.js v18+** & **npm**
- **Python 3.10+**

### 2. Instalasi & Setup
Clone repository dan instal dependensi melalui terminal:

```bash
# Clone repository
git clone https://github.com/lustresense/samlekom-wok.git
cd Figmasimrp

# Instal dependensi frontend & backend
npm install
```

### 3. Jalankan Aplikasi
Gunakan satu perintah untuk menjalankan frontend (Vite) dan backend (Python) secara bersamaan:

```bash
npm run dev
```

Buka browser dan akses: `http://localhost:5173`

---

## 👤 AKUN DEMO

Gunakan akun berikut untuk mencoba berbagai hak akses sistem. Semua akun menggunakan password: `password123`

| Role | Email | Deskripsi |
| :--- | :--- | :--- |
| **Relawan** | `relawan.demo@simrp.app` | Ikut event, submit laporan, pantau XP & level. |
| **KSH** | `ksh.demo@simrp.app` | Kader Surabaya Hebat dengan badge khusus & fitur buat event. |
| **Mod Tier 1** | `moderator1.demo@simrp.app` | ASN Pemkot: Input usulan kegiatan (Draft). |
| **Mod Tier 2** | `moderator2.demo@simrp.app` | Lurah/Camat: Verifikasi laporan & approval event. |
| **Mod Tier 3** | `moderator3.demo@simrp.app` | Admin Kota: Agregasi data & review kemitraan. |
| **Super Admin** | `admin` (username) | Akses penuh di `/admin` (password: `admin`). |

---

## 🏗️ ARSITEKTUR & TECH STACK

SIMRP dibangun dengan arsitektur yang ringan namun tangguh untuk efisiensi performa tinggi.

- **Frontend**: React 18, TypeScript, Vite 6, Tailwind CSS 4, Framer Motion.
- **Backend**: Python 3.10+ dengan HTTP server terintegrasi.
- **Database**: SQLite (Local file-based). Tidak memerlukan setup external database.
- **Penyimpanan**: Sistem file lokal (No external storage needed).

### Kenapa Tanpa Supabase?
Project ini telah dioptimasi untuk berjalan mandiri tanpa ketergantungan cloud provider eksternal seperti Supabase, memudahkan deployment di infrastruktur on-premise atau VPS standar.

---

## 🛡️ FITUR UTAMA

- **Gamifikasi Surabaya**: Sistem Level, XP Point, dan Badges (KSH Verified, Regional Badges).
- **Hierarki Verifikasi Multi-Tier**: Alur kerja profesional dari relawan hingga admin kota.
- **Responsive Navigation**: Navbar pintar yang menyesuaikan tampilan desktop dan mobile (Hamburger menu dropdown).
- **Security First**: Password hashing PBKDF2, session management, dan API rate limiting.

---

## 📂 STRUKTUR FOLDER

- `/src`: Kode sumber frontend (React, components, UI).
- `/server`: Core backend logic (Python, API endpoints, SQLite manager).
- `/database`: Penyimpanan data lokal `.db`.
- `/docs`: Dokumentasi mendalam dan panduan deployment.

---

**© 2026 Dinas Komunikasi dan Informatika Kota Surabaya**  
*SIMRP: Berdaya dari Warga, Untuk Surabaya Hebat!* 🇮🇩
