# Changelog

## [1.1.0] — integration candidate, chưa phát hành

- Import skill v1.2.1, 21 references, templates, adapters và offline regression tools.
- Giữ snapshot v1.0.0 bất biến; core/compact hiện hành chỉ cập nhật version, TEST_ONLY artifacts và instruction precedence theo Owner.
- Đồng bộ TEST_ONLY và quyền IMPLEMENT hiện có; giữ Git NONE mặc định.
- Thêm validator tích hợp, kiểm tra public-sensitive data, reproducible build và CI Windows/Ubuntu không external actions, secret hay quyền write.
- Apache-2.0 cho owned content được Owner phê duyệt; không relicense nguồn bên ngoài.


Lịch sử phiên bản của bộ prompt. File này không phải yêu cầu bắt buộc của Apache License 2.0.

## [1.0.0] - 2026-07-22

### Added

- Bản prompt đầy đủ và bản compact.
- Hướng dẫn sử dụng cho ChatGPT và Codex.
- Mẫu `AGENTS.md`.
- Năm task mode và template tương ứng.
- Evidence classification, call graph và impact assessment.
- Quy tắc testing, security, AI evaluation, guardrails, observability và release gate.
