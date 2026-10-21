# Review note — awesome-reverse-engineered (2026-10-21)

## Evidence read directly (VERIFIED: document content, not individual entries)

- Repository: https://github.com/alexgaoth/awesome-reverse-engineered ; README blob SHA `4488f8945b3bab3c350d29d4666025ed76c0bc8f`.
- README declares approximately **12,869 entries**, **20 categories**, and a "search first, evaluate, reuse" method. Counts are source-reported, dynamic, not independently audited here.
- Upstream Agent Skill: `plugin/skills/find-reverse-engineered/SKILL.md` blob SHA `996c1879fbcaa5ce988c788693ca7a94114b2bb9`. It recommends project fit, maintenance, language, license, and reading README before installing.
- Upstream script `re_index.py` blob SHA `e6250c15dfadffc3471a1c69aea0df8d6618786b` has optional network fetching and git clone actions. We **did not vendor/copy this code**, and the local tool is independently written for local read-only JSON parsing.
- License `LICENSE` MIT blob SHA `c5d0fd892acd6717eeae26eb09db2fcf62490e89`; `LICENSE-DATA` CC0 blob SHA `0e259d42c996742e9e3cba14c677129b2c1b6311`. Each listed project has its own license; source list/license does not apply to their code.
- Relevant category samples: `categories/re-tooling.md`, `categories/network-wire-protocols.md`, `categories/file-formats.md` read as pointers only; they do not guarantee safety/license of any candidate.

## What was adopted, with modifications

1. Search-before-build as an explicit decision gate, including pre-existing internal code, standard libraries and official SDK first.
2. Candidate selection using fit/activity/language/license supplemented by threat model, dependency health, maintenance, auth/secret exposure, interoperability and local-first requirements.
3. Query outside model context: local read-only JSON CLI; index **not** included in bundle, user provides it explicitly.
4. Routing across tools/protocols/formats/hardware/AI clients, but only on tasks that match.
5. Evidence log + test gate + Owner approval before adoption; legal and supply-chain unknowns produce BLOCKED or RESEARCH_MORE.

## Deliberately not adopted

- Automatic `npx skills add`, `curl | python3`, clone, install, binary execution, fetching the full dataset as a runtime side effect.
- Hardcoded star/health ratings and an assumption that listed code is necessarily safe or licensed for this intended use.
- Password handling, account scraping, DRM/paywall bypass, security-control bypass or unauthorized testing.

## Limitations

- The dataset was not locally downloaded or independently verified entry-by-entry; CLI tests use **synthetic fixture** entries and so do not validate claims about real upstream repos.
- No third-party binary/plugin executed; no live Gemma 4 runtime test.
- Legal/ToS applicability is case/jurisdiction-specific, not established by listing in the index.
