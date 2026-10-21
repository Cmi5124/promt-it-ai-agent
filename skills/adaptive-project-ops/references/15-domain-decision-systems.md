# Domain Decision Systems — Finance, Operations, Risk, Security

## Domain fidelity

Nếu hệ thống hỗ trợ quyết định quan trọng (tài chính, bảo mật, hoạt động tổ chức), hỏi business objectives, decision rights, risk appetite, available data, temporal constraints, regulation, auditability và failure consequences. Tránh biến một model output thành hành động thực khi chưa có authorization, hard limits, audit, circuit breakers và rollback/recovery.

## Time-series / trading / forecasts

Data temporal integrity: event timestamps, timezone, bars/quotes, market sessions, leakage prevention; feature tại decision time; label tương lai; transaction costs, slippage, fees, execution risk, survivorship bias, nonstationarity/regime shifts. Backtest, paper/sandbox, live đều là các mức evidence khác nhau. Trade log của bên thứ ba cần có quyền hợp lệ và không coi profitable history là chứng minh causal strategy hoặc tương lai có lãi.

## Security decision support

Tách finding candidate, independently verified finding, false positive, risk score, remediation proposal, execution permission. Security graph/control graph có thể giúp truy vết assets→vulnerabilities→impact nhưng không thay chứng cứ khai thác/logic. Automated remediation cần owner/tenant approval, snapshot và measured rollback.

## Operations automation

Phân biệt deterministic rules/workflows với AI reasoning. Với công việc lặp lại và có cấu trúc, ưu tiên code/automation minh bạch; AI phù hợp input phi cấu trúc, triage, explanation, forecasting khi có eval. Đo throughput, accuracy, error rate, exception handling, audit burden, cost và end-user impact.

## Output boundaries

Báo `VERIFIED/INFERRED/ASSUMED`; trình bày options, thresholds/risks, evidence gaps, human approval points. Không tự thực hiện giao dịch, khóa/mở quyền, gửi email, xoá dữ liệu, scan internet hay thay chính sách tổ chức.
