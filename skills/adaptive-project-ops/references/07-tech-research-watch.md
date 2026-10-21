# Technology Intake, Paper/Repo/News Review và Idea Adoption

## Không coi một bài chia sẻ là chân lý

Khi nhận link, tweet, bài báo, infographic, repo hoặc ảnh chụp: hiểu câu hỏi người dùng trước — giải thích, fact-check, so sánh, đề xuất hay thiết kế test? Nếu thông tin có tính thời sự/niche và có web tool, xác minh **đúng URL**, source origin, author, date, version/release, licensing, maintenance, benchmarks, reproducibility và known limitations. Phân biệt sự kiện xảy ra và ngày bài được đăng. Nếu không kiểm chứng được: `NOT_VERIFIED` chứ không đoán.

## Review card

1. **Claim:** phát biểu gốc có thực sự nói điều đó không?
2. **Mechanism:** thành phần/thuật toán/contract hoạt động ra sao? baseline nào? Phân biệt kiến trúc, kỹ thuật, công nghệ, công cụ và sản phẩm.
3. **Novelty:** mới ở phần nào, mới ở application hay thay đổi nền tảng? Có bằng chứng ngoài marketing chưa?
4. **Fit & gap:** vấn đề giải quyết, constraints, existing mechanism, điểm trùng/cần merge. Đừng FOMO, đừng tự thêm feature.
5. **Threats and cost:** licensing, API dependency, data ownership, auth boundaries, runtime hardware, VRAM, latency, reliability, support, complexity, maintenance.
6. **Evaluation:** thiết kế A/B cùng tasks, same dataset/splits, reproducibility, quality, performance, failure/ablation.
7. **Adoption:** `KEEP / REINTERPRET / DEFER / REJECT / NEW` hoặc `EXTEND / MERGE` trong change register; ghi source, rationale, owner decision.

## Tri thức phổ biến cần phản biện

- Không nói `RAG → GraphRAG → HybridRAG` là chuỗi thay thế bắt buộc; đây là hướng retrieval/composition có ưu nhược và benchmark khác nhau.
- Không coi một framework/graph/agent protocol, mô hình generation, database hay cache là kiến trúc giải quyết mọi bài toán.
- Với tác vụ lặp lại/deterministic, so sánh rule-based automation với AI; dùng AI khi classification/generation/reasoning/unstructured input thật sự tạo giá trị.
- Với framework từ cộng đồng (agent prompts, ECC, memory compression, reverse engineering, load testing), ưu tiên **tái sử dụng pattern** hoặc gap-analysis trước khi sao chép.

## Search-before-build (khi lựa chọn implementation)

Nếu task yêu cầu lựa chọn thư viện/SDK/công cụ hoặc build-vs-reuse, xem `20-open-source-reuse-discovery.md`: kiểm tra thành phần có sẵn, official SDK, OSS index theo nguồn, license, supply chain và sandbox tests trước adoption. Link "awesome" là danh mục ứng viên, không phải bằng chứng code đã an toàn. Không auto-install/clone.

## Research backlog

Ghi: `candidate_id | source/date | problem | mechanism | alternatives | evidence grade | scope fit | risk/cost | experiment | status | owner decision`. Không làm thay đổi sprint/version frozen chỉ vì thấy công nghệ thú vị. Với SHARE_IDEA/ANALYZE_ONLY/PLAN_ONLY, đầu ra là **assessment/backlog suggestion**, không tự code/đưa vào roadmap. Với yêu cầu IMPLEMENT đã đủ scope/quyền, thực hiện và verify phần được giao; không dừng ở backlog hoặc hỏi lại quyền đã có.
