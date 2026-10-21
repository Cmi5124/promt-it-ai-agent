# Hardware / Compute / Inference / Capacity Analysis

## Nguyên tắc

Không đánh đồng tổng VRAM nhiều GPU với một pool VRAM liên tục hoặc với năng lực chạy model tự nhiên. Xác minh model architecture (dense/MoE, active params), weights format, quantization, KV cache, activations, context length, concurrency, framework/driver/kernels, GPU topology, interconnect/PCIe, RAM/offload và memory fragmentation. Tách **fit model weights**, **load thành công**, **chạy inference**, **throughput/latency ổn định**, **training/fine-tuning**; không suy từ bước trước sang bước sau.

## Feasibility model

Estimate: weights bytes (parameter count × actual bits/param + overhead), KV cache/context, runtime buffers, output tokens, batch/concurrency, OS/process memory. Với multi-GPU: tensor/pipeline parallel, communication overhead và supported runtimes; với GPU cũ: instruction set, framework support, attention kernels, fp16/bf16/quant formats. Xác minh thông số thiết bị với nguồn hiện hành; giá là biến động, gắn ngày/nơi bán và điều kiện hàng.

## Benchmark protocol

Measure quality-regression, TTFT, TPOT, tokens/s, end-to-end latency, prefilling, decode, peak VRAM/RAM, GPU utilization, power, error/timeout/OOM rate, concurrency, serving stability, tool latency. Test prompt lengths realistic + high-context; warm/cold cache; reproducibility and tolerance. Không lấy benchmark marketing làm kết quả máy mình.

## Optimization candidates

Quantization, CPU offload, speculative decoding, continuous batching, prefix/KV cache, paged attention, compiler/kernels, model routing, small verified classifiers, storage architecture, heterogeneous compute. Mỗi candidate cần matrix `quality × memory × latency × throughput × portability × operational risk × cost`. Cloud/external compute chỉ là phương án nếu project permission và ngân sách cho phép; không bắt buộc production external inference.
