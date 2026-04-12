# 👋 KONTRIBUTOR - Setup Guide (Super Simpel!)

> **Dibuat April 2026 - Didesain khusus biar kontributor tidak pusing**

---

## ⚡ TL;DR - Cukup 3 Command

```bash
npm install
npm run dev
# Buka: http://localhost:5173
```

**Done!** Aplikasi jalan. Edit file → browser otomatis refresh.

---

## 📖 DETAILED GUIDE (Kalau Masih Bingung)

### Before Start: Cek Prerequisites (1 menit)

Buka terminal, ketik:
```bash
node --version
npm --version
python --version
```

❌ Kalau ada error atau nggak keluar versi?
1. Download Node.js dari https://nodejs.org (button hijau besar "LTS")
2. Download Python dari https://www.python.org (PENTING: centang "Add Python to PATH")
3. Restart komputer
4. Ulangi cek di atas

✅ Semuanya berhasil? Lanjut ke step berikutnya.

---

### Step 1: Download Project (30 detik)

**Opsi A (dari GitHub):**
```bash
git clone <LINK_REPO>
cd Figmasimrp
```

**Opsi B (dari ZIP):**
1. Extract ZIP ke folder
2. Buka terminal, masuk ke folder:
```bash
cd path/ke/folder/Figmasimrp
```

---

### Step 2: Install Dependencies (2-5 menit)

Ketik:
```bash
npm install
```

**Terminal akan terlihat sibuk beberapa menit.** Ini normal. Tunggu sampai muncul:
```
added 1203 packages in 2m
```

✅ **Kalau berhasil**: Lanjut ke step 3.

❌ **Kalau ada error**:
- Cek internet (harus stabil)
- Ulangi `npm install`
- Kalau masih error, screenshot → tanyakan di #dev-help

---

### Step 3: Jalankan Project (1 menit)

Ketik:
```bash
npm run dev
```

**Tunggu sampai terminal menampilkan:**
```
VITE v6.3.5  ready in 456 ms

➜  Local:   http://localhost:5173/
```

**JANGAN TUTUP TERMINAL INI!** Biarkan terbuka selamanya saat develop.

---

### Step 4: Buka Browser

1. Buka browser (Chrome, Firefox, Edge, Opera, Safari, apapun)
2. Ketik di address bar: `http://localhost:5173`
3. Press Enter

🎉 **SELESAI!** Aplikasi sudah jalan.

---

## 🎮 Test Features Dengan Demo Account

Project sudah punya akun siap pakai. Cukup login:

### Username & Password Semua Demo Account
**Password semuanya sama:** `password123`

| Role | Email |
|------|-------|
| Relawan | `relawan.demo@simrp.app` |
| Moderator | `moderator2.demo@simrp.app` |
| Admin | Buka `/admin` → username: `admin` |

**Test apa**: Ikut event → lihat poin naik → enjoy!

---

## 💻 Edit Code & Lihat Perubahan

### Setiap kali buat perubahan di `src/` folder:
1. Save file (Ctrl+S)
2. Lihat browser otomatis refresh ✨
3. Perubahan langsung muncul!

### Kalau ubah Python backend (`server/main.py`):
1. Buka terminal yang lagi jalanin `npm run dev`
2. Tekan **Ctrl+C** (stop)
3. Ketik `npm run dev` lagi
4. Browser refresh manual

---

## ❓ Ada Error?

### Error 1: "command not found: npm" atau "python not found"
**Penyebab**: Belum install atau belum restart komputer
**Solusi**: 
1. Install Node.js & Python (lihat "Before Start")
2. Restart komputer
3. Ulangi cek versi

### Error 2: Terminal error pas `npm install`
**Penyebab**: Internet nggak stabil atau ada file conflict
**Solusi**:
1. Cek internet (fast.com)
2. Ulangi `npm install`
3. Kalau masih error:
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

### Error 3: Browser blank atau kelihatan error
**Penyebab**: JavaScript error di browser
**Solusi**:
1. Tekan **F12** (buka DevTools)
2. Klik tab **Console**
3. Cari error message yang berwarna merah
4. Baca error → buka file yang bermasalah → baca code
5. Kalau nggak bisa, screenshot error → tanyakan di #dev-help

### Error 4: Port 5173 atau 8000 sudah dipakai
**Penyebab**: Aplikasi lain pakai port yang sama
**Solusi**:
1. Tutup aplikasi lain yang pakai port itu
2. Atau jalankan `npm run dev` di folder lain

### Error 5: Database corrupted
**Gejala**: Error tentang "database", atau "Cannot read property"
**Solusi**:
```bash
rm -rf database/runtime
npm run dev
```
Database akan di-generate ulang otomatis.

---

## 🔄 Sehari-Hari Workflow

**Pagi (mulai develop):**
1. Buka folder project di terminal
2. Ketik `npm run dev`
3. Buka `http://localhost:5173` di browser
4. Mulai edit code

**Siang (while developing):**
- Edit file di `src/` → Save → Browser refresh otomatis
- Pakai browser DevTools (F12) untuk debug
- Test dengan demo account

**Malam (selesai):**
1. Tekan **Ctrl+C** di terminal (stop)
2. Commit code: 
   ```bash
   git add .
   git commit -m "Add feature XYZ"
   git push origin branch-name
   ```

---

## 🏆 Contribute

### Step untuk submit code ke project:

1. **Fork repository** di GitHub (buat copy)
2. **Clone fork kamu**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Figmasimrp.git
   ```
3. **Buat branch baru**:
   ```bash
   git checkout -b feature-nama-fitur
   ```
4. **Code menggunakan `npm run dev`** (test setiap saat)
5. **Commit**:
   ```bash
   git commit -m "Add: clear feature description"
   ```
6. **Push**:
   ```bash
   git push origin feature-nama-fitur
   ```
7. **Buat Pull Request** (PR) di GitHub dengan deskripsi detail

**PR akan di-review sebelum merge ke main.**

---

## 🆘 STUCK?

### Langkah sebelum nanya:

1. **Baca** README.md utama (di root folder)
2. **Google** error message (copy-paste paste error ke Google)
3. **Cek** console (F12 → Console tab) untuk error
4. **Screenshot** terminal error → paste di #dev-help

### Informasi yang helpful saat nanya:
- Screenshot error (terminal + console browser)
- Apa yang kamu lakukan pas error terjadi
- Sudah coba apa aja?
- OS kamu (Windows/Mac/Linux)?
- Node/Python version? (ketik `node --version`, `python --version`)

---

## 📚 Dokumentasi Lengkap

**Main README.md**: `/README.md` - Dokumentasi lengkap semua fitur

**Key Sections**:
- 🚀 Quick Start (3 langkah)
- 👥 Demo Accounts (6 akun siap pakai)
- 🎯 Fitur Utama (penjelasan feature)
- 🏗️ Arsitektur (tech stack)
- 🧪 Testing Fitur (cara test setiap role)
- 🛠️ Developer Commands (semua command)
- 🏆 Contributing (PR workflow)

---

**Selamat! Kamu ready jadi kontributor! 🚀**

*Happy Coding!* 💻✨
