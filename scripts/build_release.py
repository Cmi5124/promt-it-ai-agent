#!/usr/bin/env python3
"""Prepare templates/manifests or build two validated offline release archives."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from pack_utils import SKILL_PATH, REPOSITORY_VERSION, FULL_ARCHIVE_PREFIX, DATE, SKILL_NAME, VERSION, distribution_files, file_hashes, template_names, write_text_lf

ROOT = Path(__file__).resolve().parents[1]


def prepare() -> None:
    skill = ROOT / SKILL_PATH
    destination = skill / "assets" / "templates"
    destination.resolve().relative_to(ROOT)
    destination.mkdir(parents=True, exist_ok=True)
    for name in sorted(template_names(skill)):
        source = ROOT / "templates" / name
        source.resolve().relative_to(ROOT)
        if source.is_symlink():
            raise ValueError(f"Refusing symlink canonical template: {name}")
        if not source.is_file():
            raise ValueError(f"Missing canonical template: {name}")
        if (destination / name).is_symlink():
            raise ValueError(f"Refusing symlink template destination: {name}")
        shutil.copyfile(source, destination / name)
    skill_manifest = {"name": SKILL_NAME, "version": VERSION, "date": DATE,
                      "reference_count": len(list((skill / "references").glob("*.md"))),
                      "template_count": len(template_names(skill)), "files": file_hashes(skill)}
    write_text_lf(skill / "manifest.json", json.dumps(skill_manifest, indent=2, ensure_ascii=True) + "\n")
    path = ROOT / "manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest.update(version=VERSION, repository_version=REPOSITORY_VERSION, prompt_version=REPOSITORY_VERSION, skill_version=VERSION, release_state="candidate", date=DATE, behavioral_tests_run=0,
                    reference_count=skill_manifest["reference_count"],
                    standalone_template_count=skill_manifest["template_count"])
    manifest["files"] = file_hashes(ROOT)
    write_text_lf(path, json.dumps(manifest, indent=2, ensure_ascii=True) + "\n")


def archive(root: Path, destination: Path, prefix: str) -> None:
    with ZipFile(destination, "x", compression=ZIP_DEFLATED) as output:
        for path in distribution_files(root):
            info = ZipInfo(f"{prefix}/{path.relative_to(root).as_posix()}", (2026, 10, 21, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            output.writestr(info, path.read_bytes())
    with ZipFile(destination) as output:
        if output.testzip() is not None:
            raise ValueError(f"Archive CRC failure: {destination.name}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--prepare", action="store_true", help="Sync canonical templates and regenerate manifests; does not run tests")
    action.add_argument("--output-dir", type=Path, help="Create archives and checksums in a directory outside the bundle")
    args = parser.parse_args(argv)
    try:
        if args.prepare:
            prepare()
            print("Prepared templates and both SHA-256 manifests; tests not implied.")
            return 0
        target = args.output_dir.resolve()
        if target == ROOT or ROOT in target.parents:
            raise ValueError("Output directory must be outside the bundle")
        names = [f"Promt_IT_AI_Agent_v{REPOSITORY_VERSION}_Integration_Candidate.zip", f"adaptive-project-ops_skill_v{VERSION}.zip"]
        for name in names + ["SHA256SUMS.txt"]:
            if (target / name).exists():
                raise ValueError(f"Output already exists: {name}")
        checked = subprocess.run([sys.executable, str(ROOT / "scripts/validate_repository.py")], cwd=ROOT, check=False, timeout=60)
        if checked.returncode:
            return checked.returncode
        target.mkdir(parents=True, exist_ok=True)
        archive(ROOT, target / names[0], FULL_ARCHIVE_PREFIX)
        archive(ROOT / SKILL_PATH, target / names[1], SKILL_NAME)
        sums = "".join(f"{sha256((target / name).read_bytes()).hexdigest()}  {name}\n" for name in names)
        write_text_lf(target / "SHA256SUMS.txt", sums)
        print(sums, end="")
        return 0
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
