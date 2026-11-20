# 06 — Tủ đồ thưởng cho avatar (bản hệ thống, chưa gắn nhân vật)

Ngày: 2026-11-20. Đọc cùng: [00-plan.md](../research/00-plan.md) mục 4, [03-app-patterns.md](../research/03-app-patterns.md) mục 8, [01-design-brief.md](01-design-brief.md) (giọng "bạn tập, không quát").

**Phạm vi đã đổi giữa chừng.** Ba nhân vật Nghé / Ớt / Bự bị loại (chuyện nền yếu, không liên quan nhau); dàn nhân vật mới sẽ thiết kế riêng. Vì vậy file này **không** có hồ sơ nhân vật, không có lời thoại và không có ảnh dựng Blender. Mọi thứ viết để dùng được cho bất kỳ dàn nhân vật nào; luật vừa đồ mô tả theo kiểu thân hình chứ không theo tên.

Số nguồn (S1, U3…) là số riêng của file này, không trùng với số trong 03-app-patterns.

Nhãn: **[S]** nguồn đã đọc trong phiên này (qua công cụ tóm tắt trang, nên là diễn giải) · **[U]** chỉ thấy ở đoạn trích tìm kiếm hoặc nhớ lại, chưa kiểm chứng · **[D]** quyết định thiết kế của tôi, chưa có nghiên cứu xác thực.

---

## 0. Tóm tắt

- **Không tiền ảo, không cửa hàng, không hộp may rủi, không món nào hết hạn.** Đồ chỉ có một cách lấy: đến tập.
- **Đơn vị thưởng là "mảnh".** Mỗi buổi đạt cho 1 mảnh, bằng 1/N món (N = mục tiêu tuần tự chọn), tối đa một món mỗi tuần. Đầy thanh thì nhận 1 món do chính mình chọn trong 3 món đang bày. Người tập 2 buổi/tuần và người tập 5 buổi/tuần nhận đồ nhanh như nhau.
- **Tiến độ không bao giờ mất.** Tuần hụt, tuần nghỉ có phép, nghỉ cả tháng: phần đã tích vẫn nằm đó.
- **Bậc đồ nói lên cách lấy, không phải xác suất:** *thường* = lộ trình tuần, *hiếm* = mốc và sự kiện, *huyền thoại* = mốc dài.
- Danh mục đề xuất: 4 món khởi đầu + 32 món (18 thường, 10 hiếm, 4 huyền thoại), sau đó là bản màu.
- Có một câu hỏi cần bạn chốt ở mục 9: bạn nói "thưởng đồ cho mỗi ngày tập thành công"; tôi đề xuất mỗi ngày tập cho một **mảnh** chứ không cho hẳn một món, lý do nằm ở bảng tính mục 3.3.

---

## 1. Nghiên cứu: các app khác làm tủ đồ thưởng thế nào

Nhiều trang chặn truy cập tự động (Fandom, Bulbapedia, trung tâm trợ giúp của Finch, PubMed), nên một số ô để trống hoặc gắn [U]. Ô nào ghi "chưa kiểm chứng" nghĩa là không tìm được nguồn đọc được, không phải là không có.

### 1.1 Bảng so sánh

| App | Kiếm hay mua | Bậc hiếm | Sưu tập | Theo mùa / giới hạn | Hộp may rủi hay lộ trình | Bị chê gì |
|---|---|---|---|---|---|---|
| **Finch** | Tiền ảo kiếm bằng cách hoàn thành việc tự chăm sóc, tiêu vào quần áo và đồ trang trí tổ [S1]. Gói trả tiền Finch Plus thêm đồ vào cửa hàng [S1]; giá mua trong app 5,99–69,99 USD [S2] | Chưa kiểm chứng | Chưa kiểm chứng | Sự kiện theo tháng: làm việc tự chăm sóc để nhận thú nhỏ và đồ theo mùa [S2]. Tắt được sự kiện trong cài đặt [U3] | Sự kiện là lộ trình theo ngày; người trả tiền tới đích sớm hơn (ngày 20 so với ngày 25) [U3]. Cửa hàng xoay vòng hằng ngày: chỉ có lời kể người dùng [U4] | Người dùng lâu năm nói có người tích việc cho có để lấy thưởng [S2]. Cửa hàng ngẫu nhiên bày món không đủ tiền mua [U4] |
| **Duolingo** | Streak Freeze mua bằng gem, trang bị tối đa 2 [S5]. Trang phục cho Duo: chỉ nhớ lại, chưa kiểm chứng [U] | Không thấy | Không thấy | Chưa kiểm chứng | Streak Society: "hội" dành cho người chạm mốc streak [S6]; mốc và phần thưởng cụ thể mâu thuẫn giữa các hướng dẫn [U7] | Chính Duolingo viết rằng streak chạy bằng nỗi sợ mất, và mất streak "rất nản" [S5, S8] |
| **Habitica** | Đồ cơ bản mua bằng vàng (kiếm từ việc hoàn thành thói quen), theo thứ tự cố định từng lớp nhân vật. Gem là tiền trả phí [S9] | Không có bậc màu; đồ chia theo lớp và nguồn [S9] | Có thành tựu "đủ bộ" mở khoá Tủ thần [U10] | 4 lễ hội theo mùa; đồ mới mua bằng vàng trong mùa, hết mùa phải mua bằng gem [S9] | **Tủ thần (Enchanted Armoire):** 100 vàng một lượt bốc ngẫu nhiên trong hơn 350 món. Người đăng ký nhận bộ đồ độc quyền mỗi tháng [S9] | Chưa kiểm chứng. Đáng lưu ý: hết máu thì mất một cấp, toàn bộ vàng và một món đồ [S9] |
| **Pokémon GO** | Đồ mở theo huy chương vẫn phải mua bằng xu, mà xu mua được bằng tiền thật [S11]. Có món tặng không (áo UNIQLO) [S12] | Không có bậc món; khoá theo bậc huy chương: bộ chạy bộ mở ở 10 / 100 / 1.000 km [S11] | Chưa kiểm chứng | Đồ hợp tác thương hiệu [S12] | Hoàn toàn theo ngưỡng, không có hộp may rủi cho đồ avatar | Đồ từng khoá theo giới tính nên có người không thấy món nào [U13] |
| **Fortnite** | Battle Pass 1.000 V-Bucks, chơi đủ thì kiếm lại được V-Bucks [S14] | Từng có bậc màu, **đã bỏ** từ 4/2024; người chơi than "món nào cũng như nhau" [S15] | — | Bị kiện vì đồng hồ đếm ngược ở cửa hàng; cơ quan Hà Lan phạt, Epic nói đã bỏ đồng hồ [U16] | Battle Pass là lộ trình thấy trước. 2019: đổi hộp mù trả tiền thành hộp nhìn thấy bên trong trước khi mua [S17, chỉ đọc được tiêu đề] | FTC 12/2022: hoàn 245 triệu USD vì giao diện gài bấm nhầm là mất tiền, khoá tài khoản người khiếu nại [S18] |
| **Fall Guys** | Tiền trả phí mua pass và hầu hết món từ bậc Uncommon trở lên; tiền kiếm được chỉ mua món Common [S19] | Bậc hiếm gắn thẳng với loại tiền [S19] | Hạng Vương miện: lên hạng thì mở trang phục [S19] | — | Pass 100 bậc, 50 bậc miễn phí [S19] | Người chơi phản đối việc tiền kiếm được bị mất giá [U20] |
| **Animal Crossing: New Horizons** | Toàn bộ bằng tiền trong game; không có đường nối với tiền thật [S21, S22] | Không thấy | Mua món nào thì món đó vào catalogue; thành tựu ở mốc 100–500 món [S21] | Đồ lễ hội chỉ bán 1–15/2 [S23] | Tiệm quần áo đổi hàng mỗi ngày [S23]; thành tựu Nook Miles là lộ trình cố định, thấy trước [S22] | Chưa kiểm chứng. Đáng lưu ý: giới hạn đặt 5 món/ngày để ghìm tốc độ [S21] |
| **Apple Fitness** | Chỉ kiếm, không mua: kỷ lục cá nhân, chuỗi ngày, mốc lớn [S24] | Không; chỉ chia nhóm | Phòng trưng bày hiện cả giải đang dở [S24] | Giải Ngày Trái Đất: phải tập 30 phút **đúng ngày 22/4**; Apple đã giảm số thử thách kiểu này trong 2024 [S25] | Thấy trước hoàn toàn | Trước watchOS 11, nghỉ một ngày là mất chuỗi [S26]; "không hiểu rằng hồi phục là một phần của tập luyện" [S27]; có người bỏ đồng hồ sau khi đi lại trong đêm để đóng vòng [S28]. Nay cho tạm dừng tới 90 ngày, đặt mục tiêu theo ngày trong tuần [S29] |

**Điều được ghi nhận là giữ chân người dùng**

| App | Ghi nhận |
|---|---|
| Finch | Phản ứng ăn mừng của thú nuôi và cảm giác muốn "về kể lại" cho nó; người viết đặt Finch đối lập với các app "làm bạn thấy có lỗi để quay lại" [S1] |
| Duolingo | Hoạt ảnh ở mốc streak; hạ rào giữ streak (xem bảng 1.2 và 03-app-patterns mục 8a) [S5] |
| Animal Crossing | Nook Miles+ là nguồn mục tiêu nhỏ làm mới mỗi ngày [S22] |
| Apple Fitness | Mỗi thứ Hai đồng hồ gợi ý mục tiêu dựa trên tuần trước [S29] |
| Habitica, Pokémon GO, Fortnite, Fall Guys | Chưa kiểm chứng: không tìm được nguồn đọc được |

### 1.2 Bằng chứng chung

| Chủ đề | Nguồn nói gì |
|---|---|
| Hộp may rủi | Khảo sát 7.422 người chơi: mức tiêu tiền vào hộp may rủi đi cùng mức độ nghiện cờ bạc (η² = 0,054), mạnh hơn nhiều so với các khoản mua khác (η² = 0,004); chưa rõ chiều nhân quả [S30]. Nghiên cứu này nói về hộp **trả tiền**; chưa có gì kiểm tra riêng phần thưởng ngẫu nhiên miễn phí |
| Thưởng làm mòn động lực tự thân | Tổng hợp 128 thí nghiệm: phần thưởng **báo trước** gắn với việc tham gia / hoàn thành / thành tích đều làm giảm động lực tự thân (d = −0,40 / −0,36 / −0,28); lời khen làm tăng (0,33) [S31]. Có một tổng hợp khác phản bác [U32] |
| Mặt tối của công nghệ thể dục | Tổng quan 2024: định lượng, game hoá và tính năng xã hội trong app thể dục đi kèm căng thẳng, mặc cảm vì hụt mục tiêu, và tập bù quá mức [S33, bản tóm tắt của trường] |
| Bằng chứng ngược | Luận văn 79 người dùng Strava: huy hiệu và bảng xếp hạng đi cùng gắn bó, không thấy liên hệ trực tiếp với căng thẳng (mẫu nhỏ) [U34] |
| Streak | Số liệu tự công bố của Duolingo, không có phương pháp: cho trang bị 2 freeze thì người học hằng ngày +0,38%; hoạt ảnh mốc streak làm retention ngày 7 của người mới +1,7% [S5]. Người học dồn dập bỏ nhiều hơn người học đều [S8] |

Không tìm được nghiên cứu bình duyệt nào riêng về "lo âu vì streak", và không tìm được nghiên cứu nào tách riêng tác động của trang phục avatar lên việc tập.

### 1.3 Rút ra cho app này

| Câu hỏi | Điều thấy được | Quyết định [D] |
|---|---|---|
| Kiếm hay mua | Chỗ có tiền thật là chỗ có kiện tụng và phàn nàn về tiền (Fortnite, Fall Guys). Animal Crossing và Apple Fitness chỉ kiếm, không thấy phàn nàn loại này | Chỉ kiếm. Không có cả tiền ảo: tiền ảo sinh ra cửa hàng, cửa hàng sinh ra "thiếu một chút nữa" |
| Bậc hiếm | Fortnite bỏ bậc màu mà game vẫn sống; Pokémon GO và Apple không có bậc món, chỉ có ngưỡng | Giữ 3 bậc như yêu cầu, nhưng bậc = **cách lấy**, không phải tỉ lệ rơi |
| Sưu tập | Catalogue của Animal Crossing và phòng giải của Apple đều **hiện cả món chưa có** | Tủ đồ hiện bóng mờ món chưa có, kèm điều kiện mở bằng một câu |
| Theo mùa | Giải "đúng ngày 22/4" của Apple và đồng hồ đếm ngược của Fortnite là hai kiểu bị chê | Có đồ theo mùa, cửa sổ dài 4 tuần, **năm nào cũng quay lại**, không đồng hồ đếm ngược |
| May rủi hay lộ trình | Bốc ngẫu nhiên có ở Habitica (Tủ thần), Fortnite (hộp llama, sau đổi thành nhìn thấy trước) và trứng nở ngẫu nhiên của Finch [U3]; bằng chứng xấu là về hộp trả tiền | Lộ trình thấy trước + tự chọn 1 trong 3. Phần bất ngờ duy nhất là 3 món nào được bày |
| Giữ động lực | Lời khen tăng động lực; thưởng báo trước làm giảm | Món thưởng nhỏ, đi kèm lời nhận xét về chính buổi tập. Tắt được cả tủ đồ trong cài đặt |
| Kiệt sức | Apple phải thêm tạm dừng vòng; Duolingo thấy người dồn dập bỏ nhiều hơn | Có trần theo tuần, có trần theo ngày, mảnh không mất (mục 3) |

---

## 2. Ô trang bị

| Ô | Chứa gì | Số món mặc cùng lúc |
|---|---|---|
| **Đầu** | mũ, nón, băng đô, mũ bảo hiểm | 1 |
| **Áo** | áo phông, ba lỗ, áo đấu, áo khoác, áo dài | 1 |
| **Quần** | quần đùi, quần đá bóng, quần dài | 1 |
| **Giày** | giày, dép, kèm tất nếu có | 1 |
| **Phụ kiện** | chia 5 điểm gắn: *mặt* (kính), *cổ* (khăn), *lưng* (balo, nón đeo sau lưng), *eo* (đai), *tay* (găng, băng cổ tay, đồ cầm tay) | 2, khác điểm gắn |
| **Nền** | màu nền, hoạ tiết, hào quang sau lưng | 1 |

Luật chung [D]:
- Ô nào cũng có món mặc định, không bao giờ trống.
- Mặc đủ một bộ theo chủ đề thì được thêm một **dáng ăn mừng riêng của bộ đó**. Đây là lý do để sưu tập đủ bộ mà không cần thêm món.
- Nền và hào quang là thứ hiện trên bảng nhóm và thẻ chia sẻ, nên dành cho mốc dài.
- Người dùng lưu được 3 bộ phối sẵn.

---

## 3. Luật thưởng

### 3.1 Mảnh và món

1. **Buổi đạt** = buổi có ít nhất 1 bài ghi đủ set (đúng định nghĩa ở 03-app-patterns mục 8c). Buổi ngắn lúc mệt và buổi vùng vàng / đỏ đã cắt bài đều tính. Buổi vùng đỏ đổi hẳn sang đi bộ 20–30 phút cũng nên tính [D: định nghĩa buổi đạt hiện chưa nói tới trường hợp này, cần bổ sung ở kế hoạch].
2. Mỗi buổi đạt cho **1 mảnh**, tối đa 1 mảnh mỗi ngày. Một mảnh làm đầy thêm **1/N thanh tiến độ**, với N là mục tiêu tuần **tại lúc tập**. Thanh tăng tối đa đúng 1 món mỗi tuần.
3. Đầu mỗi chu kỳ, app bày **3 món bậc thường** chưa có; người dùng chọn 1. Thanh đầy thì món về tủ, app bày 3 món mới.
   Tiến độ lưu dưới dạng **phần của một món**, không phải số mảnh. Nhờ vậy đổi N không lách được: đặt N = 6, tập 6 buổi rồi hạ xuống N = 2 vẫn chỉ ra đúng 1 món cho tuần đó.
4. Buổi vượt quá N trong tuần: không mảnh, không gì cả. Màn hình kết thúc buổi vẫn khen bình thường và nói rõ "tuần này đủ rồi".
5. Tiến độ **không bao giờ mất và không có hạn**. Tuần chỉ tập 1/3 buổi thì 1/3 món đó nằm chờ sang tuần sau.
6. Hết món bậc thường thì chu kỳ chuyển sang **bản màu** của món đã có.

Hệ quả: ai đạt mục tiêu của chính mình thì cứ 1 tuần được 1 món, bất kể N. Người chỉ đạt 2/3 buổi mỗi tuần vẫn được 1 món sau 1,5 tuần, không bị trắng tay.

### 3.2 Sự kiện trong app → phần thưởng

| Sự kiện | Thưởng | Bậc | Ghi chú |
|---|---|---|---|
| Xong onboarding | Bộ khởi đầu 4 món, tự chọn màu | — | |
| Buổi đạt | 1 mảnh = 1/N món | thường | trần 1 mảnh/ngày, 1 món/tuần |
| Thanh đầy | 1 món đã chọn | thường | |
| Đạt mục tiêu tuần | Không thêm món. Chỉ cộng streak | — | tránh thưởng hai lần cho cùng một việc |
| Streak 4 tuần | Găng tay hở ngón | hiếm | |
| Streak 12 tuần | Đai vô địch | huyền thoại | |
| Streak 26 tuần | Hào quang "Nửa năm" | huyền thoại | |
| 10 / 25 / 50 **tuần đạt cộng dồn** | Giày đế bẹt / Áo dài cách tân / Nón lá sơn mài vàng | hiếm / huyền thoại / huyền thoại | Không cần liên tiếp. Người từng đứt streak vẫn tới được hai món huyền thoại |
| PR đầu tiên | Đai lưng tập tạ | hiếm | Một lần duy nhất. PR về sau chỉ có lời khen, không có đồ (mục 4, luật 6) |
| Thử thách nhóm thành công | Áo đội | hiếm | **Cả nhóm cùng nhận**, kể cả người góp ít |
| Streak nhóm 4 tuần | Khăn cổ động của đội | hiếm | |
| Quay lại sau khi vắng từ 3 tuần | Hoodie "Tái xuất" | hiếm | Một lần. Ai cũng nhận được món này ở mốc **12 tuần đạt cộng dồn**, nên không ai phải nghỉ mới có. Người vắng rồi quay lại có thể nhận sớm hơn vài tuần, nhưng đã mất các món thường của những tuần vắng |
| Trong cửa sổ mùa, thanh đầy | Món theo mùa, thay cho món thường của chu kỳ đó nếu người dùng chọn | hiếm | 4 tuần, năm sau quay lại |

Mốc theo **số buổi** (buổi thứ 10 / 50 / 100 trong kế hoạch) giữ làm huy hiệu, **không gắn đồ**: người tập 5 buổi/tuần chạm buổi thứ 50 ở tuần 10, người tập 2 buổi/tuần phải tới tuần 25.

### 3.3 Bảng tính nhịp phát đồ

**Phương án đề xuất (mảnh, chuẩn hoá theo N).** Giả định tuần nào cũng đạt, có PR đầu tiên trong tháng đầu, nhóm thắng 1 thử thách và gặp 2 mùa trong nửa năm.

| Sau | Khởi đầu | Món thường | Mốc + sự kiện | Tổng món | Bản màu |
|---|---|---|---|---|---|
| 1 tuần | 4 | 1 | 0 | 5 | 0 |
| 4 tuần | 4 | 4 | 2 (streak 4, PR) | 10 | 0 |
| 12 tuần | 4 | 12 | 6 (+ 10 tuần cộng dồn, streak 12, hoodie, áo đội) | 22 | 0 |
| 26 tuần | 4 | 18 (hết) | 10 (+ streak 26, 25 tuần cộng dồn, 2 món mùa) | 32 | 6 |

Con số như nhau cho N = 2 và N = 5, và không đổi khi người dùng đổi N giữa chừng, vì trần là 1 món mỗi tuần.

**Phương án "mỗi buổi một món" (để so).**

| Sau | N = 2 | N = 5 |
|---|---|---|
| 4 tuần | 8 món | 20 món |
| 12 tuần | 24 món | 60 món |
| 26 tuần | 52 món | 130 món |

Với danh mục khoảng 30 món, người tập 5 buổi/tuần hết đồ ở tuần 6, trước cả mốc 12 tuần. Người tập 5 buổi có tủ đồ gấp 2,5 lần người tập 2 buổi, ngược với nguyên tắc "xếp theo % mục tiêu của riêng mỗi người" ở kế hoạch mục 4, và tạo lý do để người mới tự nâng N lên 5–6 trong khi kế hoạch mục 3.2 khuyên họ tập 3 buổi.

---

## 4. Luật chống tập quá sức và chống bóc lột

| # | Luật | Chặn điều gì |
|---|---|---|
| 1 | Trần 1 mảnh/ngày, 1 món/tuần | Tập hai buổi một ngày, tập 7 ngày/tuần để lấy đồ |
| 2 | Buổi vượt N không cho gì | Như trên |
| 3 | Tiến độ không mất, không hạn | Cố tập khi ốm để "khỏi phí" |
| 4 | **Tuần nghỉ có phép đóng băng mọi bộ đếm**: streak, cửa sổ mùa, tiến độ thử thách cá nhân. Nghỉ có phép trong mùa thì món mùa được giữ chỗ tới tuần quay lại | Mất đồ mùa vì ốm đúng dịp |
| 5 | Tuần deload và buổi vùng vàng / đỏ cho mảnh như buổi thường | Giấu mệt để được tính |
| 6 | **Không món nào gắn với mức tạ, cân nặng, số đo hay ngoại hình.** PR chỉ thưởng đồ đúng một lần | Ép tăng tạ để lấy đồ; thưởng cho việc gầy đi |
| 7 | Không tiền thật, không tiền ảo, không cửa hàng | Các phàn nàn về tiền ở Fortnite và Fall Guys |
| 8 | Không hộp may rủi; luôn thấy trước món sắp nhận | [S30] |
| 9 | Không đồng hồ đếm ngược, không "chỉ còn 2 ngày"; đồ mùa quay lại hằng năm | [S25], [U16] |
| 10 | Không món nào bị thu hồi | Cơ chế mất đồ của Habitica [S9] |
| 11 | Không thông báo đẩy nào nhắc về món đang dở | Giọng app: ngày nghỉ không có lời nhắc (brief, dòng 8) |
| 12 | Tuần hụt: avatar mặc nguyên đồ, không buồn, không xuống sắc. Màn hình chỉ hiện số mảnh đang có | Cảm giác tội lỗi |
| 13 | Thưởng nhóm phát cho cả nhóm; không có món "người đứng đầu bảng" | Bảng nhóm thành cuộc đua khối lượng |
| 14 | Tắt được tủ đồ; khi tắt, streak và huy hiệu vẫn chạy | Người thấy đồ thưởng làm mình phân tâm [S31] |
| 15 | Nếu hơn nửa số buổi trong 3 tuần là vàng / đỏ (luật chống lạm dụng, kế hoạch mục 3.6), app gợi ý giảm N; giảm N **không** làm mất tiến độ và không làm chậm nhịp nhận đồ (cũng không làm nhanh hơn: trần vẫn là 1 món/tuần) | Giữ N cao vì sợ thiệt |

Lỗ hổng đã biết: người dùng có thể tích cho có để lấy mảnh, đúng điều Finch bị phàn nàn [S2]. App không chống được bằng kỹ thuật; với nhóm 2–10 người quen nhau, feed nhóm là thứ giữ cho mọi người thật thà [D].

---

## 5. Danh mục

Tất cả là đề xuất [D]. Không món nào dùng logo, tên hay màu áo của câu lạc bộ, giải đấu hoặc nhãn hàng có thật.

### 5.1 Bộ khởi đầu (4)

| # | Món | Ô |
|---|---|---|
| K1 | Áo phông trơn | Áo |
| K2 | Quần đùi | Quần |
| K3 | Giày bata trắng | Giày |
| K4 | Băng cổ tay vải | Phụ kiện · tay |

Người dùng chọn một màu chủ đạo lúc onboarding.

### 5.2 Bậc thường (18) — lộ trình tuần, mỗi món có 3 bản màu

| # | Món | Ô | Bộ |
|---|---|---|---|
| T1 | Băng đô thập niên 80 | Đầu | **Gym cổ điển** |
| T2 | Áo ba lỗ | Áo | Gym cổ điển |
| T3 | Quần đùi viền sọc | Quần | Gym cổ điển |
| T4 | Giày thể thao + tất cao sọc | Giày | Gym cổ điển |
| T5 | Khăn bông vắt cổ | Phụ kiện · cổ | Gym cổ điển |
| T6 | Áo đấu phủi, số áo tự chọn | Áo | **Đá phủi** |
| T7 | Quần đá bóng | Quần | Đá phủi |
| T8 | Giày đinh sân cỏ nhân tạo + tất kéo cao | Giày | Đá phủi |
| T9 | Băng đội trưởng | Phụ kiện · tay | Đá phủi |
| T10 | Nón lá thể thao (quai vải dù, viền phản quang) | Đầu | **Vỉa hè** |
| T11 | Sơ mi hoa cộc tay | Áo | Vỉa hè |
| T12 | Quần đùi hoa | Quần | Vỉa hè |
| T13 | Dép tổ ong | Giày | Vỉa hè |
| T14 | Cốc trà đá | Phụ kiện · tay | Vỉa hè |
| T15 | Mũ bảo hiểm nửa đầu + kính gắn trên mũ | Đầu | **Phượt** |
| T16 | Áo khoác gió | Áo | Phượt |
| T17 | Balo | Phụ kiện · lưng | Phượt |
| T18 | Khăn rằn | Phụ kiện · cổ | Phượt |

### 5.3 Bậc hiếm (10) — mốc và sự kiện

| # | Món | Ô | Mở khi |
|---|---|---|---|
| H1 | Đai lưng tập tạ | Phụ kiện · eo | PR đầu tiên |
| H2 | Găng tay hở ngón | Phụ kiện · tay | Streak 4 tuần |
| H3 | Giày đế bẹt tập tạ | Giày | 10 tuần đạt cộng dồn |
| H4 | Hoodie "Tái xuất" | Áo | Quay lại sau khi vắng từ 3 tuần, **hoặc** 12 tuần đạt cộng dồn |
| H5 | Áo đội (màu và tên do nhóm đặt) | Áo | Thử thách nhóm thành công lần đầu |
| H6 | Khăn cổ động của đội | Phụ kiện · cổ | Streak nhóm 4 tuần |
| H7 | Bao lì xì + nền hoa đào / hoa mai (tự chọn) | Nền | Mùa Tết |
| H8 | Kính râm thể thao | Phụ kiện · mặt | Mùa hè |
| H9 | Đèn ông sao | Phụ kiện · tay | Mùa Trung thu |
| H10 | Áo đấu "Sân nhà" sọc dọc, lấy cảm hứng áo đấu chuyên nghiệp | Áo | Mùa bóng (thời điểm cần chốt theo lịch thật [U]) |

Bộ **Đồ nghề** = H1 + H2 + H3 + T2. Bộ **Đội mình** = H5 + H6 + T7.

### 5.4 Bậc huyền thoại (4) — mốc dài

| # | Món | Ô | Mở khi |
|---|---|---|---|
| L1 | Đai vô địch (đai to bản, mặt khoá vàng) | Phụ kiện · eo | Streak 12 tuần |
| L2 | Hào quang "Nửa năm" | Nền | Streak 26 tuần |
| L3 | Áo dài cách tân tập gym (tà ngắn ngang hông, xẻ cao, mặc với quần thể thao) | Áo | 25 tuần đạt cộng dồn |
| L4 | Nón lá sơn mài vàng | Đầu | 50 tuần đạt cộng dồn |

Bộ **Tết** = L3 + H7 + T10 hoặc L4.

### 5.5 Sau món thứ 36

Bản màu cho 18 món thường (3 bản mỗi món, tức thêm 54 chu kỳ). Bộ mới thêm theo đợt, mỗi đợt 4–5 món; ý tưởng dự trữ: đồ bơi hồ công cộng, đồ võ cổ truyền, đồ chạy bộ ven hồ sáng sớm, áo mưa cánh dơi.

---

## 6. Luật vừa đồ cho nhiều kiểu thân hình

Dàn nhân vật mới chưa có, nhưng yêu cầu "mỗi nhân vật một khối gốc, tỉ lệ phóng đại" ở [03-character-research.md](03-character-research.md) vẫn còn, nên hệ thống phải chịu được ít nhất ba kiểu: **khối hộp** (đầu rất to, không cổ, tay chân ngắn), **que** (người nhỏ, tay chân mảnh, đầu to) và **khối cầu** (thân rất to, đầu nhỏ, chân ngắn).

### 6.1 Nguyên tắc

1. **Mọi món mặc được trên mọi nhân vật.** Không có món "chỉ dành cho người gầy". Không ghi cỡ ở bất kỳ đâu.
2. **Món đồ là công thức, không phải khối lưới co giãn.** Mỗi món dựng lại từ các điểm neo của từng nhân vật. Co giãn một khối lưới chung sẽ làm vành nón méo và sọc áo giãn không đều trên thân tròn.
3. **Món nhận diện của nhân vật không bao giờ bị che.** Mũ nón phải khoét, lệch hoặc đeo ra sau lưng để nhường chỗ.
4. **Mặt là kênh diễn chính.** Không món nào được che lông mày hoặc mắt ở dáng mặc định.
5. **Đồ lên thân nào cũng phải đẹp theo kiểu của thân đó.** Không dùng thân to làm trò cười (áo cố tình chật, cúc bung). Điểm này đã bị nêu là rủi ro ở 04-character-concepts.

### 6.2 Điểm neo mỗi nhân vật phải khai

| Điểm neo | Dùng cho |
|---|---|
| Đỉnh đầu + bán kính đầu ở 3 độ cao | Mũ, nón, băng đô |
| **Trần lông mày** (điểm cao nhất mà mày nhướng chạm tới) | Mép dưới của mọi món đội đầu phải nằm trên đường này |
| Đường mắt + bề ngang mặt | Kính |
| Vùng cấm quanh món nhận diện | Chỗ phải khoét trên mũ nón |
| Vòng cổ / vai (không cổ thì dùng mép trên của thân) | Khăn, cổ áo |
| Các elip thân: ngực, bụng, hông | Áo, đai, cạp quần |
| Bán kính tay ở vai, khuỷu, cổ tay | Tay áo, găng, băng |
| Bán kính chân ở hông, gối, cổ chân; khuôn đế | Quần, tất, giày |
| Điểm gắn sau lưng | Balo, nón đeo lưng |

### 6.3 Luật theo từng ô

| Ô | Luật | Trường hợp khó |
|---|---|---|
| Đầu | Mép dưới trên trần lông mày. Nếu vướng món nhận diện: (a) khoét lỗ, (b) đội lệch, (c) đeo sau lưng bằng quai. Mỗi nhân vật khai sẵn cách nào cho từng loại mũ | Đầu khối hộp rất rộng: nón lá phải rộng hơn đầu, nếu không sẽ thành cái đĩa úp |
| Mặt | Kính **mặc định đẩy lên trán**; chỉ kéo xuống mắt ở dáng ăn mừng của bộ đồ | Kính che mắt là mất mí và con ngươi, tức mất gần hết biểu cảm |
| Áo | Lớp vỏ cách thân tối thiểu 8 mm (con số lấy từ mã dựng hiện có). Hoạ tiết (sọc, số áo) vẽ theo toạ độ của món, không theo lưới. Thân cầu: áo phủ kín tới cạp quần | Áo dài: tà rơi từ điểm rộng nhất của thân, không ôm bụng |
| Quần | Cạp bám elip hông. Chân rất ngắn thì quần dài thành quần lửng, đó là chủ ý | Chân que: ống quần phải rộng hơn chân rõ rệt, nếu không sẽ thành sơn lên chân |
| Giày | Dựng theo khuôn đế của nhân vật. Tất chỉ hiện khi ống chân đủ dài; không đủ thì thay bằng viền màu ở cổ giày | Nhân vật có móng thay vì bàn chân: giày thành "ủng bọc móng" |
| Eo | Đai chỉ bám **một** xương (hông) để không rách khi cúi. Thân cầu: đai nằm dưới điểm phình nhất | Nhân vật không có eo: đai đeo cao ngang ngực như đai đô vật |
| Tay | Găng thay hẳn khối bàn tay thay vì bọc ngoài. Đồ cầm tay gắn vào xương bàn tay | Bàn tay không ngón: đồ cầm tay dính vào lòng bàn tay, không dựng dáng nắm |
| Nền | Không phụ thuộc thân hình | — |

### 6.4 Khi nào cho phép món riêng của một nhân vật

Tối đa **một** món riêng cho mỗi nhân vật, thuộc bậc huyền thoại, và phải là biến thể của chính món nhận diện của nhân vật đó (ví dụ bản mạ vàng). Mọi món khác dùng chung. Lý do: nhóm 2–10 người sẽ so tủ đồ với nhau, đồ riêng nhiều thì chọn nhân vật thành chọn tủ đồ.

Người dùng đổi nhân vật thì **tủ đồ đi theo người**, không đi theo nhân vật.

---

## 7. Ghi chú kỹ thuật cho lần dựng Blender sau

Chưa dựng món nào: lệnh dừng tới trước khi bắt đầu phần Blender. Khi có dàn nhân vật mới, các điểm dưới đây rút từ việc đọc `blender/concepts/lib.py`:

- Dựng mỗi món bằng `lib.make()` từ điểm neo, gán vào xương như quần áo gốc. Tạo vật liệu chỉ qua `lib.clay()`, màu để ở dạng dữ liệu, để lần đổi shader sau áp được cho cả đồ.
- Thay món gốc bằng `hide_render = True`, không xoá: `ground()` tìm giày theo tên.
- Các nét mặt là lớp dán cách bề mặt đầu chưa tới 5 mm và không biết gì về mũ nón, nên vỏ mũ nào trùm xuống là chôn lông mày. Đây là nguồn gốc của luật "trần lông mày".
- Bàn tay hiện không có ngón nên dáng "khoe đồ" phải diễn bằng cả người, không chỉ trỏ được.
- Viết trình chạy riêng trong `blender/wardrobe/`, xuất ra `blender/out/wardrobe/`; không dùng `run.py --save` vì nó ghi đè vào `concepts/`.

---

## 8. Màn hình liên quan

- **Kết thúc buổi:** lời nhận xét về buổi tập trước, sau đó mới tới mảnh. Mảnh cuối cùng mở ra món đồ: đây là khoảnh khắc "mở khoá" cần hoạt ảnh riêng.
- **Tủ đồ:** lưới theo ô; món chưa có hiện bóng mờ + một câu điều kiện ("Streak 4 tuần"). Món mùa chưa tới mùa ghi "Quay lại vào dịp Tết".
- **Bảng nhóm và feed:** avatar hiện đúng bộ đang mặc; có món mới thì feed thêm một dòng để bạn bè thả cổ vũ. Thẻ chia sẻ Zalo / Messenger dùng avatar đang mặc đồ.

---

## 9. Cần bạn chốt

| # | Câu hỏi | Đề xuất của tôi |
|---|---|---|
| 1 | Mỗi buổi tập cho **một mảnh** (đủ N mảnh ra một món) hay cho hẳn **một món**? | Mảnh. Bảng ở mục 3.3 |
| 2 | Giữ ba bậc thường / hiếm / huyền thoại với nghĩa "cách lấy", hay muốn có yếu tố may rủi? | Không may rủi |
| 3 | Nhóm có muốn tự đặt tên và màu cho Áo đội không? | Có |
| 4 | Các con số 3 tuần vắng (hoodie), 4 tuần cửa sổ mùa, 10 / 25 / 50 tuần cộng dồn | Đều là [D], cần thử trên nhóm thật |
| 5 | Dàn nhân vật mới có được phép có món riêng không? | Tối đa một món mỗi nhân vật |

## 10. Điểm yếu của tài liệu này

- Phần nghiên cứu do một tác tử phụ đọc qua công cụ tóm tắt trang; tôi không tự mở lại từng trang. Khoảng một phần ba số ô ở bảng 1.1 là [U] hoặc "chưa kiểm chứng".
- Không có bằng chứng nào cho thấy trang phục avatar làm người ta tập đều hơn. Hệ thống này dựa trên suy luận từ bằng chứng về streak và về phần thưởng nói chung.
- Nhịp phát đồ ở mục 3.3 là số tính trên giấy, với giả định tuần nào cũng đạt.
- Danh mục chưa có hình, chưa thử trên thân hình nào.

---

## Nguồn

- [S1] Bustle, bài đánh giá Finch: https://www.bustle.com/wellness/finch-app-review-features-price
- [S2] App Store, trang Finch (mô tả sự kiện, giá, đánh giá người dùng): https://apps.apple.com/app/1528595748
- [U3] Finch Help, Seasonal Event Overview (bị chặn 403, chỉ có đoạn trích): https://help.finchcare.com/hc/en-us/articles/37780438941965-Seasonal-Event-Overview
- [U4] Tổng hợp đánh giá người dùng Finch: https://appireview.pages.dev/com.finch.finch
- [S5] Duolingo blog, How the streak builds habit: https://blog.duolingo.com/how-duolingo-streak-builds-habit
- [S6] Duolingo blog, Streak celebration parties: https://blog.duolingo.com/streak-celebration-parties/
- [U7] Hướng dẫn bên thứ ba về Streak Society: https://lingoly.io/duolingo-streak-society/ ; https://duolingoguides.com/duolingo-streak-society/
- [S8] Duolingo blog, How streaks keep learners committed (2017): https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals
- [S9] Habitica, chuỗi FAQ chính thức trong mã nguồn: https://raw.githubusercontent.com/HabitRPG/habitica/develop/website/common/locales/en/faq.json
- [U10] Habitica wiki, Legendary Equipment: https://habitica.fandom.com/wiki/Legendary_Equipment
- [S11] Game Informer, đồ Pokémon GO mở theo huy chương: https://gameinformer.com/b/news/archive/2018/02/03/pokemon-go-players-can-now-get-new-outfits-by-earning-medals.aspx
- [S12] Pokémon GO, hợp tác UNIQLO: https://pokemongo.com/news/uniqlo-collaboration
- [U13] Siliconera, đồ khoá theo giới tính: https://www.siliconera.com/?p=683224
- [S14] Digital Trends, Battle Pass Fortnite: https://www.digitaltrends.com/gaming/fornite-new-battle-pass-explained/
- [S15] TechRadar, Fortnite bỏ bậc hiếm: https://www.techradar.com/gaming/consoles-pc/fortnite-has-removed-item-rarities-and-some-players-arent-happy
- [U16] OpenCritic, vụ kiện đồng hồ đếm ngược: https://opencritic.com/news/13642/fortnite-is-being-sued-over-item-shop-fomo
- [S17] PC Gamer, hộp nhìn thấy bên trong (chỉ đọc được tiêu đề): https://www.pcgamer.com/fortnite-save-the-worlds-loot-boxes-will-let-you-see-whats-inside-them-before-you-buy
- [S18] FTC, thông cáo 19/12/2022 về Epic Games: https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations
- [S19] Fall Guys, thay đổi tiền tệ: https://www.fallguys.com/fr/news/upcoming-fall-guys-currency-changes?lang=en-US
- [U20] Destructoid, phản ứng về pass Fall Guys (403): https://www.destructoid.com/fall-guys-season-pass-frustrations-fame-kudos-show-bucks/
- [S21] Nookipedia, Catalog: https://nookipedia.com/wiki/Catalog
- [S22] Nookipedia, Nook Miles: https://nookipedia.com/wiki/Nook_Miles
- [S23] GameWith, đồ Festivale và tiệm Able Sisters: https://gamewith.net/animal-crossing-new-horizons/article/show/24426 ; https://nookipedia.com/wiki/Able_Sisters
- [S24] Apple Support, xem giải thưởng: https://support.apple.com/guide/watch/see-your-awards-apd3bf6d85a6/watchos
- [S25] MacRumors, thử thách Ngày Trái Đất 2024: https://www.macrumors.com/2024/04/16/apple-watch-earth-day-activity-challenge-2024/
- [S26] 9to5Mac, watchOS 11 cho tạm dừng vòng: https://9to5mac.com/2024/07/16/close-your-ringsbut-in-watchos-11-its-okay-if-you-dont/
- [S27] iMore, Apple Watch không hiểu hồi phục: https://www.imore.com/health-fitness/apple-watch-ultra/after-8-years-the-apple-watch-still-doesnt-understand-one-crucial-part-of-fitness
- [S28] Fortune, ám ảnh đóng vòng: https://fortune.com/well/2025/01/24/apple-watch-bullied-burn-calories-close-rings-obsession-fitness-trackers-notifications/
- [S29] Apple Support, chỉnh mục tiêu và tạm dừng vòng: https://support.apple.com/guide/watch/adjust-your-activity-ring-goals-apd29b30023c/watchos
- [S30] Zendle & Cairns 2018, PLOS ONE: https://eprints.whiterose.ac.uk/139116/ ; tin của Đại học York: https://www.york.ac.uk/news-and-events/news/2018/research/researchers-find-link-problem-gambling-loot-boxes/
- [S31] Deci, Koestner & Ryan 1999, tổng hợp 128 thí nghiệm (trang tóm tắt): https://pure.ewha.ac.kr/en/publications/a-meta-analytic-review-of-experiments-examining-the-effects-of-ex/
- [U32] Deci, Koestner & Ryan 2001, phản hồi tranh luận với Cameron & Pierce: https://www.selfdeterminationtheory.org/SDT/documents/2001_DeciKoestnerRyan.pdf
- [S33] Đại học Newcastle, tóm tắt Chen và cộng sự 2024 (Journal of Public Policy & Marketing): https://from.ncl.ac.uk/the-dark-side-of-fitness-technology
- [U34] Luận văn Đại học Liège về người dùng Strava: https://matheo.uliege.be/handle/2268.2/21279
