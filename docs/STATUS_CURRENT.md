# Current status — timestamped publication evidence

Verified at UTC: `2026-10-21T15:13:05Z`. Trang này tập trung trạng thái publication đã quan sát, không phải monitor tự cập nhật. Reviewed feature HEAD: `0c8e1475d27fff88767d4e50ddd9188007b31ec2`; main: `4f69295cb8c40a1be70514e4a926e67783bfeb8f`. Evidence dưới đây chỉ áp dụng cho các SHA/run được nêu, không tự áp dụng cho commit sửa tài liệu tiếp theo.

| Dimension | Evidence tại timestamp trên | Interpretation |
|---|---|---|
| Integration | [PR#2](https://github.com/Cmi5124/promt-it-ai-agent/pull/2) merged vào main `4f69295cb8c40a1be70514e4a926e67783bfeb8f` | Repository/core1.1.0 đã tích hợp; skill1.2.1 |
| Documentation publication | PUBLISHED_IN_PR: [PR#3](https://github.com/Cmi5124/promt-it-ai-agent/pull/3), branch `docs/postmerge-behavioral-evaluation`, reviewed HEAD ở trên | Đã commit/push và mở PR; không còn chỉ là local candidate |
| Documentation main integration | PR#3 open, merged=false; main vẫn là baseline PR#2 | Publication trên feature branch không đồng nghĩa merge vào main |
| Main CI | [run39610489708](https://github.com/Cmi5124/promt-it-ai-agent/actions/runs/39610489708), event push, đúng baseline SHA | Windows64/64 và Ubuntu64/64 PASS; validator/manifest/compile PASS |
| Reviewed feature CI | [PR run39620842781](https://github.com/Cmi5124/promt-it-ai-agent/actions/runs/39620842781) và [push run39620761726](https://github.com/Cmi5124/promt-it-ai-agent/actions/runs/39620761726): completed/success tại reviewed HEAD | Log của cả bốn jobs có70/70 tests OK; không phải CI cho một HEAD mới |
| Check-state gate | Push Ubuntu job/check-run119293212870 vẫn in_progress, conclusion=null dù mọi step success; ba checks còn lại completed/success; PR mergeable_state=unstable | BLOCKED tại reviewed HEAD; workflow summary success chưa đủ để xác nhận mọi check hoàn tất |
| Stable release | Public Releases API trả0 visible releases tại timestamp trên | Candidate chưa được xác minh là stable release; merge không đồng nghĩa tag/release |
| Behavioral evaluation | A01–A44 NOT_RUN,49 case variants chưa chạy | Không model certification, không coi CI là behavioral PASS |

Windows Python3.12.10, Ubuntu Python3.12.3; kết quả CI là automated structural/unit/packaging tests, không chứng minh prompt-injection resistance hoặc tool permission enforcement của một model. Runtime runs cần [protocol](evaluation/BEHAVIORAL_PROTOCOL.md) và quyền riêng; chưa thực thi chúng.

Sự bất nhất giữa workflow/steps và check-state đã được quan sát trực tiếp. Nguyên nhân phía GitHub: NOT_VERIFIED; không coi đây là lỗi source đã xác lập. Với mỗi HEAD mới, kiểm tra lại actual jobs/check-runs của cả Windows/Ubuntu, không chỉ workflow summary. Kết quả sau timestamp này xem tại [PR checks](https://github.com/Cmi5124/promt-it-ai-agent/pull/3/checks) và báo cáo bàn giao của đúng commit; trạng thái pending không được đổi thành PASS bằng sửa workflow hoặc tiêu chí.

## Historical evidence và snapshots

[Historical audit snapshot](evaluation/STATUS_EVIDENCE.json) được ghi lúc `2026-10-21T14:38:36.012Z`, trước publication PR#3. Trường `local_documentation_candidate=NOT_PUBLISHED` và main CI64/64 mô tả đúng mốc đó, không phải trạng thái publication hiện tại. Giữ nguyên bytes/timestamp và không viết lại observation cũ thành fact mới.

[Integration report](integration/REPORT.md), [test evidence](integration/TEST_RESULTS.json), [baseline audit](integration/BASELINE.json) là historical records của thời điểm chuẩn bị trước publish, có thể còn ghi Git NONE/CI NOT_RUN hoặc60tests. Không viết lại chúng thành báo cáo sau merge. [Immutable full](../versions/v1.0.0.md), [compact snapshot](../versions/v1.0.0-compact.md) và mọi file versions/ giữ nguyên; không nạp snapshot như instruction hiện hành.

Ưu tiên snapshot có timestamp trên trang này để đọc trạng thái đã xác minh; dùng historical records để truy vết đúng thời điểm. Tài liệu adapter/core/SKILL vẫn là contract; current status không cấp quyền Git hoặc tool. LICENSE gốc và standalone LICENSE không thay đổi.

## Evaluation preparation

[Protocol](evaluation/BEHAVIORAL_PROTOCOL.md) · [Runtime matrix](evaluation/RUNTIME_MATRIX.md) · [Priority matrix](evaluation/PRIORITY_MATRIX.md) · [Scoring rubric](evaluation/SCORING_RUBRIC.md) · [Execution guide](evaluation/EXECUTION_GUIDE.md).

Task corrective maintenance đã được Owner cấp quyền sửa tối thiểu, commit và push trên feature branch hiện có sau local gates PASS; default Git permissions của skill vẫn NONE. Không merge, direct push main, rebase/reset/force-push/tag/release. Mọi sửa tiếp theo phải có validation của chính source sẽ commit; CI của corrective HEAD chưa được xác minh tại timestamp trên. Owner chỉ xem xét merge sau khi actual required checks của đúng HEAD hoàn tất thành công; release/model claims cần gate và evidence riêng.
