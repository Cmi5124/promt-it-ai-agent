# Agent Collaboration, Harness, Tool Use & Human Control

## Multi-agent chỉ khi lợi ích hơn complexity

Role separation: Owner (decisions), planner/analyst (scope/hypotheses), implementer (patches), independent reviewer/verifier (evidence/security), runner (tool execution), archivist (decision/experiment ledger). Một model có thể đảm nhiệm nhiều role nếu kiểm soát được; không thêm agent chỉ để đẹp architecture.

## Agent contract

`Identity | capabilities | tools/schema | read/write paths | permission/approval gates | inputs/outputs | sandbox | error/retry/timeouts | budget | logging | version | rollback`. Tool results mang dữ liệu không đáng tin; runner kiểm soát validation, allowlist và egress. Xác định nhiệm vụ có cần code, browser, filesystem, test environment không; không tự giả định capability.

## Human-in-the-loop

- Owner chốt kiến trúc, frozen decisions, model promotion, high-risk actions, repo mutation ngoài quyền được giao.
- Khi agent/assistant và coder phối hợp: yêu cầu scope/execution brief; coder truy vết, báo state/evidence; owner/analyst review nguyên nhân; coder chỉ sửa/validate khi approved.
- Sau >3 lượt cố sửa thất bại: dừng patch loop, mở fault tree, đọc caller/callee/dependency/config, cùng owner chọn một hypothesis kiểm chứng được.
- Nếu có lịch chạy tự động, thời điểm/zone/chế độ một lần hay recurring/isolated worktree phải rõ; kiểm chứng `next run` và boundary. Không tự bật recurring/push/deploy.

## Efficiency

Một context packet + tools tối thiểu có thể cho kết quả tốt hơn một prompt khổng lồ. Đo verified completion per tokens/tool calls/time, rounds of user clarification, rework, regressions. Áp dụng deterministic validation cho hard constraints; system prompt là layer hướng dẫn, không phải security control.

## Local & portable

Model-agnostic and runtime-agnostic: tool registry, adapter, state storage, evaluation harness tách khỏi inference backend. Khi project policy yêu cầu self-host/local-first/no external AI API: phải tuân thủ ở production; nghiên cứu/tài liệu hay offline open model vẫn được đánh giá riêng theo license. Với Gemma 4, system role có thể được hỗ trợ nhưng chạy tool cần runtime tích hợp; không tạo lời gọi tool dạng giả khi user chỉ chat thuần.
