"""CLI regressions for FIX-03/06 and input/resource failure boundaries."""
from __future__ import annotations

import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unicodedata
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/reuse_catalog.py"
spec = importlib.util.spec_from_file_location("catalog_under_test", ROOT / "skills/adaptive-project-ops/scripts/reuse_catalog.py")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class MaintenanceCLITest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.index = self.folder / "entries.json"
        self.entries = [{"name": "Straße", "url": "https://github.com/example/road",
                         "desc": "Công cụ phân tích 🔒", "category": "Công cụ",
                         "subcategory": "Phân tích", "lang": "Tiếng Việt",
                         "topics": ["Đường phố"], "license": "MIT", "stars": 1}]
        self.write_index()

    def write_index(self):
        self.index.write_text(json.dumps(self.entries, ensure_ascii=True), encoding="utf-8")

    def cli(self, *args, encoding="utf-8"):
        env = dict(os.environ, PYTHONIOENCODING=f"{encoding}:strict", PYTHONDONTWRITEBYTECODE="1")
        return subprocess.run([sys.executable, str(SCRIPT), "--index", str(self.index), *args],
                              cwd=self.folder, env=env, capture_output=True, timeout=10, check=False)

    def decoded(self, run, encoding="utf-8"):
        self.assertEqual(run.returncode, 0, run.stderr.decode(encoding))
        return json.loads(run.stdout.decode(encoding))

    def test_strasse_casefold(self):
        """U01 | Unicode index | Straße/STRASSE/strasse | same original entry."""
        for query in ("Straße", "STRASSE", "strasse"):
            with self.subTest(query=query):
                self.assertEqual(self.decoded(self.cli("search", query))[0]["name"], "Straße")

    def test_vietnamese_composed_and_decomposed(self):
        """U02 | NFD name | NFC/NFD query | match and preserve original codepoints."""
        original = unicodedata.normalize("NFD", "Tiếng Việt")
        self.entries[0]["name"] = original
        self.write_index()
        for query in ("TIẾNG VIỆT", original):
            with self.subTest(query=query):
                self.assertEqual(self.decoded(self.cli("search", query))[0]["name"], original)

    def test_emoji_search(self):
        """U03 | emoji in description | search 🔒 | exact Unicode description retained."""
        self.assertEqual(self.decoded(self.cli("search", "🔒"))[0]["desc"], self.entries[0]["desc"])

    def test_normalization_all_search_fields(self):
        """U04 | one populated weighted field | STRASSE | each field searchable."""
        for field in ("name", "url", "desc", "category", "subcategory", "topics"):
            with self.subTest(field=field):
                self.entries = [{field: ["Straße"] if field == "topics" else "Straße"}]
                self.write_index()
                self.assertEqual(len(self.decoded(self.cli("search", "STRASSE"))), 1)

    def test_unicode_filters(self):
        """U05 | Unicode filters | decomposed category/language | one match."""
        found = self.decoded(self.cli("search", "strasse", "--category", unicodedata.normalize("NFD", "CÔNG CỤ"),
                                      "--lang", unicodedata.normalize("NFD", "TIẾNG VIỆT")))
        self.assertEqual(len(found), 1)

    def test_cp1252_json_fallback(self):
        """U06 | redirected cp1252 strict stdout | all CLI modes | parseable escaped JSON."""
        for args in (("search", "STRASSE"), ("inspect", "example/road"), ("categories",)):
            with self.subTest(args=args):
                run = self.cli(*args, encoding="cp1252")
                parsed = self.decoded(run, "cp1252")
                self.assertTrue(parsed)
                self.assertIn(b"\\u", run.stdout)
                if args[0] != "categories":
                    entry = parsed[0] if isinstance(parsed, list) else parsed
                    self.assertEqual(entry["desc"], self.entries[0]["desc"])

    def test_utf8_json_preserves_literal_unicode(self):
        """U07 | redirected UTF-8 strict stdout | Unicode metadata | literal bytes and valid JSON."""
        run = self.cli("search", "STRASSE")
        self.assertEqual(self.decoded(run)[0]["desc"], self.entries[0]["desc"])
        self.assertIn("🔒".encode("utf-8"), run.stdout)
        self.assertNotIn(b"\\u", run.stdout)

    def test_stdout_without_encoding(self):
        """U08 | StringIO stdout | print Unicode object | valid JSON without encoding attribute."""
        output = io.StringIO()
        with patch.object(sys, "stdout", output):
            catalog.print_json(self.entries)
        self.assertEqual(json.loads(output.getvalue()), self.entries)

    def test_query_length_boundary(self):
        """U09 | valid index | lengths 160/161 | exit 0 then controlled exit 2."""
        self.assertEqual(self.cli("search", "x" * 160).returncode, 0)
        run = self.cli("search", "x" * 161)
        self.assertEqual(run.returncode, 2)
        self.assertIn(b"BLOCKED", run.stderr)

    def test_limit_boundaries(self):
        """U10 | valid index | limits 1/50/51/-1 | accept only inclusive valid range."""
        for limit in (1, 50, 51, -1):
            with self.subTest(limit=limit):
                run = self.cli("search", "STRASSE", "--limit", str(limit))
                self.assertEqual(run.returncode, 0 if 1 <= limit <= 50 else 2)

    def test_invalid_list_entry(self):
        """U11 | mixed JSON array | object plus scalar | controlled BLOCKED exit 2."""
        self.index.write_text('[{}, 7]', encoding="utf-8")
        run = self.cli("search", "x")
        self.assertEqual(run.returncode, 2)
        self.assertIn(b"each entry", run.stderr)

    def test_permission_denied_read(self):
        """U12 | mocked OS denial | open index | controlled BLOCKED with no file mutation."""
        before = self.index.read_bytes()
        with patch.object(Path, "open", side_effect=PermissionError("synthetic denial")):
            with self.assertRaisesRegex(ValueError, "BLOCKED.*synthetic denial"):
                catalog.read_entries(self.index)
        self.assertEqual(self.index.read_bytes(), before)

    def test_resource_limits(self):
        """U13 | bounded fixture thresholds | oversize bytes/entry count | reject both limits."""
        with patch.object(catalog, "MAX_INDEX_BYTES", 1):
            with self.assertRaisesRegex(ValueError, "exceeds"):
                catalog.read_entries(self.index)
        with patch.object(catalog, "MAX_ENTRIES", 0):
            with self.assertRaisesRegex(ValueError, "entry limit"):
                catalog.read_entries(self.index)

    def test_search_deterministic_ascii_ranking(self):
        """U14 | original ranking weights | repeated ASCII search | active specific candidate first."""
        self.entries = [{"name": "Ghidra active", "desc": "MCP", "license": "MIT", "stars": 1},
                        {"name": "Ghidra old", "desc": "MCP", "archived": True, "stars": 1000000}]
        self.write_index()
        first = self.cli("search", "ghidra", "mcp")
        self.assertEqual(self.decoded(first)[0]["name"], "Ghidra active")
        self.assertEqual(first.stdout, self.cli("search", "ghidra", "mcp").stdout)

    def test_missing_unicode_path_cp1252(self):
        """U15 | nonexistent Unicode path, cp1252 stderr | search | controlled exit 2, no traceback."""
        self.index = self.folder / "không-có-🔒.json"
        run = self.cli("search", "x", encoding="cp1252")
        self.assertEqual(run.returncode, 2)
        self.assertIn(b"BLOCKED", run.stderr)
        self.assertNotIn(b"Traceback", run.stderr)


if __name__ == "__main__":
    unittest.main()
