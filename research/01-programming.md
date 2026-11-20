# 01 — Programming: quy tắc lập trình tập kháng lực dựa trên bằng chứng

> Mục đích: cung cấp số liệu và luật cụ thể cho **rules engine** của app gym cá nhân (2 người dùng: chồng và vợ, mức beginner đến early intermediate, phòng gym cơ bản, thiết bị chưa chắc chắn).
> Ngày tra cứu: 2026-11-19. Mọi con số đều kèm mã nguồn `[R#]`, URL nằm ở mục **References** cuối file.

## 0. Cách đọc tài liệu này

| Nhãn | Ý nghĩa |
|---|---|
| **[S]** | *Sourced*: con số lấy trực tiếp từ nguồn đã đọc (abstract PubMed, full text, hoặc trang chương trình gốc). |
| **[D]** | *Design default*: giá trị mặc định do tôi đề xuất để code được, suy ra từ các nguồn [S] nhưng **không có nghiên cứu nào kiểm chứng đúng con số đó**. Nên để dạng config chỉnh được. |
| **[UNVERIFIED]** | Không xác minh được từ nguồn gốc (trang chặn truy cập, chỉ thấy qua bản tóm tắt bên thứ ba). Không nên coi là sự thật. |

Lưu ý quan trọng về chất lượng bằng chứng:

- Phần lớn nghiên cứu làm trên **nam trẻ tuổi**, thời gian 6–12 tuần. Ví dụ meta-regression của Pelland có 79.1% nam, 20.9% nữ [R7].
- **ACSM 2026** (tổng quan 137 systematic review, >30,000 người) thay thế ACSM 2009 ở những chỗ mâu thuẫn [R6]. ACSM 2009 chỉ còn dùng cho định nghĩa trình độ và luật tăng tải 2–10% [R5].
- Các chương trình beginner (GZCLP, BBR, StrongLifts, Greyskull, Starting Strength) là **kinh nghiệm huấn luyện**, không phải thử nghiệm lâm sàng. Chúng cho ta thuật toán rõ ràng, không cho ta bằng chứng rằng thuật toán đó là tối ưu.
- Volume landmarks của RP (MV/MEV/MAV/MRV) là **heuristic huấn luyện cho người intermediate** (trang biceps ghi rõ "3–7 năm tập"), không phải giá trị cho beginner [R15].
- Kết luận tổng quát nhất của ACSM 2026: rất ít biến số thật sự thay đổi kết quả. Người chưa tập sẽ tiến bộ với nhiều kiểu chương trình, miễn là có **progression và tuân thủ** [R6]. Vì vậy app nên ưu tiên: đơn giản, đều đặn, tăng tiến rõ ràng.

Định nghĩa trình độ dùng trong file (theo ACSM 2009 [R5]):

| Level | Định nghĩa [S] | Gợi ý map vào profile [D] |
|---|---|---|
| `novice` | Chưa tập kháng lực, hoặc nghỉ tập nhiều năm | < 6 tháng tập đều |
| `intermediate` | Khoảng 6 tháng tập kháng lực đều đặn | 6 tháng – 2 năm |
| `advanced` | Nhiều năm kinh nghiệm | Ngoài phạm vi app này |

---

## 1. Volume: số set mỗi tuần cho mỗi nhóm cơ, và tần suất

### 1.1 Bằng chứng

| Phát hiện | Con số | Nguồn |
|---|---|---|
| Quan hệ liều–đáp ứng giữa set/tuần và tăng cơ | Mỗi set thêm: effect size +0.023, tương ứng +0.37% tăng cơ. Nhóm volume cao hơn so với thấp hơn: chênh 3.9%. Chia 3 mức <5, 5–9, 10+ set/tuần: chỉ là xu hướng (P = 0.074) | [R1] |
| Ngưỡng hypertrophy theo ACSM 2026 | Hypertrophy tốt hơn với **≥10 set/nhóm cơ/tuần** (có liều–đáp ứng) | [R6] |
| Lợi ích giảm dần | Meta-regression: lợi ích chững lại sau khoảng **2–3 set/bài cho strength** và khoảng **18–20 set/tuần cho hypertrophy**. ACSM khuyên **ít nhất 2 set mỗi bài** | [R6], dẫn lại [R7] |
| Hình dạng đường cong | Xác suất hậu nghiệm 100% rằng volume cao hơn cho kết quả tốt hơn ở cả hypertrophy và strength; lợi ích giảm dần, ở strength giảm dần rõ hơn nhiều | [R7] |
| Cách đếm set gián tiếp | Set gián tiếp (ví dụ bench press đối với triceps) nên tính **0.5 set** ("fractional") | [R7] |
| Liều tối thiểu khi ít thời gian | **Tối thiểu 4 set/nhóm cơ/tuần**, tải 6–15RM | [R9] |
| Liều tối thiểu cho strength | 1 set 6–12 rep, 70–85% 1RM, 2–3 lần/tuần, gần failure, trong 8–12 tuần vẫn tăng 1RM (ở nam đã có kinh nghiệm; kết quả "dưới tối ưu nhưng có ý nghĩa") | [R10] |
| Volume và strength | Set/tuần cao so với thấp: ES chênh 0.18 (thấp 0.82, cao 1.01) | [R11] |
| Network meta-analysis | Mọi kiểu tập đều hơn không tập. Xếp hạng cao nhất cho strength: tải >80% 1RM, nhiều set, 3 buổi/tuần. Cao nhất cho hypertrophy: tải cao, nhiều set, 2 buổi/tuần | [R8] |
| Đếm set thế nào | Đếm số set tập gần failure là cách đo volume hợp lý khi rep nằm trong khoảng 6 đến 20+ | [R16] |
| Ở nữ | Volume và tần suất ảnh hưởng đến strength; không biến nào ảnh hưởng rõ đến hypertrophy | [R28] |

Volume landmarks của RP (set trực tiếp/tuần, người **intermediate**) [R15]:

| Nhóm cơ | MV | MEV | MAV | MRV | Tần suất/tuần |
|---|---|---|---|---|---|
| Ngực | 2–4 | 4–6 | 6–16 | 16–24 | 2–4 |
| Lưng | không đọc được (số nằm trong ảnh) [UNVERIFIED] | | | | 2–4 |
| Đùi trước (quads) | 2–4 | 4–6 | 6–14 | 14–18 | 2–5 |
| Đùi sau (hamstrings) | 0–2 | 2–4 | 2–8 | 8–14 | 2–3 |
| Mông (glutes) | 2–6 | 6–8 | 8–24 | 24–30 | 2–5 |
| Vai giữa (side delts) | 2–6 | 6–8 | 8–24 | 24–30 | 3–6 |
| Tay trước (biceps) | 6–8 | 8–10 | 14–20 | 20–26 | 3–6 |
| Tay sau (triceps) | 0–4 | 4–6 | 6–16 | 16–20 | 2–4 |
| Bắp chân (calves) | 2–4 | 4–6 | 6–16 | 16–24 | 3–6 |
| Bụng (abs) | 0–4 | 0–4 | 4–12 | 12–20 | 3–6 |

Ghi chú về bảng RP:

- Trang tổng quan của RP lại ghi MV "khoảng 6 set/tuần", khác với các trang từng nhóm cơ (2–4) [R14]. Nội bộ RP không nhất quán, nên chỉ dùng làm tham khảo.
- Trang biceps ghi "beginners can grow with 6–10 sets" [R15].
- RP nêu giới hạn khoảng **8–12 set mỗi nhóm cơ mỗi buổi** [R15].
- RP: glutes và triceps có thể cần 0 set trực tiếp nếu đã tập nhiều squat/hinge hoặc đẩy ngực [R15].

### 1.2 Tần suất: bằng chứng mâu thuẫn, và luật chọn

| Nguồn | Kết luận |
|---|---|
| Schoenfeld 2016 [R2] | Tập 2 lần/tuần cho mỗi nhóm cơ tốt hơn 1 lần (ES 0.49 so với 0.30) |
| Schoenfeld 2019 [R3] | Khi volume bằng nhau, tần suất **không** ảnh hưởng đáng kể đến hypertrophy; chọn theo sở thích |
| Stronger By Science [R13] | Phân tích riêng: tần suất cao hơn tăng cơ nhanh hơn khoảng 38% (0.58% so với 0.42%/tuần); ở người chưa tập 47% |
| Pelland 2026 [R7] | Tần suất: ảnh hưởng lên hypertrophy tương thích với "không đáng kể"; lên strength thì có, và giảm dần |
| Grgic 2018 [R12] | Strength ES 0.74 / 0.82 / 0.93 / 1.08 cho 1 / 2 / 3 / 4+ lần/tuần, nhưng mất ý nghĩa khi volume bằng nhau. Tần suất có ảnh hưởng rõ ở nữ (p = 0.030) |
| ACSM 2026 [R6] | Hypertrophy không khác giữa 1 ngày/tuần và >5 ngày/tuần khi volume bằng nhau. Strength tốt hơn với ≥2 buổi/tuần |

**Luật chọn [D]:** mỗi nhóm cơ chính được tập **≥2 lần/tuần** khi lịch cho phép. Lý do: không nguồn nào cho thấy 2 lần tệ hơn 1 lần, strength hưởng lợi từ tần suất, và chia volume ra nhiều buổi giúp mỗi buổi không vượt trần 8–12 set/nhóm cơ. Nếu người dùng chỉ tập được 1 lần/tuần cho một nhóm cơ thì vẫn chấp nhận, miễn đủ volume tuần.

### 1.3 Bảng luật volume để code [D]

Đếm theo **fractional set**: set trực tiếp = 1, set gián tiếp = 0.5 [R7].

| Level | Sàn (min) | Mục tiêu | Trần (max) | Trần mỗi buổi | Cơ sở |
|---|---|---|---|---|---|
| `novice` | 4 | 6–10 | 12 | 6 | Sàn 4 [R9]; "beginners grow with 6–10" [R15]; ≥10 là ngưỡng hypertrophy [R6] |
| `intermediate` | 6 | 10–16 | 20 | 8–10 | ≥10 [R6]; chững ở ~18–20 [R6][R7]; trần buổi 8–12 [R15] |
| `advanced` | 8 | 12–20 | 25+ | 10–12 | Ngoài phạm vi; MRV của RP [R15] |

Luật kèm theo:

- `volume.maintenance`: khi cần duy trì (bận, ốm nhẹ, đang giảm cân nặng), giữ khoảng 1/3 volume thường ngày vẫn bảo toàn được cơ ở người trẻ [R47]. Mặc định code: `max(4, round(target / 3))` set/tuần [D].
- Nhóm cơ nhỏ (biceps, triceps, vai trước) đã nhận 0.5 set từ mỗi set compound, nên ở `novice` có thể để 0–4 set trực tiếp/tuần [D, dựa trên R7 và R15].
- Mỗi bài tối thiểu 2 set [R6].
- Tăng volume: chỉ cộng thêm khi đã tập đều ≥4 tuần và không còn tiến bộ, mỗi lần +1 đến +2 set/nhóm cơ/tuần [D, theo cách RP tăng khoảng 2 set/tuần trong ví dụ R14].

---

## 2. Rep range, RIR/RPE, thời gian nghỉ theo mục tiêu

### 2.1 Bằng chứng

**Tải và rep**

- Tải nặng (>60% 1RM) cho strength 1RM tốt hơn; hypertrophy **tương đương** giữa tải nhẹ (≤60%) và nặng khi các set đều tập đến failure [R4].
- ACSM 2026: strength tốt hơn với **≥80% 1RM**; hypertrophy không phụ thuộc tải trong khoảng 30%–100% 1RM [R6].
- Tiết kiệm thời gian: dùng 6–15RM; có thể dùng 15–40 rep nếu tập đến failure [R9].
- Helms: chủ yếu dùng 6–12 rep ở RPE 8–10 (RIR 0–2) cho hypertrophy; 1–6RM cho strength; set ≥12 rep, nghỉ <2 phút, RPE 9–10 cho sức bền cơ [R19].
- RP: nặng 5–10, vừa 10–20, nhẹ 20–30 rep; khoảng 50% số set ở vùng 10–20 [R15].
- Cả vùng rep rộng đều cho kết quả; "repetition continuum" cổ điển không còn đúng hoàn toàn [R25].
- ACSM 2009 cho novice: tải 8–12RM [R5].

**Proximity to failure (RIR)**

- Tập đến failure thật **không hơn** tập không đến failure cho hypertrophy (ES 0.12, p = 0.343) [R17].
- Meta-regression: hypertrophy tăng khi dừng set gần failure hơn; strength gần như không đổi trong dải RIR rộng [R18].
- ACSM 2026: không cần tập đến failure; mục tiêu "near-failure" hoặc **2–3 RIR** là đủ; tập đến failure có thể không nên ở một số nhóm do form xấu làm tăng nguy cơ chấn thương [R6].
- Tập đến failure làm chậm hồi phục đến 24–48 giờ [R57].

**Thang RPE theo RIR** [R19][R20]

| RPE | RIR | Mô tả |
|---|---|---|
| 10 | 0 | Không thể thêm rep nào |
| 9 | 1 | Còn 1 rep |
| 8 | 2 | Còn 2 rep |
| 7 | 3 | Còn 3 rep |
| 5–6 | 4–6 | Còn 4–6 rep |
| 3–4 | — | Nhẹ |
| 1–2 | — | Gần như không tốn sức |

Cảnh báo cho beginner:

- Người tập thường **đoán thiếu khoảng 0.95 rep** so với khả năng thật (tức là thực tế còn nhiều rep hơn họ nghĩ). Đoán chính xác hơn khi gần failure, khi tải nặng (≤12 rep) và ở các set sau [R21].
- Helms: novice nên **ghi lại RIR để làm quen**, nhưng **không nên** dùng RIR làm cơ sở duy nhất để đặt tải hay tăng tiến [R19]. Hệ quả cho app: progression dựa trên **số rep đạt được**, RIR chỉ là dữ liệu phụ.

**Nghỉ giữa set**

- Nghỉ 3 phút cho strength và hypertrophy tốt hơn nghỉ 1 phút (nam có kinh nghiệm, 8 tuần, 3×8–12RM) [R22].
- Meta-analysis Bayes: lợi ích nhỏ khi nghỉ **>60 giây**; không thấy khác biệt đáng kể khi nghỉ **>90 giây** [R24].
- Người chưa tập: nghỉ ngắn hay dài đều được; người có kinh nghiệm có thể lợi hơn khi nghỉ dài [R23].
- Iversen: người chưa tập 1–2 phút, người đã tập ≥2 phút [R9].
- ACSM 2026: thời gian nghỉ giữa set **không** ảnh hưởng nhất quán đến strength [R6]. ACSM 2009 (cũ): 3–5 phút cho tải nặng, 1–2 phút cho hypertrophy [R5].
- RP: trung bình 1–3 phút; bench press có thể cần khoảng 3 phút, pec deck dưới 45 giây [R15].

### 2.2 Bảng luật theo mục tiêu để code

| Tham số | `fat_loss` | `hypertrophy` | `strength` | `general_health` / `recomp` |
|---|---|---|---|---|
| Rep bài compound chính | 6–10 [D] | 6–10 [D] | 3–6 (≥80% 1RM [R6]); novice dùng 5–8 [D] | 8–12 (ACSM novice 8–12RM [R5]) |
| Rep bài phụ / isolation | 10–15 [D] | 10–20 [R15] | 8–12 [D] | 10–15 [D] |
| RIR mục tiêu compound | 2–3 [R6] | 1–3 [R6][R19] | 2–3 (strength không cần sát failure [R18]) | 2–3 [R6] |
| RIR mục tiêu isolation | 1–2 [D] | 0–2 [R19] | 1–2 [D] | 2–3 [D] |
| Nghỉ compound | 2 phút [D] | 2–3 phút [R22][R15] | 3–5 phút [R5][R19] | 2 phút [R9] |
| Nghỉ isolation | 60–90 giây [R24] | 60–90 giây [R24] | 90–120 giây [D] | 60–90 giây [R9] |
| Set mỗi bài | 2–3 [R6] | 2–4 | 2–3 cho strength [R6] | 2–3 |
| Volume tuần | giữ mức `hypertrophy`, không tăng | theo mục 1.3 | sàn đến giữa dải | sàn đến giữa dải |

Giải thích các ô [D]: dải rep được chọn nằm trong vùng 6–15RM mà Iversen khuyến nghị [R9] và vùng 6–12 của Helms [R19]; compound dùng rep thấp hơn để tiết kiệm thời gian và dễ giữ form.

Ghi chú riêng cho **fat loss**:

- Thâm hụt năng lượng làm giảm tăng lean mass (ES −0.57) nhưng **không** giảm tăng strength (ES −0.31, không ý nghĩa). Thâm hụt khoảng **500 kcal/ngày** là mức triệt tiêu tăng lean mass [R74].
- Giảm chậm (0.7% cân nặng/tuần) giữ và tăng lean mass tốt hơn giảm nhanh (1.4%/tuần), ở vận động viên [R75].
- Luật [D]: khi `goal = fat_loss`, **không hạ tải**; giữ tải và rep, nếu cần thì bớt set (về mức sàn). Mục tiêu là giữ sức mạnh.

Ghi chú cho **novice ở mọi mục tiêu** [D]: 4–8 tuần đầu dùng chung một khuôn (8–12 rep, RIR 2–3, 2–3 set) để học kỹ thuật, sau đó mới tách theo mục tiêu. Cơ sở: ACSM 2009 khuyên novice dùng 8–12RM [R5], và ACSM 2026 nói người chưa tập tiến bộ với hầu hết mọi chương trình [R6].

### 2.3 Khác biệt cho nữ

| Phát hiện | Con số | Nguồn |
|---|---|---|
| Hypertrophy tương đối | Không khác giữa nam và nữ (ES 0.07, p = 0.31) | [R26] |
| Hypertrophy tuyệt đối và tương đối | Tuyệt đối hơi nghiêng về nam (SMD 0.19); tương đối giống nhau (0.69%) | [R27] |
| Strength thân trên (tương đối) | Nữ tăng nhiều hơn (ES −0.60, p = 0.002) | [R26] |
| Strength thân dưới | Không khác (p = 0.20) | [R26] |
| Tập kháng lực ở nữ | Hiệu quả lớn: strength thân trên g = 1.70, thân dưới g = 1.40, hypertrophy g = 0.52 | [R28] |
| Chu kỳ kinh nguyệt | Chưa đủ bằng chứng rằng pha chu kỳ ảnh hưởng đến hiệu suất hay thích nghi | [R29] |
| Khả năng chịu mỏi | SBS cho rằng nữ ít mỏi cấp tính hơn, làm được nhiều rep hơn ở cùng %1RM; không đưa con số cụ thể | [R30] |

**Luật cho app:**

1. Dùng **cùng** volume, rep range, RIR, split cho nam và nữ [R26][R27].
2. **Không code luật theo chu kỳ kinh nguyệt.** SBS gợi ý tập nhiều hơn ở pha follicular [R30] nhưng umbrella review kết luận bằng chứng chưa đủ [R29]. Check-in hằng ngày (mục 6) đã bắt được ngày mệt.
3. Khác biệt thực tế duy nhất là **bước tăng tải**: tải tuyệt đối thấp hơn nên cùng một bước nhảy chiếm tỷ lệ % lớn hơn. StrongLifts dùng 1.25 kg cho bench và overhead press ở nữ (nam 2.5 kg) [R33]. Xem mục 4.

---

## 3. Split theo số ngày/tuần và quỹ thời gian

### 3.1 Cơ sở

- ACSM 2009: novice 2–3 ngày/tuần, intermediate 3–4, advanced 4–5 [R5].
- ACSM 2026: ≥2 buổi/tuần cho strength; nhấn mạnh cá nhân hóa để tăng tuân thủ quan trọng hơn bám một công thức [R6].
- Tối thiểu mỗi buổi: 1 bài đẩy chân (squat/leg press), 1 bài kéo thân trên, 1 bài đẩy thân trên [R9].
- Máy hay tạ tự do **không** khác biệt nhất quán về kết quả; dây kháng lực và tập tại nhà cũng hiệu quả [R6]. Nghĩa là thay bài theo thiết bị có sẵn là an toàn về mặt hiệu quả.
- Bài ưu tiên đặt **đầu buổi** (strength tốt hơn khi tập ở đầu buổi) và tập **full range of motion** [R6].
- Superset, drop set, rest-pause giảm khoảng một nửa thời gian tập mà vẫn giữ volume [R9]. Superset cho strength và hypertrophy dài hạn tương đương set thường (SMD 0.10 và −0.05), nhưng RPE cao hơn và tốn năng lượng hơn; superset **agonist–antagonist** giữ volume tốt nhất [R76].
- Các chương trình beginner đều dùng full body 3 buổi/tuần xen kẽ A/B: BBR [R32], StrongLifts [R33], Phrak Greyskull [R34], Starting Strength [R35]. GZCLP chạy 3 hoặc 4 ngày [R36][R31]. PPL chạy 6 ngày hoặc 3 ngày [R36].
- Jeff Nippard Fundamentals: 3 ngày full body, 4 ngày upper/lower, 5 ngày body-part, dài 8 tuần, cho beginner đến intermediate [UNVERIFIED: trang sản phẩm chặn truy cập, số liệu lấy từ bản tóm tắt tìm kiếm của trang chính thức R38].

### 3.2 Ước tính số set theo thời gian [D]

Giả định: 1 set làm việc mất khoảng 40 giây; compound nghỉ 2–3 phút (≈3 phút/set tính cả nghỉ); isolation nghỉ 60–90 giây (≈2 phút/set); warm-up 5–8 phút. Đây là phép tính thiết kế, không phải số đo từ nghiên cứu.

| Quỹ thời gian | Số bài | Tổng set làm việc | Ghi chú |
|---|---|---|---|
| 45 phút | 4–5 | 12–14 | Bắt buộc dùng superset đối kháng cho bài phụ; bỏ isolation trước |
| 60 phút | 5–6 | 16–20 | Mặc định |
| 90 phút | 7–8 | 24–28 | Thêm isolation; vẫn giữ trần set/buổi ở mục 1.3 |

Thứ tự cắt khi thiếu thời gian [D]: (1) isolation tay và bắp chân, (2) set thứ 3 của bài phụ, (3) chuyển bài phụ sang superset, (4) không bao giờ cắt 3 bài cốt lõi (đẩy chân, kéo, đẩy) [R9].

### 3.3 Bảng chọn split [D]

| Ngày/tuần | Split | Tần suất mỗi nhóm cơ | Phù hợp |
|---|---|---|---|
| 2 | Full Body A / B | 2 | Mọi level; đủ cho novice |
| 3 | Full Body A / B / A, tuần sau B / A / B | 3 (xen kẽ) | **Mặc định cho novice** |
| 4 | Upper A / Lower A / Upper B / Lower B | 2 | Intermediate; novice sau 3–6 tháng |
| 5 | Upper / Lower / Push / Pull / Legs | 2 | Intermediate |
| 6 | Push / Pull / Legs × 2 | 2 | Intermediate; không khuyên cho novice (ACSM: novice 2–3 ngày [R5]) |

Luật: nếu `level = novice` và `days ≥ 5` thì gợi ý 3–4 buổi tạ, các ngày còn lại dùng cho cardio hoặc đi bộ [D, theo R5].

### 3.4 Template (viết theo **movement slot** để thay bài theo thiết bị)

Slot: `SQUAT` (squat, leg press, goblet squat), `HINGE` (deadlift, RDL, hip thrust, back extension), `H_PUSH` (bench, DB press, chest press máy, push-up), `H_PULL` (row tạ đòn, DB row, cable row, máy row), `V_PUSH` (overhead press, DB shoulder press), `V_PULL` (lat pulldown, pull-up, chin-up), `SL_LEG` (split squat, lunge, step-up), `ISO_*` (isolation).

Rep ghi theo mục tiêu `hypertrophy`; đổi theo bảng 2.2 cho mục tiêu khác. Tất cả template dưới đây là [D], dựng từ cấu trúc A/B của các chương trình beginner [R32][R33][R34][R35] và giới hạn volume ở mục 1.3.

**2–3 ngày: Full Body A/B (60 phút, khoảng 16–18 set)**

| # | Buổi A | Set × Rep | Buổi B | Set × Rep |
|---|---|---|---|---|
| 1 | `SQUAT` | 3 × 6–10 | `HINGE` | 3 × 6–10 |
| 2 | `H_PUSH` | 3 × 6–10 | `V_PUSH` | 3 × 6–10 |
| 3 | `H_PULL` | 3 × 8–12 | `V_PULL` | 3 × 8–12 |
| 4 | `HINGE` nhẹ (RDL / hip thrust) | 2 × 8–12 | `SL_LEG` hoặc leg press | 2 × 10–15 |
| 5 | `V_PULL` | 2 × 10–15 | `H_PUSH` nghiêng / DB | 2 × 10–15 |
| 6 | `ISO_core` | 2 × 10–15 | `ISO_side_delt` hoặc `ISO_arms` | 2 × 12–20 |

- Bản 45 phút: giữ bài 1–3 (3 set), bài 4 (2 set), ghép bài 5 và 6 thành superset hoặc bỏ. Khoảng 11–13 set.
- Bản 90 phút: thêm `ISO_biceps` 2 set, `ISO_triceps` 2 set, `ISO_calves` 2 set, và nâng bài 4–5 lên 3 set. Khoảng 24–26 set.
- Volume tuần (3 buổi, fractional): mỗi nhóm cơ lớn khoảng 7–12 set, nằm trong dải mục tiêu novice.

**4 ngày: Upper / Lower (60 phút)**

| # | Upper A | Lower A | Upper B | Lower B |
|---|---|---|---|---|
| 1 | `H_PUSH` 3 × 6–10 | `SQUAT` 3 × 6–10 | `V_PUSH` 3 × 6–10 | `HINGE` 3 × 6–10 |
| 2 | `H_PULL` 3 × 6–10 | `HINGE` nhẹ 3 × 8–12 | `V_PULL` 3 × 6–10 | `SQUAT` nhẹ / leg press 3 × 8–12 |
| 3 | `V_PUSH` 2 × 8–12 | `SL_LEG` 2 × 10–15 | `H_PUSH` nghiêng 3 × 8–12 | `SL_LEG` 2 × 10–15 |
| 4 | `V_PULL` 2 × 8–12 | `ISO_leg_curl` 2 × 10–15 | `H_PULL` 2 × 8–12 | `ISO_leg_ext` 2 × 10–15 |
| 5 | `ISO_side_delt` 2 × 12–20 | `ISO_calves` 2 × 10–20 | `ISO_biceps` 2 × 10–15 | `ISO_calves` 2 × 10–20 |
| 6 | `ISO_triceps` 2 × 10–15 | `ISO_core` 2 × 10–15 | `ISO_triceps` hoặc `ISO_rear_delt` 2 × 10–15 | `ISO_core` 2 × 10–15 |

**Kiểm đếm set trực tiếp mỗi tuần của các template (bản 60 phút) [D]:**

| Nhóm cơ | 2 ngày (A+B) | 3 ngày (trung bình 1.5 × A+B) | 4 ngày Upper/Lower |
|---|---|---|---|
| Ngực (`H_PUSH`) | 5 | 7.5 | 6 |
| Lưng (`H_PULL` + `V_PULL`) | 8 | 12 | 10 |
| Quads (`SQUAT` + `SL_LEG` + leg ext) | 5 | 7.5 | 12 |
| Hamstrings / glutes (`HINGE` + leg curl) | 5 | 7.5 | 8 |
| Vai (`V_PUSH` + side delt) | 3–5 | 4.5–7.5 | 7 |

- Lịch 2 ngày đạt sàn 4 set [R9] nhưng thấp hơn dải mục tiêu novice (6–10) ở vài nhóm cơ. Nếu người dùng có 90 phút thì nâng các bài 2 set lên 3 set; nếu không, chấp nhận mức này (vẫn tiến bộ, chậm hơn một chút [R1]).
- Lịch 3 ngày: lưng chạm trần novice (12). Nếu cần bớt, giảm bài #5 của buổi A còn 1–2 set.
- Lịch 4 ngày: mọi nhóm cơ ≥6 set trực tiếp (sàn intermediate); cộng thêm set gián tiếp 0.5 thì ngực, vai, tay sau đạt khoảng 8–11.
- Rules engine nên **tự đếm lại** volume sau mỗi lần thay bài hoặc cắt bài theo thời gian, và cảnh báo khi một nhóm cơ rơi dưới sàn ở mục 1.3.

**5–6 ngày:** Upper / Lower / Push / Pull / Legs (5 ngày) hoặc PPL × 2 (6 ngày). Mỗi buổi 5–6 bài theo đúng luật volume mục 1.3; không vượt trần set/buổi.

**Điều chỉnh theo mục tiêu [D]:**

| Mục tiêu | Thay đổi so với template |
|---|---|
| `strength` | Bài #1 của mỗi buổi dùng 3–4 set × 3–6 rep (novice 5–8), nghỉ 3–5 phút; bớt 1–2 bài isolation để đủ thời gian |
| `fat_loss` | Giữ nguyên bài #1–#3; bài phụ chạy superset đối kháng; thêm cardio theo mục 8 |
| `general_health` | 2–3 buổi, 2 set mỗi bài, 8–12 rep, RIR 2–3 |

---

## 4. Progression: mô hình và luật chính xác

### 4.1 Bằng chứng nền

- Tăng **rep** (giữ tải) cho kết quả tương đương tăng **tải** (giữ rep): ở người đã tập 8 tuần [R39], và ở người chưa tập 10 tuần (1RM và CSA không khác) [R40]. Vì vậy double progression là hợp lệ, không chỉ là giải pháp tình thế.
- ACSM 2009: tăng tải **2–10%** khi làm được hơn số rep mong muốn **1–2 rep** [R5].
- NSCA "2-for-2": nếu ở set cuối làm được hơn mục tiêu ≥2 rep trong **2 buổi liên tiếp** thì tăng tải. Mức tăng cho người nhỏ con / ít kinh nghiệm: thân trên 2.5–5 lb (1–2 kg), thân dưới 5–10 lb (2–4 kg) [R41, nguồn thứ cấp: tài liệu ôn thi CSCS, không phải sách gốc].
- ACSM 2026: progressive overload là nguyên tắc nền, nhưng lưu ý rằng tiến bộ vẫn xảy ra khi giữ nguyên tải tương đối [R6].

### 4.2 Luật của các chương trình beginner [S]

| Chương trình | Set × Rep | Bước tăng mỗi buổi | Khi fail | Nguồn |
|---|---|---|---|---|
| r/Fitness BBR | 3 × 5+ (set cuối AMRAP, dừng khi còn 1–2 rep) | Thân trên +2.5 lb, thân dưới +5 lb. Nếu AMRAP >10 rep: +5 lb / +10 lb | Tổng <15 rep cho một bài: **giảm 10%** lần tới | [R32] |
| StrongLifts 5×5 | 5 × 5 | Squat, bench, OHP, row: 2.5 kg (5 lb). Deadlift: 5 kg rồi giảm còn 2.5 kg. Nữ: 1.25 kg cho bench và OHP | Lặp lại tải đó; fail **3 buổi** thì **giảm khoảng 10%**; sau đó dùng bước nhỏ hơn (2.5 lb ≈ 1.1 kg tổng, hoặc ít hơn) | [R33] |
| Phrak Greyskull LP | 2 × 5 rồi 1 × 5+ (deadlift 1 × 5+) | Thân trên +2.5 lb, thân dưới +5 lb; AMRAP >10 thì gấp đôi | Không đủ rep: **giảm 10%** | [R34] |
| GZCLP | T1 5×3+, T2 3×10, T3 3×15+ | T1/T2: thân trên +5 lb, thân dưới +10 lb. T3: tăng tải khi AMRAP đạt 25 rep | T1: 5×3 → 6×2 → 10×1 → test 5RM mới, khởi động lại với 85%. T2: 3×10 → 3×8 → 3×6 → quay về tải stage 1 cũ +15–20 lb | [R31] |
| Starting Strength | 3 × 5 (deadlift 1 × 5), 3 buổi/tuần cách 48–72 giờ | Squat và deadlift +5 lb mỗi lần | Trang không nêu | [R35] |

Nghỉ giữa set theo các chương trình: BBR 2–3 phút [R32]; GZCLP T1 3–5 phút, T2 2–3 phút, T3 1–1.5 phút [R31]; StrongLifts 1.5 phút lúc đầu, 3–5 phút khi nặng [R33].

Quy đổi (tính toán): 2.5 lb ≈ 1.1 kg; 5 lb ≈ 2.3 kg; 10 lb ≈ 4.5 kg. Với đĩa tạ hệ kg, bước nhỏ nhất thường là 2.5 kg tổng (2 đĩa 1.25 kg), trừ khi phòng gym có đĩa nhỏ hơn.

### 4.3 Cấu hình thiết bị (bắt buộc là setting theo từng phòng gym) [D]

Không hard-code bước nhảy. Lưu theo gym:

```
gym.increment = {
  barbell_min_step_kg:   2.5,    // 2 x 1.25 kg; đổi thành 1.25 hoặc 1.0 nếu có đĩa nhỏ
  dumbbell_step_kg:      null,   // người dùng nhập: 1, 2, hoặc 2.5 kg mỗi tay
  machine_step_kg:       null,   // 1 nấc đĩa của máy, người dùng nhập
  bar_weight_kg:         20      // xác nhận lại; nhiều phòng có đòn 10 hoặc 15 kg
}
```

Bước nhảy tạ đơn và nấc máy ở phòng gym Việt Nam: [UNVERIFIED], không có nguồn; phải hỏi người dùng lần đầu dùng mỗi thiết bị.

### 4.4 Thuật toán A — Linear progression (LP)

**Thuật toán nào quản bài nào [D]:**

| Điều kiện | Thuật toán | Rep range |
|---|---|---|
| `novice`, 4 tuần đầu (config 4–8 tuần), mọi bài | B (double progression) | 8–12, RIR 2–3 (giai đoạn học kỹ thuật, mục 2.2) |
| `novice` sau giai đoạn đầu, bài **#1 và #2** của buổi nếu là compound tạ đòn / máy nấc nhỏ và bước nhảy ≤10% | **A (LP)** | theo mục tiêu: `strength` 5–8; `hypertrophy` và `fat_loss` 6–10; `general_health` 8–12 |
| Mọi bài còn lại của `novice`; mọi bài của `intermediate` | B | theo bảng 2.2 |
| Bất kỳ bài nào có bước nhảy >10% tải hiện tại | C (B với rep range nới rộng) | xem 4.6 |

Thứ tự ưu tiên khi các bảng khác nhau: **giai đoạn học kỹ thuật** > **bảng mục tiêu 2.2** > rep ghi trong template 3.4 (template chỉ minh họa cho `hypertrophy`).

Dùng cho: `novice`, bài compound tạ đòn hoặc máy có nấc nhỏ (`SQUAT`, `HINGE`, `H_PUSH`, `V_PUSH`, `H_PULL`).

```
INPUT: sets, rep_range [lo, hi] (vd 3 x 6..10), last_session, gym.increment
step_lower = 2.5 kg            // [S] StrongLifts: squat 2.5 kg; deadlift 5 kg lúc đầu
step_upper = 2.5 kg (nam) | 1.25 kg (nữ, nếu gym có đĩa)   // [S] R33
Mỗi set: làm đến khi còn target_RIR, không vượt quá hi.
SUCCESS  = mọi set đạt >= lo        // lo là "rep mục tiêu" của LP; các chương trình gốc dùng 1 số cố định (5) [R32][R33]
IF SUCCESS:
    next_load = load + step
    IF set cuối là AMRAP và đạt > 10 rep: next_load = load + 2 * step     // [S] R32, R34
ELSE (FAIL):
    fail_count += 1
    IF fail_count < 3: next_load = load              // lặp lại, [S] R33
    ELSE: next_load = round_down(load * 0.90); fail_count = 0   // [S] giảm 10%: R32, R33, R34
```

Luật chặn [D, dựa trên 2–10% của ACSM R5]: nếu `step / load > 0.10` (ví dụ +2.5 kg trên overhead press 20 kg = 12.5%) thì **không dùng LP**, chuyển bài đó sang thuật toán B.

Điều kiện rời LP [D]: một bài bị giảm 10% **2 lần** trong 8 tuần, hoặc đã chạy LP quá 3 tháng (BBR khuyên tối đa 3 tháng [R32]; Phrak 2–4 tháng [R34]) thì chuyển bài đó sang thuật toán B.

### 4.5 Thuật toán B — Double progression

Dùng cho: mọi bài với tạ đơn, máy, isolation; mọi bài của `intermediate`; bài của `novice` khi bước nhảy >10%.

```
INPUT: rep_range [lo, hi] (vd 8..12), sets, target_RIR
Mỗi buổi: giữ nguyên tải, cố thêm rep (dừng ở target_RIR).
IF mọi set >= hi:
    confirm += 1
    IF confirm >= 1 (LP-like) hoặc >= 2 (thận trọng, kiểu 2-for-2 [R41]):
        next_load = load + min_step; rep mục tiêu quay về lo; confirm = 0
ELSE IF tổng rep >= tổng rep buổi trước: giữ tải (đang tiến bộ)
ELSE: stall_count += 1
Sau khi tăng tải:
    IF set đầu < lo: quay lại tải cũ, nới hi lên +2..3 rep (xem thuật toán C)
```

Nguồn: nguyên tắc "giữ tải đến khi chạm đỉnh rep range rồi mới tăng" được Barbell Medicine mô tả với ví dụ 8–12 rep [R82]; ngưỡng "hơn mục tiêu 1–2 rep thì tăng 2–10%" từ ACSM [R5]. Mặc định `confirm = 1` cho novice, `confirm = 2` cho bài thân trên của nữ hoặc khi bước nhảy >5% [D].

### 4.6 Thuật toán C — Rep-range progression cho bước nhảy lớn [D]

Vấn đề: tạ đơn nhảy 2.5 kg mỗi tay trên tạ 7.5 kg là +33%, vượt xa 2–10% [R5].

```
jump_pct = step / load
IF jump_pct <= 0.10:           rep_range = [lo, hi]            // bình thường
ELSE IF jump_pct <= 0.20:      rep_range = [lo, hi + 3]        // vd 8..15
ELSE:                          rep_range = [lo, hi + 6..8]     // vd 8..20
    hoặc thêm 1 set trước khi tăng tải
```

Cơ sở: hypertrophy tương đương trong dải rep rất rộng (30%–100% 1RM [R6]; 6 đến 20+ rep [R16]), và tăng rep hiệu quả ngang tăng tải [R39][R40]. Con số cụ thể của từng bậc là mặc định thiết kế.

### 4.7 Sau một buổi fail

| Tình huống | Hành động | Nguồn |
|---|---|---|
| Thiếu rep ở 1 bài, lần đầu | Lặp lại tải đó buổi sau | [R33] |
| Thiếu rep cùng tải 3 buổi | Giảm 10%, tăng lại từ đó | [R33] |
| Tổng rep <15 ở bài 3 × 5+ | Giảm 10% | [R32] |
| Fail trong ngày readiness đỏ/vàng (mục 6) | **Không tính** vào `fail_count` | [D] |
| Fail do đau | Không tính fail; chạy luật mục 9 | [D] |
| Sau khi giảm 10% | Dùng bước nhỏ hơn nếu gym có (2.5 lb ≈ 1.1 kg tổng, hoặc ít hơn) | [R33] |

---

## 5. Deload, plateau, buổi bỏ lỡ, nghỉ dài

### 5.1 Deload: bằng chứng

- Đồng thuận Delphi (34 → 21 HLV): deload là "giai đoạn giảm stress tập luyện để giảm mỏi, thúc đẩy hồi phục". Không có con số đồng thuận. Thực hành phổ biến được nêu: khoảng **7 ngày**, mỗi **4–6 tuần** (phần thảo luận nói 4–8 tuần). Cách giảm: bớt set, bớt rep, bớt ngày tập, xa failure hơn; giữ nguyên bài tập; có thể giữ cường độ và chỉ giảm volume. Deload có thể vừa lên kế hoạch trước vừa tự điều chỉnh [R42].
- Thử nghiệm duy nhất: nghỉ **hẳn 1 tuần** giữa chương trình 9 tuần (39 người) **không** giúp hypertrophy, và strength thân dưới **kém hơn** nhóm tập liên tục [R43]. Hạn chế: đó là nghỉ hoàn toàn, không phải deload giảm tải.
- RP: tuần deload ở 5+ RIR, ví dụ volume giảm từ 20 xuống 6 set [R14][R15].

### 5.2 Luật deload để code [D]

Không lên lịch deload cố định cho `novice` (cơ sở: [R43] không thấy lợi ích; LP đã có sẵn cơ chế giảm 10% khi fail). Dùng deload **phản ứng**:

```
TRIGGER deload_week nếu có >= 2 điều kiện trong 2 tuần gần nhất:
  - >= 2 bài compound bị stall (stall_count >= 2) hoặc vừa giảm 10%
  - readiness trung bình 7 ngày ở vùng đỏ/vàng (mục 6)
  - điểm soreness <= 2 (thang mục 6: 1 = đau nhiều, 5 = không đau) vẫn còn sau > 72 giờ, ở >= 2 buổi
  - người dùng tự báo "kiệt sức / chán tập"
HOẶC theo lịch (chỉ intermediate): sau 6-8 tuần tập liên tục không nghỉ    // dải 4-8 tuần, R42

DELOAD WEEK:
  sets  = round(sets * 0.5)        // "bớt set", R42; mức 50% là [D]
  load  = giữ nguyên hoặc -10%     // R42: có thể giữ cường độ, chỉ giảm volume
  RIR  >= 4                        // R42: xa failure hơn; RP: 5+ RIR (R15)
  bài tập: giữ nguyên              // R42
  sau deload: quay lại tải trước deload, không tăng trong buổi đầu
```

### 5.3 Plateau

Định nghĩa [D]: một bài không tăng tải **và** không tăng tổng rep trong **3 buổi liên tiếp** (LP), hoặc **3–4 tuần** (double progression).

Thứ tự xử lý [D, ghép từ R31, R32, R33]:

1. Kiểm tra dữ liệu check-in: ngủ, stress, cân nặng đang giảm? Nếu `goal = fat_loss` thì giữ được tải đã là thành công [R74].
2. LP: giảm 10% rồi tăng lại [R32][R33].
3. Đổi cấu trúc set-rep ở cùng tải, kiểu GZCLP: 5×3 → 6×2, hoặc 3×10 → 3×8 → 3×6 [R31].
4. Chuyển bài đó từ LP sang double progression.
5. Nếu volume tuần đang dưới mục tiêu: +1 đến +2 set/tuần cho nhóm cơ đó (volume có liều–đáp ứng [R1][R7]).
6. Nếu ≥2 bài cùng plateau: kích hoạt deload (5.2).
7. Đổi biến thể bài tập cùng slot (ví dụ bench tạ đòn sang DB press) [D].

### 5.4 Bỏ buổi và nghỉ dài: bằng chứng

- Tập 6 tuần rồi nghỉ 3 tuần, lặp 3 chu kỳ: sau 24 tuần, cơ và sức mạnh **tương đương** nhóm tập liên tục [R44].
- Nghỉ **10 tuần** giữa hai đợt tập 10 tuần: sức mạnh và cơ giảm trong lúc nghỉ, nhưng hồi lại nhanh trong 5 tuần đầu tập lại; kết quả cuối giống nhóm tập liên tục 20 tuần. Tác giả kết luận không cần quá lo về những đợt nghỉ ngắn [R45].
- Sức mạnh giữ được đến khoảng **3 tuần** không tập; sau đó giảm nhanh hơn (5–16 tuần) [R46].
- Người trẻ giữ được cơ với **1/3 liều** tập thường ngày [R47].
- Nippard (tổng hợp): quay lại sau nghỉ dài thì compound bắt đầu ở 50–60% 1RM cũ, RPE ≤5, 2–3 set/bài thay vì 3–4, khoảng 7–10 set/nhóm cơ/tuần; giai đoạn "bridge" 2–4 tuần; lấy lại sức mạnh mất khoảng một nửa thời gian đã nghỉ [R37].

### 5.5 Luật bỏ buổi / nghỉ để code

Dùng **số ngày trễ so với lịch**, không dùng số ngày thô (vì ở lịch 2 hoặc 4 ngày/tuần, mỗi bài vốn chỉ lặp lại sau 7 ngày):

```
planned_interval = số ngày dự kiến giữa 2 lần tập cùng slot theo lịch của user
                   (vd: full body 3 ngày/tuần xen kẽ A/B -> 4-5 ngày; upper/lower 4 ngày -> 3-4 ngày; 2 ngày/tuần -> 7 ngày)
overdue_days     = max(0, days_since_last_same_slot - planned_interval)
```

| `overdue_days` | Tải | Volume | Progression | Cơ sở |
|---|---|---|---|---|
| 0–3 (đúng lịch hoặc dời vài ngày) | theo thuật toán | 100% | **bình thường, vẫn được tăng** | — |
| 4–10 (lỡ khoảng 1 tuần) | **giữ tải buổi trước**, không tăng | 100% | tiếp tục từ buổi sau | [D]; sức mạnh giữ được đến khoảng 3 tuần [R46] |
| 11–21 (nghỉ khoảng 2–3 tuần) | −10% | 100%, RIR +1 trong buổi đầu | tăng lại bình thường | [D]; −10% mượn từ luật reset của LP [R32][R33] |
| 22–56 (nghỉ 3–8 tuần) | −20% đến −30% | khoảng 2/3 số set trong tuần đầu | 1–2 tuần "bridge" rồi về bình thường | [D]; nội suy giữa [R46] và [R37] |
| > 56 (nghỉ > 8 tuần) | bắt đầu ở 50–60% tải cũ, RPE ≤5 | 2–3 set/bài | bridge 2–4 tuần, sau đó LP lại | [R37] |

Luật lịch [D]:

- Lỡ 1 buổi: **dời** lịch (buổi kế tiếp trong vòng xoay A/B), không bỏ qua buổi đó.
- Tuần chỉ tập được 1 buổi: chạy 1 buổi full body với 3 bài cốt lõi. Người trẻ duy trì được khối cơ với chỉ một buổi ngắn mỗi tuần [R9]; 1/3 liều tập cũng giữ được cơ [R47].
- Không "tập bù" 2 buổi cùng nhóm cơ trong 2 ngày liên tiếp nếu buổi đầu tập sát failure (hồi phục cần 24–48 giờ [R57]).
- Hiển thị cho người dùng thông điệp từ [R45]: nghỉ ngắn không làm mất thành quả lâu dài.

---

## 6. Autoregulation từ check-in hằng ngày

### 6.1 Bằng chứng: có gì và không có gì

| Phát hiện | Nguồn |
|---|---|
| Thước đo **chủ quan** (tự báo cáo) phản ánh tải tập nhạy và nhất quán hơn thước đo khách quan thông dụng; có thể dùng độc lập | [R48] |
| Thang Perceived Recovery Status: tương quan vừa với thay đổi hiệu suất (r = −0.63), 16 người, bài chạy nước rút | [R49] |
| Flexible nonlinear periodization (người tập tự chọn buổi nặng/nhẹ theo cảm giác trong ngày): leg press +62 kg so với +16 kg; chest press không khác. Chỉ 16 beginner, 12 tuần | [R50] |
| Đặt tải theo RPE so với %1RM: cả hai hiệu quả, RPE có thể hơi lợi cho 1RM (không ý nghĩa thống kê), 21 nam có kinh nghiệm | [R51] |
| Meta-analysis: autoregulation tải so với tải cố định, strength **không khác** (MD 2.07 kg, p = 0.09) | [R52] |
| ACSM 2026: bằng chứng về autoregulation trong buổi còn **không rõ ràng** (các review cho kết quả trái chiều) | [R6] |
| Thiếu ngủ (≤6 giờ): hiệu suất giảm trung bình **7.56%**; giảm khoảng 0.4% cho mỗi giờ thức thêm; tập buổi chiều/tối bị ảnh hưởng, buổi sáng hầu như không | [R53] |
| Thiếu ngủ nhiều đêm liên tiếp giảm lực ở bài **đa khớp**, không giảm ở bài đơn khớp | [R54] |
| Stress cuộc sống cao: tăng sức mạnh bench và squat kém hơn sau 12 tuần | [R55] |
| Stress mạn tính làm chậm hồi phục lực cơ, năng lượng, độ mỏi, đau cơ trong 96 giờ sau buổi tập nặng | [R56] |
| Tập đến failure kéo dài thời gian hồi phục đến 24–48 giờ | [R57] |

**Kết luận trung thực:** các biến đầu vào (ngủ, stress, đau cơ, năng lượng) **có** cơ sở khoa học. Nhưng **không có nghiên cứu nào xác thực một công thức điểm readiness cụ thể** nào cho tập tạ, và chưa có bằng chứng rằng điều chỉnh theo điểm readiness cho kết quả tốt hơn chương trình cố định. Toàn bộ mục 6.2–6.3 là **[D]**. Lợi ích kỳ vọng thực tế là tuân thủ và an toàn, không phải tăng cơ nhanh hơn.

### 6.2 Điểm readiness [D]

Check-in 5 câu, thang 1–5 (5 là tốt nhất):

| Mục | 1 | 3 | 5 |
|---|---|---|---|
| `sleep` | < 5 giờ hoặc rất tệ | 6–7 giờ | ≥ 7.5 giờ, ngủ ngon |
| `soreness` (nhóm cơ sắp tập) | Đau, khó cử động | Hơi ê | Không đau |
| `energy` | Kiệt sức | Bình thường | Rất sung sức |
| `stress` | Rất căng thẳng | Bình thường | Thoải mái |
| `pain` (khớp/chấn thương) | **Xử lý riêng ở mục 9, không cộng vào điểm** | | |

```
R = sleep + soreness + energy + stress          // 4..20; ngày "bình thường" (3-3-3-3) = 12
GREEN  : R >= 11        // bình thường, hoặc chỉ 1 mục hơi kém (vd 3-3-3-2)
YELLOW : 8 <= R <= 10   // >= 2 mục kém
RED    : R <= 7         // gần như mọi mục đều kém
Override:
  sleep_hours <= 6            -> tối thiểu YELLOW cho bài compound     // ngưỡng 6h: R53
  sleep_hours <= 6 trong >= 2 đêm liên tiếp -> hạ 1 bậc               // R54
  soreness == 1 ở nhóm cơ X   -> bỏ hoặc giảm 50% set của X, tập nhóm khác
  ốm có sốt                   -> nghỉ
```

### 6.3 Điều chỉnh theo vùng [D]

| Vùng | Volume | Tải | RIR | Progression | Ghi chú |
|---|---|---|---|---|---|
| GREEN | 100% | theo kế hoạch | theo kế hoạch | cho phép tăng | — |
| YELLOW | −1 set ở các bài có ≥3 set (không bài nào xuống dưới 2 set [R6]); nếu mọi bài đều 2 set thì bỏ bài isolation cuối | giữ tải, **không tăng** | +1 | hoãn; không tính fail | Bỏ AMRAP và set sát failure [R57]; giữ nguyên bài compound, vì thiếu ngủ ảnh hưởng chủ yếu bài đa khớp [R54] |
| RED | −50% set; chỉ giữ 3 bài cốt lõi [R9] | −10% | ≥ 3–4 | hoãn; không tính fail | Hoặc đổi thành buổi đi bộ / LISS 20–30 phút. Liều tập giảm còn 1/3 vẫn giữ được cơ ở người trẻ [R47] |

Mức giảm 7.56% do thiếu ngủ [R53] là cơ sở cho việc giảm tải khoảng 10% ở vùng RED; các con số còn lại là mặc định thiết kế.

**Autoregulation theo hiệu suất trong buổi (ưu tiên hơn điểm check-in) [D]:**

```
Sau set làm việc đầu tiên của bài compound đầu buổi:
  IF reps <= (reps buổi trước cùng tải) - 2  OR  RIR tự báo = 0 khi mục tiêu >= 2:
        giảm tải 5-10% cho các set còn lại, hạ 1 bậc vùng cho cả buổi
  IF reps >= mục tiêu + 2 và RIR >= 3 ở ngày YELLOW:
        nâng lại lên GREEN
```

Cơ sở: Helms mô tả việc dùng RIR song song với kế hoạch để người tập "giảm cường độ nếu không hoàn thành đủ rep, hoặc tăng nếu còn dư hơn mức RIR đặt ra" [R19]. Ngưỡng 2 rep và 5–10% là [D].

Lưu ý cho novice: RIR tự báo sai lệch khoảng 1 rep [R21], nên tín hiệu **số rep thực tế** đáng tin hơn điểm cảm giác.

Chống lạm dụng [D]: nếu >50% số buổi trong 3 tuần rơi vào YELLOW/RED, đừng tiếp tục giảm; hiển thị gợi ý xem lại giấc ngủ, lượng ăn, hoặc giảm số ngày tập trong profile.

---

## 7. Warm-up

### 7.1 Bằng chứng

- Khởi động chung (5–15 phút cardio nhẹ) **không phải ưu tiên** khi ít thời gian. Khởi động chuyên biệt (set nhẹ của chính bài đó) chủ yếu có ích cho tải nặng (>80% 1RM); chỉ cần cho **bài đầu tiên của mỗi nhóm cơ** [R9].
- Một thử nghiệm (15 nam, 4 set ở 80% 1RM đến failure): không khác biệt về tổng rep giữa không khởi động, khởi động chuyên biệt, aerobic, hoặc kết hợp [R58].
- Review thân trên: khởi động động với tải cao cải thiện sức mạnh và power; stretching tĩnh ngắn không ảnh hưởng power; **không có nghiên cứu nào về phòng chấn thương** [R59].
- Meta-analysis: khởi động cải thiện hiệu suất ở 79% tiêu chí được xét; ít bằng chứng là có hại [R60].
- Stretching tĩnh <60 giây mỗi nhóm cơ không làm giảm sức mạnh; stretching dài làm giảm cấp tính; chỉ ưu tiên stretching nếu mục tiêu là độ dẻo [R9].

Kết luận: bằng chứng cho warm-up **yếu và chủ yếu về hiệu suất**, không phải về an toàn. Với beginner, warm-up set còn có giá trị luyện kỹ thuật (đây là lập luận, không phải số liệu).

### 7.2 Giao thức để code

Giao thức tham khảo từ nguồn thực hành:

- Hevy: set 1 với thanh đòn trống hoặc tạ rất nhẹ 15–20 rep; set 2 khoảng 50% × 5–6; set 3 khoảng 75% × 3; set 4 tùy chọn khoảng 90% × 1; nghỉ 45–60 giây. Mặc định máy tính của họ: 40% × 5, 60% × 5, 80% × 3. Thường 3–4 set là đủ; bài sau trong buổi cần ít hơn; warm-up set không tính vào volume [R61].
- Barbell Logic: 1–2 set × 5 với đòn trống, rồi 3–5 set tăng dần với rep giảm dần 5-3-2-1; set khởi động cuối thấp hơn set làm việc ít nhất 10–20 lb; không bao giờ để warm-up gây mỏi [R62].

Luật [D], dựa trên [R9][R61][R62]:

| Trường hợp | Warm-up set (% tải làm việc × rep) | Nghỉ |
|---|---|---|
| Bài compound đầu tiên của buổi, tải ≥ 40 kg | đòn trống × 10; 50% × 5; 75% × 3; (90% × 1 nếu rep mục tiêu ≤ 5) | 45–60 giây |
| Bài compound đầu tiên, tải < 40 kg | đòn trống hoặc 50% × 8; 75% × 3 | 45–60 giây |
| Bài compound thứ hai, khác nhóm cơ (ví dụ sau squat đến bench) | 50% × 5; 75% × 3 | 45 giây |
| Bài cùng nhóm cơ đã được khởi động | 1 set 60–70% × 5, hoặc bỏ | — |
| Isolation, máy | 1 set 50–60% × 8–10, hoặc bỏ | — |
| Khởi động chung | 3–5 phút đi bộ nhanh / đạp xe; **tùy chọn**, bỏ khi buổi 45 phút | — |

- Warm-up set dừng xa failure, không tính vào volume [R61].
- Làm tròn tải warm-up theo `gym.increment`.

---

## 8. Cardio theo mục tiêu và hiệu ứng interference

### 8.1 Bằng chứng về liều cardio

| Phát hiện | Con số | Nguồn |
|---|---|---|
| WHO 2020 | 150–300 phút/tuần cường độ vừa, hoặc 75–150 phút cường độ cao, hoặc kết hợp tương đương; khuyến nghị tập tăng cơ đều đặn cho mọi nhóm tuổi | [R63] |
| ACSM (giảm cân) | 150–250 phút/tuần: ngừa tăng cân, giảm cân khiêm tốn. **>250 phút/tuần**: giảm cân có ý nghĩa lâm sàng. Tập tạ không tăng giảm cân nhưng có thể tăng khối nạc và tăng giảm mỡ | [R64] |
| Aerobic liều–đáp ứng | Cân nặng, vòng eo, mỡ giảm tuyến tính đến **300 phút/tuần**; cần ≥150 phút/tuần cường độ vừa trở lên để có mức giảm có ý nghĩa lâm sàng | [R65] |
| Số bước và tử vong | Nguy cơ giảm dần đến **8,000–10,000 bước/ngày** ở người <60 tuổi (6,000–8,000 ở người ≥60). So với nhóm thấp nhất (trung vị 3,553 bước): HR 0.60 ở 5,801; 0.55 ở 7,842; 0.47 ở 10,901 bước | [R66] |
| Số bước và sức khỏe | Điểm uốn khoảng 5,000–7,000 bước/ngày; **7,000 bước/ngày** là mục tiêu thực tế có lợi ích lâm sàng rõ | [R67] |
| HIIT so với cardio đều (MICT) | Giảm mỡ **tương đương**; HIIT tốn ít thời gian hơn khoảng 40%. Chạy có hiệu quả giảm mỡ, đạp xe thì không thấy | [R68] |
| BBR | Cardio tối thiểu 2 ngày/tuần: 1 ngày nhẹ 15–30 phút, 1 ngày cao 10–15 phút HIIT; nếu cùng ngày tập tạ thì làm **sau** tạ | [R32] |

### 8.2 Bằng chứng về interference

| Phát hiện | Con số | Nguồn |
|---|---|---|
| Concurrent training so với chỉ tập tạ | Sức mạnh tối đa SMD −0.06 (không ý nghĩa); hypertrophy SMD −0.01 (không ý nghĩa); **sức mạnh bùng nổ** SMD −0.28 (có ý nghĩa), rõ hơn khi tập **cùng buổi** so với cách nhau ≥3 giờ | [R69] |
| Theo trình độ | Người **chưa tập**: không interference (ES 0.03). Tập vừa: −0.20 (không ý nghĩa). Người đã tập: −0.35, và chỉ khi tập **cùng buổi** (−0.66 so với −0.10 khi khác buổi) | [R70] |
| HIIT + tạ | Hypertrophy và sức mạnh thân trên không đổi; sức mạnh **thân dưới** hơi thấp hơn (ES −0.248) | [R71] |
| Meta cũ (2012) | Interference phụ thuộc loại hình (chạy, không phải đạp xe), tần suất và thời lượng cardio | [R72] |
| Review | Bằng chứng về interference lên hypertrophy yếu hơn người ta vẫn nghĩ | [R73] |

**Kết luận cho 2 người dùng này:** ở mức beginner, cardio **không** cản trở tăng cơ hay sức mạnh [R69][R70]. Không cần luật phức tạp; chỉ cần sắp thứ tự hợp lý.

### 8.3 Bảng luật cardio [D, dựa trên các nguồn trên]

| Mục tiêu | Bước/ngày | Cardio có cấu trúc mỗi tuần | HIIT |
|---|---|---|---|
| `fat_loss` | 8,000–10,000 [R66] | Tiến dần tới 150–250+ phút cường độ vừa (tính cả đi bộ nhanh) [R64][R65]; thực tế 2–4 buổi LISS 20–40 phút | 0–1 buổi 10–15 phút [R32], tùy chọn |
| `hypertrophy` | ≥ 7,000 [R67] | 2 buổi LISS 15–30 phút [R32]; hướng tới sàn WHO 150 phút tính cả đi bộ [R63] | 0–1 buổi |
| `strength` | ≥ 7,000 [R67] | 1–2 buổi LISS 15–30 phút | Tránh HIIT trước hoặc cùng buổi tập chân nặng [R71] |
| `general_health` / `recomp` | 7,000–10,000 [R66][R67] | 150–300 phút vừa hoặc 75–150 phút cao [R63] | 1 buổi 10–15 phút, tùy chọn |

Luật xếp lịch [D]:

1. Cùng ngày: **tạ trước, cardio sau** [R32]; bài ưu tiên nên ở đầu buổi [R6].
2. Nếu tách được: cách buổi tạ ≥3 giờ [R69].
3. Không xếp HIIT trong 24 giờ trước buổi `SQUAT`/`HINGE` nặng [D, theo R71].
4. Đi bộ (đếm bước) không cần luật interference; là công cụ mặc định cho `fat_loss`.
5. Khi `goal = fat_loss` và thiếu thời gian: không cắt buổi tạ để lấy chỗ cho cardio. Tạ giữ khối nạc trong lúc thâm hụt [R64][R74]; tăng số bước trước.
6. Novice mới bắt đầu: khởi điểm thấp hơn bảng (ví dụ +2,000 bước so với mức hiện tại, 2 buổi LISS 15 phút) rồi tăng dần [D].

---

## 9. An toàn

### 9.1 Mức rủi ro nền

- Bodybuilding: 0.24–1 chấn thương / 1000 giờ. Vị trí hay gặp: **vai, lưng dưới, gối**, khuỷu, cổ tay; loại: căng cơ, viêm gân, bong gân. Tỷ lệ thấp so với các môn đồng đội [R77].
- Weightlifting 2.4–3.3 và powerlifting 1.0–4.4 chấn thương / 1000 giờ; hay gặp ở cột sống, vai, gối [R78].

Tập tạ là hoạt động rủi ro thấp; app nên truyền đạt điều này để tránh sợ hãi quá mức.

### 9.2 Sàng lọc trước khi bắt đầu (onboarding)

- ACSM: sàng lọc dựa trên 3 yếu tố: (1) mức hoạt động hiện tại, (2) có dấu hiệu/triệu chứng hoặc bệnh tim mạch, chuyển hóa, thận đã biết, (3) cường độ mong muốn. Không còn dùng bảng đếm yếu tố nguy cơ, để tránh rào cản không cần thiết [R88].
- PAR-Q+ là bảng câu hỏi tự sàng lọc chuẩn; nếu có câu trả lời "có" thì nên hỏi bác sĩ hoặc chuyên gia vận động trước khi tăng hoạt động nhiều [R89]. Nội dung 7 câu hỏi: [UNVERIFIED], tôi không trích được nguyên văn; hãy lấy bản chính thức tại nguồn.

Luật onboarding [D]: hỏi (a) bệnh tim, huyết áp, tiểu đường, thận đã được chẩn đoán; (b) đau ngực, khó thở bất thường, chóng mặt hoặc ngất khi gắng sức; (c) đang mang thai hoặc sau sinh; (d) chấn thương hoặc phẫu thuật gần đây. Có bất kỳ mục nào ở (a)–(c): hiển thị khuyến cáo gặp bác sĩ trước, và chỉ cho phép chương trình cường độ nhẹ đến vừa cho đến khi người dùng xác nhận.

### 9.3 Dừng buổi tập ngay (red flags toàn thân)

| Dấu hiệu | Hành động | Nguồn |
|---|---|---|
| Đau ngực đột ngột không hết (cảm giác bóp nghẹt, đè nặng, nóng rát); đau lan ra tay, cổ, hàm, bụng, lưng; đau ngực kèm vã mồ hôi, buồn nôn, choáng, khó thở | **Gọi cấp cứu ngay** (Việt Nam: 115) | [R87] |
| Chóng mặt, sắp ngất, khó thở bất thường, tim đập loạn | Dừng buổi, nghỉ; nếu không hết thì đi khám | [D] |
| Đau nhói đột ngột, nghe/cảm thấy "rắc" hoặc "bựt", sưng nhanh, biến dạng, không chịu được lực | Dừng, không tập tiếp vùng đó, đi khám | [D]; khớp với danh sách khẩn cấp của NHS [R85][R86] |

Số cấp cứu 115 là thông tin phổ thông tại Việt Nam, tôi không tra nguồn riêng: [UNVERIFIED].

### 9.4 Red flags kỹ thuật cho beginner [D]

App nên nhắc dừng set hoặc hạ tải khi:

- Form vỡ hoặc tốc độ thanh đòn chậm hẳn (BBR dùng đúng tiêu chí này để dừng set AMRAP [R32]).
- Tập đến failure ở bài compound tạ tự do khi không có người đỡ hoặc thanh an toàn (ACSM 2026: failure không cần thiết và form xấu làm tăng nguy cơ chấn thương [R6]). Luật: `novice` + bài `SQUAT`/`H_PUSH` tạ đòn thì RIR tối thiểu = 2; RP cũng giữ 1 RIR cho bài có thể rơi tạ lên người [R15].
- Tăng tải nhanh hơn luật mục 4 (vượt 10% một lần [R5]).
- Bỏ full range of motion để nâng nặng hơn [R6].
- Tập sát failure cùng nhóm cơ hai ngày liên tiếp [R57].

### 9.5 Đau khi tập: mô hình xử lý

**Bằng chứng**

- Tập có đau (trong chương trình phục hồi đau cơ xương **mạn tính**) cho kết quả ngắn hạn hơi tốt hơn tập không đau (ES −0.27); trung và dài hạn không khác. Đau khi tập không nhất thiết là rào cản [R79].
- Các thử nghiệm trong review đó dùng ngưỡng: đau **đến 5/10** trong lúc tập, với điều kiện đau **hết vào sáng hôm sau** (hoặc trước buổi kế tiếp) và không tăng cứng khớp buổi sáng [R79].
- Pain-monitoring model: tiếp tục hoạt động có theo dõi đau không gây hại so với nghỉ hoàn toàn (gân Achilles) [R80]; mô hình gốc từ điều trị đau bánh chè–đùi [R81].
- Barbell Medicine, dấu hiệu tải đang quá mức: đau **tăng dần qua từng set**; đau **tệ hơn trong 24–48 giờ** sau buổi; đau **không về mức nền** trước buổi kế. Cách chỉnh: giảm tải (thường phải giảm nhiều hơn người ta muốn), hạ RPE (ví dụ 6 thay vì 8), tăng rep (từ 5 lên 12), tempo chậm (xuống 3 giây, lên 3 giây), đổi biến thể; tăng lại thận trọng 5–10%, dùng double progression [R82].
- E3 Rehab, các biến có thể chỉnh: tải, nỗ lực, biên độ, tempo, tần suất, volume, nghỉ, biến thể, đổi bài [R83].
- Đau bánh chè–đùi: đồng thuận chuyên gia ủng hộ **tập luyện trị liệu**, nhất là kết hợp bài cho hông và gối [R90].
- NHS, đau lưng: duy trì hoạt động, tránh nằm nghỉ lâu; dừng bài tập nào làm đau nặng hơn [R84].

**Lưu ý về giới hạn:** ngưỡng 5/10 đến từ các chương trình có chuyên viên vật lý trị liệu giám sát, cho đau mạn tính. App tự phục vụ cho beginner nên dùng ngưỡng **thận trọng hơn**. Bảng dưới là [D]. (Vợ người dùng học vật lý trị liệu, có thể rà soát lại bảng này.)

**Thang đau 0–10 và hành động [D, dựa trên R79, R82]**

| Đau trong lúc tập | Hành động |
|---|---|
| 0–2, không tăng qua các set | Tập bình thường; ghi lại |
| 3–4, âm ỉ, ổn định | **Chỉnh bài**: giảm tải 10–20%, RIR +2, tempo chậm, hoặc rút ngắn biên độ. Không tăng tải bài đó hôm nay |
| ≥ 5, hoặc tăng dần qua từng set [R82] | **Dừng bài đó**, đổi sang biến thể không đau cùng slot. Không còn biến thể nào ≤ 2/10 thì bỏ slot đó hôm nay |
| Đau nhói, buốt, lan, tê, yếu chi, khớp kẹt hoặc sụm | **Dừng tập vùng đó**; xem red flags từng vùng bên dưới |

| Sau buổi tập | Hành động |
|---|---|
| Đau về mức nền vào sáng hôm sau [R79] | Tiếp tục; có thể tăng lại 5–10% mỗi buổi [R82] |
| Đau tệ hơn trong 24–48 giờ, hoặc chưa về nền trước buổi kế [R82] | Buổi kế: giảm thêm tải / volume cho vùng đó, hoặc đổi bài |
| Đau không cải thiện sau **2 tuần** điều chỉnh (vai [R86]) hoặc "vài tuần" (gối [R85]) | Khuyên đi khám bác sĩ / vật lý trị liệu; khóa slot liên quan ở chế độ biến thể nhẹ |

Phân biệt với **đau cơ khởi phát muộn (DOMS)**: ê mỏi lan tỏa trong bụng cơ, hai bên, 1–3 ngày sau buổi tập mới hoặc nặng. Đó là dữ liệu `soreness` ở mục 6, không phải `pain` [D].

### 9.6 Theo vùng: red flags và bài thay thế

**Lưng dưới**

| Mức | Dấu hiệu | Nguồn |
|---|---|---|
| Cấp cứu ngay | Đau, tê, yếu hoặc châm chích ở **cả hai chân**; mất cảm giác quanh vùng sinh dục hoặc hậu môn; rối loạn tiểu tiện / đại tiện (bí tiểu, són); đau ngực; đau sau tai nạn nghiêm trọng | [R84] |
| Khám khẩn | Kèm sốt, ớn lạnh, mệt toàn thân; đau dữ dội đột ngột hoặc xấu đi nhanh | [R84] |

Thay bài: deadlift truyền thống → sumo hoặc Romanian deadlift; deadlift từ sàn → kéo từ bục / đĩa kê cao rồi hạ dần; squat → kê gót hoặc goblet squat; thay bằng back extension, hip thrust, leg curl để vẫn tập nhóm cơ đó [R83]. Thêm [D]: back squat → leg press hoặc split squat; barbell row → row có tựa ngực hoặc cable row ngồi. Khoảng 90% trường hợp đau lưng dưới không có nguyên nhân cấu trúc đơn lẻ rõ ràng [R82], nên mặc định là **tiếp tục vận động có điều chỉnh**, không nghỉ hẳn [R84].

**Gối**

| Mức | Dấu hiệu | Nguồn |
|---|---|---|
| Khám khẩn | Gối rất đau; không cử động được hoặc không chịu được trọng lượng; sưng to hoặc biến dạng; gối **kẹt, sụm, hoặc kêu lục cục kèm đau** (kêu không đau là bình thường); sốt kèm đỏ, nóng quanh gối | [R85] |
| Khám thường | Không cải thiện sau vài tuần | [R85] |

Thay bài: squat → split squat, step-up, lunge; squat xuống hộp để giảm biên độ [R83]. Thêm [D]: giảm độ sâu tạm thời, tempo chậm 3 giây xuống [R82], leg press với biên độ không đau, ưu tiên `HINGE` (RDL, hip thrust) để giữ volume chân; bỏ leg extension nặng nếu gây đau. Bổ sung bài hông (hip thrust, abduction) theo hướng của đồng thuận đau bánh chè–đùi [R90].

**Vai**

| Mức | Dấu hiệu | Nguồn |
|---|---|---|
| Khám khẩn | Đau đột ngột hoặc rất nặng; không cử động được tay; tay/vai biến dạng hoặc sưng to; tê châm chích không hết; mất cảm giác; tay/vai nóng hoặc lạnh bất thường; đau sau chấn thương, té ngã; đau nặng cả hai vai; sốt, mệt | [R86] |
| Khám thường | Đau tăng hoặc không cải thiện sau **2 tuần**; rất khó cử động tay | [R86] |

NHS khuyên: vẫn vận động nhẹ nhàng, **không ngừng hẳn** việc dùng vai, nhưng không làm việc khiến đau tăng và không tự bày bài nặng [R86]. Thay bài: bench tạ đòn → giảm tải (ví dụ 185 xuống 165 lb, tăng rep từ 8 lên 12), kê vật lên ngực để rút ngắn biên độ, tempo 3-1-3, nắm hẹp hơn, hoặc DB press [R83]. Thêm [D]: overhead press → landmine press hoặc incline DB press; lat pulldown sau gáy → kéo trước ngực; dips và upright row → bỏ; thêm `H_PULL` và rear delt.

### 9.7 Luật tổng hợp cho rules engine [D]

```
ON pain_report(area, score, type):
  IF type in {sharp, radiating, numbness, locking, giving_way} OR red_flag(area):
        block(area_slots); show("Đi khám"); STOP
  ELIF score >= 5 OR increasing_across_sets:
        substitute(exercise, same_slot, pain_free=True) ELSE skip_slot
  ELIF score in 3..4:
        load *= 0.8..0.9; RIR += 2; tempo = "3-0-3"; no_progression(exercise)
  log(area, score)

NEXT MORNING check-in:
  IF pain_now > baseline: next_session(area): load *= 0.8, sets -= 1
  IF days_with_pain(area) >= 14 AND no_improvement: recommend_professional(area)

Trở lại: khi 2 buổi liên tiếp <= 2/10 -> tăng lại 5-10% mỗi buổi (R82) đến tải cũ,
         rồi mới bật lại progression.
```

---

## 10. Tóm tắt tham số mặc định (để copy vào config)

| Khóa | Giá trị | Loại |
|---|---|---|
| `volume.novice` (fractional set/nhóm cơ/tuần) | min 4, target 6–10, max 12 | [D] từ R9, R15, R6 |
| `volume.intermediate` | min 6, target 10–16, max 20 | [D] từ R6, R7, R15 |
| `volume.indirect_set_weight` | 0.5 | [S] R7 |
| `volume.min_sets_per_exercise` | 2 | [S] R6 |
| `volume.max_sets_per_muscle_per_session` | 6 (novice), 8–10 (intermediate) | [D] từ R15 |
| `frequency.min_per_muscle` | 2 lần/tuần khi có thể | [D] từ R2, R6 |
| `rir.default_compound` | 2–3 | [S] R6 |
| `rir.min_novice_barbell_no_spotter` | 2 | [D] |
| `rest.compound_sec` | 120–180 (strength 180–300) | [S] R22, R5, R19 |
| `rest.isolation_sec` | 60–90 | [S] R24 |
| `lp.step_lower_kg` | 2.5 (deadlift có thể 5 lúc đầu) | [S] R33 |
| `lp.step_upper_kg` | 2.5 nam; 1.25 nữ nếu có đĩa | [S] R33 |
| `lp.max_step_pct` | 10% (vượt thì dùng double progression) | [D] từ R5 |
| `lp.fail_repeat_before_reset` | 3 buổi | [S] R33 |
| `lp.reset_pct` | −10% | [S] R32, R33, R34 |
| `lp.amrap_double_step_threshold` | > 10 rep | [S] R32, R34 |
| `dp.add_load_when` | mọi set chạm đỉnh rep range | [S] R82, R5 |
| `deload.sets_factor` | 0.5 | [D] từ R42 |
| `deload.rir_min` | 4 | [D] từ R42, R15 |
| `deload.scheduled_for_novice` | false | [D] từ R43 |
| `gap.hold_overdue_days` / `gap.minus10_overdue_days` / `gap.restart_overdue_days` | 4–10 / 11–21 / > 56 (tính theo số ngày **trễ lịch**) | [D] từ R46, R37 |
| `readiness.bands` | GREEN ≥ 11, YELLOW 8–10, RED ≤ 7 (thang 4–20; ngày bình thường = 12) | [D] |
| `readiness.sleep_flag_hours` | ≤ 6 | [S] R53 (ngưỡng định nghĩa thiếu ngủ) |
| `pain.modify_at` / `pain.stop_at` | 3 / 5 | [D] từ R79, R82 |
| `pain.refer_after_days` | 14 | [S] R86 (vai); gối "vài tuần" R85 |
| `cardio.steps` | 7,000 sàn; 8,000–10,000 cho fat loss | [S] R67, R66 |
| `cardio.weekly_min` | 150 phút vừa (WHO); 250+ cho giảm cân rõ | [S] R63, R64 |
| `cardio.order` | tạ trước, cardio sau; tách ≥ 3 giờ nếu được | [S] R32, R69 |

## 11. Những gì chưa xác minh được

| Hạng mục | Tình trạng |
|---|---|
| Số liệu chi tiết của Pelland 2026 (điểm chững theo buổi khoảng 11 fractional set, theo tuần khoảng 31) | [UNVERIFIED]: chỉ thấy trong bản tóm tắt tìm kiếm của preprint; trang preprint chặn truy cập. Con số "~18–20 set/tuần" và "~2–3 set/bài" trong file lấy từ ACSM 2026 trích dẫn lại [R6] |
| RP volume landmarks cho lưng | [UNVERIFIED]: số nằm trong ảnh |
| Jeff Nippard Fundamentals (chi tiết set, RPE) | [UNVERIFIED]: chương trình trả phí, trang sản phẩm trả lỗi 429 |
| Starting Strength: bước tăng cho bench/press, luật reset, khuyến nghị cho nữ | [UNVERIFIED]: startingstrength.com trả lỗi 403; chỉ có trang Barbell Logic [R35]. Bản tóm tắt tìm kiếm nói nữ cần bước 2.5 lb hoặc nhỏ hơn cho press trong vài tuần đầu, chưa đọc được bài gốc |
| NSCA 2-for-2 và bảng mức tăng | Nguồn thứ cấp (tài liệu ôn thi CSCS [R41]), chưa đối chiếu sách NSCA |
| ACSM 2026 infographic (số liệu rút gọn theo mục tiêu) | Trang acsm.org trả lỗi 403; đã dùng full text bài báo thay thế [R6] |
| Coleman 2024: chi tiết thiết kế (set, RIR) | Chỉ đọc abstract [R43] |
| 7 câu hỏi PAR-Q+ nguyên văn | [UNVERIFIED]: xem bản chính thức [R89] |
| Bước nhảy tạ đơn / nấc máy ở phòng gym Việt Nam | [UNVERIFIED]: phải hỏi người dùng |
| WHO: số ngày tập tăng cơ mỗi tuần | Abstract chỉ ghi "regular muscle-strengthening"; tôi không trích được con số ngày, nên không ghi |
| Mọi công thức điểm readiness | Không có nghiên cứu xác thực; toàn bộ là [D] |

---

## References

Các bài PubMed được đọc ở dạng abstract qua NCBI E-utilities, trừ khi ghi "full text".

**Volume, tần suất, tải**

- [R1] Schoenfeld BJ, Ogborn D, Krieger JW. Dose-response relationship between weekly resistance training volume and increases in muscle mass. J Sports Sci 2017. https://pubmed.ncbi.nlm.nih.gov/27433992/
- [R2] Schoenfeld BJ, Ogborn D, Krieger JW. Effects of resistance training frequency on measures of muscle hypertrophy. Sports Med 2016. https://pubmed.ncbi.nlm.nih.gov/27102172/
- [R3] Schoenfeld BJ, Grgic J, Krieger J. How many times per week should a muscle be trained to maximize muscle hypertrophy? J Sports Sci 2019. https://pubmed.ncbi.nlm.nih.gov/30558493/
- [R4] Schoenfeld BJ, Grgic J, Ogborn D, Krieger JW. Strength and hypertrophy adaptations between low- vs. high-load resistance training. J Strength Cond Res 2017. https://pubmed.ncbi.nlm.nih.gov/28834797/
- [R5] ACSM Position Stand. Progression models in resistance training for healthy adults. Med Sci Sports Exerc 2009. https://pubmed.ncbi.nlm.nih.gov/19204579/
- [R6] Currier BS et al. ACSM Position Stand. Resistance training prescription for muscle function, hypertrophy, and physical performance in healthy adults: an overview of reviews. Med Sci Sports Exerc 2026 (full text). https://pubmed.ncbi.nlm.nih.gov/41843416/ và https://pmc.ncbi.nlm.nih.gov/articles/PMC12965823/
- [R7] Pelland JC et al. The resistance training dose response: meta-regressions exploring the effects of weekly volume and frequency on muscle hypertrophy and strength gains. Sports Med 2026. https://pubmed.ncbi.nlm.nih.gov/41343037/
- [R8] Currier BS et al. Resistance training prescription for muscle strength and hypertrophy in healthy adults: Bayesian network meta-analysis. Br J Sports Med 2023. https://pubmed.ncbi.nlm.nih.gov/37414459/
- [R9] Iversen VM, Norum M, Schoenfeld BJ, Fimland MS. No time to lift? Designing time-efficient training programs for strength and hypertrophy. Sports Med 2021 (full text). https://pubmed.ncbi.nlm.nih.gov/34125411/ và https://pmc.ncbi.nlm.nih.gov/articles/PMC8449772/
- [R10] Androulakis-Korakakis P, Fisher JP, Steele J. The minimum effective training dose required to increase 1RM strength. Sports Med 2020. https://pubmed.ncbi.nlm.nih.gov/31797219/
- [R11] Ralston GW et al. The effect of weekly set volume on strength gain: a meta-analysis. Sports Med 2017. https://pubmed.ncbi.nlm.nih.gov/28755103/
- [R12] Grgic J et al. Effect of resistance training frequency on gains in muscular strength. Sports Med 2018. https://pubmed.ncbi.nlm.nih.gov/29470825/
- [R13] Stronger By Science. Training frequency for muscle growth. https://www.strongerbyscience.com/frequency-muscle/
- [R14] Renaissance Periodization. Training volume landmarks for muscle growth. https://rpstrength.com/blogs/articles/training-volume-landmarks-muscle-growth
- [R15] Renaissance Periodization, hướng dẫn theo nhóm cơ (hub: https://rpstrength.com/hypertrophy-training-guide-central-hub/):
  - Ngực: https://rpstrength.com/blogs/articles/chest-hypertrophy-training-tips
  - Lưng: https://rpstrength.com/blogs/articles/back-hypertrophy-training-tips
  - Quads: https://rpstrength.com/blogs/articles/quad-hypertrophy-training-tips
  - Hamstrings: https://rpstrength.com/blogs/articles/hamstring-hypertrophy-training-tips
  - Glutes: https://rpstrength.com/blogs/articles/glute-hypertrophy-training-tips
  - Side delts: https://rpstrength.com/blogs/articles/side-delt-hypertrophy-training-tips
  - Biceps: https://rpstrength.com/blogs/articles/bicep-hypertrophy-training-tips
  - Triceps: https://rpstrength.com/blogs/articles/triceps-hypertrophy-training-tips
  - Calves: https://rpstrength.com/blogs/articles/calves-hypertrophy-training-tips
  - Abs: https://rpstrength.com/blogs/articles/ab-hypertrophy-training-tips
- [R16] Baz-Valle E et al. Total number of sets as a training volume quantification method for muscle hypertrophy. J Strength Cond Res 2021. https://pubmed.ncbi.nlm.nih.gov/30063555/

**Proximity to failure, RPE/RIR, nghỉ giữa set**

- [R17] Refalo MC et al. Influence of resistance training proximity-to-failure on skeletal muscle hypertrophy. Sports Med 2023. https://pubmed.ncbi.nlm.nih.gov/36334240/
- [R18] Robinson ZP et al. Exploring the dose-response relationship between estimated resistance training proximity to failure, strength gain, and muscle hypertrophy. Sports Med 2024. https://pubmed.ncbi.nlm.nih.gov/38970765/
- [R19] Helms ER, Cronin J, Storey A, Zourdos MC. Application of the repetitions in reserve-based rating of perceived exertion scale for resistance training. Strength Cond J 2016 (full text). https://pubmed.ncbi.nlm.nih.gov/27531969/ và https://pmc.ncbi.nlm.nih.gov/articles/PMC4961270/
- [R20] Zourdos MC et al. Novel resistance training-specific rating of perceived exertion scale measuring repetitions in reserve. J Strength Cond Res 2016. https://pubmed.ncbi.nlm.nih.gov/26049792/
- [R21] Halperin I et al. Accuracy in predicting repetitions to task failure in resistance exercise. Sports Med 2022. https://pubmed.ncbi.nlm.nih.gov/34542869/
- [R22] Schoenfeld BJ et al. Longer interset rest periods enhance muscle strength and hypertrophy in resistance-trained men. J Strength Cond Res 2016. https://pubmed.ncbi.nlm.nih.gov/26605807/
- [R23] Grgic J et al. The effects of short versus long inter-set rest intervals in resistance training on measures of muscle hypertrophy. Eur J Sport Sci 2017. https://pubmed.ncbi.nlm.nih.gov/28641044/
- [R24] Singer A et al. Give it a rest: Bayesian meta-analysis on inter-set rest interval duration and muscle hypertrophy. Front Sports Act Living 2024 (full text). https://pubmed.ncbi.nlm.nih.gov/39205815/
- [R25] Schoenfeld BJ et al. Loading recommendations for muscle strength, hypertrophy, and local endurance: a re-examination of the repetition continuum. Sports 2021. https://pubmed.ncbi.nlm.nih.gov/33671664/

**Khác biệt giới**

- [R26] Roberts BM, Nuckols G, Krieger JW. Sex differences in resistance training. J Strength Cond Res 2020. https://pubmed.ncbi.nlm.nih.gov/32218059/
- [R27] Refalo MC et al. Sex differences in absolute and relative changes in muscle size following resistance training. PeerJ 2025. https://pubmed.ncbi.nlm.nih.gov/40028215/
- [R28] Hagstrom AD et al. The effect of resistance training in women on dynamic strength and muscular hypertrophy. Sports Med 2020. https://pubmed.ncbi.nlm.nih.gov/31820374/
- [R29] Colenso-Semple LM et al. Current evidence shows no influence of women's menstrual cycle phase on acute strength performance or adaptations to resistance exercise training. Front Sports Act Living 2023. https://pubmed.ncbi.nlm.nih.gov/37033884/
- [R30] Stronger By Science. Strength training for women. https://www.strongerbyscience.com/strength-training-women/

**Chương trình beginner và progression**

- [R31] GZCLP. The Fitness Wiki. https://thefitness.wiki/routines/gzclp/
- [R32] r/Fitness Basic Beginner Routine. The Fitness Wiki. https://thefitness.wiki/routines/r-fitness-basic-beginner-routine/
- [R33] StrongLifts 5×5: progress https://stronglifts.com/stronglifts-5x5/progress/ và failure https://stronglifts.com/stronglifts-5x5/failure/
- [R34] Phrak's Greyskull LP. Liftosaur. https://www.liftosaur.com/programs/phrakgreyskull
- [R35] Starting Strength novice linear progression (bản mô tả của Barbell Logic). https://barbell-logic.com/starting-strength-novice-linear-progression/
- [R36] Recommended routines. The Fitness Wiki. https://thefitness.wiki/routines/strength-training-muscle-building/
- [R37] Nippard J. How to get your gains back after a training break. https://jeffnippard.com/blogs/news/how-to-get-your-gains-back-after-a-training-break
- [R38] Nippard J. Fundamentals Hypertrophy Program (trang sản phẩm; không truy cập trực tiếp được). https://jeffnippard.com/products/fundamentals-hypertrophy-program
- [R39] Plotkin D et al. Progressive overload without progressing load? PeerJ 2022. https://pubmed.ncbi.nlm.nih.gov/36199287/
- [R40] Chaves TS et al. Effects of resistance training overload progression protocols on strength and muscle mass. Int J Sports Med 2024. https://pubmed.ncbi.nlm.nih.gov/38286426/
- [R41] Achievable CSCS study guide: training load and repetitions (2-for-2 rule; nguồn thứ cấp của NSCA). https://app.achievable.me/study/cscs/learn/program-design-for-resistance-training-training-frequency-exercise-order-and-training-load-and-repetitions

**Deload, nghỉ tập, detraining**

- [R42] Bell L et al. Integrating deloading into strength and physique sports training programmes: an international Delphi consensus approach. Sports Med Open 2023 (full text). https://pubmed.ncbi.nlm.nih.gov/37730925/ và https://pmc.ncbi.nlm.nih.gov/articles/PMC10511399/
- [R43] Coleman M et al. Gaining more from doing less? The effects of a one-week deload period during supervised resistance training on muscular adaptations. PeerJ 2024. https://pubmed.ncbi.nlm.nih.gov/38274324/
- [R44] Ogasawara R et al. Comparison of muscle hypertrophy following 6-month of continuous and periodic strength training. Eur J Appl Physiol 2013. https://pubmed.ncbi.nlm.nih.gov/23053130/
- [R45] Halonen EJ et al. Does taking a break matter: adaptations in muscle strength and size between continuous and periodic resistance training. Scand J Med Sci Sports 2024. https://pubmed.ncbi.nlm.nih.gov/39364857/
- [R46] McMaster DT et al. The development, retention and decay rates of strength and power in elite rugby union, rugby league and American football. Sports Med 2013. https://pubmed.ncbi.nlm.nih.gov/23529287/
- [R47] Bickel CS, Cross JM, Bamman MM. Exercise dosing to retain resistance training adaptations in young and older adults. Med Sci Sports Exerc 2011. https://pubmed.ncbi.nlm.nih.gov/21131862/

**Autoregulation và readiness**

- [R48] Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures. Br J Sports Med 2016. https://pubmed.ncbi.nlm.nih.gov/26423706/
- [R49] Laurent CM et al. A practical approach to monitoring recovery: development of a perceived recovery status scale. J Strength Cond Res 2011. https://pubmed.ncbi.nlm.nih.gov/20581704/
- [R50] McNamara JM, Stearne DJ. Flexible nonlinear periodization in a beginner college weight training class. J Strength Cond Res 2010. https://pubmed.ncbi.nlm.nih.gov/20042923/
- [R51] Helms ER et al. RPE vs. percentage 1RM loading in periodized programs matched for sets and repetitions. Front Physiol 2018. https://pubmed.ncbi.nlm.nih.gov/29628895/
- [R52] Hickmott LM et al. The effect of load and volume autoregulation on muscular strength and hypertrophy. Sports Med Open 2022. https://pubmed.ncbi.nlm.nih.gov/35038063/
- [R53] Craven J et al. Effects of acute sleep loss on physical performance: a systematic and meta-analytical review. Sports Med 2022. https://pubmed.ncbi.nlm.nih.gov/35708888/
- [R54] Knowles OE et al. Inadequate sleep and muscle strength: implications for resistance training. J Sci Med Sport 2018. https://pubmed.ncbi.nlm.nih.gov/29422383/
- [R55] Bartholomew JB et al. Strength gains after resistance training: the effect of stressful, negative life events. J Strength Cond Res 2008. https://pubmed.ncbi.nlm.nih.gov/18545186/
- [R56] Stults-Kolehmainen MA et al. Chronic psychological stress impairs recovery of muscular function and somatic sensations over a 96-hour period. J Strength Cond Res 2014. https://pubmed.ncbi.nlm.nih.gov/24343323/
- [R57] Morán-Navarro R et al. Time course of recovery following resistance training leading or not to failure. Eur J Appl Physiol 2017. https://pubmed.ncbi.nlm.nih.gov/28965198/

**Warm-up**

- [R58] Ribeiro AS et al. Effect of different warm-up procedures on the performance of resistance training exercises. Percept Mot Skills 2014. https://pubmed.ncbi.nlm.nih.gov/25153744/
- [R59] McCrary JM, Ackermann BJ, Halaki M. A systematic review of the effects of upper body warm-up on performance and injury. Br J Sports Med 2015. https://pubmed.ncbi.nlm.nih.gov/25694615/
- [R60] Fradkin AJ, Zazryn TR, Smoliga JM. Effects of warming-up on physical performance: a systematic review with meta-analysis. J Strength Cond Res 2010. https://pubmed.ncbi.nlm.nih.gov/19996770/
- [R61] Hevy. Warm-up sets. https://www.hevyapp.com/warm-up-sets/
- [R62] Barbell Logic. Why and how to warm up. https://barbell-logic.com/building-better-practices-why-and-how-to-warm-up/

**Cardio, số bước, concurrent training, giảm cân**

- [R63] Bull FC et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. Br J Sports Med 2020. https://pubmed.ncbi.nlm.nih.gov/33239350/
- [R64] Donnelly JE et al. ACSM Position Stand. Appropriate physical activity intervention strategies for weight loss and prevention of weight regain for adults. Med Sci Sports Exerc 2009. https://pubmed.ncbi.nlm.nih.gov/19127177/
- [R65] Jayedi A et al. Aerobic exercise and weight loss in adults: a systematic review and dose-response meta-analysis. JAMA Netw Open 2024. https://pubmed.ncbi.nlm.nih.gov/39724371/
- [R66] Paluch AE et al. Daily steps and all-cause mortality: a meta-analysis of 15 international cohorts. Lancet Public Health 2022. https://pubmed.ncbi.nlm.nih.gov/35247352/
- [R67] Ding D et al. Daily steps and health outcomes in adults: a systematic review and dose-response meta-analysis. Lancet Public Health 2025. https://pubmed.ncbi.nlm.nih.gov/40713949/
- [R68] Wewege M et al. The effects of high-intensity interval training vs. moderate-intensity continuous training on body composition in overweight and obese adults. Obes Rev 2017. https://pubmed.ncbi.nlm.nih.gov/28401638/
- [R69] Schumann M et al. Compatibility of concurrent aerobic and strength training for skeletal muscle size and function: an updated systematic review and meta-analysis. Sports Med 2022. https://pubmed.ncbi.nlm.nih.gov/34757594/
- [R70] Petré H et al. Development of maximal dynamic strength during concurrent resistance and endurance training in untrained, moderately trained, and trained individuals. Sports Med 2021. https://pubmed.ncbi.nlm.nih.gov/33751469/
- [R71] Sabag A et al. The compatibility of concurrent high intensity interval training and resistance training for muscular strength and hypertrophy. J Sports Sci 2018. https://pubmed.ncbi.nlm.nih.gov/29658408/
- [R72] Wilson JM et al. Concurrent training: a meta-analysis examining interference of aerobic and resistance exercises. J Strength Cond Res 2012. https://pubmed.ncbi.nlm.nih.gov/22002517/
- [R73] Murach KA, Bagley JR. Skeletal muscle hypertrophy with concurrent exercise training: contrary evidence for an interference effect. Sports Med 2016. https://pubmed.ncbi.nlm.nih.gov/26932769/
- [R74] Murphy C, Koehler K. Energy deficiency impairs resistance training gains in lean mass but not strength. Scand J Med Sci Sports 2022. https://pubmed.ncbi.nlm.nih.gov/34623696/
- [R75] Garthe I et al. Effect of two different weight-loss rates on body composition and strength and power-related performance in elite athletes. Int J Sport Nutr Exerc Metab 2011. https://pubmed.ncbi.nlm.nih.gov/21558571/
- [R76] Zhang X et al. Superset versus traditional resistance training prescriptions: a systematic review and meta-analysis. Sports Med 2025. https://pubmed.ncbi.nlm.nih.gov/39903375/

**An toàn và đau**

- [R77] Keogh JW, Winwood PW. The epidemiology of injuries across the weight-training sports. Sports Med 2017. https://pubmed.ncbi.nlm.nih.gov/27328853/
- [R78] Aasa U et al. Injuries among weightlifters and powerlifters: a systematic review. Br J Sports Med 2017. https://pubmed.ncbi.nlm.nih.gov/27707741/
- [R79] Smith BE et al. Should exercises be painful in the management of chronic musculoskeletal pain? Br J Sports Med 2017 (full text, bảng mô tả các thử nghiệm). https://pubmed.ncbi.nlm.nih.gov/28596288/ và https://pmc.ncbi.nlm.nih.gov/articles/PMC5739826/
- [R80] Silbernagel KG et al. Continued sports activity, using a pain-monitoring model, during rehabilitation in patients with Achilles tendinopathy. Am J Sports Med 2007. https://pubmed.ncbi.nlm.nih.gov/17307888/
- [R81] Thomeé R. A comprehensive treatment approach for patellofemoral pain syndrome in young women. Phys Ther 1997. https://pubmed.ncbi.nlm.nih.gov/9413448/
- [R82] Barbell Medicine. Lifting rehab mistakes. https://www.barbellmedicine.com/blog/lifting-rehab-mistakes/
- [R83] E3 Rehab. How to train around pain or injuries. https://e3rehab.com/blog/how-to-train-around-pain-or-injuries/
- [R84] NHS. Back pain. https://www.nhs.uk/conditions/back-pain/
- [R85] NHS. Knee pain. https://www.nhs.uk/conditions/knee-pain/
- [R86] NHS. Shoulder pain. https://www.nhs.uk/conditions/shoulder-pain/
- [R87] NHS. Chest pain. https://www.nhs.uk/conditions/chest-pain/
- [R88] Riebe D et al. Updating ACSM's recommendations for exercise preparticipation health screening. Med Sci Sports Exerc 2015. https://pubmed.ncbi.nlm.nih.gov/26473759/
- [R89] PAR-Q+ (bản chính thức). https://eparmedx.com/
- [R90] Collins NJ et al. 2018 Consensus statement on exercise therapy and physical interventions to treat patellofemoral pain. Br J Sports Med 2018. https://pubmed.ncbi.nlm.nih.gov/29925502/
