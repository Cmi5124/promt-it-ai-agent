# AGENTS.md example cho Promt IT(AI/Agent)

Copy file này vào repository đích và thay `<LOCAL_PROMT_FILE>` bằng đường dẫn tương đối đến bản local của `PROMT-IT-AI-AGENT.md`. Placeholder này phải được thay trước khi áp dụng.

## Quy tắc áp dụng

1. Đọc `<LOCAL_PROMT_FILE>` nếu file tồn tại và áp dụng cùng quy tắc repository này.
2. Default mode là `ANALYZE_ONLY` khi task không chỉ định mode.
3. Mỗi task phải nêu riêng phạm vi, acceptance criteria và quyền Git (`NONE`, `COMMIT`, hoặc `COMMIT_AND_PUSH`).
4. Ưu tiên file local; không bắt buộc phụ thuộc vào URL remote.
5. Quy tắc riêng của repository có thể nghiêm ngặt hơn, nhưng không được hạ chuẩn về security, evidence, secret hay prompt injection.
6. Không ghi đè thay đổi ngoài scope; dừng và báo blocker khi thiếu thông tin hoặc quyền quan trọng.
