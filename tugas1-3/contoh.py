"""Contoh kode untuk latihan query Tree-sitter."""

import os
from pathlib import Path
from .local import helper


def sapa(nama, formal=False):
    """Menyapa seseorang."""
    if formal:
        print("Selamat datang,", nama)
    else:
        print("Hai,", nama)


def tambah(a, b=1):
    return a + b


class Layanan:
    def jalankan(self):
        return tambah(2, 3)
