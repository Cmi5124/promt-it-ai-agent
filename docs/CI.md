# CI implementation and limits

Workflow local ở .github/workflows/validate.yml chạy Windows/Ubuntu, permissions contents: read, không secret, write, deployment, release hoặc external action. Checkout dùng Git có sẵn trên hosted runner, từ public repository và event SHA; các giá trị context truyền qua env, không ghép input không tin cậy thành shell code. Python standard library dùng validation/unit/build; không pip install.

Các công cụ Git/Python đã được dùng và review trong workflow local, không tải/chạy executable bên thứ ba hoặc action chưa audit. Runner phải có Git, Python và PowerShell như [GitHub runner images](https://github.com/actions/runner-images) công bố. Nếu runtime thiếu, job thất bại rõ thay vì tự cài. [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) hỗ trợ permissions, OS matrix và shell steps.

Native commands trong CI chỉ dành cho runner tạm sau khi Owner publish workflow; task local này không execute chúng và không cấp quyền Git cho agent. Actions actual runs: NOT_RUN. Syntax/static review không là CI PASS. Không dùng pull_request_target và không expose secrets cho fork code. Python/runner image version được log trong job; tương thích Ubuntu thực cần actual run.
