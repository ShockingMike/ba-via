# 01 — Brief thiết kế app tập gym ("Lên Tạ", tên tạm)

Ngày: 2026-11-19. Đi kèm: [mockups.html](mockups.html) (3 hướng × 4 màn hình, bấm thử được, có clip động tác bằng code).
Đọc cùng: [00-plan.md](../research/00-plan.md), [03-app-patterns.md](../research/03-app-patterns.md).

Nhãn: **[S]** có nguồn đã đọc trong phiên này hoặc đã có trong file nghiên cứu · **[D]** phán đoán thiết kế · **[UNVERIFIED]** chưa kiểm chứng được bằng nguồn sơ cấp.
Lưu ý về trích dẫn: các trang được đọc qua công cụ tóm tắt, nên mọi ý dưới đây là diễn giải, không phải trích nguyên văn.

## 0. Tóm tắt

- Đề xuất hướng **Phố** (biển hiệu vẽ tay, nhãn dán, biển số). Hai hướng còn lại: **Xưởng** (áp phích lò rèn, tối, gắt) và **Sớm** (giấy, chàm, nắng đào, dịu).
- Không dùng linh vật con vật. "Nhân vật" của app chính là hình người minh hoạ động tác: cùng một bộ khung vừa dạy bài, vừa ăn mừng cuối buổi.
- Ngày thường: **1 chạm** để vào buổi tập, **1 chạm** cho mỗi set, **0 chạm** bắt buộc ở màn hình kết thúc.
- Ăn mừng và đồng hồ nghỉ **không phụ thuộc** rung, tiếng hay thông báo, vì iPhone không đảm bảo ba thứ đó cho web app.

## 1. Nguyên tắc mượn từ Duolingo và các app thói quen

Mượn nguyên tắc, không mượn hình: không cú, không xanh lá #58CC02, không chữ tròn kiểu Feather/Din Round, không ngọn lửa streak, không nút có "môi" bóng dưới.

| # | Nguyên tắc | Nguồn nói gì | Áp vào app |
|---|---|---|---|
| 1 | **Chỉ cho một bước tiếp theo** | Duolingo đổi màn hình chính thành một lộ trình duy nhất vì người học không chắc mình đang dùng app "đúng cách"; lộ trình để mỗi bước luôn là bước tốt nhất [S1]. Phó chủ tịch thiết kế gọi đây là làm lại toàn bộ chiến lược sản phẩm [S2] | Màn hình "Hôm nay" chỉ có một nút chính. Không có thư viện bài tập ở trang đầu. Người mới không phải chọn gì |
| 2 | **Ngưỡng giữ chuỗi thật thấp** | Tách streak khỏi mục tiêu ngày (1 bài là giữ chuỗi): giữ chân ngày 14 +3,3%, số người có streak +10,5% [S3]. Bài "streak builds habit" nói mỗi ngày chỉ cần vài phút [S4] | Buổi ngắn lúc mệt vẫn tính đủ một buổi. Feed nhóm nói rõ điều đó ("Mệt vẫn đến. Vẫn tính đủ một buổi") |
| 3 | **Có độ chùng, không phạt** | Streak Freeze cho "độ chùng"; cho phép trang bị 2 freeze làm tăng nhẹ người học hằng ngày mà không làm họ nghỉ nhiều hơn [S4]. Gentler Streak: ngày nghỉ không làm đứt chuỗi, có trạng thái ốm/chấn thương/đi xa [S7, đoạn trích] | Streak theo tuần, tuần nghỉ có phép. Trên bảng nhóm, người đang ốm hiện "nghỉ có phép, chuỗi vẫn giữ", không có biểu tượng vỡ, không màu đỏ |
| 4 | **Phản hồi mạnh nhất ở những ngày đầu** | Từ 2 lên 3 ngày là +50%, từ 200 lên 201 là +0,5%, nên phản hồi được dồn cho giai đoạn đầu [S4]. Hoạt hình ở mốc streak: người mới còn hoạt động sau 7 ngày +1,7% [S4] | Buổi 1, 2, 3 và tuần đạt đầu tiên có ăn mừng riêng. Sau đó chỉ các mốc thật (buổi 10/50/100, 4/12/26 tuần) mới có màn lớn |
| 5 | **Ăn mừng là chuyển động có nhịp, và hiếm** | Mốc streak được thiết kế như "power-up" trong game; nhịp và thời điểm của hoạt hình quan trọng ngang hình vẽ; bản bóng bay cũ bị chê thiếu năng lượng [S5]. Thẻ chia sẻ nằm ngay trong màn ăn mừng [S5] | Cuối buổi: dấu "Xong" đóng xuống (0,1 giây) → số liệu hiện lần lượt (cách nhau 70 ms) → bánh tạ thứ 3 trượt vào thanh đòn (giây thứ 1) → số tuần nhảy 6 lên 7. Tổng dưới 1,6 giây, không chặn thao tác. Set thường chỉ có dấu ✓ đóng xuống 0,3 giây |
| 6 | **Hình ít chi tiết, dựng từ vài khối** | Phong cách Duolingo chọn ít chi tiết nhất mà vẫn rõ nghĩa, bóng dáng rõ, để vẽ nhanh hàng trăm hình và co giãn trên mọi màn hình [S6] | Nhân vật là các đoạn bo tròn, không mặt, không viền. Nhờ vậy 90 bài dùng chung một bộ khung (mục 6) |
| 7 | **Nhân vật tạo gắn bó; hoạt hình là phần thưởng** | Hoạt hình nhân vật khi trả lời đúng "tự nó là phần thưởng"; "chúng tôi là công ty về niềm vui và động lực" [S2] | Nhân vật giơ tay cuối buổi. Không cần con vật: người tập nhìn thấy chính động tác của mình |
| 8 | **Giọng văn: bạn tập, không phải huấn luyện viên quát** | Duolingo nổi tiếng nhắc streak "không ngại ngùng" [S2]; chính họ cũng tự giới hạn số thông báo để không hỏng kênh [S8]. Phê bình vòng Activity của Apple: nỗi sợ mất chuỗi rơi đúng ngày nên nghỉ [03-app-patterns, S32] | Không dùng câu gây tội lỗi ("Bạn đã bỏ lỡ…", "Đừng làm cả nhóm thất vọng"). Vùng vàng/đỏ viết như lời khuyên ("giữ tạ, chưa tăng", "hoặc đổi sang đi bộ 20–30 phút"). Ngày nghỉ không có lời nhắc nào |
| 9 | **Âm thanh và rung là lớp thêm** | Không tìm được bài chính chủ nào của Duolingo về thiết kế âm thanh hay rung. Một bản tóm tắt podcast của PM Duolingo khuyên chồng hoạt hình + rung + tiếng ở mốc lớn [UNVERIFIED, nguồn thứ cấp] | Xem mục 2: trên iPhone không dựa vào rung, không dựa vào tiếng |
| 10 | **Xếp hạng thứ ai cũng thắng được** | League của Duolingo hiệu quả vì ghép người cùng mức hoạt động, không phải bạn bè [S8]. Kudos có giá trị trong vòng nhỏ quen biết [03-app-patterns, S30] | Bảng tuần theo % mục tiêu riêng, có trần 100%. Thử thách tuần là mục tiêu chung của cả hội |

Chưa có nguồn chính chủ cho hai mảng: **onboarding** của Duolingo (phiên này không tìm bài nào về nó) và **âm thanh, rung** (đã tìm, không thấy bài chính chủ). Các quyết định ở hai mảng này là [D].

Finch (app tự chăm sóc có thú nuôi) hay được nhắc là ví dụ "không tội lỗi", nhưng phiên này chỉ tìm được bài quảng bá và bài phê bình của bên thứ ba, không có phát biểu của nhóm sáng lập → **[UNVERIFIED]**, không dùng làm căn cứ.

### Ngân sách ma sát [D]

- Một quyết định mỗi màn hình. Mặc định luôn là "như lần trước".
- Trong lúc tập: không gõ phím. Chỉ chạm ✓ và nút +/−.
- Mọi thao tác ghi dữ liệu 1 chạm đều có **Hoàn tác** hiện 5 giây ở mép trên (không che vùng ngón cái).
- Hoạt hình giao diện 140–300 ms, vào nhanh ra nhanh (ease-out mạnh). Chỉ ăn mừng cuối buổi mới được dài hơn.
- Chữ nhỏ nhất 12 px, số mục tiêu 58–70 px để đọc ở tầm một sải tay.

## 2. Web app trên màn hình chính làm được gì (iOS so với Android, 2026)

| Khả năng | Android (Chrome) | iPhone (Safari / web app màn hình chính) | Quy tắc thiết kế |
|---|---|---|---|
| Rung (`navigator.vibrate`) | Có từ Chrome 32, cần thao tác người dùng [S9] | **Không hỗ trợ** (`version_added: false`) [S9] | Rung chỉ là lớp thêm trên Android. Không phản hồi nào chỉ có rung |
| "Mẹo" rung bằng ô `<input switch>` | Không áp dụng | Safari 18 có rung cho ô switch [đoạn trích ghi chú phát hành]. Một thư viện bên thứ ba nói mẹo bấm ô ẩn chạy được iOS 17.4–26.4 và **bị Apple vá ở 26.5** [S10, UNVERIFIED] | Coi như đã chết. Không dùng |
| Web Audio | Phát được sau một thao tác chạm [S11] | Phát được sau thao tác chạm [S11], nhưng **công tắc im lặng tắt luôn Web Audio** vì phiên âm thanh mặc định là "ambient" [S12, đoạn trích]. Đặt `navigator.audioSession.type = "playback"` (Safari 16.4+ [S9]) thì vượt được | Tiếng "tách" khi ✓ và 4 nốt khi xong buổi là lớp thêm, bật/tắt được. **Tôn trọng công tắc im lặng**, không ép `playback`: phòng tập là nơi công cộng |
| Giữ sáng màn hình (Wake Lock) | Có từ Chrome 84 [S9] | Safari 16.4+; trong **web app màn hình chính chỉ chạy từ iOS 18.4** (lỗi WebKit 254545) [S9, S13] | Xin khoá khi vào màn hình tập, xin lại mỗi lần `visibilitychange`. Máy cũ hơn 18.4: vẫn dùng được, chỉ là màn hình tự tắt, nên đồng hồ không được phụ thuộc vào nó |
| JavaScript khi app xuống nền | Bị bóp dần | Bị đóng băng sau vài giây [S14, đoạn trích nguồn thứ cấp, UNVERIFIED về con số] | **Đồng hồ nghỉ lưu thời điểm kết thúc** (`Date.now() + thời lượng`), mỗi lần hiện lại thì tính lại. Mockup đã làm đúng cách này |
| Báo hết giờ nghỉ khi khoá máy | Không có báo thức cục bộ đáng tin | Không có. Chỉ push từ máy chủ mới hiện được khi khoá máy | Không hứa "báo hết giờ nghỉ khi tắt màn hình". Thay bằng: màn hình luôn sáng + đồng hồ to + (nếu bật) tiếng bíp |
| Thông báo đẩy | Có | Từ iOS 16.4, **chỉ khi đã thêm vào màn hình chính**, phải xin quyền sau một cú chạm; cần máy chủ gửi [S15, S9] | Đúng như kế hoạch: nhắc nhau để giai đoạn 2. Bản đầu không có tính năng nào cần push |
| Huy hiệu trên biểu tượng app | Không (Chrome Android) [S9] | Có từ 16.4 cho web app màn hình chính, sau khi cho phép thông báo [S9, S15] | Không dùng ở bản đầu |
| Chia sẻ (`navigator.share`) | Có từ Chrome 61 [S9] | Có từ Safari 12.1 [S9]. Chia sẻ **file ảnh** vào Zalo cần thử trên máy thật [UNVERIFIED] | Thẻ kết thúc buổi dựng bằng canvas → chia sẻ ảnh; không được thì cho tải ảnh về |

Việc phải thử trên iPhone thật của nhóm trước khi chốt: Wake Lock sau khi chuyển app rồi quay lại, chia sẻ ảnh vào Zalo, và tiếng khi gạt công tắc im lặng.

## 3. Ba hướng thiết kế

Cả ba dùng chung bố cục và dữ liệu, nhưng khác nhau ở **vật thể tiến độ**, **cách bày con số** và **bố cục ăn mừng**, nên nhìn đen trắng vẫn phân biệt được.

### Hướng 1 — PHỐ (đề xuất)

- **Tâm trạng:** biển hiệu vẽ tay, nhãn dán, biển số xe. Vui, ồn vừa đủ, rất Việt Nam.
- **Hình khối:** viền mực 2 px, bóng cứng lệch 3 px xuống phải (bấm thì nút "lún" vào bóng), bo 16 px, nhãn nghiêng −3° đến −6°. Con số nằm trong "biển số" có hai đinh tán.
- **Tiến độ tuần:** thanh đòn. Mỗi buổi xong lắp thêm một cặp bánh tạ; buổi chưa tập là bánh nét đứt.
- **Chuyển động:** nảy nhẹ kiểu đóng dấu (chỉ ở ✓ và ăn mừng), còn lại 140–200 ms ease-out.
- **Chữ:** Bricolage Grotesque 800 (tiêu đề, con số) + Be Vietnam Pro 400–700 (chữ thường).
- **Linh vật:** không. Dùng nhân vật minh hoạ động tác.

| Token | Sáng | Tối |
|---|---|---|
| `--bg` nền | `#FFF2D6` | `#15120D` |
| `--surface` thẻ | `#FFFBF0` | `#221E16` |
| `--ink` chữ, viền | `#17140F` | `#FFF2D6` |
| `--mut` chữ phụ | `#62594A` | `#B8AD97` |
| `--primary` nút chính (xanh coban) | `#2340E0` | `#7D92FF` |
| `--accent` chọn, nhấn (vàng nghệ) | `#FFC531` | `#FFC531` |
| `--hot` ăn mừng, đồng hồ (đỏ son) | `#E4402A` | `#FF6B54` |
| `--ok` đã xong (xanh cổ vịt) | `#0B7A75` | `#39BDB3` |
| `--warn` / `--bad` vùng vàng / đỏ | `#B86A00` / `#C22E1A` | `#FFB54A` / `#FF7B66` |

### Hướng 2 — XƯỞNG

- **Tâm trạng:** áp phích lò rèn. Nền than, cam lửa lò, sọc cảnh báo vàng. Mạnh, nghiêm, hơi "dân tập lâu năm".
- **Hình khối:** bo 3 px, nút chính vát hai góc, đường kẻ 1 px, không bóng, nhãn có `//` phía trước, thước đo dưới con số.
- **Tiến độ tuần:** các khối vạch nghiêng như đồng hồ đo.
- **Chuyển động:** quét ngang (clip-path) và cắt cứng, không nảy.
- **Chữ:** Big Shoulders Display 800–900 viết hoa (tiêu đề, con số 70 px) + Archivo.
- **Linh vật:** không.
- **Mặc định tối.** Bản sáng có sẵn.

| Token | Tối (gốc) | Sáng |
|---|---|---|
| `--bg` | `#0E0D0C` | `#EAE6DE` |
| `--surface` | `#1A1816` | `#F7F4EE` |
| `--ink` | `#F3EEE5` | `#141210` |
| `--mut` | `#A69E92` | `#595247` |
| `--line` | `#3A352F` | `#BEB6A8` |
| `--primary` / `--hot` (cam lò) | `#FF5A1F` | `#C43A06` |
| `--accent` | `#F5C400` | `#141210` |
| `--ok` | `#86D694` | `#2F6B3A` |
| `--warn` / `--bad` | `#F5C400` / `#FF7A66` | `#8A6400` / `#B3261E` |

### Hướng 3 — SỚM

- **Tâm trạng:** buổi tập đầu ngày. Giấy ấm, chàm, nắng màu đào. Gần với Gentler Streak về tinh thần.
- **Hình khối:** bo 22 px, không viền, bóng mềm, nút hình viên thuốc, con số nằm trong mặt tròn như mặt đồng hồ.
- **Tiến độ tuần:** các mặt trời nhỏ; buổi chưa tập là vòng rỗng.
- **Chuyển động:** chậm (0,8–1,2 giây ở ăn mừng), mặt trời mọc, chấm sáng bay lên.
- **Chữ:** Fraunces 500 (tiêu đề, con số) + Lexend.
- **Linh vật:** không.

| Token | Sáng | Tối |
|---|---|---|
| `--bg` | `#F6F1E9` | `#141627` |
| `--surface` | `#FFFFFF` | `#1E2138` |
| `--ink` | `#232640` | `#EEF0FA` |
| `--mut` | `#5F6380` | `#A6ABC9` |
| `--line` | `#E4DED3` | `#2C3050` |
| `--primary` (chàm) | `#3A4391` | `#A9B3FF` |
| `--accent` (đào) | `#F6B08C` | `#F6B08C` |
| `--hot` | `#D9623F` | `#FF9A78` |
| `--warn` / `--bad` | `#A8651A` / `#B5412A` | `#F2B872` / `#FF9A8A` |

### Phông chữ và dấu tiếng Việt

Cả 6 phông đều có bộ ký tự `vietnamese` trên Google Fonts (đã kiểm bằng cách gọi API css2). Đã dựng thử bằng Chrome và nhìn ảnh chụp các chuỗi có dấu chồng: Big Shoulders Display viết hoa ("ĐỂ SAU · ĐỔI BÀI · KỶ LỤC", "CHIA SẺ THẺ VÀO ZALO", "TẠO BUỔI CHO HÔM NAY"), Fraunces ("Tạo buổi cho hôm nay", "Squat ôm tạ trước ngực"), Bricolage Grotesque ("Đủ buổi rồi, nghỉ thôi!").

- Không phông nào bị cắt dấu ở `line-height` ≥ 1,1.
- Big Shoulders Display viết hoa có dấu chồng cao: giữ `line-height` ≥ 1,1 và không đặt `overflow:hidden` sát chữ.
- Đã loại vì thiếu tiếng Việt: Sora, Rubik, Gabarito, Instrument Serif, Bowlby One, Lilita One.
- Chưa thử trên Safari iOS thật [UNVERIFIED].

## 4. Đề xuất: Phố

1. **Đạt đúng yêu cầu "như Duolingo trở lên" mà không giống Duolingo.** Vui, rõ, nhiều phản hồi, nhưng ngôn ngữ hình là phố Việt: biển hiệu, nhãn dán, biển số, bánh tạ.
2. **Không an toàn kiểu lưới tối giản.** Viền mực và bóng cứng cho từng màn hình một dáng riêng; thẻ chia sẻ trông như tấm nhãn dán, hợp để gửi vào Zalo.
3. **Dễ đọc trong phòng tập.** Tương phản cao ở cả sáng và tối, con số 58 px, vùng chạm lớn.
4. **Rẻ để làm.** Toàn bộ là CSS và SVG, không cần hoạ sĩ vẽ từng hình. Nhân vật dùng chung bộ khung.
5. **Thân thiện với người mới.** Xưởng đẹp nhưng dễ làm người mới và các bạn nữ thấy "không dành cho mình". Sớm dễ chịu nhất nhưng ít cá tính nhất, gần với thứ đã từng bị chê là "rẻ".

Có thể lai: lấy Phố làm gốc, mượn **con số khổng lồ của Xưởng** cho màn hình ghi set, và **giọng văn dịu của Sớm** cho ngày vùng vàng/đỏ.

Rủi ro của Phố: bóng cứng lệch góc đang là mốt (dễ lỗi thời), nên phần nhận diện phải dựa vào bánh tạ, biển số và nhân vật chứ không chỉ dựa vào bóng.

## 5. Ngân sách chạm theo màn hình

| Màn hình | Ngày thường | Tệ nhất | Ghi chú |
|---|---|---|---|
| **A. Check-in** | **1** ("Như mọi khi" → vào thẳng bài đầu) | 1 chạm cho mỗi thứ khác đi + 1 chạm "Tạo buổi cho hôm nay". Ví dụ mệt + thiếu máy kéo xô = 3 | Mọi ô đều có mặc định là lần trước. Vùng xanh/vàng/đỏ đổi ngay khi chạm, trước khi bấm nút. "Đau chỗ nào?" ẩn sau 1 chạm. "Thiếu gì" ghi rõ chỉ tính cho buổi này |
| **B. Ghi set** | **1** mỗi set (✓). Đồng hồ nghỉ tự chạy | +1 cho mỗi bước tạ hoặc mỗi lần lệch. Đổi bài: 2 (mở + chọn). Để sau: 1 | ✓, Để sau, Đổi bài nằm ở 1/3 dưới màn hình. Sửa nhầm: 1 chạm Hoàn tác |
| **C. Xong buổi** | **0** bắt buộc | 1 cho câu "nhẹ / vừa / quá sức" (bỏ qua được) + 1 chia sẻ | Tấm thẻ phía trên chính là ảnh chia sẻ, không có bước "tạo thẻ" |
| **D. Nhóm** | **0** để xem | 1 chạm cổ vũ mỗi hoạt động | Không có bình luận ở bản đầu: cổ vũ 1 chạm là đủ |
| Xem kỹ thuật | 0 (clip tự chạy ngay trong thẻ bài) | 1 để mở hướng dẫn đầy đủ | |

Một buổi 6 bài, 17 set, không chỉnh gì: 1 (check-in) + 17 (set) + 5 (sang bài) = **23 chạm**.

## 6. Clip động tác bằng code: bộ khung và cách nhân rộng

**Đang có trong mockup:** một bộ khung nhìn ngang gồm 7 khớp (cổ chân, gối, hông, vai, khuỷu, cổ tay, đầu). Mỗi động tác là vài **tư thế** ghi bằng góc khớp (độ) và một **nhịp** (mốc thời gian). Code tự nội suy giữa các tư thế và vẽ các đoạn bo tròn bằng SVG. Ba clip đã chạy trên cùng bộ khung: squat ôm tạ, Romanian deadlift tạ tay, ăn mừng.

```
clip('goblet_squat', {
  top: { shin: 3,  thigh: -2,  torso: 4,  neck: -2,  arm: 168, fore: -150 },
  bot: { shin: 30, thigh: -88, torso: 30, neck: -18, arm: 158, fore: -150 },
  nhịp: [ 0s→top, 1,9s→bot, 2,3s→bot, 3,4s→top, 4,2s→top ]
})
```

Kèm theo mỗi clip: đạo cụ (tạ ôm ngực, tạ buông tay), nhóm cơ đang làm việc (sáng lên theo độ sâu), và câu nhắc theo từng pha ("Hít vào, ngồi xuống chậm").

**Nhân rộng ra 90 bài** (ước lượng [D], cần làm thử 5–6 bài nữa mới chắc):

| Nhóm | Cần thêm gì | Phủ pattern |
|---|---|---|
| Đứng, nhìn ngang, chân trụ (đang có) | Chỉ thêm tư thế + đạo cụ (thanh đòn, tạ tay, dây, cáp) | squat, hinge, đẩy vai, tay trước, tay sau, bắp chân, carry |
| Hai chân khác nhau | Cho chân xa có góc riêng (hiện hai chân dùng chung góc) | lunge, split squat, step-up |
| Treo hoặc kéo từ trên | Điểm neo ở tay thay vì ở chân | kéo xà, kéo xô |
| Ngồi hoặc nằm ghế | Điểm neo ở hông + đạo cụ ghế, máy | đẩy ngực, kéo ngang ngồi, đạp đùi, đá đùi, móc đùi |
| Chống tay hoặc nằm sàn | Điểm neo ở tay và mũi chân, thân nằm ngang | chống đẩy, plank, dead bug, glute bridge |
| **Nhìn thẳng** (bộ khung thứ hai) | Một bộ khung đối xứng trái phải | vai giữa, vai sau, và lỗi "gối đổ vào trong" |

Ước tính: 2 bộ khung, khoảng 5 kiểu neo, khoảng 12 đạo cụ, mỗi bài 2–3 tư thế. 90 bài là khoảng 90 đoạn dữ liệu dài 4–6 dòng, không phải 90 hình vẽ.

Giới hạn cần nói thẳng:
- Nhìn ngang không thể hiện được lỗi theo chiều trái phải (gối đổ vào trong, khuỷu mở 90°).
- Góc khớp do người nhập tay, phải có người biết kỹ thuật duyệt từng bài (liên quan điểm yếu "mới đối chiếu 18/90 bài" trong kế hoạch).
- Nhân vật hiện có một dáng người. Nên cho chọn 2–3 dáng và màu áo theo từng thành viên [D].
- Tôn trọng "giảm chuyển động": khi máy bật chế độ này, clip đứng yên ở tư thế đáy và chỉ chạy khi người dùng bấm Phát.

## 7. Câu hỏi còn mở

**Q: mã nhóm hay đăng nhập?** (chưa quyết, cần người dùng chọn)

| | Mã nhóm, không tài khoản | Đăng nhập Google |
|---|---|---|
| Lần đầu mở app | Nhập tên + mã nhóm: khoảng 2 chạm và một lần gõ | 1–2 chạm, nhưng có màn hình xin quyền của Google |
| Đổi máy hoặc iOS xoá dữ liệu | Phải nhập lại file sao lưu; nếu không sẽ thành "người mới" trong nhóm | Vào lại là thấy hồ sơ nhóm; nhật ký chi tiết vẫn cần sao lưu |
| Bảo mật nhóm | Ai có mã là vào được | Biết chính xác ai là ai |
| Cảm giác | Nhẹ, đúng kiểu "app của hội mình" | Nghiêm túc hơn, quen thuộc |
| Lưu ý kỹ thuật | Đơn giản nhất | Đăng nhập Google trong web app màn hình chính trên iOS cần thử kỹ [UNVERIFIED] |

Một lối giữa để cân nhắc: bắt đầu bằng mã nhóm, cho phép gắn tài khoản Google sau để giữ hồ sơ khi đổi máy.

Câu hỏi khác:
- Tên app: "Lên Tạ" chỉ là tên tạm.
- Có lai Phố với con số của Xưởng không (mục 4)?
- Âm thanh mặc định bật hay tắt? Đề xuất: tắt, hỏi một lần ở buổi đầu.

## 8. Kiểm tra đã làm trên mockup

- Dựng bằng Chrome không giao diện, xem ảnh chụp cả 3 hướng ở chế độ sáng và tối, cả trạng thái sau khi bấm.
- Chạy kịch bản bấm tự động trên hướng Phố: Như mọi khi → Hoàn tác, ✓ đến hết set 3, Để sau, Đổi bài → chọn bài, cổ vũ, phát lại ăn mừng. Tất cả chạy, không lỗi JavaScript. Clip động tác và đồng hồ nghỉ chạy theo thời gian thật.
- Ở khung 400 px: không cuộn ngang; ngày thường mọi màn hình vừa khung. Trường hợp chọn rất nhiều ô ở check-in, phần thân màn hình cuộn dọc như app thật.
- Chưa làm: thử trên iPhone và Android thật, đo tương phản bằng công cụ, thử với trình đọc màn hình.

## Nguồn

- [S1] Duolingo blog — New home screen design: https://blog.duolingo.com/new-duolingo-home-screen-design
- [S2] Apple Developer — Behind the Design: Duolingo: https://developer.apple.com/news/?id=jhkvppla
- [S3] Duolingo blog — Improving the streak (đã đọc trong 03-app-patterns, S27): https://blog.duolingo.com/improving-the-streak
- [S4] Duolingo blog — How the streak builds habit: https://blog.duolingo.com/how-duolingo-streak-builds-habit
- [S5] Duolingo blog — Streak milestone design and animation: https://blog.duolingo.com/streak-milestone-design-animation
- [S6] Duolingo blog — Shape language, Duolingo's art style: https://blog.duolingo.com/shape-language-duolingos-art-style/
- [S7] Gentler Streak, trang App Store (chỉ đọc đoạn trích kết quả tìm kiếm): https://apps.apple.com/us/app/gentler-streak-workout-tracker/id1576857102
- [S8] Lenny's Newsletter — How Duolingo reignited user growth (đã đọc trong 03-app-patterns, S28): https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth
- [S9] MDN browser-compat-data, đọc trực tiếp JSON (`api/Navigator.json`: vibrate, wakeLock, share, setAppBadge, audioSession; `api/WakeLock.json`; `api/PushManager.json`): https://github.com/mdn/browser-compat-data
- [S10] ios-haptics README (bên thứ ba): https://unpkg.com/ios-haptics@3.1.1/README.md
- [S11] MDN — Autoplay guide for media and Web Audio APIs: https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay
- [S12] WebKit bug 237322, Web Audio bị tắt khi gạt im lặng (đoạn trích): https://bugs.webkit.org/show_bug.cgi?id=237322
- [S13] WebKit bug 254545, Wake Lock không chạy trong Home Screen Web App: https://bugs.webkit.org/show_bug.cgi?id=254545 ; MDN — Screen Wake Lock API: https://developer.mozilla.org/en-US/docs/Web/API/Screen_Wake_Lock_API
- [S14] Maximiliano Firtman về iOS đóng băng web app khi xuống nền (đoạn trích, bài cũ): https://firt.dev/ios-12.2/
- [S15] WebKit blog — Web Push for Web Apps on iOS and iPadOS: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/
