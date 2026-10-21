# CI implementation and limits

Workflow local ở .github/workflows/validate.yml chạy Windows/Ubuntu, permissions contents: read, không secret, write, deployment, release hoặc external action. Checkout dùng Git có sẵn trên hosted runner, từ public repository và event SHA; các giá trị context truyền qua env, không ghép input không tin cậy thành shell code. Python standard library dùng validation/unit/build; không pip install.

Các công cụ Git/Python đã được dùng và review trong workflow local, không tải/chạy executable bên thứ ba hoặc action chưa audit. Runner phải có Git, Python và PowerShell như [GitHub runner images](https://github.com/actions/runner-images) công bố. Nếu runtime thiếu, job thất bại rõ thay vì tự cài. [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) hỗ trợ permissions, OS matrix và shell steps.

Actual main CI đã được xác minh: [run39610489708](https://github.com/Cmi5124/promt-it-ai-agent/actions/runs/39610489708) tại commit `4f69295cb8c40a1be70514e4a926e67783bfeb8f`, event push. Windows Python3.12.10 và Ubuntu Python3.12.3 đều chạy validator/manifest/compile và64 automated tests PASS. Không dùng pull_request_target và không expose secrets cho fork code.

Đây là evidence baseline main; docs/evaluation revision local mới chưa có Actions run. Static/unit/package PASS không là behavioral PASS: A01–A44 vẫn NOT_RUN. Trạng thái actual CI lấy từ run metadata/log, không từ thông báo static của validator. [Current status](STATUS_CURRENT.md) liên kết evidence và tách historical preparation reports. Task Git NONE này không chỉnh workflow hoặc trigger run mới.
