# Usage và ranh giới ba runtime

[Contract hiện hành](../docs/INSTRUCTION_CONTRACT.md) thống nhất full/compact prompt, SKILL.md, các adapters và TEST_ONLY template; không nạp snapshot lịch sử như instruction mới. [Hướng dẫn cài](../docs/INSTALLATION.md) phân biệt copy/source với runtime discovery.

| Runtime | Instructions | Execution boundary |
|---|---|---|
| ChatGPT | Full hoặc compact prompt + task; [adapter](adaptive/chatgpt-custom-instructions.md) tùy UI | Chỉ đọc file/URL hoặc tool khi capability thật có sẵn; không claim ZIP auto-install |
| Codex | AGENTS.md + [skill](../skills/adaptive-project-ops/SKILL.md) khi liên quan; [adapter](adaptive/codex-AGENTS.example.md) để tham khảo | Task cấp scope/quyền; Git NONE mặc định; read-only được phép, không tự sửa repo khác |
| Gemma 4/local | [System adapter](adaptive/gemma4-system-prompt.md), core và references được runner nạp | Model chỉ đề xuất tool call, runner thực thi và enforce quyền; không bắt buộc cloud API |

Các path references/ trong adapter tính từ gốc skill canonical, không phải folder integrations. SHARE_IDEA chỉ yêu cầu đánh giá/đề xuất, không mutation. IMPLEMENT đã được cấp đủ scope/quyền thì làm và verify, không xin lại quyền đã có. TEST_ONLY artifact chỉ trong đường dẫn được cấp, không ghi đè sản phẩm/dữ liệu và không tự stage.
