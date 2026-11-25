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
- Mỗi chú thích phải giải thích đủ mọi ký hiệu đang hiện (ví dụ đã có Đẩy, Kéo thì phải có cả Chân).
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
- Tự xem **mọi khung** trên trang, không chỉ mấy ảnh được yêu cầu (gộp tất cả vào một tấm để soát).

## Màn sức khoẻ, an toàn (từ lượt chấm 0.8–0.9)
- **Bản quyền nội dung:** không dịch hay chế lại một bảng câu hỏi có điều khoản "không được sửa" (ví dụ PAR-Q+). Tự soạn câu hỏi riêng, ghi rõ là bản nháp chờ người có chuyên môn duyệt.
- Không tự bịa luật sàng lọc trong bong bóng (ví dụ "không chắc thì chọn Có"). Bong bóng chỉ nói lời trung tính.
- **Màn khuyên là lời khuyên, không phải cửa chặn:** tiêu đề viết như một gợi ý; khi chưa chọn gì thì bong bóng trung tính, không nói như thể đã chọn sẵn.
- Không đưa con số mâu thuẫn với chữ (ví dụ "nhẹ" mà lại ghi "20–60 phút"). Mô tả chế độ bằng lời thường, ngắn và khớp nhau.
- **Biểu cảm theo ngữ cảnh nghiêm túc:** cạnh câu trả lời về bệnh tim hay khi khai chỗ đau thì không cười toe, không nháy mắt, không mắt lim dim. Dùng vẻ chăm chú, lo lắng nhẹ.
- Đạo cụ không được che mặt nhân vật (bút chì chéo qua mắt).

## Luồng hỏi đáp
- **Một chỉ báo tiến độ** mỗi màn: thanh trên cùng HOẶC các vạch đoạn, không cả hai.
- Câu hỏi Có/Không: chạm là trả lời và tự sang câu sau sau một nhịp ngắn, không cần nút Tiếp cho từng câu; luôn giữ nút quay lại.
- Thẻ câu hỏi có chiều cao cố định: đo bằng câu **dài nhất kèm dòng gợi ý**; chữ không được dính sát vạch ngăn.
- **Thẻ chưa chọn phải trông bấm được:** nền trắng có viền mảnh và vòng tròn trống ở góc (chỗ dấu tick sẽ hiện), không để giống thẻ bị vô hiệu hoá.
- Huy hiệu tick nằm **bên trong** góc thẻ hay chip, không lòi ra ngoài viền.

## Hình cơ thể để chọn vùng
- Hình không mặt nhìn từ sau dễ bị đọc nhầm thành mặt trước (lưng thành bụng). Mở ở mặt trước, vùng ở lưng đặt ở mặt sau, có nút "Mặt trước / Mặt sau", chọn vùng lưng thì hình tự quay.
- Điểm chạm trên cơ thể phải to (khoảng 44px), có nhịp sáng nhẹ khi chưa chọn gì; nhãn bên cạnh là lối chọn thứ hai ngang hàng. Bong bóng nói đúng cả hai cách chọn.
- Nền khung (gương) phải ấm, trung tính như nền kem/cát của 0.6/0.7; không dùng mảng xanh tím hay tím nhạt lạnh.
- Chọn một vùng không thấy được ở mặt đang xem thì hình phải tự lật sang mặt kia; nếu chủ lật lại, tab mặt kia hiện số vùng đã chọn.
- Cột nhãn chia đều chiều cao, không để khoảng trống chết giữa nhãn cuối và vạch ngăn.
- Màn khuyên: bong bóng sau khi chọn phải nói rõ đó là lựa chọn của chủ ("Chủ chọn tập nhẹ…"), để ảnh chụp không bị đọc như đã bật sẵn.

## Danh sách dài, dụng cụ (từ cụm 0.10–0.13)
- Danh sách nhiều mục (ví dụ 22 dụng cụ): chia nhóm gập mở được, ô hai cột; con số chính (ví dụ "Làm được X bài") nằm **ngoài** vùng cuộn để luôn thấy.
- Biểu tượng ở đầu nhóm không được trùng với biểu tượng của một ô ngay bên dưới.
- Con số tính từ dữ liệu thật (exercises.json) chứ không gõ tay; script dựng in ra số mong đợi của từng khung để đối chiếu với ảnh chụp.
- Lựa chọn "Chưa biết" là một ô bình thường cùng kiểu với các ô khác, không thêm kiểu nút mới.
- Mỗi giá trị nói luôn nghĩa thực tế bằng lời thường (ví dụ "mỗi lần thêm được 2,5 kg"), thay cho thuật ngữ.
