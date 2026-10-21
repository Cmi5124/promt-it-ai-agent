# Publication guide — current baseline and next authorized step

[Current status](docs/STATUS_CURRENT.md): PR#2 đã merge vào main4f69295cb8c40a1be70514e4a926e67783bfeb8f; feature branch integration đã được tạo/push trước đó. Main CI Windows/Ubuntu64/64 đã xác minh. Integration1.1.0 vẫn candidate chưa được xác minh stable release; A01–A44 NOT_RUN.

Các câu “chưa commit/push/PR” trong [historical integration report](docs/integration/REPORT.md) mô tả task chuẩn bị trước publication, không phải trạng thái hiện tại. Không sửa lại historical records hoặc snapshots để đổi ngày/trạng thái.

## Local documentation candidate — Git permissions NONE

Revision docs/evaluation hiện chỉ là local patch/candidate. Task này không tạo branch, commit, push, PR, merge, tag/release hoặc đổi checkout main hiện hữu. Default permission của skill không thay đổi. Evidence/build ZIP nằm ngoài source; không tự stage logs, private research, credentials, raw conversations hoặc generated copies. LICENSE/attribution giữ nguyên.

## Proposal cho task publication sau

Owner cần cấp Git permissions riêng. Khi có quyền: xác minh remote main/baseline và user changes, review/apply đúng patch vào workspace phù hợp, reconcile khi main đổi, regenerate manifests bằng builder hiện có, chạy validator/full suite/docs checks và review exact staged scope. Có thể đề xuất branch docs/post-merge-behavioral-protocol cho task đó; chưa tạo branch này. Commit/push/PR phải có quyền; merge/tag/release là quyền riêng, không push trực tiếp main.

CI64 trên baseline không cover docs revision mới; cần actual Actions trên future PR trước claim CI PASS của patch. Behavioral execution cũng cần authorization/runtime/fixture preregistration riêng theo [execution guide](docs/evaluation/EXECUTION_GUIDE.md). Không bắt buộc external inference API hoặc public raw evidence.

Rollback local: bỏ qua candidate riêng và tiếp tục dùng main đã merge; không reset/rebase/clean main. Editable source/manifests/builder là source of truth; ZIP chỉ là artifact bàn giao ngoài repo.
