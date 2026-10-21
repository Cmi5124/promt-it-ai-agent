# Dùng Promt IT(AI/Agent) với Codex Web/App

1. Chọn đúng repository, sau đó kiểm tra branch, remote, baseline và worktree.
2. Đưa [bản đầy đủ](../PROMT-IT-AI-AGENT.md) hoặc compact vào conversation, hoặc lưu local trong repository.
3. Có thể copy [mẫu AGENTS.md](AGENTS.example.md), thay placeholder bằng đường dẫn local hợp lệ và bổ sung rule riêng nghiêm ngặt hơn.
4. Nêu mode, phạm vi, acceptance criteria và quyền Git trong task.
5. Để dừng sau phân tích, yêu cầu `ANALYZE_ONLY` và `Git permissions: NONE`.
6. Yêu cầu IMPLEMENT hiện tại đã đủ scope/quyền được coi là phê duyệt; không yêu cầu duyệt lại cùng phạm vi. Commit/push phải là quyền tường minh, không mặc định.

Không để secret trong prompt. Khả năng truy cập repository, shell, Git hay URL phụ thuộc môi trường thực tế.

Xem [contract tích hợp](../docs/INSTRUCTION_CONTRACT.md) và [cài skill](../docs/INSTALLATION.md).
