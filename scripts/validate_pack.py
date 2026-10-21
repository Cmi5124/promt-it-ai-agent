#!/usr/bin/env python3
"""Offline structural and integrity checks for Adaptive Agent Skill Pack v1.2.1.
No model execution, security scan, or live testing is implied by these checks.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from pack_utils import (VERSION, distribution_files, instruction_errors,
                        local_reference_errors, manifest_errors, template_errors)

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / 'skills/adaptive-project-ops'
SKILL = SKILL_DIR / 'SKILL.md'
ERRORS: list[str] = []

REQUIRED = {
    'README.md', 'CHANGELOG.md', 'manifest.json',
    '.gitignore', '.gitattributes', 'GITHUB_PUBLISH_GUIDE.md', 'THIRD_PARTY_NOTICES.md',
    'skills/adaptive-project-ops/SKILL.md',
    'skills/adaptive-project-ops/references/04-testing-security-release.md',
    'skills/adaptive-project-ops/references/17-security-engineering.md',
    'skills/adaptive-project-ops/references/18-test-engineering.md',
    'skills/adaptive-project-ops/references/19-security-verification.md',
    'skills/adaptive-project-ops/references/20-open-source-reuse-discovery.md',
    'skills/adaptive-project-ops/scripts/reuse_catalog.py',
    'scripts/reuse_catalog.py',
    'scripts/pack_utils.py', 'scripts/build_release.py',
    'tests/test_maintenance.py', 'tests/test_packaging.py',
    'skills/adaptive-project-ops/manifest.json',
    'tests/test_reuse_catalog.py',
    'templates/OPEN_SOURCE_CANDIDATE_REVIEW.md',
    'docs/adaptive/EXTERNAL_REPO_REVIEW_2026-10-21.md',
    'integrations/adaptive/chatgpt-custom-instructions.md',
    'integrations/adaptive/gemma4-system-prompt.md',
    'integrations/adaptive/codex-AGENTS.example.md',
    'tests/ACCEPTANCE_TESTS.md',
    'docs/adaptive/PROVENANCE.md', 'docs/adaptive/TRACEABILITY_MATRIX.md',
    'docs/adaptive/RESEARCH_IDEA_ATLAS.md',
    'templates/TEST_EVIDENCE_MATRIX.md',
    'templates/TEST_STRATEGY.md', 'templates/TEST_CASES.md',
    'templates/TEST_RUN_REPORT.md', 'templates/REQUIREMENT_TEST_MATRIX.md',
    'templates/DEFECT_REPORT.md',
    'templates/SECURITY_THREAT_MODEL.md', 'templates/SECURITY_TEST_PLAN.md',
    'templates/SECURITY_FINDING.md', 'templates/RELEASE_GATE.md',
}
for name in sorted(REQUIRED):
    if not (ROOT / name).is_file():
        ERRORS.append(f'Missing required file: {name}')

if not SKILL.is_file():
    print('BLOCKED: SKILL.md missing')
    sys.exit(1)
raw = SKILL.read_text(encoding='utf-8')
match = re.match(r'\A---\n(.*?)\n---\n', raw, re.DOTALL)
if not match:
    ERRORS.append('Missing/invalid YAML-like frontmatter')
else:
    head = match.group(1)
    name = re.search(r'^name:\s*(\S+)\s*$', head, re.MULTILINE)
    desc = re.search(r'^description:\s*(.+)$', head, re.MULTILINE)
    if not name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name.group(1)):
        ERRORS.append('Invalid skill name')
    elif name.group(1) != SKILL_DIR.name or len(name.group(1)) > 64:
        ERRORS.append('Skill folder/name mismatch/length')
    if not desc or not 1 <= len(desc.group(1).strip()) <= 1024:
        ERRORS.append('Invalid skill description')
if len(raw.splitlines()) > 500:
    ERRORS.append('SKILL.md exceeds recommended 500 lines')

refs = list((SKILL_DIR / 'references').glob('*.md'))
router = set(re.findall(r'`(?:references/)?(\d\d-[a-z0-9-]+\.md)`', raw))
for ref in sorted(router):
    if not (SKILL_DIR / 'references' / ref).is_file():
        ERRORS.append(f'Broken routed reference: {ref}')
if len(router) != len(refs):
    ERRORS.append(f'Router mismatch: references={len(refs)} routed={len(router)}')
if not {'17-security-engineering.md','18-test-engineering.md','19-security-verification.md','20-open-source-reuse-discovery.md'} <= router:
    ERRORS.append('Security and testing modules not reachable from main router')

for path in distribution_files(ROOT):
    if path.suffix != '.md':
        continue
    try:
        content = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        ERRORS.append(f'Bad UTF-8: {path.relative_to(ROOT)}')
        continue
    if not content.strip():
        ERRORS.append(f'Empty markdown: {path.relative_to(ROOT)}')

ERRORS.extend(local_reference_errors(ROOT))
ERRORS.extend(local_reference_errors(SKILL_DIR))
ERRORS.extend(template_errors(ROOT))
ERRORS.extend(instruction_errors(ROOT))
ERRORS.extend(manifest_errors(SKILL_DIR))

sec = (SKILL_DIR/'references/17-security-engineering.md').read_text(encoding='utf-8')
test = (SKILL_DIR/'references/18-test-engineering.md').read_text(encoding='utf-8')
verify = (SKILL_DIR/'references/19-security-verification.md').read_text(encoding='utf-8')
for idx in range(8):
    if f'S{idx}' not in sec:
        ERRORS.append(f'Missing Security SDLC S{idx}')
    if f'V{idx}' not in verify:
        ERRORS.append(f'Missing Security Verification V{idx}')
for idx in range(9):
    if f'T{idx}' not in test:
        ERRORS.append(f'Missing Test lifecycle T{idx}')
for name in ('NORMAL','BOUNDARY','INVALID','DEPENDENCY','SECURITY'):
    if name not in test:
        ERRORS.append(f'Missing mandatory test category: {name}')
for name in ('PASS','FAIL','BLOCKED','NOT_RUN','NOT_VERIFIED'):
    if name not in test:
        ERRORS.append(f'Missing test evidence status: {name}')
for name in ('authorization','scope','stop','rollback'):
    if name not in verify.lower():
        ERRORS.append(f'Missing active-test gate: {name}')

acceptance = (ROOT/'tests/ACCEPTANCE_TESTS.md').read_text(encoding='utf-8')
for idx in range(1,45):
    if not re.search(rf'\|\s*A{idx:02d}\s*\|', acceptance):
        ERRORS.append(f'Missing behavioral test A{idx:02d}')

manifest_path = ROOT/'manifest.json'
if manifest_path.is_file():
    try:
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        if manifest.get('version') != VERSION:
            ERRORS.append('Manifest version mismatch')
        if manifest.get('reference_count') != len(refs):
            ERRORS.append('Manifest reference count mismatch')
        tracked = manifest.get('files',{})
        actual = {str(x.relative_to(ROOT)).replace('\\','/') : sha256(x.read_bytes()).hexdigest()
                  for x in distribution_files(ROOT) if x != manifest_path}
        if tracked != actual:
            missing = sorted(set(actual) - set(tracked))
            deleted = sorted(set(tracked) - set(actual))
            changed = sorted(k for k in set(actual) & set(tracked) if actual[k] != tracked[k])
            ERRORS.append(f'Manifest integrity mismatch: new={missing}; missing={deleted}; changed={changed}')
    except (ValueError, OSError) as ex:
        ERRORS.append(f'Cannot read manifest: {ex}')

print(f'Routed references: {len(router)}; templates: {len(list((ROOT / "templates").glob("*.md")))}; acceptance cases defined: 44')
if ERRORS:
    for msg in ERRORS:
        print('FAIL:', msg)
    sys.exit(1)
print('PASS: local static, route, template, protocol and SHA-256 manifest checks.')
print('NOT_RUN: ChatGPT/Gemma model behavior, live functional testing, active security scans.')
