import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser

from cek.cek import check_file, python_files


class CheckerTests(unittest.TestCase):
    def test_reports_todo_long_function_and_syntax_error(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            folder = Path(temporary_directory)
            (folder / "todo.py").write_text(
                '# TODO: finish this\nmessage = "TODO: not a comment"\n',
                encoding="utf-8",
            )
            body = "\n".join(f"    value_{index} = {index}" for index in range(35))
            (folder / "long.py").write_text(
                f"def lengthy():\n{body}\n    return value_34\n",
                encoding="utf-8",
            )
            short_body = "\n".join(f"    value_{index} = {index}" for index in range(28))
            (folder / "short.py").write_text(
                f"def short():\n{short_body}\n    return value_27\n",
                encoding="utf-8",
            )
            (folder / "broken.py").write_text("def unfinished(:\n    pass\n", encoding="utf-8")

            parser = Parser(Language(tspython.language()))
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                for path in sorted(folder.glob("*.py")):
                    check_file(path, parser)

            report = output.getvalue()
            self.assertIn("TODO: finish this", report)
            self.assertEqual(1, report.count("todo.py:"))
            self.assertIn("fungsi lengthy panjang", report)
            self.assertNotIn("fungsi short panjang", report)
            self.assertIn("broken.py:1: syntax error (MISSING)", report)

    def test_skips_common_generated_and_dependency_folders(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            folder = Path(temporary_directory)
            (folder / "app.py").write_text("pass\n", encoding="utf-8")
            excluded = folder / "venv"
            excluded.mkdir()
            (excluded / "package.py").write_text("pass\n", encoding="utf-8")

            self.assertEqual([folder / "app.py"], list(python_files(folder)))


if __name__ == "__main__":
    unittest.main()
