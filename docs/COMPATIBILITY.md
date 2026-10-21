# Version compatibility

| Component | Version | State | Compatibility |
|---|---|---|---|
| Repository upstream baseline | 1.0.0 | released baseline commit 58af404bec934cd4a3849102a0a533e9086b57d0 | Không sửa remote/history |
| Repository/core/compact integration | 1.1.0 | candidate, chưa tag/release | Chỉ contract clarification và bổ sung skill; baseline archived |
| Adaptive skill | 1.2.1 | imported with integration contract/legal metadata | Canonical skills/adaptive-project-ops; standalone có manifest/LICENSE/notices riêng |
| Immutable full snapshot | 1.0.0 | [v1.0.0](../versions/v1.0.0.md) | Byte-identical upstream blob |
| Archived compact | 1.0.0 | [compact](../versions/v1.0.0-compact.md) | Byte-identical; frozen full alias chỉ để giữ relative link gốc |
| ChatGPT/Codex/Gemma behavior | NOT_VERIFIED | A01–A44 NOT_RUN | Cần model/runtime eval, không suy PASS từ static checks |

Python syntax/unit results ghi theo môi trường thực sự chạy. Windows và Ubuntu được mô tả trong CI; không nhận CI PASS trước khi có Actions run. Root manifest version phản ánh skill/package 1.2.1, repository_version và prompt_version phản ánh candidate 1.1.0 riêng.
