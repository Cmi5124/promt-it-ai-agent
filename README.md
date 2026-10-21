# Promt IT(AI/Agent)

Promt IT(AI/Agent) là bộ quy tắc vận hành công khai cho ChatGPT và Codex khi xử lý công việc IT, code và AI Agent. Bộ quy tắc giúp yêu cầu được phân tích theo bằng chứng, giới hạn đúng phạm vi thay đổi, và báo cáo rõ phần đã hoặc chưa được kiểm chứng.

Nó không phải công cụ bảo mật tuyệt đối và không thay thế review, kiểm thử hoặc phê duyệt của con người.

## Nội dung

- [Bản đầy đủ](PROMT-IT-AI-AGENT.md): quy tắc áp dụng cho phân tích, lập kế hoạch, triển khai, review, test, bảo mật, AI/LLM/RAG/Agent và release.
- [Bản compact](PROMT-IT-AI-AGENT-COMPACT.md): bản ngắn để copy trực tiếp vào conversation.
- [Hướng dẫn ChatGPT](integrations/CHATGPT-USAGE.md) và [hướng dẫn Codex](integrations/CODEX-USAGE.md).
- [Mẫu AGENTS.md](integrations/AGENTS.example.md) và năm [task template](templates/).
- [Snapshot v1.0.0](versions/v1.0.0.md) và [lịch sử phiên bản](CHANGELOG.md).

## Cách dùng

### ChatGPT Web/App

1. Mở file Markdown hoặc bản raw mà bạn thực sự có thể truy cập.
2. Copy bản đầy đủ hoặc compact vào đầu conversation hay project instruction phù hợp.
3. Gửi một task template đã điền phạm vi, tiêu chí chấp nhận và quyền Git.
4. Nếu dùng link, yêu cầu ChatGPT xác nhận đã đọc được nội dung. Nếu không truy cập được, dán trực tiếp nội dung prompt.

Không giả định nền tảng tự đọc được URL khi nội dung chưa được xác nhận là đã truy cập.

### Codex Web/App

1. Chọn đúng repository rồi kiểm tra branch và worktree.
2. Đưa prompt vào conversation hoặc lưu một bản local trong repository.
3. Có thể dùng `AGENTS.md` để áp dụng quy tắc trong repository; ưu tiên tham chiếu file local hơn phụ thuộc hoàn toàn vào URL remote.
4. Nêu mode và quyền Git cho từng task. Commit hoặc push không được mặc định cho phép.

## Khi nào dùng bản nào

Dùng bản đầy đủ khi task có thay đổi code, rủi ro, nhiều dependency hoặc cần release assessment. Dùng bản compact khi cần khởi tạo nhanh conversation, sau đó bổ sung yêu cầu cụ thể bằng template. Bản compact tự sử dụng được nhưng không thay thế các bằng chứng cần thu thập trong repository.

## Versioning

Dự án dùng semantic versioning:

- **MAJOR**: đổi nguyên tắc hoặc hành vi không tương thích.
- **MINOR**: thêm nhóm quy tắc mới.
- **PATCH**: sửa diễn đạt hoặc làm rõ mà không đổi hành vi.

## Cấu trúc repository

| Đường dẫn | Mục đích |
| --- | --- |
| `PROMT-IT-AI-AGENT.md` | Bản quy tắc đầy đủ hiện hành. |
| `PROMT-IT-AI-AGENT-COMPACT.md` | Bản ngắn, tự sử dụng được. |
| `integrations/` | Cách áp dụng với ChatGPT, Codex và mẫu AGENTS.md. |
| `templates/` | Mẫu cho năm mode làm việc. |
| `versions/` | Snapshot bất biến theo từng version phát hành. |
| `CHANGELOG.md` | Lịch sử phiên bản của bộ prompt; không phải yêu cầu bắt buộc của Apache License 2.0. |

## Giới hạn

- Prompt không thay thế review của con người.
- Khả năng thực thi phụ thuộc vào nền tảng, model, quyền và môi trường thực tế.
- Agent có thể không truy cập được repository, URL, shell hoặc Git.
- Mọi kết quả cần được kiểm chứng; prompt không tự cấp quyền và không biến output chưa chạy thành bằng chứng thực tế.

## License

Project được phát hành theo [Apache License 2.0](LICENSE). File `LICENSE` là nguồn quy định giấy phép; repository không tạo thêm giấy phép hay `NOTICE` mới.

## Framework integration candidate — repository 1.1.0 / skill 1.2.1

Bổ sung khả năng điều phối đa dự án, không khóa vào một sản phẩm. Repository 1.1.0 là candidate chưa phát hành; core prompt được đồng bộ contract ở 1.1.0 candidate, skill vẫn là 1.2.1. Bản đầy đủ, compact và snapshot v1.0.0 được lưu theo [compatibility matrix](docs/COMPATIBILITY.md).

- [Cài và dùng skill](docs/INSTALLATION.md), [usage ba runtime](integrations/ADAPTIVE-USAGE.md), [contract](docs/INSTRUCTION_CONTRACT.md).
- [Skill canonical](skills/adaptive-project-ops/SKILL.md), [Security Engineering S0–S7](skills/adaptive-project-ops/references/17-security-engineering.md), [Test Engineering T0–T8](skills/adaptive-project-ops/references/18-test-engineering.md), [Security Verification V0–V7](skills/adaptive-project-ops/references/19-security-verification.md).
- [Conflict matrix](docs/CONFLICT_MATRIX.md), [public provenance](docs/adaptive/PROVENANCE.md), [third-party notices](THIRD_PARTY_NOTICES.md), [bảo trì](docs/MAINTENANCE.md), [CI](docs/CI.md), [publication guide](GITHUB_PUBLISH_GUIDE.md).

Canonical skill source là skills/adaptive-project-ops. Các template nghiệp vụ có một nguồn authoring tại templates/; builder copy đúng mười file được tham chiếu vào assets của skill, validator kiểm tra byte equality. Không sửa bản copy thủ công. Scripts và tests root dùng đường dẫn canonical skills; standalone không phụ thuộc repo root hoặc symlink.

```text
python scripts/validate_repository.py
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/run_regressions.py --output-dir ../integration-evidence
python scripts/build_release.py --output-dir ../integration-build
```

Chỉ chạy --prepare sau khi review thay đổi source; lệnh này tái tạo manifests, không chứng minh test PASS. Output đã tồn tại bị từ chối. CI trên GitHub chưa được thực thi chỉ vì có workflow local.
