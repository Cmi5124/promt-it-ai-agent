# CI implementation and limits

Workflow local ở .github/workflows/validate.yml chạy Windows/Ubuntu, permissions contents: read, không secret, write, deployment, release hoặc external action. Checkout dùng Git có sẵn trên hosted runner, từ public repository và event SHA; các giá trị context truyền qua env, không ghép input không tin cậy thành shell code. Python standard library dùng validation/unit/build; không pip install.

Các công cụ Git/Python đã được dùng và review trong workflow local, không tải/chạy executable bên thứ ba hoặc action chưa audit. Runner phải có Git, Python và PowerShell như [GitHub runner images](https://github.com/actions/runner-images) công bố. Nếu runtime thiếu, job thất bại rõ thay vì tự cài. [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) hỗ trợ permissions, OS matrix và shell steps.

Workflow chạy validator/manifest/compile và full automated regression suite trên event revision. Không dùng pull_request_target và không expose secrets cho fork code.

Actual CI evidence, SHA, test count, run/job/check IDs và thời điểm kiểm tra tập trung tại [current status](STATUS_CURRENT.md); historical preparation audit được giữ riêng. Kiểm tra cả workflow, jobs, steps và check-runs của đúng HEAD trên Windows/Ubuntu: workflow success chưa đủ nếu một relevant check vẫn pending. Không sửa workflow, validator hoặc test criteria để che check-state bất nhất. Static/unit/package PASS không là behavioral PASS: A01–A44 và49 variants vẫn NOT_RUN. Trạng thái actual CI lấy từ metadata/log, không từ thông báo static của validator.
