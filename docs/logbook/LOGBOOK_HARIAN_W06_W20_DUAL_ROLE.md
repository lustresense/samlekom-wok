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
"Hari ini fokus saya di 'Freeze scope MVP dan audit screen map' adalah Freeze scope MVP dan rapikan backlog prioritas. Saya mulai dengan ngerapihin backlog dan dependency backend biar batas kerja sprint jelas, lalu mengunci keputusan teknis yang paling ngaruh ke alur lanjutan. Sebelum close, saya validasi lagi keputusan yang diambil supaya output hari ini 'Scope MVP final + screen map' bisa langsung dipakai tim tanpa ambigu."
Output Farchan:
- Artefak UX+Backend harian selesai: Freeze scope MVP dan rapikan backlog prioritas.
- Outcome harian terukur: Scope MVP final + screen map.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 49-63: target mingguan W06 sebagai acuan scope MVP freeze.
- `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv` baris 1-10: daftar milestone sebagai baseline lingkup yang dikunci.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 1-30: ringkasan sistem untuk validasi batas scope.

#### Entri Ikram (UI+Frontend)
Aktivitas: Audit ulang screen Figma aktif dan mapping ke modul FE.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Audit ulang screen Figma aktif dan mapping ke modul FE. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M1: PREPARATION (W06). Setelah sinkronisasi final, 'Scope MVP final + screen map' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Audit ulang screen Figma aktif dan mapping ke modul FE.
- Outcome harian terukur: Scope MVP final + screen map.
Lampiran Ikram (Bukti Screenshot):
- `docs/ASSET_INVENTORY.md` baris 9-31: baseline inventori aset visual dan struktur folder aset.
- `docs/LIBRARY_SELECTION.md` baris 10-23: stack UI/FE resmi sebagai referensi mapping komponen.
- `src/app/App.tsx` baris 46-49 dan 138-144: baseline state auth/view pada app shell untuk audit mapping.

### Day 27 (Selasa, 3 Mar 2026): API contract v1 dan baseline FE
Status: [RENCANA]
Milestone/Group: M1: PREPARATION (W06)
Task Referensi Farchan: API Contract & Scope Definition
Task Referensi Ikram: UI Audit & Component Mapping

#### Entri Farchan (UX+Backend)
Aktivitas: Finalkan API contract v1 untuk auth/event/report.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalkan API contract v1 untuk auth/event/report sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'API contract v1 + FE baseline' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Finalkan API contract v1 untuk auth/event/report.
- Outcome harian terukur: API contract v1 + FE baseline.
Lampiran Farchan (Bukti Screenshot):
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 70-95: definisi peran aktor dan kebutuhan sistem sebagai basis API contract.
- `server/local_api.py` baris 1-26: konfigurasi dasar API dan import sebagai fondasi contract teknis.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 49-63: target W06 untuk validasi API contract selaras rencana.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalkan design token dan setup struktur FE sprint-ready.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalkan design token dan setup struktur FE sprint-ready sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'API contract v1 + FE baseline' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Finalkan design token dan setup struktur FE sprint-ready.
- Outcome harian terukur: API contract v1 + FE baseline.
Lampiran Ikram (Bukti Screenshot):
- `docs/ASSET_INVENTORY.md` baris 32-55: token warna, tipografi, dan spacing sebagai dasar design token.
- `docs/LIBRARY_SELECTION.md` baris 24-40: konfigurasi library komponen untuk setup sprint-ready.
- `src/app/App.tsx` baris 1-25: import dan setup konfigurasi app dasar yang sudah disesuaikan token.

### Day 28 (Rabu, 4 Mar 2026): Validasi design thinking artifact
Status: [RENCANA]
Milestone/Group: M1: PREPARATION (W06)
Task Referensi Farchan: ERD & Sprint Planning W07
Task Referensi Ikram: UI Audit & Component Mapping

#### Entri Farchan (UX+Backend)
Aktivitas: Finalisasi persona, journey map, dan problem framing.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalisasi persona, journey map, dan problem framing sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Dokumen persona/journey + component map' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Finalisasi persona, journey map, dan problem framing.
- Outcome harian terukur: Dokumen persona/journey + component map.
Lampiran Farchan (Bukti Screenshot):
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 44-69: latar belakang masalah dan konteks sistem sebagai dasar problem framing.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 40-75: alur pengguna per role untuk pemetaan journey map.
- `docs/logbook/logbook.md` baris 1-30: catatan awal proyek sebagai referensi persona dan stakeholder.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sinkronkan wireframe akhir ke struktur komponen FE.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Sinkronkan wireframe akhir ke struktur komponen FE. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M1: PREPARATION (W06). Setelah sinkronisasi final, 'Dokumen persona/journey + component map' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Sinkronkan wireframe akhir ke struktur komponen FE.
- Outcome harian terukur: Dokumen persona/journey + component map.
Lampiran Ikram (Bukti Screenshot):
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 23-39: struktur IA dan role workspace sebagai basis wireframe.
- `docs/LIBRARY_SELECTION.md` baris 10-23: stack komponen yang dipakai untuk sinkron struktur FE.
- `src/app/App.tsx` baris 60-100: definisi routing dan viewport sebagai kerangka komponen.

### Day 29 (Kamis, 5 Mar 2026): Acceptance criteria sprint 1
Status: [RENCANA]
Milestone/Group: M1: PREPARATION (W06)
Task Referensi Farchan: ERD & Sprint Planning W07
Task Referensi Ikram: Setup Repo & App Shell

#### Entri Farchan (UX+Backend)
Aktivitas: Tetapkan acceptance criteria dan DoD untuk fitur sprint 1.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Tetapkan acceptance criteria dan DoD untuk fitur sprint 1 dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'DoD sprint 1 + app shell aktif' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Tetapkan acceptance criteria dan DoD untuk fitur sprint 1.
- Outcome harian terukur: DoD sprint 1 + app shell aktif.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 49-63: target mingguan sebagai basis penyusunan DoD.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 110-130: scope fitur MVP sebagai acuan acceptance criteria.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 1-25: kontrol sinkron tim sebagai referensi kriteria selesai.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement route skeleton dan state dasar app shell.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement route skeleton dan state dasar app shell pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'DoD sprint 1 + app shell aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement route skeleton dan state dasar app shell.
- Outcome harian terukur: DoD sprint 1 + app shell aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 184-215: routing view dan guard per role sebagai bukti skeleton aktif.
- `docs/ASSET_INVENTORY.md` baris 9-31: struktur folder sebagai referensi organisasi modul FE.
- `docs/LIBRARY_SELECTION.md` baris 10-23: stack yang digunakan pada route skeleton.

### Day 30 (Jumat, 6 Mar 2026): Sprint planning W07
Status: [RENCANA]
Milestone/Group: M1: PREPARATION (W06)
Task Referensi Farchan: ERD & Sprint Planning W07
Task Referensi Ikram: Setup Repo & App Shell

#### Entri Farchan (UX+Backend)
Aktivitas: Kunci sprint planning W07 dan risk register.
Uraian Kegiatan (Logbook):
"Hari ini fokus saya di 'Sprint planning W07' adalah Kunci sprint planning W07 dan risk register. Saya mulai dengan ngerapihin backlog dan dependency backend biar batas kerja sprint jelas, lalu mengunci keputusan teknis yang paling ngaruh ke alur lanjutan. Sebelum close, saya validasi lagi keputusan yang diambil supaya output hari ini 'Sprint backlog W07' bisa langsung dipakai tim tanpa ambigu."
Output Farchan:
- Artefak UX+Backend harian selesai: Kunci sprint planning W07 dan risk register.
- Outcome harian terukur: Sprint backlog W07.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 64-80: target W07 sebagai acuan sprint planning.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 26-50: rencana sprint dan peran tim sebagai basis risk register.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 130-148: scope produksi sebagai referensi risiko teknis.

#### Entri Ikram (UI+Frontend)
Aktivitas: Final review readiness UI+FE untuk sprint berikutnya.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Final review readiness UI+FE untuk sprint berikutnya sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Sprint backlog W07' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Final review readiness UI+FE untuk sprint berikutnya.
- Outcome harian terukur: Sprint backlog W07.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 216-279: render final lintas halaman sebagai bukti readiness FE.
- `docs/ASSET_INVENTORY.md` baris 56-75: aset final yang sudah siap untuk sprint berikutnya.
- `docs/LIBRARY_SELECTION.md` baris 40-55: verifikasi stack sebelum sprint dimulai.

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
- Artefak UX+Backend harian selesai: Implement validasi signup/login backend.
- Outcome harian terukur: Flow login/register jalan.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1211-1245: endpoint `auth/signup` dengan validasi input awal.
- `server/local_api.py` baris 1245-1291: endpoint `auth/login` dan `auth/admin-login`.
- `server/local_api.py` baris 240-252: `create_session()` sebagai output dari login berhasil.

#### Entri Ikram (UI+Frontend)
Aktivitas: Desain state auth loading-error-success dan implement form FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Desain state auth loading-error-success dan implement form FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Flow login/register jalan' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Desain state auth loading-error-success dan implement form FE.
- Outcome harian terukur: Flow login/register jalan.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 30-44: login form dan state loading/error/success.
- `src/app/components/RegisterPage.tsx` baris 140-177: form signup dan validasi awal FE.
- `src/app/App.tsx` baris 46-49: token state dasar sebagai output form berhasil.

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
- Artefak UX+Backend harian selesai: Implement session, auth me, dan logout backend.
- Outcome harian terukur: Session flow stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 240-268: `create_session()`, `user_from_token()`, dan session lifecycle.
- `server/local_api.py` baris 1291-1310: endpoint `/auth/logout` dan session invalidation.
- `server/local_api.py` baris 24-26 dan 120: policy auth dan rate limiting untuk stabilitas sesi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi token storage dan route guard FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi token storage dan route guard FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Session flow stabil' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi token storage dan route guard FE.
- Outcome harian terukur: Session flow stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 184-190: token storage dan route guard view aktif.
- `src/app/App.tsx` baris 150-165: clear session saat logout dalam guard flow.
- `src/app/components/LoginPage.tsx` baris 1-29: setup state login sebelum token disimpan.

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
- Artefak UX+Backend harian selesai: Implement mapping permission per role.
- Outcome harian terukur: Role-based view aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 269-310: role check dan permission mapping antar endpoint.
- `server/local_api.py` baris 1211-1240: validasi role pada proses login.
- `server/local_api.py` baris 24-26: definisi user model dan role constant.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sesuaikan menu UI per role dan conditional rendering FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Sesuaikan menu UI per role dan conditional rendering FE dalam konteks 'Permission per role'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M2: AUTH SYSTEM (W07). Hasil 'Role-based view aktif' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Sesuaikan menu UI per role dan conditional rendering FE.
- Outcome harian terukur: Role-based view aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 182-215: switch view per role sebagai bukti conditional rendering.
- `src/app/components/AdminLoginPage.tsx` baris 28-29: admin view yang tampil sesuai role.
- `src/app/components/RegisterPage.tsx` baris 176-177: role assignment di signup FE.

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
- Artefak UX+Backend harian selesai: Stabilkan model error auth 400/401/429.
- Outcome harian terukur: Error auth sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 120-145: `rate_limited()` sebagai basis error 429.
- `server/local_api.py` baris 1211-1260: validasi input dengan error 400/401 pada signup/login.
- `server/local_api.py` baris 24-26: security policy sebagai acuan status code error auth.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement error handling auth di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement error handling auth di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Error auth sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement error handling auth di FE.
- Outcome harian terukur: Error auth sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 44-80: error display dan retry logic pada login form.
- `src/app/components/AdminLoginPage.tsx` baris 28-60: error state khusus admin login.
- `src/app/App.tsx` baris 46-49: global error state auth.

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
- Artefak UX+Backend harian selesai: Retest auth end-to-end lintas role.
- Outcome harian terukur: Auth lintas role stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1211-1310: full auth endpoint suite untuk retest E2E.
- `server/local_api.py` baris 240-268: siklus session lengkap dari login sampai logout.
- `server/local_api.py` baris 24-26 dan 120: baseline security config pasca retest.

#### Entri Ikram (UI+Frontend)
Aktivitas: Polish UI/FE auth dan catat defect.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Polish UI/FE auth dan catat defect dalam konteks 'Retest auth E2E'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M2: AUTH SYSTEM (W07). Hasil 'Auth lintas role stabil' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Polish UI/FE auth dan catat defect.
- Outcome harian terukur: Auth lintas role stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 80-130: styling dan UX polish halaman login.
- `src/app/components/RegisterPage.tsx` baris 140-210: complete registration flow pasca polish.
- `src/app/App.tsx` baris 184-215: routing stabil dengan semua state auth terpolish.

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
- Artefak UX+Backend harian selesai: Validasi rule create event untuk scope pilar kuota.
- Outcome harian terukur: Create event draft aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1358-1395: handler create event dan validasi rule pilar kuota.
- `server/local_api.py` baris 365-378: definisi kolom tabel `events` dan constraint.
- `server/local_api.py` baris 1433-1440: inisiasi approval readiness setelah event dibuat.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalisasi UI form event dan implement submit FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalisasi UI form event dan implement submit FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Create event draft aktif' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Finalisasi UI form event dan implement submit FE.
- Outcome harian terukur: Create event draft aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 200-224: area form create event moderator.
- `src/app/components/ModeratorDashboard.tsx` baris 340-360: tombol submit event dari FE.
- `src/app/components/UserDashboard.tsx` baris 30-48: fetch event state awal untuk sinkron form.

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
- Artefak UX+Backend harian selesai: Stabilkan endpoint create draft event.
- Outcome harian terukur: Draft list sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1395-1432: stabilisasi endpoint create draft dengan error handling.
- `server/local_api.py` baris 378-387: lifecycle state event dari draft ke pending.
- `server/local_api.py` baris 1440-1450: validasi draft sebelum masuk antrian approval.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi daftar draft event moderator di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi daftar draft event moderator di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Draft list sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi daftar draft event moderator di FE.
- Outcome harian terukur: Draft list sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 223-250: render daftar draft event di dashboard.
- `src/app/components/ModeratorDashboard.tsx` baris 100-120: inbox draft yang masuk ke moderator.
- `src/app/components/UserDashboard.tsx` baris 47-65: tampilan event list dari sisi user.

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
- Artefak UX+Backend harian selesai: Implement endpoint approval/reject event.
- Outcome harian terukur: Approval flow aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1433-1452: endpoint approval dan reject event oleh admin/mod.
- `server/local_api.py` baris 365-387: perubahan status di tabel `events` pasca approval.
- `server/local_api.py` baris 1450-1457: transisi event dari approved ke publish-ready.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement aksi approve/reject di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement aksi approve/reject di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Approval flow aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement aksi approve/reject di FE.
- Outcome harian terukur: Approval flow aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 280-310: implementasi tombol approve/reject event.
- `src/app/components/AdminDashboard.tsx` baris 100-131: panel verifikasi admin yang serupa.
- `src/app/components/ModeratorDashboard.tsx` baris 284-300: logic reject dengan reason FE.

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
- Artefak UX+Backend harian selesai: Pastikan publish event sesuai status backend.
- Outcome harian terukur: Event publish tampil benar.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1450-1457: logika publish event dan validasi status akhir.
- `server/local_api.py` baris 365-380: state lifecycle event yang memvalidasi publish readiness.
- `server/local_api.py` baris 1358-1375: constraint create event sebagai acuan publish rule.

#### Entri Ikram (UI+Frontend)
Aktivitas: Update kartu event dan badge status FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Update kartu event dan badge status FE dalam konteks 'Publish status event'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M3: EVENT MODULE (W08). Hasil 'Event publish tampil benar' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Update kartu event dan badge status FE.
- Outcome harian terukur: Event publish tampil benar.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 90-130: kartu event dengan badge status FE.
- `src/app/components/ModeratorDashboard.tsx` baris 355-370: badge status event di panel moderator.
- `src/app/components/UserDashboard.tsx` baris 47-65: refresh event state setelah publish.

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
- Artefak UX+Backend harian selesai: Uji E2E draft sampai approval sampai publish.
- Outcome harian terukur: Event governance stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1358-1452: full event flow dari create hingga approval E2E.
- `server/local_api.py` baris 365-387: integritas relasi tabel selama uji E2E governance.
- `server/local_api.py` baris 1433-1457: siklus persetujuan dan publish dalam satu pass uji.

#### Entri Ikram (UI+Frontend)
Aktivitas: Refinement UI/FE pasca uji alur event.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Refinement UI/FE pasca uji alur event dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Event governance stabil' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: Refinement UI/FE pasca uji alur event.
- Outcome harian terukur: Event governance stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 220-317: full governance panel moderator pasca refinement.
- `src/app/components/UserDashboard.tsx` baris 47-112: flow user end-to-end pasca refinement.
- `src/app/components/AdminDashboard.tsx` baris 70-131: panel admin untuk audit pasca E2E.

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
- Artefak UX+Backend harian selesai: Implement rule join event quota duplicate status.
- Outcome harian terukur: Join flow valid.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1457-1480: handler join event dengan validasi quota dan duplikasi.
- `server/local_api.py` baris 365-387: relasi tabel `events` sebagai referensi status join.
- `server/local_api.py` baris 1082-1100: endpoint list event untuk validasi status sebelum join.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement tombol join dan state full closed.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement tombol join dan state full closed pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Join flow valid' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement tombol join dan state full closed.
- Outcome harian terukur: Join flow valid.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: tombol join dengan state full/closed.
- `src/app/components/UserDashboard.tsx` baris 47-65: fetch events untuk tampilan status join.
- `src/app/components/UserDashboard.tsx` baris 47-48: refresh state setelah join berhasil.

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
- Artefak UX+Backend harian selesai: Implement endpoint riwayat partisipasi.
- Outcome harian terukur: History partisipasi tampil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1480-1510: endpoint riwayat dan history partisipasi user.
- `server/local_api.py` baris 387-404: relasi tabel `event_participation` untuk riwayat.
- `server/local_api.py` baris 1100-1124: endpoint list event dengan filter partisipasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi halaman riwayat partisipasi FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi halaman riwayat partisipasi FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'History partisipasi tampil' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi halaman riwayat partisipasi FE.
- Outcome harian terukur: History partisipasi tampil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 65-90: halaman riwayat partisipasi user.
- `src/app/components/EventList.tsx` baris 42-43: referensi join untuk sinkron riwayat.
- `src/app/components/UserDashboard.tsx` baris 111-112: fetch history partisipasi user.

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
- Artefak UX+Backend harian selesai: Implement complete event oleh KSH.
- Outcome harian terukur: Complete flow aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1510-1518: endpoint complete event khusus KSH.
- `server/local_api.py` baris 387-404: update status di tabel `event_participation`.
- `server/local_api.py` baris 1457-1470: dependency join sebagai prasyarat complete.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement CTA complete khusus KSH di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement CTA complete khusus KSH di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Complete flow aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement CTA complete khusus KSH di FE.
- Outcome harian terukur: Complete flow aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 111-120: tombol complete event khusus KSH.
- `src/app/components/UserDashboard.tsx` baris 100-112: logika role-check sebelum tampilkan CTA.
- `src/app/components/EventList.tsx` baris 42-43: kondisi list event yang menampilkan opsi complete.

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
- Artefak UX+Backend harian selesai: Validasi checklist kehadiran dan transisi status.
- Outcome harian terukur: Attendance sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1480-1518: validasi checklist attendance dan transisi status.
- `server/local_api.py` baris 365-387: state event yang berubah setelah attendance dikonfirmasi.
- `server/local_api.py` baris 1082-1124: query events untuk validasi kehadiran cross-check.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi checklist attendance FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi checklist attendance FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Attendance sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi checklist attendance FE.
- Outcome harian terukur: Attendance sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 120-145: form checklist attendance di FE.
- `src/app/components/UserDashboard.tsx` baris 111-112: trigger complete setelah attendance diisi.
- `src/app/components/EventList.tsx` baris 42-43: referensi join sebagai prasyarat attendance.

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
- Artefak UX+Backend harian selesai: Retest join attendance complete.
- Outcome harian terukur: Participation stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1457-1518: full participation flow dari join ke complete.
- `server/local_api.py` baris 387-404: integritas tabel `event_participation` pasca retest.
- `server/local_api.py` baris 1082-1124: validasi event status setelah siklus participation.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug participation pada UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug participation pada UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Participation stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Patch bug participation pada UI/FE.
- Outcome harian terukur: Participation stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-55: fix state join/full/closed pasca uji.
- `src/app/components/UserDashboard.tsx` baris 111-120: patch CTA complete setelah bug ditemukan.
- `src/app/components/UserDashboard.tsx` baris 47-65: stabilisasi fresh fetch pasca patch.

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
- Artefak UX+Backend harian selesai: Finalkan payload report step 1 dan step 2.
- Outcome harian terukur: Step 1 aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1518-1545: handler submit report dan validasi payload step 1.
- `server/local_api.py` baris 411-420: definisi kolom tabel `event_reports` untuk step 1-2.
- `server/local_api.py` baris 1126-1140: endpoint history reports sebagai acuan payload.

#### Entri Ikram (UI+Frontend)
Aktivitas: Bangun wizard report step 1 di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Bangun wizard report step 1 di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Step 1 aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Bangun wizard report step 1 di FE.
- Outcome harian terukur: Step 1 aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 92-130: layout wizard step 1 dan navigasi.
- `src/app/components/ReportingWizard.tsx` baris 180-200: field form pada step 1.
- `src/app/components/UserDashboard.tsx` baris 67-68: inisiasi fetch history laporan user.

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
- Artefak UX+Backend harian selesai: Implement submit report endpoint beserta validasi.
- Outcome harian terukur: Submit report jalan.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1545-1575: implementasi endpoint submit report beserta validasi.
- `server/local_api.py` baris 420-426: kolom bukti dan status di tabel `event_reports`.
- `server/local_api.py` baris 1140-1157: endpoint history dengan filter status pending.

#### Entri Ikram (UI+Frontend)
Aktivitas: Bangun wizard step 2 dan validasi FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Bangun wizard step 2 dan validasi FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Submit report jalan' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Bangun wizard step 2 dan validasi FE.
- Outcome harian terukur: Submit report jalan.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 200-250: layout dan field wizard step 2.
- `src/app/components/ReportingWizard.tsx` baris 92-98: submit payload setelah step 2 terisi.
- `src/app/components/UserDashboard.tsx` baris 67-90: sinkron history setelah wizard step 2.

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
- Artefak UX+Backend harian selesai: Atur validasi media proof laporan.
- Outcome harian terukur: Bukti laporan tervalidasi.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1518-1540: validasi media proof pada handler submit.
- `server/local_api.py` baris 411-426: struktur kolom bukti di tabel reports.
- `server/local_api.py` baris 1126-1157: referensi history untuk cross-check bukti.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement behavior upload dan proof field di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement behavior upload dan proof field di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Bukti laporan tervalidasi' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement behavior upload dan proof field di FE.
- Outcome harian terukur: Bukti laporan tervalidasi.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 250-316: komponen upload bukti dan preview.
- `src/app/components/ReportingWizard.tsx` baris 182: field proof pada wizard.
- `src/app/components/UserDashboard.tsx` baris 67-68: refresh history setelah upload berhasil.

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
- Artefak UX+Backend harian selesai: Sinkron status report pending di backend.
- Outcome harian terukur: History report sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1540-1575: sinkronisasi status pending di handler report.
- `server/local_api.py` baris 420-426: field status di `event_reports`.
- `server/local_api.py` baris 1140-1157: endpoint history untuk verifikasi status sinkron.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi history report user di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi history report user di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'History report sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi history report user di FE.
- Outcome harian terukur: History report sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 67-100: halaman history laporan dengan status.
- `src/app/components/ReportingWizard.tsx` baris 316-340: navigasi kembali ke history setelah submit.
- `src/app/components/ReportingWizard.tsx` baris 92-98: referensi payload untuk sinkron history.

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
- Artefak UX+Backend harian selesai: Uji E2E report submission.
- Outcome harian terukur: Reporting stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1518-1575: full submission flow untuk E2E test.
- `server/local_api.py` baris 411-426: integritas tabel reports selama E2E.
- `server/local_api.py` baris 1126-1157: validasi history setelah submit berhasil.

#### Entri Ikram (UI+Frontend)
Aktivitas: Refinement wizard report di UI/FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Refinement wizard report di UI/FE dalam konteks 'E2E reporting'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M5: REPORTING (W10). Hasil 'Reporting stabil' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Refinement wizard report di UI/FE.
- Outcome harian terukur: Reporting stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 92-98 dan 316: full wizard flow pasca refinement.
- `src/app/components/ReportingWizard.tsx` baris 182-316: refinement detail field dan submit.
- `src/app/components/UserDashboard.tsx` baris 67-68: validasi history update setelah refinement.

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
- Artefak UX+Backend harian selesai: Implement verify reject dan reason backend.
- Outcome harian terukur: Verify panel aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1576-1595: handler verify dan reject report beserta reason field.
- `server/local_api.py` baris 862-868: `apply_xp()` sebagai aksi pasca verifikasi.
- `server/local_api.py` baris 458-475: `audit_logs` untuk jejak verify/reject.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement panel verifikasi moderator FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement panel verifikasi moderator FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Verify panel aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement panel verifikasi moderator FE.
- Outcome harian terukur: Verify panel aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 170-200: inbox laporan untuk panel verifikasi.
- `src/app/components/ModeratorDashboard.tsx` baris 249-260: tombol verify pada panel.
- `src/app/components/AdminDashboard.tsx` baris 110-131: referensi panel admin yang serupa.

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
- Artefak UX+Backend harian selesai: Implement scoring dasar saat verify.
- Outcome harian terukur: Scoring sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 862-875: implementasi `apply_xp()` dan scoring engine.
- `server/local_api.py` baris 1589-1599: update poin user setelah verifikasi berhasil.
- `server/local_api.py` baris 458-480: audit log untuk rekam scoring event.

#### Entri Ikram (UI+Frontend)
Aktivitas: Tampilkan feedback status dan skor di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Tampilkan feedback status dan skor di FE dalam konteks 'Scoring dasar'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M6: VERIFICATION (W11). Hasil 'Scoring sinkron' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Tampilkan feedback status dan skor di FE.
- Outcome harian terukur: Scoring sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 249-270: feedback status setelah aksi verify.
- `src/app/components/AdminDashboard.tsx` baris 130-155: tampilan skor di panel admin.
- `src/app/components/ModeratorDashboard.tsx` baris 170-171: inbox laporan sebagai konteks scoring.

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
- Artefak UX+Backend harian selesai: Tambah audit trail status report.
- Outcome harian terukur: Audit trail terbaca.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 458-503: `audit_logs` dan `temporary_adjustments` untuk audit trail.
- `server/local_api.py` baris 1576-1590: tambahan log status di verify/reject handler.
- `server/local_api.py` baris 862-868: relasi scoring dengan audit trail.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement timeline status report FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement timeline status report FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Audit trail terbaca' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement timeline status report FE.
- Outcome harian terukur: Audit trail terbaca.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 170-190: timeline status di inbox laporan.
- `src/app/components/AdminDashboard.tsx` baris 100-131: panel admin dengan audit trail visual.
- `src/app/components/ModeratorDashboard.tsx` baris 250-270: status update di panel moderator.

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
- Artefak UX+Backend harian selesai: Stabilkan notifikasi status report backend.
- Outcome harian terukur: Notifikasi status aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1576-1599: stabilisasi notifikasi status di handler verifikasi.
- `server/local_api.py` baris 480-503: `temporary_adjustments` sebagai trigger notifikasi.
- `server/local_api.py` baris 862-875: sinkron scoring untuk notifikasi poin bertambah.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement indikator notifikasi FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement indikator notifikasi FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Notifikasi status aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement indikator notifikasi FE.
- Outcome harian terukur: Notifikasi status aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 89-120: notifikasi dan alert di header dashboard.
- `src/app/components/AdminDashboard.tsx` baris 70-100: indikator notifikasi di panel admin.
- `src/app/components/ModeratorDashboard.tsx` baris 170-171: inbox sebagai sumber notifikasi.

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
- Artefak UX+Backend harian selesai: Retest verify dan scoring end-to-end.
- Outcome harian terukur: Verifikasi stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1576-1599: full verify/reject flow untuk retest E2E.
- `server/local_api.py` baris 862-875: validasi scoring engine setelah retest.
- `server/local_api.py` baris 458-503: integritas audit log selama E2E verification.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug verifikasi pada UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug verifikasi pada UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Verifikasi stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Patch bug verifikasi pada UI/FE.
- Outcome harian terukur: Verifikasi stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 249-270: patch aksi verify pasca bug report.
- `src/app/components/AdminDashboard.tsx` baris 130-145: patch panel admin pasca uji.
- `src/app/components/ModeratorDashboard.tsx` baris 170-190: stabilisasi inbox setelah patch.

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
- Artefak UX+Backend harian selesai: Finalkan rumus XP kampung dan pilar.
- Outcome harian terukur: Leaderboard awal aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 862-875: implementasi rumus kalkulasi XP kampung dan pilar.
- `server/local_api.py` baris 987-1000: endpoint `/kampung` sebagai output leaderboard.
- `server/local_api.py` baris 1590-1595: trigger update XP setelah verifikasi report.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI leaderboard top ringkas.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI leaderboard top ringkas pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Leaderboard awal aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement UI leaderboard top ringkas.
- Outcome harian terukur: Leaderboard awal aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 278-292: rendering tabel leaderboard top FE.
- `src/app/components/UserDashboard.tsx` baris 87-88: fetch data leaderboard kampung.
- `src/data/levelingSystem.ts` baris 145-170: logic level sebagai basis tampilan rank.

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
- Artefak UX+Backend harian selesai: Sinkron update XP pasca verify.
- Outcome harian terukur: Rank update sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1595-1610: update poin user segera setelah verifikasi.
- `server/local_api.py` baris 862-870: kalkulasi XP per peserta pasca verify.
- `server/local_api.py` baris 987-1002: refleksi update XP di endpoint leaderboard.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi rank card dan nilai XP FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi rank card dan nilai XP FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Rank update sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi rank card dan nilai XP FE.
- Outcome harian terukur: Rank update sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 87-110: integrasi rank card dengan nilai XP.
- `src/data/levelingSystem.ts` baris 170-200: progress dan XP threshold per level.
- `src/app/components/UserDashboard.tsx` baris 278-292: render rank card di leaderboard.

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
- Artefak UX+Backend harian selesai: Stabilkan service progres 4 pilar.
- Outcome harian terukur: Progress pilar tampil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 862-875: layanan kalkulasi progres per pilar.
- `server/local_api.py` baris 1000-1010: query agregasi kampung untuk 4 pilar.
- `server/local_api.py` baris 1595: update pilar setelah report diverifikasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi chart radar pilar FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi chart radar pilar FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Progress pilar tampil' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi chart radar pilar FE.
- Outcome harian terukur: Progress pilar tampil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 250-278: chart radar progress 4 pilar.
- `src/data/levelingSystem.ts` baris 200-223: mapping pilar ke level dan progress bar.
- `src/app/components/UserDashboard.tsx` baris 87-88: fetch pilar data dari API.

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
- Artefak UX+Backend harian selesai: Atur aturan akses leaderboard.
- Outcome harian terukur: Akses leaderboard valid.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 987-1002: endpoint `/kampung` dengan access rule.
- `server/local_api.py` baris 862-868: validasi role sebelum kalkulasi leaderboard.
- `server/local_api.py` baris 24-26: security policy untuk akses endpoint publik.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement CTA login dan view all FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement CTA login dan view all FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Akses leaderboard valid' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement CTA login dan view all FE.
- Outcome harian terukur: Akses leaderboard valid.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 278-300: CTA "view all" pada leaderboard.
- `src/app/App.tsx` baris 182-215: routing ke halaman leaderboard penuh.
- `src/data/levelingSystem.ts` baris 145-165: logic level untuk CTA kontekstual.

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
- Artefak UX+Backend harian selesai: Uji E2E report ke XP ke leaderboard.
- Outcome harian terukur: Leaderboard stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 862-875: full XP pipeline dari report ke leaderboard.
- `server/local_api.py` baris 987-1002: validasi akhir endpoint leaderboard pasca E2E.
- `server/local_api.py` baris 1595: sinkron poin sebagai titik akhir E2E chain.

#### Entri Ikram (UI+Frontend)
Aktivitas: Polish UI/FE leaderboard.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Polish UI/FE leaderboard dalam konteks 'E2E report ke rank'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M7: GAMIFICATION (W12). Hasil 'Leaderboard stabil' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Polish UI/FE leaderboard.
- Outcome harian terukur: Leaderboard stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 87-88 dan 278-292: polish rendering leaderboard.
- `src/data/levelingSystem.ts` baris 145-223: refinement logic level dan progress pasca polish.
- `src/app/App.tsx` baris 182-215: routing halaman leaderboard yang telah dipoles.

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
- Artefak UX+Backend harian selesai: Definisikan rule 1 kegiatan 1 sertifikat.
- Outcome harian terukur: Rule sertifikat final.
Lampiran Farchan (Bukti Screenshot):
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 147-148: rule 1 kegiatan 1 sertifikat.
- `server/local_api.py` baris 1637-1650: definisi rule konversi kegiatan ke sertifikat.
- `server/local_api.py` baris 1595: basis poin yang menjadi trigger sertifikat.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI riwayat sertifikat.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI riwayat sertifikat pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Rule sertifikat final' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement UI riwayat sertifikat.
- Outcome harian terukur: Rule sertifikat final.
Lampiran Ikram (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 187-210: struktur badge untuk context riwayat sertifikat.
- `src/app/components/UserDashboard.tsx` baris 400-423: binding profil untuk tampilan sertifikat.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 34-55: acuan flow user untuk sertifikat.

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
- Artefak UX+Backend harian selesai: Implement penerbitan sertifikat.
- Outcome harian terukur: Sertifikat dapat diakses.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1650-1664: implementasi generate dan publish sertifikat.
- `server/local_api.py` baris 1595: trigger penerbitan dari scoring verify.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 147-148: referensi rule untuk validasi penerbitan.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi unduh sertifikat FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi unduh sertifikat FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Sertifikat dapat diakses' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi unduh sertifikat FE.
- Outcome harian terukur: Sertifikat dapat diakses.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 423-450: tombol unduh dan preview sertifikat.
- `src/data/validatedBadges.ts` baris 210-230: validasi badge sebelum sertifikat bisa diunduh.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 55-70: langkah unduh sertifikat untuk user.

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
- Artefak UX+Backend harian selesai: Definisikan konversi poin ke voucher.
- Outcome harian terukur: Katalog reward aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1637-1660: rule konversi poin ke voucher dalam endpoint reward.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 147-150: governance konversi poin.
- `server/local_api.py` baris 1595: basis poin sebagai sumber konversi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI katalog reward.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI katalog reward pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Katalog reward aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement UI katalog reward.
- Outcome harian terukur: Katalog reward aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 187-210: badge catalog sebagai visual reward.
- `src/app/components/UserDashboard.tsx` baris 380-423: halaman katalog reward FE.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 34-55: panduan navigasi katalog reward.

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
- Artefak UX+Backend harian selesai: Implement redeem poin dan decrement saldo.
- Outcome harian terukur: Redeem sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1660-1680: handler redeem poin dan decrement saldo.
- `server/local_api.py` baris 1637-1650: validasi saldo sebelum redeem.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 147-148: acuan rule redeem.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi redeem flow FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi redeem flow FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Redeem sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi redeem flow FE.
- Outcome harian terukur: Redeem sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 350-380: form redeem dan konfirmasi poin.
- `src/data/validatedBadges.ts` baris 230-250: validasi badge setelah redeem berhasil.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 55-70: langkah redeem poin untuk user.

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
- Artefak UX+Backend harian selesai: Uji E2E sertifikat dan redeem.
- Outcome harian terukur: Benefit relawan stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1637-1664: full reward flow untuk E2E test.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 147-150: validasi rule reward selama E2E.
- `server/local_api.py` baris 1595: chain poin ke sertifikat dalam skenario E2E.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug reward UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug reward UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Benefit relawan stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Patch bug reward UI/FE.
- Outcome harian terukur: Benefit relawan stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 187-230: patch validasi badge pasca uji reward.
- `src/app/components/UserDashboard.tsx` baris 423-450: patch tampilan sertifikat pasca bug fix.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 34-70: verifikasi flow reward pasca patch.

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
- Artefak UX+Backend harian selesai: Definisikan schema request mitra dan scope.
- Outcome harian terukur: Form mitra aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1004-1014: fetch daftar collaboration request yang sudah ada.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 110-118: lingkup governance mitra.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 161-163: aturan submission mitra.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI form mitra publik.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI form mitra publik pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Form mitra aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement UI form mitra publik.
- Outcome harian terukur: Form mitra aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 1-34: layout halaman dan form mitra publik.
- `src/app/components/ModeratorDashboard.tsx` baris 100-117: inbox request mitra awal.
- `src/app/components/ModeratorDashboard.tsx` baris 310-317: referensi aksi reviewer.

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
- Artefak UX+Backend harian selesai: Implement endpoint submit mitra status pending.
- Outcome harian terukur: Submit mitra sukses.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1297-1320: handler submit request mitra dengan status pending.
- `server/local_api.py` baris 1004-1014: endpoint GET untuk verifikasi setelah submit.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 110-118: scope untuk validasi endpoint.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi submit request mitra FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi submit request mitra FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Submit mitra sukses' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi submit request mitra FE.
- Outcome harian terukur: Submit mitra sukses.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 34-38: submit handler dan feedback FE.
- `src/app/components/ModeratorDashboard.tsx` baris 116-130: tampilan request masuk moderator.
- `src/app/components/CollaborationPage.tsx` baris 60-90: feedback status setelah submit.

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
- Artefak UX+Backend harian selesai: Implement routing request by scope.
- Outcome harian terukur: Routing request sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1320-1336: routing request berdasarkan scope ke reviewer yang tepat.
- `server/local_api.py` baris 1004-1014: feed request yang sudah dirouting untuk moderator.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 110-118 dan 161-163: rule routing scope.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi inbox review moderator FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi inbox review moderator FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Routing request sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi inbox review moderator FE.
- Outcome harian terukur: Routing request sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 116-150: inbox review request mitra.
- `src/app/components/CollaborationPage.tsx` baris 34-60: form yang menghasilkan inbox entry.
- `src/app/components/ModeratorDashboard.tsx` baris 300-320: panel aksi review dari inbox.

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
- Artefak UX+Backend harian selesai: Implement approve reject request mitra.
- Outcome harian terukur: Review flow aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1336-1360: endpoint approve/reject request mitra beserta validasi.
- `server/local_api.py` baris 1297-1320: status pending yang divalidasi sebelum aksi approve/reject.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 161-163: aturan governance approve dalam sistem mitra.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement aksi review mitra FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement aksi review mitra FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Review flow aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement aksi review mitra FE.
- Outcome harian terukur: Review flow aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 316-340: tombol approve/reject mitra di panel moderator.
- `src/app/components/ModeratorDashboard.tsx` baris 116-120: inbox yang memunculkan aksi review mitra.
- `src/app/components/CollaborationPage.tsx` baris 34-38: submit handler yang dipicu dari aksi review.

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
- Artefak UX+Backend harian selesai: Uji E2E submit sampai review mitra.
- Outcome harian terukur: Governance mitra stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1297-1360: full collaboration flow dari submit ke approval untuk E2E.
- `server/local_api.py` baris 1004-1014: validasi daftar request setelah siklus E2E selesai.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 110-118: scope mitra sebagai acuan validasi E2E.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug mitra di UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug mitra di UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Governance mitra stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Patch bug mitra di UI/FE.
- Outcome harian terukur: Governance mitra stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 60-90: patch feedback status dan state FE mitra.
- `src/app/components/ModeratorDashboard.tsx` baris 116-130: stabilisasi inbox request setelah patch.
- `src/app/components/ModeratorDashboard.tsx` baris 310-317: fix aksi approve/reject mitra pasca bug.

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
- Artefak UX+Backend harian selesai: Lakukan threat modeling dan checklist attack surface.
- Outcome harian terukur: Daftar risiko keamanan.
Lampiran Farchan (Bukti Screenshot):
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: daftar attack surface dari threat modeling checklist awal.
- `server/local_api.py` baris 24-36: definisi env variable dan policy keamanan dasar.
- `server/local_api.py` baris 99-108: CORS allowlist dan security headers awal sebagai baseline.

#### Entri Ikram (UI+Frontend)
Aktivitas: Audit area UI/FE sensitif untuk produksi.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Audit area UI/FE sensitif untuk produksi. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M10: SECURITY (W15). Setelah sinkronisasi final, 'Daftar risiko keamanan' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Audit area UI/FE sensitif untuk produksi.
- Outcome harian terukur: Daftar risiko keamanan.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 89-120: unauthorized handling sebagai area audit sensitif.
- `src/app/components/LoginPage.tsx` baris 30-44: state error auth pada area login yang sensitif.
- `src/app/App.tsx` baris 150-165: clear token dan routing proteksi sesi.

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
- Artefak UX+Backend harian selesai: Perketat input validation backend.
- Outcome harian terukur: Validasi FE-BE konsisten.
Lampiran Farchan (Bukti Screenshot):
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 18-30: checklist validasi input dan sanitasi data backend.
- `server/local_api.py` baris 1211-1230: validasi input ketat pada endpoint signup dan login.
- `server/local_api.py` baris 120-135: rate limiter sebagai lapis pertahanan dari input berulang.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sinkron validasi input di FE.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Sinkron validasi input di FE. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M10: SECURITY (W15). Setelah sinkronisasi final, 'Validasi FE-BE konsisten' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Sinkron validasi input di FE.
- Outcome harian terukur: Validasi FE-BE konsisten.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 44-80: validasi form login yang disinkronkan dengan aturan backend.
- `src/app/components/RegisterPage.tsx` baris 140-177: validasi input FE pada form signup.
- `src/app/App.tsx` baris 154-157: clear token saat session error untuk menutup celah keamanan.

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
- Artefak UX+Backend harian selesai: Aktifkan rate limit dan session policy.
- Outcome harian terukur: Throttling flow aman.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 120-145: implementasi rate limiter dan throttle policy yang diaktifkan.
- `server/local_api.py` baris 240-268: session lifecycle dan expiry policy yang diperkuat.
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 31-45: checklist session security sebagai acuan.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement handling error 429 di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement handling error 429 di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Throttling flow aman' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement handling error 429 di FE.
- Outcome harian terukur: Throttling flow aman.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 44-80: error 429 handling pada login form saat rate limit tercapai.
- `src/app/components/AdminLoginPage.tsx` baris 28-60: error state admin saat rate limit aktif.
- `src/app/App.tsx` baris 154-165: routing proteksi sesi saat throttling aktif.

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
- Artefak UX+Backend harian selesai: Konfigurasi CORS allowlist dan security headers.
- Outcome harian terukur: CORS security pass.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 99-120: konfigurasi CORS allowlist dan security headers penuh.
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: checklist CORS dan header sebagai acuan konfigurasi.
- `server/local_api.py` baris 24-36: env variable untuk domain allowlist dan header policy.

#### Entri Ikram (UI+Frontend)
Aktivitas: Uji perilaku FE pada mode production.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji perilaku FE pada mode production dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'CORS security pass' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: Uji perilaku FE pada mode production.
- Outcome harian terukur: CORS security pass.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 124-151: uji unauthorized handling pada production mode.
- `src/app/App.tsx` baris 154-157: sesi clear saat production mode dengan CORS aktif.
- `src/app/components/LoginPage.tsx` baris 80-130: uji form login pada production mock dengan CORS.

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
- Artefak UX+Backend harian selesai: Jalankan security regression dan checklist publish.
- Outcome harian terukur: Baseline security siap.
Lampiran Farchan (Bukti Screenshot):
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 46-60: regression checklist security akhir.
- `server/local_api.py` baris 24-36 dan 99-120: full security config yang diverifikasi dalam regression pass.
- `server/local_api.py` baris 120-145: re-verifikasi rate limiter pasca regression selesai.

#### Entri Ikram (UI+Frontend)
Aktivitas: Regression FE pasca hardening.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Regression FE pasca hardening untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Baseline security siap' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Regression FE pasca hardening.
- Outcome harian terukur: Baseline security siap.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 89-151: regression test full unauthorized handling FE.
- `src/app/App.tsx` baris 150-165: regression token clear dan routing guard setelah hardening.
- `src/app/components/LoginPage.tsx` baris 30-80: retest full login form pasca security hardening.

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
- Artefak UX+Backend harian selesai: Integrasi modul lintas domain round 1.
- Outcome harian terukur: Integrasi lintas modul.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 1-18: konfigurasi dev startup sebelum integrasi dijalankan.
- `server/local_api.py` baris 1211-1358: endpoint auth dan event sebagai modul pertama integrasi.
- `DEMO_ACCOUNTS.md` baris 8-26: akun demo untuk uji integrasi lintas role.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi UI+FE round 1.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi UI+FE round 1 pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Integrasi lintas modul' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi UI+FE round 1.
- Outcome harian terukur: Integrasi lintas modul.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 182-190: switch view role sebagai inti integrasi FE round 1.
- `src/app/components/UserDashboard.tsx` baris 47-90: alur user FE dalam integrasi round 1.
- `src/app/components/ModeratorDashboard.tsx` baris 223-260: panel moderator dalam integrasi round 1.

### Day 77 (Selasa, 12 Mei 2026): Skenario demo role
Status: [RENCANA]
Milestone/Group: M11: INTEGRATION (W16)
Task Referensi Berdua: Lintas Modul & Skenario Demo

#### Entri Farchan (UX+Backend)
Aktivitas: Susun skenario demo per role.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun skenario demo per role dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Script demo v1' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Susun skenario demo per role.
- Outcome harian terukur: Script demo v1.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 19-29: startup full API untuk rehearsal skenario demo.
- `DEMO_ACCOUNTS.md` baris 8-20: detail akun admin dan moderator untuk skenario demo.
- `server/local_api.py` baris 1358-1457: endpoint event-participation untuk demo role user.

#### Entri Ikram (UI+Frontend)
Aktivitas: Siapkan alur demo di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Siapkan alur demo di FE dalam konteks 'Skenario demo role'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M11: INTEGRATION (W16). Hasil 'Script demo v1' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Siapkan alur demo di FE.
- Outcome harian terukur: Script demo v1.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 182-215: routing demo per role view yang disiapkan.
- `src/app/components/UserDashboard.tsx` baris 90-112: segmen demo alur pelaporan user.
- `src/app/components/ModeratorDashboard.tsx` baris 260-317: segmen demo alur moderator.

### Day 78 (Rabu, 13 Mei 2026): Seed data demo
Status: [RENCANA]
Milestone/Group: M11: INTEGRATION (W16)
Task Referensi Berdua: Seed Data & Candidate Build

#### Entri Farchan (UX+Backend)
Aktivitas: Siapkan seed data demo realistis.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Siapkan seed data demo realistis pada konteks 'Seed data demo'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M11: INTEGRATION (W16). Setelah selesai, saya pastikan 'Demo data siap' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Siapkan seed data demo realistis.
- Outcome harian terukur: Demo data siap.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 19-29: startup dengan seed data demo aktif.
- `server/local_api.py` baris 365-430: tabel events dan reports sebagai target seed data.
- `DEMO_ACCOUNTS.md` baris 8-26: akun yang terikat ke seed data demo realistis.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sinkron tampilan FE dengan seed data.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Sinkron tampilan FE dengan seed data. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M11: INTEGRATION (W16). Setelah sinkronisasi final, 'Demo data siap' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Sinkron tampilan FE dengan seed data.
- Outcome harian terukur: Demo data siap.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 47-90: render FE setelah seed data dimuat.
- `src/app/components/ModeratorDashboard.tsx` baris 100-140: sinkron inbox moderator dengan seed data.
- `src/app/App.tsx` baris 182-215: routing konsisten dengan seed data yang berhasil dimuat.

### Day 79 (Kamis, 14 Mei 2026): Dry run UAT internal
Status: [RENCANA]
Milestone/Group: M11: INTEGRATION (W16)
Task Referensi Berdua: Seed Data & Candidate Build

#### Entri Farchan (UX+Backend)
Aktivitas: Lakukan dry run UAT internal.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Lakukan dry run UAT internal. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'UAT dry-run notes' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Lakukan dry run UAT internal.
- Outcome harian terukur: UAT dry-run notes.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 19-29: startup API untuk dry run UAT internal.
- `DEMO_ACCOUNTS.md` baris 8-26: akun UAT semua role untuk dry run.
- `server/local_api.py` baris 1457-1620: flow participation-report-verify-reward untuk UAT.

#### Entri Ikram (UI+Frontend)
Aktivitas: Polish UI/FE untuk demo.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Polish UI/FE untuk demo dalam konteks 'Dry run UAT internal'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M11: INTEGRATION (W16). Hasil 'UAT dry-run notes' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Polish UI/FE untuk demo.
- Outcome harian terukur: UAT dry-run notes.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 47-112: full user flow setelah polish untuk demo.
- `src/app/App.tsx` baris 182-215: routing halaman yang dipoles untuk demo UAT.
- `src/app/components/ModeratorDashboard.tsx` baris 223-317: moderator panel setelah full polish.

### Day 80 (Jumat, 15 Mei 2026): Freeze candidate build
Status: [RENCANA]
Milestone/Group: M11: INTEGRATION (W16)
Task Referensi Berdua: Seed Data & Candidate Build

#### Entri Farchan (UX+Backend)
Aktivitas: Freeze candidate build backend.
Uraian Kegiatan (Logbook):
"Hari ini fokus saya di 'Freeze candidate build' adalah Freeze candidate build backend. Saya mulai dengan ngerapihin backlog dan dependency backend biar batas kerja sprint jelas, lalu mengunci keputusan teknis yang paling ngaruh ke alur lanjutan. Sebelum close, saya validasi lagi keputusan yang diambil supaya output hari ini 'Candidate build' bisa langsung dipakai tim tanpa ambigu."
Output Farchan:
- Artefak UX+Backend harian selesai: Freeze candidate build backend.
- Outcome harian terukur: Candidate build.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 19-29: startup lokal untuk freeze build test final.
- `server/local_api.py` baris 1211-1620: full API endpoint suite yang di-freeze sebagai baseline.
- `DEMO_ACCOUNTS.md` baris 8-26: akun final yang di-freeze bersama candidate build.

#### Entri Ikram (UI+Frontend)
Aktivitas: Final FE polish candidate.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Final FE polish candidate sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Candidate build' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Final FE polish candidate.
- Outcome harian terukur: Candidate build.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 182-215: routing final kandidat build.
- `src/app/components/UserDashboard.tsx` baris 47-112: full user flow dalam candidate build final.
- `src/app/components/ModeratorDashboard.tsx` baris 223-317: moderator panel di candidate build final.

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
- Artefak UX+Backend harian selesai: Finalisasi test case backend.
- Outcome harian terukur: Test plan final.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-70: daftar modul yang akan diuji pada fase QA.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-115: prioritas test case per severity.
- `docs/status/SYSTEM_SUMMARY.md` baris 237-244: checklist uji fungsional inti untuk test plan.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalisasi test case UI/FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalisasi test case UI/FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Test plan final' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Finalisasi test case UI/FE.
- Outcome harian terukur: Test plan final.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 70-100: area uji admin flow untuk test case.
- `src/app/components/UserDashboard.tsx` baris 47-90: area uji user flow untuk test case.
- `src/app/components/ModeratorDashboard.tsx` baris 223-260: area uji moderator untuk test case.

### Day 82 (Selasa, 19 Mei 2026): Eksekusi test domain inti
Status: [RENCANA]
Milestone/Group: M12: QA EXECUTION (W17)
Task Referensi Berdua: Test Plan & QA Tahap 1

#### Entri Farchan (UX+Backend)
Aktivitas: Eksekusi test auth event report.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Eksekusi test auth event report. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Laporan uji harian' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Eksekusi test auth event report.
- Outcome harian terukur: Laporan uji harian.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-70: daftar issue domain auth-event yang diuji.
- `server/local_api.py` baris 1211-1358: endpoint auth dan event sebagai subjek eksekusi test.
- `docs/status/SYSTEM_SUMMARY.md` baris 253-262: checklist fungsional auth-event untuk validasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: QA responsive dan flow FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke QA responsive dan flow FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Laporan uji harian' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: QA responsive dan flow FE.
- Outcome harian terukur: Laporan uji harian.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 100-131: uji responsif panel admin.
- `src/app/components/ModeratorDashboard.tsx` baris 260-285: uji flow moderator responsif.
- `src/app/components/UserDashboard.tsx` baris 90-112: uji flow user responsif.

### Day 83 (Rabu, 20 Mei 2026): Eksekusi test domain lanjutan
Status: [RENCANA]
Milestone/Group: M12: QA EXECUTION (W17)
Task Referensi Berdua: QA Tahap 2 & Triage Bug

#### Entri Farchan (UX+Backend)
Aktivitas: Eksekusi test verify reward mitra.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Eksekusi test verify reward mitra. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Defect list update' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Eksekusi test verify reward mitra.
- Outcome harian terukur: Defect list update.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 71-92: daftar issue domain verify-reward-mitra yang diuji.
- `server/local_api.py` baris 1576-1694: endpoint verify-reward-mitra sebagai subjek eksekusi test.
- `docs/status/SYSTEM_SUMMARY.md` baris 237-262: checklist fungsional verify dan reward.

#### Entri Ikram (UI+Frontend)
Aktivitas: QA usability dan edge-case FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke QA usability dan edge-case FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Defect list update' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: QA usability dan edge-case FE.
- Outcome harian terukur: Defect list update.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 170-220: uji edge-case inbox moderator.
- `src/app/components/UserDashboard.tsx` baris 300-380: uji usability katalog reward user.
- `src/app/components/AdminDashboard.tsx` baris 70-100: uji edge-case panel admin.

### Day 84 (Kamis, 21 Mei 2026): Triage defect
Status: [RENCANA]
Milestone/Group: M12: QA EXECUTION (W17)
Task Referensi Berdua: QA Tahap 2 & Triage Bug

#### Entri Farchan (UX+Backend)
Aktivitas: Triage defect berdasarkan severity dan owner.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Triage defect berdasarkan severity dan owner pada konteks 'Triage defect'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M12: QA EXECUTION (W17). Setelah selesai, saya pastikan 'Bugboard terurut' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Triage defect berdasarkan severity dan owner.
- Outcome harian terukur: Bugboard terurut.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: triage list dengan severity dan owner.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: pool issue yang di-triage berdasar QA.
- `docs/status/SYSTEM_SUMMARY.md` baris 237-244: acuan severity dari summary sistem.

#### Entri Ikram (UI+Frontend)
Aktivitas: Reproduksi bug dan kumpulkan evidence FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Reproduksi bug dan kumpulkan evidence FE dalam konteks 'Triage defect'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M12: QA EXECUTION (W17). Hasil 'Bugboard terurut' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Reproduksi bug dan kumpulkan evidence FE.
- Outcome harian terukur: Bugboard terurut.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 100-131: reproduksi bug admin flow.
- `src/app/components/UserDashboard.tsx` baris 47-90: reproduksi bug user flow.
- `src/app/components/ModeratorDashboard.tsx` baris 223-260: reproduksi bug moderator flow.

### Day 85 (Jumat, 22 Mei 2026): Patch plan W18
Status: [RENCANA]
Milestone/Group: M12: QA EXECUTION (W17)
Task Referensi Berdua: QA Tahap 2 & Triage Bug

#### Entri Farchan (UX+Backend)
Aktivitas: Susun patch plan untuk W18.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun patch plan untuk W18 dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Rencana patch final' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Susun patch plan untuk W18.
- Outcome harian terukur: Rencana patch final.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: patch plan berdasarkan triage hasil QA.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: backlog issue yang masuk patch plan W18.
- `docs/status/SYSTEM_SUMMARY.md` baris 253-262: target stabilisasi yang disasar patch plan.

#### Entri Ikram (UI+Frontend)
Aktivitas: Susun patch plan UI/FE untuk W18.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun patch plan UI/FE untuk W18 dengan nentuin struktur UI, prioritas aksi pengguna, dan kebutuhan data tiap layar. Saya pastikan keputusan desainnya tetap implementable di FE, bukan berhenti di visual saja. Output 'Rencana patch final' saya susun biar tim bisa lanjut kerja dengan acuan yang konkret."
Output Ikram:
- Artefak UI+Frontend harian selesai: Susun patch plan UI/FE untuk W18.
- Outcome harian terukur: Rencana patch final.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 223-285: area UI/FE moderator yang masuk daftar patch.
- `src/app/components/UserDashboard.tsx` baris 47-112: area user flow yang diprioritaskan di W18.
- `src/app/components/AdminDashboard.tsx` baris 70-131: patch plan area admin untuk W18.

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
- Artefak UX+Backend harian selesai: Fix bug high severity backend.
- Outcome harian terukur: Patch high severity.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1211-1260: patch validasi auth yang menjadi high severity.
- `server/local_api.py` baris 1358-1432: patch endpoint event draft yang high severity.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-115: status patch high severity yang dikerjakan.

#### Entri Ikram (UI+Frontend)
Aktivitas: Fix bug high severity UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug high severity UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Patch high severity' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Fix bug high severity UI/FE.
- Outcome harian terukur: Patch high severity.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-55: patch join state high severity.
- `src/app/components/ReportingWizard.tsx` baris 92-130: patch wizard submit high severity.
- `src/app/components/AdminGodMode.tsx` baris 111-135: patch role assignment high severity.

### Day 87 (Selasa, 26 Mei 2026): Fix medium batch 1
Status: [RENCANA]
Milestone/Group: M13: BUG FIXING (W18)
Task Referensi Berdua: Fix High/Critical Bugs

#### Entri Farchan (UX+Backend)
Aktivitas: Fix bug medium batch 1 backend.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug medium batch 1 backend untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Patch medium batch 1' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Fix bug medium batch 1 backend.
- Outcome harian terukur: Patch medium batch 1.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1433-1518: patch endpoint approval-join medium severity.
- `server/local_api.py` baris 1518-1575: patch submit report medium severity.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 115-123: status patch medium batch 1.

#### Entri Ikram (UI+Frontend)
Aktivitas: Fix bug medium batch 1 UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug medium batch 1 UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Patch medium batch 1' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Fix bug medium batch 1 UI/FE.
- Outcome harian terukur: Patch medium batch 1.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 180-250: patch wizard step 2 medium severity.
- `src/app/components/EventList.tsx` baris 42-43: retest join state setelah patch medium.
- `src/app/components/AdminGodMode.tsx` baris 135-144: patch komponen role medium severity.

### Day 88 (Rabu, 27 Mei 2026): Retest patch
Status: [RENCANA]
Milestone/Group: M13: BUG FIXING (W18)
Task Referensi Berdua: Fix Medium & Retest Stabil

#### Entri Farchan (UX+Backend)
Aktivitas: Retest patch backend.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest patch backend. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Retest report' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Retest patch backend.
- Outcome harian terukur: Retest report.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1202-1400: retest domain auth-event pasca semua patch.
- `server/local_api.py` baris 1400-1620: retest domain report-verify-reward pasca patch.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: update status setelah retest.

#### Entri Ikram (UI+Frontend)
Aktivitas: Retest patch FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest patch FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Retest report' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: Retest patch FE.
- Outcome harian terukur: Retest report.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 92-316: full wizard retest pasca semua patch.
- `src/app/components/EventList.tsx` baris 42-55: retest join flow FE pasca patch medium.
- `src/app/components/AdminGodMode.tsx` baris 111-144: retest role assignment FE.

### Day 89 (Kamis, 28 Mei 2026): Fix critical path sisa
Status: [RENCANA]
Milestone/Group: M13: BUG FIXING (W18)
Task Referensi Berdua: Fix Medium & Retest Stabil

#### Entri Farchan (UX+Backend)
Aktivitas: Fix sisa bug critical path backend.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix sisa bug critical path backend untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Patch critical closed' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Fix sisa bug critical path backend.
- Outcome harian terukur: Patch critical closed.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1576-1637: patch domain verify-scoring critical path backend.
- `server/local_api.py` baris 1637-1694: patch domain reward-redeem critical path backend.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: konfirmasi closed status critical path.

#### Entri Ikram (UI+Frontend)
Aktivitas: Fix sisa bug critical path UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix sisa bug critical path UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Patch critical closed' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Fix sisa bug critical path UI/FE.
- Outcome harian terukur: Patch critical closed.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-55: patch join state critical path pasca bug fix.
- `src/app/components/ReportingWizard.tsx` baris 92-130: patch wizard submit critical path FE.
- `src/app/components/AdminGodMode.tsx` baris 111-135: patch role assignment critical path FE.

### Day 90 (Jumat, 29 Mei 2026): Stabilization build
Status: [RENCANA]
Milestone/Group: M13: BUG FIXING (W18)
Task Referensi Berdua: Fix Medium & Retest Stabil

#### Entri Farchan (UX+Backend)
Aktivitas: Susun stabilization build backend.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun stabilization build backend dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Stabilization build final' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Susun stabilization build backend.
- Outcome harian terukur: Stabilization build final.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1202-1694: full API suite yang diverifikasi dalam stabilization build.
- `server/local_api.py` baris 862-875: scoring dan XP engine yang distabilkan sebagai bagian build.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-123: full status checklist seluruh modul dalam build final.

#### Entri Ikram (UI+Frontend)
Aktivitas: Stabilization pass UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilization pass UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Stabilization build final' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Stabilization pass UI/FE.
- Outcome harian terukur: Stabilization build final.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-55: stabilization pass join state FE pasca semua patch.
- `src/app/components/ReportingWizard.tsx` baris 92-316: stabilization pass full wizard flow FE.
- `src/app/components/AdminGodMode.tsx` baris 111-144: stabilization pass komponen role assignment FE.

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
- Artefak UX+Backend harian selesai: Update grand design final berbasis implementasi.
- Outcome harian terukur: Dokumen + visual final.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 1-18: overview proyek sebagai dasar pembaruan grand design final.
- `docs/README.md` baris 5-16: indeks dokumen teknis yang diperbarui berbasis implementasi aktual.
- `docs/logbook/logbook.md` baris 350-418: progres implementasi W06 sebagai referensi update grand design.

#### Entri Ikram (UI+Frontend)
Aktivitas: Siapkan capture UI dan flow final.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Siapkan capture UI dan flow final sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Dokumen + visual final' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Siapkan capture UI dan flow final.
- Outcome harian terukur: Dokumen + visual final.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LandingPage.tsx` baris 20-30: capture section hero landing awal untuk dokumentasi visual.
- `src/app/components/CollaborationPage.tsx` baris 1-34: capture layout halaman mitra publik untuk aset deck.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 1-40: struktur navigasi IA sebagai konteks capture UI flow.

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
- Artefak UX+Backend harian selesai: Finalisasi logbook dan bukti teknis.
- Outcome harian terukur: Arsip bukti siap.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 19-26: peta dokumentasi proyek sebagai referensi finalisasi logbook teknis.
- `docs/README.md` baris 17-30: panduan paket sidang sebagai referensi pengarsipan bukti teknis.
- `docs/logbook/logbook.md` baris 686-754: progres implementasi W08-W09 sebagai bukti teknis modul event.

#### Entri Ikram (UI+Frontend)
Aktivitas: Rapikan file desain dan aset FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Rapikan file desain dan aset FE dalam konteks 'Finalisasi logbook bukti'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M14: DOCS & PITCH (W19). Hasil 'Arsip bukti siap' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Rapikan file desain dan aset FE.
- Outcome harian terukur: Arsip bukti siap.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LandingPage.tsx` baris 75-108: capture hero section landing untuk aset visual yang diarsipkan.
- `src/app/components/CollaborationPage.tsx` baris 60-104: capture form dan status mitra untuk file desain final.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 40-80: hirarki halaman sebagai referensi penataan aset FE.

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
- Artefak UX+Backend harian selesai: Finalisasi narasi presentasi dan script.
- Outcome harian terukur: Draft deck final.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 1-18: ringkasan proyek sebagai fondasi narasi dan poin utama script presentasi.
- `docs/README.md` baris 5-16: indeks dokumen sebagai referensi poin kunci script pitch sidang.
- `docs/logbook/logbook.md` baris 1022-1090: progres W10-W11 sebagai materi narasi modul report dan verifikasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Siapkan visual slide dan video demo FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Siapkan visual slide dan video demo FE dalam konteks 'Finalisasi narasi presentasi'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M14: DOCS & PITCH (W19). Hasil 'Draft deck final' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Siapkan visual slide dan video demo FE.
- Outcome harian terukur: Draft deck final.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LandingPage.tsx` baris 20-30 dan 75-108: capture landing untuk visual slide presentasi akhir.
- `src/app/components/CollaborationPage.tsx` baris 58-74: capture form mitra sebagai adegan pembuka video demo.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 80-120: alur navigasi FE sebagai storyboard video demo.

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
- Artefak UX+Backend harian selesai: Rehearsal presentasi dan QnA bank.
- Outcome harian terukur: Rehearsal notes.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 19-26: peta dokumentasi sebagai acuan QnA bank teknis sidang.
- `docs/README.md` baris 5-16: indeks dokumen untuk persiapan jawaban pertanyaan sidang.
- `docs/logbook/logbook.md` baris 1358-1426: progres W12-W13 sebagai materi rehearsal modul gamifikasi dan reward.

#### Entri Ikram (UI+Frontend)
Aktivitas: Rehearsal flow demo di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Rehearsal flow demo di FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Rehearsal notes' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: Rehearsal flow demo di FE.
- Outcome harian terukur: Rehearsal notes.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LandingPage.tsx` baris 20-30: urutan tampilan pertama dalam rehearsal flow demo FE.
- `src/app/components/CollaborationPage.tsx` baris 104-168: tampilan sukses mitra sebagai adegan penutup rehearsal.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 120-166: alur navigasi per role sebagai panduan urutan rehearsal.

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
- Artefak UX+Backend harian selesai: Revisi final dokumen KP.
- Outcome harian terukur: Paket sidang siap.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 19-26: peta final dokumentasi sebagai acuan revisi terakhir dokumen KP.
- `docs/README.md` baris 17-30: instruksi paket sidang sebagai referensi revisi akhir teknis.
- `docs/logbook/logbook.md` baris 1526-1594: progres implementasi W14-W15 untuk bagian akhir dokumen KP.

#### Entri Ikram (UI+Frontend)
Aktivitas: Revisi final visual dan flow FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Revisi final visual dan flow FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Paket sidang siap' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Revisi final visual dan flow FE.
- Outcome harian terukur: Paket sidang siap.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LandingPage.tsx` baris 20-30 dan 75-108: revisi final tampilan landing untuk paket sidang.
- `src/app/components/CollaborationPage.tsx` baris 58-74 dan 104-168: revisi final tampilan mitra untuk paket sidang.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 166-206: acuan visual akhir setelah semua revisi selesai.

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
- Artefak UX+Backend harian selesai: UAT final dengan mentor dan checklist.
- Outcome harian terukur: UAT checklist.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/logbook.md` baris 1526-1560: acuan aktivitas Day 96 untuk UAT checklist dengan mentor.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 52-55: sinkron hari pertama UAT antara Farchan dan Ikram.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 84-87: kriteria penerimaan UAT final W20.

#### Entri Ikram (UI+Frontend)
Aktivitas: Catat feedback UI/FE final.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Catat feedback UI/FE final sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'UAT checklist' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Catat feedback UI/FE final.
- Outcome harian terukur: UAT checklist.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 84-87: kriteria UAT final untuk pencatatan feedback UI/FE.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 52-55: sinkron feedback UAT hari pertama antara dua anggota.
- `src/app/App.tsx` baris 216-250: routing view yang diuji dalam sesi UAT bersama mentor.

### Day 97 (Selasa, 9 Jun 2026): Patch minor final
Status: [RENCANA]
Milestone/Group: M15: CLOSING (W20)
Task Referensi Berdua: UAT Mentor & Minor Patch

#### Entri Farchan (UX+Backend)
Aktivitas: Implement perubahan minor final backend.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Implement perubahan minor final backend sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Minor patch complete' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement perubahan minor final backend.
- Outcome harian terukur: Minor patch complete.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/logbook.md` baris 1560-1570: acuan aktivitas Day 97 untuk patch minor backend.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 55-57: sinkron patch minor antar anggota tim pasca UAT.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63: target penutupan W20 setelah patch minor.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement patch minor final UI/FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Implement patch minor final UI/FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Minor patch complete' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement patch minor final UI/FE.
- Outcome harian terukur: Minor patch complete.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63: acuan output minor patch sebelum closing W20.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 55-57: sinkron minor patch UI/FE antara anggota tim.
- `src/app/App.tsx` baris 250-279: bagian routing tambahan yang di-patch minor dalam closing sprint.

### Day 98 (Rabu, 10 Jun 2026): Readiness final
Status: [RENCANA]
Milestone/Group: M15: CLOSING (W20)
Task Referensi Berdua: Handover & Submit Laporan

#### Entri Farchan (UX+Backend)
Aktivitas: Final readiness note operasional.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Final readiness note operasional sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Readiness note' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Final readiness note operasional.
- Outcome harian terukur: Readiness note.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/logbook.md` baris 1570-1580: acuan aktivitas Day 98 untuk penyusunan readiness note.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 57-59: kontrol readiness akhir tim sebelum handover.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 80-87: checklist readiness dan kriteria sign-off operasional.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalisasi handoff UI/FE note.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalisasi handoff UI/FE note sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Readiness note' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Finalisasi handoff UI/FE note.
- Outcome harian terukur: Readiness note.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 80-84: checklist handoff per milestone sebagai referensi note.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 57-59: catatan readiness akhir FE untuk handoff dokumen.
- `src/app/App.tsx` baris 216-279: full routing final sebagai bagian dari handoff UI/FE kepada pihak terkait.

### Day 99 (Kamis, 11 Jun 2026): Closing report dan handover
Status: [RENCANA]
Milestone/Group: M15: CLOSING (W20)
Task Referensi Berdua: Handover & Submit Laporan

#### Entri Farchan (UX+Backend)
Aktivitas: Susun closing report dan handover teknis.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun closing report dan handover teknis dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Closing package' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Susun closing report dan handover teknis.
- Outcome harian terukur: Closing package.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/logbook.md` baris 1580-1590: acuan aktivitas Day 99 untuk penyusunan closing report.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 50-52: template handover teknis tim dalam closing package.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 84-87: kriteria handover proyek untuk closing package.

#### Entri Ikram (UI+Frontend)
Aktivitas: Arsip source UI/FE dan dokumentasi.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Arsip source UI/FE dan dokumentasi dalam konteks 'Closing report dan handover'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M15: CLOSING (W20). Hasil 'Closing package' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Arsip source UI/FE dan dokumentasi.
- Outcome harian terukur: Closing package.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 84-87: acuan output arsip sebelum sign-off final proyek.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 50-52: panduan arsip dan penyimpanan dokumen tim.
- `src/app/App.tsx` baris 216-250: routing FE sebagai bagian dari arsip source yang diserahkan dalam closing.

### Day 100 (Jumat, 12 Jun 2026): Presentasi akhir dan retrospektif
Status: [RENCANA]
Milestone/Group: M15: CLOSING (W20)
Task Referensi Berdua: Handover & Submit Laporan

#### Entri Farchan (UX+Backend)
Aktivitas: Presentasi akhir dan retrospektif proyek.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Presentasi akhir dan retrospektif proyek pada konteks 'Presentasi akhir dan retrospektif'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M15: CLOSING (W20). Setelah selesai, saya pastikan 'Proyek ditutup' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Presentasi akhir dan retrospektif proyek.
- Outcome harian terukur: Proyek ditutup.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/logbook.md` baris 1590-1594: catatan penutupan Day 100 sebagai hari terakhir proyek.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 52-59: retrospektif akhir lintas anggota tim dua orang.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63 dan 84-87: evaluasi capaian akhir seluruh milestone proyek.

#### Entri Ikram (UI+Frontend)
Aktivitas: Support demo akhir dan sign-off.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Support demo akhir dan sign-off dalam konteks 'Presentasi akhir dan retrospektif'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M15: CLOSING (W20). Hasil 'Proyek ditutup' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Support demo akhir dan sign-off.
- Outcome harian terukur: Proyek ditutup.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63 dan 84-87: acuan timeline milestone untuk slide penutup presentasi akhir.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 52-59: sinkron akhir tim dua orang pasca presentasi dan sign-off.
- `src/app/App.tsx` baris 216-279: routing final FE sebagai bukti kelengkapan saat sign-off proyek.

