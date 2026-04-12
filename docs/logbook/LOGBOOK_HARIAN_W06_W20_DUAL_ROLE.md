# LOGBOOK HARIAN W06-W20 (DUA ORANG, RINCI PER PIC)
## SIMREKAP - Format Harian Day 26 sampai Day 100

Komposisi tim:
- Farchan: `UX + Backend`
- Ikram: `UI Design + Frontend`

Aturan isi harian:
- Setiap Day berisi 2 entri terpisah: `Farchan` dan `Ikram`.
- Masing-masing entri wajib punya `Aktivitas`, `Uraian Kegiatan`, `Output`, dan `Lampiran` sendiri.
- Status default semua Day: `[RENCANA]` lalu diubah ke `[TERLAKSANA]` saat selesai.

## Validasi Kalender W06-W20 (5 Hari Kerja per Pekan)
| Week | Day ID | Rentang Tanggal | Hari Kerja |
|---|---|---|---|
| W06 | D26-D30 | 2 Mar - 6 Mar 2026 | Senin-Jumat |
| W07 | D31-D35 | 9 Mar - 13 Mar 2026 | Senin-Jumat |
| W08 | D36-D40 | 16 Mar - 20 Mar 2026 | Senin-Jumat |
| W09 | D41-D45 | 23 Mar - 27 Mar 2026 | Senin-Jumat |
| W10 | D46-D50 | 30 Mar - 3 Apr 2026 | Senin-Jumat |
| W11 | D51-D55 | 6 Apr - 10 Apr 2026 | Senin-Jumat |
| W12 | D56-D60 | 13 Apr - 17 Apr 2026 | Senin-Jumat |
| W13 | D61-D65 | 20 Apr - 24 Apr 2026 | Senin-Jumat |
| W14 | D66-D70 | 27 Apr - 1 Mei 2026 | Senin-Jumat |
| W15 | D71-D75 | 4 Mei - 8 Mei 2026 | Senin-Jumat |
| W16 | D76-D80 | 11 Mei - 15 Mei 2026 | Senin-Jumat |
| W17 | D81-D85 | 18 Mei - 22 Mei 2026 | Senin-Jumat |
| W18 | D86-D90 | 25 Mei - 29 Mei 2026 | Senin-Jumat |
| W19 | D91-D95 | 1 Jun - 5 Jun 2026 | Senin-Jumat |
| W20 | D96-D100 | 8 Jun - 12 Jun 2026 | Senin-Jumat |

Referensi sinkron wajib:
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md`
- `docs/logbook/PROJECT_MANAGEMENT_15_WEEKS_SIMREKAP.md`
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md`
- `docs/logbook/logbook.md`
- `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv`

## PEKAN 6 (W06): Pra-Produksi Final

Status Pekan: Proyeksi
Milestone Aktif: M1: PREPARATION (W06)
Task Utama: Farchan - API Contract & Scope Definition | Ikram - UI Audit & Component Mapping

### Day 26 (Senin, 2 Mar 2026): Freeze scope MVP dan audit screen map
Status: [RENCANA]
Milestone/Group: M1: PREPARATION (W06)
Task Referensi Farchan: API Contract & Scope Definition
Task Referensi Ikram: UI Audit & Component Mapping

#### Entri Farchan (UX+Backend)
Aktivitas: Freeze scope MVP dan rapikan backlog prioritas.
Uraian Kegiatan (Logbook):
"Saya mulai hari ini dengan nge-lock batas MVP backend supaya sprint berikutnya tidak melebar. Fokus saya ada di prioritas domain auth, event, dan report, lalu saya urutkan backlog berdasarkan dependency integrasi FE-BE (mana yang wajib jadi duluan dan mana yang bisa menyusul). Setelah itu saya kunci scope yang masuk sprint W07 dan menandai item non-MVP sebagai backlog parkir, jadi tim punya batas kerja yang jelas untuk eksekusi."
Output Farchan:
- Scope MVP backend dikunci ke alur inti `auth -> event -> report` tanpa menambah fitur baru di luar sprint.
- Backlog W06-W07 sudah diprioritaskan berdasarkan urutan dependency implementasi.
- Ada daftar item non-MVP yang diparkir untuk fase berikutnya supaya sprint tetap realistis.
- Bukti screenshot utama: `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv` baris 2: rincian D26 freeze scope MVP backend.
- Bukti screenshot pendukung 1: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 54: fokus W06 `Freeze MVP + final API contract`.
- Bukti screenshot pendukung 2: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 100: task W06 `Freeze MVP + acceptance criteria + API v1`.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv` baris 2: entri D26 freeze scope MVP dan audit backlog backend.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 54: fokus W06 sebagai fase freeze MVP.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 100: breakdown task W06 untuk track UX+BE.

#### Entri Ikram (UI+Frontend)
Aktivitas: Audit ulang screen Figma aktif dan mapping ke modul FE.
Uraian Kegiatan (Logbook):
"Saya audit ulang seluruh screen aktif dari Figma lalu saya cocokkan satu per satu ke modul FE yang sudah ada di kode. Fokusnya saya bikin peta yang jelas antara halaman public, auth gate, dan protected app shell supaya implementasi komponen tidak salah arah saat sprint berjalan. Dari audit ini saya tandai screen prioritas, screen yang belum punya komponen, dan screen yang bisa langsung dipakai jadi baseline sprint-ready."
Output Ikram:
- Screen map final sudah dibagi per zona: `Public`, `Auth Gate`, `Protected App Shell`.
- Mapping screen ke komponen FE sudah jelas untuk landing/login/register/dashboard.
- Ada daftar gap komponen yang perlu disiapkan sebelum sprint W07 dimulai.
- Bukti screenshot utama: `docs/architecture/SITEMAP_IA_SIMRP.md` baris 28-39: struktur sitemap public + protected shell.
- Bukti screenshot pendukung 1: `docs/guides/README_SIMRP.md` baris 145-157: mapping modul komponen FE utama.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 236-255: render route landing/login/register sebagai acuan screen mapping.
Lampiran Ikram (Bukti Screenshot):
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 28-39: pembagian halaman pada sitemap ringkas.
- `docs/guides/README_SIMRP.md` baris 145-157: daftar komponen frontend untuk mapping screen-to-component.
- `src/app/App.tsx` baris 236-255: implementasi route/page untuk landing, login, dan register.

### Day 27 (Selasa, 3 Mar 2026): API contract v1 dan baseline FE
Status: [RENCANA]
Milestone/Group: M1: PREPARATION (W06)
Task Referensi Farchan: API Contract & Scope Definition
Task Referensi Ikram: UI Audit & Component Mapping

#### Entri Farchan (UX+Backend)
Aktivitas: Finalkan API contract v1 untuk auth/event/report.
Uraian Kegiatan (Logbook):
"Saya hari ini fokus menyelesaikan kontrak API v1 untuk tiga domain inti: auth, events, dan reports. Saya cek ulang field wajib, format request/response, status code error, dan guard role supaya FE bisa integrasi tanpa nebak-nebak payload. Setelah itu saya rapikan endpoint matrix sebagai acuan implementasi sprint supaya semua request utama sudah punya kontrak yang konsisten."
Output Farchan:
- Kontrak endpoint auth (`signup/login/admin-login`) sudah final untuk kebutuhan sprint auth.
- Kontrak endpoint event create draft dan report submit sudah sinkron dengan validasi backend.
- Daftar endpoint inti sudah terdokumentasi sebagai referensi integrasi FE-BE.
- Bukti screenshot utama: `server/local_api.py` baris 1314-1398: route auth + validasi payload/error.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1498-1572: route create event draft beserta rule payload.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1658-1714: route submit report dan update participation.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1314-1398: kontrak endpoint `auth/signup`, `auth/login`, dan `auth/admin-login`.
- `server/local_api.py` baris 1498-1572: kontrak endpoint `POST /events` untuk draft event.
- `server/local_api.py` baris 1658-1714: kontrak endpoint `POST /reports` untuk submit laporan.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalkan design token dan setup struktur FE sprint-ready.
Uraian Kegiatan (Logbook):
"Saya menutup pekerjaan hari ini dengan merapikan baseline FE supaya siap masuk sprint implementasi. Pekerjaan utama saya adalah menegaskan pilihan library, struktur aset, dan alur route dasar agar komponen yang dibangun berikutnya konsisten dari sisi style maupun state behavior. Hasilnya jadi fondasi frontend yang rapi untuk langsung dipakai integrasi API v1."
Output Ikram:
- Baseline FE sudah terkunci: stack library utama, util styling, dan pola komponen.
- Struktur aset visual dan konvensi penempatan file FE sudah jelas.
- Routing awal app shell siap dipakai sebagai kerangka implementasi sprint.
- Bukti screenshot utama: `docs/LIBRARY_SELECTION.md` baris 10-23: daftar library inti FE yang dipakai.
- Bukti screenshot pendukung 1: `docs/ASSET_INVENTORY.md` baris 16-31: struktur aset + status inventaris awal.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 188-201: sinkronisasi route utama frontend.
Lampiran Ikram (Bukti Screenshot):
- `docs/LIBRARY_SELECTION.md` baris 10-23: baseline teknis library frontend.
- `docs/ASSET_INVENTORY.md` baris 16-31: standardisasi struktur aset UI/FE.
- `src/app/App.tsx` baris 188-201: route skeleton sebagai fondasi app shell.

### Day 28 (Rabu, 4 Mar 2026): Validasi design thinking artifact
Status: [RENCANA]
Milestone/Group: M1: PREPARATION (W06)
Task Referensi Farchan: ERD & Sprint Planning W07
Task Referensi Ikram: UI Audit & Component Mapping

#### Entri Farchan (UX+Backend)
Aktivitas: Finalisasi persona, journey map, dan problem framing.
Uraian Kegiatan (Logbook):
"Saya fokus merapikan artefak design thinking supaya tim punya acuan masalah dan kebutuhan pengguna yang tajam sebelum sprint coding penuh. Saya finalkan problem framing berdasarkan konteks kampung-centric, lalu saya turunkan ke persona dan alur journey yang nyambung ke fitur relawan, moderator, dan admin. Dengan itu keputusan backend yang diambil tetap berangkat dari kebutuhan user flow, bukan sekadar teknis endpoint."
Output Farchan:
- Problem statement dan konteks kampung-centric sudah final sebagai dasar keputusan fitur.
- Definisi persona/peran aktor sudah jelas untuk relawan, KSH, dan moderator.
- Journey utama user-moderator sudah dipetakan agar sinkron ke implementasi modul.
- Bukti screenshot utama: `docs/architecture/GRAND_DESIGN_FINAL.md` baris 26-33: masalah inti yang disasar sistem.
- Bukti screenshot pendukung 1: `docs/architecture/GRAND_DESIGN_FINAL.md` baris 47-55: definisi aktor relawan dan perannya.
- Bukti screenshot pendukung 2: `docs/architecture/SITEMAP_IA_SIMRP.md` baris 21-26: alur utama user/moderator/admin.
Lampiran Farchan (Bukti Screenshot):
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 26-33: framing masalah operasional lapangan.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 47-55: peran relawan sebagai persona utama.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 21-26: alur utama per role pada IA final.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sinkronkan wireframe akhir ke struktur komponen FE.
Uraian Kegiatan (Logbook):
"Saya sinkronkan wireframe final ke struktur komponen frontend supaya tidak ada gap antara desain dan implementasi. Saya mapping tiap alur utama ke komponen nyata di kode, termasuk route auth, dashboard, dan panel moderator, lalu saya cek state-state penting yang harus muncul di FE. Hasilnya jadi component map yang jelas untuk dipakai saat slicing dan integrasi di sprint berikutnya."
Output Ikram:
- Component map FE final sudah mencakup halaman public, auth, user dashboard, dan moderator panel.
- Mapping wireframe ke komponen existing sudah diverifikasi untuk alur inti sprint.
- Catatan gap komponen prioritas sudah disiapkan sebagai backlog implementasi FE.
- Bukti screenshot utama: `docs/guides/README_SIMRP.md` baris 145-157: daftar komponen FE hasil mapping wireframe.
- Bukti screenshot pendukung 1: `src/app/App.tsx` baris 236-275: mapping render route ke halaman/komponen utama.
- Bukti screenshot pendukung 2: `src/app/components/ModeratorDashboard.tsx` baris 188-215: struktur komponen input event moderator.
Lampiran Ikram (Bukti Screenshot):
- `docs/guides/README_SIMRP.md` baris 145-157: daftar komponen frontend utama.
- `src/app/App.tsx` baris 236-275: implementasi pemetaan route ke komponen.
- `src/app/components/ModeratorDashboard.tsx` baris 188-215: komponen form event untuk flow moderator.

### Day 29 (Kamis, 5 Mar 2026): Acceptance criteria sprint 1
Status: [RENCANA]
Milestone/Group: M1: PREPARATION (W06)
Task Referensi Farchan: ERD & Sprint Planning W07
Task Referensi Ikram: Setup Repo & App Shell

#### Entri Farchan (UX+Backend)
Aktivitas: Tetapkan acceptance criteria dan DoD untuk fitur sprint 1.
Uraian Kegiatan (Logbook):
"Hari ini saya pecah fitur sprint 1 menjadi acceptance criteria yang bisa diuji satu per satu. Saya tulis indikator selesai untuk alur auth, event, dan report, lalu saya sinkronkan dengan milestone harian biar tidak ada task yang kabur atau overlap. Hasil akhirnya adalah DoD yang operasional untuk dipakai tim saat develop dan saat review hasil harian."
Output Farchan:
- DoD sprint 1 backend disusun per domain (auth, event, report) dengan kriteria lulus yang terukur.
- Acceptance criteria harian untuk D29 ditetapkan agar sinkron dengan target milestone W06.
- Checklist evaluasi sprint sudah siap dipakai untuk retest dan review implementasi.
- Bukti screenshot utama: `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv` baris 3: entri D29 `Tetapkan acceptance criteria sprint 1`.
- Bukti screenshot pendukung 1: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 100: task W06 mencantumkan acceptance criteria.
- Bukti screenshot pendukung 2: `docs/logbook/PROJECT_MANAGEMENT_15_WEEKS_SIMREKAP.md` baris 80: task W06 (15 pekan) untuk freeze scope + acceptance criteria + API v1.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv` baris 3: evidence task D29 acceptance criteria sprint 1.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 100: acceptance criteria muncul di task inti W06.
- `docs/logbook/PROJECT_MANAGEMENT_15_WEEKS_SIMREKAP.md` baris 80: sinkron task W06 pada plan 15 pekan.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement route skeleton dan state dasar app shell.
Uraian Kegiatan (Logbook):
"Saya implement kerangka route dan state inti app shell supaya transisi antar halaman dasar sudah jalan. Fokus implementasi ada di setup current page, auth state, dan sinkronisasi URL supaya behavior aplikasi konsisten saat user pindah halaman. Setelah itu saya tes flow dasar landing-login-register-dashboard untuk memastikan shell siap dipakai sprint implementasi fitur."
Output Ikram:
- Route skeleton app sudah aktif untuk halaman public, auth, dan dashboard.
- State dasar app shell (`currentPage`, `currentUser`, `authToken`, `currentView`) sudah terpasang.
- Sinkronisasi route browser dan render komponen sudah tervalidasi untuk flow awal.
- Bukti screenshot utama: `src/app/App.tsx` baris 34-41: state dasar app shell.
- Bukti screenshot pendukung 1: `src/app/App.tsx` baris 88-107: sinkronisasi path URL ke page state.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 236-275: render route landing/auth/dashboard.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 34-41: deklarasi state utama app shell.
- `src/app/App.tsx` baris 88-107: logika route guard dan path mapping.
- `src/app/App.tsx` baris 236-275: output render komponen per halaman.

### Day 30 (Jumat, 6 Mar 2026): Sprint planning W07
Status: [RENCANA]
Milestone/Group: M1: PREPARATION (W06)
Task Referensi Farchan: ERD & Sprint Planning W07
Task Referensi Ikram: Setup Repo & App Shell

#### Entri Farchan (UX+Backend)
Aktivitas: Kunci sprint planning W07 dan risk register.
Uraian Kegiatan (Logbook):
"Saya menutup pekan ini dengan finalisasi sprint planning W07 dan daftar risiko eksekusi. Saya review dependency antar task backend, menentukan urutan kerja yang paling aman, lalu menandai risiko utama integrasi agar ada mitigasi sejak awal sprint. Hasilnya backlog W07 jadi lebih siap eksekusi karena urutan kerja, kapasitas, dan potensi hambatan sudah dipetakan."
Output Farchan:
- Backlog sprint W07 sudah terkunci dengan urutan prioritas eksekusi backend.
- Risk register awal sprint tersusun untuk risiko integrasi auth dan session flow.
- Rencana kerja W07 sudah sinkron antara plan 20 pekan, plan 15 pekan, dan milestone detail.
- Bukti screenshot utama: `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv` baris 3: entri D30 `Kunci risk register dan sprint planning W07`.
- Bukti screenshot pendukung 1: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 55: fokus W07 `Auth dan role guard`.
- Bukti screenshot pendukung 2: `docs/logbook/PROJECT_MANAGEMENT_15_WEEKS_SIMREKAP.md` baris 40: fokus W07 pada roadmap 15 pekan.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv` baris 3: bukti task D30 untuk lock sprint planning W07.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 55: target W07 sebagai tujuan sprint berikutnya.
- `docs/logbook/PROJECT_MANAGEMENT_15_WEEKS_SIMREKAP.md` baris 40: validasi fokus W07 pada plan sinkron.

#### Entri Ikram (UI+Frontend)
Aktivitas: Final review readiness UI+FE untuk sprint berikutnya.
Uraian Kegiatan (Logbook):
"Di akhir pekan saya review kesiapan UI+FE sebelum masuk sprint W07, terutama untuk flow auth dan kerangka dashboard. Saya cek apakah route, state dasar, dan komponen prioritas sudah cukup stabil untuk dipakai integrasi endpoint minggu depan. Dari review ini saya menghasilkan checklist readiness yang jelas, termasuk bagian yang sudah siap dan bagian yang harus dipantau saat sprint berjalan."
Output Ikram:
- Checklist readiness UI/FE sprint W07 sudah disusun berbasis komponen yang benar-benar aktif.
- Flow dasar app (landing/login/register/dashboard) sudah lolos review fungsional awal.
- Catatan area rawan rework sudah ditandai untuk dipantau pada saat integrasi auth.
- Bukti screenshot utama: `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv` baris 5: entri D30 `Final review readiness UI/FE sprint 1`.
- Bukti screenshot pendukung 1: `src/app/App.tsx` baris 236-275: status render halaman inti untuk readiness check.
- Bukti screenshot pendukung 2: `docs/LIBRARY_SELECTION.md` baris 33-37: keputusan jalur komponen/notifikasi/chart yang dipakai di sprint.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv` baris 5: bukti task D30 readiness UI/FE.
- `src/app/App.tsx` baris 236-275: kondisi route/page yang direview untuk sprint readiness.
- `docs/LIBRARY_SELECTION.md` baris 33-37: standar library aktif sebagai acuan stabilitas UI/FE.

## PEKAN 7 (W07): Auth dan Role Guard

Status Pekan: Proyeksi
Milestone Aktif: M2: AUTH SYSTEM (W07)
Task Utama: Farchan - API Login, Register & Session | Ikram - Slicing UI & Integrasi Login

### Day 31 (Senin, 9 Mar 2026): Validasi login register
Status: [RENCANA]
Milestone/Group: M2: AUTH SYSTEM (W07)
Task Referensi Farchan: API Login, Register & Session
Task Referensi Ikram: Slicing UI & Integrasi Login

#### Entri Farchan (UX+Backend)
Aktivitas: Implement validasi signup/login backend.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement validasi signup/login backend pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Flow login/register jalan' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Flow login/register jalan.
- Aktivitas yang diselesaikan: Implement validasi signup/login backend.
- Bukti screenshot utama: `server/local_api.py` baris 269-281: `create_session()` dan token generation.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 978-979: endpoint `GET /auth/me` untuk validasi token aktif.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1211-1291: validasi payload dan guard endpoint auth.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 269-281: `create_session()` dan token generation.
- `server/local_api.py` baris 978-979: endpoint `GET /auth/me` untuk validasi token aktif.
- `server/local_api.py` baris 1211-1291: validasi payload dan guard endpoint auth.

#### Entri Ikram (UI+Frontend)
Aktivitas: Desain state auth loading-error-success dan implement form FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Desain state auth loading-error-success dan implement form FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Flow login/register jalan' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Flow login/register jalan.
- Aktivitas yang diselesaikan: Desain state auth loading-error-success dan implement form FE.
- Bukti screenshot utama: `src/app/components/LoginPage.tsx` baris 99-103: rendering error state login.
- Bukti screenshot pendukung 1: `src/app/components/RegisterPage.tsx` baris 154-170: submit register dan auto-login flow.
- Bukti screenshot pendukung 2: `src/app/components/RegisterPage.tsx` baris 224-227: error feedback pada form register.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 99-103: rendering error state login.
- `src/app/components/RegisterPage.tsx` baris 154-170: submit register dan auto-login flow.
- `src/app/components/RegisterPage.tsx` baris 224-227: error feedback pada form register.

### Day 32 (Selasa, 10 Mar 2026): Session dan route guard
Status: [RENCANA]
Milestone/Group: M2: AUTH SYSTEM (W07)
Task Referensi Farchan: API Login, Register & Session
Task Referensi Ikram: Slicing UI & Integrasi Login

#### Entri Farchan (UX+Backend)
Aktivitas: Implement session, auth me, dan logout backend.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement session, auth me, dan logout backend pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Session flow stabil' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Session flow stabil.
- Aktivitas yang diselesaikan: Implement session, auth me, dan logout backend.
- Bukti screenshot utama: `server/local_api.py` baris 978-979: endpoint `GET /auth/me` untuk validasi token aktif.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1211-1291: validasi payload dan guard endpoint auth.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 24-26 dan 120: security policy, rate-limit default, dan konstanta API.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 978-979: endpoint `GET /auth/me` untuk validasi token aktif.
- `server/local_api.py` baris 1211-1291: validasi payload dan guard endpoint auth.
- `server/local_api.py` baris 24-26 dan 120: security policy, rate-limit default, dan konstanta API.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi token storage dan route guard FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi token storage dan route guard FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Session flow stabil' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Session flow stabil.
- Aktivitas yang diselesaikan: Integrasi token storage dan route guard FE.
- Bukti screenshot utama: `src/app/components/RegisterPage.tsx` baris 154-170: submit register dan auto-login flow.
- Bukti screenshot pendukung 1: `src/app/components/RegisterPage.tsx` baris 224-227: error feedback pada form register.
- Bukti screenshot pendukung 2: `src/app/components/AdminLoginPage.tsx` baris 28-36: auth flow halaman admin.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/RegisterPage.tsx` baris 154-170: submit register dan auto-login flow.
- `src/app/components/RegisterPage.tsx` baris 224-227: error feedback pada form register.
- `src/app/components/AdminLoginPage.tsx` baris 28-36: auth flow halaman admin.

### Day 33 (Rabu, 11 Mar 2026): Permission per role
Status: [RENCANA]
Milestone/Group: M2: AUTH SYSTEM (W07)
Task Referensi Farchan: RBAC & Error Handling Auth
Task Referensi Ikram: Role Routing & Handling FE

#### Entri Farchan (UX+Backend)
Aktivitas: Implement mapping permission per role.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement mapping permission per role pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Role-based view aktif' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Role-based view aktif.
- Aktivitas yang diselesaikan: Implement mapping permission per role.
- Bukti screenshot utama: `server/local_api.py` baris 1211-1291: validasi payload dan guard endpoint auth.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 24-26 dan 120: security policy, rate-limit default, dan konstanta API.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1835-1866: auth guard pada method update/delete lintas role.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1211-1291: validasi payload dan guard endpoint auth.
- `server/local_api.py` baris 24-26 dan 120: security policy, rate-limit default, dan konstanta API.
- `server/local_api.py` baris 1835-1866: auth guard pada method update/delete lintas role.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sesuaikan menu UI per role dan conditional rendering FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Sesuaikan menu UI per role dan conditional rendering FE dalam konteks 'Permission per role'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M2: AUTH SYSTEM (W07). Hasil 'Role-based view aktif' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Role-based view aktif.
- Aktivitas yang diselesaikan: Sesuaikan menu UI per role dan conditional rendering FE.
- Bukti screenshot utama: `src/app/components/RegisterPage.tsx` baris 224-227: error feedback pada form register.
- Bukti screenshot pendukung 1: `src/app/components/AdminLoginPage.tsx` baris 28-36: auth flow halaman admin.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 135-145: role guard dan session assignment setelah login.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/RegisterPage.tsx` baris 224-227: error feedback pada form register.
- `src/app/components/AdminLoginPage.tsx` baris 28-36: auth flow halaman admin.
- `src/app/App.tsx` baris 135-145: role guard dan session assignment setelah login.

### Day 34 (Kamis, 12 Mar 2026): Standarisasi error auth
Status: [RENCANA]
Milestone/Group: M2: AUTH SYSTEM (W07)
Task Referensi Farchan: RBAC & Error Handling Auth
Task Referensi Ikram: Role Routing & Handling FE

#### Entri Farchan (UX+Backend)
Aktivitas: Stabilkan model error auth 400/401/429.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilkan model error auth 400/401/429 untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Error auth sinkron' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Deliverable utama hari ini: Error auth sinkron.
- Aktivitas yang diselesaikan: Stabilkan model error auth 400/401/429.
- Bukti screenshot utama: `server/local_api.py` baris 24-26 dan 120: security policy, rate-limit default, dan konstanta API.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1835-1866: auth guard pada method update/delete lintas role.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1314-1397: handler `auth/signup`, `auth/login`, dan `auth/admin-login`.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 24-26 dan 120: security policy, rate-limit default, dan konstanta API.
- `server/local_api.py` baris 1835-1866: auth guard pada method update/delete lintas role.
- `server/local_api.py` baris 1314-1397: handler `auth/signup`, `auth/login`, dan `auth/admin-login`.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement error handling auth di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement error handling auth di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Error auth sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Error auth sinkron.
- Aktivitas yang diselesaikan: Implement error handling auth di FE.
- Bukti screenshot utama: `src/app/components/AdminLoginPage.tsx` baris 28-36: auth flow halaman admin.
- Bukti screenshot pendukung 1: `src/app/App.tsx` baris 135-145: role guard dan session assignment setelah login.
- Bukti screenshot pendukung 2: `src/app/components/LoginPage.tsx` baris 37-43: submit login call ke API.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminLoginPage.tsx` baris 28-36: auth flow halaman admin.
- `src/app/App.tsx` baris 135-145: role guard dan session assignment setelah login.
- `src/app/components/LoginPage.tsx` baris 37-43: submit login call ke API.

### Day 35 (Jumat, 13 Mar 2026): Retest auth E2E
Status: [RENCANA]
Milestone/Group: M2: AUTH SYSTEM (W07)
Task Referensi Farchan: RBAC & Error Handling Auth
Task Referensi Ikram: Role Routing & Handling FE

#### Entri Farchan (UX+Backend)
Aktivitas: Retest auth end-to-end lintas role.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest auth end-to-end lintas role. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Auth lintas role stabil' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Auth lintas role stabil.
- Aktivitas yang diselesaikan: Retest auth end-to-end lintas role.
- Bukti screenshot utama: `server/local_api.py` baris 1835-1866: auth guard pada method update/delete lintas role.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1314-1397: handler `auth/signup`, `auth/login`, dan `auth/admin-login`.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 269-281: `create_session()` dan token generation.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1835-1866: auth guard pada method update/delete lintas role.
- `server/local_api.py` baris 1314-1397: handler `auth/signup`, `auth/login`, dan `auth/admin-login`.
- `server/local_api.py` baris 269-281: `create_session()` dan token generation.

#### Entri Ikram (UI+Frontend)
Aktivitas: Polish UI/FE auth dan catat defect.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Polish UI/FE auth dan catat defect dalam konteks 'Retest auth E2E'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M2: AUTH SYSTEM (W07). Hasil 'Auth lintas role stabil' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Auth lintas role stabil.
- Aktivitas yang diselesaikan: Polish UI/FE auth dan catat defect.
- Bukti screenshot utama: `src/app/App.tsx` baris 135-145: role guard dan session assignment setelah login.
- Bukti screenshot pendukung 1: `src/app/components/LoginPage.tsx` baris 37-43: submit login call ke API.
- Bukti screenshot pendukung 2: `src/app/components/LoginPage.tsx` baris 99-103: rendering error state login.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 135-145: role guard dan session assignment setelah login.
- `src/app/components/LoginPage.tsx` baris 37-43: submit login call ke API.
- `src/app/components/LoginPage.tsx` baris 99-103: rendering error state login.

## PEKAN 8 (W08): Event Draft Approval Publish

Status Pekan: Proyeksi
Milestone Aktif: M3: EVENT MODULE (W08)
Task Utama: Farchan - API Create & Edit Draft Event | Ikram - UI Form Event & List Draft

### Day 36 (Senin, 16 Mar 2026): Rule create event
Status: [RENCANA]
Milestone/Group: M3: EVENT MODULE (W08)
Task Referensi Farchan: API Create & Edit Draft Event
Task Referensi Ikram: UI Form Event & List Draft

#### Entri Farchan (UX+Backend)
Aktivitas: Validasi rule create event untuk scope pilar kuota.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Validasi rule create event untuk scope pilar kuota. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M3: EVENT MODULE (W08). Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Create event draft aktif' punya dasar teknis yang jelas."
Output Farchan:
- Deliverable utama hari ini: Create event draft aktif.
- Aktivitas yang diselesaikan: Validasi rule create event untuk scope pilar kuota.
- Bukti screenshot utama: `server/local_api.py` baris 1498-1572: `POST /events` create draft dan validasi scope.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1573-1597: approval/reject event dengan guard role.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1597-1629: endpoint join event dan validasi kuota/status.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1498-1572: `POST /events` create draft dan validasi scope.
- `server/local_api.py` baris 1573-1597: approval/reject event dengan guard role.
- `server/local_api.py` baris 1597-1629: endpoint join event dan validasi kuota/status.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalisasi UI form event dan implement submit FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalisasi UI form event dan implement submit FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Create event draft aktif' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Deliverable utama hari ini: Create event draft aktif.
- Aktivitas yang diselesaikan: Finalisasi UI form event dan implement submit FE.
- Bukti screenshot utama: `src/app/components/ModeratorDashboard.tsx` baris 190-214: payload create event dari FE.
- Bukti screenshot pendukung 1: `src/app/components/ModeratorDashboard.tsx` baris 166-170: action approve/reject event.
- Bukti screenshot pendukung 2: `src/app/components/ModeratorDashboard.tsx` baris 678-700: tombol approve/reject pada daftar draft.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 190-214: payload create event dari FE.
- `src/app/components/ModeratorDashboard.tsx` baris 166-170: action approve/reject event.
- `src/app/components/ModeratorDashboard.tsx` baris 678-700: tombol approve/reject pada daftar draft.

### Day 37 (Selasa, 17 Mar 2026): Draft event list
Status: [RENCANA]
Milestone/Group: M3: EVENT MODULE (W08)
Task Referensi Farchan: API Create & Edit Draft Event
Task Referensi Ikram: UI Form Event & List Draft

#### Entri Farchan (UX+Backend)
Aktivitas: Stabilkan endpoint create draft event.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilkan endpoint create draft event untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Draft list sinkron' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Deliverable utama hari ini: Draft list sinkron.
- Aktivitas yang diselesaikan: Stabilkan endpoint create draft event.
- Bukti screenshot utama: `server/local_api.py` baris 1573-1597: approval/reject event dengan guard role.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1597-1629: endpoint join event dan validasi kuota/status.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1629-1658: endpoint complete event dan transisi status.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1573-1597: approval/reject event dengan guard role.
- `server/local_api.py` baris 1597-1629: endpoint join event dan validasi kuota/status.
- `server/local_api.py` baris 1629-1658: endpoint complete event dan transisi status.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi daftar draft event moderator di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi daftar draft event moderator di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Draft list sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Draft list sinkron.
- Aktivitas yang diselesaikan: Integrasi daftar draft event moderator di FE.
- Bukti screenshot utama: `src/app/components/ModeratorDashboard.tsx` baris 166-170: action approve/reject event.
- Bukti screenshot pendukung 1: `src/app/components/ModeratorDashboard.tsx` baris 678-700: tombol approve/reject pada daftar draft.
- Bukti screenshot pendukung 2: `src/app/components/EventList.tsx` baris 42-43: trigger join event dari user.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 166-170: action approve/reject event.
- `src/app/components/ModeratorDashboard.tsx` baris 678-700: tombol approve/reject pada daftar draft.
- `src/app/components/EventList.tsx` baris 42-43: trigger join event dari user.

### Day 38 (Rabu, 18 Mar 2026): Approval reject flow
Status: [RENCANA]
Milestone/Group: M3: EVENT MODULE (W08)
Task Referensi Farchan: Logic Approval & Publish API
Task Referensi Ikram: UI Approval Flow & Status

#### Entri Farchan (UX+Backend)
Aktivitas: Implement endpoint approval/reject event.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement endpoint approval/reject event pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Approval flow aktif' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Approval flow aktif.
- Aktivitas yang diselesaikan: Implement endpoint approval/reject event.
- Bukti screenshot utama: `server/local_api.py` baris 1597-1629: endpoint join event dan validasi kuota/status.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1629-1658: endpoint complete event dan transisi status.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1185-1229: listing events/reports untuk sinkron dashboard.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1597-1629: endpoint join event dan validasi kuota/status.
- `server/local_api.py` baris 1629-1658: endpoint complete event dan transisi status.
- `server/local_api.py` baris 1185-1229: listing events/reports untuk sinkron dashboard.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement aksi approve/reject di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement aksi approve/reject di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Approval flow aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Approval flow aktif.
- Aktivitas yang diselesaikan: Implement aksi approve/reject di FE.
- Bukti screenshot utama: `src/app/components/ModeratorDashboard.tsx` baris 678-700: tombol approve/reject pada daftar draft.
- Bukti screenshot pendukung 1: `src/app/components/EventList.tsx` baris 42-43: trigger join event dari user.
- Bukti screenshot pendukung 2: `src/app/components/EventList.tsx` baris 169-175: state disabled berdasarkan kuota/status.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 678-700: tombol approve/reject pada daftar draft.
- `src/app/components/EventList.tsx` baris 42-43: trigger join event dari user.
- `src/app/components/EventList.tsx` baris 169-175: state disabled berdasarkan kuota/status.

### Day 39 (Kamis, 19 Mar 2026): Publish status event
Status: [RENCANA]
Milestone/Group: M3: EVENT MODULE (W08)
Task Referensi Farchan: Logic Approval & Publish API
Task Referensi Ikram: UI Approval Flow & Status

#### Entri Farchan (UX+Backend)
Aktivitas: Pastikan publish event sesuai status backend.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Pastikan publish event sesuai status backend pada konteks 'Publish status event'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M3: EVENT MODULE (W08). Setelah selesai, saya pastikan 'Event publish tampil benar' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Deliverable utama hari ini: Event publish tampil benar.
- Aktivitas yang diselesaikan: Pastikan publish event sesuai status backend.
- Bukti screenshot utama: `server/local_api.py` baris 1629-1658: endpoint complete event dan transisi status.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1185-1229: listing events/reports untuk sinkron dashboard.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 365-387: definisi tabel `events` dan relasi participation.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1629-1658: endpoint complete event dan transisi status.
- `server/local_api.py` baris 1185-1229: listing events/reports untuk sinkron dashboard.
- `server/local_api.py` baris 365-387: definisi tabel `events` dan relasi participation.

#### Entri Ikram (UI+Frontend)
Aktivitas: Update kartu event dan badge status FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Update kartu event dan badge status FE dalam konteks 'Publish status event'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M3: EVENT MODULE (W08). Hasil 'Event publish tampil benar' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Event publish tampil benar.
- Aktivitas yang diselesaikan: Update kartu event dan badge status FE.
- Bukti screenshot utama: `src/app/components/EventList.tsx` baris 42-43: trigger join event dari user.
- Bukti screenshot pendukung 1: `src/app/components/EventList.tsx` baris 169-175: state disabled berdasarkan kuota/status.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 49-50: fetch event list untuk user view.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: trigger join event dari user.
- `src/app/components/EventList.tsx` baris 169-175: state disabled berdasarkan kuota/status.
- `src/app/components/UserDashboard.tsx` baris 49-50: fetch event list untuk user view.

### Day 40 (Jumat, 20 Mar 2026): Uji E2E event governance
Status: [RENCANA]
Milestone/Group: M3: EVENT MODULE (W08)
Task Referensi Farchan: Logic Approval & Publish API
Task Referensi Ikram: UI Approval Flow & Status

#### Entri Farchan (UX+Backend)
Aktivitas: Uji E2E draft sampai approval sampai publish.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji E2E draft sampai approval sampai publish. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Event governance stabil' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Event governance stabil.
- Aktivitas yang diselesaikan: Uji E2E draft sampai approval sampai publish.
- Bukti screenshot utama: `server/local_api.py` baris 1185-1229: listing events/reports untuk sinkron dashboard.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 365-387: definisi tabel `events` dan relasi participation.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1498-1572: `POST /events` create draft dan validasi scope.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1185-1229: listing events/reports untuk sinkron dashboard.
- `server/local_api.py` baris 365-387: definisi tabel `events` dan relasi participation.
- `server/local_api.py` baris 1498-1572: `POST /events` create draft dan validasi scope.

#### Entri Ikram (UI+Frontend)
Aktivitas: Refinement UI/FE pasca uji alur event.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Refinement UI/FE pasca uji alur event dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Event governance stabil' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Deliverable utama hari ini: Event governance stabil.
- Aktivitas yang diselesaikan: Refinement UI/FE pasca uji alur event.
- Bukti screenshot utama: `src/app/components/EventList.tsx` baris 169-175: state disabled berdasarkan kuota/status.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 49-50: fetch event list untuk user view.
- Bukti screenshot pendukung 2: `src/app/components/ModeratorDashboard.tsx` baris 190-214: payload create event dari FE.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 169-175: state disabled berdasarkan kuota/status.
- `src/app/components/UserDashboard.tsx` baris 49-50: fetch event list untuk user view.
- `src/app/components/ModeratorDashboard.tsx` baris 190-214: payload create event dari FE.

## PEKAN 9 (W09): Participation Flow

Status Pekan: Proyeksi
Milestone Aktif: M4: PARTICIPATION (W09)
Task Utama: Farchan - API Join & History Partisipasi | Ikram - UI Button Join & History User

### Day 41 (Senin, 23 Mar 2026): Rule join event
Status: [RENCANA]
Milestone/Group: M4: PARTICIPATION (W09)
Task Referensi Farchan: API Join & History Partisipasi
Task Referensi Ikram: UI Button Join & History User

#### Entri Farchan (UX+Backend)
Aktivitas: Implement rule join event quota duplicate status.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement rule join event quota duplicate status pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Join flow valid' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Join flow valid.
- Aktivitas yang diselesaikan: Implement rule join event quota duplicate status.
- Bukti screenshot utama: `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 57-87: alur user ikut event dari UI.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1597-1629: join event rule (quota/duplicate/status).
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1629-1658: complete event dan validasi output summary.
Lampiran Farchan (Bukti Screenshot):
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 57-87: alur user ikut event dari UI.
- `server/local_api.py` baris 1597-1629: join event rule (quota/duplicate/status).
- `server/local_api.py` baris 1629-1658: complete event dan validasi output summary.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement tombol join dan state full closed.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement tombol join dan state full closed pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Join flow valid' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Join flow valid.
- Aktivitas yang diselesaikan: Implement tombol join dan state full closed.
- Bukti screenshot utama: `src/app/components/UserDashboard.tsx` baris 351-367: daftar event terpublish untuk attendance.
- Bukti screenshot pendukung 1: `src/app/components/EventList.tsx` baris 56-57: split event upcoming/completed di FE.
- Bukti screenshot pendukung 2: `src/app/components/EventList.tsx` baris 190-209: render tab completed events.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 351-367: daftar event terpublish untuk attendance.
- `src/app/components/EventList.tsx` baris 56-57: split event upcoming/completed di FE.
- `src/app/components/EventList.tsx` baris 190-209: render tab completed events.

### Day 42 (Selasa, 24 Mar 2026): Riwayat partisipasi
Status: [RENCANA]
Milestone/Group: M4: PARTICIPATION (W09)
Task Referensi Farchan: API Join & History Partisipasi
Task Referensi Ikram: UI Button Join & History User

#### Entri Farchan (UX+Backend)
Aktivitas: Implement endpoint riwayat partisipasi.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement endpoint riwayat partisipasi pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'History partisipasi tampil' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: History partisipasi tampil.
- Aktivitas yang diselesaikan: Implement endpoint riwayat partisipasi.
- Bukti screenshot utama: `server/local_api.py` baris 1597-1629: join event rule (quota/duplicate/status).
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1629-1658: complete event dan validasi output summary.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1185-1229: endpoint riwayat events/reports untuk user flow.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1597-1629: join event rule (quota/duplicate/status).
- `server/local_api.py` baris 1629-1658: complete event dan validasi output summary.
- `server/local_api.py` baris 1185-1229: endpoint riwayat events/reports untuk user flow.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi halaman riwayat partisipasi FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi halaman riwayat partisipasi FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'History partisipasi tampil' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: History partisipasi tampil.
- Aktivitas yang diselesaikan: Integrasi halaman riwayat partisipasi FE.
- Bukti screenshot utama: `src/app/components/EventList.tsx` baris 56-57: split event upcoming/completed di FE.
- Bukti screenshot pendukung 1: `src/app/components/EventList.tsx` baris 190-209: render tab completed events.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 74-85: aksi complete event oleh user/KSH.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 56-57: split event upcoming/completed di FE.
- `src/app/components/EventList.tsx` baris 190-209: render tab completed events.
- `src/app/components/UserDashboard.tsx` baris 74-85: aksi complete event oleh user/KSH.

### Day 43 (Rabu, 25 Mar 2026): Complete event oleh KSH
Status: [RENCANA]
Milestone/Group: M4: PARTICIPATION (W09)
Task Referensi Farchan: API Complete & Attendance
Task Referensi Ikram: UI Checklist & Complete Action

#### Entri Farchan (UX+Backend)
Aktivitas: Implement complete event oleh KSH.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement complete event oleh KSH pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Complete flow aktif' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Complete flow aktif.
- Aktivitas yang diselesaikan: Implement complete event oleh KSH.
- Bukti screenshot utama: `server/local_api.py` baris 1629-1658: complete event dan validasi output summary.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1185-1229: endpoint riwayat events/reports untuk user flow.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1498-1572: metadata event untuk kontrol akses partisipasi.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1629-1658: complete event dan validasi output summary.
- `server/local_api.py` baris 1185-1229: endpoint riwayat events/reports untuk user flow.
- `server/local_api.py` baris 1498-1572: metadata event untuk kontrol akses partisipasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement CTA complete khusus KSH di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement CTA complete khusus KSH di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Complete flow aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Complete flow aktif.
- Aktivitas yang diselesaikan: Implement CTA complete khusus KSH di FE.
- Bukti screenshot utama: `src/app/components/EventList.tsx` baris 190-209: render tab completed events.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 74-85: aksi complete event oleh user/KSH.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 95-104: filter reportable events.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 190-209: render tab completed events.
- `src/app/components/UserDashboard.tsx` baris 74-85: aksi complete event oleh user/KSH.
- `src/app/components/UserDashboard.tsx` baris 95-104: filter reportable events.

### Day 44 (Kamis, 26 Mar 2026): Checklist attendance
Status: [RENCANA]
Milestone/Group: M4: PARTICIPATION (W09)
Task Referensi Farchan: API Complete & Attendance
Task Referensi Ikram: UI Checklist & Complete Action

#### Entri Farchan (UX+Backend)
Aktivitas: Validasi checklist kehadiran dan transisi status.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Validasi checklist kehadiran dan transisi status. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M4: PARTICIPATION (W09). Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Attendance sinkron' punya dasar teknis yang jelas."
Output Farchan:
- Deliverable utama hari ini: Attendance sinkron.
- Aktivitas yang diselesaikan: Validasi checklist kehadiran dan transisi status.
- Bukti screenshot utama: `server/local_api.py` baris 1185-1229: endpoint riwayat events/reports untuk user flow.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1498-1572: metadata event untuk kontrol akses partisipasi.
- Bukti screenshot pendukung 2: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas issue participation domain.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1185-1229: endpoint riwayat events/reports untuk user flow.
- `server/local_api.py` baris 1498-1572: metadata event untuk kontrol akses partisipasi.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas issue participation domain.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi checklist attendance FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi checklist attendance FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Attendance sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Attendance sinkron.
- Aktivitas yang diselesaikan: Integrasi checklist attendance FE.
- Bukti screenshot utama: `src/app/components/UserDashboard.tsx` baris 74-85: aksi complete event oleh user/KSH.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 95-104: filter reportable events.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 319-367: flow event page + tombol complete.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 74-85: aksi complete event oleh user/KSH.
- `src/app/components/UserDashboard.tsx` baris 95-104: filter reportable events.
- `src/app/components/UserDashboard.tsx` baris 319-367: flow event page + tombol complete.

### Day 45 (Jumat, 27 Mar 2026): Retest participation flow
Status: [RENCANA]
Milestone/Group: M4: PARTICIPATION (W09)
Task Referensi Farchan: API Complete & Attendance
Task Referensi Ikram: UI Checklist & Complete Action

#### Entri Farchan (UX+Backend)
Aktivitas: Retest join attendance complete.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest join attendance complete. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Participation stabil' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Participation stabil.
- Aktivitas yang diselesaikan: Retest join attendance complete.
- Bukti screenshot utama: `server/local_api.py` baris 1498-1572: metadata event untuk kontrol akses partisipasi.
- Bukti screenshot pendukung 1: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas issue participation domain.
- Bukti screenshot pendukung 2: `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 57-87: alur user ikut event dari UI.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1498-1572: metadata event untuk kontrol akses partisipasi.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas issue participation domain.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 57-87: alur user ikut event dari UI.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug participation pada UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug participation pada UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Participation stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Deliverable utama hari ini: Participation stabil.
- Aktivitas yang diselesaikan: Patch bug participation pada UI/FE.
- Bukti screenshot utama: `src/app/components/UserDashboard.tsx` baris 95-104: filter reportable events.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 319-367: flow event page + tombol complete.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 351-367: daftar event terpublish untuk attendance.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 95-104: filter reportable events.
- `src/app/components/UserDashboard.tsx` baris 319-367: flow event page + tombol complete.
- `src/app/components/UserDashboard.tsx` baris 351-367: daftar event terpublish untuk attendance.

## PEKAN 10 (W10): Submit Report

Status Pekan: Proyeksi
Milestone Aktif: M5: REPORTING (W10)
Task Utama: Farchan - API Submit Report & Payload | Ikram - UI Wizard Report Step 1-2

### Day 46 (Senin, 30 Mar 2026): Payload wizard report
Status: [RENCANA]
Milestone/Group: M5: REPORTING (W10)
Task Referensi Farchan: API Submit Report & Payload
Task Referensi Ikram: UI Wizard Report Step 1-2

#### Entri Farchan (UX+Backend)
Aktivitas: Finalkan payload report step 1 dan step 2.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalkan payload report step 1 dan step 2 sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Step 1 aktif' benar-benar siap dipakai."
Output Farchan:
- Deliverable utama hari ini: Step 1 aktif.
- Aktivitas yang diselesaikan: Finalkan payload report step 1 dan step 2.
- Bukti screenshot utama: `docs/status/SYSTEM_SUMMARY.md` baris 188-190: endpoint report submit/list/verify.
- Bukti screenshot pendukung 1: `docs/guides/README_SIMRP.md` baris 191-193: kontrak API report pada dokumentasi teknis.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1658-1729: submit report + verify report workflow.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/SYSTEM_SUMMARY.md` baris 188-190: endpoint report submit/list/verify.
- `docs/guides/README_SIMRP.md` baris 191-193: kontrak API report pada dokumentasi teknis.
- `server/local_api.py` baris 1658-1729: submit report + verify report workflow.

#### Entri Ikram (UI+Frontend)
Aktivitas: Bangun wizard report step 1 di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Bangun wizard report step 1 di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Step 1 aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Step 1 aktif.
- Aktivitas yang diselesaikan: Bangun wizard report step 1 di FE.
- Bukti screenshot utama: `src/app/components/AdminDashboard.tsx` baris 366-428: review report list dan action verify.
- Bukti screenshot pendukung 1: `src/app/components/ModeratorDashboard.tsx` baris 386-449: verify report flow di moderator panel.
- Bukti screenshot pendukung 2: `src/app/components/ReportingWizard.tsx` baris 83-92: payload submit report step wizard.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 366-428: review report list dan action verify.
- `src/app/components/ModeratorDashboard.tsx` baris 386-449: verify report flow di moderator panel.
- `src/app/components/ReportingWizard.tsx` baris 83-92: payload submit report step wizard.

### Day 47 (Selasa, 31 Mar 2026): Submit report endpoint
Status: [RENCANA]
Milestone/Group: M5: REPORTING (W10)
Task Referensi Farchan: API Submit Report & Payload
Task Referensi Ikram: UI Wizard Report Step 1-2

#### Entri Farchan (UX+Backend)
Aktivitas: Implement submit report endpoint beserta validasi.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement submit report endpoint beserta validasi pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Submit report jalan' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Submit report jalan.
- Aktivitas yang diselesaikan: Implement submit report endpoint beserta validasi.
- Bukti screenshot utama: `docs/guides/README_SIMRP.md` baris 191-193: kontrak API report pada dokumentasi teknis.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1658-1729: submit report + verify report workflow.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 926-934: rule `can_verify_report()` sesuai role moderator/admin.
Lampiran Farchan (Bukti Screenshot):
- `docs/guides/README_SIMRP.md` baris 191-193: kontrak API report pada dokumentasi teknis.
- `server/local_api.py` baris 1658-1729: submit report + verify report workflow.
- `server/local_api.py` baris 926-934: rule `can_verify_report()` sesuai role moderator/admin.

#### Entri Ikram (UI+Frontend)
Aktivitas: Bangun wizard step 2 dan validasi FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Bangun wizard step 2 dan validasi FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Submit report jalan' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Submit report jalan.
- Aktivitas yang diselesaikan: Bangun wizard step 2 dan validasi FE.
- Bukti screenshot utama: `src/app/components/ModeratorDashboard.tsx` baris 386-449: verify report flow di moderator panel.
- Bukti screenshot pendukung 1: `src/app/components/ReportingWizard.tsx` baris 83-92: payload submit report step wizard.
- Bukti screenshot pendukung 2: `src/app/components/ReportingWizard.tsx` baris 169-171: event selector pada report wizard.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 386-449: verify report flow di moderator panel.
- `src/app/components/ReportingWizard.tsx` baris 83-92: payload submit report step wizard.
- `src/app/components/ReportingWizard.tsx` baris 169-171: event selector pada report wizard.

### Day 48 (Rabu, 1 Apr 2026): Validasi bukti laporan
Status: [RENCANA]
Milestone/Group: M5: REPORTING (W10)
Task Referensi Farchan: Validasi Proof & E2E Status
Task Referensi Ikram: Validasi Form & UI History

#### Entri Farchan (UX+Backend)
Aktivitas: Atur validasi media proof laporan.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Atur validasi media proof laporan. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M5: REPORTING (W10). Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Bukti laporan tervalidasi' punya dasar teknis yang jelas."
Output Farchan:
- Deliverable utama hari ini: Bukti laporan tervalidasi.
- Aktivitas yang diselesaikan: Atur validasi media proof laporan.
- Bukti screenshot utama: `server/local_api.py` baris 1658-1729: submit report + verify report workflow.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 926-934: rule `can_verify_report()` sesuai role moderator/admin.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 934-957: `apply_xp()` saat report approved.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1658-1729: submit report + verify report workflow.
- `server/local_api.py` baris 926-934: rule `can_verify_report()` sesuai role moderator/admin.
- `server/local_api.py` baris 934-957: `apply_xp()` saat report approved.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement behavior upload dan proof field di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement behavior upload dan proof field di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Bukti laporan tervalidasi' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Bukti laporan tervalidasi.
- Aktivitas yang diselesaikan: Implement behavior upload dan proof field di FE.
- Bukti screenshot utama: `src/app/components/ReportingWizard.tsx` baris 83-92: payload submit report step wizard.
- Bukti screenshot pendukung 1: `src/app/components/ReportingWizard.tsx` baris 169-171: event selector pada report wizard.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 58-59: fetch report history user.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 83-92: payload submit report step wizard.
- `src/app/components/ReportingWizard.tsx` baris 169-171: event selector pada report wizard.
- `src/app/components/UserDashboard.tsx` baris 58-59: fetch report history user.

### Day 49 (Kamis, 2 Apr 2026): Sinkron status report
Status: [RENCANA]
Milestone/Group: M5: REPORTING (W10)
Task Referensi Farchan: Validasi Proof & E2E Status
Task Referensi Ikram: Validasi Form & UI History

#### Entri Farchan (UX+Backend)
Aktivitas: Sinkron status report pending di backend.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Sinkron status report pending di backend. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M5: REPORTING (W10). Setelah itu saya catat poin koreksi dan konfirmasi final biar 'History report sinkron' punya dasar teknis yang jelas."
Output Farchan:
- Deliverable utama hari ini: History report sinkron.
- Aktivitas yang diselesaikan: Sinkron status report pending di backend.
- Bukti screenshot utama: `server/local_api.py` baris 926-934: rule `can_verify_report()` sesuai role moderator/admin.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 934-957: `apply_xp()` saat report approved.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 462-473: tabel `xp_kelurahan` dan `xp_pillar` untuk scoring.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 926-934: rule `can_verify_report()` sesuai role moderator/admin.
- `server/local_api.py` baris 934-957: `apply_xp()` saat report approved.
- `server/local_api.py` baris 462-473: tabel `xp_kelurahan` dan `xp_pillar` untuk scoring.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi history report user di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi history report user di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'History report sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: History report sinkron.
- Aktivitas yang diselesaikan: Integrasi history report user di FE.
- Bukti screenshot utama: `src/app/components/ReportingWizard.tsx` baris 169-171: event selector pada report wizard.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 58-59: fetch report history user.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 396: pass `reportableEvents` ke wizard.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 169-171: event selector pada report wizard.
- `src/app/components/UserDashboard.tsx` baris 58-59: fetch report history user.
- `src/app/components/UserDashboard.tsx` baris 396: pass `reportableEvents` ke wizard.

### Day 50 (Jumat, 3 Apr 2026): E2E reporting
Status: [RENCANA]
Milestone/Group: M5: REPORTING (W10)
Task Referensi Farchan: Validasi Proof & E2E Status
Task Referensi Ikram: Validasi Form & UI History

#### Entri Farchan (UX+Backend)
Aktivitas: Uji E2E report submission.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji E2E report submission. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Reporting stabil' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Reporting stabil.
- Aktivitas yang diselesaikan: Uji E2E report submission.
- Bukti screenshot utama: `server/local_api.py` baris 934-957: `apply_xp()` saat report approved.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 462-473: tabel `xp_kelurahan` dan `xp_pillar` untuk scoring.
- Bukti screenshot pendukung 2: `docs/status/SYSTEM_SUMMARY.md` baris 188-190: endpoint report submit/list/verify.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 934-957: `apply_xp()` saat report approved.
- `server/local_api.py` baris 462-473: tabel `xp_kelurahan` dan `xp_pillar` untuk scoring.
- `docs/status/SYSTEM_SUMMARY.md` baris 188-190: endpoint report submit/list/verify.

#### Entri Ikram (UI+Frontend)
Aktivitas: Refinement wizard report di UI/FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Refinement wizard report di UI/FE dalam konteks 'E2E reporting'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M5: REPORTING (W10). Hasil 'Reporting stabil' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Reporting stabil.
- Aktivitas yang diselesaikan: Refinement wizard report di UI/FE.
- Bukti screenshot utama: `src/app/components/UserDashboard.tsx` baris 58-59: fetch report history user.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 396: pass `reportableEvents` ke wizard.
- Bukti screenshot pendukung 2: `src/app/components/AdminDashboard.tsx` baris 366-428: review report list dan action verify.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 58-59: fetch report history user.
- `src/app/components/UserDashboard.tsx` baris 396: pass `reportableEvents` ke wizard.
- `src/app/components/AdminDashboard.tsx` baris 366-428: review report list dan action verify.

## PEKAN 11 (W11): Verify dan Scoring Dasar

Status Pekan: Proyeksi
Milestone Aktif: M6: VERIFICATION (W11)
Task Utama: Farchan - API Verify & Scoring Tambah XP | Ikram - Panel Verifikasi Admin/Mod

### Day 51 (Senin, 6 Apr 2026): Verify reject reason
Status: [RENCANA]
Milestone/Group: M6: VERIFICATION (W11)
Task Referensi Farchan: API Verify & Scoring Tambah XP
Task Referensi Ikram: Panel Verifikasi Admin/Mod

#### Entri Farchan (UX+Backend)
Aktivitas: Implement verify reject dan reason backend.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement verify reject dan reason backend pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Verify panel aktif' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Verify panel aktif.
- Aktivitas yang diselesaikan: Implement verify reject dan reason backend.
- Bukti screenshot utama: `server/local_api.py` baris 487-537: tabel `audit_logs` dan `temporary_adjustments`.
- Bukti screenshot pendukung 1: `docs/status/SYSTEM_SUMMARY.md` baris 118-121: verification inbox dan SLA verifikasi.
- Bukti screenshot pendukung 2: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: issue list domain verify/scoring.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 487-537: tabel `audit_logs` dan `temporary_adjustments`.
- `docs/status/SYSTEM_SUMMARY.md` baris 118-121: verification inbox dan SLA verifikasi.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: issue list domain verify/scoring.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement panel verifikasi moderator FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement panel verifikasi moderator FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Verify panel aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Verify panel aktif.
- Aktivitas yang diselesaikan: Implement panel verifikasi moderator FE.
- Bukti screenshot utama: `src/app/components/AdminDashboard.tsx` baris 366-428: status report list pending/verified/rejected.
- Bukti screenshot pendukung 1: `src/app/components/UserProfile.tsx` baris 12-14: perhitungan status report di profile.
- Bukti screenshot pendukung 2: `src/app/components/UserProfile.tsx` baris 172-178: badge status report pada riwayat user.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 366-428: status report list pending/verified/rejected.
- `src/app/components/UserProfile.tsx` baris 12-14: perhitungan status report di profile.
- `src/app/components/UserProfile.tsx` baris 172-178: badge status report pada riwayat user.

### Day 52 (Selasa, 7 Apr 2026): Scoring dasar
Status: [RENCANA]
Milestone/Group: M6: VERIFICATION (W11)
Task Referensi Farchan: API Verify & Scoring Tambah XP
Task Referensi Ikram: Panel Verifikasi Admin/Mod

#### Entri Farchan (UX+Backend)
Aktivitas: Implement scoring dasar saat verify.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement scoring dasar saat verify pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Scoring sinkron' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Scoring sinkron.
- Aktivitas yang diselesaikan: Implement scoring dasar saat verify.
- Bukti screenshot utama: `docs/status/SYSTEM_SUMMARY.md` baris 118-121: verification inbox dan SLA verifikasi.
- Bukti screenshot pendukung 1: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: issue list domain verify/scoring.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1716-1729: verify report endpoint dan update poin.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/SYSTEM_SUMMARY.md` baris 118-121: verification inbox dan SLA verifikasi.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: issue list domain verify/scoring.
- `server/local_api.py` baris 1716-1729: verify report endpoint dan update poin.

#### Entri Ikram (UI+Frontend)
Aktivitas: Tampilkan feedback status dan skor di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Tampilkan feedback status dan skor di FE dalam konteks 'Scoring dasar'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M6: VERIFICATION (W11). Hasil 'Scoring sinkron' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Scoring sinkron.
- Aktivitas yang diselesaikan: Tampilkan feedback status dan skor di FE.
- Bukti screenshot utama: `src/app/components/UserProfile.tsx` baris 12-14: perhitungan status report di profile.
- Bukti screenshot pendukung 1: `src/app/components/UserProfile.tsx` baris 172-178: badge status report pada riwayat user.
- Bukti screenshot pendukung 2: `src/app/components/ModeratorDashboard.tsx` baris 155-159: handler verify report di FE.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserProfile.tsx` baris 12-14: perhitungan status report di profile.
- `src/app/components/UserProfile.tsx` baris 172-178: badge status report pada riwayat user.
- `src/app/components/ModeratorDashboard.tsx` baris 155-159: handler verify report di FE.

### Day 53 (Rabu, 8 Apr 2026): Audit trail report
Status: [RENCANA]
Milestone/Group: M6: VERIFICATION (W11)
Task Referensi Farchan: Audit Trail & Status Notification
Task Referensi Ikram: UI Timeline & Indicator FE

#### Entri Farchan (UX+Backend)
Aktivitas: Tambah audit trail status report.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Tambah audit trail status report. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M6: VERIFICATION (W11). Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Audit trail terbaca' punya dasar teknis yang jelas."
Output Farchan:
- Deliverable utama hari ini: Audit trail terbaca.
- Aktivitas yang diselesaikan: Tambah audit trail status report.
- Bukti screenshot utama: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: issue list domain verify/scoring.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1716-1729: verify report endpoint dan update poin.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 926-934: akses verify berbasis role.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: issue list domain verify/scoring.
- `server/local_api.py` baris 1716-1729: verify report endpoint dan update poin.
- `server/local_api.py` baris 926-934: akses verify berbasis role.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement timeline status report FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement timeline status report FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Audit trail terbaca' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Audit trail terbaca.
- Aktivitas yang diselesaikan: Implement timeline status report FE.
- Bukti screenshot utama: `src/app/components/UserProfile.tsx` baris 172-178: badge status report pada riwayat user.
- Bukti screenshot pendukung 1: `src/app/components/ModeratorDashboard.tsx` baris 155-159: handler verify report di FE.
- Bukti screenshot pendukung 2: `src/app/components/ModeratorDashboard.tsx` baris 386-449: UI action approve/reject report.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserProfile.tsx` baris 172-178: badge status report pada riwayat user.
- `src/app/components/ModeratorDashboard.tsx` baris 155-159: handler verify report di FE.
- `src/app/components/ModeratorDashboard.tsx` baris 386-449: UI action approve/reject report.

### Day 54 (Kamis, 9 Apr 2026): Notifikasi status report
Status: [RENCANA]
Milestone/Group: M6: VERIFICATION (W11)
Task Referensi Farchan: Audit Trail & Status Notification
Task Referensi Ikram: UI Timeline & Indicator FE

#### Entri Farchan (UX+Backend)
Aktivitas: Stabilkan notifikasi status report backend.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilkan notifikasi status report backend untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Notifikasi status aktif' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Deliverable utama hari ini: Notifikasi status aktif.
- Aktivitas yang diselesaikan: Stabilkan notifikasi status report backend.
- Bukti screenshot utama: `server/local_api.py` baris 1716-1729: verify report endpoint dan update poin.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 926-934: akses verify berbasis role.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 934-957: side-effect scoring pada XP kampung/pilar.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1716-1729: verify report endpoint dan update poin.
- `server/local_api.py` baris 926-934: akses verify berbasis role.
- `server/local_api.py` baris 934-957: side-effect scoring pada XP kampung/pilar.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement indikator notifikasi FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement indikator notifikasi FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Notifikasi status aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Notifikasi status aktif.
- Aktivitas yang diselesaikan: Implement indikator notifikasi FE.
- Bukti screenshot utama: `src/app/components/ModeratorDashboard.tsx` baris 155-159: handler verify report di FE.
- Bukti screenshot pendukung 1: `src/app/components/ModeratorDashboard.tsx` baris 386-449: UI action approve/reject report.
- Bukti screenshot pendukung 2: `src/app/components/AdminDashboard.tsx` baris 81-84: verify report oleh admin.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 155-159: handler verify report di FE.
- `src/app/components/ModeratorDashboard.tsx` baris 386-449: UI action approve/reject report.
- `src/app/components/AdminDashboard.tsx` baris 81-84: verify report oleh admin.

### Day 55 (Jumat, 10 Apr 2026): Retest verify scoring
Status: [RENCANA]
Milestone/Group: M6: VERIFICATION (W11)
Task Referensi Farchan: Audit Trail & Status Notification
Task Referensi Ikram: UI Timeline & Indicator FE

#### Entri Farchan (UX+Backend)
Aktivitas: Retest verify dan scoring end-to-end.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest verify dan scoring end-to-end. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Verifikasi stabil' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Verifikasi stabil.
- Aktivitas yang diselesaikan: Retest verify dan scoring end-to-end.
- Bukti screenshot utama: `server/local_api.py` baris 926-934: akses verify berbasis role.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 934-957: side-effect scoring pada XP kampung/pilar.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 487-537: tabel `audit_logs` dan `temporary_adjustments`.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 926-934: akses verify berbasis role.
- `server/local_api.py` baris 934-957: side-effect scoring pada XP kampung/pilar.
- `server/local_api.py` baris 487-537: tabel `audit_logs` dan `temporary_adjustments`.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug verifikasi pada UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug verifikasi pada UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Verifikasi stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Deliverable utama hari ini: Verifikasi stabil.
- Aktivitas yang diselesaikan: Patch bug verifikasi pada UI/FE.
- Bukti screenshot utama: `src/app/components/ModeratorDashboard.tsx` baris 386-449: UI action approve/reject report.
- Bukti screenshot pendukung 1: `src/app/components/AdminDashboard.tsx` baris 81-84: verify report oleh admin.
- Bukti screenshot pendukung 2: `src/app/components/AdminDashboard.tsx` baris 366-428: status report list pending/verified/rejected.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 386-449: UI action approve/reject report.
- `src/app/components/AdminDashboard.tsx` baris 81-84: verify report oleh admin.
- `src/app/components/AdminDashboard.tsx` baris 366-428: status report list pending/verified/rejected.

## PEKAN 12 (W12): XP dan Leaderboard

Status Pekan: Proyeksi
Milestone Aktif: M7: GAMIFICATION (W12)
Task Utama: Farchan - Aggregation & Rank Update API | Ikram - UI Leaderboard & Rank Card

### Day 56 (Senin, 13 Apr 2026): Formula XP final
Status: [RENCANA]
Milestone/Group: M7: GAMIFICATION (W12)
Task Referensi Farchan: Aggregation & Rank Update API
Task Referensi Ikram: UI Leaderboard & Rank Card

#### Entri Farchan (UX+Backend)
Aktivitas: Finalkan rumus XP kampung dan pilar.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalkan rumus XP kampung dan pilar sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Leaderboard awal aktif' benar-benar siap dipakai."
Output Farchan:
- Deliverable utama hari ini: Leaderboard awal aktif.
- Aktivitas yang diselesaikan: Finalkan rumus XP kampung dan pilar.
- Bukti screenshot utama: `server/local_api.py` baris 1082-1089: leaderboard kelurahan by kecamatan/scope.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 462-473: storage XP pilar dan XP kelurahan.
- Bukti screenshot pendukung 2: `docs/architecture/GRAND_DESIGN_FINAL.md` baris 40-45: prinsip pillar-balance dan leaderboard.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1082-1089: leaderboard kelurahan by kecamatan/scope.
- `server/local_api.py` baris 462-473: storage XP pilar dan XP kelurahan.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 40-45: prinsip pillar-balance dan leaderboard.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI leaderboard top ringkas.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI leaderboard top ringkas pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Leaderboard awal aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Leaderboard awal aktif.
- Aktivitas yang diselesaikan: Implement UI leaderboard top ringkas.
- Bukti screenshot utama: `src/app/components/LevelProgressionCard.tsx` baris 97: progress persentase ke level berikutnya.
- Bukti screenshot pendukung 1: `src/data/levelingSystem.ts` baris 145-172: calculate level by role.
- Bukti screenshot pendukung 2: `src/data/levelingSystem.ts` baris 196-228: progress to next level.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LevelProgressionCard.tsx` baris 97: progress persentase ke level berikutnya.
- `src/data/levelingSystem.ts` baris 145-172: calculate level by role.
- `src/data/levelingSystem.ts` baris 196-228: progress to next level.

### Day 57 (Selasa, 14 Apr 2026): Sinkron update rank
Status: [RENCANA]
Milestone/Group: M7: GAMIFICATION (W12)
Task Referensi Farchan: Aggregation & Rank Update API
Task Referensi Ikram: UI Leaderboard & Rank Card

#### Entri Farchan (UX+Backend)
Aktivitas: Sinkron update XP pasca verify.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Sinkron update XP pasca verify. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M7: GAMIFICATION (W12). Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Rank update sinkron' punya dasar teknis yang jelas."
Output Farchan:
- Deliverable utama hari ini: Rank update sinkron.
- Aktivitas yang diselesaikan: Sinkron update XP pasca verify.
- Bukti screenshot utama: `server/local_api.py` baris 462-473: storage XP pilar dan XP kelurahan.
- Bukti screenshot pendukung 1: `docs/architecture/GRAND_DESIGN_FINAL.md` baris 40-45: prinsip pillar-balance dan leaderboard.
- Bukti screenshot pendukung 2: `src/data/levelingSystem.ts` baris 145-172: hitung level user/mod/admin berdasarkan poin.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 462-473: storage XP pilar dan XP kelurahan.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 40-45: prinsip pillar-balance dan leaderboard.
- `src/data/levelingSystem.ts` baris 145-172: hitung level user/mod/admin berdasarkan poin.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi rank card dan nilai XP FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi rank card dan nilai XP FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Rank update sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Rank update sinkron.
- Aktivitas yang diselesaikan: Integrasi rank card dan nilai XP FE.
- Bukti screenshot utama: `src/data/levelingSystem.ts` baris 145-172: calculate level by role.
- Bukti screenshot pendukung 1: `src/data/levelingSystem.ts` baris 196-228: progress to next level.
- Bukti screenshot pendukung 2: `src/data/validatedBadges.ts` baris 208-230: rule `canAssignBadge()` untuk validasi badge.
Lampiran Ikram (Bukti Screenshot):
- `src/data/levelingSystem.ts` baris 145-172: calculate level by role.
- `src/data/levelingSystem.ts` baris 196-228: progress to next level.
- `src/data/validatedBadges.ts` baris 208-230: rule `canAssignBadge()` untuk validasi badge.

### Day 58 (Rabu, 15 Apr 2026): Service progres pilar
Status: [RENCANA]
Milestone/Group: M7: GAMIFICATION (W12)
Task Referensi Farchan: Pilar Progress & Optimasi Query
Task Referensi Ikram: Visual Chart 4 Pilar & CTA

#### Entri Farchan (UX+Backend)
Aktivitas: Stabilkan service progres 4 pilar.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilkan service progres 4 pilar untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Progress pilar tampil' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Deliverable utama hari ini: Progress pilar tampil.
- Aktivitas yang diselesaikan: Stabilkan service progres 4 pilar.
- Bukti screenshot utama: `docs/architecture/GRAND_DESIGN_FINAL.md` baris 40-45: prinsip pillar-balance dan leaderboard.
- Bukti screenshot pendukung 1: `src/data/levelingSystem.ts` baris 145-172: hitung level user/mod/admin berdasarkan poin.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 934-957: agregasi XP dan update leaderboard data.
Lampiran Farchan (Bukti Screenshot):
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 40-45: prinsip pillar-balance dan leaderboard.
- `src/data/levelingSystem.ts` baris 145-172: hitung level user/mod/admin berdasarkan poin.
- `server/local_api.py` baris 934-957: agregasi XP dan update leaderboard data.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi chart radar pilar FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi chart radar pilar FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Progress pilar tampil' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Progress pilar tampil.
- Aktivitas yang diselesaikan: Integrasi chart radar pilar FE.
- Bukti screenshot utama: `src/data/levelingSystem.ts` baris 196-228: progress to next level.
- Bukti screenshot pendukung 1: `src/data/validatedBadges.ts` baris 208-230: rule `canAssignBadge()` untuk validasi badge.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 239-264: tabel leaderboard pada user dashboard.
Lampiran Ikram (Bukti Screenshot):
- `src/data/levelingSystem.ts` baris 196-228: progress to next level.
- `src/data/validatedBadges.ts` baris 208-230: rule `canAssignBadge()` untuk validasi badge.
- `src/app/components/UserDashboard.tsx` baris 239-264: tabel leaderboard pada user dashboard.

### Day 59 (Kamis, 16 Apr 2026): Rule akses leaderboard
Status: [RENCANA]
Milestone/Group: M7: GAMIFICATION (W12)
Task Referensi Farchan: Pilar Progress & Optimasi Query
Task Referensi Ikram: Visual Chart 4 Pilar & CTA

#### Entri Farchan (UX+Backend)
Aktivitas: Atur aturan akses leaderboard.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Atur aturan akses leaderboard dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Akses leaderboard valid' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Deliverable utama hari ini: Akses leaderboard valid.
- Aktivitas yang diselesaikan: Atur aturan akses leaderboard.
- Bukti screenshot utama: `src/data/levelingSystem.ts` baris 145-172: hitung level user/mod/admin berdasarkan poin.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 934-957: agregasi XP dan update leaderboard data.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1054-1061: query leaderboard kampung terurut total XP.
Lampiran Farchan (Bukti Screenshot):
- `src/data/levelingSystem.ts` baris 145-172: hitung level user/mod/admin berdasarkan poin.
- `server/local_api.py` baris 934-957: agregasi XP dan update leaderboard data.
- `server/local_api.py` baris 1054-1061: query leaderboard kampung terurut total XP.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement CTA login dan view all FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement CTA login dan view all FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Akses leaderboard valid' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Akses leaderboard valid.
- Aktivitas yang diselesaikan: Implement CTA login dan view all FE.
- Bukti screenshot utama: `src/data/validatedBadges.ts` baris 208-230: rule `canAssignBadge()` untuk validasi badge.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 239-264: tabel leaderboard pada user dashboard.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 288-309: badge XP dan rank card leaderboard.
Lampiran Ikram (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 208-230: rule `canAssignBadge()` untuk validasi badge.
- `src/app/components/UserDashboard.tsx` baris 239-264: tabel leaderboard pada user dashboard.
- `src/app/components/UserDashboard.tsx` baris 288-309: badge XP dan rank card leaderboard.

### Day 60 (Jumat, 17 Apr 2026): E2E report ke rank
Status: [RENCANA]
Milestone/Group: M7: GAMIFICATION (W12)
Task Referensi Farchan: Pilar Progress & Optimasi Query
Task Referensi Ikram: Visual Chart 4 Pilar & CTA

#### Entri Farchan (UX+Backend)
Aktivitas: Uji E2E report ke XP ke leaderboard.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji E2E report ke XP ke leaderboard. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Leaderboard stabil' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Leaderboard stabil.
- Aktivitas yang diselesaikan: Uji E2E report ke XP ke leaderboard.
- Bukti screenshot utama: `server/local_api.py` baris 934-957: agregasi XP dan update leaderboard data.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1054-1061: query leaderboard kampung terurut total XP.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1082-1089: leaderboard kelurahan by kecamatan/scope.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 934-957: agregasi XP dan update leaderboard data.
- `server/local_api.py` baris 1054-1061: query leaderboard kampung terurut total XP.
- `server/local_api.py` baris 1082-1089: leaderboard kelurahan by kecamatan/scope.

#### Entri Ikram (UI+Frontend)
Aktivitas: Polish UI/FE leaderboard.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Polish UI/FE leaderboard dalam konteks 'E2E report ke rank'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M7: GAMIFICATION (W12). Hasil 'Leaderboard stabil' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Leaderboard stabil.
- Aktivitas yang diselesaikan: Polish UI/FE leaderboard.
- Bukti screenshot utama: `src/app/components/UserDashboard.tsx` baris 239-264: tabel leaderboard pada user dashboard.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 288-309: badge XP dan rank card leaderboard.
- Bukti screenshot pendukung 2: `src/app/components/LevelProgressionCard.tsx` baris 97: progress persentase ke level berikutnya.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 239-264: tabel leaderboard pada user dashboard.
- `src/app/components/UserDashboard.tsx` baris 288-309: badge XP dan rank card leaderboard.
- `src/app/components/LevelProgressionCard.tsx` baris 97: progress persentase ke level berikutnya.

## PEKAN 13 (W13): Sertifikat dan Reward

Status Pekan: Proyeksi
Milestone Aktif: M8: REWARD (W13)
Task Utama: Farchan - Generate Sertifikat & Rule Konversi | Ikram - UI History Sertifikat & Katalog

### Day 61 (Senin, 20 Apr 2026): Rule sertifikat
Status: [RENCANA]
Milestone/Group: M8: REWARD (W13)
Task Referensi Farchan: Generate Sertifikat & Rule Konversi
Task Referensi Ikram: UI History Sertifikat & Katalog

#### Entri Farchan (UX+Backend)
Aktivitas: Definisikan rule 1 kegiatan 1 sertifikat.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Definisikan rule 1 kegiatan 1 sertifikat dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Rule sertifikat final' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Deliverable utama hari ini: Rule sertifikat final.
- Aktivitas yang diselesaikan: Definisikan rule 1 kegiatan 1 sertifikat.
- Bukti screenshot utama: `src/data/validatedBadges.ts` baris 160-208: definisi badge/reward rule berbasis validasi.
- Bukti screenshot pendukung 1: `src/data/validatedBadges.ts` baris 208-230: `canAssignBadge()` untuk kontrol assignment.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1781-1808: temporary points/badge adjustment (governance reward).
Lampiran Farchan (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 160-208: definisi badge/reward rule berbasis validasi.
- `src/data/validatedBadges.ts` baris 208-230: `canAssignBadge()` untuk kontrol assignment.
- `server/local_api.py` baris 1781-1808: temporary points/badge adjustment (governance reward).

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI riwayat sertifikat.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI riwayat sertifikat pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Rule sertifikat final' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Rule sertifikat final.
- Aktivitas yang diselesaikan: Implement UI riwayat sertifikat.
- Bukti screenshot utama: `src/data/validatedBadges.ts` baris 208-230: validasi pemberian badge/reward.
- Bukti screenshot pendukung 1: `src/app/components/UserProfile.tsx` baris 152-178: history kontribusi sebagai basis reward visual.
- Bukti screenshot pendukung 2: `src/app/components/AdminGodMode.tsx` baris 117-136: add temporary points/badge dari UI admin.
Lampiran Ikram (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 208-230: validasi pemberian badge/reward.
- `src/app/components/UserProfile.tsx` baris 152-178: history kontribusi sebagai basis reward visual.
- `src/app/components/AdminGodMode.tsx` baris 117-136: add temporary points/badge dari UI admin.

### Day 62 (Selasa, 21 Apr 2026): Penerbitan sertifikat
Status: [RENCANA]
Milestone/Group: M8: REWARD (W13)
Task Referensi Farchan: Generate Sertifikat & Rule Konversi
Task Referensi Ikram: UI History Sertifikat & Katalog

#### Entri Farchan (UX+Backend)
Aktivitas: Implement penerbitan sertifikat.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement penerbitan sertifikat pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Sertifikat dapat diakses' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Sertifikat dapat diakses.
- Aktivitas yang diselesaikan: Implement penerbitan sertifikat.
- Bukti screenshot utama: `src/data/validatedBadges.ts` baris 208-230: `canAssignBadge()` untuk kontrol assignment.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1781-1808: temporary points/badge adjustment (governance reward).
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1271-1274: listing temporary adjustments untuk audit.
Lampiran Farchan (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 208-230: `canAssignBadge()` untuk kontrol assignment.
- `server/local_api.py` baris 1781-1808: temporary points/badge adjustment (governance reward).
- `server/local_api.py` baris 1271-1274: listing temporary adjustments untuk audit.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi unduh sertifikat FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi unduh sertifikat FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Sertifikat dapat diakses' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Sertifikat dapat diakses.
- Aktivitas yang diselesaikan: Integrasi unduh sertifikat FE.
- Bukti screenshot utama: `src/app/components/UserProfile.tsx` baris 152-178: history kontribusi sebagai basis reward visual.
- Bukti screenshot pendukung 1: `src/app/components/AdminGodMode.tsx` baris 117-136: add temporary points/badge dari UI admin.
- Bukti screenshot pendukung 2: `src/app/components/AdminGodMode.tsx` baris 73-96: role assignment dan governance akses.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserProfile.tsx` baris 152-178: history kontribusi sebagai basis reward visual.
- `src/app/components/AdminGodMode.tsx` baris 117-136: add temporary points/badge dari UI admin.
- `src/app/components/AdminGodMode.tsx` baris 73-96: role assignment dan governance akses.

### Day 63 (Rabu, 22 Apr 2026): Konversi poin voucher
Status: [RENCANA]
Milestone/Group: M8: REWARD (W13)
Task Referensi Farchan: Generate Sertifikat & Rule Konversi
Task Referensi Ikram: UI History Sertifikat & Katalog

#### Entri Farchan (UX+Backend)
Aktivitas: Definisikan konversi poin ke voucher.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Definisikan konversi poin ke voucher dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Katalog reward aktif' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Deliverable utama hari ini: Katalog reward aktif.
- Aktivitas yang diselesaikan: Definisikan konversi poin ke voucher.
- Bukti screenshot utama: `server/local_api.py` baris 1781-1808: temporary points/badge adjustment (governance reward).
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1271-1274: listing temporary adjustments untuk audit.
- Bukti screenshot pendukung 2: `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin dan progress user.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1781-1808: temporary points/badge adjustment (governance reward).
- `server/local_api.py` baris 1271-1274: listing temporary adjustments untuk audit.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin dan progress user.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI katalog reward.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI katalog reward pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Katalog reward aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Katalog reward aktif.
- Aktivitas yang diselesaikan: Implement UI katalog reward.
- Bukti screenshot utama: `src/app/components/AdminGodMode.tsx` baris 117-136: add temporary points/badge dari UI admin.
- Bukti screenshot pendukung 1: `src/app/components/AdminGodMode.tsx` baris 73-96: role assignment dan governance akses.
- Bukti screenshot pendukung 2: `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin ke level berikutnya.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminGodMode.tsx` baris 117-136: add temporary points/badge dari UI admin.
- `src/app/components/AdminGodMode.tsx` baris 73-96: role assignment dan governance akses.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin ke level berikutnya.

### Day 64 (Kamis, 23 Apr 2026): Redeem poin
Status: [RENCANA]
Milestone/Group: M8: REWARD (W13)
Task Referensi Farchan: API Redeem Poin & Retest
Task Referensi Ikram: Integrasi Flow Redeem Poin

#### Entri Farchan (UX+Backend)
Aktivitas: Implement redeem poin dan decrement saldo.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement redeem poin dan decrement saldo pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Redeem sinkron' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Redeem sinkron.
- Aktivitas yang diselesaikan: Implement redeem poin dan decrement saldo.
- Bukti screenshot utama: `server/local_api.py` baris 1271-1274: listing temporary adjustments untuk audit.
- Bukti screenshot pendukung 1: `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin dan progress user.
- Bukti screenshot pendukung 2: `docs/architecture/GRAND_DESIGN_FINAL.md` baris 145-154: rule sertifikat dan konversi poin reward.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1271-1274: listing temporary adjustments untuk audit.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin dan progress user.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 145-154: rule sertifikat dan konversi poin reward.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi redeem flow FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi redeem flow FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Redeem sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Redeem sinkron.
- Aktivitas yang diselesaikan: Integrasi redeem flow FE.
- Bukti screenshot utama: `src/app/components/AdminGodMode.tsx` baris 73-96: role assignment dan governance akses.
- Bukti screenshot pendukung 1: `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin ke level berikutnya.
- Bukti screenshot pendukung 2: `src/data/validatedBadges.ts` baris 160-208: definisi achievement/reward badges.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminGodMode.tsx` baris 73-96: role assignment dan governance akses.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin ke level berikutnya.
- `src/data/validatedBadges.ts` baris 160-208: definisi achievement/reward badges.

### Day 65 (Jumat, 24 Apr 2026): Retest reward flow
Status: [RENCANA]
Milestone/Group: M8: REWARD (W13)
Task Referensi Farchan: API Redeem Poin & Retest
Task Referensi Ikram: Integrasi Flow Redeem Poin

#### Entri Farchan (UX+Backend)
Aktivitas: Uji E2E sertifikat dan redeem.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji E2E sertifikat dan redeem. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Benefit relawan stabil' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Benefit relawan stabil.
- Aktivitas yang diselesaikan: Uji E2E sertifikat dan redeem.
- Bukti screenshot utama: `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin dan progress user.
- Bukti screenshot pendukung 1: `docs/architecture/GRAND_DESIGN_FINAL.md` baris 145-154: rule sertifikat dan konversi poin reward.
- Bukti screenshot pendukung 2: `src/data/validatedBadges.ts` baris 160-208: definisi badge/reward rule berbasis validasi.
Lampiran Farchan (Bukti Screenshot):
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin dan progress user.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 145-154: rule sertifikat dan konversi poin reward.
- `src/data/validatedBadges.ts` baris 160-208: definisi badge/reward rule berbasis validasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug reward UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug reward UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Benefit relawan stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Deliverable utama hari ini: Benefit relawan stabil.
- Aktivitas yang diselesaikan: Patch bug reward UI/FE.
- Bukti screenshot utama: `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin ke level berikutnya.
- Bukti screenshot pendukung 1: `src/data/validatedBadges.ts` baris 160-208: definisi achievement/reward badges.
- Bukti screenshot pendukung 2: `src/data/validatedBadges.ts` baris 208-230: validasi pemberian badge/reward.
Lampiran Ikram (Bukti Screenshot):
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 257-258: milestone poin ke level berikutnya.
- `src/data/validatedBadges.ts` baris 160-208: definisi achievement/reward badges.
- `src/data/validatedBadges.ts` baris 208-230: validasi pemberian badge/reward.

## PEKAN 14 (W14): Kolaborasi Mitra

Status Pekan: Proyeksi
Milestone Aktif: M9: MITRA (W14)
Task Utama: Farchan - Schema & Public API Mitra | Ikram - Landing Page Mitra & Submit FE

### Day 66 (Senin, 27 Apr 2026): Schema request mitra
Status: [RENCANA]
Milestone/Group: M9: MITRA (W14)
Task Referensi Farchan: Schema & Public API Mitra
Task Referensi Ikram: Landing Page Mitra & Submit FE

#### Entri Farchan (UX+Backend)
Aktivitas: Definisikan schema request mitra dan scope.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Definisikan schema request mitra dan scope dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Form mitra aktif' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Deliverable utama hari ini: Form mitra aktif.
- Aktivitas yang diselesaikan: Definisikan schema request mitra dan scope.
- Bukti screenshot utama: `server/local_api.py` baris 501-568: schema `collaboration_requests` dan migrasi kolom scope.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1096-1119: list request mitra dengan filter status/scope.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1400-1441: submit request mitra dari public form.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 501-568: schema `collaboration_requests` dan migrasi kolom scope.
- `server/local_api.py` baris 1096-1119: list request mitra dengan filter status/scope.
- `server/local_api.py` baris 1400-1441: submit request mitra dari public form.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI form mitra publik.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI form mitra publik pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Form mitra aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Form mitra aktif.
- Aktivitas yang diselesaikan: Implement UI form mitra publik.
- Bukti screenshot utama: `src/app/components/CollaborationPage.tsx` baris 122: submit payload form mitra ke API.
- Bukti screenshot pendukung 1: `src/app/components/CollaborationPage.tsx` baris 230-241: copy UX flow pengajuan mitra.
- Bukti screenshot pendukung 2: `src/app/components/ModeratorDashboard.tsx` baris 107: fetch inbox collaboration requests.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 122: submit payload form mitra ke API.
- `src/app/components/CollaborationPage.tsx` baris 230-241: copy UX flow pengajuan mitra.
- `src/app/components/ModeratorDashboard.tsx` baris 107: fetch inbox collaboration requests.

### Day 67 (Selasa, 28 Apr 2026): Submit request mitra
Status: [RENCANA]
Milestone/Group: M9: MITRA (W14)
Task Referensi Farchan: Schema & Public API Mitra
Task Referensi Ikram: Landing Page Mitra & Submit FE

#### Entri Farchan (UX+Backend)
Aktivitas: Implement endpoint submit mitra status pending.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement endpoint submit mitra status pending pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Submit mitra sukses' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Submit mitra sukses.
- Aktivitas yang diselesaikan: Implement endpoint submit mitra status pending.
- Bukti screenshot utama: `server/local_api.py` baris 1096-1119: list request mitra dengan filter status/scope.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1400-1441: submit request mitra dari public form.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1476-1490: approval/reject request mitra.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1096-1119: list request mitra dengan filter status/scope.
- `server/local_api.py` baris 1400-1441: submit request mitra dari public form.
- `server/local_api.py` baris 1476-1490: approval/reject request mitra.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi submit request mitra FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi submit request mitra FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Submit mitra sukses' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Submit mitra sukses.
- Aktivitas yang diselesaikan: Integrasi submit request mitra FE.
- Bukti screenshot utama: `src/app/components/CollaborationPage.tsx` baris 230-241: copy UX flow pengajuan mitra.
- Bukti screenshot pendukung 1: `src/app/components/ModeratorDashboard.tsx` baris 107: fetch inbox collaboration requests.
- Bukti screenshot pendukung 2: `src/app/components/ModeratorDashboard.tsx` baris 180: action approve/reject request mitra.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 230-241: copy UX flow pengajuan mitra.
- `src/app/components/ModeratorDashboard.tsx` baris 107: fetch inbox collaboration requests.
- `src/app/components/ModeratorDashboard.tsx` baris 180: action approve/reject request mitra.

### Day 68 (Rabu, 29 Apr 2026): Routing request mitra
Status: [RENCANA]
Milestone/Group: M9: MITRA (W14)
Task Referensi Farchan: Routing & Approval Mitra API
Task Referensi Ikram: Inbox Admin & Review Action FE

#### Entri Farchan (UX+Backend)
Aktivitas: Implement routing request by scope.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement routing request by scope pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Routing request sinkron' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Routing request sinkron.
- Aktivitas yang diselesaikan: Implement routing request by scope.
- Bukti screenshot utama: `server/local_api.py` baris 1400-1441: submit request mitra dari public form.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1476-1490: approval/reject request mitra.
- Bukti screenshot pendukung 2: `src/app/components/CollaborationPage.tsx` baris 122 dan 241: payload submit mitra dan workflow review.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1400-1441: submit request mitra dari public form.
- `server/local_api.py` baris 1476-1490: approval/reject request mitra.
- `src/app/components/CollaborationPage.tsx` baris 122 dan 241: payload submit mitra dan workflow review.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi inbox review moderator FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi inbox review moderator FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Routing request sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Routing request sinkron.
- Aktivitas yang diselesaikan: Integrasi inbox review moderator FE.
- Bukti screenshot utama: `src/app/components/ModeratorDashboard.tsx` baris 107: fetch inbox collaboration requests.
- Bukti screenshot pendukung 1: `src/app/components/ModeratorDashboard.tsx` baris 180: action approve/reject request mitra.
- Bukti screenshot pendukung 2: `src/app/components/FaqPage.tsx` baris 21-22: dokumentasi alur kolaborasi di FE.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 107: fetch inbox collaboration requests.
- `src/app/components/ModeratorDashboard.tsx` baris 180: action approve/reject request mitra.
- `src/app/components/FaqPage.tsx` baris 21-22: dokumentasi alur kolaborasi di FE.

### Day 69 (Kamis, 30 Apr 2026): Approve reject mitra
Status: [RENCANA]
Milestone/Group: M9: MITRA (W14)
Task Referensi Farchan: Routing & Approval Mitra API
Task Referensi Ikram: Inbox Admin & Review Action FE

#### Entri Farchan (UX+Backend)
Aktivitas: Implement approve reject request mitra.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement approve reject request mitra pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Review flow aktif' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Review flow aktif.
- Aktivitas yang diselesaikan: Implement approve reject request mitra.
- Bukti screenshot utama: `server/local_api.py` baris 1476-1490: approval/reject request mitra.
- Bukti screenshot pendukung 1: `src/app/components/CollaborationPage.tsx` baris 122 dan 241: payload submit mitra dan workflow review.
- Bukti screenshot pendukung 2: `src/app/components/ModeratorDashboard.tsx` baris 107 dan 180: inbox + approval collaboration request.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1476-1490: approval/reject request mitra.
- `src/app/components/CollaborationPage.tsx` baris 122 dan 241: payload submit mitra dan workflow review.
- `src/app/components/ModeratorDashboard.tsx` baris 107 dan 180: inbox + approval collaboration request.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement aksi review mitra FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement aksi review mitra FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Review flow aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Review flow aktif.
- Aktivitas yang diselesaikan: Implement aksi review mitra FE.
- Bukti screenshot utama: `src/app/components/ModeratorDashboard.tsx` baris 180: action approve/reject request mitra.
- Bukti screenshot pendukung 1: `src/app/components/FaqPage.tsx` baris 21-22: dokumentasi alur kolaborasi di FE.
- Bukti screenshot pendukung 2: `src/app/components/LandingPage.tsx` baris 99: CTA ke halaman collaboration dari landing.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 180: action approve/reject request mitra.
- `src/app/components/FaqPage.tsx` baris 21-22: dokumentasi alur kolaborasi di FE.
- `src/app/components/LandingPage.tsx` baris 99: CTA ke halaman collaboration dari landing.

### Day 70 (Jumat, 1 Mei 2026): E2E governance mitra
Status: [RENCANA]
Milestone/Group: M9: MITRA (W14)
Task Referensi Farchan: Routing & Approval Mitra API
Task Referensi Ikram: Inbox Admin & Review Action FE

#### Entri Farchan (UX+Backend)
Aktivitas: Uji E2E submit sampai review mitra.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Uji E2E submit sampai review mitra. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M9: MITRA (W14). Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Governance mitra stabil' punya dasar teknis yang jelas."
Output Farchan:
- Deliverable utama hari ini: Governance mitra stabil.
- Aktivitas yang diselesaikan: Uji E2E submit sampai review mitra.
- Bukti screenshot utama: `src/app/components/CollaborationPage.tsx` baris 122 dan 241: payload submit mitra dan workflow review.
- Bukti screenshot pendukung 1: `src/app/components/ModeratorDashboard.tsx` baris 107 dan 180: inbox + approval collaboration request.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 501-568: schema `collaboration_requests` dan migrasi kolom scope.
Lampiran Farchan (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 122 dan 241: payload submit mitra dan workflow review.
- `src/app/components/ModeratorDashboard.tsx` baris 107 dan 180: inbox + approval collaboration request.
- `server/local_api.py` baris 501-568: schema `collaboration_requests` dan migrasi kolom scope.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug mitra di UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug mitra di UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Governance mitra stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Deliverable utama hari ini: Governance mitra stabil.
- Aktivitas yang diselesaikan: Patch bug mitra di UI/FE.
- Bukti screenshot utama: `src/app/components/FaqPage.tsx` baris 21-22: dokumentasi alur kolaborasi di FE.
- Bukti screenshot pendukung 1: `src/app/components/LandingPage.tsx` baris 99: CTA ke halaman collaboration dari landing.
- Bukti screenshot pendukung 2: `src/app/components/CollaborationPage.tsx` baris 122: submit payload form mitra ke API.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/FaqPage.tsx` baris 21-22: dokumentasi alur kolaborasi di FE.
- `src/app/components/LandingPage.tsx` baris 99: CTA ke halaman collaboration dari landing.
- `src/app/components/CollaborationPage.tsx` baris 122: submit payload form mitra ke API.

## PEKAN 15 (W15): Security Hardening

Status Pekan: Proyeksi
Milestone Aktif: M10: SECURITY (W15)
Task Utama: Farchan - Threat Model & Input Validation | Ikram - Audit UI Sensitif & Sync Validasi

### Day 71 (Senin, 4 Mei 2026): Threat modeling
Status: [RENCANA]
Milestone/Group: M10: SECURITY (W15)
Task Referensi Farchan: Threat Model & Input Validation
Task Referensi Ikram: Audit UI Sensitif & Sync Validasi

#### Entri Farchan (UX+Backend)
Aktivitas: Lakukan threat modeling dan checklist attack surface.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Lakukan threat modeling dan checklist attack surface pada konteks 'Threat modeling'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M10: SECURITY (W15). Setelah selesai, saya pastikan 'Daftar risiko keamanan' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Deliverable utama hari ini: Daftar risiko keamanan.
- Aktivitas yang diselesaikan: Lakukan threat modeling dan checklist attack surface.
- Bukti screenshot utama: `server/local_api.py` baris 557-568: migrasi schema untuk keamanan kompatibilitas data.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 24-26 dan 120: security/rate limit baseline konfigurasi backend.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 852-864: cleanup expired temporary adjustments.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 557-568: migrasi schema untuk keamanan kompatibilitas data.
- `server/local_api.py` baris 24-26 dan 120: security/rate limit baseline konfigurasi backend.
- `server/local_api.py` baris 852-864: cleanup expired temporary adjustments.

#### Entri Ikram (UI+Frontend)
Aktivitas: Audit area UI/FE sensitif untuk produksi.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Audit area UI/FE sensitif untuk produksi. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M10: SECURITY (W15). Setelah sinkronisasi final, 'Daftar risiko keamanan' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Deliverable utama hari ini: Daftar risiko keamanan.
- Aktivitas yang diselesaikan: Audit area UI/FE sensitif untuk produksi.
- Bukti screenshot utama: `src/app/App.tsx` baris 159-173: logout request + clear token localStorage.
- Bukti screenshot pendukung 1: `src/lib/api.ts` baris 53-60: handling unauthorized dan standar error object FE.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 56-60: validasi token ke endpoint `auth/me`.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 159-173: logout request + clear token localStorage.
- `src/lib/api.ts` baris 53-60: handling unauthorized dan standar error object FE.
- `src/app/App.tsx` baris 56-60: validasi token ke endpoint `auth/me`.

### Day 72 (Selasa, 5 Mei 2026): Hardening validasi input
Status: [RENCANA]
Milestone/Group: M10: SECURITY (W15)
Task Referensi Farchan: Threat Model & Input Validation
Task Referensi Ikram: Audit UI Sensitif & Sync Validasi

#### Entri Farchan (UX+Backend)
Aktivitas: Perketat input validation backend.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Perketat input validation backend pada konteks 'Hardening validasi input'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M10: SECURITY (W15). Setelah selesai, saya pastikan 'Validasi FE-BE konsisten' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Deliverable utama hari ini: Validasi FE-BE konsisten.
- Aktivitas yang diselesaikan: Perketat input validation backend.
- Bukti screenshot utama: `server/local_api.py` baris 24-26 dan 120: security/rate limit baseline konfigurasi backend.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 852-864: cleanup expired temporary adjustments.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1835-1866: auth guard untuk metode mutasi data.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 24-26 dan 120: security/rate limit baseline konfigurasi backend.
- `server/local_api.py` baris 852-864: cleanup expired temporary adjustments.
- `server/local_api.py` baris 1835-1866: auth guard untuk metode mutasi data.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sinkron validasi input di FE.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Sinkron validasi input di FE. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M10: SECURITY (W15). Setelah sinkronisasi final, 'Validasi FE-BE konsisten' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Deliverable utama hari ini: Validasi FE-BE konsisten.
- Aktivitas yang diselesaikan: Sinkron validasi input di FE.
- Bukti screenshot utama: `src/lib/api.ts` baris 53-60: handling unauthorized dan standar error object FE.
- Bukti screenshot pendukung 1: `src/app/App.tsx` baris 56-60: validasi token ke endpoint `auth/me`.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 183: bind `setOnUnauthorized()` untuk auto logout.
Lampiran Ikram (Bukti Screenshot):
- `src/lib/api.ts` baris 53-60: handling unauthorized dan standar error object FE.
- `src/app/App.tsx` baris 56-60: validasi token ke endpoint `auth/me`.
- `src/app/App.tsx` baris 183: bind `setOnUnauthorized()` untuk auto logout.

### Day 73 (Rabu, 6 Mei 2026): Rate limit dan session policy
Status: [RENCANA]
Milestone/Group: M10: SECURITY (W15)
Task Referensi Farchan: Rate Limit, CORS & Regression
Task Referensi Ikram: Error Handling FE & Responsiveness

#### Entri Farchan (UX+Backend)
Aktivitas: Aktifkan rate limit dan session policy.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Aktifkan rate limit dan session policy pada konteks 'Rate limit dan session policy'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M10: SECURITY (W15). Setelah selesai, saya pastikan 'Throttling flow aman' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Deliverable utama hari ini: Throttling flow aman.
- Aktivitas yang diselesaikan: Aktifkan rate limit dan session policy.
- Bukti screenshot utama: `server/local_api.py` baris 852-864: cleanup expired temporary adjustments.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1835-1866: auth guard untuk metode mutasi data.
- Bukti screenshot pendukung 2: `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: checklist hardening produksi.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 852-864: cleanup expired temporary adjustments.
- `server/local_api.py` baris 1835-1866: auth guard untuk metode mutasi data.
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: checklist hardening produksi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement handling error 429 di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement handling error 429 di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Throttling flow aman' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Throttling flow aman.
- Aktivitas yang diselesaikan: Implement handling error 429 di FE.
- Bukti screenshot utama: `src/app/App.tsx` baris 56-60: validasi token ke endpoint `auth/me`.
- Bukti screenshot pendukung 1: `src/app/App.tsx` baris 183: bind `setOnUnauthorized()` untuk auto logout.
- Bukti screenshot pendukung 2: `src/app/components/LoginPage.tsx` baris 99-103: error auth rendering.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 56-60: validasi token ke endpoint `auth/me`.
- `src/app/App.tsx` baris 183: bind `setOnUnauthorized()` untuk auto logout.
- `src/app/components/LoginPage.tsx` baris 99-103: error auth rendering.

### Day 74 (Kamis, 7 Mei 2026): CORS dan security headers
Status: [RENCANA]
Milestone/Group: M10: SECURITY (W15)
Task Referensi Farchan: Rate Limit, CORS & Regression
Task Referensi Ikram: Error Handling FE & Responsiveness

#### Entri Farchan (UX+Backend)
Aktivitas: Konfigurasi CORS allowlist dan security headers.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Konfigurasi CORS allowlist dan security headers pada konteks 'CORS dan security headers'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M10: SECURITY (W15). Setelah selesai, saya pastikan 'CORS security pass' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Deliverable utama hari ini: CORS security pass.
- Aktivitas yang diselesaikan: Konfigurasi CORS allowlist dan security headers.
- Bukti screenshot utama: `server/local_api.py` baris 1835-1866: auth guard untuk metode mutasi data.
- Bukti screenshot pendukung 1: `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: checklist hardening produksi.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 141-157: `open_sqlite()` dan `connect_db()` untuk integritas akses DB.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1835-1866: auth guard untuk metode mutasi data.
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: checklist hardening produksi.
- `server/local_api.py` baris 141-157: `open_sqlite()` dan `connect_db()` untuk integritas akses DB.

#### Entri Ikram (UI+Frontend)
Aktivitas: Uji perilaku FE pada mode production.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji perilaku FE pada mode production dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'CORS security pass' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Deliverable utama hari ini: CORS security pass.
- Aktivitas yang diselesaikan: Uji perilaku FE pada mode production.
- Bukti screenshot utama: `src/app/App.tsx` baris 183: bind `setOnUnauthorized()` untuk auto logout.
- Bukti screenshot pendukung 1: `src/app/components/LoginPage.tsx` baris 99-103: error auth rendering.
- Bukti screenshot pendukung 2: `src/app/components/AdminLoginPage.tsx` baris 39: error handling login admin.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 183: bind `setOnUnauthorized()` untuk auto logout.
- `src/app/components/LoginPage.tsx` baris 99-103: error auth rendering.
- `src/app/components/AdminLoginPage.tsx` baris 39: error handling login admin.

### Day 75 (Jumat, 8 Mei 2026): Security regression
Status: [RENCANA]
Milestone/Group: M10: SECURITY (W15)
Task Referensi Farchan: Rate Limit, CORS & Regression
Task Referensi Ikram: Error Handling FE & Responsiveness

#### Entri Farchan (UX+Backend)
Aktivitas: Jalankan security regression dan checklist publish.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Jalankan security regression dan checklist publish pada konteks 'Security regression'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M10: SECURITY (W15). Setelah selesai, saya pastikan 'Baseline security siap' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Deliverable utama hari ini: Baseline security siap.
- Aktivitas yang diselesaikan: Jalankan security regression dan checklist publish.
- Bukti screenshot utama: `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: checklist hardening produksi.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 141-157: `open_sqlite()` dan `connect_db()` untuk integritas akses DB.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 557-568: migrasi schema untuk keamanan kompatibilitas data.
Lampiran Farchan (Bukti Screenshot):
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: checklist hardening produksi.
- `server/local_api.py` baris 141-157: `open_sqlite()` dan `connect_db()` untuk integritas akses DB.
- `server/local_api.py` baris 557-568: migrasi schema untuk keamanan kompatibilitas data.

#### Entri Ikram (UI+Frontend)
Aktivitas: Regression FE pasca hardening.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Regression FE pasca hardening untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Baseline security siap' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Deliverable utama hari ini: Baseline security siap.
- Aktivitas yang diselesaikan: Regression FE pasca hardening.
- Bukti screenshot utama: `src/app/components/LoginPage.tsx` baris 99-103: error auth rendering.
- Bukti screenshot pendukung 1: `src/app/components/AdminLoginPage.tsx` baris 39: error handling login admin.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 159-173: logout request + clear token localStorage.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 99-103: error auth rendering.
- `src/app/components/AdminLoginPage.tsx` baris 39: error handling login admin.
- `src/app/App.tsx` baris 159-173: logout request + clear token localStorage.

## PEKAN 16 (W16): Integrasi Total

Status Pekan: Proyeksi
Milestone Aktif: M11: INTEGRATION (W16)
Task Utama: Berdua - Lintas Modul & Skenario Demo

### Day 76 (Senin, 11 Mei 2026): Integrasi lintas modul round 1
Status: [RENCANA]
Milestone/Group: M11: INTEGRATION (W16)
Task Referensi Berdua: Lintas Modul & Skenario Demo

#### Entri Farchan (UX+Backend)
Aktivitas: Integrasi modul lintas domain round 1.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi modul lintas domain round 1 pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Integrasi lintas modul' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Deliverable utama hari ini: Integrasi lintas modul.
- Aktivitas yang diselesaikan: Integrasi modul lintas domain round 1.
- Bukti screenshot utama: `src/app/App.tsx` baris 279-303: mount dashboard per role (user/moderator/admin).
- Bukti screenshot pendukung 1: `DEMO_ACCOUNTS.md` baris 10-26: akun demo multi-role untuk skenario integrasi.
- Bukti screenshot pendukung 2: `scripts/dev-local.mjs` baris 19-29: bootstrap process FE-BE lokal untuk integrasi.
Lampiran Farchan (Bukti Screenshot):
- `src/app/App.tsx` baris 279-303: mount dashboard per role (user/moderator/admin).
- `DEMO_ACCOUNTS.md` baris 10-26: akun demo multi-role untuk skenario integrasi.
- `scripts/dev-local.mjs` baris 19-29: bootstrap process FE-BE lokal untuk integrasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi UI+FE round 1.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi UI+FE round 1 pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Integrasi lintas modul' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Deliverable utama hari ini: Integrasi lintas modul.
- Aktivitas yang diselesaikan: Integrasi UI+FE round 1.
- Bukti screenshot utama: `src/app/components/AdminDashboard.tsx` baris 72-78: integrasi fetch event/report admin.
- Bukti screenshot pendukung 1: `DEMO_ACCOUNTS.md` baris 10-26: akun dan skenario demo multi-role.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 205-216: switch context view antar role.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 72-78: integrasi fetch event/report admin.
- `DEMO_ACCOUNTS.md` baris 10-26: akun dan skenario demo multi-role.
- `src/app/App.tsx` baris 205-216: switch context view antar role.

### Day 77 (Selasa, 12 Mei 2026): Skenario demo role
Status: [RENCANA]
Milestone/Group: M11: INTEGRATION (W16)
Task Referensi Berdua: Lintas Modul & Skenario Demo

#### Entri Farchan (UX+Backend)
Aktivitas: Susun skenario demo per role.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun skenario demo per role dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Script demo v1' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Deliverable utama hari ini: Script demo v1.
- Aktivitas yang diselesaikan: Susun skenario demo per role.
- Bukti screenshot utama: `DEMO_ACCOUNTS.md` baris 10-26: akun demo multi-role untuk skenario integrasi.
- Bukti screenshot pendukung 1: `scripts/dev-local.mjs` baris 19-29: bootstrap process FE-BE lokal untuk integrasi.
- Bukti screenshot pendukung 2: `scripts/dev-local.mjs` baris 45-56: controlled shutdown untuk mencegah DB corruption.
Lampiran Farchan (Bukti Screenshot):
- `DEMO_ACCOUNTS.md` baris 10-26: akun demo multi-role untuk skenario integrasi.
- `scripts/dev-local.mjs` baris 19-29: bootstrap process FE-BE lokal untuk integrasi.
- `scripts/dev-local.mjs` baris 45-56: controlled shutdown untuk mencegah DB corruption.

#### Entri Ikram (UI+Frontend)
Aktivitas: Siapkan alur demo di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Siapkan alur demo di FE dalam konteks 'Skenario demo role'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M11: INTEGRATION (W16). Hasil 'Script demo v1' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Script demo v1.
- Aktivitas yang diselesaikan: Siapkan alur demo di FE.
- Bukti screenshot utama: `DEMO_ACCOUNTS.md` baris 10-26: akun dan skenario demo multi-role.
- Bukti screenshot pendukung 1: `src/app/App.tsx` baris 205-216: switch context view antar role.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 279-303: dashboard mount per role untuk demo.
Lampiran Ikram (Bukti Screenshot):
- `DEMO_ACCOUNTS.md` baris 10-26: akun dan skenario demo multi-role.
- `src/app/App.tsx` baris 205-216: switch context view antar role.
- `src/app/App.tsx` baris 279-303: dashboard mount per role untuk demo.

### Day 78 (Rabu, 13 Mei 2026): Seed data demo
Status: [RENCANA]
Milestone/Group: M11: INTEGRATION (W16)
Task Referensi Berdua: Seed Data & Candidate Build

#### Entri Farchan (UX+Backend)
Aktivitas: Siapkan seed data demo realistis.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Siapkan seed data demo realistis pada konteks 'Seed data demo'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M11: INTEGRATION (W16). Setelah selesai, saya pastikan 'Demo data siap' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Deliverable utama hari ini: Demo data siap.
- Aktivitas yang diselesaikan: Siapkan seed data demo realistis.
- Bukti screenshot utama: `scripts/dev-local.mjs` baris 19-29: bootstrap process FE-BE lokal untuk integrasi.
- Bukti screenshot pendukung 1: `scripts/dev-local.mjs` baris 45-56: controlled shutdown untuk mencegah DB corruption.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1904: runtime output base URL dan DB path.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 19-29: bootstrap process FE-BE lokal untuk integrasi.
- `scripts/dev-local.mjs` baris 45-56: controlled shutdown untuk mencegah DB corruption.
- `server/local_api.py` baris 1904: runtime output base URL dan DB path.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sinkron tampilan FE dengan seed data.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Sinkron tampilan FE dengan seed data. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M11: INTEGRATION (W16). Setelah sinkronisasi final, 'Demo data siap' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Deliverable utama hari ini: Demo data siap.
- Aktivitas yang diselesaikan: Sinkron tampilan FE dengan seed data.
- Bukti screenshot utama: `src/app/App.tsx` baris 205-216: switch context view antar role.
- Bukti screenshot pendukung 1: `src/app/App.tsx` baris 279-303: dashboard mount per role untuk demo.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 49-59: integrasi fetch event/report user.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 205-216: switch context view antar role.
- `src/app/App.tsx` baris 279-303: dashboard mount per role untuk demo.
- `src/app/components/UserDashboard.tsx` baris 49-59: integrasi fetch event/report user.

### Day 79 (Kamis, 14 Mei 2026): Dry run UAT internal
Status: [RENCANA]
Milestone/Group: M11: INTEGRATION (W16)
Task Referensi Berdua: Seed Data & Candidate Build

#### Entri Farchan (UX+Backend)
Aktivitas: Lakukan dry run UAT internal.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Lakukan dry run UAT internal. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'UAT dry-run notes' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: UAT dry-run notes.
- Aktivitas yang diselesaikan: Lakukan dry run UAT internal.
- Bukti screenshot utama: `scripts/dev-local.mjs` baris 45-56: controlled shutdown untuk mencegah DB corruption.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1904: runtime output base URL dan DB path.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 205-216: switch view lintas role pada app shell.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 45-56: controlled shutdown untuk mencegah DB corruption.
- `server/local_api.py` baris 1904: runtime output base URL dan DB path.
- `src/app/App.tsx` baris 205-216: switch view lintas role pada app shell.

#### Entri Ikram (UI+Frontend)
Aktivitas: Polish UI/FE untuk demo.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Polish UI/FE untuk demo dalam konteks 'Dry run UAT internal'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M11: INTEGRATION (W16). Hasil 'UAT dry-run notes' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: UAT dry-run notes.
- Aktivitas yang diselesaikan: Polish UI/FE untuk demo.
- Bukti screenshot utama: `src/app/App.tsx` baris 279-303: dashboard mount per role untuk demo.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 49-59: integrasi fetch event/report user.
- Bukti screenshot pendukung 2: `src/app/components/ModeratorDashboard.tsx` baris 127-151: integrasi fetch moderation data.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 279-303: dashboard mount per role untuk demo.
- `src/app/components/UserDashboard.tsx` baris 49-59: integrasi fetch event/report user.
- `src/app/components/ModeratorDashboard.tsx` baris 127-151: integrasi fetch moderation data.

### Day 80 (Jumat, 15 Mei 2026): Freeze candidate build
Status: [RENCANA]
Milestone/Group: M11: INTEGRATION (W16)
Task Referensi Berdua: Seed Data & Candidate Build

#### Entri Farchan (UX+Backend)
Aktivitas: Freeze candidate build backend.
Uraian Kegiatan (Logbook):
"Hari ini fokus saya di 'Freeze candidate build' adalah Freeze candidate build backend. Saya mulai dengan ngerapihin backlog dan dependency backend biar batas kerja sprint jelas, lalu mengunci keputusan teknis yang paling ngaruh ke alur lanjutan. Sebelum close, saya validasi lagi keputusan yang diambil supaya output hari ini 'Candidate build' bisa langsung dipakai tim tanpa ambigu."
Output Farchan:
- Deliverable utama hari ini: Candidate build.
- Aktivitas yang diselesaikan: Freeze candidate build backend.
- Bukti screenshot utama: `server/local_api.py` baris 1904: runtime output base URL dan DB path.
- Bukti screenshot pendukung 1: `src/app/App.tsx` baris 205-216: switch view lintas role pada app shell.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 279-303: mount dashboard per role (user/moderator/admin).
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1904: runtime output base URL dan DB path.
- `src/app/App.tsx` baris 205-216: switch view lintas role pada app shell.
- `src/app/App.tsx` baris 279-303: mount dashboard per role (user/moderator/admin).

#### Entri Ikram (UI+Frontend)
Aktivitas: Final FE polish candidate.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Final FE polish candidate sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Candidate build' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Deliverable utama hari ini: Candidate build.
- Aktivitas yang diselesaikan: Final FE polish candidate.
- Bukti screenshot utama: `src/app/components/UserDashboard.tsx` baris 49-59: integrasi fetch event/report user.
- Bukti screenshot pendukung 1: `src/app/components/ModeratorDashboard.tsx` baris 127-151: integrasi fetch moderation data.
- Bukti screenshot pendukung 2: `src/app/components/AdminDashboard.tsx` baris 72-78: integrasi fetch event/report admin.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 49-59: integrasi fetch event/report user.
- `src/app/components/ModeratorDashboard.tsx` baris 127-151: integrasi fetch moderation data.
- `src/app/components/AdminDashboard.tsx` baris 72-78: integrasi fetch event/report admin.

## PEKAN 17 (W17): QA Execution

Status Pekan: Proyeksi
Milestone Aktif: M12: QA EXECUTION (W17)
Task Utama: Berdua - Test Plan & QA Tahap 1

### Day 81 (Senin, 18 Mei 2026): Finalisasi test case
Status: [RENCANA]
Milestone/Group: M12: QA EXECUTION (W17)
Task Referensi Berdua: Test Plan & QA Tahap 1

#### Entri Farchan (UX+Backend)
Aktivitas: Finalisasi test case backend.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalisasi test case backend sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Test plan final' benar-benar siap dipakai."
Output Farchan:
- Deliverable utama hari ini: Test plan final.
- Aktivitas yang diselesaikan: Finalisasi test case backend.
- Bukti screenshot utama: `docs/guides/QUICKSTART.md` baris 218-227: smoke test checklist auth-event-report.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1202-1694: area endpoint inti yang diretest saat bugfix.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.
Lampiran Farchan (Bukti Screenshot):
- `docs/guides/QUICKSTART.md` baris 218-227: smoke test checklist auth-event-report.
- `server/local_api.py` baris 1202-1694: area endpoint inti yang diretest saat bugfix.
- `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalisasi test case UI/FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalisasi test case UI/FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Test plan final' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Deliverable utama hari ini: Test plan final.
- Aktivitas yang diselesaikan: Finalisasi test case UI/FE.
- Bukti screenshot utama: `src/app/components/ReportingWizard.tsx` baris 92: retest submit report.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 239-264: retest leaderboard rendering.
- Bukti screenshot pendukung 2: `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 92: retest submit report.
- `src/app/components/UserDashboard.tsx` baris 239-264: retest leaderboard rendering.
- `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.

### Day 82 (Selasa, 19 Mei 2026): Eksekusi test domain inti
Status: [RENCANA]
Milestone/Group: M12: QA EXECUTION (W17)
Task Referensi Berdua: Test Plan & QA Tahap 1

#### Entri Farchan (UX+Backend)
Aktivitas: Eksekusi test auth event report.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Eksekusi test auth event report. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Laporan uji harian' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Laporan uji harian.
- Aktivitas yang diselesaikan: Eksekusi test auth event report.
- Bukti screenshot utama: `server/local_api.py` baris 1202-1694: area endpoint inti yang diretest saat bugfix.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.
- Bukti screenshot pendukung 2: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1202-1694: area endpoint inti yang diretest saat bugfix.
- `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.

#### Entri Ikram (UI+Frontend)
Aktivitas: QA responsive dan flow FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke QA responsive dan flow FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Laporan uji harian' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Deliverable utama hari ini: Laporan uji harian.
- Aktivitas yang diselesaikan: QA responsive dan flow FE.
- Bukti screenshot utama: `src/app/components/UserDashboard.tsx` baris 239-264: retest leaderboard rendering.
- Bukti screenshot pendukung 1: `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.
- Bukti screenshot pendukung 2: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 239-264: retest leaderboard rendering.
- `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.

### Day 83 (Rabu, 20 Mei 2026): Eksekusi test domain lanjutan
Status: [RENCANA]
Milestone/Group: M12: QA EXECUTION (W17)
Task Referensi Berdua: QA Tahap 2 & Triage Bug

#### Entri Farchan (UX+Backend)
Aktivitas: Eksekusi test verify reward mitra.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Eksekusi test verify reward mitra. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Defect list update' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Defect list update.
- Aktivitas yang diselesaikan: Eksekusi test verify reward mitra.
- Bukti screenshot utama: `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.
- Bukti screenshot pendukung 1: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.
- Bukti screenshot pendukung 2: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage severity dan owner patch.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage severity dan owner patch.

#### Entri Ikram (UI+Frontend)
Aktivitas: QA usability dan edge-case FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke QA usability dan edge-case FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Defect list update' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Deliverable utama hari ini: Defect list update.
- Aktivitas yang diselesaikan: QA usability dan edge-case FE.
- Bukti screenshot utama: `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.
- Bukti screenshot pendukung 1: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.
- Bukti screenshot pendukung 2: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas defect dan owner patch.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas defect dan owner patch.

### Day 84 (Kamis, 21 Mei 2026): Triage defect
Status: [RENCANA]
Milestone/Group: M12: QA EXECUTION (W17)
Task Referensi Berdua: QA Tahap 2 & Triage Bug

#### Entri Farchan (UX+Backend)
Aktivitas: Triage defect berdasarkan severity dan owner.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Triage defect berdasarkan severity dan owner pada konteks 'Triage defect'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M12: QA EXECUTION (W17). Setelah selesai, saya pastikan 'Bugboard terurut' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Deliverable utama hari ini: Bugboard terurut.
- Aktivitas yang diselesaikan: Triage defect berdasarkan severity dan owner.
- Bukti screenshot utama: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.
- Bukti screenshot pendukung 1: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage severity dan owner patch.
- Bukti screenshot pendukung 2: `docs/status/SYSTEM_SUMMARY.md` baris 166-195: endpoint checklist untuk test coverage.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage severity dan owner patch.
- `docs/status/SYSTEM_SUMMARY.md` baris 166-195: endpoint checklist untuk test coverage.

#### Entri Ikram (UI+Frontend)
Aktivitas: Reproduksi bug dan kumpulkan evidence FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Reproduksi bug dan kumpulkan evidence FE dalam konteks 'Triage defect'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M12: QA EXECUTION (W17). Hasil 'Bugboard terurut' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Bugboard terurut.
- Aktivitas yang diselesaikan: Reproduksi bug dan kumpulkan evidence FE.
- Bukti screenshot utama: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.
- Bukti screenshot pendukung 1: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas defect dan owner patch.
- Bukti screenshot pendukung 2: `src/app/components/EventList.tsx` baris 42-43: retest flow join event.
Lampiran Ikram (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas defect dan owner patch.
- `src/app/components/EventList.tsx` baris 42-43: retest flow join event.

### Day 85 (Jumat, 22 Mei 2026): Patch plan W18
Status: [RENCANA]
Milestone/Group: M12: QA EXECUTION (W17)
Task Referensi Berdua: QA Tahap 2 & Triage Bug

#### Entri Farchan (UX+Backend)
Aktivitas: Susun patch plan untuk W18.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun patch plan untuk W18 dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Rencana patch final' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Deliverable utama hari ini: Rencana patch final.
- Aktivitas yang diselesaikan: Susun patch plan untuk W18.
- Bukti screenshot utama: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage severity dan owner patch.
- Bukti screenshot pendukung 1: `docs/status/SYSTEM_SUMMARY.md` baris 166-195: endpoint checklist untuk test coverage.
- Bukti screenshot pendukung 2: `docs/guides/QUICKSTART.md` baris 218-227: smoke test checklist auth-event-report.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage severity dan owner patch.
- `docs/status/SYSTEM_SUMMARY.md` baris 166-195: endpoint checklist untuk test coverage.
- `docs/guides/QUICKSTART.md` baris 218-227: smoke test checklist auth-event-report.

#### Entri Ikram (UI+Frontend)
Aktivitas: Susun patch plan UI/FE untuk W18.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun patch plan UI/FE untuk W18 dengan nentuin struktur UI, prioritas aksi pengguna, dan kebutuhan data tiap layar. Saya pastikan keputusan desainnya tetap implementable di FE, bukan berhenti di visual saja. Output 'Rencana patch final' saya susun biar tim bisa lanjut kerja dengan acuan yang konkret."
Output Ikram:
- Deliverable utama hari ini: Rencana patch final.
- Aktivitas yang diselesaikan: Susun patch plan UI/FE untuk W18.
- Bukti screenshot utama: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas defect dan owner patch.
- Bukti screenshot pendukung 1: `src/app/components/EventList.tsx` baris 42-43: retest flow join event.
- Bukti screenshot pendukung 2: `src/app/components/ReportingWizard.tsx` baris 92: retest submit report.
Lampiran Ikram (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas defect dan owner patch.
- `src/app/components/EventList.tsx` baris 42-43: retest flow join event.
- `src/app/components/ReportingWizard.tsx` baris 92: retest submit report.

## PEKAN 18 (W18): Bug Fixing

Status Pekan: Proyeksi
Milestone Aktif: M13: BUG FIXING (W18)
Task Utama: Berdua - Fix High/Critical Bugs

### Day 86 (Senin, 25 Mei 2026): Fix high severity
Status: [RENCANA]
Milestone/Group: M13: BUG FIXING (W18)
Task Referensi Berdua: Fix High/Critical Bugs

#### Entri Farchan (UX+Backend)
Aktivitas: Fix bug high severity backend.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug high severity backend untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Patch high severity' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Deliverable utama hari ini: Patch high severity.
- Aktivitas yang diselesaikan: Fix bug high severity backend.
- Bukti screenshot utama: `docs/status/SYSTEM_SUMMARY.md` baris 166-195: endpoint checklist untuk test coverage.
- Bukti screenshot pendukung 1: `docs/guides/QUICKSTART.md` baris 218-227: smoke test checklist auth-event-report.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1202-1694: area endpoint inti yang diretest saat bugfix.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/SYSTEM_SUMMARY.md` baris 166-195: endpoint checklist untuk test coverage.
- `docs/guides/QUICKSTART.md` baris 218-227: smoke test checklist auth-event-report.
- `server/local_api.py` baris 1202-1694: area endpoint inti yang diretest saat bugfix.

#### Entri Ikram (UI+Frontend)
Aktivitas: Fix bug high severity UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug high severity UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Patch high severity' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Deliverable utama hari ini: Patch high severity.
- Aktivitas yang diselesaikan: Fix bug high severity UI/FE.
- Bukti screenshot utama: `src/app/components/EventList.tsx` baris 42-43: retest flow join event.
- Bukti screenshot pendukung 1: `src/app/components/ReportingWizard.tsx` baris 92: retest submit report.
- Bukti screenshot pendukung 2: `src/app/components/UserDashboard.tsx` baris 239-264: retest leaderboard rendering.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: retest flow join event.
- `src/app/components/ReportingWizard.tsx` baris 92: retest submit report.
- `src/app/components/UserDashboard.tsx` baris 239-264: retest leaderboard rendering.

### Day 87 (Selasa, 26 Mei 2026): Fix medium batch 1
Status: [RENCANA]
Milestone/Group: M13: BUG FIXING (W18)
Task Referensi Berdua: Fix High/Critical Bugs

#### Entri Farchan (UX+Backend)
Aktivitas: Fix bug medium batch 1 backend.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug medium batch 1 backend untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Patch medium batch 1' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Deliverable utama hari ini: Patch medium batch 1.
- Aktivitas yang diselesaikan: Fix bug medium batch 1 backend.
- Bukti screenshot utama: `docs/guides/QUICKSTART.md` baris 218-227: smoke test checklist auth-event-report.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1202-1694: area endpoint inti yang diretest saat bugfix.
- Bukti screenshot pendukung 2: `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.
Lampiran Farchan (Bukti Screenshot):
- `docs/guides/QUICKSTART.md` baris 218-227: smoke test checklist auth-event-report.
- `server/local_api.py` baris 1202-1694: area endpoint inti yang diretest saat bugfix.
- `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.

#### Entri Ikram (UI+Frontend)
Aktivitas: Fix bug medium batch 1 UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug medium batch 1 UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Patch medium batch 1' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Deliverable utama hari ini: Patch medium batch 1.
- Aktivitas yang diselesaikan: Fix bug medium batch 1 UI/FE.
- Bukti screenshot utama: `src/app/components/ReportingWizard.tsx` baris 92: retest submit report.
- Bukti screenshot pendukung 1: `src/app/components/UserDashboard.tsx` baris 239-264: retest leaderboard rendering.
- Bukti screenshot pendukung 2: `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 92: retest submit report.
- `src/app/components/UserDashboard.tsx` baris 239-264: retest leaderboard rendering.
- `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.

### Day 88 (Rabu, 27 Mei 2026): Retest patch
Status: [RENCANA]
Milestone/Group: M13: BUG FIXING (W18)
Task Referensi Berdua: Fix Medium & Retest Stabil

#### Entri Farchan (UX+Backend)
Aktivitas: Retest patch backend.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest patch backend. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Retest report' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Retest report.
- Aktivitas yang diselesaikan: Retest patch backend.
- Bukti screenshot utama: `server/local_api.py` baris 1202-1694: area endpoint inti yang diretest saat bugfix.
- Bukti screenshot pendukung 1: `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.
- Bukti screenshot pendukung 2: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1202-1694: area endpoint inti yang diretest saat bugfix.
- `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.

#### Entri Ikram (UI+Frontend)
Aktivitas: Retest patch FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest patch FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Retest report' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Deliverable utama hari ini: Retest report.
- Aktivitas yang diselesaikan: Retest patch FE.
- Bukti screenshot utama: `src/app/components/UserDashboard.tsx` baris 239-264: retest leaderboard rendering.
- Bukti screenshot pendukung 1: `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.
- Bukti screenshot pendukung 2: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 239-264: retest leaderboard rendering.
- `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.

### Day 89 (Kamis, 28 Mei 2026): Fix critical path sisa
Status: [RENCANA]
Milestone/Group: M13: BUG FIXING (W18)
Task Referensi Berdua: Fix Medium & Retest Stabil

#### Entri Farchan (UX+Backend)
Aktivitas: Fix sisa bug critical path backend.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix sisa bug critical path backend untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Patch critical closed' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Deliverable utama hari ini: Patch critical closed.
- Aktivitas yang diselesaikan: Fix sisa bug critical path backend.
- Bukti screenshot utama: `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.
- Bukti screenshot pendukung 1: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.
- Bukti screenshot pendukung 2: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage severity dan owner patch.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1700-1760: verify/assign-role path untuk regression test.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage severity dan owner patch.

#### Entri Ikram (UI+Frontend)
Aktivitas: Fix sisa bug critical path UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix sisa bug critical path UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Patch critical closed' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Deliverable utama hari ini: Patch critical closed.
- Aktivitas yang diselesaikan: Fix sisa bug critical path UI/FE.
- Bukti screenshot utama: `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.
- Bukti screenshot pendukung 1: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.
- Bukti screenshot pendukung 2: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas defect dan owner patch.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 366-428: retest verify report admin flow.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas defect dan owner patch.

### Day 90 (Jumat, 29 Mei 2026): Stabilization build
Status: [RENCANA]
Milestone/Group: M13: BUG FIXING (W18)
Task Referensi Berdua: Fix Medium & Retest Stabil

#### Entri Farchan (UX+Backend)
Aktivitas: Susun stabilization build backend.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun stabilization build backend dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Stabilization build final' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Deliverable utama hari ini: Stabilization build final.
- Aktivitas yang diselesaikan: Susun stabilization build backend.
- Bukti screenshot utama: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.
- Bukti screenshot pendukung 1: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage severity dan owner patch.
- Bukti screenshot pendukung 2: `docs/status/SYSTEM_SUMMARY.md` baris 166-195: endpoint checklist untuk test coverage.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue untuk eksekusi QA harian.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage severity dan owner patch.
- `docs/status/SYSTEM_SUMMARY.md` baris 166-195: endpoint checklist untuk test coverage.

#### Entri Ikram (UI+Frontend)
Aktivitas: Stabilization pass UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilization pass UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Stabilization build final' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Deliverable utama hari ini: Stabilization build final.
- Aktivitas yang diselesaikan: Stabilization pass UI/FE.
- Bukti screenshot utama: `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.
- Bukti screenshot pendukung 1: `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas defect dan owner patch.
- Bukti screenshot pendukung 2: `src/app/components/EventList.tsx` baris 42-43: retest flow join event.
Lampiran Ikram (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar bug dan testcase uji.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas defect dan owner patch.
- `src/app/components/EventList.tsx` baris 42-43: retest flow join event.

## PEKAN 19 (W19): Dokumen dan Pitch

Status Pekan: Proyeksi
Milestone Aktif: M14: DOCS & PITCH (W19)
Task Utama: Farchan - Update Bab KP & Bukti Teknis | Ikram - Capture UI & Rapikan Aset FE

### Day 91 (Senin, 1 Jun 2026): Update dokumen final
Status: [RENCANA]
Milestone/Group: M14: DOCS & PITCH (W19)
Task Referensi Farchan: Update Bab KP & Bukti Teknis
Task Referensi Ikram: Capture UI & Rapikan Aset FE

#### Entri Farchan (UX+Backend)
Aktivitas: Update grand design final berbasis implementasi.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Update grand design final berbasis implementasi sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Dokumen + visual final' benar-benar siap dipakai."
Output Farchan:
- Deliverable utama hari ini: Dokumen + visual final.
- Aktivitas yang diselesaikan: Update grand design final berbasis implementasi.
- Bukti screenshot utama: `docs/guides/README_SIMRP.md` baris 175-193: endpoint matrix untuk dokumen teknis.
- Bukti screenshot pendukung 1: `docs/guides/QUICKSTART.md` baris 237-251: rujukan runbook dan user guide.
- Bukti screenshot pendukung 2: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP, UAT, dan next steps.
Lampiran Farchan (Bukti Screenshot):
- `docs/guides/README_SIMRP.md` baris 175-193: endpoint matrix untuk dokumen teknis.
- `docs/guides/QUICKSTART.md` baris 237-251: rujukan runbook dan user guide.
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP, UAT, dan next steps.

#### Entri Ikram (UI+Frontend)
Aktivitas: Siapkan capture UI dan flow final.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Siapkan capture UI dan flow final sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Dokumen + visual final' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Deliverable utama hari ini: Dokumen + visual final.
- Aktivitas yang diselesaikan: Siapkan capture UI dan flow final.
- Bukti screenshot utama: `docs/guides/QUICKSTART.md` baris 218-227: checklist uji final untuk dokumentasi.
- Bukti screenshot pendukung 1: `docs/guides/README_SIMRP.md` baris 148-157: daftar komponen FE untuk lampiran laporan.
- Bukti screenshot pendukung 2: `docs/guides/README_SIMRP.md` baris 175-193: API matrix untuk slide teknis.
Lampiran Ikram (Bukti Screenshot):
- `docs/guides/QUICKSTART.md` baris 218-227: checklist uji final untuk dokumentasi.
- `docs/guides/README_SIMRP.md` baris 148-157: daftar komponen FE untuk lampiran laporan.
- `docs/guides/README_SIMRP.md` baris 175-193: API matrix untuk slide teknis.

### Day 92 (Selasa, 2 Jun 2026): Finalisasi logbook bukti
Status: [RENCANA]
Milestone/Group: M14: DOCS & PITCH (W19)
Task Referensi Farchan: Update Bab KP & Bukti Teknis
Task Referensi Ikram: Capture UI & Rapikan Aset FE

#### Entri Farchan (UX+Backend)
Aktivitas: Finalisasi logbook dan bukti teknis.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalisasi logbook dan bukti teknis sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Arsip bukti siap' benar-benar siap dipakai."
Output Farchan:
- Deliverable utama hari ini: Arsip bukti siap.
- Aktivitas yang diselesaikan: Finalisasi logbook dan bukti teknis.
- Bukti screenshot utama: `docs/guides/QUICKSTART.md` baris 237-251: rujukan runbook dan user guide.
- Bukti screenshot pendukung 1: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP, UAT, dan next steps.
- Bukti screenshot pendukung 2: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: target fase akhir W17-W20.
Lampiran Farchan (Bukti Screenshot):
- `docs/guides/QUICKSTART.md` baris 237-251: rujukan runbook dan user guide.
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP, UAT, dan next steps.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: target fase akhir W17-W20.

#### Entri Ikram (UI+Frontend)
Aktivitas: Rapikan file desain dan aset FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Rapikan file desain dan aset FE dalam konteks 'Finalisasi logbook bukti'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M14: DOCS & PITCH (W19). Hasil 'Arsip bukti siap' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Arsip bukti siap.
- Aktivitas yang diselesaikan: Rapikan file desain dan aset FE.
- Bukti screenshot utama: `docs/guides/README_SIMRP.md` baris 148-157: daftar komponen FE untuk lampiran laporan.
- Bukti screenshot pendukung 1: `docs/guides/README_SIMRP.md` baris 175-193: API matrix untuk slide teknis.
- Bukti screenshot pendukung 2: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP dan readiness.
Lampiran Ikram (Bukti Screenshot):
- `docs/guides/README_SIMRP.md` baris 148-157: daftar komponen FE untuk lampiran laporan.
- `docs/guides/README_SIMRP.md` baris 175-193: API matrix untuk slide teknis.
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP dan readiness.

### Day 93 (Rabu, 3 Jun 2026): Finalisasi narasi presentasi
Status: [RENCANA]
Milestone/Group: M14: DOCS & PITCH (W19)
Task Referensi Farchan: Script Pitch & Rehearsal QnA
Task Referensi Ikram: Deck PPT & Video Demo Flow

#### Entri Farchan (UX+Backend)
Aktivitas: Finalisasi narasi presentasi dan script.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalisasi narasi presentasi dan script sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Draft deck final' benar-benar siap dipakai."
Output Farchan:
- Deliverable utama hari ini: Draft deck final.
- Aktivitas yang diselesaikan: Finalisasi narasi presentasi dan script.
- Bukti screenshot utama: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP, UAT, dan next steps.
- Bukti screenshot pendukung 1: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: target fase akhir W17-W20.
- Bukti screenshot pendukung 2: `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkron role/team untuk laporan.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP, UAT, dan next steps.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: target fase akhir W17-W20.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkron role/team untuk laporan.

#### Entri Ikram (UI+Frontend)
Aktivitas: Siapkan visual slide dan video demo FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Siapkan visual slide dan video demo FE dalam konteks 'Finalisasi narasi presentasi'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M14: DOCS & PITCH (W19). Hasil 'Draft deck final' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Draft deck final.
- Aktivitas yang diselesaikan: Siapkan visual slide dan video demo FE.
- Bukti screenshot utama: `docs/guides/README_SIMRP.md` baris 175-193: API matrix untuk slide teknis.
- Bukti screenshot pendukung 1: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP dan readiness.
- Bukti screenshot pendukung 2: `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkronisasi kontribusi tim.
Lampiran Ikram (Bukti Screenshot):
- `docs/guides/README_SIMRP.md` baris 175-193: API matrix untuk slide teknis.
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP dan readiness.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkronisasi kontribusi tim.

### Day 94 (Kamis, 4 Jun 2026): Rehearsal presentasi
Status: [RENCANA]
Milestone/Group: M14: DOCS & PITCH (W19)
Task Referensi Farchan: Script Pitch & Rehearsal QnA
Task Referensi Ikram: Deck PPT & Video Demo Flow

#### Entri Farchan (UX+Backend)
Aktivitas: Rehearsal presentasi dan QnA bank.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Rehearsal presentasi dan QnA bank. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Rehearsal notes' valid secara operasional."
Output Farchan:
- Deliverable utama hari ini: Rehearsal notes.
- Aktivitas yang diselesaikan: Rehearsal presentasi dan QnA bank.
- Bukti screenshot utama: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: target fase akhir W17-W20.
- Bukti screenshot pendukung 1: `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkron role/team untuk laporan.
- Bukti screenshot pendukung 2: `README.md` baris 17-29: peta dokumentasi final dan handover package.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: target fase akhir W17-W20.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkron role/team untuk laporan.
- `README.md` baris 17-29: peta dokumentasi final dan handover package.

#### Entri Ikram (UI+Frontend)
Aktivitas: Rehearsal flow demo di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Rehearsal flow demo di FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Rehearsal notes' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Deliverable utama hari ini: Rehearsal notes.
- Aktivitas yang diselesaikan: Rehearsal flow demo di FE.
- Bukti screenshot utama: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP dan readiness.
- Bukti screenshot pendukung 1: `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkronisasi kontribusi tim.
- Bukti screenshot pendukung 2: `README.md` baris 17-29: peta dokumen final dan handover.
Lampiran Ikram (Bukti Screenshot):
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status MVP dan readiness.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkronisasi kontribusi tim.
- `README.md` baris 17-29: peta dokumen final dan handover.

### Day 95 (Jumat, 5 Jun 2026): Revisi paket sidang
Status: [RENCANA]
Milestone/Group: M14: DOCS & PITCH (W19)
Task Referensi Farchan: Script Pitch & Rehearsal QnA
Task Referensi Ikram: Deck PPT & Video Demo Flow

#### Entri Farchan (UX+Backend)
Aktivitas: Revisi final dokumen KP.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Revisi final dokumen KP sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Paket sidang siap' benar-benar siap dipakai."
Output Farchan:
- Deliverable utama hari ini: Paket sidang siap.
- Aktivitas yang diselesaikan: Revisi final dokumen KP.
- Bukti screenshot utama: `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkron role/team untuk laporan.
- Bukti screenshot pendukung 1: `README.md` baris 17-29: peta dokumentasi final dan handover package.
- Bukti screenshot pendukung 2: `docs/guides/README_SIMRP.md` baris 175-193: endpoint matrix untuk dokumen teknis.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkron role/team untuk laporan.
- `README.md` baris 17-29: peta dokumentasi final dan handover package.
- `docs/guides/README_SIMRP.md` baris 175-193: endpoint matrix untuk dokumen teknis.

#### Entri Ikram (UI+Frontend)
Aktivitas: Revisi final visual dan flow FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Revisi final visual dan flow FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Paket sidang siap' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Deliverable utama hari ini: Paket sidang siap.
- Aktivitas yang diselesaikan: Revisi final visual dan flow FE.
- Bukti screenshot utama: `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkronisasi kontribusi tim.
- Bukti screenshot pendukung 1: `README.md` baris 17-29: peta dokumen final dan handover.
- Bukti screenshot pendukung 2: `docs/guides/QUICKSTART.md` baris 218-227: checklist uji final untuk dokumentasi.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 53-60: sinkronisasi kontribusi tim.
- `README.md` baris 17-29: peta dokumen final dan handover.
- `docs/guides/QUICKSTART.md` baris 218-227: checklist uji final untuk dokumentasi.

## PEKAN 20 (W20): UAT Final dan Closing

Status Pekan: Proyeksi
Milestone Aktif: M15: CLOSING (W20)
Task Utama: Berdua - UAT Mentor & Minor Patch

### Day 96 (Senin, 8 Jun 2026): UAT final mentor
Status: [RENCANA]
Milestone/Group: M15: CLOSING (W20)
Task Referensi Berdua: UAT Mentor & Minor Patch

#### Entri Farchan (UX+Backend)
Aktivitas: UAT final dengan mentor dan checklist.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain UAT final dengan mentor dan checklist sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'UAT checklist' benar-benar siap dipakai."
Output Farchan:
- Deliverable utama hari ini: UAT checklist.
- Aktivitas yang diselesaikan: UAT final dengan mentor dan checklist.
- Bukti screenshot utama: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: target closing phase W19-W20.
- Bukti screenshot pendukung 1: `docs/logbook/PROJECT_MANAGEMENT_15_WEEKS_SIMREKAP.md` baris 50-53: output final skenario W19-W20.
- Bukti screenshot pendukung 2: `README.md` baris 17-29: package handover dan dokumen final.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: target closing phase W19-W20.
- `docs/logbook/PROJECT_MANAGEMENT_15_WEEKS_SIMREKAP.md` baris 50-53: output final skenario W19-W20.
- `README.md` baris 17-29: package handover dan dokumen final.

#### Entri Ikram (UI+Frontend)
Aktivitas: Catat feedback UI/FE final.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Catat feedback UI/FE final sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'UAT checklist' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Deliverable utama hari ini: UAT checklist.
- Aktivitas yang diselesaikan: Catat feedback UI/FE final.
- Bukti screenshot utama: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: fokus closing dan handover.
- Bukti screenshot pendukung 1: `README.md` baris 17-29: final package documentation.
- Bukti screenshot pendukung 2: `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum submit.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: fokus closing dan handover.
- `README.md` baris 17-29: final package documentation.
- `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum submit.

### Day 97 (Selasa, 9 Jun 2026): Patch minor final
Status: [RENCANA]
Milestone/Group: M15: CLOSING (W20)
Task Referensi Berdua: UAT Mentor & Minor Patch

#### Entri Farchan (UX+Backend)
Aktivitas: Implement perubahan minor final backend.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Implement perubahan minor final backend sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Minor patch complete' benar-benar siap dipakai."
Output Farchan:
- Deliverable utama hari ini: Minor patch complete.
- Aktivitas yang diselesaikan: Implement perubahan minor final backend.
- Bukti screenshot utama: `docs/logbook/PROJECT_MANAGEMENT_15_WEEKS_SIMREKAP.md` baris 50-53: output final skenario W19-W20.
- Bukti screenshot pendukung 1: `README.md` baris 17-29: package handover dan dokumen final.
- Bukti screenshot pendukung 2: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness dan UAT final.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_15_WEEKS_SIMREKAP.md` baris 50-53: output final skenario W19-W20.
- `README.md` baris 17-29: package handover dan dokumen final.
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness dan UAT final.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement patch minor final UI/FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Implement patch minor final UI/FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Minor patch complete' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Deliverable utama hari ini: Minor patch complete.
- Aktivitas yang diselesaikan: Implement patch minor final UI/FE.
- Bukti screenshot utama: `README.md` baris 17-29: final package documentation.
- Bukti screenshot pendukung 1: `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum submit.
- Bukti screenshot pendukung 2: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness/UAT final.
Lampiran Ikram (Bukti Screenshot):
- `README.md` baris 17-29: final package documentation.
- `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum submit.
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness/UAT final.

### Day 98 (Rabu, 10 Jun 2026): Readiness final
Status: [RENCANA]
Milestone/Group: M15: CLOSING (W20)
Task Referensi Berdua: Handover & Submit Laporan

#### Entri Farchan (UX+Backend)
Aktivitas: Final readiness note operasional.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Final readiness note operasional sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Readiness note' benar-benar siap dipakai."
Output Farchan:
- Deliverable utama hari ini: Readiness note.
- Aktivitas yang diselesaikan: Final readiness note operasional.
- Bukti screenshot utama: `README.md` baris 17-29: package handover dan dokumen final.
- Bukti screenshot pendukung 1: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness dan UAT final.
- Bukti screenshot pendukung 2: `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum sign-off.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 17-29: package handover dan dokumen final.
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness dan UAT final.
- `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum sign-off.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalisasi handoff UI/FE note.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalisasi handoff UI/FE note sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Readiness note' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Deliverable utama hari ini: Readiness note.
- Aktivitas yang diselesaikan: Finalisasi handoff UI/FE note.
- Bukti screenshot utama: `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum submit.
- Bukti screenshot pendukung 1: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness/UAT final.
- Bukti screenshot pendukung 2: `CONTRIBUTING.md` baris 7-22: standar review quality gate.
Lampiran Ikram (Bukti Screenshot):
- `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum submit.
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness/UAT final.
- `CONTRIBUTING.md` baris 7-22: standar review quality gate.

### Day 99 (Kamis, 11 Jun 2026): Closing report dan handover
Status: [RENCANA]
Milestone/Group: M15: CLOSING (W20)
Task Referensi Berdua: Handover & Submit Laporan

#### Entri Farchan (UX+Backend)
Aktivitas: Susun closing report dan handover teknis.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun closing report dan handover teknis dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Closing package' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Deliverable utama hari ini: Closing package.
- Aktivitas yang diselesaikan: Susun closing report dan handover teknis.
- Bukti screenshot utama: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness dan UAT final.
- Bukti screenshot pendukung 1: `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum sign-off.
- Bukti screenshot pendukung 2: `CONTRIBUTING.md` baris 7-22: workflow review kualitas sebelum close proyek.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness dan UAT final.
- `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum sign-off.
- `CONTRIBUTING.md` baris 7-22: workflow review kualitas sebelum close proyek.

#### Entri Ikram (UI+Frontend)
Aktivitas: Arsip source UI/FE dan dokumentasi.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Arsip source UI/FE dan dokumentasi dalam konteks 'Closing report dan handover'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M15: CLOSING (W20). Hasil 'Closing package' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Closing package.
- Aktivitas yang diselesaikan: Arsip source UI/FE dan dokumentasi.
- Bukti screenshot utama: `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness/UAT final.
- Bukti screenshot pendukung 1: `CONTRIBUTING.md` baris 7-22: standar review quality gate.
- Bukti screenshot pendukung 2: `src/app/App.tsx` baris 240-254: entry point login/admin/register untuk demo sign-off.
Lampiran Ikram (Bukti Screenshot):
- `docs/status/SYSTEM_SUMMARY.md` baris 430-451: status readiness/UAT final.
- `CONTRIBUTING.md` baris 7-22: standar review quality gate.
- `src/app/App.tsx` baris 240-254: entry point login/admin/register untuk demo sign-off.

### Day 100 (Jumat, 12 Jun 2026): Presentasi akhir dan retrospektif
Status: [RENCANA]
Milestone/Group: M15: CLOSING (W20)
Task Referensi Berdua: Handover & Submit Laporan

#### Entri Farchan (UX+Backend)
Aktivitas: Presentasi akhir dan retrospektif proyek.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Presentasi akhir dan retrospektif proyek pada konteks 'Presentasi akhir dan retrospektif'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M15: CLOSING (W20). Setelah selesai, saya pastikan 'Proyek ditutup' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Deliverable utama hari ini: Proyek ditutup.
- Aktivitas yang diselesaikan: Presentasi akhir dan retrospektif proyek.
- Bukti screenshot utama: `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum sign-off.
- Bukti screenshot pendukung 1: `CONTRIBUTING.md` baris 7-22: workflow review kualitas sebelum close proyek.
- Bukti screenshot pendukung 2: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: target closing phase W19-W20.
Lampiran Farchan (Bukti Screenshot):
- `docs/guides/QUICKSTART.md` baris 218-227: smoke test final sebelum sign-off.
- `CONTRIBUTING.md` baris 7-22: workflow review kualitas sebelum close proyek.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: target closing phase W19-W20.

#### Entri Ikram (UI+Frontend)
Aktivitas: Support demo akhir dan sign-off.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Support demo akhir dan sign-off dalam konteks 'Presentasi akhir dan retrospektif'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M15: CLOSING (W20). Hasil 'Proyek ditutup' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Deliverable utama hari ini: Proyek ditutup.
- Aktivitas yang diselesaikan: Support demo akhir dan sign-off.
- Bukti screenshot utama: `CONTRIBUTING.md` baris 7-22: standar review quality gate.
- Bukti screenshot pendukung 1: `src/app/App.tsx` baris 240-254: entry point login/admin/register untuk demo sign-off.
- Bukti screenshot pendukung 2: `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: fokus closing dan handover.
Lampiran Ikram (Bukti Screenshot):
- `CONTRIBUTING.md` baris 7-22: standar review quality gate.
- `src/app/App.tsx` baris 240-254: entry point login/admin/register untuk demo sign-off.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 65-68: fokus closing dan handover.

