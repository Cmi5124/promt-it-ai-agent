#!/usr/bin/env python3
"""Bundle-root CLI entry point for the self-contained agent skill catalogue reader."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parents[1] / "skills" / "adaptive-project-ops" / "scripts" / "reuse_catalog.py"), run_name="__main__")
