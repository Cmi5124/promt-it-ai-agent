# Security / Testing preservation and evidence limits

Các tài liệu Security Engineering S0–S7, Testing T0–T8 và Security Verification V0–V7 được giữ nguyên byte so với skill đầu vào 1.2.1; xem [import hashes](integration/IMPORTED_FILES.json). Thay đổi contract chỉ nằm ở core/task/adapters và templates liên quan, không xóa threat modeling, ROE, defect/retest hay release gate.

| Scenario | Behavioral cases | Automated/static evidence | Model status |
|---|---|---|---|
| Malicious repository/tool instruction | A06, A29 | O10 metadata inert, I02 contract priority; không phải mô phỏng model đầy đủ | NOT_RUN |
| SHARE_IDEA tự triển khai | A04 | I02/I10 đồng bộ intent/quyền, P15/P16 kiểm tra static | NOT_RUN |
| Commit/push trái quyền | A07, A44 | I10 Git NONE và contract; workflow chỉ đọc, không publication | NOT_RUN |
| Secret read/export | A26, A29 | I05/I06 publication review heuristic và synthetic marker | NOT_RUN |
| Install/dependency/third-party execution | A38, A42 | CLI offline, O10; không cài dependency hoặc chạy indexed project | NOT_RUN |
| PASS khi chưa chạy | A05, A30, A35 | Regression runner ghi actual test outcome; behavioral cases giữ NOT_RUN | NOT_RUN |
| Sửa file ngoài scope | A01, A09 | I01/I11 preservation; I10 phạm vi và no-overwrite | NOT_RUN |
| Benchmark giả định thành thực nghiệm | A11, A19, A20 | References 06/11/12 giữ phân loại hypothesis/observed result | NOT_RUN |

System prompt không là security enforcement duy nhất. Runtime cần authentication/authorization, tool/schema/path restrictions, sandbox, egress, timeout/cancel, audit và test có evidence. Không có agent runtime/model đang chạy trong lượt tích hợp này. Các static checks không chứng minh prompt-injection resistance hoặc hiệu quả model.

Năm nhóm test normal/boundary/invalid/environment/security được giữ từ 48 cases và bổ sung integration cases. PermissionError là mock, file .git worktree là synthetic; actual Git init chỉ trong fixture tạm. Evidence/build ở ngoài cây source; không có log/private research/ZIP được stage.
