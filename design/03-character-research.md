# 03 — Nghiên cứu nhân vật: vì sao nhân vật Duolingo "có hồn"

Ngày: 2026-11-20. Đi kèm: [04-character-concepts.md](04-character-concepts.md) và ảnh tham khảo trong [refs/duo/](refs/duo/).
Bối cảnh: nhân vật đất nặn bản đầu (`blender/out/neutral_preview.png`) bị chê "thiếu tính cách, thua xa Duolingo".

Nhãn: **[S]** nguồn đã đọc trong phiên này (qua công cụ tóm tắt, nên là diễn giải chứ không trích nguyên văn) · **[Q]** tự nhìn thấy trên ảnh chính chủ đã tải về · **[S2]** nguồn thứ cấp · **[D]** phán đoán thiết kế.

## 0. Tóm tắt

- Nhân vật bản đầu sạch về kỹ thuật nhưng mọi quyết định đều "trung bình": tỉ lệ trung tính, mặt cười mặc định, bóng dáng giống mọi con búp bê khác. Duolingo làm ngược lại ở từng điểm: **mỗi nhân vật là một hình khối, một thái độ, một chi tiết nhận diện**.
- Tính cách đến từ bốn thứ, xếp theo sức nặng: (1) bóng dáng và tỉ lệ phóng đại, (2) mí mắt + lông mày, (3) dáng đứng có đường lực, (4) câu chuyện và giọng nói. Chất liệu, ánh sáng gần như không góp gì.
- Duolingo tách vai: **Duo (không phải người) lo cảm xúc và thương hiệu, dàn nhân vật người lo nội dung**. App tập gym nên cân nhắc đúng cấu trúc đó: linh vật lo check-in, streak, ăn mừng; hình người đơn giản lo minh hoạ động tác.

## 1. Duolingo đã làm gì

### 1.1 Điều họ tự nói

| # | Nguyên tắc | Nguồn nói gì |
|---|---|---|
| 1 | **Mọi nhân vật mượn "bộ gen" của Duo** | Dàn nhân vật người phải giống Duo để thuộc cùng một thế giới: dựng hình học, mắt to, thân có hình riêng, bàn chân tách rời. Bài có hình vẽ Duo và Junior dựng từ cùng các khối cơ bản [S1] |
| 2 | **Người thường nhưng "lệch một cách đáng yêu"** | Họ từng cân nhắc viking, người ngoài hành tinh rồi bỏ vì xa việc học; chọn người hiện đại có cá tính rất kỳ quặc. Làm khoảng một năm rưỡi, nhiều vòng [S1] |
| 3 | **Ba khối cơ bản, bo tròn hết** | Hình minh hoạ dựng từ chữ nhật bo góc, hình tròn, tam giác bo; không có góc nhọn. Đầu và thân thường chỉ 1–2 khối; mắt là hình viên thuốc bo tròn hoàn toàn [S3, đoạn trích kết quả tìm kiếm; trang design.duolingo.com hiện đã chuyển hướng nên không đọc trực tiếp được] |
| 4 | **Ít chi tiết nhất mà vẫn rõ nghĩa** | Khoảng 15 khối là vừa; 6 thì quá trừu tượng, 30 thì quá rối [S3]. "Ít chi tiết nhất đủ để truyền đạt" [S2] |
| 5 | **Phóng đại gần tới mức biếm hoạ** | Chi tiết chính được phóng đại gần như biếm hoạ, kèm "nhịp": cố ý xen kẽ khối to, khối nhỏ [S2] |
| 6 | **Bóng dáng trước, chi tiết sau** | Vật chính phải đọc được bằng bóng đen; đó là bước đầu để nhận ra ngay [S2] |
| 7 | **Lặp lại hình khối trong một nhân vật** | Lặp một hình xuyên suốt thiết kế để ngôn ngữ hình khối của nhân vật đó thống nhất [S3, đoạn trích] |
| 8 | **Tính cách viết trước, theo cặp đối lập** | Zari cực hướng ngoại, bạn thân Lily cực hướng nội và mỉa mai để tự vệ; Bea tham vọng, hay lo, Lin thì thảnh thơi. "Trái dấu hút nhau" để có kịch tính. Mỗi người có một chi tiết vui rất cụ thể: Zari "tham gia 10 câu lạc bộ, làm chủ tịch 8"; Lily "chỉ nghe ban nhạc bạn chưa từng nghe tên"; Bea "chưa bao giờ thấy thích mát-xa"; Lin "mê bánh mì kẹp" [S4] |
| 9 | **Hoạt hình là phần thưởng, mỗi người ăn mừng một kiểu** | Mỗi nhân vật có hoạt hình riêng khi trả lời đúng [S1]. Hệ thống rig dùng chung để đổi nhân vật, biểu cảm mà không dựng lại [S5, S2-thứ cấp] |

### 1.2 Điều tự nhìn thấy trên ảnh chính chủ [Q]

Ảnh: `refs/duo/cast-jumping.png` (cả dàn đang nhảy), `refs/duo/cast-cover.png`, `refs/duo/duo-junior-shapes.gif`.

- **Mỗi người một khối gốc.** Junior: hộp vuông bo. Eddy: chữ nhật đứng. Lucy: hình thang lùn. Oscar: quả trứng úp. Vikram: quả lê. Lily: dải hẹp dài. Tô đen vẫn phân biệt được cả chín người.
- **Không có cổ. Đầu to bằng hoặc hơn thân.** Chân tay là que; bàn chân là viên thuốc rời khỏi chân.
- **Mỗi người một món nhận diện, nhìn ra ngay từ bóng đen:** rèm tóc tím của Lily, mái bồng + ria của Oscar, khăn xếp + râu của Vikram, băng đô + tóc vàng của Eddy, búi tóc của Lucy, chỏm tóc cam của Junior.
- **Mí mắt làm gần hết việc diễn.** Lily và Lin: mí sụp nửa mắt, con ngươi liếc ngang → chán đời. Oscar: mí chéo vào trong + mày rậm → cau có. Eddy và Junior: mắt mở hết cỡ. Zari, Bea: mắt nhắm thành nét cong khi cười.
- **Miệng là hình khối, không phải nét:** miệng mở tô đỏ sẫm, có lưỡi, có dải răng. Không ai dùng "nụ cười mặc định".
- **Dáng lệch và có đường lực.** Trong ảnh cả dàn nhảy, không ai đứng thẳng; thân nghiêng, tay chân choãi theo một đường cong. Lily là ngoại lệ có chủ ý: người khác nhảy, cô bước đi, và chính điều đó là tính cách.
- **Mỗi người một khối màu chủ đạo** (Lily tím, Zari hồng, Eddy đỏ, Junior xanh lơ, Lucy cam).
- **Bất đối xứng:** tóc lệch, một mắt nheo, một bên mày nhướng.

## 2. Các linh vật khác

| Ví dụ | Điều rút ra | Nguồn |
|---|---|---|
| **Fall Guys** | Đề bài tính cách là "kém thể thao nhưng đầy tham vọng": làm được động tác nhưng trông không hề lực sĩ. Lời khuyên thiết kế: lùi ra xa mà vẫn đọc được, thử che nửa dưới xem còn nhận ra không. Thân đơn giản nên thay đồ rất dễ | [S6, S2-thứ cấp] |
| **Headspace** | Nhân vật cố ý mơ hồ, không hẳn là người, nhiều hình dạng và màu để ai cũng thấy mình. Bản cập nhật mở rộng cảm xúc: không chỉ cười mà có cả căng thẳng, buồn. Mặt tối giản: hai chấm mắt, một nét miệng | [S7, S8 – thứ cấp] |
| **Finch** | Phiên này không tìm được phát biểu của nhóm thiết kế. Bỏ, không dùng làm căn cứ | — |
| **Mii so với dân làng Animal Crossing** [D] | Mii là hệ lắp ghép trung tính: ai cũng tạo được, không ai nhớ. Dân làng Animal Crossing cùng một bộ khung nhưng mỗi con có loài, màu, kiểu tính cách và câu cửa miệng. Nhân vật bản đầu của ta thuộc kiểu Mii | Phán đoán, không có nguồn |
| **Nhân vật khối đơn giản của Pixar** [D] | Một khối gốc cho mỗi người (vuông = vững, tròn = hiền, tam giác = sắc sảo), rồi tương phản khối giữa các nhân vật đứng cạnh nhau | Kiến thức nghề phổ biến [S9, S10 – bài tổng hợp] |
| Lý thuyết chung | Tròn = thân thiện; vuông = vững, đáng tin; tam giác/góc nhọn = năng động, sắc. Chốt bóng dáng trước khi thêm chi tiết. Một, hai chi tiết đáng nhớ thắng một thiết kế rối. Đầu to quá cỡ tạo cảm giác tinh nghịch | [S9, S10 – thứ cấp] |

## 3. Vì sao nhân vật bản đầu thất bại (đối chiếu từng điểm) [D]

| Tiêu chí | Duolingo | Nhân vật bản đầu |
|---|---|---|
| Khối gốc | Mỗi người một khối | Không có: đầu tròn, thân trung tính |
| Tỉ lệ | Đầu ≥ thân, không cổ, chân que | Tỉ lệ búp bê phổ thông, có cổ |
| Bóng đen | Nhận ra từng người | Giống mọi búp bê tóc búi |
| Mắt | Tròng trắng + con ngươi + mí | Hạt đen bóng, không mí, không liếc được |
| Mày, miệng | Đổi theo cảm xúc | Đúc cứng: một nét cười cho mọi tư thế |
| Thái độ | Viết trước, có câu chuyện | Không có |
| Chi tiết nhận diện | Một món mỗi người | Không có |
| Dáng | Lệch, có đường lực | Đứng gần thẳng, vẫy tay |

## 4. Quy tắc áp vào vòng thiết kế này [D]

1. Một khối gốc cho mỗi nhân vật, lặp lại ở đầu, thân, phụ kiện.
2. Đầu chiếm 40–50% chiều cao (trừ khi cố ý đảo ngược), không cổ.
3. Một món nhận diện đọc được trong bóng đen, **và món đó biết diễn** (tai cụp, tóc rũ khi mệt).
4. Mặt là hình phẳng dán lên khối 3D: tròng trắng, con ngươi liếc được, mí trên nghiêng được, mí dưới đẩy lên được, mày rời từng bên, miệng thay được (nét, chữ D, tròn, lượn sóng), răng, lưỡi.
5. Mặc định luôn bất đối xứng: một mày cao hơn, miệng lệch.
6. Viết tính cách và một câu thoại trước khi dựng hình.
7. Thử bóng đen cho mọi dáng chính.
8. Không cú, không hạt đậu Fall Guys, không chim Finch, không chấm tròn Headspace, không dùng lại hình của ai.

## 5. Chỗ còn thiếu

- Không tìm được bài chính chủ của Duolingo giải thích khối gốc của từng nhân vật; phần 1.2 là tự quan sát.
- Trang `design.duolingo.com/illustration/characters` đã chuyển hướng về blog; các ý [S3] lấy từ đoạn trích của công cụ tìm kiếm, chưa đọc được bản gốc.
- Chưa tìm được bài nào của hoạ sĩ Duolingo nói riêng về đường lực hay cách dựng lông mày.

## Nguồn

- [S1] Duolingo Blog, "Building character" — https://blog.duolingo.com/building-character/
- [S2] Duolingo Blog, "Shape language: Duolingo's art style" — https://blog.duolingo.com/shape-language-duolingos-art-style/
- [S3] Duolingo Design, Illustration / Characters — https://design.duolingo.com/illustration và https://design.duolingo.com/illustration/characters (nay chuyển hướng về https://blog.duolingo.com/hub/design/)
- [S4] Duolingo Blog, "Duolingo female character origin stories" — https://blog.duolingo.com/duolingo-female-character-origin-stories
- [S5] Rive, "Duolingo's AI-powered video call brings Lily to life" — https://rive.app/blog/duolingo-s-ai-powered-video-call-brings-lily-to-life
- [S6] GGRecon, "Fall Guys developers reveal what makes their jelly beans so lovable" — https://www.ggrecon.com/articles/fall-guys-developers-reveal-what-makes-their-jelly-beans-so-lovable ; PlayStation Blog, "Creating the character designs of Fall Guys" — https://blog.playstation.com/?p=224711
- [S7] raw.studio, "Case study: How Headspace designs for mindfulness" — https://raw.studio/?p=1771
- [S8] It's Nice That, bài về bản làm mới Headspace — https://www.itsnicethat.com/articles/italic-studio-headspace-graphic-design-project-250424
- [S9] Dream Farm Studios, "Shape language in character design" — https://dreamfarmstudios.com/shape-language-in-character-design/
- [S10] CG-Wire, "Character shape language" — https://blog.cg-wire.com/character-shape-language/
- Ảnh tham khảo đã tải (từ [S1], [S2]): `refs/duo/cast-jumping.png`, `cast-cover.png`, `duo-junior-shapes.gif`, `cat-shapes.png`, `shape-cover.png`
