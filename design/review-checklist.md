# Checklist tự soát trước khi gửi chấm

Tổng hợp từ các lượt so mù màn 0.1–0.7 và bản v2. Người dựng màn (Opus) phải tự soát hết danh sách này **trước khi** gửi Fable chấm, để Fable chỉ phải bắt lỗi tinh, không phải bắt lại lỗi cũ.

## Bố cục
- Mỗi màn có **một điểm nhấn** rõ ràng: nhân vật, hoặc một con số to. Không để hai thứ cùng cỡ tranh nhau.
- **Không có khoảng trống chết:** soát phía trên nhân vật, phía trên nút chính, phía dưới tiêu đề, và ở mọi trạng thái (trống, đã chọn, lỗi).
- **Câu hỏi hoặc tiêu đề luôn nằm cố định trên đầu màn**, không biến mất sau khi chọn (giống 0.4).
- **Cố định khung giữa các biến thể:** nhân vật, chấm chuyển trang, tên và bong bóng thoại không được nhảy vị trí khi đổi lựa chọn hoặc đổi nhân vật.
- **Thẻ co theo nội dung**, không để thừa chỗ ở trạng thái ít dữ liệu.
- **Một câu hỏi mỗi màn** (kiểu Duolingo). Hai câu hỏi trên một màn thì bị chê là form hay danh sách khô khan; tách thành nhiều bước trong cùng một khung.
- **Tiêu đề và mọi thứ nằm gọn trong cột nội dung.** Không tràn qua lề, kể cả đạo cụ trong cảnh (ghế, bàn).
- **Không để đoạn chữ mồ côi** lơ lửng phía trên nút chính. Gắn nó vào thẻ liên quan hoặc vào bong bóng thoại.
- **Bong bóng thoại không được che đầu nhân vật.**
- **Bong bóng và nội dung không được mâu thuẫn**, ví dụ bong bóng nói "4" trong khi con số trên màn là "6".
- **Không lặp lại cùng một hình** ở cùng cỡ ngay cạnh nhau (đạo cụ nhân vật cầm và biểu tượng trong thẻ).

## Nhân vật (bạn đồng hành)
- Dáng và biểu cảm phải **khớp tính cách**: Khăn nhút nhát, Bình mê lập kế hoạch, Găng lười mà khoẻ.
- **Phản ứng theo từng trạng thái** bằng biểu cảm hoặc dáng khác nhau. Chỉ đổi chữ trong bong bóng là chưa đủ.
- **Không để viền sáng (halo) quanh lông** khi cắt nền: tách nền theo đúng màu nền thật, hoặc dùng premultiplied alpha.
- Có bóng đổ nhẹ dưới chân. Không lơ lửng. Các nhân vật có kích thước nhìn tương đương nhau.
- Không dán cùng một ảnh render vào hai biến thể khác nhau.

## Thành phần giao diện
- **Dấu tick là huy hiệu ở góc trên bên phải thẻ.** Chữ trong thẻ không bị đẩy lệch khi chọn hay bỏ chọn.
- **Một kiểu đánh dấu đã chọn** cho toàn app: nền xanh ngọc kèm dấu tick, giống chip ở 0.5. Không trộn nút radio bên phải với tick bên trái.
- Lựa chọn chưa chọn **không được trông như bị vô hiệu hoá**.
- Lựa chọn phải có **phản hồi đáng giá**: biểu tượng phóng to, nhân vật phản ứng. Không để trông như danh sách cài đặt.
- **Biểu tượng phải đọc được ở cỡ 46px**, nét đậm, không xoay nghiêng. Không dùng ngọn lửa cho việc khác ngoài streak.
- **Ô màu, biểu tượng phải là chất nỉ** đồng bộ với nhân vật, không dùng chấm tròn phẳng.
- **Màu cam chỉ dùng cho nút chính.** Không thêm kiểu nút mới (ví dụ nút viền tối) ngoài các kiểu đã có ở 0.4/0.5.
- Nút phụ ("Để sau") là chữ nhỏ, không to hơn nút chính.
- **Báo lỗi phải nhìn thấy rõ:** viền và chữ màu hổ phách, có icon, ô nhập rung nhẹ, nhân vật lộ vẻ lo.
- Dòng gợi ý trong ô (placeholder) nhạt và nhỏ hơn chữ đã nhập. Có trạng thái đang gõ (con trỏ, viền focus).

## Lời văn
- Gọi người dùng là **"chủ"**. Gọi nhân vật là **"bạn đồng hành"**. **Không dùng chữ "vía" hay "nhóc tạ"**.
- Không dùng thuật ngữ khó hiểu ("streak", "mảnh đồ") mà không giải thích bằng lời thường ở lần đầu xuất hiện.
- Không viết câu khiến lựa chọn của người dùng nghe như vô nghĩa ("chọn gì cũng vậy").
- Nhãn nút phải khớp với những gì đang hiện trên màn: bấm "Mở hộp" thì hộp phải đang đóng; còn đang onboarding thì nút là "Tiếp", không phải "Xong".
- Dùng **một thuật ngữ thống nhất** cho một khái niệm, ví dụ đã dùng "cài app" thì không lẫn "màn hình chính".
- Không trách móc, không phán xét mục tiêu hay số buổi người dùng chọn.

## Kỹ thuật
- Không cuộn ngang ở bề rộng 400px. Tôn trọng `prefers-reduced-motion`.
- Ảnh nhúng nén lại, mỗi trang càng nhẹ càng tốt (mục tiêu dưới 3 MB).
- Chụp ảnh 390×844 cho trạng thái chính và các biến thể quan trọng, rồi tự xem ảnh trước khi gửi chấm.
