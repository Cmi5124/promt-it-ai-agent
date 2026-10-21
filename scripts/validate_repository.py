#!/usr/bin/env python3
"""Validate integrated source without writing, staging or publishing artifacts."""
from pathlib import Path
import subprocess
import sys

from repository_checks import repository_errors

ROOT=Path(__file__).resolve().parents[1]


def main():
    try:
        checked=subprocess.run([sys.executable,str(ROOT/'scripts/validate_pack.py')],cwd=ROOT,check=False,timeout=60)
        if checked.returncode:
            return checked.returncode
        errors=repository_errors(ROOT)
        if errors:
            for error in errors: print('FAIL:',error)
            return 1
        print('PASS: repository preservation, synchronized contract and static publication review.')
        print('NOT_RUN: model behavior and actual GitHub Actions. Static secret review is heuristic.')
        return 0
    except (OSError,ValueError,subprocess.TimeoutExpired) as error:
        print(f'BLOCKED: {error}',file=sys.stderr)
        return 2


if __name__=='__main__':
    raise SystemExit(main())
