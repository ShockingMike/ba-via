# Tạ Nhỏ (app tập gym, tên cũ "Ba Vía"): hướng dẫn cho mọi phiên Claude

Người dùng làm dự án này bằng **nhiều tài khoản Claude khác nhau**. Vì vậy mọi trạng thái và quyết định phải nằm trong file của thư mục này, không nằm trong artifact hay bộ nhớ của riêng một tài khoản.

## Theo dõi tiến độ: `TRACKING.md`
- Đây là nguồn sự thật DUY NHẤT về tiến độ: 96 màn hình theo thứ tự người dùng gặp, 19 giai đoạn lộ trình, 17 quyết định.
- Khi bắt đầu phiên: đọc `TRACKING.md` để biết đang ở đâu.
- Khi xong một việc:
  - sửa cột **Trạng thái** của dòng tương ứng: `Chưa làm` · `Đang thiết kế` · `Đã thiết kế` · `Đang code` · `Xong`;
  - thêm một dòng vào **Nhật ký** (ngày, ai/nick nào, làm gì);
  - chạy `node tools/tracking-summary.js` để tính lại phần Tóm tắt.
- Khi người dùng chốt một quyết định: ghi vào cột **Đã chốt** của bảng Quyết định.
- **Màn nào thiết kế xong PHẢI có ảnh** (người dùng xem lại trên GitHub): chạy `python tools/add-shot.py <mã-màn> <ảnh-chính> [ảnh-biến-thể...]`. Script tạo `shots/<mã>.jpg`, `shots/<mã>-2.jpg`… và trang theo dõi tự hiện ảnh. Copy bản HTML bấm thử vào `prototypes/<mã>.html` (để nick nào cũng mở được trên GitHub Pages; link claude.ai chỉ mở được bằng một nick). Trong TRACKING.md, cột Ghi chú thêm `[ảnh](shots/<mã>.jpg) · [bấm thử](prototypes/<mã>.html)`. Khi báo người dùng, LUÔN đưa link bấm thử `https://shockingmike.github.io/ba-via/prototypes/<mã>.html`.
- Sau khi sửa: commit và `git push` lên repo công khai `github.com/ShockingMike/ba-via`. GitHub Actions tự dựng lại trang theo dõi ở https://shockingmike.github.io/ba-via/. Nếu máy chưa có lệnh `gh`, dùng bản portable ở `tools/gh/bin/gh.exe`.
- Repo là **công khai**: không đẩy email, tên thật, khoá API hay file nặng. `.gitignore` đã chặn Blender, ảnh render và mockup HTML.
- Không đổi thứ tự hay mã màn. Muốn thêm màn mới thì thêm dòng với mã mới và ghi vào Nhật ký.

## Tài liệu chính
- `research/00-plan.md`: kế hoạch sản phẩm. `research/01-programming.md`: luật tập. `research/exercises.json`: 90 bài tập.
- `design/08-screen-plan.md` và `design/screens.json`: chi tiết từng màn (nội dung, trạng thái con, hình cần render), lộ trình, quyết định.
- `design/07-cast-pitches.md` mục C: thế giới Ba Vía (ĐÃ CHỐT). `design/06-avatar-wardrobe.md`: hệ thống tủ đồ.
- `design/screens-v2.html`: 6 màn đã duyệt hướng, kèm bộ quy tắc thiết kế ở đầu CSS. Mọi màn mới phải theo bộ quy tắc này.
- `blender/`: nhân vật nỉ len (Khăn, Bình, Găng đã duyệt, bản chốt ở `blender/via/approved/`), tủ đồ (`blender/via/wardrobe.py`), README trong `blender/via/`.

## Quyết định đã chốt (đừng hỏi lại)
- PWA chạy trên cả iPhone và Android. Mỗi người có profile riêng, check-in hằng ngày, app ra bài, có bài thay thế khi thiếu dụng cụ.
- Mỗi người lưu nhiều phòng tập. Bảng nhóm, streak nhóm và thử thách có ngay từ bản đầu (Firebase).
- KHÔNG chia sẻ ra ngoài (không Zalo/Messenger): chỉ đăng vào nhóm trong app.
- **Tên app: "Tạ Nhỏ"** (chốt 2026-11-20, thay "Ba Vía" vì khó hiểu). Khẩu hiệu "Ai cũng bắt đầu từ quả tạ nhỏ." Ba nhân vật (Khăn, Bình, Găng) gọi chung là **bạn đồng hành** (KHÔNG gọi "nhóc tạ"; người dùng chốt 2026-11-20), chọn nhân vật = **chọn bạn đồng hành**, cổ vũ bạn = **đập tay**, nhóm = **"Hội Tạ Nhỏ [tên]"**. KHÔNG dùng chữ "vía" trong app nữa (các tài liệu cũ vẫn gọi là vía, chỉ là tên nội bộ). Chi tiết: `design/09-naming.md`.
- **Logo: hướng C "Ba màu, một quả tạ"** (chốt 2026-11-21): một quả tạ nỉ ghép từ màu của ba bạn đồng hành. File cuối ở `design/logo/final/` (chỉ có trên máy, không đẩy lên repo). Chi tiết: `design/10-logo.md`.
- Thế giới đồ bỏ quên (tài liệu cũ gọi là "Ba Vía"), shader **nỉ/len chọc**. Mặt Găng: phương án C (quai găng làm băng đô).
- Mỗi buổi tập được 1 mảnh đồ, đủ mảnh thành 1 món, tối đa 1 món/tuần.
- **D2:** mỗi món đồ là một lớp render 3D nỉ riêng, có che khuất đúng, xếp chồng lên nhau trên máy. Mỗi bạn đồng hành có **6 màu cố định** (chốt 2026-11-21).
- Đồ thu thập được phải **mặc thật** lên avatar (mesh 3D gắn vào rig), không dùng icon dán đè.
- Asset làm bằng phần mềm trong máy (Blender portable ở `tools/`). Không dùng Higgsfield hay OpenArt cho app này.
- **Thiết kế xong hết rồi mới code** (D14, chốt 2026-11-21): không code phần nào, kể cả rules engine, trước khi các màn bản đầu được thiết kế và duyệt.
- Hướng dẫn tập bằng "bóng trong gương" như bản v2: người dùng khen "mượt rồi".

## Cách làm việc người dùng muốn
- **Chia việc theo model (chốt 2026-11-25), mục tiêu là tiết kiệm token Fable mà chất lượng giữ nguyên hoặc tốt hơn:**
  - **Opus dựng** màn hình, viết HTML, chạy Blender, chụp ảnh. Trước khi gửi chấm, Opus phải tự soát hết `design/review-checklist.md`.
  - **Fable chỉ chấm** (so mù với ảnh app thật): một lượt ngắn, trả về điểm và danh sách lỗi. Fable cũng được dùng cho các quyết định sáng tạo lớn (nhân vật, logo, tên, phong cách).
  - Vòng lặp: Opus dựng → Fable chấm → Opus sửa → Fable chấm lại nếu điểm dưới 8/10.
  - Mỗi lỗi mới Fable bắt được thì thêm vào `design/review-checklist.md`, để lần sau Opus tự tránh.
- Không tự khen chất lượng. Trước khi đưa người dùng xem, cho một agent khác so mù với ảnh app thật (Duolingo, Finch, Gentler Streak trong `design/refs/`) rồi sửa.
- Nhân vật hay asset mới: đưa vài phương án để người dùng chọn, không tự chốt.
- Trả lời người dùng bằng tiếng Việt, gọn, dễ đọc.
