# Changelog

## [Unreleased] — documentation and behavioral evaluation preparation

- Đồng bộ current status sau merge; giữ historical reports/snapshots nguyên byte.
- Chuẩn bị49 behavioral case variants, runtime/risk/scoring/evidence protocol; tất cả NOT_RUN, chưa có model evaluation.
- Publication trên feature branch, PR merge và CI của đúng HEAD được theo dõi tại [current status có timestamp](docs/STATUS_CURRENT.md); không thay core/skill version hoặc default permissions. Giữ snapshot audit trước publication nguyên byte.

## [1.1.0] — integrated on main, candidate chưa stable release

- PR#2 merged tại4f69295cb8c40a1be70514e4a926e67783bfeb8f; [main CI](https://github.com/Cmi5124/promt-it-ai-agent/actions/runs/39610489708) Windows/Ubuntu64/64 PASS.
- [Current status](docs/STATUS_CURRENT.md) tách integration/CI/release/behavioral evidence; không suy model certification từ merge.

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
