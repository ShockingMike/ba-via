# Ba Vía (app tập gym): hướng dẫn cho mọi phiên Claude

Người dùng làm dự án này bằng **nhiều tài khoản Claude khác nhau**. Vì vậy mọi trạng thái và quyết định phải nằm trong file của thư mục này, không nằm trong artifact hay bộ nhớ của riêng một tài khoản.

## Theo dõi tiến độ: `TRACKING.md`
- Đây là nguồn sự thật DUY NHẤT về tiến độ: 96 màn hình theo thứ tự người dùng gặp, 19 giai đoạn lộ trình, 17 quyết định.
- Khi bắt đầu phiên: đọc `TRACKING.md` để biết đang ở đâu.
- Khi xong một việc:
  - sửa cột **Trạng thái** của dòng tương ứng: `Chưa làm` · `Đang thiết kế` · `Đã thiết kế` · `Đang code` · `Xong`;
  - thêm một dòng vào **Nhật ký** (ngày, ai/nick nào, làm gì);
  - chạy `node tools/tracking-summary.js` để tính lại phần Tóm tắt.
- Khi người dùng chốt một quyết định: ghi vào cột **Đã chốt** của bảng Quyết định.
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
- Thế giới **Ba Vía**, shader **nỉ/len chọc**. Mặt Găng: phương án C (quai găng làm băng đô).
- Mỗi buổi tập được 1 mảnh đồ, đủ mảnh thành 1 món, tối đa 1 món/tuần.
- Đồ thu thập được phải **mặc thật** lên avatar (mesh 3D gắn vào rig), không dùng icon dán đè.
- Asset làm bằng phần mềm trong máy (Blender portable ở `tools/`). Không dùng Higgsfield hay OpenArt cho app này.
- Hướng dẫn tập bằng "bóng trong gương" như bản v2: người dùng khen "mượt rồi".

## Cách làm việc người dùng muốn
- Agent nghiên cứu và thiết kế chạy với model **fable** (người dùng muốn Fable làm cố vấn).
- Không tự khen chất lượng. Trước khi đưa người dùng xem, cho một agent khác so mù với ảnh app thật (Duolingo, Finch, Gentler Streak trong `design/refs/`) rồi sửa.
- Nhân vật hay asset mới: đưa vài phương án để người dùng chọn, không tự chốt.
- Trả lời người dùng bằng tiếng Việt, gọn, dễ đọc.
