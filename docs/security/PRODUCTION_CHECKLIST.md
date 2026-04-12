# Production Deployment Checklist - SIMRP

## 📋 Pre-Deployment Checklist

### 1. Environment Configuration

#### Create `.env.local` file:
```bash
# Copy from .env.example
cp .env.example .env.local
```

#### Required Production Settings:
```bash
# CRITICAL: Set to production
SIMRP_ENV=production

# CRITICAL: Strong admin credentials (min 16 characters)
SIMRP_ADMIN_LOGIN_USERNAME=admin_surabaya
SIMRP_ADMIN_PASSWORD=Str0ng!P@ssw0rd#2026#Secure

# CRITICAL: Increase password hashing iterations
SIMRP_PBKDF2_ITERATIONS=600000

# CRITICAL: Shorter session lifetime
SIMRP_SESSION_TTL_HOURS=12

# CRITICAL: Your production domain
SIMRP_ALLOWED_ORIGINS=https://simrp.surabaya.go.id

# Optional: Custom admin seed password (for database seeding)
SIMRP_SEED_ADMIN_PASSWORD=

# Database path (default is usually fine)
SIMRP_DB_PATH=/var/lib/simrp/database.db

# Rate limiting (adjust based on expected traffic)
SIMRP_RATE_LIMIT_WINDOW_SECONDS=60
SIMRP_RATE_LIMIT_AUTH_MAX=10
SIMRP_RATE_LIMIT_MUTATION_MAX=200
SIMRP_MAX_BODY_BYTES=8388608
```

---

### 2. Server Requirements

#### Minimum Specifications:
- **CPU**: 2 cores
- **RAM**: 2 GB
- **Storage**: 10 GB SSD
- **OS**: Linux (Ubuntu 20.04+ recommended) or Windows Server

#### Software Requirements:
- **Python**: 3.10 or higher
- **Node.js**: 18 or higher
- **npm**: 8 or higher

---

### 3. Infrastructure Setup

#### HTTPS/SSL Certificate
```bash
# Using Let's Encrypt (free)
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d simrp.surabaya.go.id

# Or configure your SSL certificate in reverse proxy
```

#### Reverse Proxy (nginx example):
```nginx
server {
    listen 80;
    server_name simrp.surabaya.go.id;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name simrp.surabaya.go.id;

    ssl_certificate /etc/letsencrypt/live/simrp.surabaya.go.id/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/simrp.surabaya.go.id/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        proxy_pass http://127.0.0.1:5173;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location /make-server-32aa5c5c/ {
        proxy_pass http://127.0.0.1:8000/make-server-32aa5c5c/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

### 4. Deployment Steps

#### Step 1: Install Dependencies
```bash
# Install Python dependencies (if any)
# Install Node.js dependencies
npm ci --production
```

#### Step 2: Build Frontend
```bash
npm run build
```

#### Step 3: Set Environment Variables
```bash
# Option A: Export in shell
export SIMRP_ENV=production
export SIMRP_ADMIN_LOGIN_USERNAME=admin_surabaya
export SIMRP_ADMIN_PASSWORD=Str0ng!P@ssw0rd#2026#Secure
# ... other variables

# Option B: Use .env.local file (recommended)
# Edit .env.local with production values
```

#### Step 4: Start Services

**Option A: Manual Start**
```bash
# Terminal 1: Start API server
python server/local_api.py &

# Terminal 2: Serve built files (nginx recommended for production)
# Or use a simple static file server
npx serve dist -l 5173
```

**Option B: Systemd Service (Linux)**

Create `/etc/systemd/system/simrp-api.service`:
```ini
[Unit]
Description=SIMRP API Server
After=network.target

[Service]
Type=simple
User=simrp
WorkingDirectory=/opt/simrp
Environment="SIMRP_ENV=production"
EnvironmentFile=/opt/simrp/.env.local
ExecStart=/usr/bin/python3 /opt/simrp/server/local_api.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable simrp-api
sudo systemctl start simrp-api
sudo systemctl status simrp-api
```

---

### 5. Database Backup Strategy

#### Automated Backups (cron job):
```bash
# Add to crontab (daily backup at 2 AM)
0 2 * * * cp /opt/simrp/database/runtime/database.db /opt/simrp/database/backups/backup-$(date +\%Y\%m\%d).db

# Keep only last 30 days
0 3 * * * find /opt/simrp/database/backups -name "*.db" -mtime +30 -delete
```

#### Manual Backup:
```bash
# Create backup
cp database/runtime/database.db database/backups/backup-$(date +%Y%m%d-%H%M%S).db

# Restore from backup
cp database/backups/backup-YYYYMMDD-HHMMSS.db database/runtime/database.db
```

---

### 6. Security Hardening

#### File Permissions:
```bash
# Set restrictive permissions
chmod 750 /opt/simrp
chmod 640 /opt/simrp/.env.local
chmod 640 database/runtime/database.db
chown -R simrp:simrp /opt/simrp
```

#### Firewall Configuration:
```bash
# UFW (Ubuntu)
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 80/tcp    # HTTP (for Let's Encrypt)
sudo ufw allow 443/tcp   # HTTPS
sudo ufw enable

# Or configure your firewall accordingly
```

#### Disable Demo Accounts (Optional):
```bash
# Set a seed password to prevent default demo passwords
SIMRP_SEED_ADMIN_PASSWORD=YourCustomSeedPassword123!
```

---

### 7. Monitoring Setup

#### Health Check Endpoint:
```bash
# Test health endpoint
curl https://simrp.surabaya.go.id/make-server-32aa5c5c/health

# Expected: {"status":"ok"}
```

#### Log Monitoring:
```bash
# View API logs (if using systemd)
sudo journalctl -u simrp-api -f

# Or check application logs
tail -f /var/log/simrp/api.log
```

#### Uptime Monitoring:
- Set up uptime monitoring (UptimeRobot, Pingdom, etc.)
- Monitor endpoint: `/make-server-32aa5c5c/health`
- Recommended check interval: 5 minutes

---

### 8. Testing Before Go-Live

#### Functional Tests:
```bash
# 1. Health check
curl https://simrp.surabaya.go.id/make-server-32aa5c5c/health

# 2. Admin login test
curl -X POST https://simrp.surabaya.go.id/make-server-32aa5c5c/auth/admin-login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin_surabaya","password":"Str0ng!P@ssw0rd#2026#Secure"}'

# 3. User registration test
curl -X POST https://simrp.surabaya.go.id/make-server-32aa5c5c/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","password":"Test123!","kelurahan":"Keputih"}'

# 4. CORS test (should reject)
curl -H "Origin: http://evil.com" \
  https://simrp.surabaya.go.id/make-server-32aa5c5c/health
# Should NOT include Access-Control-Allow-Origin header
```

#### Load Testing (Optional):
```bash
# Install Apache Bench
sudo apt install apache2-utils

# Test with 100 requests, 10 concurrent
ab -n 100 -c 10 https://simrp.surabaya.go.id/make-server-32aa5c5c/health
```

---

### 9. Go-Live Checklist

- [ ] All environment variables set correctly
- [ ] HTTPS certificate installed and valid
- [ ] Reverse proxy configured
- [ ] Database backups automated
- [ ] Monitoring set up
- [ ] Admin credentials changed from defaults
- [ ] Demo accounts disabled or secured
- [ ] Firewall configured
- [ ] Health check passing
- [ ] All functional tests passing
- [ ] Log rotation configured
- [ ] Emergency contact information documented

---

### 10. Post-Deployment

#### Immediate Actions:
1. Verify all endpoints are accessible
2. Test login flows (admin, moderator, user)
3. Test event creation and approval flow
4. Test report submission and verification
5. Check leaderboard functionality

#### First Week:
1. Monitor error logs daily
2. Check database size growth
3. Monitor failed login attempts
4. Review rate limiting effectiveness
5. Gather user feedback

#### Ongoing Maintenance:
1. Weekly: Review logs for anomalies
2. Weekly: Verify backups are working
3. Monthly: Update dependencies
4. Monthly: Review security settings
5. Quarterly: Full security audit

---

### 11. Rollback Plan

If deployment fails:

```bash
# 1. Stop services
sudo systemctl stop simrp-api

# 2. Restore previous database backup
cp database/backups/previous-backup.db database/runtime/database.db

# 3. Revert code (if using git)
git checkout previous-version

# 4. Rebuild
npm run build

# 5. Restart
sudo systemctl start simrp-api
```

---

### 12. Emergency Contacts

| Role | Name | Contact |
|------|------|---------|
| System Admin | [Name] | [Phone/Email] |
| Database Admin | [Name] | [Phone/Email] |
| Security Team | [Name] | [Phone/Email] |
| Development Lead | [Name] | [Phone/Email] |

---

## 📞 Support

For deployment issues, refer to:
- Technical Documentation: `docs/guides/README_SIMRP.md`
- Security Guide: `docs/security/SECURITY.md`
- User Manual: `docs/guides/PETUNJUK_PENGGUNAAN.md`

---

**Last Updated**: April 2026
**Version**: 1.0
