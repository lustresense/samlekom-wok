# 🚀 QUICK START - Setup SIMRP Dalam 5 Menit

> **Panduan singkat untuk kontributor baru. Kalau masih bingung, baca README.md utama di root folder.**

---

## ⚡ 3 STEP SEDERHANA

### 1️⃣ Cek Prerequisites (1 menit)

Buka terminal, ketik:
```bash
node --version      # Harus v18+ (contoh: v20.10.0)
npm --version       # Harus 8+ (contoh: 9.6.4)
python --version    # Harus 3.10+ (contoh: 3.11.8)
```

**Kalau ada yang nggak keluar?** Install dulu:
- **Node.js**: https://nodejs.org (pilih LTS) → Restart komputer
- **Python**: https://www.python.org → Centang "Add Python to PATH" → Restart komputer

---

### 2️⃣ Download & Install (2 menit)

```bash
# Extract ZIP atau clone repo ke folder

cd Figmasimrp                  # Masuk folder
npm install                    # Download semua library (tunggu 2-5 menit)
```

✅ Kalau selesai, muncul: `added XXX packages`

---

### 3️⃣ Jalankan & Buka Browser (2 menit)

```bash
npm run dev        # Jalankan project
```

✅ Tunggu sampai terlihat:
```
VITE v6.3.5  ready in XXX ms

➜  Local:   http://localhost:5173/
```

**JANGAN TUTUP TERMINAL INI** - biarkan terbuka selamanya.

Buka browser ke: `http://localhost:5173`

🎉 **SELESAI!** Aplikasi sudah jalan.

---

## 🎮 CEPAT TEST

Login dengan akun demo siap pakai:

| Role | Email | Password | Test Apa |
|------|-------|----------|----------|
| Relawan | `relawan.demo@simrp.app` | `password123` | Ikut event, lihat ranking |
| Moderator | `moderator2.demo@simrp.app` | `password123` | Approve event, verify laporan |
| Admin | Admin page: `/admin` → `admin` / `admin` | - | God mode, manage semua |

---

## 🛠️ COMMAND PENTING

| Command | Apa |
|---------|-----|
| `npm run dev` | ✨ Jalankan selamanya (paling penting!) |
| `npm run dev:web` | Frontend doang (jarang) |
| `npm run api` | Backend doang (jarang) |
| `npm run build` | Build untuk production (deploy) |

---

## ❓ ADA ERROR?

1. **"command not found"** → Restart komputer
2. **Terminal error saat `npm install`** → Ulangi, cek internet
3. **Browser blank** → F12 → Console → baca error → screenshot di #dev-help
4. **Database error** → Jalankan:
   ```bash
   rm -rf database/runtime
   npm run dev
   ```

---

## 📚 DOKUMENTASI LENGKAP

**Baca README.md utama** (di root folder `Figmasimrp/`) untuk:
- ✅ Setup detail
- ✅ Semua demo account
- ✅ Troubleshooting lengkap
- ✅ Fitur-fitur penjelasan
- ✅ How to contribute

---

**Happy coding! 🚀**
Email: test@example.com
Password: password123
Kode Pos: 60111 (Keputih, Sukolilo)
```

---

## 📱 Testing Bottom Navigation

1. Login as user
2. Look at bottom of screen
3. Click each tab: **Home** → **Event** → **Profile** → **More**
4. ✅ Active tab should have **FULL YELLOW background** (#FDB913)

---

## 🎨 Visual Identity Check

### Primary Colors
- Green: `#0B6E4F` (Headers, buttons, primary actions)
- Yellow: `#FDB913` (Active states, highlights, CTAs)

### 4 Pillar Colors
- 🌱 Lingkungan: Green `#10B981`
- 🤝 Gotong Royong: Blue `#3B82F6`
- 💼 Ekonomi Kreatif: Orange `#F59E0B`
- 🛡️ Keamanan: Red `#EF4444`

---

## 🧪 Quick API Test

### Test Health Endpoint
```bash
curl https://YOUR_PROJECT_ID.supabase.co/functions/v1/make-server-32aa5c5c/health \
  -H "Authorization: Bearer YOUR_ANON_KEY"
```

Expected response:
```json
{"status":"ok"}
```

---

## 📦 Pre-Loaded Data

### 8 Sample Events
System automatically seeds 8 events on first load:
1. Kerja Bakti Lingkungan (Pilar 1)
2. Senam Pagi Sehat (Pilar 2)
3. Pelatihan UMKM Digital (Pilar 3)
4. Ronda Malam (Pilar 4)
5. Bazar UMKM (Pilar 3)
6. Penghijauan Pohon (Pilar 1)
7. Posyandu (Pilar 2)
8. Sosialisasi Bank Sampah (Pilar 1)

### Geographic Data
- 31 Kecamatan Surabaya
- 154 Kelurahan
- Full postal code mapping

---

## 🐛 Quick Troubleshooting

### Problem: Page is blank
**Solution:** Check console for errors. Ensure Supabase is connected.

### Problem: Kode pos not working
**Solution:** Only Surabaya postal codes (60xxx) are valid. Try: 60111, 60243, 60175

### Problem: Bottom nav not showing
**Solution:** Make sure you're logged in as user (not admin)

### Problem: Events not loading
**Solution:** Check localStorage for `simrp_db_seeded`. Clear it to re-seed.

### Problem: Can't login as admin
**Solution:** Use exact credentials: `admin` / `admin` (case-sensitive)

---

## 🔍 Quick Code Navigation

### Want to modify...
- **Landing page?** → `/src/app/components/LandingPage.tsx`
- **User dashboard?** → `/src/app/components/UserDashboard.tsx`
- **Admin panel?** → `/src/app/components/AdminDashboard.tsx`
- **Reporting wizard?** → `/src/app/components/ReportingWizard.tsx`
- **Geographic data?** → `/src/data/geographicData.ts`
- **Backend API?** → `/supabase/functions/server/index.tsx`
- **Colors/theme?** → `/src/styles/theme.css`
- **Fonts?** → `/src/styles/fonts.css`

---

## 📱 Mobile Testing

### Test on Mobile Device
1. Get your local IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. Access: `http://YOUR_IP:5173`
3. Test touch interactions
4. Test bottom navigation
5. Test photo upload (use device camera)

### Chrome DevTools Mobile Simulation
1. Press F12
2. Click device toolbar icon (or Ctrl+Shift+M)
3. Select "iPhone 12 Pro" or "Pixel 5"
4. Test all features

---

## 🎯 Success Checklist

After setup, verify these work:

- [ ] Landing page loads with Surabaya colors
- [ ] Admin login works (admin/admin)
- [ ] User registration works with postal code 60111
- [ ] Bottom navigation shows 4 tabs with yellow active state
- [ ] 8 events visible in Events tab
- [ ] Can join an event
- [ ] Can create a report with photo
- [ ] Admin can verify reports
- [ ] User gets points after verification
- [ ] Profile shows correct level and stats
- [ ] Offline mode shows WifiOff icon
- [ ] Toast notifications appear on actions

---

## 🚀 Next Steps After Quick Start

1. **Read Full Docs**: Check `README_SIMRP.md`
2. **User Manual**: Read `PETUNJUK_PENGGUNAAN.md` (Bahasa Indonesia)
3. **System Overview**: Check `../status/SYSTEM_SUMMARY.md`
4. **Test All Flows**: Use the testing scenarios above
5. **Customize**: Modify colors, text, or add features
6. **Deploy**: Follow deployment guide in README

---

## 📞 Need Help?

### Check Documentation
- Technical: `README_SIMRP.md`
- User Guide: `PETUNJUK_PENGGUNAAN.md`
- System Specs: `../status/SYSTEM_SUMMARY.md`

### Common Resources
- Supabase Docs: https://supabase.com/docs
- React Docs: https://react.dev
- Tailwind CSS: https://tailwindcss.com

---

## 🎉 You're Ready!

The system is fully functional. Start testing and customizing!

**Happy coding! 🚀**

---

**Built for Kota Surabaya** 🇮🇩  
**© 2025 Diskominfo Surabaya**
