# Cài đặt và activation

Không có dependency ngoài Python standard library cho CLI/build/tests. Git cần cho regression metadata và real checkout fixtures; không tự cấp quyền Git trên repository sản phẩm. Không cần external inference API.

Canonical folder: [skills/adaptive-project-ops](../skills/adaptive-project-ops/). Copy nguyên folder gồm SKILL.md, references, assets/templates, scripts, manifest.json, LICENSE và notices vào nơi runtime thực sự hỗ trợ. Không chỉ copy SKILL.md. Không sửa hoặc nạp snapshot v1.0.0 thay core hiện hành.

## Codex

Repository này giữ editable source ở skills/. Codex local discovery dùng .agents/skills theo [tài liệu chính thức](https://learn.chatgpt.com/docs/build-skills). Nếu muốn discovery tự động, tự copy nguyên folder skill sang .agents/skills của workspace triển khai hoặc vị trí user/runtime hỗ trợ; không cần symlink. Thư mục generated đó không nằm trong source publish và không được thêm Git. Bản local instructions [AGENTS.md](../AGENTS.md) có link explicit để đọc source skill khi liên quan; link không đồng nghĩa skill tự được cài hoặc nạp vô điều kiện.

Với source checkout đã có generated copy, dùng ignored path và không chạy strict manifest gate trên cây đã có file generated; kiểm tra/build từ source sạch hoặc xóa bản generated theo quyền riêng. Không tự sửa cấu hình toàn cục. Không tạo duplicate skill ở nhiều vị trí discovery.

## ChatGPT

Cung cấp full/compact prompt và task; chỉ đưa skill/reference liên quan hoặc dùng khả năng nạp skill mà giao diện thực sự hỗ trợ. Upload ZIP không tự chứng minh đã cài. Nếu không có file loader, dán nội dung cần dùng; không giả định model tự đọc URL hoặc file local.

## Gemma 4 / local

Dùng [adapter](../integrations/adaptive/gemma4-system-prompt.md) qua chat template đúng của runtime; [Google formatting](https://ai.google.dev/gemma/docs/core/prompt-formatting-gemma4) mô tả system/tool turns. Runner phải thực hiện filesystem/tools, validate arguments, enforce permission, timeout/cancel và audit. Không có tool thì không tự nhận đã chạy. Chỉ nạp core và 1–3 references đúng task; không cần Internet/Git/shell/inference API mặc định.

## Build

Sau thay đổi đã được duyệt: `python scripts/build_release.py --prepare`, chạy validators/tests, rồi `python scripts/build_release.py --output-dir ../integration-build`. Full repository candidate và standalone được tạo từ canonical source; không đưa ZIP vào Git history. Đây là candidate, không phải GitHub Release.


## Verified integration và behavioral limits

[Current status](STATUS_CURRENT.md): integration1.1.0 đã vào main và main CI64/64 đã xác minh trên Windows/Ubuntu. Đây vẫn là candidate, chưa được xác minh stable release; cài/copy skill không đồng nghĩa model certification. [Behavioral protocol](evaluation/BEHAVIORAL_PROTOCOL.md) hiện chỉ chuẩn bị, A01–A44 NOT_RUN. Historical reports giữ trạng thái theo thời điểm cũ; tài liệu local mới cần publication và CI riêng.
