# Task: TEST_ONLY

- Repository: `<REPOSITORY>`
- Branch: `<BRANCH>`
- Baseline: `<BASELINE>`
- Task: `<TASK>`
- In scope: `<IN_SCOPE>`
- Out of scope: `<OUT_OF_SCOPE>`
- Acceptance criteria: `<ACCEPTANCE_CRITERIA>`
- Git permissions: `NONE`

Không sửa source code, production configuration, dữ liệu người dùng hoặc hành vi sản phẩm; không ghi đè dữ liệu hiện có. Chỉ chạy test không phá hủy dữ liệu bằng command tìm thấy và xác minh từ repository. Ghi command thực tế, precondition, actual result, evidence và status từng test. Phân biệt `NOT_RUN`, `NOT_VERIFIED`, `BLOCKED`, `FAIL` và `PASS`; không bịa command hoặc kết quả.

TEST_ONLY được tạo fixture, cache, temporary files, logs và test evidence chỉ trong đường dẫn/phạm vi được cấp phép; không sửa source code, production configuration, dữ liệu người dùng hoặc hành vi sản phẩm; không ghi đè dữ liệu hiện có. Artifact có lifecycle: tạo trong thư mục tạm mới hoặc ignored path đã cấp, dùng cho run, giữ evidence theo retention đã chốt, cleanup chỉ trong phạm vi được phép; không tự đưa artifact vào Git. Yêu cầu IMPLEMENT hiện tại có đủ scope/quyền là phê duyệt trong phạm vi đó; không hỏi lại quyền đã cấp. Git permissions mặc định NONE; mọi commit/push/merge/reset/PR/release cần quyền riêng hợp lệ, không suy từ quyền sửa file hoặc test.
