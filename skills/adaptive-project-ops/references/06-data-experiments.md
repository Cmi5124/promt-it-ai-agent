# Data Engineering, Dataset Governance và Scientific Experiments

## Dataset lifecycle

`SOURCE → LICENSE/CONSENT → INGEST → VALIDATE → NORMALIZE → DEDUP → SPLIT → FEATURE/ANNOTATION → TRAIN/EVAL → LINEAGE/RETENTION`. Kiểm tra dữ liệu nhạy cảm/PII, provenance, rights, quality, class imbalance, schema, encoding, missing/duplicate, corruption, label noise, edge cases, version. Không xem file là dataset hợp lệ chỉ vì đã download.

- Phân biệt nguồn gốc và train/validation/test partitions; group/time-disjoint khi domain cần. Chống leakage, temporal look-ahead, duplicated near-identical samples, benchmark contamination.
- Training features chỉ được sử dụng thông tin có tại thời điểm dự đoán; label tương lai nằm riêng. Điều này đặc biệt quan trọng với time-series, financial analytics, predictive maintenance.
- Với image/video/audio/text: giữ origin, license, transform chain, label/mask/bbox/timecode, split, checksum, annotation quality và khả năng trace ngược.
- Pipeline: idempotency, checkpoint, retry/backoff, DLQ, data integrity, validation, cancellation, lineage and replay; DB source-of-truth xác định rõ, cache/queue không tự động là truth.

## Experiment protocol

Mỗi thử nghiệm: `Research ID (R) | question | hypothesis | baseline | candidate | independent variables | fixed variables | dataset/split | metrics | environment | resources | seed | procedure | artifacts | observed result | failure analysis | decision`.

- Đo first viable baseline trước khi tăng complexity.
- Dùng version immutable, append-only logs, reproduce config/data/eval, không ghi đè failure; nếu thay đổi protocol thì không so sánh điểm như cùng benchmark.
- Phân tích lỗi theo lớp/nhóm, false positives/negatives, confusion patterns; nếu có OOF predictions thì lưu cùng split và version; tránh optimize dựa riêng leaderboard public.
- Tách `NOT_RUN`, `BLOCKED`, `FAIL`, `PASS`; research hypothesis không được nâng thành production claim trước independent validation.
- Kế hoạch cost/compute/memory/energy/time; nếu dataset/model quá lớn thì lập feasibility và staged eval, không tự hứa train thành công.

## Pretrain / Fine-tune / RAG choices

Quyết định dựa trên mục tiêu, quality/size/licenses của dữ liệu, token budget, compute, evaluation gap, target latency và maintainability. Không có một số lượng token/tokenizer/architecture universal hợp lệ cho mọi model. So sánh from-scratch, PEFT/QLoRA, adaptation, retrieval/tooling công bằng bằng cùng protocol, ghi rõ giới hạn.

## Reproducibility manifests

Artifact nên có dataset manifest, code SHA, split IDs, configs, runtime versions, GPU, seed, metrics, raw output, error logs, license notes, approval. Không xuất hiện kết quả giả hay metric “ước lượng” dưới nhãn thực nghiệm.
