# 🔧 Database Login Fix

## Masalah

Login user/moderator/admin selalu gagal dengan error "Email/password salah" meskipun:
- User ada di database
- Password benar ("password123")
- Verify password function benar

## Root Cause

**Database file terkunci oleh multiple Python processes** yang tidak terminated dengan benar.

Ketika database dikunci:
1. File tidak bisa dihapus (`del` command gagal silently)
2. New seeding di-skip karena user sudah ada (insert_user check email exists)
3. Password hash lama (yang salah) tetap digunakan

## Solusi

### 1. Kill semua Python processes
```bash
taskkill /F /IM python.exe /IM python3.10.exe
```

### 2. Delete database files
```bash
del /f /q database\runtime\database.db*
```

### 3. Re-seed database
```bash
python -c "import sys; sys.path.insert(0, 'server'); from local_api import init_schema; init_schema()"
```

### 4. Start server
```bash
python server\local_api.py
```

## Demo Credentials

| Role | Email/Username | Password |
|------|---------------|----------|
| User | relawan.demo@simrp.app | password123 |
| KSH | ksh.demo@simrp.app | password123 |
| Moderator T1 | moderator1.demo@simrp.app | password123 |
| Moderator T2 | moderator2.demo@simrp.app | password123 |
| Moderator T2 (Camat) | moderator2.camat@simrp.app | password123 |
| Moderator T3 | moderator3.demo@simrp.app | password123 |
| Admin | admin (at /admin) | admin |

## Prevention

Selalu kill semua Python processes sebelum:
- Delete database
- Re-start server
- Re-seed data

```bash
# Clean shutdown script
taskkill /F /IM python.exe /IM python3.10.exe /IM node.exe
```

---

**Fixed**: April 3, 2026  
**Status**: ✅ All logins working
