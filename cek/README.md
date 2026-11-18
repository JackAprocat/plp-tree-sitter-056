# Tree-sitter Python Checker

CLI untuk memindai proyek Python dan melaporkan komentar `TODO`/`FIXME`,
fungsi yang mencakup lebih dari 30 baris, serta file dengan kesalahan parse.

## Instalasi

Dari folder root tugas:

```powershell
python -m pip install -r requirements.txt
```

## Menjalankan

```powershell
python cek\cek.py path\ke\proyek
```

Folder `.git`, `node_modules`, `venv`, `.venv`, dan `__pycache__` dilewati.
Jumlah baris fungsi dihitung dari awal sampai akhir node `function_definition`;
fungsi di dalam kelas dan fungsi bersarang juga dihitung.

Contoh:

```text
src\handler.py:12: # TODO: add validation
src\handler.py:20: fungsi process_order panjang (34 baris)
src\broken.py:8: syntax error (MISSING)
```

## Tes

```powershell
python -m unittest discover -s cek\tests -v
```
