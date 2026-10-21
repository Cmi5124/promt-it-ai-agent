"""Repository preservation, approved contract and public-tree checks (offline)."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re

from pack_utils import distribution_files

CONTRACT_FILES = (
    'PROMT-IT-AI-AGENT.md', 'PROMT-IT-AI-AGENT-COMPACT.md',
    'skills/adaptive-project-ops/SKILL.md', 'skills/adaptive-project-ops/references/00-task-contract.md',
    'integrations/adaptive/chatgpt-custom-instructions.md',
    'integrations/adaptive/codex-AGENTS.example.md', 'integrations/adaptive/gemma4-system-prompt.md',
    'templates/TEST-ONLY.md',
)
APPROVED_EXISTING_CHANGES = {'README.md','CHANGELOG.md','PROMT-IT-AI-AGENT.md',
                            'PROMT-IT-AI-AGENT-COMPACT.md','integrations/CODEX-USAGE.md','templates/TEST-ONLY.md'}


def preservation_errors(root: Path) -> list[str]:
    errors=[]
    audit=json.loads((root/'docs/integration/BASELINE.json').read_text(encoding='utf-8'))
    for item in audit['baseline_files']:
        if item['path'] in APPROVED_EXISTING_CHANGES:
            continue
        path=root/item['path']
        if not path.is_file() or sha256(path.read_bytes()).hexdigest()!=item['sha256']:
            errors.append(f"Baseline preservation failure: {item['path']}")
    for item in json.loads((root/'docs/integration/IMPORTED_FILES.json').read_text(encoding='utf-8')):
        path=root/item['path']
        if not path.is_file() or sha256(path.read_bytes()).hexdigest()!=item['sha256']:
            errors.append(f"Imported functional content drift: {item['path']}")
    original=root/'versions/v1.0.0.md'
    if original.read_bytes()!=(root/'versions/PROMT-IT-AI-AGENT.md').read_bytes():
        errors.append('Frozen full alias differs from v1.0.0')
    compact=next(x for x in audit['baseline_files'] if x['path']=='PROMT-IT-AI-AGENT-COMPACT.md')
    if sha256((root/'versions/v1.0.0-compact.md').read_bytes()).hexdigest()!=compact['sha256']:
        errors.append('Archived compact differs from v1.0.0')
    return errors


def contract_errors(root: Path) -> list[str]:
    text=(root/'docs/INSTRUCTION_CONTRACT.md').read_text(encoding='utf-8')
    policy=next(line for line in text.splitlines() if line.startswith('TEST_ONLY được tạo fixture'))
    errors=[]
    for name in CONTRACT_FILES:
        content=(root/name).read_text(encoding='utf-8')
        if policy not in content:
            errors.append(f'Synchronized TEST_ONLY/IMPLEMENT contract missing: {name}')
        if 'Không sửa code hay tạo thay đổi.' in content:
            errors.append(f'Obsolete absolute artifact prohibition: {name}')
    usage=(root/'integrations/CODEX-USAGE.md').read_text(encoding='utf-8')
    if 'Chỉ yêu cầu implementation sau khi plan/scope được phê duyệt.' in usage:
        errors.append('Obsolete repeat-approval contract in CODEX-USAGE')
    if 'không yêu cầu duyệt lại cùng phạm vi' not in usage:
        errors.append('Current Owner approval clarification missing')
    if not all(token in text for token in ('runtime','Owner','repository contracts','core Agent Skill','domain references','optional examples')):
        errors.append('Instruction precedence incomplete')
    return errors


def publication_errors(root: Path) -> list[str]:
    """Heuristic static checks, not a certification that no secret exists."""
    errors=[]
    patterns={
        'personal Windows home path': r'[A-Za-z]:[\\/]Users[\\/]',
        'OpenAI-like credential': r'\bsk-[A-Za-z0-9_-]{24,}',
        'GitHub-like credential': r'\bgh[pousr]_[A-Za-z0-9]{24,}',
        'AWS-like credential': r'\bAKIA[A-Z0-9]{16}\b',
        'private key block': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
        'private historical provenance': r'(?m)^## (?:OWNER-CONFIRMED IN CONTEXT|.*HISTORICAL SYNTHESIS)',
    }
    for path in distribution_files(root):
        rel=path.relative_to(root).as_posix()
        if path.suffix.lower() in {'.zip','.key','.pem'} or path.name=='.env':
            errors.append(f'Non-source/sensitive file in public tree: {rel}')
            continue
        content=path.read_text(encoding='utf-8')
        for label,pattern in patterns.items():
            if re.search(pattern,content):
                errors.append(f'Publication review flag ({label}): {rel}')
    return errors


def repository_errors(root: Path) -> list[str]:
    return preservation_errors(root)+contract_errors(root)+publication_errors(root)
