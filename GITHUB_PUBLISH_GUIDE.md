# Publication guide — Owner review first

Chưa commit/push/PR/tag/release. Candidate branch đề xuất: feat/adaptive-agent-skill-pack-v1.2.1, chưa tạo. Kiểm tra [contract](docs/INSTRUCTION_CONTRACT.md), [compatibility](docs/COMPATIBILITY.md), [provenance](docs/adaptive/PROVENANCE.md), [CI](docs/CI.md) và kết quả integration trước khi cấp quyền publish riêng.

Editable source và reproducible builder là source of truth; không đưa ZIP, raw logs, private research/history, credentials hay local generated discovery copies vào Git history. LICENSE gốc giữ nguyên; owned imported content áp dụng Apache-2.0 theo Owner, external references giữ rights riêng.

Sau khi Owner cấp quyền Git trong một task riêng, có thể thực hiện tuần tự các lệnh sau từ checkout đúng baseline. Đây là đề xuất, KHÔNG được chạy trong task integration hiện tại:

```text
git status --short
git diff --check
git switch -c feat/adaptive-agent-skill-pack-v1.2.1
git diff
git add --patch
git diff --cached --stat
git diff --cached --check
git commit -m "feat: integrate adaptive agent skill pack v1.2.1"
git push -u origin feat/adaptive-agent-skill-pack-v1.2.1
```

Chọn thêm từng file mới đã review; tránh git add . để không stage artifacts. Không push trực tiếp main. PR/merge/tag/release cần scope/quyền riêng và CI evidence thực. Rollback trước publish là bỏ bản candidate riêng và tiếp tục dùng baseline; không cần reset/clean/history rewrite.
