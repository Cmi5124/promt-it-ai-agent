"""Shared offline file, manifest and local-reference policy for v1.2.1."""
from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

VERSION = "1.2.1"
DATE = "2026-10-21"
SKILL_NAME = "adaptive-project-ops"
SKILL_PATH = Path("skills") / SKILL_NAME
REPOSITORY_VERSION = "1.1.0"
FULL_ARCHIVE_PREFIX = "promt-it-ai-agent"


def write_text_lf(path: Path, content: str) -> None:
    """Keep hashed text stable across Windows and Git LF checkout rules."""
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)


def distribution_files(root: Path) -> list[Path]:
    """Exclude Git metadata and existing Python bytecode exceptions only."""
    found = []
    for directory, names, files in os.walk(root, followlinks=False):
        names[:] = sorted(n for n in names if n not in {".git", "__pycache__"})
        for name in names:
            if (Path(directory) / name).is_symlink():
                raise ValueError(f"Symlink directory is not a distribution resource: {name}")
        for name in sorted(files):
            if name == ".git" or name.endswith(".pyc"):
                continue
            path = Path(directory) / name
            if path.is_symlink():
                raise ValueError(f"Symlink file is not a distribution resource: {path.relative_to(root)}")
            found.append(path)
    return sorted(found)


def file_hashes(root: Path) -> dict[str, str]:
    return {p.relative_to(root).as_posix(): sha256(p.read_bytes()).hexdigest()
            for p in distribution_files(root) if p != root / "manifest.json"}


def template_names(skill: Path) -> set[str]:
    names = set()
    for doc in (skill / "references").glob("*.md"):
        names.update(re.findall(r"\.\./assets/templates/([A-Za-z0-9_-]+\.md)", doc.read_text(encoding="utf-8")))
    return names


def template_errors(root: Path) -> list[str]:
    skill = root / SKILL_PATH
    expected = template_names(skill)
    target = skill / "assets" / "templates"
    actual = {p.name for p in target.iterdir() if p.is_file()} if target.is_dir() else set()
    errors = []
    if expected != actual:
        errors.append(f"Template set mismatch: expected={sorted(expected)} actual={sorted(actual)}")
    for name in sorted(expected):
        original, copied = root / "templates" / name, target / name
        if not original.is_file() or not copied.is_file():
            errors.append(f"Missing canonical/copied template: {name}")
        elif original.read_bytes() != copied.read_bytes():
            errors.append(f"Template divergence: {name}")
    return errors


def manifest_errors(root: Path) -> list[str]:
    try:
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        if not isinstance(manifest, dict) or not isinstance(manifest.get("files"), dict):
            return ["Invalid manifest object/files mapping"]
        errors = []
        if manifest.get("version") != VERSION:
            errors.append("Manifest version mismatch")
        actual, tracked = file_hashes(root), manifest["files"]
        if actual != tracked:
            new = sorted(set(actual) - set(tracked))
            missing = sorted(set(tracked) - set(actual))
            changed = sorted(k for k in actual.keys() & tracked.keys() if actual[k] != tracked[k])
            errors.append(f"Manifest integrity mismatch: new={new}; missing={missing}; changed={changed}")
        return errors
    except (OSError, ValueError) as error:
        return [f"Cannot verify manifest: {error}"]


def local_reference_errors(root: Path) -> list[str]:
    """Validate explicit links plus maintained legacy router/resource code spans.

    Fenced examples and external source filenames are not local dependencies.
    Explicit relative links resolve only from their document, never by guessing.
    Legacy references use the documented skill-root/reference-dir conventions.
    """
    root = root.resolve()
    skill = root if (root / "SKILL.md").is_file() else root / SKILL_PATH
    errors = []
    for doc in distribution_files(root):
        if doc.suffix != ".md":
            continue
        text = doc.read_text(encoding="utf-8")
        body = re.sub(r"(?ms)^\s*(```|~~~).*?^\s*\1\s*$", "", text)
        explicit = re.findall(r"\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", body)
        explicit += re.findall(r"(?m)^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", body)
        resources = []
        for target in explicit:
            target = target.strip("<>")
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            resources.append((unquote(parts.path), False))
        for token in re.findall(r"`([^`\n]+)`", body):
            if re.fullmatch(r"\d\d-[a-z0-9-]+\.md", token):
                resources.append((token, True))
            elif re.fullmatch(r"(?:\.\./scripts/|\.\./assets/|references/)[A-Za-z0-9_./-]+\.(?:md|py|json|yaml)", token):
                resources.append((token, True))
        for target, legacy in resources:
            options = [doc.parent / target]
            if legacy:
                options += [skill / target, skill / "references" / target]
            safe = []
            for option in options:
                resolved = option.resolve()
                try:
                    resolved.relative_to(root)
                except ValueError:
                    continue
                safe.append(resolved)
            if not any(p.exists() for p in safe):
                errors.append(f"Broken/out-of-package local reference: {doc.relative_to(root)} -> {target}")
    return errors


def instruction_errors(root: Path) -> list[str]:
    """Static consistency checks; these do not establish model behavior."""
    errors = []
    files = [f"{SKILL_PATH.as_posix()}/SKILL.md", f"{SKILL_PATH.as_posix()}/references/00-task-contract.md",
             "integrations/adaptive/gemma4-system-prompt.md", "integrations/adaptive/chatgpt-custom-instructions.md",
             "integrations/adaptive/codex-AGENTS.example.md"]
    for name in files:
        text = (root / name).read_text(encoding="utf-8")
        for required in ("SHARE_IDEA", "ANALYZE_ONLY", "PLAN_ONLY", "IMPLEMENT",
                         "đọc file, tìm kiếm nội dung, kiểm tra metadata, status, diff và configuration",
                         "Không sửa file, cài dependency", "TEST_ONLY/IMPLEMENT", "không hỏi lại",
                         "không tự sửa roadmap/file", "quyền runtime"):
            if required not in text:
                errors.append(f"Missing instruction contract {required!r} in {name}")
        if "không tạo/sửa file, chạy lệnh hay hành động thay đổi state" in text:
            errors.append(f"Read-only command prohibition conflict: {name}")
    acceptance = (root / "tests/ACCEPTANCE_TESTS.md").read_text(encoding="utf-8")
    rows = re.findall(r"(?m)^\|\s*(A\d\d)\s*\|(.+)$", acceptance)
    if {key for key, _ in rows} != {f"A{i:02}" for i in range(1, 45)} or len(rows) != 44:
        errors.append("Acceptance scenario IDs must remain A01..A44 exactly once")
    for key, row in rows:
        if row.split("|")[-2].strip() != "NOT_RUN":
            errors.append(f"Model evidence unavailable; expected NOT_RUN for {key}")
        if key in {"A04", "A44"} and ("IMPLEMENT" not in row or "scope" not in row):
            errors.append(f"Explicit implementation authorization missing from {key}")
    return errors
