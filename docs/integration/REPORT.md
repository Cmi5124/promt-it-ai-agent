# Repository Integration Report — 1.1.0 candidate / skill 1.2.1

## Executive summary

Tích hợp local, Git permissions NONE. Source gate đạt **60/60 automated tests PASS**, gồm 48 test nhập từ v1.2.1 và 12 integration tests mới. Không dùng kết quả 48/48 cũ làm bằng chứng của integration. Trạng thái source: **READY_WITH_RISKS**, chưa publish. Model A01–A44, native Ubuntu và actual GitHub Actions vẫn NOT_RUN.

## Baseline / audit

GitHub main đã được kiểm tra lại ở commit 58af404bec934cd4a3849102a0a533e9086b57d0; default branch main, baseline repository/prompt 1.0.0, LICENSE Apache-2.0. Bản local tương ứng HEAD main sạch khi audit; working-tree CRLF khác blob LF nhưng không có user changes. Snapshot mới được tạo từ 14 Git blob đã kiểm chứng, không sửa checkout cũ và không clone/create branch/worktree. Candidate là source snapshot không có .git; không được mô tả là một branch mới.

Hai input ZIP SHA-256 và CRC được kiểm tra; full input manifest và sự đồng nhất của skill trong hai ZIP đạt. Xem [baseline/input audit](BASELINE.json). Input artifacts v1.2.1 giữ nguyên. Không có Git publication/commit/PR/merge/tag/release hay history mutation trong task này; git init chỉ nằm trong test fixtures tạm được suite dùng.

## Integration decisions / conflict resolution

[Conflict matrix](../CONFLICT_MATRIX.md) so sánh operating modes, evidence, security, testing, project management, AI/Agent, routing, Git và release gates. Hai conflict thực sự đã được Owner quyết định trước sửa: TEST_ONLY artifact boundaries và không lặp approval IMPLEMENT đã cấp. Đồng bộ một contract trong full/compact prompt, SKILL.md, task contract, ba adapters và TEST_ONLY template. Artifact chỉ trong path/scope cấp phép, có lifecycle, không overwrite source/prod/user data và không tự đưa vào Git. Snapshot versions là lịch sử, không phải contract hiện hành.

Không xóa rule cũ ngầm; root prompt hiện hành tăng metadata sang 1.1.0 candidate và chỉ sửa row TEST_ONLY cùng block precedence/contract cần thiết. Bản full 1.0.0 và compact được archive nguyên byte; frozen full alias phục vụ relative link của compact archive. Existing LICENSE và tám file baseline ngoài phần được Owner duyệt giữ nguyên; sáu file baseline đổi là README, CHANGELOG, full, compact, CODEX-USAGE và TEST-ONLY. Không đổi router hay nội dung Security/Testing references 17–19.

## Structure, canonical source and version matrix

Canonical skill: skills/adaptive-project-ops, đầy đủ references/assets/scripts/manifest/LICENSE/notices, không cần symlink hay repo root khi copy. Root templates có một nguồn authoring; mười bản copy trong skill được builder sync và validator so byte để tránh divergence. Root scripts/tests chỉ đổi các path cần thiết từ layout pack sang skills/ và integrations/adaptive/. [Compatibility matrix](../COMPATIBILITY.md) tách repository/core candidate 1.1.0, upstream baseline/snapshots 1.0.0 và skill 1.2.1. Không tạo tag/release.

[Installation](../INSTALLATION.md) phân biệt editable source, Codex discovery .agents/skills, copy thủ công và runtime file loader. [Usage](../../integrations/ADAPTIVE-USAGE.md) hỗ trợ ChatGPT/Codex/Gemma mà không giả định filesystem/network/shell/tool capability hoặc bắt buộc external inference API. Skill không bị ép nạp cho task không liên quan.

## Tests, actual evidence and limits

Source run UTC 2026-10-21T09:41:33.454218+00:00: **60 PASS, 0 FAIL, 0 BLOCKED, 0 NOT_RUN**. Mỗi record có ID, preconditions/input, expected, actual, evidence và status trong [matrix](TEST_MATRIX.md), [JSON](TEST_RESULTS.json), [raw test log](TEST_RUN.txt). Absolute host paths được redacted trong bản public JSON; kết quả/status không bị thay đổi. Raw original evidence giữ ngoài source publish.

Năm nhóm normal/boundary/invalid/environment/security được bao phủ. P02 thực thi git init trong fixture, P03 synthetic worktree file, U06/U07 strict cp1252/UTF-8, P14 isolated skill copy, P18 archive/manifest/CRC, I07 build hai lần hash bằng nhau, I01/I11 snapshot/import preservation, I02/I03/I10 contract/no-overwrite, I05/I06/I12 publication failure paths. PermissionError là mock, không phải ACL test thật. [Security scenario mapping](../SECURITY_AND_TESTING.md) chỉ rõ model cases NOT_RUN và static evidence riêng.

Các command đã chạy từ root candidate: python scripts/build_release.py --prepare; python scripts/validate_repository.py; python -m compileall -q scripts skills/adaptive-project-ops/scripts tests; python scripts/run_regressions.py --output-dir ../evidence-integration-final. Suite 60/60 đã chạy sau port và chạy lại sau clarification cuối. Không có test bị bỏ/hạ chuẩn.

No project-specific lint/type-check configuration existed. Đã compile Python và review logic/type/dependency/security/timeout tĩnh; không tuyên bố đã chạy linter/type checker. Final artifact extraction tests và checksum nằm trong report bàn giao ngoài ZIP để tránh self-referential hashes.

## Security / public-source / license assessment

Không phát hiện secret, raw private research/history hoặc đường dẫn home cá nhân trong public source sau heuristic scan và manual review. Không claim secret-free certification. Private provenance/history và machine logs từ pack input không được copy vào source; phương pháp tổng quát được giữ trong docs/adaptive. Root scanner không in nội dung credential; synthetic tests không dùng secret thật. Không vendor third-party code/dataset/binary.

Owner đã phê duyệt Apache-2.0 cho phần owned imported content. LICENSE upstream không sửa, standalone có LICENSE riêng. MIT code / CC0 data của awesome-reverse-engineered được đọc từ primary repository và chỉ attribution qua links; không áp Apache-2.0 lên chúng hoặc lên các standard/docs ngoài. Xem [third-party notices](../../THIRD_PARTY_NOTICES.md), [public provenance](../adaptive/PROVENANCE.md). Đây là evidence audit, không phải legal opinion cho mọi jurisdiction.

## CI implementation

[CI report](../CI.md): local workflow Windows/Ubuntu, contents: read, zero external actions, no user secret/write/deploy/release, dùng native Git/Python/PowerShell. YAML đã parse bằng PyYAML sẵn có; hai run blocks đã parse bằng PowerShell AST, không thực thi checkout/publication. Không cài dependency. Actual Actions: NOT_RUN; native Ubuntu: NOT_RUN. Không đánh đồng syntax/static pass với CI pass.

## Publication checklist and rollback

- [x] Scope/diff reviewed; baseline immutable snapshots and LICENSE preserved.
- [x] Canonical skill, controls/lifecycles, strict manifests, UTF-8/cp1252 and standalone regressions pass in source run.
- [x] Public-sensitive review and Owner license decision documented; no source ZIP/log/private history accidentally staged.
- [x] Version/installation/runtime instructions and instruction precedence synchronized.
- [x] Reproducible builds verified locally; no network/install/inference dependency added.
- [ ] Actual GitHub Actions Windows/Ubuntu runs — NOT_RUN until separately authorized publication.
- [ ] Model behavioral A01–A44 — NOT_RUN.
- [ ] Owner publication approval in a separate task; current Git NONE.

Rollback trước publish: tiếp tục dùng upstream baseline; source candidate nằm riêng và checkout cũ không bị thay đổi. Không cần reset/clean/rebase hoặc data migration. [Publication guide](../../GITHUB_PUBLISH_GUIDE.md) chỉ đề xuất branch feat/adaptive-agent-skill-pack-v1.2.1 và các command review/stage/commit/push cho task được cấp quyền sau; chưa command nào trong nhóm publish được chạy.

## Readiness, blockers and Owner decisions

**READY_WITH_RISKS** cho local integration/pre-publish technical review, phụ thuộc kiểm tra artifact cuối được báo trong handoff report. Không có blocker triển khai còn lại. Owner đã quyết định license và conflict contract; không hỏi lại quyền IMPLEMENT đã cấp. Publication vẫn không được phép trong task hiện tại. Rủi ro còn lại: model/runtime, actual CI/native Ubuntu, other Python versions và heuristic secret detection limits.

## Changed-file inventory

| File | Change | First changed line |
|---|---|---:|
| `CHANGELOG.md` | modified | 2 |
| `PROMT-IT-AI-AGENT-COMPACT.md` | modified | 3 |
| `PROMT-IT-AI-AGENT.md` | modified | 3 |
| `README.md` | modified | 66 |
| `integrations/CODEX-USAGE.md` | modified | 8 |
| `templates/TEST-ONLY.md` | modified | 12 |
| `.gitattributes` | added | 1 |
| `.github/workflows/validate.yml` | added | 1 |
| `.gitignore` | added | 1 |
| `AGENTS.md` | added | 1 |
| `GITHUB_PUBLISH_GUIDE.md` | added | 1 |
| `THIRD_PARTY_NOTICES.md` | added | 1 |
| `docs/CI.md` | added | 1 |
| `docs/COMPATIBILITY.md` | added | 1 |
| `docs/CONFLICT_MATRIX.md` | added | 1 |
| `docs/INSTALLATION.md` | added | 1 |
| `docs/INSTRUCTION_CONTRACT.md` | added | 1 |
| `docs/MAINTENANCE.md` | added | 1 |
| `docs/SECURITY_AND_TESTING.md` | added | 1 |
| `docs/adaptive/EXTERNAL_REPO_REVIEW_2026-10-21.md` | added | 1 |
| `docs/adaptive/PACK_README.md` | added | 1 |
| `docs/adaptive/PROVENANCE.md` | added | 1 |
| `docs/adaptive/RESEARCH_IDEA_ATLAS.md` | added | 1 |
| `docs/adaptive/TRACEABILITY_MATRIX.md` | added | 1 |
| `docs/integration/BASELINE.json` | added | 1 |
| `docs/integration/IMPORTED_FILES.json` | added | 1 |
| `docs/integration/TEST_MATRIX.md` | added | 1 |
| `docs/integration/TEST_RESULTS.json` | added | 1 |
| `docs/integration/TEST_RUN.txt` | added | 1 |
| `integrations/ADAPTIVE-USAGE.md` | added | 1 |
| `integrations/adaptive/chatgpt-custom-instructions.md` | added | 1 |
| `integrations/adaptive/codex-AGENTS.example.md` | added | 1 |
| `integrations/adaptive/gemma4-system-prompt.md` | added | 1 |
| `manifest.json` | added | 1 |
| `scripts/build_release.py` | added | 1 |
| `scripts/pack_utils.py` | added | 1 |
| `scripts/repository_checks.py` | added | 1 |
| `scripts/reuse_catalog.py` | added | 1 |
| `scripts/run_regressions.py` | added | 1 |
| `scripts/validate_pack.py` | added | 1 |
| `scripts/validate_repository.py` | added | 1 |
| `skills/adaptive-project-ops/LICENSE` | added | 1 |
| `skills/adaptive-project-ops/SKILL.md` | added | 1 |
| `skills/adaptive-project-ops/THIRD_PARTY_NOTICES.md` | added | 1 |
| `skills/adaptive-project-ops/assets/templates/DEFECT_REPORT.md` | added | 1 |
| `skills/adaptive-project-ops/assets/templates/OPEN_SOURCE_CANDIDATE_REVIEW.md` | added | 1 |
| `skills/adaptive-project-ops/assets/templates/RELEASE_GATE.md` | added | 1 |
| `skills/adaptive-project-ops/assets/templates/REQUIREMENT_TEST_MATRIX.md` | added | 1 |
| `skills/adaptive-project-ops/assets/templates/SECURITY_FINDING.md` | added | 1 |
| `skills/adaptive-project-ops/assets/templates/SECURITY_TEST_PLAN.md` | added | 1 |
| `skills/adaptive-project-ops/assets/templates/SECURITY_THREAT_MODEL.md` | added | 1 |
| `skills/adaptive-project-ops/assets/templates/TEST_CASES.md` | added | 1 |
| `skills/adaptive-project-ops/assets/templates/TEST_RUN_REPORT.md` | added | 1 |
| `skills/adaptive-project-ops/assets/templates/TEST_STRATEGY.md` | added | 1 |
| `skills/adaptive-project-ops/manifest.json` | added | 1 |
| `skills/adaptive-project-ops/references/00-task-contract.md` | added | 1 |
| `skills/adaptive-project-ops/references/01-requirements-architecture.md` | added | 1 |
| `skills/adaptive-project-ops/references/02-repository-engineering.md` | added | 1 |
| `skills/adaptive-project-ops/references/03-debugging-root-cause.md` | added | 1 |
| `skills/adaptive-project-ops/references/04-testing-security-release.md` | added | 1 |
| `skills/adaptive-project-ops/references/05-ai-llm-agent-systems.md` | added | 1 |
| `skills/adaptive-project-ops/references/06-data-experiments.md` | added | 1 |
| `skills/adaptive-project-ops/references/07-tech-research-watch.md` | added | 1 |
| `skills/adaptive-project-ops/references/08-context-memory-skills.md` | added | 1 |
| `skills/adaptive-project-ops/references/09-project-governance.md` | added | 1 |
| `skills/adaptive-project-ops/references/10-academic-reports.md` | added | 1 |
| `skills/adaptive-project-ops/references/11-hardware-runtime.md` | added | 1 |
| `skills/adaptive-project-ops/references/12-multimodal-encoding.md` | added | 1 |
| `skills/adaptive-project-ops/references/13-reverse-engineering.md` | added | 1 |
| `skills/adaptive-project-ops/references/14-agent-orchestration.md` | added | 1 |
| `skills/adaptive-project-ops/references/15-domain-decision-systems.md` | added | 1 |
| `skills/adaptive-project-ops/references/16-evidence-source-protocol.md` | added | 1 |
| `skills/adaptive-project-ops/references/17-security-engineering.md` | added | 1 |
| `skills/adaptive-project-ops/references/18-test-engineering.md` | added | 1 |
| `skills/adaptive-project-ops/references/19-security-verification.md` | added | 1 |
| `skills/adaptive-project-ops/references/20-open-source-reuse-discovery.md` | added | 1 |
| `skills/adaptive-project-ops/scripts/reuse_catalog.py` | added | 1 |
| `templates/DECISION_ADR.md` | added | 1 |
| `templates/DEFECT_REPORT.md` | added | 1 |
| `templates/EXPERIMENT_CARD.md` | added | 1 |
| `templates/OPEN_SOURCE_CANDIDATE_REVIEW.md` | added | 1 |
| `templates/PROJECT_PROFILE.example.yaml` | added | 1 |
| `templates/RELEASE_GATE.md` | added | 1 |
| `templates/REQUIREMENT_TEST_MATRIX.md` | added | 1 |
| `templates/SECURITY_FINDING.md` | added | 1 |
| `templates/SECURITY_TEST_PLAN.md` | added | 1 |
| `templates/SECURITY_THREAT_MODEL.md` | added | 1 |
| `templates/SESSION_CONTEXT_PACKET.md` | added | 1 |
| `templates/TASK_CONTRACT.md` | added | 1 |
| `templates/TECH_IDEA_INTAKE.md` | added | 1 |
| `templates/TEST_CASES.md` | added | 1 |
| `templates/TEST_EVIDENCE_MATRIX.md` | added | 1 |
| `templates/TEST_RUN_REPORT.md` | added | 1 |
| `templates/TEST_STRATEGY.md` | added | 1 |
| `tests/ACCEPTANCE_TESTS.md` | added | 1 |
| `tests/test_integration.py` | added | 1 |
| `tests/test_maintenance.py` | added | 1 |
| `tests/test_packaging.py` | added | 1 |
| `tests/test_reuse_catalog.py` | added | 1 |
| `versions/PROMT-IT-AI-AGENT.md` | added | 1 |
| `versions/v1.0.0-compact.md` | added | 1 |

File REPORT.md, CHANGES.json và manifests cũng được tạo/cập nhật tự động. Diff đầy đủ và actual final-artifact output được bàn giao ngoài source repo; không đưa build ZIP vào Git history mặc định.
