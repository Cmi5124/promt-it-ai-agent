# Context Engineering, Memory, Agent Skills và Compression

## Phân lớp và provenance

Tách `system/policy`, `current task`, `owner decisions`, `repo/project source-of-truth`, `evidence`, `recent conversation`, `long-term memory`, `retrieved external context`, `tool observations`, `agent working state`, `archived state`. Mỗi layer có priority, TTL/validity, owner, source, ACL, mutation policy và conflict resolution. Không tự coi summary là bằng chứng runtime.

## Context packet thay raw dump

Một packet hiệu quả gồm: `objective | mode | authoritative baseline | accepted decisions | current repo/data state | constraints | file/line pointers | evidence links | acceptance | pending questions | risk | allowed tools | last safe checkpoint`. Không nhét tất cả history hay log vào một lần. Duy trì recoverability: tóm tắt kèm nguồn/ID, có thể truy hồi bản gốc khi chất lượng quan trọng.

## Long-context failure

Kiểm tra lost-in-middle, stale facts, contradictory memory, tool-output injection, irrelevant retrieval, instruction hierarchy confusion và context window truncation. Nén/tách tầng theo relevance và budget; đặt retrieval priority; có freshness filter; dùng eviction với khả năng restore. **Đừng loại bỏ bằng chứng quan trọng chỉ để tiết kiệm token.**

## Image-coded context / multimodal encoding là HYPOTHESIS

Mã hóa văn bản, metadata, dataset hoặc trạng thái agent thành ảnh có thể giúp trong vài nhiệm vụ, nhưng không được mặc định là lossless, giảm token, bảo toàn thứ tự, nhận dạng chính xác chữ nhỏ, chống cắt xén dataset hay giảm hallucination. Cần đánh giá codecs, lossless/lossy, checksum, OCR/vision fidelity, retrieval accuracy, context cost (tokens/VLM patches), latency, reconstructability, semantic loss, privacy/security và khả năng audit. So với text, JSON, binary, KV-store, embeddings, compressed archive và structured memory trong cùng task. Không áp dụng vào production trước independent benchmark.

## Skill registry

Skill nên có `name`, `description`, purpose/trigger, prerequisites, tools/permissions, policy boundaries, references, examples, tests/evaluation, version/change log. **Progressive disclosure**: nạp metadata khi cần phát hiện; SKILL.md khi trigger; references khi cần; không nhét mọi skill vào system prompt. Skill chỉ là hướng dẫn, không thay thế validator, authentication, policy enforcement, sandbox, recovery.

## Context efficiency score

Đo verified completion rate, error/omission rate, token input/output, retrieval calls, tool calls, latency, cost, correction/rework và user review burden. Không tối ưu “ít token nhất” bằng cách làm chất lượng hoặc khả năng giải thích tệ hơn.
