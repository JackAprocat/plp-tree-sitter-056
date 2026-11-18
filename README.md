# Praktikum Tree-sitter

Implementasi artefak kode untuk materi `Part 1 - Tree-sitter.md`.

## Struktur

- `tugas1-3/`: contoh parse pohon, penjelajah node, dan query Python.
- `tree-sitter-filter/`: grammar DSL filter, corpus pengujian, dan query highlight.
- `cek/`: CLI untuk menemukan komentar TODO/FIXME, fungsi panjang, dan parse error.
- `proposal-draf.md`: draf topik proyek pilihan.
- `laporan-template.md`: kerangka laporan; lengkapi dengan bukti hasil kerja Anda.

## Setup Python

Di PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Menjalankan latihan

```powershell
.\.venv\Scripts\python.exe tugas1-3\t1.py
.\.venv\Scripts\python.exe tugas1-3\jelajah.py tugas1-3\contoh.py
.\.venv\Scripts\python.exe tugas1-3\q.py tugas1-3\contoh.py fungsi
.\.venv\Scripts\python.exe -m unittest discover -s cek\tests -v
.\.venv\Scripts\python.exe cek\cek.py tugas1-3
```

## Grammar filter

Prasyarat: Node.js/npm, tree-sitter CLI, dan compiler C. Dari PowerShell:

```powershell
cd tree-sitter-filter
npm install
npm install-scripts approve tree-sitter-cli
npm rebuild tree-sitter-cli
.\node_modules\.bin\tree-sitter.cmd generate
.\node_modules\.bin\tree-sitter.cmd test
```

Pada npm yang memblokir lifecycle scripts, dua perintah tengah mengizinkan
installer CLI resmi menyiapkan binary Tree-sitter lokal.
Jika parser-directory CLI belum dikonfigurasi untuk highlight, `tree-sitter parse`
dan `tree-sitter test` tetap dapat dijalankan dari folder grammar. Untuk
`tree-sitter highlight`, jalankan `tree-sitter init-config` lalu tambahkan
folder induk `tree-sitter-filter/` ke `parser-directories`.

## Catatan bukti tugas

Output mesin dapat dibuat ulang dengan perintah di atas. Prediksi pohon tulisan
tangan, pemeriksaan manual pada repositori nyata, tangkapan layar, kendala yang
Anda alami, dan catatan AI harus dilengkapi sendiri secara jujur sebelum
pengumpulan.
