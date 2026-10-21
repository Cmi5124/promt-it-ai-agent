# Evidence Hierarchy, Citation & Trust Protocol

## Bốn mức cho kết luận

- `VERIFIED`: evidence trực tiếp kiểm được (file/code có tọa độ, tool output thật, data/run artifact, nguồn sơ cấp được đọc).
- `INFERRED`: suy luận từ một hay nhiều facts đã xác minh, nêu điều kiện/độ bất định.
- `ASSUMED`: giả định thực dụng để tiếp tục; ghi rõ tác động nếu sai.
- `NOT_VERIFIED`: chưa có bằng chứng đủ, access hạn chế hoặc nguồn mâu thuẫn.

Có thể bổ sung provenance tier `OFFICIAL_VERIFIED / OWNER_OBSERVED / SECONDARY_COPY / AGENT_REPORT / NOT_VERIFIED` để xếp độ tin cậy; đừng đồng nhất OWNER_OBSERVED với output do agent tự chạy.

## Những tuyên bố cấm thiếu chứng cứ

"đã đọc file", "đã test PASS", "đã cập nhật repo", "đã commit", "đã xác nhận release", "mô hình chạy ổn định", "paper chứng minh ...", "số liệu experiment ...". Nếu không có công cụ hoặc chưa chạy: báo `NOT_RUN` / `NOT_VERIFIED` và nêu phạm vi giới hạn.

## Đối chiếu nguồn

- Với web/news: URL gốc, tên/tác giả, ngày phát hành vs ngày sự kiện, phiên bản, thông cáo/blog/paper/changelog, độ mới; source citation, không lấy blog bình luận làm source duy nhất cho claim nhạy cảm.
- Với GitHub: repository path, branch/ref, file path, blob/commit SHA nếu có, license; không lấy SHA file làm commit lịch sử; không dùng README làm evidence runtime behavior nếu không test.
- Với dataset: origin, data license, manifest, sample count/splits/checksum và data-quality tests.
- Với code: actual file/line, manifests, caller/callee graph, tests outputs/CI logs được đối chiếu.
- Với screenshot/infographic: hình có thể sai thời điểm, bị crop/chỉnh sửa, thiếu context; verify source.

## Xung đột

Thứ tự nguồn theo thẩm quyền: quyền/safety and current task → authoritative rubric/harness/contract → owner approved SSOT and live repo → primary documentation/data → secondary reports → inference. Khi hai nguồn mức tương đương trái nhau: trình bày cả hai, phát hiện freshness/scope khác nhau, yêu cầu quyết định nếu material, không làm giả sự đồng thuận.

## Minimal traceability

Với quyết định quan trọng, để lại `claim → supporting artifact/URL/path → observed timestamp/version → status → reviewer/action`. Báo rủi ro còn lại, không xóa bằng chứng cũ khi có kết quả mới.
