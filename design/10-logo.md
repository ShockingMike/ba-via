# 10 — Logo "Tạ Nhỏ"

Ngày: 2026-11-20. Đọc cùng: [09-naming.md](09-naming.md) (hệ 5), trang chọn: [logo-options.html](logo-options.html), file: [logo/](logo/).

**Đã chốt 2026-11-21: người dùng chọn hướng C "Ba màu, một quả tạ".** Bản cuối và file ở mục "Bản cuối" cuối file này và trong `logo/final/`. Phần trên ghi nghiên cứu, bốn hướng và kết quả chấm mù của bước chọn hướng.

Từ ngữ: Khăn, Bình, Găng là **bạn đồng hành**. Quả tạ là biểu tượng của thương hiệu, không phải nhân vật, nên không hướng nào vẽ mặt lên quả tạ.

## 1. Nghiên cứu

Cách làm: tải icon App Store thật (iTunes Search API, `artworkUrl512`) của Duolingo, Finch, Headspace, Strava, Nike Training Club, Ladder, Gentler Streak, Fitbod, và bốn thương hiệu dẫn bằng nhân vật (Duolingo ABC, Pokémon Sleep, Neko Atsume 2, Waterllama), thu về 180/60/40 px rồi nhìn cạnh nhau. Ảnh nằm ở `logo/_work/ref/` (chỉ để so, không dùng trong trang chọn). Phần "nhận xét" dưới đây là quan sát trên ảnh đó; phần "nguồn" là điều đọc được từ tài liệu. Chỉ xem icon; chữ logo của các hãng không được xem trực tiếp, cột "Chữ" chỉ ghi điều đọc được, chỗ nào không có nguồn thì ghi "chưa kiểm".

| Thương hiệu | Icon là gì | Vì sao đọc được ở 60 px | Chữ |
|---|---|---|---|
| Duolingo | Mặt cú cắt sát, hai mắt chiếm gần nửa ô | Một khối, hai mắt to, không có chữ | Chữ riêng Feather Bold, vẽ theo dáng lông của Duo (nguồn: Creative Bloq, Johnson Banks) |
| Finch | Mặt chim cắt sát hơn nữa: hai mắt, mỏ, má | Chỉ 4 mảng màu phẳng | chưa kiểm |
| Headspace | Một chấm cam có nét cười | Một hình, một màu, nền trắng | chưa kiểm (một nguồn thứ cấp nói chấm cam cố ý không tròn đều) |
| Strava | Một ký hiệu hai mũi nhọn trắng trên cam | Một hình, hai màu, tương phản cao | chưa kiểm |
| Nike Training Club | Swoosh + "NTC" đen trên trắng | Đọc được nhờ 3 chữ rất to; là ngoại lệ vì đã có swoosh | — |
| Ladder | Một chữ cái vẽ thành cái thang, đen trên vàng chanh | Một chữ cái = một ý (thang) | Chính chữ đó là logo |
| Gentler Streak | Một khối trái tim/hạt đậu cam, nổi nhẹ trên nền trắng | Một hình, bóng đổ rất nhẹ | — |
| Fitbod | Chữ F trong lục giác | Hình học, hai màu | — |
| Duolingo ABC, Pokémon Sleep, Neko Atsume, Waterllama | Nhân vật | Bản nào cắt sát mặt thì rõ; bản vẽ cả cảnh (Pokémon Sleep, Tamagotchi) thành nhiễu ở 40 px | — |

Rút ra:

1. **Một hình, tối đa ba màu.** Icon nào còn rõ ở 40 px cũng chỉ có một vật và hai, ba mảng màu.
2. **Hình chiếm 60–90 % ô.** Vòng tròn nằm trong ô vuông bo góc phí khoảng 40 % diện tích.
3. **Không có chữ trong icon**, trừ khi chữ chính là hình (Ladder, NTC).
4. **Chất liệu biến mất dưới 60 px.** Sợi nỉ chỉ còn là nhiễu; cỡ nhỏ phải dùng bản phẳng. Apple cũng khuyên tránh ảnh chụp và chi tiết nhỏ trong icon (nguồn: HIG, đọc qua bản trích).
5. **Màu nền là một nửa nhận diện.** Cam `#FF5B1E` của app nằm sát cam Strava và Headspace, và bộ quy tắc thiết kế dành cam cho nút chính. Vì vậy không hướng nào dùng nền cam.
6. **Chữ "sở hữu được" khi có một chi tiết lặp lại ở icon.** Duolingo lấy dáng lông vào chữ; Ladder lấy chữ làm icon.
7. **Quả tạ là hình app gym nào cũng dùng** (đã ghi ở file 09). Cái riêng phải đến từ tỉ lệ, màu, hoặc một ý chỉ tên này mới có.

Ý chỉ tên này mới có: trong tiếng Việt, dấu chấm dưới chữ "ạ" tên là **dấu nặng**. Thay nó bằng một quả tạ là đúng nghĩa đen.

## 2. Chữ "Tạ Nhỏ"

- Nền: Baloo 2 ExtraBold (đúng chữ hiển thị của app), xuất thành đường nét (path), không còn là `<text>`.
- Tự vẽ: **dấu hỏi** trên "ỏ" (một nét tròn đầu, dày gần bằng thân chữ, không có chấm) và **dấu nặng** dưới "ạ" (chấm tròn, hoặc quả tạ ở hướng B). Dựng từ chữ gốc T, a, N, h, o rồi đặt dấu riêng.
- Tự chỉnh khoảng cách: T ôm vào a (−58 đơn vị), N–h, h–o sát lại, khoảng giữa hai chữ hẹp hơn mặc định.
- Luật rút từ chấm mù: dấu nặng **không tô màu nhạt** ở cỡ nhỏ (mất dấu thì thành "Ta Nhỏ"); quả tạ trong chữ đổi về chấm tròn khi chữ thấp hơn khoảng 24 px (`logo/B-wordmark-nho.svg`).

## 3. Bốn hướng

| | Hướng | Biểu tượng | Chữ | Nền icon |
|---|---|---|---|---|
| A | Quả tạ khâu tay | Quả tạ nỉ mập, bốn mũi khâu mỗi đầu, tay cầm quấn băng | Tạ Nhỏ, chấm tròn | Xanh ngọc `#22B8A9` |
| B | Dấu nặng là quả tạ | Chữ "ạ", dấu nặng là quả tạ | tạ nhỏ viết thường, dấu nặng là quả tạ | Vàng `#FFC93C` |
| C | Ba màu, một quả tạ | Quả tạ ghép màu ba bạn đồng hành: đầu xanh ngọc, tay cầm cam, đầu chàm | TẠ NHỎ viết hoa, giãn chữ | Kem `#FFF1CF` |
| D | Khăn khoe tạ | Mặt Khăn (bạn đồng hành) cắt sát, tay giơ quả tạ nhỏ | Tạ Nhỏ, chấm tròn | Xanh ngọc của khăn / kem ở bản nỉ |

Mỗi hướng có: bản dựng nỉ (Blender, dùng `vlib.felt()` và sợi của dàn nhân vật), bản phẳng SVG, lockup, icon 1024/180 (nỉ) và 60/40 (phẳng và nỉ để so), bản một màu dương và âm.

Hướng D dùng rig Khăn đã duyệt, chỉ đổi tư thế; không sửa file `v_khan.py`.

## 4. Chấm mù

Theo luật dự án, không tự chấm. Mỗi vòng một agent khác chỉ nhận ảnh (icon của ta đặt cạnh Duolingo, Finch, Strava ở 180/60/40 px và bản 40 px phóng 4 lần) và ba câu hỏi: đọc được ở 40 px không, có riêng không, người làm nghề có gọi là nghiệp dư không. Ảnh: `logo/_work/t/gate1_*.png`, `gate2_*.png`, `gate3_*.png`.

| Vòng | Kết quả (thang 10, icon tham chiếu là mốc) | Đã sửa |
|---|---|---|
| 1 | A 5 · B 6,5 · C 4 (miếng vá tròn có chữ: "mẫu huy hiệu thủ công, bỏ") · D 4 (Khăn nấp sau thanh tạ: "robot xanh, tạ đòn chứ không phải tạ tay"). Dấu hỏi "giống dấu chấm hỏi, nhẹ hơn thân chữ" | Bỏ miếng vá, thay C bằng quả tạ ba màu. D làm lại thành mặt cắt sát. A bỏ thẻ giặt, đổi đường khâu đứt thành bốn mũi to. Vẽ lại dấu hỏi |
| 2 | Bản phẳng: B 6,5 · A 5,5 · C 5 · D 4,5. Bản nỉ thấp hơn bản phẳng ở mọi hướng khi xuống 60/40 px. C: "hai đầu khác dáng trông như lỗi". B: "quả tạ quá nhỏ, cam trên vàng thiếu tương phản". Dấu nặng tô màu "gần như mất ở cỡ nhỏ" | C: hai đầu cùng dáng, còn ba màu. B: quả tạ to gấp rưỡi, tay cầm màu mực, đặt sát chữ. Dấu nặng về màu mực, nâng lên; dấu hỏi dày thêm |
| 3 | Nỉ / phẳng: C 7 / 6,5 · D 6,5 / 6 · A 6 / 5,5 · B 5 / 6. Xếp hạng đảo: C, A, D, B. B: "ở 40 px người lạ thấy icon Amazon; chữ ạ đứng riêng là một từ khác". C: "biểu tượng riêng nhất, nhưng nền kem chìm trên nền sáng, bản một màu giống cái búa". Dấu hỏi và chấm tròn: không sai chính tả; quả tạ làm dấu nặng ở cỡ rất nhỏ thì mất dấu | Chưa sửa gì sau vòng này. Luật cỡ nhỏ cho dấu nặng đã có (`B-wordmark-nho.svg`) |

Kết luận thẳng: **chưa hướng nào đạt mức hoàn thiện của ba icon tham chiếu**, và ba người chấm **không thống nhất**: vòng 1, 2 xếp B đầu; vòng 3 xếp C đầu và B cuối. Cả ba vòng đều coi A là phương án an toàn và đề nghị để D làm sticker thay vì icon.

## 5. Đề xuất

**Icon: hướng C (quả tạ ba màu). Chữ: giữ ý dấu nặng là quả tạ của B, chỉ dùng ở cỡ lớn.** Lý do đổi so với hai vòng đầu: nhận xét "giống icon Amazon" ở vòng 3 là rủi ro thật với B khi làm icon, còn ý dấu nặng vẫn dùng tốt trong chữ.

Điểm yếu còn lại:
- B làm icon: dễ lẫn với icon Amazon ở 40 px; "ạ" đứng riêng là một từ khác.
- C: nền kem chìm trên hình nền sáng (phải đổi nền hoặc thêm viền), tay cầm còn mảnh.
- Thân chữ vẫn là nét Baloo 2; muốn thật sự riêng phải vẽ lại cả năm chữ cái.
- A ở 40 px chỉ là "một quả tạ".
- C cần biết ba bạn đồng hành mới hiểu; bản một màu mất ý và hơi giống cái búa.
- D đặt mặt một bạn đồng hành lên icon, thiệt cho người chọn Bình hoặc Găng; quả tạ gần như mất ở 40 px.
- Bản nỉ chỉ dùng được từ 180 px trở lên.
- Chưa thử trên máy thật, chưa thử icon Android dạng adaptive, chưa có bản maskable cho PWA.

## 6. File

- `logo/<A|B|C|D>-mark.svg`, `-mark-1mau.svg`, `-mark-1mau-am.svg`, `-wordmark.svg`, `-wordmark-1mau.svg`, `-lockup.svg`, `-lockup-1mau.svg`
- `logo/<X>-icon-phang.svg` (đủ chi tiết), `-icon-phang-nho.svg` (cho 60/40), `-icon-phang-60.png`, `-icon-phang-40.png`
- `logo/<X>-icon-ni-1024.png`, `-180.png`, `-60.png`, `-40.png`; `logo/<X>-ni-render.png` (nền trong)
- `logo/B-wordmark-nho.svg`: chữ B với dấu nặng tròn cho cỡ nhỏ
- `logo/_work/`: mã dựng lại. `logo_scene.py` (Blender: `blender -b -P logo_scene.py -- A --size 1400 --samples 160 --tag _n --noshadow`), `flat.py` (SVG), `comp.py` (ghép icon nỉ), `build.py` (xuất mọi file), `make_page.py` (trang chọn), `gate.py` (bảng chấm mù). `glyphs.json` là nguồn duy nhất của nét chữ (xuất từ Baloo 2 wght 800 bằng fontTools), phải giữ

## Nguồn

- Creative Bloq, chữ Feather Bold của Duolingo — https://www.creativebloq.com/news/feather-bold
- Johnson Banks, "Everyone can Duolingo" — https://www.johnsonbanks.co.uk/templates/work/duolingo
- Duolingo, hướng dẫn logo — https://design.duolingo.com/identity/logos
- Fabrik, lịch sử logo Headspace — https://fabrikbrands.com/branding-matters/logofile/headspace-logo-history-symbol-and-meaning/
- Apple Human Interface Guidelines, App icons — https://developer.apple.com/design/human-interface-guidelines/app-icons
- Sketch, phỏng vấn nhóm Gentler Streak — https://sketch.com/blog/gentler-streak

---

# Bản cuối — hướng C đã chọn (2026-11-21)

Người dùng chọn hướng C "Ba màu, một quả tạ". File cuối nằm ở `logo/final/`. Các mục 5 (đề xuất) ở trên chỉ còn là lịch sử.

## Đã sửa

| Điểm yếu | Cách sửa |
|---|---|
| Nền kem chìm trên hình nền sáng | Thử sáu nền (mực, mực nhạt, vàng, kem, cam, tím mận) trên màn sáng, tối và ảnh nền (`logo/_work/t/final_tiles.png`). Chọn **vàng `#FFC93C`**: đứng được ở cả ba, và xanh ngọc, chàm nổi rõ nhất. Mực bị chìm trên màn tối |
| Tay cầm mảnh | Bản phẳng: cao 300 trên đầu tạ 580 (trước là 176). Bản nỉ: bán kính 0,096 (trước 0,066). Cam tay cầm đậm hơn một nấc (`#F2500F`) |
| Bản một màu giống cái búa | Hai đầu tạ cùng một dáng; bản một màu chỉ có hai đầu tạ, khe hở, tay cầm và một rãnh ngang mỗi đầu. Dùng mask nên rãnh là lỗ thật, đặt trên nền nào cũng được |
| Cỡ rất nhỏ | Vẽ riêng cho 32 px trở xuống: hai đầu tạ và tay cầm, không chi tiết (`mark-nho.svg`, `mark-1mau-*-nho.svg`, favicon, icon 40) |
| Ba bản vẽ lệch nhau | Một hình gốc cho mọi bản: đầu tạ 288 × 580 bo 116, vòng cổ tạ, tay cầm 300, nghiêng 12°, một sọc kem mỗi đầu (sọc khăn của Khăn ở dưới, băng đô của Găng ở trên). Bản nỉ dựng lại theo đúng hình này, bỏ vạch chia trên tay cầm |
| Chữ | "Tạ Nhỏ" viết hoa đầu chữ (người chấm vòng 3 của bước chọn hướng thấy bản viết hoa cả là cứng nhất). Dấu hỏi: một nét dày 92 đơn vị, đặt giữa chữ o. Dấu nặng: một "bánh tạ" vuông bo 126 × 108, nghiêng 12° như quả tạ. Lockup chừa một khoảng trước chữ T |

## Chấm mù bản cuối (3 vòng, cạnh Duolingo, Finch, Strava, màn sáng và tối)

| Vòng | Icon nỉ | Icon phẳng | Lockup | Một màu | Ý chính |
|---|---|---|---|---|---|
| 1 | 6 | 6,5 | 6,5 | 5 | Nền vàng đứng được ở cả hai màn. Bản nỉ nghiêng ngược bản phẳng; một màu ở 16 px hỏng |
| 2 | 6,5 | 6 | 5,5 | 4 | "Bốn bản vẽ anh em chứ không phải một"; vạch chia trên tay cầm thành nhiễu; biểu tượng dính vào chữ T |
| 3 | 6 | 6,5 | 7 | 5 | Không có lỗi chính tả tiếng Việt. Cam trên vàng là cặp tương phản thấp nhất; nền còn phẳng; dấu hỏi còn nhẹ hơn thân chữ |

Sau vòng 3 không sửa thêm, nên bảng trên đúng với file đang có. Người chấm vòng 3 nói hai đầu tạ không đều; trong file hai đầu cùng kích thước, cái họ thấy là do nghiêng.

## Còn yếu

- **Bản một màu mới sửa được một phần** (5/10 ở vòng cuối): ở 24 px là "quả tạ, vừa đủ"; ở 96 và 48 px rãnh ngang cộng độ nghiêng vẫn gợi cái búa hoặc viên thuốc. Bản không rãnh cho cỡ nhỏ cũng từng bị nhận xét giống khúc xương, nên bỏ rãnh chưa chắc là cách sửa.
- Tay cầm cam trên nền vàng mờ đi trước tiên ở 40 px.
- Nền icon là một màu phẳng, chưa có chiều sâu như icon tham chiếu.
- Bản một màu ở 16 px chỉ còn là một gạch; đừng dùng dưới 24 px.
- Bản nỉ chỉ dùng từ 152 px trở lên.
- Dấu hỏi còn hơi nhẹ so với thân chữ; thân chữ vẫn là nét Baloo 2.
- Chưa thử trên máy thật và chưa thử icon adaptive của Android.

## File trong `logo/final/`

- Icon: `icon-1024/512/192/180/152.png` (nỉ), `icon-120/60.png` (phẳng), `icon-40.png` (phẳng, bản vẽ cỡ nhỏ), `icon-maskable-512/192.png` (hình nằm trong vùng an toàn 80 %), `icon.svg`, `icon-nho.svg`, `icon-rat-nho.svg`
- `favicon.svg`, `favicon-32.png`
- `lockup-ngang.svg`, `lockup-doc.svg`, `lockup-ngang-nho.svg`; một màu: `lockup-ngang-1mau-dam.svg`, `-sang.svg`, `lockup-doc-1mau-dam.svg`, `-sang.svg`
- `wordmark.svg`, `wordmark-sang.svg`, `wordmark-lon-dau-ta.svg` (dấu nặng là quả tạ, chỉ cho cỡ lớn)
- `mark.svg`, `mark-nho.svg`, `mark-1mau-dam.svg`, `mark-1mau-sang.svg`, `mark-1mau-dam-nho.svg`, `mark-1mau-sang-nho.svg`
- `hero-ni.png`: bản dựng nỉ, nền trong, không bóng, cho màn chờ và màn chào
- Các file `logo/C-*` là bản của bước chọn hướng (và đã bị dựng lại với quả tạ mới trên nền kem cũ); dùng `logo/final/` thay cho chúng.
- Dựng lại: `logo/_work/final.py build` (sau khi chạy `logo_scene.py -- C --size 1600 --samples 192 --tag _n --noshadow`)
