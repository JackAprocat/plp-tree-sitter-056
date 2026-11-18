import argparse
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor


LANGUAGE = Language(tspython.language())
LONG_FUNCTION_QUERY = Query(
    LANGUAGE,
    """
    (function_definition
      name: (identifier) @nama) @fungsi
    """,
)
TODO_QUERY = Query(
    LANGUAGE,
    '((comment) @komentar (#match? @komentar "TODO|FIXME"))',
)
EXCLUDED_DIRECTORIES = {".git", "node_modules", "venv", ".venv", "__pycache__"}


def first_parse_issue(node):
    if node.is_error:
        return node, "ERROR"
    if node.is_missing:
        return node, "MISSING"

    for child in node.children:
        issue = first_parse_issue(child)
        if issue is not None:
            return issue
    return None


def check_file(path, parser):
    source = path.read_bytes()
    tree = parser.parse(source)

    for node in QueryCursor(TODO_QUERY).captures(tree.root_node).get("komentar", []):
        print(f"{path}:{node.start_point[0] + 1}: {node.text.decode(errors='replace').strip()}")

    for _, captures in QueryCursor(LONG_FUNCTION_QUERY).matches(tree.root_node):
        function = captures["fungsi"][0]
        name = captures["nama"][0].text.decode(errors="replace")
        lines = function.end_point[0] - function.start_point[0] + 1
        if lines > 30:
            print(f"{path}:{function.start_point[0] + 1}: fungsi {name} panjang ({lines} baris)")

    if tree.root_node.has_error:
        issue = first_parse_issue(tree.root_node)
        if issue is None:
            raise RuntimeError(f"Parse tree for {path} reports an error without an error node")
        node, issue_type = issue
        print(f"{path}:{node.start_point[0] + 1}: syntax error ({issue_type})")


def python_files(folder):
    for path in sorted(folder.rglob("*.py")):
        if not EXCLUDED_DIRECTORIES.intersection(path.parts):
            yield path


def main():
    arg_parser = argparse.ArgumentParser(
        description="Cari TODO/FIXME, fungsi panjang, dan kesalahan sintaks Python."
    )
    arg_parser.add_argument("folder", type=Path, help="Folder proyek yang dipindai")
    args = arg_parser.parse_args()

    if not args.folder.exists() or not args.folder.is_dir():
        arg_parser.error(f"folder tidak ditemukan atau bukan direktori: {args.folder}")

    parser = Parser(LANGUAGE)
    for path in python_files(args.folder):
        check_file(path, parser)


if __name__ == "__main__":
    main()
