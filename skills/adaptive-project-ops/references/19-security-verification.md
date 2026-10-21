# Security Verification — Authorized Test Procedure & Evidence

**Kích hoạt:** kiểm thử bảo mật web/API/local services, code review security, assessment, pentest được ủy quyền, adversarial AI/Agent testing, security regression. Đọc thêm `17-security-engineering.md` (threat & controls) và `18-test-engineering.md` (test evidence) khi cần.

## 0. ROE — Rules of Engagement trước mọi kiểm thử chủ động

Phải có scope được cấp quyền thực tế:

- `WHO`: asset owner/authorized contact, test operator, reviewer; quyền của agent và tài khoản test.
- `WHAT`: định danh target chính xác (repo/app/domain/IP/environment), feature/account/tenant, phiên bản, dữ liệu **được phép truy cập**, exclusions/out-of-scope.
- `WHEN/HOW`: window, được phép test category nào (static, dependency, API, manual, DAST, fuzz/load), rate/concurrency/duration caps, network egress restrictions, IP allowlist nếu có.
- `SAFEGUARDS`: nonproduction/isolated target, synthetic data, backups, visibility/monitoring, stop threshold, kill switch/rollback contact, reporting/disclosure rules.
- `GO/NO-GO`: nhận diện shared infrastructure/third-party services, hosting provider policy và tác động tới người khác. Nếu unclear hoặc unauthorized: `BLOCKED` cho active scan/exploitation; chỉ được thiết kế kế hoạch hoặc static review an toàn theo quyền sẵn có.

**Không tự chạy** brute force, DoS/DDoS, high-rate fuzzing, destructive payloads, data exfiltration, credential stuffing hay tấn công production. Có quyền sở hữu domain chưa đủ chứng minh toàn bộ hạ tầng/third party nằm trong scope. Nếu xuất hiện secret thật/dữ liệu khách hàng, không copy ra ngoài; chuyển sang incident workflow.

Template: [SECURITY_TEST_PLAN.md](../assets/templates/SECURITY_TEST_PLAN.md).

## 1. Workflow V0–V7

| Phase | Hoạt động | Evidence cần |
|---|---|---|
| V0 AUTH | ROE, permitted operations, exclusions, approved safe environment | Authorization/scope/stop limits; nếu thiếu: BLOCKED |
| V1 RECON | Asset inventory & config/architecture/source review trong quyền | Verified versions and test surface; no invented endpoints |
| V2 THREAT → CASES | Map threat/control/ASVS/WSTG category → negative test cases | Linked risk/test matrix, expected secure behavior |
| V3 STATIC | SAST/manual secure review, secret scanning **không tiết lộ**, SCA/SBOM/lockfile, IaC/config inspection | Tool, version, exact finding, false positive caveat |
| V4 CONTROLLED DYNAMIC | Functional negative auth and validation, API contracts, safe DAST/fuzz/performance where ROE permits | Minimal proof, rate/limit adherence, logs redacted |
| V5 TRIAGE | Reproduce safely, de-duplicate, assess exploitability/impact/confidence | Finding severity, evidence, not scanner score alone |
| V6 FIX/RETEST | Remediation in separate authorized IMPLEMENT; regression/negative tests in TEST_ONLY | Before-after, threat closure, new risk check |
| V7 CLOSE | Residual risk, unresolved/blocked tests, review/signoff, secure evidence retention | Security test report, release recommendation |

Các công cụ chỉ là ví dụ **candidate**; không tự khẳng định đã cài/running: SAST (Semgrep/CodeQL), SCA (OSV/Trivy/Dependabot), DAST (ZAP), fuzz (AFL++/libFuzzer), cloud/IaC policy scanning. Chỉ chạy command khi được xác minh trong môi trường và được cấp quyền.

## 2. Ma trận security test theo bề mặt

| Bề mặt | Tình huống cần kiểm tra | Expected secure behavior |
|---|---|---|
| Identity | Không token, token hết hạn, token sai scope/audience, session sau logout | Reject và không có side effect, không leak thông tin |
| Authorization | User A truy cập object B, role thấp gọi privileged operation, cross-tenant | Server/tool enforce deny; audit; không data leak |
| Input/output | Types, encoding/Unicode, XSS/injection, path traversal, malicious upload, query abuse | Validate/canonicalize/parameterize đúng, output encode, safe error |
| Network & SSRF | Redirect/domain/scheme restrictions, metadata/internal hosts trong request có URL | Egress and allowlist enforce, no access unauthorized |
| Data & secrets | Logs/export/cache/backups/error traces, retention/tenant cleanup | Redaction, permission, storage and lifecycle control |
| Dependency | Outdated vulnerable dependency, unpinned download, malicious artifacts | Provenance, advisory triage, fail-closed policy when risk high |
| Concurrency/resilience | Duplicate requests, retry/idempotency, race, bounded load | State integrity, resource ceilings, graceful degradation |
| Agent & tools | Prompt injection từ retrieved content, unauthorized tool action, malicious args, tool result impersonation | Instruction hierarchy maintained; tool runner enforces auth/sandbox |
| Memory/RAG | Tenant data retrieval, poison chunks, stale docs, cite spoofing | ACL/provenance/groundedness validated, no cross-tenant leaks |
| Model/dataset | Poisoning or unsafe serialization, licensing/provenance of checkpoints | Quarantined/untrusted artifacts; integrity check and constrained loading |

Test inputs không chứa credential thật hay payload phát tán. Với security proof chỉ dùng test data và chứng minh tối thiểu đủ tái hiện trong môi trường được ủy quyền, dừng trước exfil/destruction.

## 3. AI/Agent red-team workflow an toàn

1. Chốt synthetic canary và capability/permission boundary, sandboxed tools; xác định tool nào **không** được phép gọi.
2. Baseline normal legitimate task; lưu tool schema and expected lawful action.
3. Xây test loại: direct/indirect prompt injection; role spoof; retrieved content instruction; fake tool errors; escalation/unauthorized writes; memory poisoning; cross-session contamination; tool argument override; unsafe code output; hallucinated file/command.
4. Chạy có giới hạn: mỗi test case nhập cùng inputs, giữ evidence tool traces; phân biệt model suggestion vs **actual** executed action.
5. Verify refusal/abstention AND actual app-side deny. Không tính model "không làm" nếu runtime đã thực thi trái quyền, và ngược lại.
6. Retest after fixes, kiểm tra false positives tác động đến legitimate user flows.

Metrics: attack-success measured by verified unauthorized side effect, unauthorized tool attempted, permission denial effectiveness, data leak occurrence (synthetic), false refusal, task completion, recovery, latency; định nghĩa denominator, seeds và environment.

## 4. Finding lifecycle & disclosure

`FINDING → VALIDATION → SEVERITY/CONFIDENCE → OWNER TRIAGE → MITIGATION/FIX → RETEST → RESIDUAL RISK → CLOSE/ACCEPT/DEFER`.

- Evidence `VERIFIED` chỉ khi reproducible hoặc có artifact trực tiếp. Static scanner output đơn độc có thể là **candidate**, phải triage false positives.
- Severity: impact × likelihood × exposure, kể cả dữ liệu/availability/business; ghi confidence riêng, không bịa CVSS nếu chưa chấm đúng vector.
- Report có affected version/environment, minimal sanitized evidence, requirements/tests, remediation, rollback, retest status, Owner decision. Giữ bằng chứng kín, phân quyền, giới hạn retention.
- Phát hiện critical hoặc out-of-scope asset trong lúc chạy: **STOP**, báo Owner theo kênh đã thống nhất; không pivot/lateral movement để "xác minh sâu hơn".

## 5. Frameworks và phiên bản (mapping có điều kiện)

- Web/API security requirements: **OWASP ASVS 5.0.0 (stable)** — `https://asvs.owasp.org/`.
- Web security testing method: **OWASP WSTG v4.2 (stable)** — `https://owasp.github.io/www-project-web-security-testing-guide/v42/`. WSTG 5.0 latest là development, không đánh đồng stable.
- Software lifecycle: **NIST SSDF 1.1 final** — `https://csrc.nist.gov/pubs/sp/800/218/final`.
- GenAI applications: **OWASP Top 10 for LLM Applications 2025** — `https://genai.owasp.org/llm-top-10/`.

Các tài liệu này là nguồn tham chiếu; chỉ viện dẫn test ID cụ thể khi đã đọc đúng version. Không tự tuyên bố compliance, pentest PASS hay "zero vulnerabilities" từ việc chạy scanner một lần.
