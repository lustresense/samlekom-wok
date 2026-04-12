# Demo Accounts SIMRP

## 🔐 Security Update (April 2026)

**PENTING**: Password admin sekarang di-generate **OTOMATIS** setiap kali server dimulai untuk keamanan!

### Admin Login
- **Username**: `admin` (halaman `/admin`)
- **Password**: Lihat di **console output** saat server dijalankan
  ```
  [SECURITY] Generated random admin password.
  [SECURITY] Admin password: xxxxxxxxxxxx
  ```
- **Custom Password**: Set environment variable `SIMRP_SEED_ADMIN_PASSWORD=YourPassword` sebelum menjalankan server

### User/Moderator Login
- Semua akun non-admin login dari halaman `/login` (email + password)
- Password tetap: `password123` (untuk demo purposes)

---

## Kredensial Demo

| Role | Tier/Mode | Nama | Username/Email | Password | Tujuan Demo |
|---|---|---|---|---|---|
| Admin | Super Admin | Administrator | `admin` (halaman `/admin`) | **Random** (lihat console) | Login admin, switch view, monitoring global |
| Moderator | Tier 1 (ASN) | Pak Raka ASN | `moderator1.demo@simrp.app` | `password123` | Buat draft kegiatan |
| Moderator | Tier 2 (Lurah) | Bu Sinta Lurah | `moderator2.demo@simrp.app` | `password123` | Approve draft skala kelurahan, verifikasi laporan |
| Moderator | Tier 2 (Camat) | Pak Dimas Camat | `moderator2.camat@simrp.app` | `password123` | Approve draft skala kecamatan |
| Moderator | Tier 3 | Pak Arif | `moderator3.demo@simrp.app` | `password123` | Monitoring agregat/insight |
| User | Relawan | Andi Relawan | `relawan.demo@simrp.app` | `password123` | Join event, submit laporan |
| User | Relawan | Nia Relawan | `relawan2.demo@simrp.app` | `password123` | Simulasi peserta tambahan |
| User | Relawan | Budi Relawan | `relawan3.demo@simrp.app` | `password123` | Simulasi peserta tambahan |
| User | KSH | Kak Esa | `ksh.demo@simrp.app` | `password123` | Tandai event selesai |

---

## 🚀 Quick Start untuk Demo

### 1. Start Server
```bash
npm run dev
```

### 2. Catat Password Admin
Saat server start, lihat output:
```
============================================================
SIMRP API Server - Security Status
============================================================
[MODE] Development (SIMRP_ENV=development)
[WARNING] Development mode has relaxed security settings.
[WARNING] Do NOT use in production!

[SECURITY] Generated random admin password.
[SECURITY] Admin password: AbCdEfGhIjKl
[SECURITY] Set SIMRP_SEED_ADMIN_PASSWORD env var to use a custom password.
============================================================
```
**Password admin**: `AbCdEfGhIjKl` (contoh - akan berbeda setiap session!)

### 3. Login Admin
1. Buka `http://localhost:5173/admin`
2. Username: `admin`
3. Password: **dari console output**

---

## 🎬 Skenario Demo Cepat (Create -> Approve -> Join -> Report -> Verify)

1. Login `moderator1.demo@simrp.app`: buat draft event.
2. Login `moderator2.demo@simrp.app` atau `moderator2.camat@simrp.app`: approve draft sesuai scope.
3. Login relawan (`relawan.demo@simrp.app` / `relawan2.demo@simrp.app`): join event.
4. Login `ksh.demo@simrp.app`: tandai event selesai.
5. Login relawan yang sudah join: klik `Lapor Kegiatan` lalu submit report.
6. Login Tier 2/Admin: verifikasi report (approve/reject).
7. Cek tab `Leaderboards` untuk lihat perubahan ranking kampung.

---

## 🔧 Custom Admin Password (Optional)

Untuk demo dengan password tetap, gunakan environment variable:

### Windows (PowerShell):
```powershell
$env:SIMRP_SEED_ADMIN_PASSWORD="DemoPassword123!"; npm run dev
```

### Windows (CMD):
```cmd
set SIMRP_SEED_ADMIN_PASSWORD=DemoPassword123! && npm run dev
```

### Linux/Mac:
```bash
SIMRP_SEED_ADMIN_PASSWORD="DemoPassword123!" npm run dev
```

### Permanent (.env.local):
```bash
cp .env.example .env.local
# Edit .env.local, set:
SIMRP_SEED_ADMIN_PASSWORD=DemoPassword123!
```

---

## ⚠️ Production Notes

**JANGAN gunakan password default untuk production!**

Sebelum deploy:
1. Set `SIMRP_ENV=production`
2. Set `SIMRP_ADMIN_PASSWORD` dengan strong password (min 16 karakter)
3. Set `SIMRP_PBKDF2_ITERATIONS=600000`
4. Review [Production Checklist](./docs/security/PRODUCTION_CHECKLIST.md)

---

**Last Updated**: April 2026
**Version**: 2.0 (Security Updated)
