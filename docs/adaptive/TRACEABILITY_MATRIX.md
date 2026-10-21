# Traceability — public engineering guidance

Các dòng sau là phương pháp nhập từ skill v1.2.1; không chứa lịch sử hội thoại, không là bằng chứng model đã tuân thủ. Chúng không tự cấp quyền task.

| ID | Normalized requirement | Primary skill section | Evidence class |
|---|---|---|---|
| GOV-01 | Default analysis-only unless explicit action authorization | 00-task-contract | IMPORTED_GUIDANCE/SOURCE_REPO |
| GOV-02 | Owner controls major changes; file permission separate from Git/production | 00-task-contract, 09-project-governance | IMPORTED_GUIDANCE |
| GOV-03 | No silent scope expansion, refactor or architecture/framework migration | 02-repository-engineering | IMPORTED_GUIDANCE/SOURCE_REPO |
| GOV-04 | Material missing information → ask; minor uncertainty → explicit assumption | 00-task-contract | IMPORTED_GUIDANCE |
| GOV-05 | Preserve current approved decisions over speculative new ideas | 09-project-governance | IMPORTED_GUIDANCE |
| GOV-06 | SSOT, append-only history, immutable version snapshots, forward corrections | 09-project-governance | IMPORTED_GUIDANCE |
| GOV-07 | Charter, SMART, scope, SOW, WBS/100% Rule, SRS traceability | 01-requirements-architecture, 09-project-governance | IMPORTED_GUIDANCE |
| GOV-08 | Definition of Ready/Done; pass gates by evidence not calendar | 09-project-governance | IMPORTED_GUIDANCE |
| GOV-09 | Distinguish version, sprint S, research/experiment R | 09-project-governance, 06-data-experiments | IMPORTED_GUIDANCE |
| GOV-10 | Portfolio registry, WIP discipline, gated selection of next activity | 09-project-governance | IMPORTED_GUIDANCE |
| REQ-01 | Elicit business flow, alternative/errors, NFR, outputs and acceptance | 01-requirements-architecture | SOURCE_REPO/IMPORTED_GUIDANCE |
| REQ-02 | Future-proof at extension boundary, not speculative feature bloat | 01-requirements-architecture | IMPORTED_GUIDANCE |
| REQ-03 | Protect modular core from UI/provider infra, enable optional adapters | 01-requirements-architecture | IMPORTED_GUIDANCE |
| CODE-01 | Read actual repo: callers/callees, configs, dependency, tests, contracts | 02-repository-engineering | IMPORTED_GUIDANCE/SOURCE_REPO |
| CODE-02 | Do not invent API, code, run output or test evidence | 02-repository-engineering, 16-evidence-source-protocol | IMPORTED_GUIDANCE |
| CODE-03 | Complete integration-ready implementation, minimal diff, no placeholders | 02-repository-engineering | IMPORTED_GUIDANCE |
| CODE-04 | Diagnose persistent failures (>3) with root cause; no endless blind fixes | 03-debugging-root-cause | IMPORTED_GUIDANCE |
| TEST-01 | Normal/boundary/invalid/dependency/security groups, expected/actual/status | 18-test-engineering, 04-testing-security-release | IMPORTED_GUIDANCE/SOURCE_REPO |
| TEST-02 | No PASS without executed tests and evidence; release gate integrity | 18-test-engineering, 04-testing-security-release | IMPORTED_GUIDANCE |
| TEST-03 | Security boundaries: auth, prompt injection, data leakage, rollback | 17-security-engineering, 19-security-verification | IMPORTED_GUIDANCE/SOURCE_REPO |
| TEST-04 | Security testing only authorized isolated assets; minimize blast radius | 19-security-verification | IMPORTED_GUIDANCE |
| RES-01 | Verify links/papers/news/repos; distinguish original claim vs interpretation | 07-tech-research-watch | IMPORTED_GUIDANCE |
| RES-02 | Candidate adoption through gap/benchmark/risk/backlog, not FOMO | 07-tech-research-watch | IMPORTED_GUIDANCE |
| RES-03 | Controlled variables, reproducible experiments, append-only failure logs | 06-data-experiments | IMPORTED_GUIDANCE |
| RES-04 | Split/no leakage, OOF/per-class error, avoid public leaderboard overfit | 06-data-experiments | IMPORTED_GUIDANCE |
| AI-01 | Model-only vs tool-assisted vs full-agent metrics separate | 05-ai-llm-agent-systems | SOURCE_REPO/IMPORTED_GUIDANCE |
| AI-02 | RAG retrieval relevance ≠ sufficient evidence/answerability | 05-ai-llm-agent-systems | IMPORTED_GUIDANCE |
| AI-03 | Permission/provenance/context budget/recoverable memory lifecycle | 08-context-memory-skills | IMPORTED_GUIDANCE |
| AI-04 | Modular, provider-neutral agent/tool interface; owner retains autonomy | 14-agent-orchestration | IMPORTED_GUIDANCE |
| AI-05 | Benchmarked efficiency = verified success per token/tool/rework | 05-ai-llm-agent-systems, 14-agent-orchestration | IMPORTED_GUIDANCE |
| AI-06 | Conditional local-first/self-hosting/no external API per scoped product | 14-agent-orchestration | IMPORTED_GUIDANCE/IMPORTED_GUIDANCE |
| AI-07 | Image-coded context/data is research hypothesis; verify round-trip/fidelity | 12-multimodal-encoding, 08-context-memory-skills | IMPORTED_GUIDANCE |
| HW-01 | Model/GPU feasibility needs weights+KV+runtime+topology not just VRAM sum | 11-hardware-runtime | IMPORTED_GUIDANCE |
| HW-02 | Inference evaluation quality/performance/resource/cost hardware facts | 11-hardware-runtime | IMPORTED_GUIDANCE |
| DOC-01 | Report rubric and actual source first, no fabricated citation/experiment | 10-academic-reports | IMPORTED_GUIDANCE/SOURCE_REPO |
| DOC-02 | Generate DOCX only when asked; editable Word components | 10-academic-reports | IMPORTED_GUIDANCE/SOURCE_REPO |
| DOC-03 | A4, TNR13 and format defaults conditionally academic/rubric | 10-academic-reports | SOURCE_REPO |
| SEC-01 | Evidence-driven security hunter/verifier and independent validation | 13-reverse-engineering, 17-security-engineering, 19-security-verification | IMPORTED_GUIDANCE |
| SEC-02 | Reverse engineering: legal/authorized scope, untrusted binary/tool | 13-reverse-engineering | IMPORTED_GUIDANCE |
| AGT-01 | Agent roles/planner/coder/verifier; staged approval for risky action | 14-agent-orchestration | IMPORTED_GUIDANCE |
| AGT-02 | Model can propose tool calls, runtime must enforce execution boundaries | 14-agent-orchestration | SOURCE_REPO/IMPORTED_GUIDANCE |
| OUT-01 | Direct Vietnamese, technically precise, proportionate depth | SKILL.md and 00-task-contract | IMPORTED_GUIDANCE |
| OUT-02 | Explicit evidence status, what changed/not run, blocker and owner decisions | 16-evidence-source-protocol | IMPORTED_GUIDANCE |
| ID | Normalized requirement | Primary reference / template | Evidence class |
|---|---|---|---|
| SEC-03 | Secure SDLC S0–S7 và threat modeling có DFD/trust boundaries/threat ledger | 17-security-engineering / SECURITY_THREAT_MODEL | IMPORTED_GUIDANCE + SOURCE_REPO + STANDARD_REFERENCE |
| SEC-04 | Kiểm soát identity, authorization, tenant isolation, data/privacy, supply chain, AI/Agent tools | 17-security-engineering | SOURCE_REPO + STANDARD_REFERENCE |
| SEC-05 | Rules of Engagement cho active testing: scope, authorization, test limits, stop/rollback | 19-security-verification / SECURITY_TEST_PLAN | IMPORTED_GUIDANCE + IMPORTED_GUIDANCE |
| SEC-06 | Security verification V0–V7 gồm static/dynamic/API/auth/adversarial, finding & retest | 19-security-verification / SECURITY_FINDING | IMPORTED_GUIDANCE + STANDARD_REFERENCE |
| TEST-05 | Test lifecycle T0–T8: requirements, strategy, design, data/env, execute, defect, regression, closure | 18-test-engineering / TEST_STRATEGY | IMPORTED_GUIDANCE + SOURCE_REPO |
| TEST-06 | RTM nối REQ/THREAT → TEST → RUN → EVIDENCE → DEFECT → RETEST → GATE | 18-test-engineering / REQUIREMENT_TEST_MATRIX | IMPORTED_GUIDANCE + SOURCE_REPO |
| TEST-07 | Phân biệt planning coverage với executed coverage; RUN actual và test result proof | 18-test-engineering / TEST_RUN_REPORT | SOURCE_REPO |
| TEST-08 | Retest bug khác regression; defect severity khác priority; flakiness không retry-until-green | 18-test-engineering / DEFECT_REPORT | ENGINEERING_BEST_PRACTICE |
| REL-01 | Independent release gates và residual risk signoff riêng với permission deploy | 04-testing-security-release / RELEASE_GATE | SOURCE_REPO |
| ID | Normalized requirement | Evidence class | Module |
|---|---|---|---|
| REUSE-01 | Search-before-build; nội bộ/standard/official trước RE alternatives | IMPORTED_GUIDANCE + THIRD_PARTY_REVIEW | 20-open-source-reuse-discovery |
| REUSE-02 | Shortlist, license, maintenance, provenance, security, supply-chain và architecture fit | THIRD_PARTY_REVIEW + ENGINEERING_PRACTICE | 20-open-source-reuse-discovery / OPEN_SOURCE_CANDIDATE_REVIEW |
| REUSE-03 | Optional offline index, no auto-network/clone/install/secret handling | IMPORTED_GUIDANCE + SECURITY_BOUNDARY | scripts/reuse_catalog.py |
| REUSE-04 | Selection phải có test, owner approval, traceable evidence | IMPORTED_GUIDANCE | 17/18/19 + 20 |
| PACK-01 | Download toàn bộ bundle với adapters/templates/tests, repo-ready, không auto-push | IMPORTED_GUIDANCE | README / GITHUB_PUBLISH_GUIDE |
