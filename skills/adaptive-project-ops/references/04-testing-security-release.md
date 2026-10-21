# Quality / Security / Release Gate Orchestrator (compatibility entry)

File điều phối của phiên bản trước được **giữ nguyên đường dẫn** để không làm hỏng adapter/đường tham chiếu cũ. Các quy trình chi tiết đã tách độc lập:

- `18-test-engineering.md`: T0→T8 (requirements, strategy, test cases, fixtures, execution, defects, regression, closure); 5 nhóm test, result status, evidence, RTM.
- `17-security-engineering.md`: S0→S7 (secure SDLC, threat modeling, controls, AI/Agent security, vulnerabilities, treatment).
- `19-security-verification.md`: V0→V7 (authorized security test ROE, SAST/SCA/DAST, API/Auth, controlled fuzz/load, AI red team, retest).

## Quality gates trước release

1. **Scope/requirements**: acceptance criteria và affected components đã đối chiếu; những chỗ thiếu quan trọng không bị lờ đi.
2. **Test execution**: critical flows, normal/boundary/invalid/dependency-failure/security as relevant đã có actual results, hoặc báo rõ gap. Không có test output thì `NOT_RUN/NOT_VERIFIED`.
3. **Defects**: không còn unresolved `CRITICAL` hoặc `HIGH` trái release policy. `READY_WITH_RISKS` cần documented exception, risk owner và approval; không tự downgrade severity.
4. **Security/privacy**: threat/control coverage và permission boundaries được xem xét; active security tests chỉ theo ROE đã cấp.
5. **Data/compatibility**: migrations, integrity, cross-version API/config/contracts có evidence; recovery và rollback được xem xét.
6. **Ops/resilience**: error reporting, observability, dependency/recovery, resource envelopes theo target environment.
7. **Supply chain & provenance**: dependencies, manifests, source/version, license đã rà trong phạm vi khả dụng.
8. **Authorization**: release/deployment/commit/push/migrations là quyền riêng, **không được suy ra** từ quyền viết code.

## Gate outcome

- `READY`: đủ evidence cho toàn bộ gate bắt buộc, không còn blocker cấm release.
- `READY_WITH_RISKS`: gate tối thiểu đạt, residual risk được nêu và Owner đã chấp thuận phù hợp policy; **không** dùng để hợp thức hóa critical security/data risk.
- `BLOCKED`: thiếu quyền, kết quả FAIL quan trọng, rủi ro nghiêm trọng hoặc điều kiện quan trọng chưa đạt.
- `NOT_VERIFIED`: bằng chứng chưa đủ để đưa ra kết luận release.

Dùng [RELEASE_GATE.md](../assets/templates/RELEASE_GATE.md); báo đầy đủ tests run/not-run, coverage gaps, findings, rollback, Owner decisions. Một suite `PASS` không tự động cho phép release.
