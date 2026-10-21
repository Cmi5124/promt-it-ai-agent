"""Offline CLI tests for reuse_catalog.py; fixtures are synthetic, not upstream evidence."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "reuse_catalog.py"


class ReuseCatalogTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)
        self.index = self.dir / "entries.json"
        self.data = [
            {"name": "Ghidra bridge", "url": "https://github.com/example/ghidra-bridge", "desc": "Ghidra MCP adapter", "category": "RE Tooling", "lang": "Python", "license": "MIT", "stars": 100, "archived": False, "topics": ["ghidra", "mcp"]},
            {"name": "Ghidra deprecated", "url": "https://github.com/example/old", "desc": "Ghidra MCP adapter", "category": "RE Tooling", "lang": "Python", "stars": 1000000, "archived": True},
            {"name": "PSD reader", "url": "https://github.com/example/psd-reader", "desc": "PSD file parser", "category": "File Formats", "lang": "Rust", "license": "Apache-2.0", "stars": 9},
        ]
        self.index.write_text(json.dumps(self.data), encoding="utf-8")

    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), "--index", str(self.index), *args],
                              cwd=self.dir, capture_output=True, text=True, timeout=6, check=False)

    def test_normal_search_ranks_active_specific_candidate(self) -> None:
        run = self.run_cli("search", "ghidra", "mcp")
        self.assertEqual(run.returncode, 0, run.stderr)
        found = json.loads(run.stdout)
        self.assertEqual(found[0]["name"], "Ghidra bridge")
        self.assertEqual(found[0]["license"], "MIT")
        self.assertIn("INDEX_METADATA_ONLY", found[0]["source_status"])

    def test_boundary_no_hits(self) -> None:
        run = self.run_cli("search", "not-present-xyz")
        self.assertEqual(run.returncode, 0)
        self.assertEqual(json.loads(run.stdout), [])

    def test_boundary_invalid_limit(self) -> None:
        run = self.run_cli("search", "psd", "--limit", "0")
        self.assertEqual(run.returncode, 2)
        self.assertIn("BLOCKED", run.stderr)

    def test_filter_category_language(self) -> None:
        run = self.run_cli("search", "parser", "--category", "formats", "--lang", "Rust")
        self.assertEqual(run.returncode, 0)
        self.assertEqual([r["name"] for r in json.loads(run.stdout)], ["PSD reader"])

    def test_inspect_repo(self) -> None:
        run = self.run_cli("inspect", "example/ghidra-bridge")
        self.assertEqual(run.returncode, 0)
        self.assertEqual(json.loads(run.stdout)["name"], "Ghidra bridge")

    def test_categories(self) -> None:
        run = self.run_cli("categories")
        self.assertEqual(run.returncode, 0)
        self.assertEqual(json.loads(run.stdout)["RE Tooling"], 2)

    def test_invalid_corrupt_json(self) -> None:
        self.index.write_text("not JSON", encoding="utf-8")
        run = self.run_cli("search", "ghidra")
        self.assertEqual(run.returncode, 2)
        self.assertIn("BLOCKED", run.stderr)

    def test_invalid_entry_shape(self) -> None:
        self.index.write_text('{"repositories":[]}', encoding="utf-8")
        run = self.run_cli("search", "ghidra")
        self.assertEqual(run.returncode, 2)
        self.assertIn("BLOCKED", run.stderr)

    def test_dependency_missing_index(self) -> None:
        self.index.unlink()
        run = self.run_cli("search", "ghidra")
        self.assertEqual(run.returncode, 2)
        self.assertIn("unavailable", run.stderr)

    def test_security_metadata_is_inert_not_executed(self) -> None:
        marker = self.dir / "SHOULD_NOT_EXIST"
        self.data[0]["desc"] = f"$(touch {marker}) ; rm -rf / ; malicious embedded text"
        self.data[0]["name"] = "Ghidra\n\x1b[2J injected"
        self.index.write_text(json.dumps(self.data), encoding="utf-8")
        run = self.run_cli("search", "ghidra")
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertFalse(marker.exists())
        self.assertNotIn("\x1b", run.stdout)
        self.assertEqual(json.loads(run.stdout)[0]["name"], "Ghidra injected")

    def test_missing_license_is_marked_not_verified(self) -> None:
        run = self.run_cli("inspect", "example/old")
        self.assertEqual(run.returncode, 0)
        self.assertEqual(json.loads(run.stdout)["license"], "NOT_VERIFIED")


if __name__ == "__main__":
    unittest.main()
