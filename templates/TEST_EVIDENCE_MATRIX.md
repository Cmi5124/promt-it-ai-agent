# Test / Verification Matrix — risk-based / multi-project

| TEST ID | REQ/THREAT | Group / test level | Precondition / fixture | Procedure / verified command | Expected | Actual observed | RUN ID / Evidence | Defect/Finding | Status |
|---|---|---|---|---|---|---|---|---|---|
| T-NORMAL-01 | REQ-* | Normal | Synthetic fixture | NOT_EXECUTED | Valid flow/output/state | NOT_OBSERVED | NONE | - | NOT_RUN |
| T-BOUND-01 | REQ-* | Boundary | At threshold | NOT_EXECUTED | Explicit boundary result | NOT_OBSERVED | NONE | - | NOT_RUN |
| T-INVALID-01 | REQ-* | Invalid | Wrong type/shape | NOT_EXECUTED | Safe reject/no mutation | NOT_OBSERVED | NONE | - | NOT_RUN |
| T-ENV-01 | REQ-* | Dependency/env failure | Isolated injected outage | NOT_EXECUTED | Bounded timeout/recovery | NOT_OBSERVED | NONE | - | NOT_RUN |
| T-SEC-01 | THREAT-* | Security/auth if applicable | Authorized synthetic accounts | NOT_EXECUTED | Deny unauthorized, no leak | NOT_OBSERVED | NONE | - | NOT_RUN |

**Test statuses**: `PASS` executed and meets expected + evidence, `FAIL` executed and violates, `BLOCKED` prerequisites/permissions prevent, `NOT_RUN` not executed, `NOT_VERIFIED` cannot validate claimed outcome. `N/A` chỉ applicability có căn cứ, không tính PASS. Thêm performance/concurrency/migration/AI tool-adversarial tests theo risk. Luôn lưu source version, environment, actual command và results.

Xem `REQUIREMENT_TEST_MATRIX.md`, `TEST_STRATEGY.md`, `TEST_RUN_REPORT.md`, `DEFECT_REPORT.md`; test & release process ở `../skills/adaptive-project-ops/references/18-test-engineering.md` và [04-testing-security-release.md](../skills/adaptive-project-ops/references/04-testing-security-release.md).
