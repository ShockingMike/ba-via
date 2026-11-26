# 11 — Danh mục tủ đồ MVP: 12 món đồ bỏ quên

**BẢN NHÁP, CHƯA CHỐT.** Viết ngày 2026-11-26 cho quyết định D3 (đồ bỏ quên, 12 món, giữ luật mảnh và mốc streak 4/12/26 tuần). Mọi tên, chuyện, bậc và thứ tự dưới đây là đề xuất để chủ dự án chọn; chưa món mới nào được dựng hay thử trên rig.

Đọc cùng: [06-avatar-wardrobe.md](06-avatar-wardrobe.md) (luật mảnh, bậc, mốc), [07-cast-pitches.md](07-cast-pitches.md) mục C (thế giới), `blender/via/wardrobe.py` và `blender/via/README.md` (cách dựng và điểm neo).

## 0. Tóm tắt

| # | Món | Ô | Bậc | Cách lấy |
|---|---|---|---|---|
| 1 | Băng cổ tay vải | cổ tay | khởi đầu | Có sẵn sau màn 0.15 |
| 2 | Tất lệch đôi | ống chân | khởi đầu | Có sẵn sau màn 0.15 |
| 3 | Băng đô len 1996 | đầu | thường | N mảnh, món đầu tiên (tuần 1) |
| 4 | Dép tổ ong | bàn chân | thường | N mảnh |
| 5 | Mũ lưỡi trai hở chóp | đầu | thường | N mảnh |
| 6 | Cốc trà đá mượn quán | cầm tay | thường | N mảnh |
| 7 | Túi bao tử cô trông xe | bụng | thường | N mảnh |
| 8 | Chìa khoá tủ số 17 | cổ | thường | N mảnh |
| 9 | Tạ lon sữa tự đúc | cầm tay | hiếm | Kỷ lục đầu tiên (một lần) |
| 10 | Kính bơi lạc bể | đầu | hiếm · mốc streak | Streak 4 tuần |
| 11 | Huy chương "Tiến bộ nhất" 2009 | cổ | huyền thoại · mốc streak | Streak 12 tuần |
| 12 | Vương miện giấy sinh nhật | đầu | huyền thoại · mốc streak | Streak 26 tuần |

Đếm: 2 khởi đầu, 6 thường, 1 hiếm sự kiện, 3 mốc streak. 7 ô: đầu (4), cổ (2), cầm tay (2), cổ tay, ống chân, bàn chân, bụng (mỗi ô 1).

Ba điều cần chủ dự án biết trước khi chọn (chi tiết ở mục 8):
1. **Số mảnh không ghi theo món.** Theo tài liệu 06, một món thường cần N mảnh, N là lời hứa tuần của từng người. "3 mảnh" của Băng đô len trên màn 0.15 là vì bản mẫu có N = 3. Món mốc và món kỷ lục không cần mảnh.
2. **6 món thường hết ở tuần 6.** Sau đó lộ trình tuần chỉ còn bản màu (luật 6, tài liệu 06) cho tới khi có đợt món mới.
3. **Món "cả hội cùng nhận"** (màn 1.6a, 3.1) không có trong 12 món; đề xuất nằm ở mục dự bị.

## 1. Ô trang bị cho ba bạn đồng hành

Tài liệu 06 chia ô theo quần áo người. Ba bạn đồng hành không có cổ, eo hay thân tách khỏi mặt, nên bản này dùng 7 ô riêng. Mỗi ô mặc một món; các ô khác nhau mặc cùng lúc được.

| Ô | Khăn | Bình | Găng | Đã có neo trong `wardrobe.py`? |
|---|---|---|---|---|
| **đầu** | vòng quanh khăn trùm, z 0.616, trên đường lông mày (0.583) | vòng quanh **nắp**, đi theo nắp khi nắp bật | **thay** băng trán cam có sẵn, z 0.583 | Có (`head`) |
| **cổ** | vòng kín quanh thân ngay dưới miệng, z ≈ 0.35, nằm dưới lớp khăn trùm (khăn trùm lên thì chỉ thấy đoạn phía trước); mặt dây rơi xuống z ≈ 0.29 | vòng quanh ống **dưới miệng**, z ≈ 0.42 (miệng ở 0.452, không được vòng ở vành nắp vì sẽ cắt ngang lông mày và mắt); mặt dây ở z ≈ 0.38, trên vạch nước 0.345. Phải né gốc tay (vai ở 0.425) và huy hiệu vàng trên ngực | chỗ thắt giữa găng và thân, z ≈ 0.295; mặt dây nằm trên ngực, z ≈ 0.22 | **Chưa** (`neck`) |
| **bụng** | vòng quanh thân z ≈ 0.24, giữa sọc kem và tua rua, đeo ngoài khăn trùm | vòng quanh ống z ≈ 0.27, trên phần nước | vòng quanh thân nhỏ z ≈ 0.215 (đúng chỗ quai găng ở bản mặt "orig": rx 0.126, ry 0.104) | **Chưa** (`waist`) |
| **cổ tay** | `forearm.L/R`, r 0.033 | r 0.022 | r 0.042 | Có |
| **cầm tay** | dính vào lòng bàn tay phải (`hand.R`), không dựng dáng nắm | như Khăn, tay nhỏ hơn (r 0.037) | dính vào nắm tay phải (r 0.054) | **Chưa** (`hand`) |
| **ống chân** | `shin.L/R`, r 0.035 | r 0.025 | r 0.040 | Có (`leg`) |
| **bàn chân** | `foot.L/R`, khuôn `SOLE`, bàn chân elip 0.054 × 0.080 | 0.046 × 0.072 | 0.058 × 0.086 | **Chưa** (`foot`) |

Kiểm tra mặc chồng (đã rà trên giấy, chưa rà trên rig):

| Cặp | Kết quả |
|---|---|
| ống chân + bàn chân | Chồng được: tất nằm trên `shin`, dép nằm trên `foot`. Tất đi với dép tổ ong là chủ ý. |
| cổ tay + cầm tay | Chồng được: băng nằm trên `forearm`, đồ cầm nằm trên `hand`. |
| cổ + bụng | Chồng được trên cả ba (cách nhau ít nhất 7 cm). Trên Găng hai vòng gần nhau nhất: mặt dây (z 0.22) đè lên túi bao tử (z 0.215), cần lệch mặt dây sang một bên hoặc để túi lệch hông. |
| đầu + cổ | Chồng được trên cả ba: vòng cổ nằm dưới miệng, cách ô đầu cả khuôn mặt. |
| đầu + đầu | Không. Kính bơi đẩy lên trán nằm đúng chỗ băng đô, nên kính bơi thuộc ô đầu, không có ô "mặt". |
| cổ + áo choàng của Khăn | Rủi ro: ở dáng áo choàng, nút buộc áo choàng nằm ở z 0.328 phía trước, trùng chỗ mặt dây. Cần lệch mặt dây sang x ≈ +0.05. |

Không có ô **lưng** trong 12 món: avatar nhìn từ phía trước nên đồ sau lưng gần như không thấy, và lưng Khăn đã có áo choàng với nhãn giặt. Không có ô **mặt**: kính kéo xuống mắt làm mất biểu cảm (tài liệu 06, mục 6.3).

Luật chung giữ từ tài liệu 06: không món nào che lông mày hay mắt; khăn trùm của Khăn vẫn kéo sụp và hất ra được; nắp Bình vẫn bật; năm ngón của Găng vẫn diễn đủ 7 dáng (`open`, `fist`, `thumb`, `limp`, `five`, `point`, `lazy`). Vì vậy **không món nào gắn lên ngón của Găng** và không có mũ kín chóp.

## 2. Luật mảnh, bậc và mốc (theo tài liệu 06, không đổi)

- Mỗi buổi đạt cho 1 mảnh, tối đa 1 mảnh mỗi ngày. Một món thường cần **N mảnh** (N = lời hứa tuần), tối đa 1 món mỗi tuần. Buổi dừng giữa chừng tính buổi nhưng không cho mảnh; buổi đi bộ không tính.
- Bậc nói cách lấy, không phải xác suất: **thường** = lộ trình tuần; **hiếm** = mốc và sự kiện; **huyền thoại** = mốc dài.
- Ba mốc streak: **4 tuần → Kính bơi lạc bể · 12 tuần → Huy chương "Tiến bộ nhất" 2009 · 26 tuần → Vương miện giấy sinh nhật.** Nhận ngay khi chạm mốc, không cần mảnh, và nhận thêm ngoài món thường của tuần đó.
- Kỷ lục đầu tiên → Tạ lon sữa tự đúc, một lần duy nhất. Kỷ lục về sau chỉ có lời khen.
- Mốc 4 tuần khớp luật của thế giới: "món nào quá ba mươi ngày không ai nhận thì thuộc về bạn đồng hành".

## 3. Mười hai món

Ghi chú chung cho người dựng (EN): every item is a builder `def item(L, A, tag)` in `wardrobe.py`, parts via `L.mk(..., temp=True)`, rings sunk 45 %, cuffs 9–12 mm proud. Each item carries a cream or ink edge so it reads on all six body colours and next to Găng's orange band. Colours marked *new* must be added to `COL`.

### 1. Băng cổ tay vải — cổ tay · khởi đầu

- **Chuyện:** Của một bác đánh cầu lông sân bên, sang xin nước rồi để quên. Bác vẫn sang xin nước, chưa lần nào hỏi lại.
- **Khăn / Bình / Găng:** đã dựng và đã thử trên cả ba; đai nằm ở 6–62 % đoạn cổ tay → khuỷu.
- **Build (EN):** exists as `cotay`: yellow terry cuff on both forearms, cream centre line. Do not redesign.

### 2. Tất lệch đôi — ống chân · khởi đầu

- **Chuyện:** Hai chiếc, hai chủ, hai mùa khác nhau. Trong hộp chưa bao giờ có đôi nào đủ cả hai.
- **Khăn / Bình / Găng:** đã dựng; chân rất ngắn nên tất phủ gần hết ống chân, đó là chủ ý.
- **Build (EN):** exists as `tat`: left sock cream with two red hoops, right sock plain navy. Do not redesign.

### 3. Băng đô len 1996 — đầu · thường · món đầu tiên

- **Chuyện:** Ai đó được mẹ đan cho năm 1996, năm ấy thêu ở mặt trong. Đeo đi tập một hôm rồi để lại trên móc. (Bản v2 đang dùng câu "Chủ cũ tập đúng một buổi"; nên thay vì nghe như chê người bỏ tập.)
- **Khăn:** quanh khăn trùm. Giới hạn đã biết: ở dáng áo choàng, cuộn khăn sau gáy đâm vào băng đô từ phía sau.
- **Bình:** quanh nắp, nghiêng theo nắp.
- **Găng:** thay băng trán cam có sẵn; cởi ra thì băng cam trở lại.
- **Build (EN):** exists as `bando`: three knitted ribs, orange / cream / orange. Do not redesign.

### 4. Dép tổ ong — bàn chân · thường

- **Chuyện:** Ai đó đi dép đến, thay giày tập, rồi đi giày về. Đôi dép đứng chờ ở cửa từ hôm ấy.
- **Khăn:** đế rộng hơn bàn chân kem mỗi bên 6 mm; quai phủ nửa trước, gót hở.
- **Bình:** cùng công thức theo khuôn `SOLE` nhỏ hơn; bàn chân màu đậm của Bình lộ ở gót.
- **Găng:** bàn chân to nhất, quai phải rộng hơn 86 mm chiều dài chân một chút để không thành "sơn lên chân".
- **Mặc với tất:** được, và nên có trong ảnh giới thiệu (tất lệch đôi + dép tổ ong).
- **Build (EN):** new anchor `foot` (bone `foot.L/R`, sole from `SOLE`). Sole = flat slab 12 mm thick, 6 mm wider than the foot. The foot already touches the floor at z = 0, so either wrap the sole up around the foot's lower edge (preferred, no height change) or lift the whole character 12 mm and re-run `ground()`; do not let the slab go through the floor. Strap = half-tube over the front 55 % of the foot. Honeycomb = 2 rows × 3 ink dots as flat decals on the strap. Colours: `it_yellow` body, `it_ink` dots and sole edge. Yellow is needed because Khăn's feet are cream; check it on the `amber` colourway.

### 5. Mũ lưỡi trai hở chóp — đầu · thường

- **Chuyện:** Của một cô đi bộ quanh hồ mỗi sáng, ghé vào xin cốc nước rồi để quên trên quầy. Nhãn trên mũ bong từ lâu, không ai nhớ nó từng in gì.
- **Vì sao hở chóp:** dấu nhận diện của cả ba đều nằm trên đầu. Mũ chỉ gồm đai và lưỡi trai thì cùng một công thức vừa cả ba, không cần ba thiết kế riêng.
- **Khăn:** đai quanh khăn trùm, lưỡi trai chìa ra trước ở z ≈ 0.63, hất lên 15°; đỉnh khăn trùm lộ ra làm "chóp".
- **Bình:** đai quanh nắp, lưỡi trai đi theo nắp; chính cái nắp là chóp mũ. Vòi uống và quai xách trên nắp không bị che.
- **Găng:** đai thay băng trán cam, năm ngón chui qua chỗ hở chóp. Lông mày vẫn bị chặn dưới đai như cũ.
- **Build (EN):** `_ring()` band (tube 0.016) + brim = flattened half-ellipsoid, 70 mm deep, bound to the same bone and transform as the band, tilted up 15° so it never crosses the brow line from the avatar camera (elevation 5°). Colours: `it_cream` band, `it_navy` brim, `it_red` piping on the brim edge. No logo, no text.

### 6. Cốc trà đá mượn quán — cầm tay · thường

- **Chuyện:** Cốc của quán trà đá đầu ngõ. Ai đó mang vào uống dở giữa hai hiệp; bà chủ quán vẫn tính là "cho mượn".
- **Khăn:** dính vào lòng bàn tay phải, cốc cao bằng khoảng 1,6 lần bàn tay.
- **Bình:** cùng cỡ cốc; trên Bình trông to hơn vì tay nhỏ, giữ nguyên vì buồn cười đúng kiểu (bình nước cầm cốc nước).
- **Găng:** dính vào mặt ngoài nắm tay phải, lệch lên trên để nắm tay không nuốt mất cốc.
- **Build (EN):** new anchor `hand` (bone `hand.R`, palm point + radius per species). Glass = slightly tapered cylinder, r 0.030, h 0.075. Felt cannot be transparent, so: tea-coloured body, cream rim ring, two cream cubes sitting proud of the rim. Colours: `it_tea` *new* (`#C8862A`), `it_cream`. Check against the `amber` and `orange` colourways; the cream rim is what separates it.

### 7. Túi bao tử cô trông xe — bụng · thường

- **Chuyện:** Của cô trông xe ngoài cổng. Bên trong không có tiền, chỉ có ba vé gửi xe quá hạn và một viên kẹo bạc hà.
- **Khăn:** dây đeo ngoài khăn trùm ở z ≈ 0.24, túi nằm trước bụng, giữa sọc kem và tua rua. Trông như khăn tắm thắt đai, đó là chủ ý.
- **Bình:** dây quanh ống ở z ≈ 0.27; túi **lệch về góc trước bên trái** (khoảng 45°) để không che hình tròn in trên phần nước và không chạm bàn tay buông (z 0.20–0.275 ở bên hông).
- **Găng:** dây quanh thân nhỏ; túi to gần bằng thân nên đeo lệch về góc trước, không đeo chính giữa và không ra hẳn bên hông (vướng nắm tay).
- **Build (EN):** new anchor `waist` (bone `chest` on all three; cross-section per species, Khăn needs the same hood / cape padding as `head`). Strap = `_ring()` tube 0.010. Pouch = half-ellipsoid 0.075 × 0.035 × 0.045 on the strap, with a cream zip line as a flat decal. Colours: `it_red` pouch, `it_ink` strap, `it_cream` zip.

### 8. Chìa khoá tủ số 17 — cổ · thường

- **Chuyện:** Tủ số 17 vẫn khoá. Không ai nhớ trong đó có gì, và chưa ai dám mở.
- **Khăn:** dây lò xo vòng quanh thân dưới miệng, nằm dưới khăn trùm nên chỉ thấy đoạn phía trước; thẻ số rơi xuống ngay trên sọc kem.
- **Bình:** dây vòng quanh ống ngay dưới miệng, thẻ số nằm giữa miệng và vạch nước, lệch khỏi huy hiệu vàng.
- **Găng:** dây nằm ở chỗ thắt giữa găng và thân (chỗ duy nhất trong ba bạn có cổ thật), thẻ số nằm trên ngực.
- **Build (EN):** new anchor `neck` (ring cross-section + pendant point per species; values in section 1). Cord = thin ring, tube 0.007, with shallow bumps to suggest the coiled spring. Tag = flat yellow disc r 0.028 with "17" as an ink decal; key = small cream bar with two teeth beside the tag. The disc is what reads at avatar size; the key is detail. Colours: `it_red` cord, `it_yellow` tag, `it_cream` key. Story hook: locker 17 can be opened in a later season.

### 9. Tạ lon sữa tự đúc — cầm tay · hiếm · kỷ lục đầu tiên

- **Chuyện:** Hai lon sữa đặc đổ xi măng, xuyên một đoạn ống nước. Quả tạ đầu tiên của ai đó, tự làm ở nhà, mang đến khoe rồi quên mang về.
- **Vì sao hợp:** đúng khẩu hiệu "Ai cũng bắt đầu từ quả tạ nhỏ", và hợp mốc kỷ lục đầu tiên mà không nói gì về mức tạ của chủ.
- **Khăn / Bình:** cán tạ dính ngang lòng bàn tay phải, hai lon ló ra hai bên bàn tay.
- **Găng:** cán xuyên qua nắm tay phải. Găng là bạn duy nhất trông như đang nắm thật.
- **Build (EN):** uses anchor `hand`. Bar = cylinder r 0.010, l 0.13. Cans = two cylinders r 0.030, h 0.040; cream side with one red hoop (a label that has been peeled, no brand), grey cement end caps. Colours: `it_cream`, `it_red`, `it_grey` *new* (`#9AA0A6`). Same slot as the iced-tea glass, so only one is held at a time.

### 10. Kính bơi lạc bể — đầu · hiếm · streak 4 tuần

- **Chuyện:** Phòng tập không có bể bơi. Cả phòng đã bàn ba lần mà chưa ai giải thích được.
- **Khăn:** dây quanh khăn trùm, hai mắt kính đẩy lên trán ở z ≈ 0.63, mép dưới vẫn trên lông mày.
- **Bình:** dây quanh nắp, mắt kính nằm ở mặt trước nắp, nghiêng theo nắp.
- **Găng:** dây kính thay băng trán cam; mắt kính nằm phía trên dây, tựa vào gốc ngón trỏ và ngón giữa.
- **Không bao giờ kéo xuống mắt** ở dáng thường. Có thể kéo xuống ở một dáng ăn mừng riêng, làm sau.
- **Build (EN):** strap = `_ring()` tube 0.010. Lenses = two flattened ellipsoids 0.032 × 0.012 × 0.026, 0.07 apart, each with a cream rim ring, plus a short ink nose bridge. Lenses sit ABOVE the strap, not on it; the bottom edge of each lens must clear the top of the brow (`brow_z` + half `brow_th`) by at least 5 mm on every species. Colours: `it_ink` strap, `it_sky` *new* (`#6EC6FF`) lenses, `it_cream` rims. Check `it_sky` on the `blue` colourway; the cream rims carry it.

### 11. Huy chương "Tiến bộ nhất" 2009 — cổ · huyền thoại · streak 12 tuần

- **Chuyện:** Giải "Tiến bộ nhất" của hội thao phường năm 2009. Người nhận gửi ở quầy, dặn "giữ hộ, mai lấy".
- **Khăn:** cùng điểm neo với chìa khoá: ruy băng vòng quanh thân dưới miệng, nằm dưới khăn trùm; đoạn phía trước võng thành chữ V, huy chương nằm ngay trên sọc kem.
- **Bình:** ruy băng vòng quanh ống dưới miệng, huy chương nằm giữa miệng và vạch nước; huy chương to nên được phép che huy hiệu vàng.
- **Găng:** ruy băng quanh chỗ thắt cổ, huy chương to gần bằng nửa ngực.
- **Build (EN):** uses anchor `neck`. Ribbon = flat band 0.018 wide following the neck ring, front section drawn as a V down to the pendant point. Medal = disc r 0.036, 8 mm thick, with a raised cream star decal. Colours: `it_red` ribbon, `it_yellow` medal, `it_cream` star. Larger than the locker tag on purpose: this is a 12-week item and must read in the avatar crop.

### 12. Vương miện giấy sinh nhật — đầu · huyền thoại · streak 26 tuần

- **Chuyện:** Sinh nhật phòng tập năm nọ: bánh kem hết trong năm phút, vương miện giấy thì còn nguyên.
- **Khăn:** vòng quanh khăn trùm, răng cưa cao tới đỉnh đầu.
- **Bình:** vòng quanh nắp như giấy bọc bánh, nghiêng theo nắp; răng cưa không cao quá mặt nắp để vòi uống vẫn thấy.
- **Găng:** đai thay băng trán cam, răng cưa thấp (≤ 35 mm) đứng trước gốc ngón. **Năm ngón của Găng chính là năm chóp vương miện.**
- **Build (EN):** band = `_ring()` in cream (tube 0.014) at the head anchor; above it 7–9 flat triangular teeth, 4 mm thick, following the same cross-section and transform; three red felt dots on the front teeth as "gems drawn with a marker". Colours: `it_yellow` teeth, `it_cream` band, `it_red` dots. The cream band keeps it apart from the `amber` body. Teeth are bound to the head anchor, never to Găng's fingers, so all crest poses still work.

## 4. Ba mốc streak: đề xuất và hai phương án khác

| Mốc | **A (đề xuất)** | B | C |
|---|---|---|---|
| 4 tuần | Kính bơi lạc bể (đầu) | Kính bơi lạc bể (đầu) | Chìa khoá tủ số 17 (cổ) |
| 12 tuần | Huy chương "Tiến bộ nhất" 2009 (cổ) | Vương miện giấy sinh nhật (đầu) | Huy chương "Tiến bộ nhất" 2009 (cổ) |
| 26 tuần | Vương miện giấy sinh nhật (đầu) | Tạ lon sữa tự đúc (cầm tay) | Vương miện giấy sinh nhật (đầu) |
| Kỷ lục đầu tiên | Tạ lon sữa tự đúc | Huy chương "Tiến bộ nhất" 2009 | Tạ lon sữa tự đúc |

- **A:** lên dần về độ "oách": kính bơi buồn cười, huy chương đáng nể, vương miện là nhất. Hai món ở ô đầu (4 và 26 tuần) chắc chắn thấy được trong ảnh avatar tròn trên bảng hội. Điểm yếu: theo `blender/out/via/avatars.png`, khung avatar hiện cắt ở khoảng sọc kem của Khăn và huy hiệu của Bình, nên huy chương 12 tuần nằm sát mép dưới trên hai bạn này (trên Găng thì thấy rõ). Muốn huy chương lọt khung thì phải nới khung avatar xuống một chút.
- **B:** mốc dài nhất là quả tạ nhỏ, khớp khẩu hiệu của app. Điểm yếu: đồ cầm tay không lọt vào ảnh avatar cắt đầu, nên cả hội khó thấy mốc 26 tuần.
- **C:** mốc 4 tuần là chiếc chìa khoá (nhẹ nhàng hơn kính bơi); kính bơi xuống bậc thường. Điểm yếu: thẻ số nhỏ, kém nổi cho một khoảnh khắc ăn mừng.

## 5. Thứ tự mở trong những tuần đầu

Giả định tuần nào cũng đạt lời hứa. Chạm kỷ lục đầu tiên thường rơi vào tuần 2–5.

| Lúc | Nhận gì | Tổng món |
|---|---|---|
| Xong onboarding (0.15) | Băng cổ tay vải + Tất lệch đôi; Băng đô len 1996 chờ trong hộp, thanh 0/N | 2 |
| Tuần 1 | Băng đô len 1996 (cố định, không chọn) | 3 |
| Tuần 2 | Chọn 1 trong 3: **Dép tổ ong · Mũ lưỡi trai hở chóp · Cốc trà đá mượn quán** | 4 |
| Tuần 3 | Chọn 1 trong 3: hai món còn lại của tuần 2 + **Túi bao tử cô trông xe** | 5 |
| Tuần 4 | Chọn 1 trong 3: hai món còn lại + **Chìa khoá tủ số 17**. Cùng tuần: **streak 4 tuần → Kính bơi lạc bể** | 7 |
| Tuần 5 | Chọn 1 trong 2 món thường còn lại | 8 |
| Tuần 6 | Món thường cuối cùng | 9 |
| Kỷ lục đầu tiên | Tạ lon sữa tự đúc | 10 |
| Tuần 7–11 | Bản màu của món thường đã có (xem câu hỏi 2, mục 8) | 10 |
| Tuần 12 | Huy chương "Tiến bộ nhất" 2009 | 11 |
| Tuần 26 | Vương miện giấy sinh nhật | 12 |

Lý do xếp như vậy: tuần 2 bày ba ô khác nhau (bàn chân, đầu, cầm tay) để lựa chọn đầu tiên thật sự khác nhau, và để sau tuần 2 người dùng đã có đồ ở ít nhất 4 ô. Túi bao tử và chìa khoá vào sau vì cần hai điểm neo mới (`waist`, `neck`), dựng sau cũng không chặn tuần đầu.

Thứ tự dựng đề xuất cho người dựng: dép tổ ong → mũ lưỡi trai hở chóp → kính bơi → vương miện (bốn món dùng neo `head` có sẵn hoặc neo `foot` đơn giản) → cốc trà đá, tạ lon sữa (neo `hand`) → chìa khoá, huy chương (neo `neck`) → túi bao tử (neo `waist`).

## 6. Bốn bộ phối thử (để kiểm tra 12 món có ra dáng không)

| Bộ | Gồm |
|---|---|
| Ra quán | Mũ lưỡi trai hở chóp + Cốc trà đá + Tất lệch đôi + Dép tổ ong |
| Trông xe | Túi bao tử + Chìa khoá tủ số 17 + Dép tổ ong |
| Hội thao 2009 | Băng đô len 1996 + Huy chương + Băng cổ tay vải + Tất lệch đôi |
| Sinh nhật phòng tập | Vương miện giấy + Huy chương + Tạ lon sữa |

Cái giá của việc có 4 món ở ô đầu: Vương miện giấy và Kính bơi, hai món mốc cùng ô, không mặc chung được. Nếu chủ dự án thấy đó là vấn đề, đổi mốc theo phương án B hoặc C.

## 7. Bốn món dự bị để đổi

| Món | Ô | Hợp với bậc | Chuyện | Lưu ý |
|---|---|---|---|---|
| **Quạt nhựa phòng không điều hoà** | cầm tay | thường | Phòng có một cái quạt trần và mười hai người. Chiếc quạt này từng là của người đứng xa quạt trần nhất. | Dễ dựng nhất trong các món dự bị: một đĩa dẹt và một cán. Bóng dáng to, đọc tốt hơn cốc trà đá. Mặt quạt để trơn, không in quảng cáo. |
| **Băng tay "Hội mình"** | bắp tay (ô mới, trên `upper_arm`) | hiếm · cả hội cùng nhận | Băng đội trưởng của một đội bóng phủi tan từ lâu, cả đội để lại một lúc. | Lấp chỗ trống "món cả hội cùng nhận khi xong thử thách hội". Mặc chung được với băng cổ tay. Tay Bình rất mảnh (r 0.025), cần thử. |
| **Mũ bảo hiểm nửa đầu** | đầu | thường | Ai đó về bằng xe của bạn, mũ ở lại. Sáng hôm sau đi làm mới nhớ. | Rất Việt Nam, nhưng là mũ kín chóp: Khăn và Bình đội được, Găng thì không (năm ngón). Găng phải treo mũ ở khuỷu tay, tức là ba thiết kế khác nhau. |
| **Áo mưa giấy** | thân (ô mới) | hiếm · mùa mưa | Trời tạnh trước khi tập xong, nên không ai nhớ mình có mang áo mưa. | Đã có tên trong bản v2 ("Mùa mưa mới có"). Khó nhất: nỉ không trong suốt được, áo trùm che mất khăn trùm, nắp và mào ngón, nên cần ba thiết kế riêng. Nên để sau MVP. |

Đã cân nhắc và loại: chiếc găng tay phải (là nút thắt giữa mùa truyện của Găng, không làm món đồ), khăn mặt in hoa (trên Khăn thành khăn đội khăn), bình nước (trên Bình thành bình cầm bình; cốc trà đá đã giữ được trò đùa này ở mức nhẹ), đai lưng tập tạ và găng hở ngón của tài liệu 06 (đồ của người tập giỏi, không phải đồ bỏ quên vui).

## 8. Đã chốt 2026-11-26: tất cả theo đề xuất, câu 7 là N mảnh

| # | Câu hỏi | Đề xuất |
|---|---|---|
| 1 | Chọn bộ ba mốc streak: A, B hay C (mục 4)? | A |
| 2 | 6 món thường hết ở tuần 6. Từ tuần 7 bày bản màu (luật có sẵn), hay thêm món thường vào đợt đầu? | Giữ 12 món, tuần 7 trở đi là bản màu; đợt sau thêm 4–5 món (ưu tiên quạt nhựa) |
| 3 | Món "cả hội cùng nhận" có nằm trong 12 món không? Nếu có thì bỏ món nào? | Để ngoài 12 món; dùng Băng tay "Hội mình" khi làm thử thách hội |
| 4 | Giữ tên bậc "huyền thoại" cho mốc 12 và 26 tuần, hay gọi chung là "mốc streak"? | Giữ ba bậc thường / hiếm / huyền thoại như tài liệu 06 |
| 5 | Kỷ lục đầu tiên có gắn với một món không (tài liệu 08 đang ghi là có)? | Có: Tạ lon sữa tự đúc |
| 6 | Câu chuyện Băng đô len 1996 trong bản v2 ("Chủ cũ tập đúng một buổi") có đổi không? | Đổi sang câu ở mục 3, để không món nào nhắc chuyện bỏ tập |
| 7 | Yêu cầu ghi "Băng đô len 1996 (3 mảnh)", tài liệu 06 ghi N mảnh theo lời hứa tuần. Theo bên nào? | Theo tài liệu 06: N mảnh; 3 chỉ là số của bản mẫu |

## 9. Điểm yếu của bản nháp này

- Mọi con số neo mới (`neck`, `waist`, `hand`, `foot`) đọc từ mã `v_khan.py`, `v_binh.py`, `v_gang.py`, chưa thử trên rig. Vị trí cổ của Khăn (z 0.35, sát dưới miệng ở 0.398) là chỗ dễ sai nhất.
- Chưa món mới nào được render, nên "đọc được ở cỡ avatar" mới là phán đoán. Thẻ số 17 và cốc trà đá là hai món có nguy cơ quá nhỏ.
- 4 trên 12 món ở ô đầu. Ô đầu dễ thấy nhất, nhưng làm giảm số cách phối.
- Ba màu mới (`it_tea`, `it_sky`, `it_grey`) chưa qua bảng kiểm màu `checker.py`.
- Các câu chuyện là bản viết đầu, chưa ai đọc thử thành tiếng.
