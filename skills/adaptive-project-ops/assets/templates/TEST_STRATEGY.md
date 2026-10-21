# Test Strategy / Plan — [Task or Release ID]

- Mode / Authorization: `PLAN_ONLY` / `TEST_ONLY` (chọn theo nhiệm vụ)
- Scope in/out: [xác định]; baseline/version/branch: [đã xác minh hoặc NOT_VERIFIED]
- Requirements/AC/NFR: [IDs]; risk criticality: [LOW/MEDIUM/HIGH/CRITICAL]
- Test levels/types applicable: [unit/component/integration/contract/E2E/perf/security/AI...]
- Five test groups: normal; boundary; invalid; dependency/env failure; security/auth or reasoned N/A
- Coverage target & denominator: [n requirement có test / tổng requirement]; coverage exceptions: [IDs]
- Test data/fixture/privacy: [synthetic, data lineage, secrets handling]
- Environment/tools/commands: [verified source only; do not invent]
- Entry criteria: [required state, permissions, dependencies, rollback safeguards]
- Execution order: [risk priority] and dependency constraints: [..]
- Stop conditions: [critical errors, data integrity, environmental alarms, scope breach]
- Exit criteria: [required test evidence, security findings, accepted residual risks]
- Defect triage: [severity/priority, owner]; retest/regression strategy: [..]
- Deliverables: [RTM, case list, runs, defects, evidence, gate]
- Owner approvals pending: [..]

**Status:** `PLAN_ONLY/NOT_RUN` cho đến khi có run evidence.
