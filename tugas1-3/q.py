import argparse
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor


LANGUAGE = Language(tspython.language())
QUERY_FILES = {
    "identifier": Path(__file__).with_name("semua_identifier.scm"),
    "fungsi": Path(__file__).with_name("nama_fungsi_dan_parameter.scm"),
    "print": Path(__file__).with_name("pemanggilan_print.scm"),
    "import": Path(__file__).with_name("modul_import.scm"),
}


def run_query(kind, root):
    query = Query(LANGUAGE, QUERY_FILES[kind].read_text(encoding="utf-8"))
    cursor = QueryCursor(query)

    if kind == "fungsi":
        for _, captures in cursor.matches(root):
            name = captures["nama"][0].text.decode()
            params = captures["params"][0]
            print(f"fungsi {name}: {params.named_child_count} parameter")
    else:
        capture_name = {"identifier": "id", "print": "fungsi", "import": "modul"}[kind]
        captures = cursor.captures(root).get(capture_name, [])
        for node in captures:
            print(f"{kind}: {node.text.decode()}")


def main():
    parser = argparse.ArgumentParser(description="Jalankan query Tree-sitter pada file Python.")
    parser.add_argument("file", type=Path)
    parser.add_argument("query", choices=QUERY_FILES)
    args = parser.parse_args()

    source = args.file.read_bytes()
    tree = Parser(LANGUAGE).parse(source)
    run_query(args.query, tree.root_node)


if __name__ == "__main__":
    main()
