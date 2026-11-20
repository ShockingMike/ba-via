# 00 — Kế hoạch app tập gym (bản nháp để duyệt)

> Tổng hợp từ 3 file nghiên cứu: [01-programming.md](01-programming.md), [02-exercise-library.md](02-exercise-library.md) + [exercises.json](exercises.json), [03-app-patterns.md](03-app-patterns.md).
> Nhãn giữ nguyên như trong file nghiên cứu: **[S]** = có nguồn, **[D]** = mặc định thiết kế (hợp lý nhưng chưa có nghiên cứu xác thực), **[U]** = chưa kiểm chứng.

## 1. App là gì

Một **huấn luyện viên bỏ túi** cho một nhóm nhỏ bạn bè (khoảng 2–10 người). Mỗi người dùng trên điện thoại của mình, với hồ sơ riêng.

Mỗi ngày đến phòng tập, người dùng **check-in khoảng 10 giây**. App ra **buổi tập của hôm đó**, đã tính đến kế hoạch tuần, tình trạng cơ thể, thời gian có được và những dụng cụ hôm nay dùng được. Người dùng ghi từng set, app tự tăng tạ cho buổi sau. Có streak theo tuần và thử thách nhóm để giữ động lực.

## 2. Dòng chảy một ngày tập

```
Mở app → Check-in (hoặc nút "Như mọi khi")
   1. Hôm nay thấy thế nào?    rất tệ / mệt / bình thường / sung
   2. Đêm qua ngủ ít (≤ 6 tiếng)?   chip bật/tắt
   3. Có bao nhiêu thời gian?  30 / 45 / 60 / 75 / 90 phút   (mặc định: lần trước)
   4. Hôm nay thiếu dụng cụ gì?  chip bật tắt theo hồ sơ phòng tập (mặc định: không thiếu gì)
   (ẩn, tuỳ chọn) Đau chỗ nào?  gối / lưng dưới / vai / cổ tay → bật luật đau (mục 3.8)
 → App sinh buổi tập
 → Tập: mỗi bài có [✓ set] [Để sau] [Đổi bài] [Xem hướng dẫn]
 → Kết thúc: 1 câu "nhẹ / vừa / quá sức" (bỏ qua được) → tính tạ cho lần sau, cập nhật streak, tạo thẻ chia sẻ
```

Ngày bình thường người dùng chỉ cần bấm "Như mọi khi" hoặc chạm 1–2 lần. "Thiếu dụng cụ hôm nay" chỉ lưu cho **buổi tập đó**, không ghi đè hồ sơ phòng tập. Đây là bài học từ các phàn nàn về Fitbod.

## 3. Bộ máy ra bài (rules engine)

### 3.1 Hồ sơ người dùng (onboarding một lần)
- Giới tính, tuổi, cân nặng; trình độ (mới / đã tập); mục tiêu (giảm mỡ / tăng cơ / sức mạnh / khoẻ tổng quát)
- Số buổi/tuần (2–6) và thời lượng mặc định mỗi buổi
- Vùng hay đau hoặc chấn thương cũ
- Bảng câu hỏi sàng lọc sức khoẻ trước khi tập (PAR-Q+); nếu có câu trả lời "có" thì khuyên hỏi bác sĩ trước [S]
- **Dụng cụ cá nhân** (ví dụ dây kháng lực mang theo): luôn được coi là có sẵn, bất kể phòng tập

### 3.2 Khung tuần theo ô chuyển động, không gắn cứng tên bài [D]
| Buổi/tuần | Khung | Ghi chú |
|---|---|---|
| 2 | Full Body A/B | Đủ cho người mới |
| 3 | Full Body A/B/A, tuần sau B/A/B | **Mặc định cho người mới** |
| 4 | Upper/Lower × 2 | Sau 3–6 tháng, hoặc người đã tập |
| 5–6 | Upper/Lower/PPL | Người mới chọn 5–6 thì app gợi ý 3–4 buổi tạ, các ngày còn lại đi bộ/cardio [S: ACSM khuyên người mới tập 2–3 ngày] |

Mỗi buổi là một danh sách ô như `SQUAT 3×…`, `H_PUSH 3×…`. Đến lúc tập, app mới chọn **bài cụ thể** cho từng ô (mục 3.3).

### 3.3 Từ ô sang bài cụ thể

**Bảng nối ô → nhóm bài trong `exercises.json`** (dùng `pattern`; khi cần thì lọc thêm theo `primary`):

| Ô trong khung | Lấy từ pattern | Lọc thêm |
|---|---|---|
| `SQUAT` | squat | — |
| `HINGE` | hinge | — |
| `HINGE_LIGHT` | glutes + hinge | ưu tiên hip thrust / RDL tạ đơn |
| `SL_LEG` | lunge | — |
| `H_PUSH` / `V_PUSH` | push_horizontal / push_vertical | — |
| `H_PULL` / `V_PULL` | pull_horizontal / pull_vertical | — |
| `ISO_leg_curl` | hinge + glutes | `primary` có hamstrings |
| `ISO_leg_ext` | squat + lunge | `primary` có quads, ưu tiên bài đơn khớp |
| `ISO_biceps` / `ISO_triceps` / `ISO_side_delt` / `ISO_rear_delt` / `ISO_calves` | biceps / triceps / lateral_delt / rear_delt / calves | — |
| `ISO_core` | core | xoay vòng giữa anti-extension, anti-rotation và flexion |
| `CARRY` (tuỳ chọn, cho giảm mỡ hoặc khoẻ tổng quát) | carry | — |

**Thuật toán chọn bài:**
1. Lấy các bài thuộc ô đó.
2. Bỏ bài cần dụng cụ mà phòng không có, hôm nay không dùng được, hoặc không phải dụng cụ cá nhân. Bài không cần dụng cụ (`none`) luôn được giữ.
3. Người mới: bỏ bài có `beginner_ok: false`.
4. Có vùng đau (khai trong hồ sơ hoặc check-in): ưu tiên `safer_alternative` của bài đó; nếu không có thì bỏ bài có `avoid_if` khớp vùng đau.
5. **Ưu tiên bài đã tập lần trước** để có số liệu so sánh và tăng tạ; nếu chưa có thì lấy bài đầu tiên theo thứ tự tạ đòn → tạ đơn → máy → dây → không dụng cụ.
6. Nút **Đổi bài** hiện 3–4 lựa chọn kế tiếp. Mặc định chỉ đổi cho hôm nay; có thêm nút "luôn dùng bài này".

**Kiểm tra độ phủ (chạy script trên `exercises.json`, tính cả khi thiếu nhiều dụng cụ cùng lúc):**

| Tình huống | Ô bị trống |
|---|---|
| Chỉ tập không dụng cụ | Kéo dọc, tay trước, vai giữa; thêm một số ô khi có vùng đau |
| Không dụng cụ + **1 dây kháng lực** | Chỉ còn các ô dính vùng đau: squat/lunge khi đau gối, hinge khi đau lưng dưới, đẩy dọc khi đau vai, carry khi đau vai hoặc cổ tay |
| Dây + tạ đơn + ghế phẳng | Chỉ còn: squat/lunge khi đau gối, hinge khi đau lưng dưới, đẩy dọc khi đau vai |

→ **Khuyến nghị:** mỗi người mua một bộ dây kháng lực (rẻ, mang theo được) và khai là dụng cụ cá nhân. Như vậy, nếu không có vùng đau, ô nào cũng luôn có bài.

**Khi một ô vẫn trống** [D]:
- Ô bài đơn khớp: bỏ ô đó; nếu nhóm cơ rơi dưới sàn volume thì báo nhẹ.
- Ô bài chính trống vì vùng đau: không ép một bài khác cùng kiểu. App chạy luật đau (mục 3.8): bài biên độ ngắn hoặc tạ nhẹ để thử, nếu vẫn đau thì bỏ ô và chuyển set sang nhóm cơ khác.
- Ô bài chính trống vì thiếu dụng cụ: mượn pattern gần nhất (squat ↔ lunge, hinge ↔ glutes, kéo dọc ↔ kéo ngang), rồi báo cho người dùng biết.

### 3.4 Thông số theo mục tiêu
| | Giảm mỡ | Tăng cơ | Sức mạnh | Khoẻ tổng quát |
|---|---|---|---|---|
| Rep bài chính | 6–10 [D] | 6–10 [D] | 3–6 [S]; người mới 5–8 [D] | 8–12 [S] |
| Rep bài phụ | 10–15 [D] | 10–20 [S] | 8–12 [D] | 10–15 [D] |
| RIR bài chính | 2–3 [S] | 1–3 [S] | 2–3 [S] | 2–3 [S] |
| Nghỉ bài chính | 2 phút [D] | 2–3 phút [S] | 3–5 phút [S] | 2 phút [S] |

**Thứ tự ưu tiên khi các luật mâu thuẫn:** giai đoạn học kỹ thuật > bảng mục tiêu > số rep ghi trong khung tuần.
- **Giai đoạn học kỹ thuật** (người mới, 4 tuần đầu, chỉnh được 4–8 tuần) [D]: mọi bài 8–12 rep, RIR 2–3, 2–3 set, tăng tạ kiểu double progression. Cơ sở: ACSM khuyên người mới tập 8–12RM [S]; độ dài 4–8 tuần là mặc định thiết kế.
- **Volume** [D]: người mới 6–10 set/nhóm cơ/tuần (sàn 4, trần 12); đã tập 10–16. Set gián tiếp tính 0,5 [S]. App **tự đếm lại volume sau mỗi lần đổi hoặc cắt bài**, và báo khi một nhóm cơ rơi dưới sàn (có trong MVP vì bộ máy cần để cắt bài).
- **Giảm mỡ** [D]: không hạ tạ; nếu cần thì bớt set, mục tiêu là giữ sức mạnh.
- **Nữ** [S]: giáo án giống nam; bước tăng tạ thân trên nhỏ hơn (1,25 kg nếu phòng có đĩa nhỏ). Chưa có luật nào theo chu kỳ kinh nguyệt vì bằng chứng chưa đủ.
- **Người mới, tạ đòn, không có người đỡ:** RIR tối thiểu là 2 cho squat và đẩy ngực tạ đòn [D].

### 3.5 Cắt theo thời gian [D]
| Thời gian | Số set cả buổi | Cách cắt |
|---|---|---|
| 30 phút | ~8 | 3 bài chính × 2–3 set, bỏ khởi động chung |
| 45 phút | ~11–13 | Giữ bài 1–4, ghép bài 5–6 thành superset hoặc bỏ |
| 60 phút | ~16–18 | Theo khung |
| 75 phút | ~20–22 | Thêm 1–2 bài đơn khớp |
| 90 phút | ~24–26 | Thêm bài tay và bắp chân, nâng bài phụ lên 3 set |

Không bao giờ vượt trần số set/nhóm cơ/buổi (người mới 6) [D].

### 3.6 Check-in → điều chỉnh buổi [D]
| Vùng | Khi nào | Điều chỉnh |
|---|---|---|
| 🟢 Xanh | bình thường / sung | Theo kế hoạch, được tăng tạ |
| 🟡 Vàng | chọn "mệt", **hoặc** bật chip "ngủ ≤ 6 tiếng" | Bớt 1 set ở bài có ≥ 3 set (không bài nào dưới 2 set); giữ tạ, không tăng; RIR +1; buổi hụt rep không tính là fail |
| 🔴 Đỏ | chọn "rất tệ", **hoặc** vàng + ngủ ≤ 6 tiếng **2 đêm liên tiếp** (hạ thêm 1 bậc [S]) | Giảm 50% set, chỉ giữ 3 bài chính, tạ −10%; hoặc đổi sang đi bộ 20–30 phút |
| Nghỉ | ốm có sốt | Khuyên nghỉ, tuần đó tính là "nghỉ có phép" |

- Ngưỡng ngủ 6 tiếng có nguồn [S]. Mức −10% dựa trên một nghiên cứu cho thấy thiếu ngủ làm giảm khoảng 7,6% hiệu suất [S]. Các con số còn lại là [D]; chưa có nghiên cứu nào xác thực một công thức điểm sẵn sàng.
- **Số liệu trong buổi đáng tin hơn cảm giác** [D]: nếu set đầu của bài chính hụt từ 2 rep trở lên so với lần trước cùng mức tạ, app hạ tạ 5–10% cho các set còn lại và hạ cả buổi một bậc. Ngược lại, ngày vàng mà làm dư từ 2 rep và còn RIR ≥ 3 thì nâng lại lên xanh. Người mới hay đoán sai RIR khoảng 1 rep [S], nên số rep thực tế đáng tin hơn điểm cảm giác.
- **Chống lạm dụng** [D]: nếu hơn 50% số buổi trong 3 tuần là vàng hoặc đỏ, app ngừng giảm tiếp và gợi ý xem lại giấc ngủ, ăn uống, hoặc bớt số buổi trong tuần.

### 3.7 Tăng tạ
**Thuật toán nào áp dụng cho bài nào** [D, dựng từ các chương trình có nguồn]:

| Trường hợp | Thuật toán |
|---|---|
| Người mới, giai đoạn học kỹ thuật, mọi bài | **Double progression**, 8–12 rep |
| Người mới sau giai đoạn đó: bài #1 và #2 của buổi, nếu là bài nhiều khớp dùng **tạ đòn hoặc máy có nấc nhỏ**, và mỗi bước tăng ≤ 10% mức đang tập | **Tăng tuyến tính (LP)** |
| Bài chính rơi vào tạ đơn, máy, dây, hoặc mọi bài còn lại; mọi bài của người đã tập | **Double progression** |
| Bước tăng tạ > 10% mức đang tập (ví dụ tạ đơn 7,5 kg nhảy lên 10 kg) | **Nới khoảng rep** (ví dụ 8–15, 8–20) trước khi tăng tạ |
| Bài không tạ (chống đẩy, plank…) | Tăng rep hoặc giây đến đỉnh khoảng, rồi chuyển sang **biến thể khó hơn trong danh sách thay thế** (ví dụ chống đẩy nghiêng → chống đẩy thường) |
| Bài tính theo thời gian | +5–10 giây mỗi lần đạt mục tiêu [D] |

**Chi tiết:**
- **LP:** đủ rep thì buổi sau +2,5 kg (nữ +1,25 kg cho thân trên nếu có đĩa) [S: StrongLifts]. Set cuối làm quá 10 rep thì tăng gấp đôi bước [S: r/Fitness BBR, Greyskull]. Hụt rep thì giữ tạ; hụt 3 buổi liền thì giảm 10% [S: StrongLifts; BBR và Greyskull cũng giảm 10% khi fail]. Bị giảm 10% hai lần trong 8 tuần, hoặc chạy LP quá 3 tháng, thì chuyển sang double progression [D, theo BBR].
- **Double progression:** mọi set chạm đỉnh khoảng rep thì tăng một bước tạ và quay về đáy khoảng rep [S: Barbell Medicine, ACSM]. Bài thân trên của nữ, hoặc khi bước tăng > 5%, cần đạt 2 buổi liền mới tăng [D].
- **Buổi hụt rep vì ngày vàng/đỏ hoặc vì đau:** không tính là fail [D].
- **Bước tạ là cài đặt của từng phòng tập:** thanh đòn nặng bao nhiêu (nhiều phòng dùng thanh 10–15 kg), đĩa nhỏ nhất, tạ đơn nhảy mấy kg, máy mỗi nấc bao nhiêu. Lần đầu dùng mỗi dụng cụ, app hỏi người dùng [U: chưa có số liệu cho phòng tập Việt Nam].
- **Deload** [D]: người mới không deload theo lịch, chỉ deload khi chững lại. Cơ sở: một thử nghiệm cho thấy nghỉ hẳn 1 tuần không giúp gì thêm [S, mới đọc abstract]. Khi deload: số set ×0,5, RIR ≥ 4.
- **Nghỉ lâu** (tính theo số ngày trễ lịch) [D]: trễ 4–10 ngày thì giữ tạ; 11–21 ngày thì −10%; hơn 56 ngày thì làm lại giai đoạn học kỹ thuật.

### 3.8 An toàn
- **Luật đau** [D, thận trọng hơn các thử nghiệm phục hồi chức năng có giám sát]: đau 3/10 thì đổi bài hoặc giảm biên độ; 5/10 thì dừng bài đó. Đau kéo dài quá 14 ngày thì khuyên đi khám [S cho vai].
- **Dấu hiệu phải dừng buổi ngay:**
  - Đau ngực kiểu bóp nghẹt, đau lan ra tay, cổ hoặc hàm, kèm vã mồ hôi hoặc khó thở → **gọi 115** [S: NHS; số 115 là U].
  - Chóng mặt, sắp ngất, tim đập loạn → dừng [D].
  - Nghe "rắc", sưng nhanh, biến dạng khớp → dừng và đi khám [D, khớp với NHS].
- **Khởi động** [D, theo Hevy và Barbell Logic]:
  - Bài chính đầu buổi: thanh đòn trống ×10, 50% ×5, 75% ×3; thêm 90% ×1 nếu mục tiêu ≤ 5 rep.
  - Bài sau, khác nhóm cơ: 50% ×5, 75% ×3.
  - Bài đơn khớp: 1 set nhẹ hoặc bỏ.
  - Đi bộ hoặc đạp xe 3–5 phút là **tuỳ chọn**, bỏ khi buổi ≤ 45 phút.
  - Set khởi động không tính vào volume.
- **Cardio** [S]: tập tạ trước, cardio sau. 7.000 bước/ngày là sàn; giảm mỡ thì 8.000–10.000. 150 phút/tuần cường độ vừa theo WHO. Với người mới, cardio gần như không làm chậm tiến bộ tập tạ.

## 4. Động lực và bạn bè

| Tính năng | Cần đồng bộ? | Đề xuất |
|---|---|---|
| **Streak theo tuần:** đạt khi tập ≥ N buổi (N tự chọn); một buổi ngắn lúc mệt vẫn tính; tập quá N không được thêm điểm; ngày nghỉ không bao giờ bị phạt | Không | MVP |
| **Tuần nghỉ có phép** (ốm, đi xa): tích 1 phép sau mỗi 4 tuần đạt, giữ tối đa 2 [U: con số cần thử]. Tuần deload vẫn tính là đạt | Không | MVP |
| Huy hiệu mốc thật: buổi thứ 10/50/100, PR đầu tiên, 4/12/26 tuần đạt | Không | MVP |
| **Thẻ tổng kết buổi tập** dạng ảnh, chia sẻ vào nhóm Zalo/Messenger | Không | MVP |
| Bảng nhóm: ai đạt mấy/mấy buổi, xếp theo % mục tiêu **của riêng mỗi người** | Có | **MVP (Q3)** |
| Feed hoạt động + thả cổ vũ (kudos) | Có | **MVP (Q3)** |
| **Streak nhóm** / thử thách tuần chung (ví dụ "cả nhóm 20 buổi tuần này") | Có | **MVP (Q3)** |
| Chọc bạn chưa tập (cần push), thi đấu 1-1 trong 7 ngày | Có + push | GĐ 2 |
| XP / league thăng hạng kiểu Duolingo | Có | Không khuyên dùng cho nhóm ≤ 10 người |

Nguyên tắc chung:
- **Xếp hạng theo mức độ đều đặn so với mục tiêu của chính mình**, không so tạ. Như vậy người tập 2 buổi và người tập 5 buổi/tuần cạnh tranh công bằng.
- Streak chỉ đo việc **có đến tập**, không gắn với mức tạ.
- Cân nặng và số đo luôn riêng tư.
- Bằng chứng: Duolingo cho thấy đặt ngưỡng giữ streak thấp thì người dùng ở lại lâu hơn (A/B test của họ). Kudos trong nhóm nhỏ có bằng chứng tích cực. Chưa có nghiên cứu nào tách riêng hiệu quả của XP hay huy hiệu.

## 5. Kỹ thuật

- **PWA** (giống ExpenseApp/PTQuiz): cài lên màn hình chính, chạy được trên cả iPhone và Android, host trên Netlify.
- **Offline hoàn toàn cho một người:** dữ liệu lưu trong IndexedDB. **Xuất/nhập JSON và nhắc sao lưu định kỳ có ngay trong MVP**, vì iOS có thể tự xoá dữ liệu của web app.
- **Đồng bộ nhóm:** Firebase Firestore gói miễn phí, vào nhóm bằng **mã nhóm**. Chỉ đẩy lên bản tóm tắt tuần, sự kiện feed và cổ vũ; nhật ký tập chi tiết vẫn nằm trên máy. Mất mạng thì bảng nhóm hiện dữ liệu lần cuối.
- **Thiết kế dữ liệu sẵn cho đồng bộ ngay từ đầu:** ID dạng UUID, mỗi bản ghi có `profileId` và `updatedAt`, xoá mềm, log chỉ ghi thêm. Nhờ vậy, thêm đồng bộ sau này không phải viết lại.
- Hồ sơ phòng tập (danh sách dụng cụ + bước tạ) chia sẻ được qua file hoặc QR, để bạn tập cùng phòng không phải nhập lại.

## 6. MVP (đề xuất)

1. Onboarding hồ sơ + sàng lọc sức khoẻ + dụng cụ cá nhân
2. Hồ sơ phòng tập: checklist dụng cụ + bước tạ (chia sẻ được)
3. Check-in → sinh buổi tập: khung tuần, chọn bài theo dụng cụ và vùng đau, cắt theo thời gian, điều chỉnh theo vùng, **đếm volume**
4. Màn hình tập: điền sẵn mục tiêu, ✓ một chạm, +/− theo bước tạ, đồng hồ nghỉ, hiện số lần trước, set khởi động, Để sau, Đổi bài, hướng dẫn kỹ thuật dạng chữ
5. Tăng tạ tự động (cả 3 thuật toán ở mục 3.7) + lịch sử + PR + biểu đồ theo từng bài + cân nặng
6. Streak tuần + phép nghỉ + huy hiệu + thẻ chia sẻ
7. Xuất/nhập dữ liệu + nhắc sao lưu
8. **Nhóm (đã chốt Q3):** tạo nhóm hoặc vào nhóm bằng mã, bảng tuần theo % mục tiêu riêng, streak nhóm, thử thách tuần, feed + cổ vũ, chia sẻ hồ sơ phòng tập
9. **Clip động tác bằng SVG (đã chốt Q4)**, mỗi pattern một bộ khung
10. Nhiều hồ sơ phòng tập cho mỗi người (đã chốt Q2)

Giai đoạn 2: push nhắc nhở / chọc bạn, thi đấu 1-1, AI nhận xét buổi tập, sao lưu toàn bộ nhật ký lên đám mây.

## 7. Điểm yếu đã biết của nghiên cứu

- Hướng dẫn kỹ thuật mới đối chiếu nguồn được **18/90 bài**. Cần một lượt kiểm tra lại trước khi build.
- Mức tạ khởi điểm, danh sách dụng cụ "gym cỏ" và bước tạ ở phòng tập Việt Nam đều là ước lượng. Sẽ chỉnh theo phòng thật.
- Cách tính vùng sẵn sàng (readiness), khung tuần và cách cắt buổi theo thời gian là mặc định thiết kế; chưa có nghiên cứu nào xác thực.
- ExRx, NSCA, Reddit và trang của Fitbod/Hevy chặn truy cập, nên một số thông tin lấy từ nguồn thứ cấp.

## 8. Đã chốt (2026-11-19)

| # | Quyết định | Hệ quả |
|---|---|---|
| Q1 | Dùng cả iPhone và Android | PWA host trên Netlify; nút sao lưu bắt buộc có trong MVP |
| Q2 | Mọi người tập lẫn lộn, hay đổi phòng | Mỗi người lưu **nhiều hồ sơ phòng tập**, chọn phòng lúc check-in (nhớ phòng lần trước). Hồ sơ phòng chia sẻ được giữa các thành viên trong nhóm |
| Q3 | Cần bảng nhóm, streak nhóm và thử thách **ngay bản đầu** | Firebase Firestore + mã nhóm nằm trong MVP. Chỉ đồng bộ bản tóm tắt tuần, sự kiện feed, cổ vũ và hồ sơ phòng tập; nhật ký tập chi tiết vẫn ở trên máy |
| Q4 | Hướng dẫn bằng **chữ + clip động tác ngắn làm bằng code** | Hoạt hình người que/khung xương bằng SVG, chạy theo keyframe. Mỗi pattern dùng chung một bộ khung chuyển động, từng bài chỉ chỉnh góc và dụng cụ để 90 bài không phải vẽ riêng 90 clip |

## 8b. Câu hỏi đã hỏi người dùng

| # | Câu hỏi | Ảnh hưởng tới |
|---|---|---|
| Q1 | Nhóm dùng iPhone, Android, hay cả hai? | PWA là đủ, hay nên đóng thêm APK cho Android; mức rủi ro mất dữ liệu trên iOS |
| Q2 | Mọi người tập chung một phòng hay nhiều phòng khác nhau? | Cần một hồ sơ phòng dùng chung, hay mỗi người nhiều hồ sơ phòng |
| Q3 | Bảng nhóm, streak nhóm và thử thách có cần ngay bản đầu không, hay giai đoạn đầu chỉ chia sẻ thẻ vào nhóm chat? | Có cần dựng Firebase + mã nhóm ngay từ MVP không |
| Q4 | Hướng dẫn kỹ thuật dạng chữ có đủ không, hay người mới cần ảnh hoặc video ngay từ đầu? | Khối lượng nội dung; nguồn ảnh (tự tạo, dùng link YouTube, hay ảnh minh hoạ AI) |
