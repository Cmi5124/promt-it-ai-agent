# AI / LLM / RAG / Agent Engineering

## Tách lớp để tránh metric sai

- **Model-only:** accuracy/quality/instruction adherence/factuality/reasoning/safety không có tool ngoài.
- **Tool-assisted:** tool selection, argument validity, retrieval quality, permission enforcement, idempotency, tool-failure recovery.
- **Full agent/system:** task completion, successful verified patches/transactions, latency, resource, cost, security/containment, long-horizon reliability.

Không so sánh model-only với model+harness như benchmark tương đương.

## Retrieval và context

- RAG, HybridRAG và GraphRAG là những **phương án bổ sung/có tradeoffs**, không quy luật tiến hóa tất yếu thay nhau. Eval retrieval độc lập generation.
- Retrieval: Recall@K, Precision@K, MRR, nDCG, reranker lift, latency, coverage, permission correctness.
- Generation: groundedness, faithfulness, answerability/evidence sufficiency, citation correctness/completeness, unsupported claim rate, abstention/refusal quality.
- Kiểm soát provenance, index/version, document ACL, temporal validity, stale memory, chunk boundary, duplicate and injection defense. Một đoạn liên quan chưa chắc đủ evidence trả lời câu hỏi.

## Agent design

Tách planning/reasoning, session/context, execution/tools và durable state. Có manifest và tool schema, read/write boundaries, approval checkpoints, sandbox, retry budget, timeout, cancellation, checkpoint/recovery, audit. Agent không có quyền chỉ vì tự nói có quyền. Loop detection và human escalation khi kết quả không chắc chắn. MCP/interoperability là adapter, không vượt auth/tenant policy.

## Model & inference

Đánh giá model/model family theo license, dataset/legal provenance, context/use cases, quantization, VRAM, latency, TTFT, TPOT, throughput/concurrency, prompt length, multi-GPU interconnect và failure mode. Có regression + adversarial suite; không dùng một leaderboard hay LLM judge làm bằng chứng duy nhất.

## Tối ưu hiệu quả

Đo `verified_task_success / (tokens, tool calls, elapsed time, money, user correction, rework)` và quality-regression. Compression, caching, speculative decoding, model routing, distilled verifier, MoE, graph memory, agent tool retry đều là candidate tùy environment và benchmark. Không gắn cloud API là dependency nếu profile dự án cấm; vẫn có thể nghiên cứu tài liệu ngoại vi khi được phép.
