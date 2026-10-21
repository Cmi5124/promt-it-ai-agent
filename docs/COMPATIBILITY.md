# Version compatibility

| Component | Version | State | Compatibility |
|---|---|---|---|
| Repository upstream baseline | 1.0.0 | released baseline commit 58af404bec934cd4a3849102a0a533e9086b57d0 | Không sửa remote/history |
| Repository/core/compact integration | 1.1.0 | integrated main4f69295, candidate chưa stable release | Chỉ contract clarification và bổ sung skill; baseline archived |
| Adaptive skill | 1.2.1 | imported with integration contract/legal metadata | Canonical skills/adaptive-project-ops; standalone có manifest/LICENSE/notices riêng |
| Immutable full snapshot | 1.0.0 | [v1.0.0](../versions/v1.0.0.md) | Byte-identical upstream blob |
| Archived compact | 1.0.0 | [compact](../versions/v1.0.0-compact.md) | Byte-identical; frozen full alias chỉ để giữ relative link gốc |
| ChatGPT/Codex/Gemma behavior | NOT_VERIFIED | A01–A44 NOT_RUN | Cần model/runtime eval, không suy PASS từ static checks |

Main [CI run39610489708](https://github.com/Cmi5124/promt-it-ai-agent/actions/runs/39610489708) đã xác minh Windows Python3.12.10 và Ubuntu Python3.12.3 cùng64/64PASS tại baseline `4f69295cb8c40a1be70514e4a926e67783bfeb8f`. Local docs revision mới chưa có CI run; runtime/model behavior vẫn NOT_VERIFIED, A01–A44 NOT_RUN. Xem [current status](STATUS_CURRENT.md) và [runtime evaluation matrix](evaluation/RUNTIME_MATRIX.md). Root manifest version phản ánh skill/package 1.2.1, repository_version và prompt_version phản ánh candidate 1.1.0 riêng.
