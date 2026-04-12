# SIMRP Security Guide

## 📋 Overview

Dokumentasi keamanan untuk SIMRP (Sistem Informasi Manajemen Rekap Partisipatif Kota Surabaya).

---

## 🔐 Authentication & Authorization

### Password Hashing
- **Algorithm**: PBKDF2-HMAC-SHA256
- **Iterations**: 210,000 (development), 600,000+ (production recommended)
- **Salt**: 16 bytes random per user
- **Storage format**: `{salt_hex}:{digest_hex}`

### Session Management
- **Token format**: URL-safe base64 (48 bytes entropy)
- **Session TTL**: 
  - Development: 168 hours (7 days)
  - Production: 24 hours (configurable via `SIMRP_SESSION_TTL_HOURS`)
- **Storage**: SQLite `sessions` table
- **Invalidation**: On logout, token deleted from database

### Rate Limiting
| Endpoint | Limit | Window |
|----------|-------|--------|
| `/auth/login` | 10 requests | 60 seconds |
| `/auth/signup` | 10 requests | 60 seconds |
| `/auth/admin-login` | 10 requests | 60 seconds |
| Mutation (POST/PUT/DELETE) | 120 requests | 60 seconds |

---

## 🛡️ Security Headers

### All Responses Include:
```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: no-referrer
Permissions-Policy: geolocation=(), microphone=(), camera=()
Cache-Control: no-store
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; ...
```

### Production Only:
```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

### Content Security Policy (CSP)
- **Scripts**: Self only (+ inline for React)
- **Styles**: Self + Google Fonts
- **Fonts**: Self + Google Fonts CDN
- **Images**: Self + data: URIs
- **Connect**: Self (API endpoints)

---

## 🔒 Environment Variables

### Required for Production:
```bash
SIMRP_ENV=production
SIMRP_ADMIN_LOGIN_USERNAME=your_admin_username
SIMRP_ADMIN_PASSWORD=your_strong_password_here
SIMRP_PBKDF2_ITERATIONS=600000
SIMRP_SESSION_TTL_HOURS=24
SIMRP_ALLOWED_ORIGINS=https://yourdomain.com
```

### Optional Configuration:
```bash
SIMRP_DB_PATH=/path/to/database.db
SIMRP_RATE_LIMIT_WINDOW_SECONDS=60
SIMRP_RATE_LIMIT_AUTH_MAX=10
SIMRP_RATE_LIMIT_MUTATION_MAX=120
SIMRP_MAX_BODY_BYTES=8388608
SIMRP_SEED_ADMIN_PASSWORD=custom_seed_password
```

---

## 📁 File Security

### Git-Ignored Files:
```
.env.local
database/runtime/*.db
database/*.db-journal
database/*.db-wal
server/__pycache__/
```

### Database Location:
- **Default**: `./database/runtime/database.db`
- **Configurable**: `SIMRP_DB_PATH` environment variable
- **Backup**: Store in `./database/backups/` (git-tracked)

---

## 🚨 Production Checklist

### Before Deployment:

#### 1. Environment Configuration
- [ ] Set `SIMRP_ENV=production`
- [ ] Change `SIMRP_ADMIN_PASSWORD` to strong password (min 16 chars, mixed case, numbers, symbols)
- [ ] Set `SIMRP_PBKDF2_ITERATIONS=600000` or higher
- [ ] Configure `SIMRP_ALLOWED_ORIGINS` with your domain
- [ ] Set `SIMRP_SESSION_TTL_HOURS=24` or less

#### 2. Infrastructure Security
- [ ] Enable HTTPS (SSL/TLS certificate)
- [ ] Configure reverse proxy (nginx/Apache)
- [ ] Set up firewall rules
- [ ] Enable database backups
- [ ] Configure log rotation

#### 3. Application Security
- [ ] Review rate limiting settings
- [ ] Test authentication flows
- [ ] Verify CORS configuration
- [ ] Enable audit logging
- [ ] Remove/disable demo accounts

#### 4. Monitoring
- [ ] Set up error logging
- [ ] Configure health check endpoint (`/health`)
- [ ] Monitor failed login attempts
- [ ] Track API usage patterns

---

## 🔍 Security Testing

### Manual Testing:

#### 1. Authentication
```bash
# Test rate limiting
for i in {1..15}; do
  curl -X POST http://localhost:8000/make-server-32aa5c5c/auth/login \
    -H "Content-Type: application/json" \
    -d '{"email":"test@test.com","password":"wrong"}'
done
# Should return 429 after 10 attempts
```

#### 2. Session Expiry
```bash
# Login and get token
TOKEN=$(curl -X POST http://localhost:8000/make-server-32aa5c5c/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@demo.com","password":"password123"}' \
  | jq -r '.token')

# Test authenticated endpoint
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/make-server-32aa5c5c/auth/me
```

#### 3. CORS Validation
```bash
# Should reject unauthorized origin
curl -H "Origin: http://evil.com" \
  http://localhost:8000/make-server-32aa5c5c/health
# Should NOT include Access-Control-Allow-Origin header
```

---

## 🐛 Known Limitations (MVP)

### Current Limitations:
1. **No email verification** - Users auto-confirmed on registration
2. **No password reset** - Must contact admin for password recovery
3. **No 2FA** - Single factor authentication only
4. **No account lockout** - Rate limiting but no permanent lockout
5. **No audit logs** - Admin actions not logged (planned)
6. **Base64 image storage** - Should use cloud storage in production

### Planned Improvements:
- Email verification flow
- Password reset via email
- Two-factor authentication (2FA)
- Account lockout after repeated failures
- Comprehensive audit logging
- Cloud storage integration (Supabase Storage)

---

## 📞 Security Contact

For security issues or vulnerabilities, please report to the development team.

**DO NOT** disclose security vulnerabilities publicly without prior coordination.

---

## 📚 References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://docs.python.org/3/library/security.html)
- [Content Security Policy Guide](https://content-security-policy.com/)
- [PBKDF2 Recommendations](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---

**Last Updated**: April 2026
**Version**: 1.0
