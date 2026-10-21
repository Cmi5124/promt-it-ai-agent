# Test Engineering — Quy trình kiểm thử end-to-end, traceability & evidence

**Kích hoạt:** yêu cầu thiết kế kiểm thử, viết test, chạy test, review quality, regression, QA/UAT, debug validation, benchmark/release. **Quyền:** lập test plan ≠ quyền chạy; `TEST_ONLY` không cho phép sửa code/sản phẩm, xoá database, cài package chưa duyệt, deploy, stress môi trường production.

## Test lifecycle — T0 đến T8

| Bước | Hoạt động cụ thể | Output / Exit check |
|---|---|---|
| T0 — REQUIREMENT REVIEW | Xác định spec/rubric, success criteria, precondition, input/output, critical user journeys, data/privacy, NFR. Tag mâu thuẫn/thiếu | Requirements list có IDs và mức priority; blocker được báo |
| T1 — TEST STRATEGY | Chọn mục tiêu, scope/exclusion, test levels/types, automated/manual, tools **đã xác minh**, coverage/risk budget, reporting, roles | `TEST_STRATEGY.md` đã nhất quán với task; chưa chạy gì |
| T2 — TEST DESIGN | Requirement-to-test mapping, EP/BVA, decision table, state transitions, pairwise khi cần; 5 nhóm tối thiểu | Test cases có expected kết quả định lượng/quan sát được |
| T3 — TEST DATA & ENV | Synthetic fixtures, reset/teardown, test accounts, schema, dependency/service version, seed, isolated environment, baseline snapshot | Entry criteria: reproducible, permission, safeguards, rollback |
| T4 — EXECUTE | Chạy từng case trong mode được phép; capture exact commands, runtime config, timestamps, exit code, output redacted, screenshots/log | Actual+evidence chỉ cho case thật sự đã chạy; statuses trung thực |
| T5 — DEFECT MANAGEMENT | Record actual≠expected, reproducibility, severity vs priority, owner, root cause hypothesis, linked affected requirements; không sửa ngoài scope | Defect ID, steps reproduce, evidence và trạng thái |
| T6 — FIX VERIFICATION | Khi fix được duyệt/thực hiện: retest targeted bug; regression vùng ảnh hưởng; confirm compatibility/security | Before/after artifacts, regression results; không chấp nhận flaky pass đơn lẻ |
| T7 — EXIT ASSESSMENT | Tổng hợp passed/failed/blocked/not-run, coverage/gap, residual risks, performance context, signoff | READY / READY_WITH_RISKS / BLOCKED / NOT_VERIFIED theo policy |
| T8 — ARCHIVE | Frozen manifest, logs, cases, versions, decision records, unresolved issues | Reproducibility packet; append-only evidence/immutable snapshots |

Quy trình áp dụng theo độ rủi ro: task nhỏ dùng test tối thiểu có ý nghĩa; release/thay đổi dữ liệu/authorization bắt buộc chiều sâu tương ứng. Không có "test 100%" nếu không định nghĩa denominator, coverage và môi trường.

## 1. Test design bắt buộc theo user contract

**Năm nhóm test** cho một thay đổi phần mềm (security/auth nếu thích hợp với hệ thống):

1. `NORMAL`: luồng hợp lệ/happy path; giá trị đầu ra, side effects, state persisted đúng.
2. `BOUNDARY`: min/max, 0/1, null/empty, limits, off-by-one, timezone/encoding, precision, memory/quota.
3. `INVALID`: malformed/wrong type, missing fields, unknown enum, duplicate requests, out-of-order state, input không trusted.
4. `DEPENDENCY/ENV FAILURE`: network timeout, disk full, DB unavailable, GPU OOM, service 5xx, stale cache, cancellation, retry budget và recovery.
5. `SECURITY/AUTH`: authentication/authz, cross-user/tenant, secret handling, input abuse, tool privilege; chỉ khi tính năng có boundary liên quan. Không có auth thì xét relevant trust/resource boundary khác; ghi `N/A` có lý do, **không báo PASS giả**.

**Bổ sung theo scope:** unit, component, integration, contract, API, E2E, migration, backward compatibility, regression, concurrency/race, property-based, fuzzing controlled, load/performance/soak, chaos/recovery, accessibility, usability, data lineage, model eval, tool-call validation, adversarial/safety.

Thiết kế bằng equivalence partitioning, boundary value, decision table, state graph, transition coverage, pairwise, fault injection, mutation testing khi phù hợp; không chạy các loại trên chỉ vì có tên trong danh sách.

## 2. Traceability bắt buộc

Đường truy vết tối thiểu: `REQ/NFR/THREAT ID → acceptance condition → TEST ID → actual run ID → evidence → defect/finding → retest → release gate`.

- Không bỏ sót negative path hay authorization-sensitive condition do chỉ test happy path.
- Nếu test không có requirement, nêu risk/hypothesis làm căn cứ.
- Nếu requirement chưa có test, ghi coverage gap và nguyên nhân, không che giấu.
- Coverage có thể đo requirements covered, branch/path, state transition, data partition, API/schema contract, threat control. **Code coverage ≠ chất lượng hay bảo mật**.

Templates: [REQUIREMENT_TEST_MATRIX.md](../assets/templates/REQUIREMENT_TEST_MATRIX.md), [TEST_STRATEGY.md](../assets/templates/TEST_STRATEGY.md), [TEST_CASES.md](../assets/templates/TEST_CASES.md).

## 3. Execution contract — never fabricate

Một test record phải có:

`TEST_ID | RUN_ID | REQ/RISK_ID | environment | preconditions | test data | steps/command (verified) | expected | actual | evidence | status | defect_id`.

- **PASS**: đã chạy, actual thoả expected, evidence lưu được; **FAIL**: chạy và sai expected; **BLOCKED**: không thể tiến hành do điều kiện/quyền/dependency; **NOT_RUN**: đã thiết kế nhưng chưa chạy; **NOT_VERIFIED**: có claim mà bằng chứng chưa đủ hoặc không đọc được.
- `N/A` chỉ là nhãn applicability kèm lý do, không là test pass. Một lệnh trả `exit 0` chỉ chứng minh lệnh đó thành công theo semantics của nó, không suy toàn suite pass.
- Không bịa tên test command, test framework, file, fixture, logs hoặc API. Đọc repository/manifest/CI config để xác minh trước.
- Không tự sửa môi trường/restore database/seed destructive; cần quyền riêng. Redact PII và secret trong logs/evidence.
- Khi test liên tục flake: phân biệt nondeterminism, shared state, timeout, race, real defect; ghi retry protocol trước, không auto retry đến khi green rồi công bố PASS.

Template: [TEST_RUN_REPORT.md](../assets/templates/TEST_RUN_REPORT.md).

## 4. Defect workflow, prioritization & regression

`NEW → TRIAGED → REPRODUCED → [ASSIGNED/FIX IN AUTHORIZED MODE] → FIXED_CANDIDATE → RETESTED → CLOSED`, hoặc `BLOCKED/DEFERRED/REOPENED`.

- Severity phản ánh hậu quả; priority phản ánh lịch sửa theo business/time; có thể khác nhau. Không tự giảm severity để qua gate.
- Defect report: version, exact input, steps, expected/actual, environmental differences, minimal reproducible, log/timestamp, impact, affected requirements, suspected cause `INFERRED` cho đến xác minh.
- Retest chứng minh lỗi cụ thể được sửa; regression chứng minh những hành vi đã chọn không bị phá; cả hai có mục đích khác nhau.
- Với API/DB schema: test forward/backward compatibility, migrations, rollback/backfill, repeatability và concurrency khi cần.
- Sau 3 lần sửa không có kết quả: kích hoạt `03-debugging-root-cause.md`, không tiếp tục patch loop không evidence.

Template: [DEFECT_REPORT.md](../assets/templates/DEFECT_REPORT.md).

## 5. Performance, resilience & AI testing tùy domain

- Performance: define latency p50/p95/p99, throughput, concurrency, request shape, warmup, resource sampling, duration, environment & noise; single local benchmark ≠ production capacity.
- Load/stress/soak: phải có permission, time window, concurrency/rate caps, isolation, health guard, stop criterion và recovery; coi `19-security-verification.md` nếu có risk security.
- AI model: model-only metrics, held-out/OOF, leakage guards, seeds, per-class error, calibration, cost/VRAM/latency; không dùng LLM judge duy nhất.
- LLM agents: instruction priority, prompt injection resistance, tool-arg schema, authorization boundaries, tool failure/retry/cancel, task completion+verifier, context retention, false action, cross-user/session leak.
- Data pipelines: input integrity, data contracts, idempotency, dedup, DLQ, race, schema evolution, lineage, GDPR/privacy rule theo jurisdiction thực tế nếu áp dụng.
- Reports/artifacts: source accuracy, rubric, editable structure, format/pagination, links, no fabricated result; không nhầm đó là unit tests.

## 6. Exit gate & handoff

**Entry:** requirements và environment đủ rõ, quyền phù hợp, test data và stop conditions. **Exit:** relevant critical paths tested; no unresolved disallowed critical risk; regressions measured; gaps explicit; Owner signed off residual risks/permissions when needed. Không hạ acceptance vì deadline.

Handoff gồm: scope/test levels, requirement coverage (numerator/denominator), test run summary, `PASS/FAIL/BLOCKED/NOT_RUN/NOT_VERIFIED`, defects (severity/priority), evidence links, CI/runtime version, env mismatch, residual risks, rollback readiness, next actions, Owner decisions.

Chỉ tuyên bố "tested" cho phép thử **thật đã chạy**. Nếu chỉ tạo test plan/cases, toàn bộ execution = `NOT_RUN`.
