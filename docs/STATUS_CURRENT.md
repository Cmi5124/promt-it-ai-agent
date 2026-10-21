# Current status — verified baseline and local documentation candidate

Baseline được kiểm tra: `4f69295cb8c40a1be70514e4a926e67783bfeb8f`. Nguồn machine-readable: [status evidence](evaluation/STATUS_EVIDENCE.json), kèm thời điểm audit UTC. Đây là snapshot trạng thái tại audit, không phải monitor tự cập nhật.

| Dimension | Current evidence | Interpretation |
|---|---|---|
| Integration | [PR#2](https://github.com/Cmi5124/promt-it-ai-agent/pull/2) merged vào main `4f69295cb8c40a1be70514e4a926e67783bfeb8f` | Repository/core1.1.0 đã tích hợp; skill1.2.1 |
| Main CI | [run39610489708](https://github.com/Cmi5124/promt-it-ai-agent/actions/runs/39610489708), event push, đúng baseline SHA | Windows64/64 và Ubuntu64/64 PASS; validator/manifest/compile PASS |
| Stable release | Public Releases API trả0 visible releases tại audit | Candidate chưa được xác minh là stable release; merge không đồng nghĩa tag/release |
| Behavioral evaluation | A01–A44 NOT_RUN,49 case variants chưa chạy | Không model certification, không coi CI là behavioral PASS |
| Documentation revision này | LOCAL_DOCUMENTATION_CANDIDATE, Git permissions NONE | Chưa publish; CI baseline64 không phải CI cho các file mới của revision này |

Windows Python3.12.10, Ubuntu Python3.12.3; kết quả CI là automated structural/unit/packaging tests, không chứng minh prompt-injection resistance hoặc tool permission enforcement của một model. Future runtime runs cần [protocol](evaluation/BEHAVIORAL_PROTOCOL.md) và quyền riêng; task chuẩn bị này không thực thi chúng.

## Historical evidence và snapshots

[Integration report](integration/REPORT.md), [test evidence](integration/TEST_RESULTS.json), [baseline audit](integration/BASELINE.json) là historical records của thời điểm chuẩn bị trước publish, có thể còn ghi Git NONE/CI NOT_RUN hoặc60tests. Không viết lại chúng thành báo cáo sau merge. [Immutable full](../versions/v1.0.0.md), [compact snapshot](../versions/v1.0.0-compact.md) và mọi file versions/ giữ nguyên; không nạp snapshot như instruction hiện hành.

Ưu tiên trang current này để đọc trạng thái hiện tại; dùng historical records để truy vết đúng thời điểm. Tài liệu adapter/core/SKILL vẫn là contract; current status không cấp quyền Git hoặc tool. LICENSE gốc và standalone LICENSE không thay đổi.

## Evaluation preparation

[Protocol](evaluation/BEHAVIORAL_PROTOCOL.md) · [Runtime matrix](evaluation/RUNTIME_MATRIX.md) · [Priority matrix](evaluation/PRIORITY_MATRIX.md) · [Scoring rubric](evaluation/SCORING_RUBRIC.md) · [Execution guide](evaluation/EXECUTION_GUIDE.md).

Chỉ propose publication sau review local patch, diff/scope, manifests và tests của chính revision mới. Không tạo branch/commit/push/PR/tag/release trong task Git NONE này. Release/model claims cần gate và evidence riêng.
