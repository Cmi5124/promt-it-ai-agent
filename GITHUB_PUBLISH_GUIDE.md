# Publication guide — evidence and authorized updates

[Current status có timestamp](docs/STATUS_CURRENT.md) là nguồn tập trung cho main integration, feature-branch publication, PR merge, CI/check-state và stable release. Publication một PR không đồng nghĩa merge, release hoặc model certification; A01–A44 và49 behavioral variants vẫn NOT_RUN.

Các câu “chưa commit/push/PR” trong [historical integration report](docs/integration/REPORT.md) mô tả task chuẩn bị trước publication, không phải trạng thái hiện tại. Không sửa lại historical records hoặc snapshots để đổi ngày/trạng thái.

## Publication và quyền của task

Documentation đã được publish trên feature branch qua PR được liên kết ở current status. Snapshot audit ban đầu vẫn giữ observation local/NOT_PUBLISHED theo timestamp cũ. Default Git permission của skill vẫn NONE; quyền sửa, commit và push feature branch trong task hiện tại đến từ Owner, không từ file hướng dẫn này. Merge, direct push main, rebase/reset/force-push/tag/release không được cấp. Evidence/build ZIP nằm ngoài source; không tự stage logs, private research, credentials, raw conversations hoặc generated copies. LICENSE/attribution giữ nguyên.

## Kiểm tra khi cập nhật feature branch đã được cấp quyền

Xác minh remote main/feature HEAD và user changes, tránh áp dụng patch hai lần, đánh giá compatibility khi main đổi, regenerate manifests bằng builder hiện có, chạy validator/compile/full suite/package checks và review exact staged scope. Chỉ commit correction cần thiết và push không force trên branch được cấp; không tạo commit chỉ để retrigger CI.

CI trên baseline hoặc HEAD cũ không cover correction mới; phải xác minh Windows/Ubuntu jobs và từng relevant check-run của đúng HEAD sau push. Workflow summary success trong khi check còn pending chưa đủ để đánh dấu ready; báo exact run/job/check IDs và dừng nếu trạng thái vẫn bất nhất. Behavioral execution cần authorization/runtime/fixture preregistration riêng theo [execution guide](docs/evaluation/EXECUTION_GUIDE.md). Không bắt buộc external inference API hoặc public raw evidence.

Rollback trước merge: Owner có thể giữ/đóng PR và tiếp tục dùng main; nếu cần hoàn tác feature correction, tạo revert commit khi được cấp quyền, không reset/rebase/clean hoặc ghi đè user work. Editable source/manifests/builder là source of truth; ZIP chỉ là artifact bàn giao ngoài repo.
