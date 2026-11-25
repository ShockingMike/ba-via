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
- Một món chỉ nằm ở **một** màn: không vừa có ô "Dây kháng lực" trong danh sách vừa có thẻ bảo "thêm dây ở bước sau". Đồ cá nhân chỉ khai ở màn đồ cá nhân.
- Mẫu "đầy đủ" phải tích sẵn **tất cả**; nhóm đang gập vẫn ghi tên các món đã tích (hoặc "Đủ cả" / "Chưa có món nào").
- Khi đã có thẻ ghi chú, bong bóng chỉ còn **một dòng ngắn**, để danh sách không bị đẩy xuống dưới mép màn.
- Bong bóng không lặp lại dòng phụ của ô vừa chọn: bong bóng nói **vì sao**, ô nói **là gì**.
- Dòng lựa chọn có số đo (kg, cỡ) nên có hình nỉ vẽ theo cỡ thật (thanh dài ngắn, đĩa to nhỏ). Biểu tượng vuông thì đặt khung vuông, nếu không mọi cỡ trông như nhau.
- Nhãn "Khuyên dùng" nằm trong thẻ (dưới tiêu đề), không đè lên dấu tick hay lòi ra ngoài viền. Lựa chọn loại trừ ("Không mang gì") là một dòng full bề ngang dưới vạch ngăn.
- Ô có ảnh nỉ đặt bằng class CSS: dùng `background-color`, không dùng `background:` viết gộp, vì nó xoá mất ảnh (dải tuần ở 0.15 từng mất viên nỉ vì lỗi này).
- Cảnh rộng (nhiều hộp, cả hội) phải gom gọn để khi co theo bề ngang cột vẫn đủ cao; đừng để cảnh dài ngang rồi bé tí.
- **Mọi luồng mời bạn phải có hành động chia sẻ:** nút chính "Chia sẻ mã" mở bảng chia sẻ của máy (mã + tên hội + một câu mời), "Sao chép" là nút phụ. Luật "không chia sẻ ra ngoài" chỉ áp cho bài tập, không áp cho mã mời.
- Mã mời hiển thị và ô nhập mã dùng **cùng một cách chia nhóm** (3 + 3) và cùng một vạch ngăn.
- Phần cố định của tên (ví dụ "Hội Tạ Nhỏ") là một chip không sửa được trong ô nhập; bộ đếm ký tự chỉ hiện khi gần chạm giới hạn.
- Bong bóng đặt vào khoảng trống của cảnh (trên hộp), không đè lên đầu nhân vật.
- Màn kết thúc là **khoảnh khắc vui**, không phải form tóm tắt: nhân vật to, là tâm điểm, có hiệu ứng nhỏ (an toàn với giảm chuyển động); phần tóm tắt gom thành một hàng chip.
- Ô quà tặng (món đã có) không viền xanh ngọc, có nhãn "Mới", để không trông như lựa chọn bấm được. Ảnh món đồ phải đủ to để đọc (cắt sát một món nếu ảnh gốc có cả đôi đứng xa nhau).
- Dấu chú thích trong một biểu thức Python kéo dài nhiều dòng có thể nuốt mất phần sau: kiểm tra mọi lớp CSS ảnh thực sự có trong trang.

## Ghép vào bản trải nghiệm (app.html)
- [ ] Mỗi trạng thái là `<section class="unit">` có `<p class="cap">`; trạng thái người dùng gặp đầu tiên có chú thích chứa "Vừa mở" hoặc "Chưa chọn".
- [ ] Nút chính ở bước cuối gọi toast `Bản mẫu: sang <mã màn kế>.`; nút lùi gọi `Bản mẫu: về <mã màn trước>.` Đúng mã theo TRACKING.
- Gộp ảnh nhân vật từ nhiều lần render khác camera hoặc khác cỡ ảnh: KHÔNG dùng chung một khung cắt hợp (union crop), vì nhân vật sẽ nhỏ đi; cắt từng ảnh theo khung riêng rồi đưa về cùng chiều cao.
- Chiều cao theo phần trăm của một cha flex không có chiều cao cụ thể sẽ thành 0: ảnh nhân hoặc cảnh biến mất. Dùng chiều cao cố định cho khung ảnh.
- Khi có dải nhắc phụ (sao lưu…), khung nhân vật phải co lại để bong bóng không đè lên đầu.
- Ngày tháng ở đầu màn phải khớp với ô "hôm nay" trong dải tuần.

## Vòng hằng ngày (từ lượt chấm 1.1–1.3)
- **Luật "cái gì được tính" nói đối xứng:** mọi lựa chọn ghi kết quả cùng một kiểu, cùng một chỗ, cùng độ đậm ("Tính 1 buổi · 1 mảnh" / "Không tính vào lời hứa tuần"); không phủ định kép, không in đậm riêng một thẻ.
- **Mỗi bài tập có một hình** cho người mới (tạm thời một hình nỉ cho mỗi kiểu động tác; chuỗi riêng từng bài để sau), kèm tên tiếng Việt dễ hiểu, tên tiếng Anh nhỏ.
- **Nút chỉ có biểu tượng phải có chữ** (Đổi bài, Để sau). Không dùng biểu tượng đồng hồ nếu không phải hẹn giờ.
- **Thay đổi được nhắc thì phải thấy và có đánh dấu:** khi bong bóng nói về một bài, bài đó tự cuộn vào tầm nhìn và có viền.
- **Nhãn lặp trên mọi dòng thì đưa lên đầu danh sách** (một dòng ghi chú), không lặp lại từng dòng.
- **Điểm chạm trên cơ thể nằm đúng bộ phận được gọi tên** (cổ tay ở cổ tay, gối ở gối); hình đủ to để chạm.
- **Điều khiển không áp dụng thì thu lại**, không làm mờ (ví dụ chọn "Không đau" thì bỏ hẳn bước mức đau, kiểu đau).
- **Danh sách cuộn mờ dần dưới nút cố định**, và có chỗ trống cuối danh sách để dòng cuối nổi lên trên lớp mờ.
- **Biểu tượng tab cắt sạch nền**, không có ô vuông xám.
- **Câu số liệu huấn luyện phải soát cách hiểu ngược:** "còn sức làm thêm 2–3 lần" dễ bị đọc thành "làm thêm 2–3 lần"; viết "dừng khi còn sức làm thêm 2–3 lần nữa, đừng cố tới hết sức".
- Thanh trượt web mặc định không hợp với giao diện nỉ: dùng các bậc nỉ có chữ.
- Một câu hỏi mỗi bước, kể cả trong tấm trượt: chỗ đau → mức → kiểu → kết quả.
- Lựa chọn chưa chọn: nền trắng, viền mảnh, vòng tròn trống ở cùng một chỗ dấu tick sẽ hiện.
- Một sân khấu cố định cho mọi trạng thái của màn chính: nhân vật cùng chiều cao, bóng đổ dính chân.
- **Bong bóng ở màn chính có vị trí dọc cố định** giữa mọi trạng thái (đặt tuyệt đối ở đầu sân khấu), không trôi theo chiều cao nhân vật.
- **Nhãn nhỏ và tiêu đề thẻ không nói cùng một ý** ("Tuần này đủ rồi" / "Đủ tuần rồi"): tiêu đề phải thêm thông tin mới.
- **Biểu tượng tab dạng nhân vật**: cắt sát mặt (thấy mắt) để khi chuyển xám vẫn đọc được, không thành khối xám.
- **Nút chính ghim đáy giữa các bước**; lựa chọn giãn ra lấp chỗ trống, không để nút nhảy lên xuống.
- **Lựa chọn loại trừ ("Đủ cả", "Không đau") tách riêng** thành một dòng ở trên, không nằm lẫn như một chip ngang hàng.
- **Tấm trượt có tiêu đề riêng từng bước và chỉ báo bước**, co theo nội dung; ghi chú chỉ hiện ở bước nó thuộc về.
- **Hình nỉ của bài phải khớp tên bài** (ghế dốc thì có ghế nằm nghiêng, bài ngồi thì ngồi); soát từng hình với tên trước khi gửi.
- **Danh sách tự cuộn có lớp mờ cả trên lẫn dưới**, để không thẻ nào bị cắt ngang chữ.
- **Đuôi bong bóng chỉ về phía nhân vật**; bong bóng chính tối đa 3 dòng.
- **Dấu chấm trang trí cũng là viên nỉ**, không dùng chấm phẳng.
- Hình người dùng để chọn vùng: tay dang ra để cổ tay không trùng hông; khung hình co theo bề ngang để không cắt mất tay.

## Thanh điều hướng (chốt 2026-11-26)
- **Mẫu duy nhất: thanh C.** Viên thuốc trắng nổi, ba mục có chữ (Hôm nay, Hội, Tủ đồ); quả cầu Khăn đứng riêng bên phải là mục Tôi, có vòng tiến độ tuần màu xanh ngọc (số buổi đã tập / lời hứa N).
- **Mục đang chọn:** biểu tượng tô nhạt và nét dày hơn, chữ đậm màu mực, chấm vàng nhỏ #FFC93C. Không dùng màu cam (cam chỉ cho nút chính).
- **Biểu tượng và hiệu ứng chạm** là bộ cuối trong `design/nav-icons/` (sáu SVG + `nav-anim.js`), không vẽ lại riêng từng màn.
- **Màn mới bắt buộc dùng markup chung:** `<nav class="navg"><div class="navbar"><button class="tab" data-icon="homnay|hoi|tudo">…</button></div><button class="orb">…</button></nav>`, sinh bằng hàm `tabbar()` trong `screen-1.1-1.3-src/screens1x.py`, và CSS khối "shared bottom nav" trong `t11h.html`.
- Bản bấm thử phải là một file HTML: **nhúng thẳng** `nav-anim.js` vào trang (thay `{{id}}` bằng một mã khác để qua bước kiểm tra chỗ trống của script dựng, và thoát chuỗi `</script` trong phần chú thích, nếu không khối script bị cắt giữa chừng và biểu tượng không hiện).
- Thanh nằm trong dòng chảy dưới nút chính (không đè lên nút "Vào tập"), cách thanh home 30px.
- Trong bản mẫu, chạm Hội, Tủ đồ, Tôi chỉ hiện toast "Bản mẫu: tab … chưa có bản thiết kế." rồi trả mục chọn về; không dùng chữ "sang <mã>" khi màn đó chưa có.

## Màn tập (từ cụm 1.4)
- Trong buổi tập không có thanh điều hướng; nút X ở góc mở xác nhận dừng buổi.
- Hình bóng trong gương không được cắt mất đầu: khi khung gương phải thấp lại (vì có thẻ thông báo), dùng `object-fit:contain` trên nền cùng màu kính.
- Tên bài không được cắt bằng dấu ba chấm: đưa nút phụ (Hướng dẫn) vào góc khung gương thay vì đặt cạnh tên.
- Lời bạn đồng hành nằm một dòng riêng dưới chấm set, không chen cạnh chấm set rồi bị cắt.
- Hình tĩnh theo kiểu động tác phải khớp dụng cụ của bài (thanh đòn thì hình cầm thanh đòn, không phải tạ tay).
- Dừng buổi giữa chừng: đã xong ít nhất 1 bài thì tính 1 buổi · 1 mảnh; chưa xong bài nào thì lưu nháp, chưa tính. Nói rõ trên tấm xác nhận.
- Thông báo kỷ lục là dải nổi tự tắt, không chặn đồng hồ nghỉ hay nút bên dưới.
- Chuỗi có dấu % trong mã Python dùng toán tử % phải viết %% (lỗi "unsupported format character").
- **Nút trong buổi tập tối thiểu 48pt** (nút −/+ 52pt, ±15s và X 46–48pt); không có hành động chỉ là chữ, mỗi hành động là chip có biểu tượng và chữ.
- **Nút chính và hai ô số ở toạ độ cố định** qua mọi trạng thái (khoá đáy màn); dưới mỗi số có ô cố định 2 dòng cho "đích" hoặc số đĩa.
- **Hành động an toàn (Báo đau) có ở mọi trạng thái con**, kể cả lúc nghỉ.
- **Mũi tên phải khớp chữ** (xuống = XUỐNG); lúc nghỉ không hiện nhãn pha động tác.
- **Cùng một giá trị phải khớp giữa các màn** (tạ khởi động 1.4 = 1.4d; số phút 1.1 = 1.3).
- **Không có thông báo nội bộ trong giao diện** người dùng thấy.
- **Câu dự phòng theo từng loại dụng cụ** (tạ tay 2 kg, thanh đòn với đĩa 1,25 kg, máy 5 kg mỗi nấc).
- **Toast không bao giờ che hình hướng dẫn** trong gương.
- **Không hỏi câu cài đặt giữa set**: chỉ hỏi lúc nghỉ hoặc lúc xem trước.
- **Không chèn nút giữa câu chữ**: nút nằm một dòng riêng.
- Dừng buổi sau ít nhất 1 bài: tính 1 buổi (chuỗi tuần, lời hứa) nhưng không có mảnh đồ; 0 bài là nháp, không tính.
