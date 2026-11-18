import argparse

import tree_sitter_python as tspython
from tree_sitter import Language, Parser


def jelajah(node, kedalaman=0, field=None):
    baris, kolom = node.start_point
    label = f"{field}: " if field else ""
    print("  " * kedalaman + f"{label}{node.type} [{baris + 1}:{kolom}]")

    for index, child in enumerate(node.children):
        if child.is_named:
            jelajah(child, kedalaman + 1, node.field_name_for_child(index))


def main():
    arg_parser = argparse.ArgumentParser(description="Cetak pohon node bernama dari file Python.")
    arg_parser.add_argument("file", help="Path file Python")
    args = arg_parser.parse_args()

    parser = Parser(Language(tspython.language()))
    source = open(args.file, "rb").read()
    tree = parser.parse(source)
    jelajah(tree.root_node)


if __name__ == "__main__":
    main()
