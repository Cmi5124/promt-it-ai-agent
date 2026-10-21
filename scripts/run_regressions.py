#!/usr/bin/env python3
"""Run offline unittest suite and write per-test evidence outside the bundle."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import platform
import sys
import time
import unittest
from pack_utils import write_text_lf

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = {
    "test_normal_search_ranks_active_specific_candidate": ("O01", "three synthetic entries", "search ghidra mcp", "active specific candidate ranks first; license and evidence status retained"),
    "test_boundary_no_hits": ("O02", "synthetic index", "unmatched query", "exit 0 and empty JSON list"),
    "test_boundary_invalid_limit": ("O03", "synthetic index", "limit 0", "exit 2 and BLOCKED"),
    "test_filter_category_language": ("O04", "mixed categories/languages", "parser, formats, Rust", "only PSD reader returned"),
    "test_inspect_repo": ("O05", "synthetic repository URL", "example/ghidra-bridge", "matching entry returned"),
    "test_categories": ("O06", "three entries", "categories", "RE Tooling count is 2"),
    "test_invalid_corrupt_json": ("O07", "invalid JSON file", "search ghidra", "exit 2 and BLOCKED"),
    "test_invalid_entry_shape": ("O08", "object instead of JSON list", "search ghidra", "exit 2 and BLOCKED"),
    "test_dependency_missing_index": ("O09", "missing fixture file", "search ghidra", "exit 2 and unavailable error"),
    "test_security_metadata_is_inert_not_executed": ("O10", "metadata containing shell text/control bytes", "search ghidra", "no marker execution; control characters removed"),
    "test_missing_license_is_marked_not_verified": ("O11", "entry without license", "inspect example/old", "license NOT_VERIFIED"),
}


class EvidenceResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []
        self.active = {}

    def startTest(self, test):
        super().startTest(test)
        method = test.id().rsplit(".", 1)[-1]
        details = ORIGINAL.get(method)
        if details is None:
            doc = test.shortDescription() or ""
            parts = [part.strip().rstrip(".") for part in doc.split("|")]
            if len(parts) != 4:
                raise ValueError(f"Test metadata missing: {test.id()}")
            details = tuple(parts)
        key, precondition, data, expected = details
        self.active[test.id()] = {"id": key, "test": test.id(), "preconditions": precondition,
                                  "input": data, "expected": expected, "actual": "Not completed",
                                  "status": "NOT_RUN", "evidence": "TEST_RUN.txt", "started": time.monotonic()}

    def outcome(self, test, status, actual):
        self.active[test.id()].update(status=status, actual=actual)

    def addSuccess(self, test):
        super().addSuccess(test)
        self.outcome(test, "PASS", "All assertions completed successfully; asserted outputs are defined in the named test.")

    def addFailure(self, test, error):
        super().addFailure(test, error)
        self.outcome(test, "FAIL", self._exc_info_to_string(error, test))

    def addError(self, test, error):
        super().addError(test, error)
        self.outcome(test, "FAIL", self._exc_info_to_string(error, test))

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.outcome(test, "BLOCKED", reason)

    def addSubTest(self, test, subtest, error):
        super().addSubTest(test, subtest, error)
        if error is not None:
            self.outcome(test, "FAIL", self._exc_info_to_string(error, subtest))

    def stopTest(self, test):
        record = self.active.pop(test.id())
        record["duration_seconds"] = round(time.monotonic() - record.pop("started"), 4)
        self.records.append(record)
        super().stopTest(test)


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    target = args.output_dir.resolve()
    if target == ROOT or ROOT in target.parents:
        parser.error("Evidence output must be outside bundle to preserve manifest integrity")
    target.mkdir(parents=True, exist_ok=True)
    names = ("TEST_RESULTS.json", "TEST_MATRIX.md", "TEST_RUN.txt")
    if any((target / name).exists() for name in names):
        parser.error("Evidence output exists; choose a fresh directory")
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern="test_*.py")
    log = io.StringIO()
    result = unittest.TextTestRunner(stream=log, verbosity=2, resultclass=EvidenceResult).run(suite)
    records = sorted(result.records, key=lambda record: record["id"])
    summary = {"run_utc": datetime.now(timezone.utc).isoformat(), "platform": platform.platform(),
               "python": sys.version, "command": [sys.executable, *sys.argv], "cwd": str(Path.cwd()),
               "tests_run": result.testsRun, "counts": {status: sum(r["status"] == status for r in records)
                                                         for status in ("PASS", "FAIL", "BLOCKED", "NOT_RUN")},
               "model_behavioral_tests": "A01-A44 NOT_RUN", "tests": records}
    write_text_lf(target / names[0], json.dumps(summary, ensure_ascii=True, indent=2) + "\n")
    write_text_lf(target / names[2], log.getvalue())
    lines = ["# Automated regression matrix — v1.2.1", "", f"Run UTC: {summary['run_utc']}", "",
             "Evidence: [verbose unittest output](TEST_RUN.txt), [machine-readable results](TEST_RESULTS.json).",
             "PASS means assertions in the named automated test passed; P15/P16 are static checks, not model runs.", "",
             "| ID | Preconditions | Input | Expected | Actual | Status |", "|---|---|---|---|---|---|"]
    for record in records:
        lines.append("| " + " | ".join(cell(record[key]) for key in ("id", "preconditions", "input", "expected", "actual", "status")) + " |")
    write_text_lf(target / names[1], "\n".join(lines) + "\n")
    print(json.dumps({key: summary[key] for key in ("tests_run", "counts", "model_behavioral_tests")}, ensure_ascii=True))
    return 0 if result.wasSuccessful() and not result.skipped else 1


if __name__ == "__main__":
    raise SystemExit(main())
