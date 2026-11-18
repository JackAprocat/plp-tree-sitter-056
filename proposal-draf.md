# Draf Proposal Proyek

## Judul
Pemeriksa larangan `console.log` pada kode produksi JavaScript

## Masalah dan pengguna
Developer dan reviewer pada tim aplikasi web enterprise perlu memastikan bahwa
kode produksi tidak meninggalkan pemanggilan `console.log`, yang dapat
membocorkan informasi internal atau menambah noise log. Pemeriksa ini memberi
laporan lokasi sebelum perubahan digabungkan.

## Mengapa tidak cukup meminta AI
Pemeriksaan AI bersifat probabilistik, dapat melewatkan pemanggilan tertentu,
dan perlu dijalankan lagi untuk setiap perubahan. Pemindai Tree-sitter
deterministik, cepat, dan dapat dijalankan lokal atau di CI pada setiap commit.
Parser juga dapat membedakan pemanggilan fungsi dari teks `console.log` di
komentar atau string.

## Bahasa, framework, dan grammar
JavaScript (proyek web Express); binding grammar Python: `tree-sitter-javascript`.
Skop awal hanya file `.js`, dengan pengecualian direktori test dan vendor yang
ditentukan lewat konfigurasi sederhana.

## Contoh yang dideteksi dan dikecualikan

```javascript
console.log("debug"); // harus terdeteksi
```

```javascript
// console.log("contoh di komentar") -- tidak terdeteksi
const pesan = "console.log bukan pemanggilan"; // tidak terdeteksi
```

## Rancangan query

```scheme
(call_expression
  function: (member_expression
    object: (identifier) @obj
    property: (property_identifier) @method)
  (#eq? @obj "console")
  (#eq? @method "log")) @call
```

## Output
Laporan terminal dengan path, nomor baris, dan potongan pemanggilan; exit code
non-zero jika temuan ditemukan agar dapat dipakai sebagai quality gate CI.

## Rencana dan risiko
1. Pastikan grammar dan struktur node pada contoh JavaScript.
2. Implementasikan query, pemindaian folder, pengecualian direktori, dan tes
   positif/negatif.
3. Uji pada satu repositori web kecil dan cocokkan sebagian temuan secara manual.

Risiko utama adalah variasi pola penulisan (misalnya alias `const log =
console.log`) dan file generated/vendor. Versi awal hanya mendeteksi pemanggilan
langsung; batasan itu akan didokumentasikan, bukan diklaim sebagai analisis
semantik lengkap.
