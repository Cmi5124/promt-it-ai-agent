# Business Requirements → Architecture

## 1. Yêu cầu nghiệp vụ không phải là sơ đồ hay framework

Xác định stakeholder, user journey, actor, trigger, precondition, main/alternative/exception flow, business rule, nonfunctional requirements, data/privacy boundary, success metric. Tách:
- Business requirement: lý do và kết quả nghiệp vụ.
- Functional requirement: hệ thống **phải làm gì**.
- Non-functional/quality attribute: latency, throughput, availability, privacy, security, portability, extensibility, observability, maintainability, cost.
- Constraint: công nghệ/chi phí/hạ tầng/harness/rubric/permissions.
- Acceptance criterion: quan sát được, có điều kiện đầu vào và expected.

Yêu cầu phải có ID, độ ưu tiên, nguồn, trạng thái, owner, dependencies, verification method. Không suy ra một UI/mockup là evidence cho backend/business logic.

## 2. Feasibility trước chọn architecture

Đánh giá technical, resource/compute, financial, legal/license, data access, deadline, skills, operability. Nêu `VERIFIED/ASSUMED` cho mỗi giả định. Phân biệt prototype, MVP, release, production, research candidate.

## 3. Architecture có kiểm soát

- Từ flow nghiệp vụ ⇒ domain/bounded contexts, state, module, contract, data ownership, event/queue, failure paths.
- Ưu tiên kiến trúc có thể hiểu, test, rollback; modular monolith thường là baseline đánh giá khi dự án còn nhỏ, **không bắt buộc cho mọi dự án**.
- Tách lõi nghiệp vụ khỏi UI, model provider, DB, queue, transport; adapter/port rõ khi có lý do thật.
- So sánh component reuse vs new abstraction; hỗ trợ future-proofing bằng extension points hợp lý, **không build feature chỉ vì có thể sẽ cần**.
- Kiểm tra authentication, authorization, roles/tenant, privacy, schema migrations, transaction/idempotency, retries, timeout, degraded mode, observability.
- Thiết kế kiến trúc dựa trên luồng dữ liệu và hành vi thật; đừng bịa module hoặc interface.

## 4. Traceability

`BR → FR/NFR → Design decision/ADR → module/interface/data → test → evidence → gate`. Khi đổi requirement/architecture: impact matrix cho caller/callee, API/schema, data, security, performance, code/test, delivery và rollback.

## 5. Kiểm tra đầu ra

Lập `Scope`, `Out of scope`, solution alternatives (kèm tradeoffs), architecture diagram nếu user yêu cầu, interface/data contracts, risk register, test strategy, Owner decision points. Luôn ghi rõ thiết kế **đề xuất** khác với triển khai **đã xác minh**.
