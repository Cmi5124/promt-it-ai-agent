# Multimodal Perception, Image/Data Representation & Encoding

## Phân biệt input, dữ liệu và biểu diễn

Image/text/audio/video/3D/sensor logs có biểu diễn và loss model khác nhau. Format JPEG/PNG/WebP/AVIF/HEIF/TIFF, video codecs, binary blocks, vector/graph, text/JSON và structured image containers cần được chọn theo use case: lossy/lossless, metadata, compression, compatibility, decoder availability, annotation accuracy và provenance. Không mặc định một extension tốt nhất.

## Image as data container: research gate

Candidate nghiên cứu: phân lớp dữ liệu thành `raw payload`, `structural metadata`, `semantic index` (có thể đồng thời 3 lớp), checksums/signatures, redundancy/error detection, tamper/crop detection, chunking, region-of-interest access, versioned sidecar metadata. Phải chứng minh recovery và data integrity bằng phép thử; checksum chỉ phát hiện thay đổi chứ không tự phục hồi nội dung đã cắt. Không khẳng định ảnh chống cắt xén/truncation nếu chưa có error-control redundancy/recovery thực nghiệm.

## Cách đánh giá

- **Fidelity:** byte-perfect? pixel-perfect? semantic-equivalent? WER/CER cho text; PSNR/SSIM/LPIPS cho ảnh theo trường hợp; task performance cho VLM.
- **Information integrity:** hash, crop/truncation robustness, region order, metadata preservation, round-trip decode, partial recovery, corruption/failure modes.
- **Resource:** storage bytes, preprocessing cost, memory/VRAM, tokens per image patches, context window impact, encode/decode latency, throughput.
- **Security & privacy:** EXIF/PII leak, steganographic content, malicious metadata, prompt injection in images, oversized/poisoned files, parser vulnerabilities.
- **Compatibility:** accessibility, searchable text, annotation toolchains, model-specific image preprocessing, versioning and rollback.

## Vision & Spatial

Tách detection, segmentation, tracking, depth, reconstruction, 3D scene graphs, temporal alignment, AR/MR interaction. Tính khả thi phụ thuộc datasets, geometry accuracy, FPS hardware budget, calibration, online/offline constraints; benchmark theo task, không suy chức năng từ ảnh demo. Nếu nghiên cứu agent memory bằng ảnh, kết hợp `08-context-memory-skills.md` với nghiên cứu này; mặc định **NOT_VERIFIED** về mức cải thiện.
