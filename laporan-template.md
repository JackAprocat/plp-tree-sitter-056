# Template Laporan Praktikum Tree-sitter

> Lengkapi dengan bukti milik Anda. Jangan mengklaim pemeriksaan manual,
> tangkapan layar, atau percobaan yang belum dilakukan.

## Tugas 1–3
- Output tersimpan di `tugas1-3/output_t1.txt` dan `tugas1-3/output_query_*.txt`.
- Penjelajah sudah dijalankan pada fixture 108 baris; output ada di
  `tugas1-3/output_jelajah_100_baris.txt`.
- Penjelajah juga dijalankan pada file nyata `tests/test_node.py` (424 baris)
  dari repositori uji; output ada di `tugas1-3/output_jelajah_real_100_baris.txt`.
- Hasil query fixture: 3 fungsi, 2 pemanggilan `print`, 3 modul import
  (termasuk relative import).
- Prediksi pohon tulisan tangan dan perbandingan hasil:
- Temuan node anonim serta `ERROR`/`MISSING`:
- Hasil hitungan manual:

## Tugas 4–5
- Hasil terakhir `tree-sitter test`: 9/9 kasus lulus.
- Kasus prioritas `and`/`or`, tanda kurung, `not`, tipe nilai, `in`, dan `contains`:
- `tree-sitter highlight --check contoh.filter`: semua capture memenuhi standar.
- Hasil highlight HTML tersedia di `tree-sitter-filter/output_highlight.html`.
- Query proposal JavaScript diuji pada kode positif, komentar, dan string;
  hasilnya satu pemanggilan nyata, tanpa parse error (`proposal-query-check.txt`).
- Tangkapan layar:
- Kendala dan penyelesaian:

## Tugas 6
- Repositori nyata: `tree-sitter/py-tree-sitter` (hasil 16 temuan disimpan
  di `cek/output_repo_scan.txt`: satu FIXME dan 15 fungsi panjang; tidak ada
  file dengan parse error).
- Dua file yang dipilih untuk pemeriksaan manual: `docs/conf.py` dan
  `examples/walk_tree.py`. Keduanya tidak menghasilkan temuan scanner setelah
  pembacaan manual; catat tangkapan layar atau pemeriksaan tambahan Anda:

## Catatan penggunaan AI
AI digunakan untuk membantu menyiapkan kode tugas. Review dan tes menemukan
beberapa kekurangan hasil awal:

- Konfigurasi grammar memiliki properti typo ` грамmars`; properti itu dihapus
  dan pemeriksaan konfigurasi mengonfirmasi key `grammars` yang benar.
- Pohon harapan awal menampilkan operator anonim yang tidak muncul di S-expression,
  dan kasus kurung memiliki satu kurung penutup yang kurang. Corpus awal gagal;
  setelah diperbaiki, `tree-sitter test` lulus 9/9 kasus.
- Fixture Tugas 2 sempat memiliki UTF-8 BOM sehingga node pertama berada di
  kolom 3; setelah dibuat ulang tanpa BOM, node berada di kolom 0.
- Tes Tugas 6 awalnya mengharapkan node `ERROR`, tetapi hasil parser input itu
  adalah `MISSING`; assertion diperbaiki dan 2 tes unit lulus.

Catat prompt AI dan pemeriksaan yang Anda lakukan untuk setiap tugas, serta
tambahkan kesalahan lain hanya jika benar-benar ditemukan dengan bukti.

## Kendala dan solusi
- Kendala:
- Cara mengatasi:
