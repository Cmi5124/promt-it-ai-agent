# Debugging, Incident và Root-Cause Tracing

## Quy trình

1. **Symptom**: capture error message, trace/time, config, input, environment, expected vs actual; phân biệt symptom với cause.
2. **Reproduce**: minimal reproduction, deterministic seed nếu có, isolation, environment/version/capacity, rollback-safe setup.
3. **Trace**: request/transaction lifecycle, event timeline, state mutation, dependencies, caller/callee, caches, DB, permissions, retry/timeout/concurrency.
4. **Hypotheses**: lập danh sách nguyên nhân, mỗi giả thuyết cần supporting/contradicting evidence và phép thử phân biệt.
5. **Root cause**: chỉ kết luận khi có chứng cứ loại trừ hoặc xác nhận; tách root cause, contributing factors, triggering condition, detection gap.
6. **Repair plan**: patch tối thiểu, regression cases, rollback, failure injection, observability.
7. **Verify**: trước/sau, test hồi quy, môi trường thực tế có quyền, ghi actual result.

## Quy tắc chống fix vòng lặp

Sau **3 lần sửa thất bại** (hoặc phát hiện lỗi có nguy cơ dữ liệu/bảo mật), ngừng đổi code thử-vận-may. Bắt đầu bug forensics: audit từ hợp đồng nghiệp vụ đến call graph, data/state và môi trường; agent có thể chỉ truy vết theo phạm vi do Owner định rồi bàn giao evidence để Owner phân tích. Chỉ tiếp tục sửa khi có giả thuyết kiểm chứng được hoặc Owner quyết định. Đây là ngưỡng cảnh báo mặc định, không phải cho phép tự động 3 lần sửa khi chưa được ủy quyền.

## Fault taxonomy

Logic, state management, serialization/schema, stale config/secret, dependency version, filesystem/permission, race/deadlock, queue retry loop, cache inconsistency, memory/VRAM exhaustion, GPU/kernel incompatibility, bad data/leakage, benchmark contamination, tool/agent orchestration, deployment difference.

Không sửa vấn đề khác vừa thấy trong lúc debug; báo ngoài scope thành separate finding. Không che dấu lỗi bằng cách bỏ test/hạ acceptance criteria. Với incident, phân biệt mitigation (giảm tác động), corrective action (sửa nguyên nhân), preventive action (chặn tái phát).
