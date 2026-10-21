# Test Case Catalog — [Version/Scope]

| Test ID | REQ/AC/THREAT | Group/level | Preconditions and fixture | Steps/command verified | Expected observable result | Actual | Evidence/Run ID | Status |
|---|---|---|---|---|---|---|---|---|
| TC-NORMAL-01 | REQ-* | NORMAL/unit or E2E | Specify fixture | Not executed | Expected valid output and side effect | Not observed | None | NOT_RUN |
| TC-BOUND-01 | REQ-* | BOUNDARY | Max/min/empty | Not executed | Defined boundary outcome | Not observed | None | NOT_RUN |
| TC-INVALID-01 | REQ-* | INVALID | Wrong type/malformed | Not executed | Safe reject/no mutation | Not observed | None | NOT_RUN |
| TC-FAIL-01 | REQ-* | DEPENDENCY_FAILURE | Controlled failure | Not executed | Bounded retry/recover | Not observed | None | NOT_RUN |
| TC-SEC-01 | THREAT-* | SECURITY/AUTH (if applicable) | Isolated account and synthetic data | Not executed | Unauthorized deny/no leakage | Not observed | None | NOT_RUN |

Tạo test case chi tiết trước chạy; đây là **mẫu**, không phải các case đã chạy. `N/A` chỉ khi không áp dụng, kèm căn cứ.
