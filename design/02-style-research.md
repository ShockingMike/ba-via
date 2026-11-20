# 02 — Nghiên cứu phong cách hình ảnh (chưa có mockup)

Ngày: 2026-11-19. Đi kèm: [moodboard.html](moodboard.html) (bảng ảnh tham khảo, xếp theo họ phong cách) và thư mục [refs/](refs/) (45 ảnh đã giữ + `manifest.json`).
Đọc cùng: [01-design-brief.md](01-design-brief.md), [00-plan.md](../research/00-plan.md).

Nhãn: **[Q]** tự nhìn thấy trên ảnh chụp trong phiên này · **[S]** có nguồn đã đọc · **[S2]** nguồn thứ cấp (bài tổng hợp, diễn đàn) · **[D]** phán đoán thiết kế · **[UNVERIFIED]** chưa kiểm chứng.

## 0. Tóm tắt

- Ba hướng cũ (Phố, Xưởng, Sớm) trông rẻ vì cùng một lý do gốc: **toàn bộ hình ảnh là hình phẳng vẽ bằng code**. Trong các app **fitness và thói quen** đã xem, không app nào trông đẹp mà thiếu một nguồn hình giàu chi tiết: ảnh/video người thật, hình 3D có ánh sáng, hoặc minh hoạ do hoạ sĩ vẽ. Ngoại lệ là app công cụ thuần chữ (Things, Linear, Streaks, stoic.), đẹp nhờ kỷ luật chữ và khoảng trắng rất cao; app này phải dạy động tác nên không đi đường đó được.
- Đề xuất 6 họ phong cách (mục 4). Rút gọn còn 2 để chọn: **E — Đất nặn 3D** và **B — Phòng tập đêm**.
- **Đề nghị mở lại quyết định Q4** trong kế hoạch ("clip người que bằng SVG"). Thay bằng: clip vòng lặp dựng sẵn của **một nhân vật nhất quán**, kèm 2 ảnh tư thế đầu/cuối cho mọi bài (mục 5).
- Vòng này không dựng mockup, đúng yêu cầu.

## 1. Đã xem gì, bằng cách nào

**Cách xem.** Mọi ảnh được xem dưới dạng bảng ghép (mỗi màn hình cao 560 px), không mở từng ảnh riêng, trừ hai ảnh Seven.

**Cách lấy ảnh.** Ảnh màn hình chính thức trên App Store, lấy qua API tra cứu công khai của iTunes (`itunes.apple.com/search`), tải bản rộng 600 px. Đây là ảnh do chính nhà phát triển đăng, nên giao diện bên trong là thật nhưng đã được chọn lọc và có dòng tiêu đề quảng cáo phía trên. Ngoài ra chụp bằng Chrome không giao diện: trang báo chí của Apple về Liquid Glass, trang Apple Design Awards, trang tìm kiếm Dribbble.

**Độ phủ** (42 app đã tải và xem ảnh; 45 ảnh được giữ):

| Nhóm | Đã xem [Q] | Giữ ảnh trong moodboard |
|---|---|---|
| Fitness, sức khoẻ cao cấp | Apple Fitness/Fitness+, WHOOP, Oura, Strava, Nike Training Club, Ladder, Future, Gentler Streak, Fitbod, Hevy, Alpha Progression, Centr, Peloton, Runna, Bevel, Athlytic, Caliber, Gymverse, SHRED, Zing, Seven | Apple Fitness, WHOOP, Oura, NTC, Ladder, Future, Gentler Streak, Fitbod, Hevy, Alpha Progression, Peloton, Bevel, Caliber, Seven |
| Thói quen, học tập | Duolingo, Headspace, Finch, Calm, Opal, (Not Boring) Habits, Streaks, Structured, Tiimo, Waterllama, Ahead, stoic., How We Feel | Duolingo, Headspace, Finch, Opal, (Not Boring) Habits, Streaks, Structured, Tiimo, Waterllama, stoic., How We Feel |
| App dẫn dắt về thiết kế | Arc Search, Linear, Things 3, Airbnb, Flighty, Copilot, Amie, Partiful | Linear, Things 3, Airbnb, Partiful |
| Xu hướng 2025–2026 | Liquid Glass (4 ảnh báo chí Apple), 8 concept 3D/clay trên Dribbble, bố cục bento (thấy ở Apple Fitness, Bevel, stoic., Peloton) | 2 ảnh Liquid Glass, 4 concept Dribbble |

**Không lấy được hoặc không dùng được:**
- Mobbin: trang treo, không tải xong. Screenlane, Behance: chưa thử.
- fitbod.me: bị Cloudflare chặn (dùng ảnh App Store thay thế).
- apple.com/apple-fitness-plus: chỉ chụp được một khung hình video, đã xoá.
- Trang Apple Design Awards: tải được (đang hiện danh sách 2026), toàn chữ và icon nhỏ, không giữ ảnh. Thấy Structured có tên trong hạng mục Inclusivity [Q].
- apple.com/os/ios: đã chuyển sang iOS 27, ảnh tải chậm nên trang trống; đã xoá. Ảnh Liquid Glass lấy từ bài báo chí tháng 6/2025.
- Các concept Dribbble là **bản vẽ ý tưởng, không phải sản phẩm thật**; ảnh nhỏ (356 px) vì cắt từ trang tìm kiếm.

## 2. Vì sao ba hướng cũ trông rẻ

Đã mở lại `mockups.html` và so cạnh ảnh tham khảo. Nói thẳng:

1. **Nhân vật là hình phẳng vẽ bằng code.** Các đoạn bo tròn tô một màu, khớp là chấm tròn, không có ánh sáng, không có bóng đổ, không có mặt. Trong khi đó mọi app fitness đã xem đều dùng thứ giàu chi tiết hơn hẳn cho đúng vị trí này: video người thật (Fitbod, Future, Alpha Progression, Caliber, Ladder, Peloton, Centr), hình 3D giải phẫu có đổ bóng (Hevy), hoặc nhân vật 3D cách điệu (Seven) [Q]. Hình người que là thứ người dùng nhìn nhiều nhất trong app, nên nó kéo cả app xuống.
2. **Không có hình ảnh thật ở bất kỳ đâu.** Không ảnh, không render, không minh hoạ có tay nghề. Mắt người đọc "đắt tiền" qua chi tiết mà CSS không tự sinh ra được: da, vải, kim loại, độ mờ hậu cảnh, ánh sáng. WHOOP, Oura, Opal đều đặt giao diện lên một lớp ảnh hoặc 3D [Q].
3. **Neo-brutalism là phong cách mốt, và dễ làm nhất.** Viền mực 2 px + bóng cứng lệch góc là thứ mọi template miễn phí đang dùng. Không app nào trong 42 app đã xem dùng nó [Q]. Brief cũ cũng tự ghi rủi ro này.
4. **Quá nhiều màu ngang hàng.** Phố dùng 6 màu (kem, mực, coban, vàng nghệ, đỏ son, xanh cổ vịt) cùng lúc trên một màn hình. App cao cấp dùng **nền trung tính + đúng một màu nhấn**: Ladder và Apple Fitness là đen + vàng chanh; WHOOP là xám than + xanh lá cho đúng một vòng tròn; Things là trắng + xanh dương; Airbnb là trắng + hồng chỉ ở vài điểm [Q]. Duolingo nhiều màu, nhưng mỗi màn hình chỉ có một màu chủ đạo trên nền trắng [Q].
5. **Mật độ quá dày, mọi thứ đều có viền.** Màn check-in nhồi 5 câu hỏi và khoảng 20 chip vào một màn hình, chip nào cũng viền đậm như nhau, nên không có thứ bậc. So với Duolingo: một câu hỏi mỗi màn hình, một nút to ở đáy. So với WHOOP: một con số 85% chiếm nửa màn hình [Q]. Brief cũ đúng về "một quyết định mỗi màn hình" nhưng mockup không làm theo.
6. **Không có chiều sâu.** Mọi bề mặt là màu phẳng. App cao cấp có ít nhất một kiểu chiều sâu: gradient rất nhẹ trên nền (Bevel, Copilot), kính mờ (Apple, Opal), ảnh làm nền thẻ (Future, Peloton), bóng mềm nhiều lớp (Things, Airbnb) [Q].
7. **Chữ thiếu thang bậc.** Tiêu đề, nhãn, chip gần cùng cỡ và cùng độ đậm. App cao cấp chênh rất mạnh: con số 60–90 px đứng cạnh nhãn 11–12 px viết hoa giãn chữ (WHOOP, Oura, Stoic) [Q].
8. **Chuyển động chưa đủ tay nghề để gánh.** Hoạt hình nội suy góc khớp tuyến tính trông máy móc. Duolingo có hẳn một nhóm làm Rive và các "creative technologist" [S1].

**Một điều công bằng:** không phải app thật nào cũng đẹp. Hevy, Alpha Progression, Gymverse, Athlytic, SHRED trông kém hẳn Ladder hay WHOOP dù cùng thể loại, và chúng mắc đúng các lỗi trên: xanh dương mặc định, nhiều màu, chữ nghiêng in hoa ồn ào, ảnh thu nhỏ lộn xộn [Q]. Tức là thể loại gym tracker vốn dễ trông rẻ; muốn vượt lên phải mượn kỷ luật của nhóm WHOOP/Things/Duolingo.

## 3. App cao cấp làm thế nào

| Yếu tố | Quan sát [Q] | Rút ra cho app này [D] |
|---|---|---|
| **Thang chữ** | Một con số hoặc một câu rất to, phần còn lại nhỏ và nhạt. WHOOP: "85%" to giữa vòng tròn. Duolingo: số "3" cao bằng 1/5 màn hình. Stoic: "good morning." là thứ duy nhất trên đầu trang | Mỗi màn hình có đúng một phần tử cỡ 56–90 px. Nhãn 11–13 px. Bỏ các cỡ lưng chừng |
| **Khoảng trắng** | Things và Airbnb để lề rộng, mỗi dòng cao; Duolingo để trống 40% màn hình bài học | Giảm một nửa số thứ trên màn check-in: hỏi lần lượt, hoặc chỉ hiện "Như mọi khi" + 1 dòng tóm tắt |
| **Chiều sâu** | Ba cách: kính mờ trên nền ảnh (Apple, Opal); thẻ tối nổi trên nền đen bằng chênh sáng rất nhỏ, không viền (Apple Fitness, Linear, Peloton); bóng mềm rộng trên nền sáng (Things, Airbnb, Copilot) | Chọn một cách cho cả app. Bỏ viền mực |
| **Hình ảnh** | Fitness cao cấp = ảnh/video người thật, ánh sáng điện ảnh, nền tối (Ladder, Peloton, Future, NTC, Centr). App thói quen = nhân vật minh hoạ (Duolingo, Finch, Gentler Streak, Headspace, Waterllama). App công cụ = gần như không hình, bù bằng chữ và khoảng trắng (Things, Linear) | Phải chọn một nguồn hình và đầu tư thật. Đây là quyết định lớn nhất |
| **Kỷ luật màu** | Nền trung tính + 1 màu nhấn. Màu trạng thái (xanh/vàng/đỏ) dùng rất tiết kiệm | 1 màu nhấn. Vùng xanh/vàng/đỏ của check-in chỉ hiện ở một chấm hoặc một vòng |
| **Chuyển động** | Không đánh giá được từ ảnh tĩnh. Duolingo dùng Rive với state machine để trộn hoạt hình theo ngữ cảnh [S1] | Ít nhưng kỹ: một khoảnh khắc ăn mừng làm thật tốt; phần còn lại chỉ là chuyển cảnh 150–250 ms |
| **Bento** | Apple Fitness (Summary), Bevel, Stoic chia trang thành các ô bo góc lớn, mỗi ô một số liệu | Hợp cho trang "Tuần này" và trang nhóm; không hợp cho màn hình ghi set |

### Nhân vật: Duolingo, Headspace, Finch làm thế nào

- **Duolingo.** Nhân vật dựng trong Rive. Với nhân vật Lily trong tính năng gọi video, nhóm làm 8 hoạt hình đầu + 8 hoạt hình thân, trộn bằng state machine thành hơn 64 biến thể; file Rive cuối cùng dưới 1 MB; hoạ sĩ, animator và kỹ sư họp hai lần mỗi tuần; công ty tuyển riêng "creative technologist" để tối ưu file Rive [S1]. Hình khối đơn giản, ít chi tiết để vẽ được hàng trăm hình [brief 01, S6]. Trên ảnh: nhân vật luôn đứng trên nền trắng trống, nút to có màu riêng [Q].
- **Headspace.** Hệ minh hoạ nội bộ: nhân vật là khối màu đặc, mặt đơn giản, màu cam–vàng–xanh đậm [Q]. Một bài hướng dẫn bên thứ ba nói họ có hơn 3.000 hình và bộ quy tắc chặt [S2]. It's Nice That đưa tin bộ nhận diện mới mở rộng nhiều kiểu mặt, nhiều cảm xúc [S2].
- **Finch.** Chim 2D vector, mắt chấm, cảnh nền có gradient mềm; nhân vật mặc đồ, có bạn đồng hành [Q]. Không tìm được nguồn chính chủ nào về công cụ họ dùng → **[UNVERIFIED]**.
- **Gentler Streak.** Nhân vật là một khối cam có tay chân, vẽ 2D phẳng nhưng dáng rất sống; mỗi trạng thái cơ thể có một tư thế riêng [Q]. Đoạt Apple Design Award [Q, ghi trên ảnh].

Điểm chung: nhân vật của họ **do hoạ sĩ thiết kế**, có mặt, có cảm xúc, có dáng riêng. Hình người que không mặt trong mockup cũ không phải là nhân vật theo nghĩa này.

## 4. Sáu họ phong cách

Tên họ là tên tạm để dễ gọi. Mỗi họ mượn nguyên tắc, không chép nhận diện của hãng nào.

### A — Kính sáng (kiểu Apple, iOS 26)

- **Ảnh tham khảo:** Apple Liquid Glass (2 ảnh), Apple Fitness (Summary), Apple Fitness+ (Plans), Opal (đồng hồ), Bevel (Recovery).
- **Định nghĩa.** Chữ: grotesk trung tính kiểu hệ thống, số to đậm. Màu: nền đen hoặc ảnh phong cảnh mờ, nội dung trong thẻ kính bán trong suốt; một màu nhấn sáng (vàng chanh ở Apple Fitness). Chiều sâu: mờ nền, viền sáng mảnh, gradient mềm trong thẻ. Hình ảnh: ảnh làm nền, vòng tiến độ. Chuyển động: thanh điều hướng co giãn, chuyển cảnh mượt.
- **Cảm giác cho app này:** "app xịn của Apple". Quen, tin cậy, hơi lạnh. Ít cá tính riêng.
- **Dễ dùng trong phòng tập:** tốt nếu nền tối; chữ trên kính dễ kém tương phản khi nền phía sau sáng.
- **Khả thi với PWA một người làm:** trung bình. `backdrop-filter` chạy trên Safari và Chrome, nhưng hiệu ứng khúc xạ thật của Liquid Glass không làm được bằng CSS, chỉ làm gần giống [D]. Rủi ro: trên Android trông như đồ nhái iOS.
- **Demo bài tập hợp:** video hoặc render 3D trên nền tối.

### B — Phòng tập đêm (athletic tối, cao cấp)

- **Ảnh tham khảo:** WHOOP (Recovery), Oura, Ladder (2 ảnh), Peloton, Future, Linear.
- **Định nghĩa.** Chữ: grotesk đậm hoặc hơi rộng cho tiêu đề (Ladder), nhãn nhỏ viết hoa giãn chữ (WHOOP). Màu: gần đen + **một** màu nhấn (vàng chanh, hoặc xanh lá). Chiều sâu: thẻ tối hơn/sáng hơn nền một chút, không viền; ảnh có ánh sáng điện ảnh làm nền thẻ. Hình ảnh: ảnh/video người thật là nhân vật chính. Chuyển động: gọn, nhanh.
- **Cảm giác cho app này:** nghiêm túc, "mình đang tập thật". Dễ trông đắt tiền nhất trong 6 họ.
- **Dễ dùng trong phòng tập:** tốt nhất. Tương phản cao, số to, đỡ chói.
- **Khả thi:** CSS rất dễ. **Toàn bộ chất lượng nằm ở ảnh và video.** Hướng "Xưởng" cũ chính là họ này mà không có ảnh, nên trông rẻ. Nếu không có nguồn hình tốt thì đừng chọn.
- **Lưu ý:** brief cũ lo người mới và các bạn nữ thấy "không dành cho mình". Ladder và Peloton cho thấy vẫn làm thân thiện được bằng ảnh người cười, lời chào tên riêng, bo góc lớn [Q].
- **Demo bài tập hợp:** video người thật hoặc clip dựng sẵn kiểu ảnh thật trên nền tối.

### C — Bạn đồng hành (minh hoạ ấm, có nhân vật)

- **Ảnh tham khảo:** Duolingo (2 ảnh), Gentler Streak (2 ảnh), Headspace, Finch, Waterllama.
- **Định nghĩa.** Chữ: tròn, đậm, thân thiện. Màu: nền trắng hoặc pastel; 3–4 màu thương hiệu nhưng mỗi màn hình một màu chủ đạo. Chiều sâu: gần như phẳng, nút có "đế" dày. Hình ảnh: một nhân vật 2D do hoạ sĩ thiết kế, xuất hiện ở mọi khoảnh khắc cảm xúc. Chuyển động: nhân vật phản ứng (Rive).
- **Cảm giác cho app này:** vui, đúng chuẩn "như Duolingo". Hợp nhóm bạn mới tập.
- **Dễ dùng:** rất tốt (một việc mỗi màn hình, nút to).
- **Khả thi:** **khó nhất ở khâu nhân vật.** Cần thiết kế nhân vật thật sự và làm hoạt hình bằng Rive. Phần giao diện thì dễ. Rủi ro: làm nửa vời sẽ lại ra đúng thứ vừa bị chê.
- **Demo bài tập hợp:** yếu. Nhân vật kiểu khối tròn không dạy được kỹ thuật squat; các app họ này không phải dạy động tác. Sẽ phải dùng một nguồn hình thứ hai cho demo.

### D — Trang giấy (editorial sáng, tĩnh)

- **Ảnh tham khảo:** Things 3, Airbnb, Structured, Tiimo, Nike Training Club, How We Feel, stoic.
- **Định nghĩa.** Chữ: một phông grotesk tinh, hoặc serif cho tiêu đề (Tiimo, How We Feel); chênh cỡ mạnh. Màu: trắng hoặc trắng ấm + 1 màu nhấn. Chiều sâu: bóng mềm rất nhẹ, đường kẻ mảnh. Hình ảnh: ảnh nhỏ bo góc (Airbnb, NTC) hoặc icon đen đặc (stoic.). Chuyển động: tinh tế, gần như không thấy.
- **Cảm giác cho app này:** sạch, bình tĩnh, "người lớn". Ít phấn khích.
- **Dễ dùng:** tốt; ngoài trời và nơi sáng rất dễ đọc.
- **Khả thi:** cao nhất về kỹ thuật. Nhưng hướng "Sớm" cũ là một bản yếu của họ này. Thiếu ảnh và thiếu độ chính xác về chữ thì thành nhạt.
- **Demo bài tập hợp:** ảnh/video trên nền sáng, hoặc render kiểu Hevy trên nền trắng.

### E — Đất nặn 3D (3D mềm, vui)

- **Ảnh tham khảo:** 4 concept Dribbble (Nixtio, sleek.design, Heloxone, Dymas Alfin), Seven, Opal (viên đá 3D), (Not Boring) Habits (ngọn núi 3D).
- **Định nghĩa.** Chữ: grotesk bo nhẹ, đậm. Màu: nền trắng hoặc pastel rất nhạt (hoặc tối), 1–2 màu nhấn; màu sắc đến từ chính các hình 3D. Chiều sâu: hình 3D có ánh sáng mềm và bóng đổ là nguồn chiều sâu chính; thẻ bento bo góc lớn. Hình ảnh: nhân vật 3D kiểu đất nặn/đồ chơi, đồ vật 3D (tạ, cúp, ngọn lửa). Chuyển động: hình 3D xoay nhẹ, nảy.
- **Cảm giác cho app này:** vui như Duolingo nhưng "đắt" hơn nhờ ánh sáng và chất liệu. Một nhân vật duy nhất vừa là linh vật, vừa tập mẫu động tác, vừa ăn mừng.
- **Dễ dùng:** tốt, nếu giữ giao diện đơn giản và để hình 3D gánh phần giàu chi tiết.
- **Khả thi:** giao diện là CSS thường. Hình 3D **dựng sẵn thành ảnh/clip**, không cần chạy 3D thời gian thực trong app. Anh đã có quy trình tạo character sheet và clip bằng AI cho việc studio, nên đây là họ tận dụng được thế mạnh sẵn có nhất [D]. Rủi ro: nhân vật lệch giữa các clip; phải khoá bằng character sheet.
- **Lưu ý trung thực:** 4/7 ảnh tham khảo là concept Dribbble chứ chưa phải sản phẩm đã phát hành. Sản phẩm thật gần nhất đã thấy: Seven (nhân vật cách điệu kiểu 3D tô phẳng, kém tinh hơn concept), Opal và (Not Boring) Habits (vật thể 3D, không có nhân vật). Tức là chưa thấy app đã phát hành nào làm trọn họ này ở mức concept; đây là rủi ro.
- **Demo bài tập hợp:** chính nhân vật 3D đó, clip vòng lặp dựng sẵn. Hợp nhất trong 6 họ.

### F — Đồ hoạ đậm (tối giản, màu mạnh)

- **Ảnh tham khảo:** Streaks, (Not Boring) Habits (dấu tích), stoic. (bản tối), Partiful.
- **Định nghĩa.** Chữ: đậm, to, đôi khi viết hoa. Màu: một nền bão hoà duy nhất hoặc đen trắng tuyệt đối. Chiều sâu: không có, hoặc một vật 3D duy nhất. Hình ảnh: icon to, hình học. Chuyển động: mạnh, có nhịp.
- **Cảm giác cho app này:** cá tính, như áp phích.
- **Khả thi:** dễ về kỹ thuật, **rất khó về thẩm mỹ**. Đây là họ gần với ba hướng vừa bị chê nhất; Streaks và stoic. đẹp vì cực kỳ tiết chế. Không có chỗ tự nhiên cho demo bài tập.
- **Đánh giá:** không nên chọn. Đưa vào để thấy ranh giới.

### So sánh nhanh

| Họ | Gần "Duolingo trở lên" | Dễ trông đắt | Dễ dùng trong phòng tập | Khả thi một người làm | Có lời giải cho 90 demo |
|---|---|---|---|---|---|
| A Kính sáng | Trung bình | Cao | Khá | Trung bình | Có (video/3D) |
| B Phòng tập đêm | Trung bình | **Cao nhất** | **Tốt nhất** | Cao, nếu có hình | Có (video/clip) |
| C Bạn đồng hành | **Cao nhất** | Trung bình | Tốt | Thấp (nhân vật + Rive) | Yếu |
| D Trang giấy | Thấp | Khá | Tốt | **Cao nhất** | Có (ảnh/render) |
| E Đất nặn 3D | Cao | Cao | Tốt | Khá, nhờ dựng sẵn | **Tốt nhất** |
| F Đồ hoạ đậm | Thấp | Thấp–cao tuỳ tay | Khá | Cao về code | Không |

**Hai họ nên vào vòng trong: E và B.**
- **E** đạt đúng mong muốn "vui như Duolingo" mà không cần hoạ sĩ 2D và animator Rive, và giải luôn bài toán demo bằng cùng một nhân vật.
- **B** là công thức đã được chứng minh của fitness cao cấp, dễ đọc nhất trong phòng tập, và phần khó của nó (hình người thật, ánh sáng điện ảnh) trùng với thứ anh đang làm hằng ngày.
- Có thể lai: nền tối và kỷ luật màu của B + nhân vật 3D của E (xem concept Dymas Alfin trong moodboard). Lớp kính của A dùng được cho thanh điều hướng ở cả hai.

## 5. Demo 90 bài tập: các lựa chọn

### App khác đang làm gì [Q]

| App | Cách làm | Ghi chú |
|---|---|---|
| Fitbod | Video người thật, nền studio tối, màu trầm | Trang của Fitbod nói thư viện do huấn luyện viên được quay chuyên nghiệp [S2]; App Store ghi video nhiều góc [S2] |
| Future, Ladder, Peloton, Centr, Apple Fitness+ | Video người thật toàn màn hình | Là sản phẩm chính của họ |
| Alpha Progression, Caliber | Video người thật trong phòng tập + chữ hướng dẫn | Trông "thật" nhưng kém sang |
| Hevy | Render 3D mô hình giải phẫu, nhóm cơ chính tô đỏ, nền trắng | Rõ nhóm cơ, hơi lạnh |
| Seven | Nhân vật người cách điệu, trông như mô hình 3D tô màu phẳng, bóng đổ nhẹ, màu tươi | Gần họ E nhất, nhưng thô hơn các concept Dribbble |
| Fitbod, Strava, Caliber | Thêm bản đồ cơ thể tô màu nhóm cơ | Bổ trợ, không thay demo |
| free-exercise-db (mã nguồn mở) | 2 ảnh mỗi bài (đầu/cuối), hơn 800 bài, giấy phép Unlicense | Trang không nói nguồn gốc ảnh → quyền với ảnh [UNVERIFIED] [S3] |

Không tìm được nguồn nào nói Hevy hay Seven sản xuất hình bằng công cụ gì → [UNVERIFIED].

### Xếp hạng cho một PWA, 90 bài, một người làm [D]

| # | Cách | Đẹp | Khả thi | Dung lượng, kỹ thuật | Nhận xét |
|---|---|---|---|---|---|
| 1 | **Clip vòng lặp dựng sẵn của một nhân vật nhất quán** (3D đất nặn hoặc kiểu ảnh thật), tạo bằng AI từ ảnh tư thế đầu + cuối | Cao | Khá | MP4 H.264, 480×480, 2–4 giây, ước 150–400 KB/clip → 15–35 MB cho 90 bài; tải dần và lưu cache; trên iOS cần `muted playsinline` [D, chưa đo] | Có ánh sáng, chất liệu, chiều sâu. Rủi ro: AI làm sai kỹ thuật hoặc lệch nhân vật → mỗi clip phải có người biết kỹ thuật duyệt. Khoá nhân vật bằng character sheet |
| 2 | **2 ảnh tư thế (đầu/cuối) chuyển mờ qua lại**, cùng nhân vật | Khá–cao | **Cao** | WebP ~30–60 KB/ảnh → 5–10 MB | Kiểm soát kỹ thuật chính xác nhất. Chính là nguyên liệu đầu vào của cách 1, nên làm trước cho cả 90 bài |
| 3 | Ảnh/video người thật tự quay | Cao nếu quay tốt | Trung bình | Như cách 1 | Đáng tin nhất về kỹ thuật. Cần người mẫu, phòng tập, ánh sáng đồng nhất cho 90 bài. Nhóm bạn tự quay thì vui nhưng khó đều |
| 4 | three.js + mô hình 3D có xương + animation | Khá (dễ ra chất "game") | Thấp | three.js + mô hình GLB vài MB; chạy thời gian thực trên máy yếu | Xem mục giấy phép bên dưới. Phải tự làm animation cho phần lớn 90 bài bằng Blender |
| 5 | Rive (2D, có xương) | Cao **nếu có hoạ sĩ** | Thấp–trung bình | Runtime web mã nguồn mở MIT, không phí [S4]; WASM khoảng 78 KB [S2]; file `.riv` rất nhỏ | Tốt nhất cho linh vật và ăn mừng. Với 90 động tác thì vẫn là hình 2D phẳng phải vẽ và làm xương bằng tay. Gói miễn phí xuất file kèm màn hình chờ Rive; bỏ được từ gói 9 USD/tháng [S4] |
| 6 | Lottie | Trung bình | Trung bình | JSON, lớn hơn Rive theo số liệu của chính Rive [S2] | Hoạt hình mua sẵn mỗi cái một phong cách → lộn xộn |
| 7 | Người que SVG chạy bằng code (**Q4 hiện tại**) | **Thấp** | Cao nhất | Gần như 0 KB | Là nguyên nhân số 1 khiến mockup trông rẻ |

### Giấy phép nguồn animation 3D

- **Mixamo (Adobe).** Theo FAQ được Adobe đăng lại trên diễn đàn: dùng được cho dự án thương mại, không bắt ghi công; **không được phát tán file gốc** cho người ngoài nhóm; không được dùng để huấn luyện máy học [S2 — không đọc được trang FAQ gốc, bị 403]. Với PWA, file GLB nằm công khai trên web, ai cũng tải được → vùng xám [D]. Số động tác gym có sẵn trên Mixamo ít hơn 90 nhiều [UNVERIFIED, theo trí nhớ].
- **Gói trả tiền** (MoveKit, CGTrader, Superhive): có các gói animation gym bán theo clip hoặc theo gói; điều khoản cụ thể chưa đọc [UNVERIFIED].
- **AMASS:** giấy phép chỉ cho nghiên cứu khoa học, giáo dục, dự án nghệ thuật phi thương mại; cấm dùng trong sản phẩm thương mại và cấm phát tán lại [S5]. Không dùng được.
- **CMU Motion Capture Database:** không đọc được trang điều khoản trong phiên này (lỗi chứng chỉ) → [UNVERIFIED]. Dù giấy phép thế nào, đây là dữ liệu chuyển động thô, vẫn phải gắn vào mô hình và chỉnh tay.
- **Muscle & Motion:** điều khoản chuẩn cấm dùng thương mại [S2].

### Khuyến nghị

1. **Mở lại Q4.** Bỏ người que SVG làm hình chính.
2. Tạo **một nhân vật** (character sheet nhiều góc) theo họ phong cách được chọn.
3. Làm **2 ảnh tư thế đầu/cuối cho cả 90 bài** (cách 2). Có người biết kỹ thuật duyệt từng cặp.
4. Nâng **khoảng 20 bài phổ biến nhất** lên clip vòng lặp (cách 1), rồi làm dần phần còn lại.
5. Giữ dữ liệu tư thế và câu nhắc theo pha của brief cũ làm lớp chữ chồng lên clip.
6. Rive chỉ dùng cho **một** khoảnh khắc ăn mừng, và chỉ khi chọn họ C hoặc E.

Toàn bộ khuyến nghị này dựa trên phán đoán, **chưa thử thực tế**. Bước 3 và 4 tốn công tạo hình hàng loạt. Nên thử 5 bài trước (squat, đẩy ngực tạ đơn, kéo xô, plank, RDL) để biết AI giữ nhân vật và làm đúng kỹ thuật đến đâu, rồi mới cam kết.

## 6. Việc cần người dùng quyết

1. Chọn 1–2 họ phong cách trong moodboard.
2. Đồng ý mở lại Q4 (đổi người que SVG sang clip/ảnh dựng sẵn) hay không.
3. Nếu chọn B: dùng hình người kiểu ảnh thật hay nhân vật 3D?

## Nguồn

- [S1] Rive blog — Duolingo's AI-powered Video Call brings Lily to life: https://rive.app/blog/duolingo-s-ai-powered-video-call-brings-lily-to-life ; Rive blog — Creative technologists at Duolingo (chỉ đọc đoạn trích): https://rive.app/blog/creative-technologists-duolingo-s-solution-to-the-designer-to-developer-handoff
- [S2] Nguồn thứ cấp, đọc qua kết quả tìm kiếm:
  - Mixamo FAQ đăng lại trên Adobe Community: https://community.adobe.com/t5/mixamo-discussions/mixamo-faq-licensing-royalties-ownership-eula-and-tos/td-p/13234775 (trang gốc https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html trả về 403)
  - Kích thước WASM của Rive: https://dev.to/alex_barashkov/optimization-techniques-for-rive-animations-in-react-apps-1a8p ; so sánh của Rive: https://rive.app/blog/rive-as-a-lottie-alternative ; phản biện của LottieFiles: https://lottiefiles.com/blog/working-with-lottie-animations/lottiefiles-or-rive
  - Fitbod về thư viện bài tập: https://fitbod.me/about-fitbod-exercises ; trang App Store Fitbod: https://apps.apple.com/us/app/id1041517543
  - Headspace: https://blakecrosley.com/guides/design/headspace ; https://www.itsnicethat.com/articles/italic-studio-headspace-graphic-design-project-250424
  - Muscle & Motion: https://www.muscleandmotion.com/ ; MoveKit: https://alternativeto.net/software/movekit/about/
- [S5] AMASS licence: https://amass.is.tue.mpg.de/license.html
- [S3] free-exercise-db: https://github.com/yuhonas/free-exercise-db
- [S4] Rive pricing: https://rive.app/pricing
- Apple Newsroom — Liquid Glass (09/06/2025): https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/
- Apple Design Awards: https://developer.apple.com/design/awards/
- Dribbble — tìm "fitness app 3d": https://dribbble.com/search/fitness-app-3d

### Trang App Store của các app đã giữ ảnh

- Airbnb: https://apps.apple.com/us/app/airbnb/id401626263
- Alpha Progression Gym Tracker: https://apps.apple.com/us/app/alpha-progression-gym-tracker/id1462277793
- Bevel: AI Health Coach: https://apps.apple.com/us/app/bevel-ai-health-coach/id6456176249
- Caliber: Strength Training: https://apps.apple.com/us/app/caliber-strength-training/id1482405410
- How We Feel: https://apps.apple.com/us/app/how-we-feel/id1562706384
- Duolingo: Learn Languages: https://apps.apple.com/us/app/duolingo-learn-languages/id570060128
- Finch: Self-Care Pet: https://apps.apple.com/us/app/finch-self-care-pet/id1528595748
- Fitbod: Gym & Fitness Planner: https://apps.apple.com/us/app/fitbod-gym-fitness-planner/id1041517543
- Apple Fitness: https://apps.apple.com/us/app/apple-fitness/id1208224953
- Future Pro: Personal Training: https://apps.apple.com/us/app/future-pro-personal-training/id1288178982
- Gentler Streak Workout Tracker: https://apps.apple.com/us/app/gentler-streak-workout-tracker/id1576857102
- Headspace: Sleep & Meditation: https://apps.apple.com/us/app/headspace-sleep-meditation/id493145008
- Hevy - Workout Tracker Gym Log: https://apps.apple.com/us/app/hevy-workout-tracker-gym-log/id1458862350
- LADDER Strength Training Plans: https://apps.apple.com/us/app/ladder-strength-training-plans/id1502936453
- Linear Mobile: https://apps.apple.com/us/app/linear-mobile/id1645587184
- (Not Boring) Habits: https://apps.apple.com/us/app/not-boring-habits/id1593891243
- Nike Training Club: https://apps.apple.com/us/app/nike-training-club/id301521403
- Opal: Screen Time Control: https://apps.apple.com/us/app/opal-screen-time-control/id1497465230
- Oura: https://apps.apple.com/us/app/oura/id1043837948
- Partiful: Party Invite Maker: https://apps.apple.com/us/app/partiful-party-invite-maker/id1662982304
- Peloton: Fitness & Workouts: https://apps.apple.com/us/app/peloton-fitness-workouts/id792750948
- Seven: 7 Minute Workout: https://apps.apple.com/us/app/seven-7-minute-workout/id650276551
- stoic. journal & mental health: https://apps.apple.com/us/app/stoic-journal-mental-health/id1312926037
- Streaks: https://apps.apple.com/us/app/streaks/id963034692
- Structured: Daily Planner Todo: https://apps.apple.com/us/app/structured-daily-planner-todo/id1499198946
- Things 3: https://apps.apple.com/us/app/things-3/id904237743
- Tiimo: To-Do List Planner: https://apps.apple.com/us/app/tiimo-to-do-list-planner/id1480220328
- Water tracker Waterllama: https://apps.apple.com/us/app/water-tracker-waterllama/id1454778585
- WHOOP: https://apps.apple.com/us/app/whoop/id933944389
