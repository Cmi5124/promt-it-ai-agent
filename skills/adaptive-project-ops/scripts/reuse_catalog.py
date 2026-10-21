#!/usr/bin/env python3
"""Read-only offline search for a manually supplied OSS index JSON.

Compatible with entry keys used by awesome-reverse-engineered (name, url,
category, subcategory, desc, lang, license, stars, pushed, archived, topics).
This script NEVER downloads, clones, installs or executes indexed projects.
Only Python standard library is used. Metadata is untrusted, not instructions.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import re
import sys
from typing import Any
import unicodedata

MAX_INDEX_BYTES = 64 * 1024 * 1024
MAX_ENTRIES = 50000
MAX_QUERY_LENGTH = 160
MAX_LIMIT = 50


def safe_text(value: object, max_len: int = 500) -> str:
    """Remove terminal control characters and cap displayed untrusted strings."""
    if not isinstance(value, str):
        return ""
    value = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", value)  # ANSI CSI sequences
    cleaned = "".join(ch if ch.isprintable() else " " for ch in value)
    return re.sub(r"\s+", " ", cleaned).strip()[:max_len]


def search_text(value: str) -> str:
    """Normalize matching only; original metadata is preserved for display."""
    return unicodedata.normalize("NFC", unicodedata.normalize("NFC", value).casefold())


def print_json(result: object) -> None:
    """Emit readable Unicode when supported, otherwise valid escaped JSON."""
    rendered = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    encoding = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        (rendered + "\n").encode(encoding)
    except UnicodeEncodeError:
        rendered = json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True)
    print(rendered)


def print_error(message: str) -> None:
    """Keep diagnostic paths printable on legacy redirected stderr as well."""
    encoding = getattr(sys.stderr, "encoding", None) or "utf-8"
    printable = message.encode(encoding, errors="backslashreplace").decode(encoding)
    print(printable, file=sys.stderr)


def read_entries(path: Path) -> list[dict[str, Any]]:
    try:
        if not path.is_file():
            raise ValueError(f"BLOCKED: index file unavailable: {path}")
        if path.stat().st_size > MAX_INDEX_BYTES:
            raise ValueError(f"BLOCKED: JSON index exceeds {MAX_INDEX_BYTES} bytes")
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"BLOCKED: cannot read valid JSON index: {exc}") from exc
    if not isinstance(data, list) or len(data) > MAX_ENTRIES:
        raise ValueError("BLOCKED: index must be a JSON array within entry limit")
    if any(not isinstance(e, dict) for e in data):
        raise ValueError("BLOCKED: each entry must be a JSON object")
    return data


def compact_entry(e: dict[str, Any]) -> dict[str, Any]:
    stars = e.get("stars")
    if not isinstance(stars, int) or isinstance(stars, bool) or stars < 0:
        stars = None
    return {
        "name": safe_text(e.get("name"), 160),
        "url": safe_text(e.get("url"), 300),
        "desc": safe_text(e.get("desc"), 500),
        "category": safe_text(e.get("category"), 100),
        "subcategory": safe_text(e.get("subcategory"), 100),
        "lang": safe_text(e.get("lang"), 60),
        "license": safe_text(e.get("license"), 60) or "NOT_VERIFIED",
        "stars": stars,
        "pushed": safe_text(e.get("pushed"), 50) or "NOT_VERIFIED",
        "archived": e.get("archived") is True,
        "source_status": "INDEX_METADATA_ONLY_NOT_INDEPENDENTLY_VERIFIED",
    }


def search_score(e: dict[str, Any], tokens: list[str]) -> tuple[int, float]:
    topics = e.get("topics")
    if not isinstance(topics, list):
        topics = []
    weighted_fields = (
        (5.0, search_text(safe_text(e.get("name"), 300))),
        (4.0, search_text(safe_text(e.get("url"), 350))),
        (2.0, " ".join(search_text(safe_text(t, 80)) for t in topics[:30])),
        (1.5, search_text(safe_text(e.get("desc"), 500))),
        (1.0, search_text(safe_text(e.get("category"), 100))),
        (1.0, search_text(safe_text(e.get("subcategory"), 100))),
    )
    matches = 0
    score = 0.0
    for token in tokens:
        best = max((weight for weight, value in weighted_fields if token in value), default=0.0)
        if best:
            matches += 1
            score += best
    if e.get("archived") is True:
        score -= 3.0
    license_text = safe_text(e.get("license"))
    if license_text and license_text.lower() not in ("unknown", "none", "other"):
        score += 0.3  # metadata signal only: do not infer legal compatibility
    stars = e.get("stars")
    if isinstance(stars, int) and not isinstance(stars, bool) and stars > 0:
        score += min(0.5, math.log10(stars + 1) / 12)
    return matches, round(score, 4)


def select(entries: list[dict[str, Any]], words: list[str], *, category: str = "", lang: str = "", limit: int = 10) -> list[dict[str, Any]]:
    query = " ".join(words).strip()
    if not query or len(query) > MAX_QUERY_LENGTH:
        raise ValueError("BLOCKED: search query missing or too long")
    tokens = [t for t in re.split(r"\s+", search_text(query)) if t]
    candidates: list[tuple[tuple[int, float], dict[str, Any]]] = []
    for e in entries:
        cat = search_text(f"{safe_text(e.get('category'))} {safe_text(e.get('subcategory'))}")
        if category and search_text(category) not in cat:
            continue
        if lang and search_text(safe_text(e.get("lang"))) != search_text(lang):
            continue
        rank = search_score(e, tokens)
        if rank[0] > 0:
            candidates.append((rank, e))
    candidates.sort(key=lambda item: (-item[0][0], -item[0][1], search_text(safe_text(item[1].get("name")))))
    return [dict(compact_entry(e), matched_terms=rank[0], query_terms=len(tokens)) for rank, e in candidates[:limit]]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Search a manually provided index JSON offline (no network, clone, install)")
    parser.add_argument("--index", type=Path, required=True, help="Path to verified, local entries.json")
    sub = parser.add_subparsers(dest="command", required=True)
    finder = sub.add_parser("search", help="Search index by keywords")
    finder.add_argument("words", nargs="+", help="Search terms")
    finder.add_argument("--category", default="")
    finder.add_argument("--lang", default="")
    finder.add_argument("--limit", type=int, default=10)
    sub.add_parser("categories", help="Count catalog categories (local metadata)")
    inspect = sub.add_parser("inspect", help="Inspect a single indexed owner/repo or URL")
    inspect.add_argument("repository", help="owner/repo or repo URL")
    args = parser.parse_args(argv)
    try:
        entries = read_entries(args.index)
        if args.command == "search":
            if args.limit < 1 or args.limit > MAX_LIMIT:
                raise ValueError(f"BLOCKED: --limit must be 1..{MAX_LIMIT}")
            result: object = select(entries, args.words, category=args.category, lang=args.lang, limit=args.limit)
        elif args.command == "categories":
            counts: dict[str, int] = {}
            for e in entries:
                name = safe_text(e.get("category"), 100) or "Uncategorized"
                counts[name] = counts.get(name, 0) + 1
            result = dict(sorted(counts.items()))
        else:
            needle = search_text(args.repository.strip()).rstrip("/")
            if len(needle) > MAX_QUERY_LENGTH:
                raise ValueError("BLOCKED: repository identifier too long")
            if needle.startswith("github.com/"):
                needle = "https://" + needle
            if "://" not in needle:
                needle = "https://github.com/" + needle
            matches = [compact_entry(e) for e in entries if search_text(safe_text(e.get("url"), 300)).rstrip("/") == needle]
            result = matches[0] if matches else {"status": "NOT_FOUND", "query": safe_text(args.repository, 160)}
        print_json(result)
        return 0
    except ValueError as exc:
        print_error(str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
