# Project Lifecycle, Agile/Scrum, Portfolio & Change Control

## Lifecycle chuẩn vừa đủ

`Idea/Feasibility → Project Initiation/Charter → Scope/Requirements → Architecture/Design → Roadmap/WBS/Sprint → Build/Research/Test → Evidence/Release → Retrospective/Iteration`. Các bước có thể lặp nhưng không bỏ qua gate bản chất. Quản lý dự án xuyên suốt, không áp một số chương/sprint/tháng cố định.

### Artefact chọn theo độ phức tạp

Vision/problem statement; Project Charter; SMART goals; Product/Project Scope; SOW; stakeholder/RACI; SRS/acceptance; WBS theo **100% Rule**; architecture/ADR; Risk Register; Decision Log; Research Backlog; Dependency/Blocker Register; Sprint Backlog; quality/test plan; evidence ledger; release gate; changelog; portfolio registry. Không cần tạo tất cả cho một câu hỏi đơn giản.

## Hierarchy và naming

`Portfolio → Project/Product/Lab → Version/Release → Phase/Gate → Sprint (S) → Task/Subtask → Test/Evidence` và `Research track/Experiment (R)` liên kết ngang. `R` không đồng nghĩa `S`; version không đồng nghĩa sprint; mỗi version có thể gồm nhiều sprint; không đổi naming đã khóa nếu thiếu quyết định. Khi đặt tên mới, giải thích quy ước, ký hiệu và cách map ID/traceability.

## SSOT, append-only, freeze

Tạo một canonical source-of-truth rõ; docs khác link đến đó, không sao chép truth mâu thuẫn. Frozen version/baseline giữ nguyên, ghi correction kiểu forward-only hoặc new version; append experiment/failure logs. Không force-push/history-rewrite hoặc xóa snapshot để làm report đẹp.

## Sprint / Release gates

- Definition of Ready: goal/scope/acceptance/dependency/owner/inputs/test budget đã rõ.
- Definition of Done: output đúng, thực nghiệm/test chứng thực, regressions, risk/known issues, reproducible evidence, owner acceptance khi cần.
- Exit gate không PASS vì deadline hoặc số dòng code. Chỉ chuyển sprint/phase khi evidence và quyền điều phối đủ.
- New ideas vào backlog trừ khi Owner phê duyệt change request; review scope/schedule/risk/contract và quyết định rebaseline trước khi chen giữa sprint.

## Portfolio prioritization

Mỗi item có `goal, status, priority, impact, effort, costs, readiness, dependencies, deadlines, opportunity, risk, gate`. Trạng thái ví dụ `IDEA/BACKLOG/READY/ACTIVE/BLOCKED/ON_HOLD/DONE` nhưng không tự thay status có sẵn. Khi project hoàn tất: verify completion → portfolio review → re-score candidates → Owner approval rồi mới active. WIP giới hạn theo capacity thật, không đề nghị mở dự án vô hạn.

## Trade-off về future-proofing

Cho phép extension contracts và testability từ đầu; tách *thiết kế cho thay đổi* khỏi *triển khai trước mọi chức năng giả định*. Mọi abstraction mới phải giải thích chi phí, lợi ích, trigger, undo plan và ownership.
