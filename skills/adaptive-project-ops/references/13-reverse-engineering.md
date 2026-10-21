# Reverse Engineering / Black-Box Analysis / Lab Research

## Scope và quyền hợp lệ

Chỉ kiểm tra ứng dụng/artefact có quyền phân tích và trong phạm vi luật/giấy phép áp dụng. Không hướng dẫn vượt DRM, chiếm quyền hệ thống hay truy cập dữ liệu người khác trái phép. Không chạy binary/tool bên ngoài không tin cậy với đặc quyền cao; ưu tiên lab cô lập, snapshot, network/egress control, data minimization.

## Chia lớp bằng chứng

1. Public docs, headers, metadata, manifests/licenses/packaging.
2. Static code/object/symbol/AST/resource/config/dependency analysis (khi được phép).
3. Dynamic black-box behavior: inputs, outputs, state transitions, timing, errors, permissions, logs; dùng test harness kiểm soát.
4. Protocol/API/schema/UX inference từ nhiều observation; phân biệt observed contract vs hypothesized implementation.
5. Reconstructed design/model candidates; **không** biến giả thuyết thành mã nguồn gốc.

## Trước khi tự reverse-engineer

Tìm nguồn tái sử dụng có giấy phép và phù hợp qua `20-open-source-reuse-discovery.md`. "Search before build" tránh decompile khi đã có parser/protocol/SDK tương thích. Không tự khởi chạy repo tìm được; verify provenance và license.

## Agent-assisted analysis

Nếu tool qua MCP/agent cung cấp extraction, decompilation, app inspection, tracing: xác minh tool, version, privileges, filesystem/network behavior, supported formats, evidence export, prompt injection boundary, cleanup. Tool chỉ là adapter; không cho plugin tự vượt quyền hoặc tự chạy code extracted.

## Benchmark và report

Ghi `artifact origin/version/hash | consent/license | tool/environment | exact methods | observations | inferred behavior | uncertainties | reproducibility | risks`. Đối chiếu source nếu có, không phán “giải mã hoàn toàn” chỉ vì tìm được bundle/resources. Khi nghiên cứu kỹ thuật bảo mật hoặc sao chép cơ chế, ưu tiên học pattern và xây implementation độc lập hợp lệ.
