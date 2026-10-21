# Repository / skill comparison and conflict matrix

Owner đã phê duyệt contract tích hợp và Apache-2.0 cho owned content; Git permissions của task tích hợp vẫn NONE.

| Dimension | Existing repository 1.0.0 | Skill 1.2.1 | Classification | Integration decision |
|---|---|---|---|---|
| Operating modes | ANALYZE/PLAN/IMPLEMENT/REVIEW/TEST | Cùng modes, thêm SHARE_IDEA intent | SAME + COMPLEMENTARY | Giữ mode; SHARE_IDEA không cấp quyền |
| Evidence | VERIFIED/INFERRED/ASSUMED/NOT_VERIFIED | Cùng nhãn và run states | SAME | Không PASS khi chưa chạy |
| Security | Injection/auth/secret/least privilege | S0–S7, threats, V0–V7, ROE | COMPLEMENTARY | Giữ mọi lifecycle/control; prompt không là enforcement duy nhất |
| Testing | Five groups; TEST_ONLY template cấm tạo thay đổi | T0–T8, fixture/cache/evidence có quyền | CONFLICT resolved by Owner | Chỉ cho artifact trong scope/path, lifecycle rõ; cấm source/prod/user-data writes và overwrite |
| Project management | Scope/impact/approval | SSOT/sprint/research/portfolio | COMPLEMENTARY | Domain reference theo nhu cầu, không tạo project tự động |
| AI/Agent | Metrics/guardrails/tools | Model/tool/system split, memory/retrieval | COMPLEMENTARY | Không bịa tool; runtime thực thi và enforce quyền |
| Skill routing | Chưa có skill folder | Router 21 references | COMPLEMENTARY | Canonical skills/adaptive-project-ops, không tự nạp task không liên quan |
| Git permissions | Explicit per task | File permission không cấp Git | SAME | NONE mặc định, không commit/push/PR/tag/release trong task hiện tại |
| Implementation approval | CODEX-USAGE yêu cầu plan/scope duyệt trước | Yêu cầu đủ scope/quyền có thể cấp ngay | CONFLICT resolved by Owner | Request IMPLEMENT hiện tại là phê duyệt scope; không hỏi lại cùng quyền |
| Release gates | READY/READY_WITH_RISKS/BLOCKED/NOT_VERIFIED | Cùng gate + evidence matrix | SAME + COMPLEMENTARY | Technical pass không suy publication permission/CI/model PASS |
| Precedence | Repo contract + actual permission | Core/domain/template guidance | COMPLEMENTARY | Runtime → Owner task → repo → core skill → domain → examples; archive không active |

Không có rule bị đánh dấu DEPRECATED hoặc bị xóa ngầm. UNKNOWN còn lại là model/runtime behavior, native OS chưa chạy và actual GitHub Actions. Khi phát sinh conflict mới thay đổi scope/security/architecture/quyền hoặc nguy cơ mất dữ liệu, dừng phần đó và hỏi Owner.
