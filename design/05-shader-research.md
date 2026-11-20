# 05 — Nghiên cứu kiểu dựng hình (shader) cho dàn nhân vật

Ngày: 2026-11-20. Đọc cùng: [04-character-concepts.md](04-character-concepts.md).
Câu hỏi gốc: *"xem lại xem cách shader có gì độc đáo hơn không"*.
Chưa chốt gì: phần cuối là đề xuất, người chọn là bạn.

**Tóm tắt.** Đã thử 5 kiểu trên cùng một nhân vật (Nghé, dáng hero), mỗi kiểu kèm avatar 128 px. Hai kiểu tôi đề xuất là **nỉ / len chọc** và **riso hạt 2.5D** (bản có nét mực mảnh cho người mẫu động tác). Cả hai đã chạy được trên Mộc (dáng người, đang squat) mà không chỉnh tay riêng. Nghé chỉ là vật thử: toàn bộ kiểu dựng gắn vào thư viện chứ không gắn vào nhân vật, nên dàn nhân vật mới dùng lại được ngay.

Ảnh so sánh: `blender/out/shaders/comparison.png`
Linh vật cạnh người mẫu: `blender/out/shaders/cast_felt.png`, `cast_riso.png`, `cast_risoline.png`

---

## 1. Vì sao bản hiện tại trông "chung chung"

Không chỉ do shader. Nhìn `blender/out/concepts/nghe/hero_preview.png` thì có ba thứ cộng lại:

1. Chất liệu Principled mặc định (nhám 0,5, chút tán xạ dưới bề mặt): đây chính là "vinyl / đất sét mềm" mà gần như mọi bộ icon 3D trên Dribbble đang dùng.
2. Bốn đèn mảng to, mềm: không có bóng đổ nào có hình, mọi thứ chuyển sắc đều.
3. Bề mặt và viền hình trơn tuyệt đối: không có dấu vết của vật liệu hay bàn tay làm ra nó.

Vì vậy mỗi kiểu dưới đây đổi cả ba: chất liệu, đèn, và viền hình hoặc hậu kỳ. Chỉ đổi shader thì ra đúng ảnh cũ phủ một lớp lọc.

## 2. Mười kiểu đã khảo sát

Cột "cỡ nhỏ" là khả năng đọc ở avatar 96 px. Cột "90+ ảnh" tính trên máy này (RTX 4070), ảnh 1200 px.
Ghi chú nguồn: mục nào ghi *(đã mở)* là tôi đọc được trang; *(qua tìm kiếm)* là chỉ có bản tóm tắt kết quả tìm kiếm, chưa mở được trang gốc. Phần "làm trong Blender" là kiến thức Blender của tôi cộng với thứ đã thử thật trong vòng này, không phải trích từ nguồn.

| # | Kiểu | Cái làm nó khác biệt | Làm trong Blender | 90+ ảnh | Rủi ro lệch nhau giữa các ảnh | Cỡ nhỏ |
|---|---|---|---|---|---|---|
| 1 | **Cel / toon + viền mực** (Guilty Gear Xrd/Strive, Genshin, Hi-Fi Rush) | Không có sắc độ trung gian; ranh sáng tối là một nét vẽ có chủ ý; viền mực. Nguyên tắc của Arc System Works: "giết mọi thứ trông 3D" | Shader-to-RGB + ColorRamp chỉ có ở EEVEE. Viền: vỏ lật ngược (inverted hull), Line Art hoặc Freestyle. Tôi làm cách khác để chạy được cả Cycles: dựng lớp màu phẳng + lớp ánh sáng rồi cắt ngưỡng ở hậu kỳ | Rẻ nhất: ~12 giây/ảnh | Thấp nếu ngưỡng cố định. Điểm yếu: bề mặt hơi gợn là ranh sáng tối răng cưa (theo tôi biết ASW sửa pháp tuyến bằng tay từng nhân vật; nguồn tìm được chỉ xác nhận là pháp tuyến phải được kiểm soát rất kỹ) | Rất tốt, viền giữ hình tới 48 px |
| 2 | **Vẽ tay kiểu Arcane** (Fortiche) | Mọi ánh sáng, bóng, nét cọ được vẽ tay lên texture; bề mặt như tranh sơn | Cần trải UV và hoạ sĩ vẽ texture từng nhân vật. Không tự động hoá được | Đắt nhất về công người | Cao: phụ thuộc tay người vẽ | Kém: nét cọ biến mất, còn lại như ảnh mờ |
| 3 | **In offset kiểu Spider-Verse** | Chấm halftone thay cho chuyển sắc, nét gạch, bản màu in lệch, viền mực dày. Phim làm gần hết ở khâu ghép hình (Nuke), không phải ở shader | Hậu kỳ trên các lớp dựng: chấm theo sắc độ, dịch lệch bản màu | ~12 giây/ảnh | Thấp (thuần toán) | Tốt về hình, nhưng nền chấm làm avatar bị rối |
| 4 | **Đất nặn stop-motion** (Aardman, Laika) | Vân tay, vết dụng cụ, bề mặt lồi lõm, đèn sân khấu thật, hình hơi lệch | Bump vân tay bằng Voronoi + sóng tròn, Displace cho bề mặt lồi lõm, đèn nhỏ và gắt. Có sẵn addon Clay Doh, MakeThatClay | ~20 giây/ảnh | Thấp | Kém: vân tay mất hẳn dưới ~600 px, còn lại gần giống bản hiện tại |
| 5 | **Nỉ / bông / len** (Yoshi's Crafted World, Woolly World, Kirby's Epic Yarn) | Sợi lông phá viền hình, chất vải thật, mặt mũi là miếng nỉ cắt đính lên. Cảm giác đồ thủ công | Hệ hạt tóc (sợi ngắn + sợi lạc dài), Sheen, miếng mặt cho dày lên bằng Solidify. Phải là Cycles. Kiểu đan móc thì cần UV | ~55 giây/ảnh (đắt nhất trong các kiểu tự động) | Thấp, hạt giống cố định | Tốt: mặt nỉ tương phản mạnh; lông thành viền mềm |
| 6 | **Hạt đậu bóng kiểu Fall Guys** | Hình bầu cực đơn giản, nhựa bóng, màu chói. Bắt nguồn từ một món đồ chơi vinyl | Principled + lớp phủ bóng. Dễ | ~20 giây/ảnh (ước tính, chưa dựng) | Thấp | Tốt, nhưng **quá gần bản hiện tại** nên không trả lời câu hỏi |
| 7 | **Riso / 2.5D hạt** (kiểu Headspace có hạt) | Không viền; sắc độ làm bằng hạt chấm; số mực giới hạn, in chồng, lệch bản, giấy có thớ | Hậu kỳ: xác suất hạt theo lớp ánh sáng; bóng là một bản mực in chồng | ~12 giây/ảnh | Thấp | Khá: hình vẫn rõ nhưng hạt mịn mất đi, phải có mảng nền màu giữ hình |
| 8 | **Mờ kiểu phim ngắn Pixar** | Tán xạ dưới bề mặt, đèn điện ảnh | Cycles SSS + đèn kỹ | ~20–40 giây/ảnh (ước tính, chưa dựng) | Thấp | Tốt, nhưng cũng **gần bản hiện tại** |
| 9 | **Tượng đồ chơi sơn tay** (art toy, sofubi) | Nhựa bóng, đường ráp khuôn, sơn phun chuyển màu, chi tiết sơn lệch nhẹ | Lớp phủ bóng + mặt nạ sơn. Muốn ra chất cần UV hoặc vẽ mặt nạ | ~20 giây/ảnh (ước tính, chưa dựng) | Trung bình | Khá |
| 10 | **Phẳng 2D + Rive** (Duolingo) | Ít mảng nhất có thể, góc nhìn phẳng, không bóng đổ, tính cách nằm ở chuyển động | Không phải việc của Blender: vẽ vector rồi dựng khớp trong Rive | Không dựng hình; công nằm ở hoạ sĩ + diễn hoạt | Thấp nhất | Tốt nhất |

Bốn kiểu không dựng thử và lý do: (2) Arcane cần hoạ sĩ vẽ texture, không hợp với 90+ ảnh sinh bằng mã; (6) và (8) chỉ là biến thể của thứ đang có; (9) cần UV và mặt nạ sơn; (10) là hướng 2D, đã bàn ở các tài liệu trước.

## 3. Năm bản thử (Nghé, dáng hero, 1200 px + avatar 128 px)

Thời gian đo thật, mỗi lần gồm cả dựng nhân vật, ảnh lớn và ảnh avatar:

| Kiểu | Ảnh lớn | Avatar | Cả lượt | Ước tính 90 ảnh lớn |
|---|---|---|---|---|
| 0. Hiện tại (đối chứng) | 15,6 s | 3,2 s | 19 s | ~25 phút |
| 1. Cel + viền mực | 10,3 s dựng lớp + ~1,6 s hậu kỳ | 6,6 s | 18 s (dùng chung lớp với 2 và 3) | ~18 phút |
| 2. Truyện tranh in offset | cùng lớp, +1,6 s | như trên | như trên | ~18 phút |
| 3. Riso hạt 2.5D | cùng lớp, +1,6 s | như trên | như trên | ~18 phút |
| 4. Nỉ / len chọc | 37 s | 16 s | 57 s | ~55 phút |
| 5. Đất nặn stop-motion | 16,4 s | 3,5 s | 20 s | ~25 phút |

Ba kiểu 2D dùng chung một lần dựng lớp (màu phẳng, màu phẳng + viền mực, và một ảnh ánh sáng mã hoá ba kênh: đèn chính, đèn ven, độ khuất). Đổi kiểu chỉ mất 1,6 giây, không phải dựng lại.

### Nhận xét thẳng từng kiểu

**1. Cel + viền mực** (`cel/nghe_hero.png`)
- Được: rõ ràng nhất, rẻ nhất, ở 48 px vẫn nhận ra Nghé. Viền mực màu chàm (không phải đen) làm nó bớt "hoạt hình mặc định".
- Chưa được: đây là kiểu ít khác biệt nhất trong năm kiểu. Đặt cạnh ảnh Chai của Hi-Fi Rush (`refs/hifi_chai.jpg`) thì thiếu hẳn phần "nét vẽ có chủ ý": nét của họ dày mỏng theo hình và bóng là mảng được vẽ, còn nét của tôi đều một cỡ và ranh sáng tối đi theo hình học. Đặt cạnh dàn Duolingo (`design/refs/duo/cast-jumping.png`) thì lộ ra điều quan trọng hơn: Duolingo không có viền, không có bóng, cá tính nằm ở hình khối và dáng. Tức là cel không kéo ta lại gần Duolingo, nó chỉ là bản 3D được tô gọn lại. (Ảnh Guilty Gear tải không được nên tôi không so trực tiếp.)

**2. Truyện tranh in offset** (`comic/nghe_hero.png`)
- Được: cá tính mạnh nhất khi nhìn ảnh lớn. Chấm halftone, nét gạch trong vùng tối, viền lệch màu hồng và xanh đều đọc được.
- Chưa được: ồn. Nền chấm tranh chỗ với nhân vật, ở avatar thì thành nhiễu. Đặt vào giao diện có chữ và nút sẽ phải bỏ nền, mà bỏ nền thì mất một nửa chất. Và đây là kiểu đang rất nhiều người bắt chước.

**3. Riso hạt 2.5D** (`riso/nghe_hero.png`, bản có nét: `risoline/`)
- Được: đẹp nhất về mặt đồ hoạ, hợp giao diện app nhất (nền giấy, mảng màu phẳng, ít chi tiết thừa). Bóng bằng hạt và bản mực in chồng cho cảm giác in tay mà vẫn giữ khối 3D.
- So với Headspace (`design/refs/f3-warm-05-headspace-5.jpg`): ảnh đó là vector phẳng hoàn toàn, không có hạt, nên bản của tôi có chất liệu hơn. Nhưng đĩa tròn vàng cam phía sau nhân vật lại trùng đúng mô-típ mặt trời của Headspace; nếu chọn hướng này nên đổi hình hoặc màu mảng nền để khỏi bị nói là giống.
- Chưa được: (a) không có viền nên phần màu sáng tan vào nền giấy; vòng 1 cái sừng gần như biến mất, vòng 2 phải thêm đĩa màu vàng phía sau mới giữ được hình. Tức là kiểu này **bắt buộc có mảng nền màu**. (b) Ở 128 px hạt mịn mất, avatar trông như tranh phẳng có chuyển sắc mềm: vẫn đẹp, nhưng cái "riso" chỉ sống ở ảnh lớn. (c) Tay và thân cùng màu chỉ tách nhau bằng hạt bóng, nên với người mẫu động tác tôi làm thêm bản lai có nét mực mảnh.

**4. Nỉ / len chọc** (`felt/nghe_hero.png`)
- Được: khác hẳn mọi app tập luyện đang có. Sợi lông phá viền hình, miếng mặt nỉ đính nổi đổ bóng thật, nhìn là muốn cầm. Avatar đọc tốt vì mặt tương phản mạnh với nền lông.
- Chưa được: (a) đắt gấp ba lần các kiểu khác. (b) **Màu chưa giải quyết xong.** Vòng 3 bị bạc màu vì lớp Sheen, vòng 4 chỉnh quá tay thành xanh dương điện, bản cuối vẫn tối hơn và xanh hơn hẳn màu chàm `#6360E0` của bảng màu (nhìn `comparison.png` là thấy, không phải lệch nhẹ). Nguyên nhân tôi đoán: sợi tự che bóng lẫn nhau làm tối và đậm màu, cộng với nút chỉnh HSV. Đã hết 5 vòng nên tôi để nguyên và ghi ra đây. (c) Lông làm mờ chi tiết mảnh; nếu dàn nhân vật mới có ngón tay thì phải thử lại. (d) Đặt cạnh bìa Yoshi's Crafted World (`refs/felt_yoshi_cover.jpg`): lông của họ ngắn và dày hơn, màu tươi và sáng hơn nhiều, đèn chính mạnh hơn; bản của tôi tối và trầm. Còn thiếu đường chỉ khâu, thứ làm nên cảm giác "may tay".

**5. Đất nặn stop-motion** (`clay/nghe_hero.png`)
- Được: bề mặt lồi lõm và đèn gắt cho cảm giác vật thật hơn bản hiện tại.
- Chưa được: yếu nhất. Vân tay phải soi ở cỡ 1200 px mới thấy, ở avatar thì gần như không phân biệt được với bản đối chứng. Vòng 1 vân tay ra thành đường đồng mức như lỗi máy in 3D; vòng 2–3 mắt bị bóng loáng che mất con ngươi. Sửa xong, đặt cạnh ảnh Morph (`refs/clay_morph.jpg`) thì thấy rõ khoảng cách: Morph lì, có vệt miết ngón tay và chỗ dày chỗ mỏng, còn bản của tôi vẫn đọc ra nhựa trơn có vài chỗ phồng. Thêm nữa, hướng đất nặn đã bị loại một lần ở vòng nhân vật.

### Nhật ký vòng duyệt

- **Vòng 1** (600–700 px): ba kiểu 2D chạy ngay. Nỉ ra cục bông xù che hết mặt. Đất nặn ra vân đồng mức, mắt hỏng.
- **Vòng 2**: cel thêm sắc độ thứ ba; riso thêm đĩa nền. Nỉ treo máy hơn 6 phút: đo lại thì độ dài sợi trong Blender tính bằng 4 × vận tốc phát chứ không theo ô "hair length", tức sợi đang dài 2–5 đơn vị. Sửa xong còn 27 giây và ra đúng chất nỉ.
- **Vòng 3** (1200 px): nỉ bạc màu; đất nặn mất con ngươi do mắt phản chiếu đèn và do bề mặt lồi lõm không đi theo xương.
- **Vòng 4**: đưa lớp lồi lõm lên trước khung xương, hạ bóng mắt, vân tay thưa lại. Nỉ tăng màu thì thành quá tay.
- **Vòng 5**: nỉ về màu gần đúng. Dựng Mộc, thêm bản riso có nét. Dừng.

Ảnh hỏng của các vòng trước đã xoá; trong thư mục chỉ còn bản cuối.

## 4. Thử trên dáng người (Mộc đang squat)

Dàn nhân vật hiện tại sẽ bị thay, nên thay vì dựng Ớt và Bự, tôi thử hai kiểu đề xuất trên một hình dạng khác hẳn: Mộc, tỉ lệ người, tay chân dài, đang cầm tạ.

- **Nỉ** (`cast_felt.png`): Mộc ra thành búp bê nỉ, cùng một thế giới với Nghé. Tạ không qua hàm dựng của thư viện nên vẫn là nhựa trơn; khi làm thật cần quyết định đạo cụ có phủ nỉ không. Tay, đùi, thân cùng màu và cùng phủ lông nên góc khớp đọc kém hơn một chút so với bản có viền.
- **Riso** (`cast_riso.png`) và **riso + nét** (`cast_risoline.png`): bản có nét đọc tư thế rõ hơn (viền tách đùi, cẳng tay và tạ). Bản không nét đẹp hơn cho linh vật. Hai bản sinh ra từ cùng một lần dựng nên dùng lẫn không tốn gì, nhưng cần quyết định: toàn bộ có nét, hay chỉ người mẫu có nét.

Cả hai lần đều không chỉnh tham số riêng cho Mộc, ngoài khung máy quay avatar.

## 5. Đề xuất

**Hạng 1 — Nỉ / len chọc.** Lý do: đây là kiểu duy nhất mà người xem nhận ra ngay "app này không giống app nào", và nó hợp tinh thần nhóm bạn tập với nhau (đồ thủ công, ấm, hơi vụng). Nó cũng giữ được ở cỡ nhỏ. Cái giá thật:
- Khoảng 55 phút cho 90 ảnh, so với 18–25 phút của các kiểu khác. Vẫn là một lần chạy qua đêm, không phải trở ngại.
- Màu hiện đang sai so với bảng màu (tối và xanh hơn) và chưa sửa được trong 5 vòng; phải giải quyết xong trước khi dựng hàng loạt, và cân lại theo từng bảng màu nhân vật mới.
- Cần thêm một vòng cho đường chỉ khâu và cho đạo cụ thì mới tới mức Yoshi.
- Chưa thử chuyển động. Nếu sau này cần hoạt hình thì lông sẽ là chi phí lớn.

**Hạng 2 — Riso hạt 2.5D, người mẫu động tác dùng bản có nét.** Lý do: rẻ nhất, hợp giao diện nhất, hoàn toàn tất định (cùng đầu vào thì cùng đầu ra), đổi bảng màu không cần chỉnh gì. Cái giá thật:
- Luôn phải có mảng nền màu sau nhân vật; nhân vật đứng trơ trên nền sáng sẽ mất viền.
- Ở avatar nhỏ nó mất chất hạt, chỉ còn là minh hoạ phẳng đẹp. Độ độc đáo thấp hơn nỉ.
- Phong cách hạt đang phổ biến trong minh hoạ; cái riêng ở đây là khối 3D bên dưới.

**Không đề xuất:** đất nặn (mất hết ở cỡ nhỏ, đã bị loại một lần), cel thuần (rõ nhưng ít khác biệt nhất), truyện tranh offset (mạnh ở poster, ồn trong giao diện; hợp cho màn ăn mừng hoặc ảnh chia sẻ hơn là phong cách chính).

Nếu phải chọn một câu: **muốn khác biệt thì chọn nỉ, muốn chắc tay và rẻ thì chọn riso.** Hai kiểu không nên trộn trong cùng một màn hình.

### Điều tôi không chứng minh được

- Mới thử 2 nhân vật, 2 dáng. Chưa thử biểu cảm khác, chưa thử trên nền tối, chưa đặt vào màn hình app thật.
- Ảnh tham chiếu mỏng: 7 tấm tải được (áp phích, ảnh chụp màn hình từ Wikipedia và Foundry) ở `blender/out/shaders/refs/`, cộng hai tấm có sẵn trong `design/refs/` (dàn Duolingo, màn hình Headspace). Tìm ảnh qua công cụ tìm kiếm trả về kết quả rác nên tôi bỏ. Không có ảnh in riso thật và không có ảnh Guilty Gear; phần hạt riso tôi đánh giá theo hiểu biết về kỹ thuật in. Mỗi kiểu chỉ được so với một tấm, và tôi chỉ đặt cạnh nhau ở bản cuối chứ không phải ở từng vòng.
- Hai nguồn không mở được: bản PDF bài nói của Motomura (máy chủ từ chối kết nối) và bài Codrops về hạt riso (bị chặn 403). Thông tin từ hai nguồn này chỉ qua tóm tắt tìm kiếm.
- "Có nhớ được không, có thích không" là câu của người dùng thật.

## 6. Cách dựng lại

Mã ở `blender/shaders/`, không sửa gì trong `blender/concepts/` (gắn vào bằng cách thay `lib.clay`, `lib.make`, `lib.decal`, `lib.stage` trước khi nhân vật được dựng, nên nhân vật mới viết theo cùng thư viện sẽ dùng được ngay).

```
tools\blender-4.5.16-windows-x64\blender.exe -b -P blender\shaders\style_run.py -- <nghe|moc> <dáng> <base|felt|clay|npr> [--size 1200] [--avatar 512] [--samples 192]
python blender\shaders\sheet.py finish  nghe_hero      (hậu kỳ 2D + avatar 128 px cho mọi kiểu)
python blender\shaders\sheet.py compare nghe_hero      (-> out\shaders\comparison.png)
python blender\shaders\sheet.py cast nghe_hero moc_squat felt riso risoline
python blender\shaders\post2d.py <thư mục lớp> <flat|cel|comic|riso|risoline> <ảnh ra> [cỡ cuối]
```

- `style_run.py`: chất liệu nỉ, đất nặn, và bộ dựng lớp cho các kiểu 2D (viền mực bằng vỏ lật ngược).
- `post2d.py`: cel, truyện tranh, riso từ các lớp. Cỡ nét, bước chấm, cỡ hạt khai theo điểm ảnh **của ảnh cuối**, nên avatar 128 px có hoạ tiết thiết kế riêng cho 128 px chứ không phải hoạ tiết 1200 px bị thu nhỏ. Có sẵn kiểu `flat` (mảng phẳng không bóng, gần Duolingo) để đối chiếu.
- Các lớp trung gian giữ ở `out/shaders/_passes/` (4 MB) để chỉnh hậu kỳ mà không phải dựng lại.

## 7. Nguồn

Cel / toon
- Motomura, "GuiltyGearXrd's Art Style: The X Factor Between 2D and 3D", GDC 2015: https://gdcvault.com/play/1022031/GuiltyGearXrd-s-Art-Style-The · bản PDF: https://www.ggxrd.com/Motomura_Junya_GuiltyGearXrd.pdf *(qua tìm kiếm; PDF không mở được)*
- Arc System Works đăng lại bài nói: https://www.arcsystemworks.com/guilty-gear-xrd-art-talk-at-game-developers-conference-2015/ *(qua tìm kiếm)*
- 80.lv, "The Making of Hi-Fi Rush's 3D Toon Rendering Style" (bài nói GDC 2024 của Tango Gameworks): https://80.lv/articles/the-making-of-hi-fi-rush-s-3d-toon-rendering-style *(đã mở; bài chỉ nêu đề mục, không có chi tiết kỹ thuật)*

Spider-Verse
- Foundry, "Re-writing the rule book on Spider-Man: Into the Spider-Verse" (các công cụ Hatcher, Thresher, ChromaShifter trong Nuke): https://www.foundry.com/insights/film-tv/graphic-look-in-comp-spiderman *(đã mở)*
- Foundry, "Creating Spider-Man: Across the Spider-Verse with Nuke, Mari & Katana": https://foundry.com/insights/film-tv/across-the-spider-verse-nuke-mari-katana *(qua tìm kiếm)*
- AWN, "Rewriting the Visual Rule Book on Spider-Man: Into the Spider-Verse": https://www.awn.com/print/animationworld/rewriting-visual-rule-book-spider-man-spider-verse *(qua tìm kiếm)*

Arcane
- 80.lv, hoạ sĩ Arcane kết hợp vẽ tay và 3D cho phông nền: https://80.lv/articles/arcane-artists-show-how-they-combine-traditional-art-3d-for-backgrounds *(qua tìm kiếm)*
- RedShark, vì sao Arcane đẹp: https://redsharknews.com/why-netflixs-arcane-looks-so-good-how-fortiche-ramped-up-the-animation-pipeline *(qua tìm kiếm)*

Đất nặn
- 80.lv, Clay Doh (shader đất nặn thủ tục cho Cycles và EEVEE, có vân tay và vết nứt): https://80.lv/articles/clay-d-oh-a-clay-shader-for-blender *(đã mở)*
- MakeThatClay (mã nguồn mở): https://www.github.com/kents00/MakethatClay *(qua tìm kiếm)*
- SouthernShotty, hoạt hình kiểu stop-motion trong Blender 2.8: https://www.3dart.it/stop-motion-style-animation-in-3d-blender-2-8/ *(qua tìm kiếm)*
- School of Motion, claymation trong Cinema 4D (nguyên tắc: tốc độ khung thấp, bề mặt đổi theo khung): https://www.schoolofmotion.com/tutorials/claymation-cinema-4d *(qua tìm kiếm)*

Nỉ / len
- Yoshi's Crafted World: https://en.wikipedia.org/wiki/Yoshi%27s_Crafted_World *(qua tìm kiếm; ảnh bìa đã xem)*
- Nintendo Life, phỏng vấn nhóm làm Yoshi's Woolly World: https://www.nintendolife.com/news/2015/06/interview_knitting_together_the_pattern_of_yoshis_woolly_world_and_cuddly_amiibo *(qua tìm kiếm)*
- Nintendo Everything, nhóm Crafted World nói về Unreal Engine 4: https://nintendoeverything.com/tag/etsunobu-ebisu/ *(qua tìm kiếm)*

Fall Guys
- PlayStation Blog, "Creating the Character Designs of Fall Guys": https://blog.playstation.com/?p=224711 *(qua tìm kiếm)*
- Kotaku, "The Art of Fall Guys": https://kotaku.com/the-art-of-fall-guys-1845500683 *(qua tìm kiếm)*

Riso / hạt
- Codrops, "Creating a Risograph Grain Light Effect in Three.js": https://tympanus.net/codrops/2022/03/07/creating-a-risograph-grain-light-effect-in-three-js/ *(qua tìm kiếm; trang chặn 403)*
- Mã kèm theo: https://github.com/Robpayot/risograph-grain-shader *(qua tìm kiếm)*

Duolingo
- "Shape language: Duolingo's art style": https://blog.duolingo.com/shape-language-duolingos-art-style/ *(đã mở)*
- Hướng dẫn minh hoạ: https://design.duolingo.com/illustration *(qua tìm kiếm)*
- Rive, trang về diễn hoạt nhân vật (nêu Duolingo dựng nhân vật trong Rive): https://rive.app/use-cases/character-animation *(qua tìm kiếm)*

## 8. File

| | Đường dẫn |
|---|---|
| Bảng so sánh 6 ô | `blender/out/shaders/comparison.png` |
| Linh vật + người mẫu | `blender/out/shaders/cast_felt.png`, `cast_riso.png`, `cast_risoline.png` |
| Ảnh từng kiểu | `blender/out/shaders/<base|cel|comic|riso|risoline|felt|clay>/<nghe_hero|moc_squat>.png` và `..._avatar128.png` (đất nặn chỉ có Nghé) |
| Ảnh tham chiếu | `blender/out/shaders/refs/` |
| Mã | `blender/shaders/style_run.py`, `post2d.py`, `sheet.py` |
