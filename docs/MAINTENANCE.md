# Maintenance

Sửa canonical skill trong skills/adaptive-project-ops, templates authoring trong root templates/, adapters trong integrations/adaptive. Không sửa bản copy assets/templates thủ công. --prepare đồng bộ copy và tạo hai manifests; validator không tự chữa hash lỗi. Chạy validate_repository, toàn suite và build reproducibility sau khi sửa.

Không đổi snapshot versions/v1.0.0.md hoặc LICENSE gốc. Core/compact hiện hành chỉ sửa khi Owner/task cho phép, đồng bộ TEST_ONLY/precedence trong các runtime và regression tests. Không gọi 48/48 baseline là PASS của integration; chạy lại và lưu evidence ngoài repo.

Artifact lifecycle: chọn thư mục tạm mới hoặc ignored path được cấp, không overwrite; tách fixture/cache khỏi sản phẩm; giữ log theo retention, cleanup chỉ dưới quyền đã cấp. Không đưa log máy cá nhân, raw conversation, research cá nhân hoặc ZIP vào source publish. Dữ liệu index bên ngoài không được vendor tự động.
