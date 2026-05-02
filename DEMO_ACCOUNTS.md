# Demo Accounts SIMRP

## 🔐 Security Update (April 2026)

**PENTING**: Untuk production, kredensial admin login harus diset via environment variable.

### Admin Login
- **Username**: `admin` (halaman `/admin`)
- **Development default**: `admin`
- **Production**: wajib set `SIMRP_ADMIN_LOGIN_USERNAME` dan `SIMRP_ADMIN_LOGIN_PASSWORD`
- **Custom password (dev/prod)**: set `SIMRP_ADMIN_LOGIN_PASSWORD=YourPassword`

### User/Moderator Login
- Semua akun non-admin login dari halaman `/login` (email + password)
- Password demo default: `password123`
- Bisa diganti via `SIMRP_DEMO_PASSWORD`
- Akun demo otomatis di-sync ke DB saat startup jika `SIMRP_ENABLE_DEMO_SEED=true`

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
Default development:
- Username: `admin`
- Password: `admin`

Jika ingin ubah:
- set `SIMRP_ADMIN_LOGIN_USERNAME`
- set `SIMRP_ADMIN_LOGIN_PASSWORD`

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
$env:SIMRP_ADMIN_LOGIN_PASSWORD="DemoPassword123!"; npm run dev
```

### Windows (CMD):
```cmd
set SIMRP_ADMIN_LOGIN_PASSWORD=DemoPassword123! && npm run dev
```

### Linux/Mac:
```bash
SIMRP_ADMIN_LOGIN_PASSWORD="DemoPassword123!" npm run dev
```

### Permanent (.env.local):
```bash
cp .env.example .env.local
# Edit .env.local, set:
SIMRP_ADMIN_LOGIN_PASSWORD=DemoPassword123!
```

### Kontrol Demo Seed
- `SIMRP_ENABLE_DEMO_SEED=true|false` (default: `true` di development, `false` di production)
- `SIMRP_DEMO_PASSWORD=...` (default: `password123`)

---

## ⚠️ Production Notes

**JANGAN gunakan password default untuk production!**

Sebelum deploy:
1. Set `SIMRP_ENV=production`
2. Set `SIMRP_ADMIN_LOGIN_USERNAME` dan `SIMRP_ADMIN_LOGIN_PASSWORD` dengan strong credential
3. Set `SIMRP_PBKDF2_ITERATIONS=600000`
4. Set `SIMRP_ALLOWED_ORIGINS=https://domain-fe-kamu.com`
5. Pastikan `SIMRP_ENABLE_DEMO_SEED=false`
6. Review [Production Checklist](./docs/security/PRODUCTION_CHECKLIST.md)

---

**Last Updated**: April 2026
**Version**: 2.0 (Security Updated)
