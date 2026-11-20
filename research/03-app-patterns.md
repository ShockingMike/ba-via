# 03 — Mẫu UX & tính năng từ các app tập gym / AI coach

Ngày nghiên cứu: 2026-11-19. Mục tiêu: rút mẫu thiết kế cho PWA gym cá nhân (check-in mỗi ngày → sinh buổi tập → ghi set → tự tăng tiến, đổi bài 1 chạm).

**Phạm vi đã cập nhật:** không chỉ 2 vợ chồng mà là **nhóm bạn nhỏ ~2–10 người**, mỗi người dùng app trên điện thoại riêng với hồ sơ riêng. Đồng bộ giữa mọi người là tuỳ chọn (nice-to-have). Người dùng muốn tính năng xã hội kiểu Duolingo để giữ động lực → xem **mục 8** (xã hội + streak) và **mục 9** (đồng bộ cho nhóm).

## 0. Giới hạn của nghiên cứu này (đọc trước)

- **Reddit không đọc trực tiếp được** (công cụ tìm kiếm bị chặn domain reddit.com). Mọi ý "người dùng Reddit nói…" trong file này là qua nguồn thứ cấp và được gắn [UNVERIFIED].
- **Trang chính chủ của Fitbod và Hevy help center trả 403.** Thông tin Fitbod lấy từ đoạn trích kết quả tìm kiếm của help.fitbod.me, bài Android Central, và blog đối thủ. Phần nào chỉ dựa vào đó đều có ghi chú.
- **Nhiều nguồn là blog của đối thủ** (JEFIT, Alpha Progression, Boostcamp, Dr. Muscle viết về app khác). Đã đánh dấu ở mục Nguồn; số liệu chỉ có ở một nguồn loại này gắn [UNVERIFIED].
- **Mục 8–9 (bổ sung sau):** nhận định về Nike Training Club, Ladder, Future dựa trên blog đối thủ. Các nguồn gộp nhiều URL (S12–S16, S29–S35) là đoạn trích từ kết quả tìm kiếm; chưa xác nhận được từng ý ứng với URL nào. Ba ý về nghiên cứu gamification ở mục 8b (trừ STEP UP) thuộc loại này.
- **Giá cả** chỉ nêu sơ bộ, các nguồn lệch nhau; không nên dựa vào.
- [UNVERIFIED] = suy đoán hoặc chưa kiểm chứng được bằng nguồn sơ cấp.

## 1. Ba phát hiện sát nhất với bài toán "thiết bị không chắc, đổi bài 1 chạm"

| Mẫu | App làm | Áp dụng cho app mình |
|---|---|---|
| Hỏi phạm vi khi đổi bài | Boostcamp: đổi bài ngay trong buổi, app hỏi áp dụng cho hôm nay hay cả các buổi sau [S10]. Volt: chọn buổi này / cả block / vĩnh viễn [S17] | Mặc định "chỉ hôm nay" (không hỏi, 1 chạm). Nút phụ "luôn dùng bài này" để khỏi thêm bước |
| Tách "máy đang bận" khỏi "không tập được" | Gymkee: máy bận → đổi thứ tự (giữ bài, làm sau); không tập được → thay bài [S17] | 2 hành động riêng trên mỗi bài: **"Để sau"** (đẩy xuống cuối) và **"Đổi bài"** |
| Thiết bị + bước tạ gắn với hồ sơ phòng tập | Alpha Progression: nhiều gym profile, mỗi profile có thiết bị và mức tạ riêng; gợi ý tăng tiến tính theo bước tạ thật có ở phòng (vd 20 → 22,5 kg) [S8] | Lưu danh sách thiết bị + bước tạ của phòng 1 lần; check-in chỉ đánh dấu cái **hôm nay không dùng được** |

Cảnh báo từ Fitbod: người dùng phàn nàn các gym profile ghi đè lẫn nhau (sửa thời lượng/thiết bị ở profile này làm đổi profile kia), mất thời gian chỉnh lại ngay tại phòng tập [S14, nguồn tổng hợp review, chưa rõ ngày]. Bài học: trạng thái "hôm nay thiếu máy X" phải là dữ liệu **của buổi tập**, không ghi đè lên hồ sơ phòng tập.

## 2. Cách từng app sinh / điều chỉnh buổi tập

| App | Cách sinh buổi tập | Thích ứng theo | Thiết bị | Đổi bài |
|---|---|---|---|---|
| **Fitbod** | Sinh mới mỗi buổi từ: mục tiêu, trình độ, thiết bị, kiểu chia buổi, sở thích [S1] | % hồi phục từng nhóm cơ 0–100% (hồi đủ tối đa ~7 ngày), ưu tiên cơ đã hồi; cơ còn mệt → giảm cường độ hoặc bài khác, không bỏ hẳn [S1]. Mỗi lần bỏ / thay / xoá / thêm bài đều là tín hiệu cho lần sau [S1] | Chọn khi cài đặt; có nhiều gym profile [S14]. Chỉnh thời lượng 15–90 phút, app sinh lại trong vài giây [S2, S6] | "Replace" → bài tương tự cùng nhóm cơ; có "gợi ý nhiều hơn / ít hơn / loại trừ" [S1, S2]. Số chạm cụ thể [UNVERIFIED] |
| **JuggernautAI** | Chương trình theo block (hypertrophy / strength / peaking), thiên powerlifting [S4] | Readiness trước buổi → chỉnh tải/khối lượng trong ngày; RPE của top set và back-down set → chỉnh các set sau; cuối tuần chỉnh tuần sau [S4]. Ví dụ: đùi/mông đau → hạ tải squat riêng hôm đó; chạm RPE 10 ở set 2 → app bỏ set 3 [S5] | Tối thiểu rack + ghế + tạ đòn; không có gym profile chi tiết [S5, S8] | Đổi theo ngày hoặc cho cả block [S5] |
| **RP Hypertrophy** | Người dùng chọn template hoặc tự dựng mesocycle (chọn nhóm cơ ưu tiên); **người dùng tự chọn bài** [S7] | Phản hồi pump / đau cơ / workload → tăng hoặc giữ số set tuần sau. Pump thấp + ít đau + "dễ" → thêm set; pump mạnh + hồi kịp + sát giới hạn → giữ nguyên. Có thể tự thêm/xoá set [S9] | Không có hồ sơ thiết bị; tự chọn bài phù hợp [S7] | Tự sửa buổi tập tại phòng [S7]; luồng đổi bài cụ thể [UNVERIFIED] |
| **Alpha Progression** | Plan generator hỏi: mục tiêu, kinh nghiệm, số buổi/tuần, thời lượng buổi, thiết bị, bước tạ, nhóm cơ ưu tiên [S8] | Không có readiness. Gợi ý tạ + rep cho từng set dựa trên lịch sử, các set trước trong buổi và bước tạ có sẵn; chỉnh được cả tải lẫn rep [S8] | Nhiều gym profile (Pro) [S8] | Luồng đổi bài [UNVERIFIED] |
| **Hevy** | Tracker thuần: tự tạo routine. "Hevy Trainer" (Pro, từ 02/2026) tăng tạ khi chạm đầu trên của khoảng rep [S6, chỉ một nguồn đối thủ → UNVERIFIED] | Không | Không | Menu ba chấm trên bài: replace / reorder / remove [S3] → 2–3 chạm |
| **Strong** | Tracker thuần, không gợi ý nên nâng gì [S6] | Không | Không | [UNVERIFIED] |
| **JEFIT** | "Adaptive Plan" 12 tuần = 3 block × 4 tuần, kết thúc bằng deload (bản trả phí) [S6, blog chính chủ] | Theo block | [UNVERIFIED] | [UNVERIFIED] |
| **Boostcamp** | Thư viện chương trình có sẵn của coach (5/3/1, PPL…), có quiz chọn chương trình và tuỳ chọn AI dựng plan theo lịch + thiết bị [S10] | Theo chương trình; auto-progression chưa được nguồn xác nhận [UNVERIFIED] | Qua AI builder [S10] | Đổi ngay trong buổi + hỏi phạm vi; app gợi ý bài thay thế [S10] |
| **Caliber** | Plan theo chu kỳ, ít bài mỗi nhóm cơ, lặp nhiều tuần; mỗi tuần cố thêm rep hoặc tạ ở ít nhất 1 bài. Bản trả phí có coach người thật cập nhật plan [S11] | Coach xem log | [UNVERIFIED] | [UNVERIFIED] |

**Hai trường phái:**
- **Sinh mới mỗi buổi (Fitbod):** linh hoạt với thiết bị/thời gian — đúng nhu cầu của mình. Điểm yếu được nêu: không có kế hoạch nhiều tuần [S6], gợi ý ban đầu chung chung cho tới khi đủ dữ liệu [S14], không hợp người tập lâu năm [S13].
- **Chương trình cố định + tự điều chỉnh (RP, Juggernaut, Alpha, Caliber):** tăng tiến rõ ràng vì lặp lại cùng bài. Điểm yếu: cứng khi lịch/thiết bị thay đổi (nhận định về RP đến từ blog đối thủ [UNVERIFIED]).
- **Đề xuất lai:** khung tuần cố định theo *nhóm chuyển động* (vd đẩy ngang, kéo dọc, squat, hinge), mỗi ô có bài mặc định + danh sách bài thay thế tương đương. Check-in chỉ quyết định: bao nhiêu ô, bài nào trong ô, bao nhiêu set. Tăng tiến theo dõi **riêng từng bài**, nên đổi bài không làm mất lịch sử.

## 3. Câu hỏi check-in: app nào hỏi gì, bao nhiêu câu

| App | Thời điểm | Số câu | Nội dung |
|---|---|---|---|
| JuggernautAI | Trước buổi | 4 thang 1–5 + đau mỏi từng nhóm cơ | Động lực, giấc ngủ, ăn đủ chưa, đau/mệt [S5]. Còn hỏi thêm trong buổi, sau buổi, cuối tuần, cuối block; tổng hợp thành Readiness Score 0–100 [S8, blog đối thủ] |
| RP Hypertrophy | Sau khi tập | 3 (có nguồn nói 4) | Pump, đau cơ, workload [S9]. Đau khớp có trong trang marketing nhưng bài help chính chủ không nêu [S7, S9] → [UNVERIFIED]. Thang điểm và thời điểm chính xác [UNVERIFIED] |
| Fitbod | Trong buổi | 0 câu trước buổi [UNVERIFIED] | Đánh giá độ khó sau mỗi set [S2]; thời lượng và thiết bị là cài đặt, không phải câu hỏi [S2] |
| Alpha Progression | — | 0 | Không dùng readiness; RIR tuỳ chọn [S8] |
| Hevy / Strong / Boostcamp | — | 0 | RPE tuỳ chọn theo set [S3, S10, S15] |
| Caliber | — | [UNVERIFIED] | — |

**Nhận xét:** app càng "AI coach" càng hỏi nhiều. Không tìm được bằng chứng trực tiếp về việc người dùng phàn nàn check-in dài (tìm kiếm không ra) → nguyên tắc "ít câu" dưới đây là phán đoán thiết kế, không phải kết luận từ dữ liệu.

**Đề xuất cho app mình — 3 câu, 3 chạm, dưới 10 giây:**

| # | Câu hỏi | Kiểu nhập | Mặc định |
|---|---|---|---|
| 1 | Hôm nay thấy thế nào? | 3 mức: mệt / bình thường / sung | Bình thường |
| 2 | Có bao nhiêu thời gian? | Chip: 30 / 45 / 60 / 75 phút | Lần trước |
| 3 | Hôm nay thiếu/bận thiết bị gì? | Chip bật tắt theo danh sách thiết bị phòng tập | Không thiếu gì |

- Có nút "Như mọi khi" → bỏ qua cả 3 câu.
- Câu tuỳ chọn, ẩn sau "thêm": đau chỗ nào (chọn vùng cơ thể) → loại bài dùng vùng đó.
- Đau mỏi cơ không cần hỏi: suy ra từ log (kiểu % hồi phục của Fitbod).
- Sau buổi: tối đa 1 câu ("buổi này: nhẹ / vừa / quá sức"), bỏ qua được.

## 4. UX ghi set

| Thành phần | App làm tốt | Chi tiết đáng chép |
|---|---|---|
| Tự điền số lần trước | Hevy: cột PREVIOUS, chọn "lần gần nhất của bài này" hoặc "lần gần nhất trong cùng routine" [S3]. Strong: số lần trước ngay dưới bài, chạm vào set để ghi với cùng tạ + rep [S15]. Boostcamp: hiện set/rep/tạ tuần trước [S10]. Caliber: hiện rep + tạ lần cuối [S11] | Điền sẵn **mục tiêu hôm nay** (đã cộng tăng tiến); 1 chạm ✓ là xong set, chỉ sửa khi lệch |
| Loại set | Hevy: chạm số thứ tự set để đổi normal / warm-up / drop / failure [S3] | MVP chỉ cần normal + warm-up |
| Đồng hồ nghỉ | Hevy và Strong: tự chạy khi đánh dấu xong set, đặt riêng từng bài [S3, S15]. Alpha và Juggernaut: hiện ở Live Activity / thông báo [S8] | Tự chạy sau ✓. Hạn chế của Hevy: không đặt được thời gian nghỉ khác nhau cho set khởi động và set chính trong cùng bài [S16] |
| RPE / RIR | Hevy: cột RPE bật trong cài đặt, mặc định tắt [S3]. Alpha: RIR tuỳ chọn, tăng tiến vẫn chạy khi không nhập [S8]. Juggernaut: RPE là lõi, cần kinh nghiệm tự đánh giá [S4, S5] | Mặc định ẩn. Thay bằng 1 chạm sau set cuối của mỗi bài: "còn sức / vừa / hết sức" |
| Tính bánh tạ | Hevy: nút Calculator trên bàn phím, chọn trọng lượng đòn + bánh tạ có sẵn [S3]. Boostcamp: tự hiện số bánh mỗi bên cho từng set [S10]. Strong: máy tính chỉ nhận các loại đòn phổ biến [S15] | Hiện sẵn "mỗi bên: 20 + 5" dưới mức tạ, đơn vị kg, khai báo đòn và bánh tạ của phòng |
| Khởi động | Hevy: warm-up calculator, công thức chỉnh được [S3]. Juggernaut: Guided Warmups, cảm giác set khởi động có thể đổi mục tiêu trong ngày [S8, blog đối thủ] | Để sau MVP |
| Ghi chú | Hevy: ghi chú routine (hiện mỗi lần), ghi chú buổi, ghi chú ghim theo bài [S3] | Ghi chú ghim theo bài (vd "ghế nấc 4") rất hợp khi máy móc thay đổi |
| Báo PR tức thì | Hevy: báo ngay khi set vừa xong là kỷ lục [S3] | Rẻ, tạo động lực → MVP |
| Video hướng dẫn | Caliber: video tự phát lại, đôi khi không tải được [S11]. Boostcamp: chỉ là animation [S10] | PWA offline: ảnh tĩnh / mô tả ngắn; video là link ngoài |

Lưu ý nhập liệu cho PWA [UNVERIFIED — kinh nghiệm thiết kế, không từ nguồn]: nút +/− theo đúng bước tạ, bàn phím số (`inputmode="decimal"`), vùng chạm lớn, giữ màn hình sáng (Wake Lock API), ghi xuống IndexedDB ngay sau mỗi set để không mất dữ liệu khi tắt app.

## 5. Màn hình tiến độ đáng có

| Màn hình | App tham khảo | Ưu tiên |
|---|---|---|
| PR theo bài + 1RM ước tính | Strong (tab Records, miễn phí) [S6]; Hevy (báo PR trực tiếp) [S3] | MVP |
| Biểu đồ theo bài (tạ tốt nhất / 1RM ước tính theo thời gian) | Strong PRO, Hevy, Alpha Pro [S6, S8] | MVP (1 biểu đồ đường) |
| Số set mỗi nhóm cơ / tuần | Hevy, JEFIT, Fitbod (Weekly Set Targets) [S6] | Sau MVP |
| Bản đồ nhiệt nhóm cơ / hồi phục | Fitbod (% hồi phục) [S1, S2]; Boostcamp (heatmap khối lượng, Pro) [S10] | Sau MVP — nhưng dữ liệu hồi phục cần cho bộ sinh buổi tập ngay từ đầu |
| Cân nặng + số đo | Alpha (miễn phí), Strong (PRO), Juggernaut (cân nặng, giấc ngủ) [S6, S8] | MVP: chỉ cân nặng. Số đo: sau |
| Chuỗi / độ đều đặn | Alpha (streak, thành tích), Juggernaut (consistency) [S8] | MVP: **streak theo tuần** (đạt số buổi đã hẹn). Không dùng streak theo ngày — chi tiết ở mục 8c |
| Điểm sức mạnh tổng hợp | Caliber (Strength Score, Strength Balance); người review thấy không rõ bài nào được tính, đôi khi vô lý [S11] | Bỏ qua |
| Ảnh tiến độ | Boostcamp Pro [S10] | Sau (nặng dung lượng, khó đồng bộ) |
| So sánh trong nhóm | Hevy có Compare và bảng xếp hạng bạn bè [S6, blog đối thủ] | Sau (cần đồng bộ): bảng tuần của nhóm — xem mục 8 |

## 6. Khen / chê — chép gì, tránh gì

| App | Được khen | Bị chê |
|---|---|---|
| Fitbod | Tuỳ biến nhanh, sinh lại trong vài giây; tránh tập quá tải một nhóm cơ; giới thiệu bài mới kèm video [S2]. Thay bài nhanh khi máy bận [S14] | Gym profile ghi đè nhau [S14]. Không có bản miễn phí [S6, S13]. Không có kế hoạch nhiều tuần [S6]. Giao diện "trơ trọi", ghi tay kém liền mạch [S2]. Cần vài buổi mới hiệu chỉnh xong [S13]. Bài tự tạo không sửa được và bị loại khỏi gợi ý, không có xuất dữ liệu [S6, blog đối thủ → UNVERIFIED] |
| Hevy | Bản miễn phí rộng rãi nhất [S12, thứ cấp]. Ghi set đầy đủ tính năng [S3] | Miễn phí giới hạn 4 routine, 7 bài tự tạo, 3 tháng lịch sử [S6, S12] |
| Strong | Ghi set nhanh nhất, ít ma sát nhất giữa các set [S6]. Xuất CSV miễn phí [S6] | Miễn phí chỉ 3 routine; biểu đồ và số đo trả phí; không gợi ý tăng tiến [S6, S12] |
| JEFIT | Thư viện bài tập và plan lớn, có web [S6, blog chính chủ] | Quảng cáo ở bản miễn phí, có nguồn nói chen cả vào đồng hồ nghỉ [S12, nguồn đối thủ → UNVERIFIED] |
| Boostcamp | Chương trình của coach nổi tiếng, phần lớn miễn phí, có offline, gợi ý bài thay thế [S10] | Điều hướng rối, bản cập nhật giao diện gây khó hiểu, builder khó học [S10] |
| Alpha Progression | Gợi ý tăng tiến cụ thể từng set; gym profile [S8, S16] | Tính năng lõi nằm sau Pro [S8] |
| RP Hypertrophy | Cấu trúc rõ, tăng tiến quá tải, điều chỉnh theo cá nhân, chạy trên web [S18] | Đắt; không thân thiện người mới; không quy định thời gian nghỉ [S18, blog đối thủ]. Phụ thuộc tự đánh giá chính xác [S18] |
| JuggernautAI | AI phản ứng nhanh và hợp lý [S5] | Dashboard rối lúc đầu, chữ xanh trên nền đen khó đọc, đắt, cần kinh nghiệm đánh giá RPE [S5] |
| Caliber | Bản miễn phí đầy đủ, không quảng cáo; plan có cơ sở khoa học [S11] | Strength Score khó hiểu; video đôi khi không tải [S11] |

**Nên chép**
- Điền sẵn số + 1 chạm ✓ để xong set (Strong, Hevy).
- Đồng hồ nghỉ tự chạy sau ✓ (Hevy, Strong).
- Gợi ý tạ/rep cụ thể cho từng set, theo đúng bước tạ phòng tập (Alpha).
- Thay bài bằng bài tương đương cùng nhóm cơ; mỗi lần thay là tín hiệu ưu tiên cho lần sau (Fitbod).
- Hồi phục suy ra từ log, không hỏi (Fitbod).
- "Để sau" và "Đổi bài" là 2 hành động riêng (Gymkee).
- Ghi chú ghim theo bài (Hevy).
- Xuất dữ liệu miễn phí (Strong).

**Nên tránh**
- Sinh bài ngẫu nhiên mỗi buổi khiến không thấy tăng tiến → giữ khung tuần ổn định.
- Hỏi nhiều thang điểm trước buổi (kiểu Juggernaut) cho người tập phổ thông.
- Bắt buộc RPE/RIR; nhiều nguồn nói cần kinh nghiệm mới đánh giá đúng [S5, S18].
- Thay đổi tạm thời hôm nay ghi đè lên cấu hình lâu dài (lỗi gym profile của Fitbod).
- Chỉ số tổng hợp khó giải thích (Strength Score của Caliber).
- Dashboard dày đặc ở màn hình đầu (Juggernaut, Boostcamp).

## 7. MVP và các giai đoạn sau (PWA offline-first, nhóm 2–10 người)

### MVP

| Nhóm | Tính năng |
|---|---|
| Hồ sơ | Mỗi máy 1 hồ sơ chính: mục tiêu, trình độ, số buổi/tuần đã hẹn, đơn vị kg. (Cho phép thêm hồ sơ thứ 2 trên cùng máy nếu có người dùng chung) |
| Phòng tập | Danh sách thiết bị + bước tạ + đòn/bánh tạ; chia sẻ cho bạn bằng mã/file để khỏi nhập lại |
| Thư viện bài | ~60–100 bài, mỗi bài gắn: nhóm cơ, kiểu chuyển động, thiết bị cần → từ đó tính bài thay thế |
| Check-in | 3 câu (mục 3) + nút "Như mọi khi" |
| Sinh buổi tập | Khung tuần theo nhóm chuyển động; lọc theo thiết bị hôm nay; cắt số bài/set theo thời gian; giảm set khi "mệt" |
| Đổi bài | 1 chạm → 3–4 bài tương đương dùng thiết bị đang có; "Để sau" riêng. Mặc định chỉ áp dụng hôm nay |
| Ghi set | Điền sẵn mục tiêu, ✓ 1 chạm, +/− theo bước tạ, đồng hồ nghỉ tự chạy, hiện số lần trước |
| Tăng tiến | Double progression theo từng bài: đạt đầu trên khoảng rep ở mọi set → tăng 1 bước tạ; hụt nhiều buổi liền → giảm tải. Cùng nguyên lý mà một nguồn đối thủ mô tả cho Hevy Trainer [S6 → UNVERIFIED] |
| Tiến độ | Lịch sử buổi tập, PR theo bài + báo PR, 1 biểu đồ theo bài, cân nặng |
| Động lực (1 người, offline) | Streak theo tuần + "tuần nghỉ có phép", vài huy hiệu mốc, thẻ tổng kết buổi tập để chia sẻ vào nhóm chat (mục 8) |
| Dữ liệu | IndexedDB, hoạt động hoàn toàn offline, cài lên màn hình chính, **xuất/nhập JSON** |

### Giai đoạn sau

- Đồng bộ nhóm: bảng tuần, feed, thả cổ vũ, thử thách chung, nhắc nhau (mục 8, 9).
- Bản đồ hồi phục nhóm cơ, số set/nhóm cơ/tuần.
- Tính bánh tạ, set khởi động tự động, superset, drop set.
- RPE/RIR tuỳ chọn; tuần deload tự động.
- Số đo cơ thể, ảnh tiến độ.
- Nhiều phòng tập (profile), mỗi profile độc lập hoàn toàn.
- AI viết nhận xét/giải thích buổi tập (cần gọi API → cần mạng).

### Lưu trữ trên iOS — rủi ro cần kiểm tra trên máy thật

- WebKit: web app trên màn hình chính có cùng quota với khi mở trong trình duyệt (tới ~60% dung lượng đĩa cho mỗi origin ở app trình duyệt); dữ liệu mặc định ở chế độ "best-effort" và **có thể bị xoá** khi thiếu dung lượng hoặc lâu không tương tác [S19].
- `navigator.storage.persist()` được cấp theo heuristic, ví dụ site được mở dưới dạng Home Screen Web App [S19]. Có báo cáo lỗi nó luôn trả `false` trên Safari 17 macOS [S20] → không dựa vào.
- Giới hạn 7 ngày của ITP: Apple từng nói web app trên màn hình chính có bộ đếm riêng, không thuộc Safari [S20, nguồn thứ cấp/cũ]; bài WebKit 2023 không khẳng định miễn trừ [S19] → [UNVERIFIED], phải thử trên iPhone của chính người dùng trong nhóm.
- iOS không có Background Sync → đồng bộ khi mở app / khi app lấy lại focus / khi có mạng [S21, nguồn thứ cấp].
- **Kết luận:** xuất JSON + nhắc sao lưu định kỳ phải nằm trong MVP, bất kể chọn phương án đồng bộ nào.

### Đồng bộ

Xem **mục 9** (đã viết lại cho nhóm 2–10 người).

## 8. Tính năng xã hội & streak kiểu Duolingo

### 8a. Duolingo: cơ chế và bằng chứng

| Cơ chế | Cách hoạt động | Bằng chứng / số liệu | Độ tin cậy |
|---|---|---|---|
| Streak (chuỗi ngày) | Đếm số ngày liên tiếp hoàn thành ít nhất 1 bài. Từ ~2019 tách khỏi "mục tiêu ngày": chỉ cần **1 bài** là giữ chuỗi [S27] | A/B test: retention ngày 14 +3,3%, số người học hằng ngày +1%, số người đang có streak +10,5% sau 20 ngày (thay đổi tương đối). Người có streak 7 ngày quay lại hôm sau nhiều gấp 2,4 lần. Đánh đổi: ít người đạt mục tiêu ngày hơn [S27] | Chính chủ, có A/B test |
| Mốc 7–10 ngày | Qua mốc 10 ngày thì tỉ lệ bỏ giảm mạnh; tác giả tự lưu ý có thể là tương quan / thiên lệch chọn mẫu [S28] | Tỉ lệ DAU có streak 7+ ngày tăng gần gấp 3, lên hơn một nửa DAU [S28] | Lời kể của người trong cuộc, không phải thí nghiệm riêng |
| Streak freeze | Giữ chuỗi khi lỡ 1 ngày; phải có sẵn **trước** ngày bị lỡ; chuỗi được giữ nhưng không tăng [S38, hướng dẫn bên thứ ba]. Trang bị tối đa 2 cái cùng lúc [S38, blog Duolingo, trích đoạn]. Giá 200 gem, mức trần cao hơn cho streak dài: các hướng dẫn mâu thuẫn nhau [UNVERIFIED] | Chỉ có nhận định định tính: các chỉnh sửa về freeze, lịch, hoạt ảnh, phần thưởng "cải thiện đáng kể retention", **không có con số riêng** [S28] | Yếu |
| Thông báo cứu streak | Nhắc khi sắp mất chuỗi; là "thắng lợi lớn đầu tiên" [S28]. Kèm nguyên tắc "bảo vệ kênh": không tăng số thông báo nếu không có lý do mạnh [S28] | Không có con số riêng | Lời kể |
| League (giải đấu tuần) | Xếp nhóm với người **cùng mức độ hoạt động** (không phải bạn bè), top thăng hạng mỗi tuần; mượn từ FarmVille 2, tự động tham gia [S28] | Thời gian học tổng +17%, số người học rất chăm (≥1 giờ/ngày, 5 ngày/tuần) tăng gấp 3; D1 và D7 cải thiện có ý nghĩa thống kê [S28] | Lời kể của người trong cuộc |
| Friend Streak | Chuỗi chung với tối đa 5 bạn, mỗi bạn 1 chuỗi riêng, phải chấp nhận lời mời; mỗi người làm 1 bài/ngày để giữ [S29] | Người có ít nhất 1 chuỗi chung có khả năng hoàn thành bài hằng ngày cao hơn 22% — là **tương quan** do Duolingo công bố, không phải nhân quả [S29] | Chính chủ, tương quan |
| Friends Quest | Mỗi tuần ghép cặp với 1 bạn đang hoạt động, cùng đóng góp vào 1 mục tiêu chung, có 5 ngày để xong; thưởng XP boost hoặc gem [S29] | Không có số liệu retention. Có báo cáo lỗi ghép cặp ngẫu nhiên, tab trống (11/2025) [S29, nguồn thứ cấp] | Cơ chế: chính chủ. Tác động: [UNVERIFIED] |
| Thứ thất bại | Bộ đếm lượt kiểu Gardenscapes: trung tính, không tăng retention hay DAU. Chương trình giới thiệu bạn: chỉ +3% người dùng mới [S28] | — | Lời kể |

**Rút ra cho app gym:**
- Hạ ngưỡng giữ chuỗi xuống mức tối thiểu là đòn bẩy có bằng chứng rõ nhất (1 bài = giữ streak). Tương đương ở gym: **đến tập và ghi một buổi ngắn** là tính, không cần hoàn thành đủ kế hoạch.
- League của Duolingo hiệu quả nhờ ghép người **cùng mức**, không phải bạn bè. Nhóm 2–10 bạn chênh trình độ thì bảng xếp hạng thô (ai nâng nặng nhất) không tái tạo được điều này → xếp hạng theo **độ đều đặn**, thứ ai cũng có thể thắng.
- Cơ chế cộng tác (Friend Streak, Friends Quest) hợp với nhóm bạn thật hơn là league.
- Thông báo: từ iOS/iPadOS 16.4, web app **đã thêm vào màn hình chính** mới xin được quyền push, và phải xin sau một thao tác trực tiếp của người dùng (bấm nút) [S39]. Push đi qua máy chủ của Apple nên cần một backend gửi đi [S39; phần "cần backend" là suy luận]. Không có backend thì không có nhắc nhở từ xa.

### 8b. Tính năng xã hội ở app thể dục

| App | Tính năng | Bằng chứng / đánh giá |
|---|---|---|
| Strava | Kudos, club, thử thách, feed | Nghiên cứu ĐH Radboud trên 329 thành viên của 5 club chạy bộ ở Hà Lan: nhận nhiều kudos hơn → chạy nhiều hơn; ở 4/5 club, ảnh hưởng từ bạn tập còn mạnh hơn kudos. Mẫu nhỏ, hẹp về văn hoá [S30]. Nghiên cứu UX của chính Strava (2017): kudos chủ yếu đến từ cùng một nhóm thân (một người nói 95%) → giá trị nằm ở **vòng nhỏ quen biết** [S30]. Số liệu retention của Strava do bên thứ ba dẫn là cũ và không kiểm chứng được [UNVERIFIED] |
| Hevy | Tab Home là feed buổi tập của người mình follow (tên buổi, mô tả, thời lượng, khối lượng, PR); bình luận; hồ sơ riêng tư cần duyệt follow; bảng xếp hạng theo từng bài giữa bạn bè [S40, chính chủ, trích đoạn] | Không tìm được số liệu tác động [UNVERIFIED]. Một số review coi phần xã hội là gây xao nhãng [S40, thứ cấp] |
| Fitbod | Không có lớp xã hội đáng kể [UNVERIFIED — không nguồn nào đã đọc nhắc đến] | — |
| Apple Fitness | Chia sẻ Activity với bạn; thi đấu 1-1 trong **7 ngày**, điểm = % vòng Activity đã đóng mỗi ngày, trần 600 điểm/ngày (4.200/tuần) [S41, Apple Support, trích đoạn]. watchOS 11 thêm **tạm dừng vòng Activity** (1 ngày đến nhiều tuần, có nguồn nói tối đa 90 ngày) mà không mất chuỗi, sau nhiều năm bị chê không cho nghỉ [S31, S32] | Chấm điểm theo % mục tiêu riêng + có trần mỗi ngày → công bằng giữa người khác trình độ và không thưởng vô hạn cho tập quá sức. Apple cũng phải bổ sung cơ chế nghỉ |
| Nike Training Club | Thử thách + thông báo | Một bài review chấm 2/5 về khả năng giữ trách nhiệm: chỉ có thông báo và thử thách thì yếu [S33, blog đối thủ → UNVERIFIED] |
| Ladder | Vào "team" cùng theo 1 chương trình 4–12 tuần, thấy mình so với đồng đội, thử thách hằng tuần [S33, blog đối thủ] | Mô hình trách nhiệm theo nhóm; không có số liệu [UNVERIFIED] |
| Future | Coach người thật 1-1, khoảng 199 USD/tháng [S33, blog đối thủ] | Trách nhiệm đến từ con người, không phải cơ chế game |

**Nghiên cứu về gamification trong vận động:**
- Thử nghiệm STEP UP (JAMA Internal Medicine 2019, 602 người, 24 tuần + 12 tuần theo dõi): cả 3 nhánh gamification đều tăng số bước so với đối chứng — cạnh tranh +920, hỗ trợ +689, cộng tác +637 bước/ngày. Sau khi ngừng trò chơi, **chỉ nhánh cạnh tranh** còn khác biệt có ý nghĩa (+569 bước/ngày) [S34]. Lưu ý: đối tượng là người thừa cân, đo số bước, không phải tập tạ.
- [Từ tóm tắt tìm kiếm, chưa xác nhận URL] Một thử nghiệm 2022: app có gamification được dùng nhiều ngày hơn, bảng xếp hạng là tính năng được xem nhiều nhất; nhưng mức đạt mục tiêu không khác biệt [S35, trích đoạn].
- [Từ tóm tắt tìm kiếm, chưa xác nhận URL] Một bản preprint: gamification kiểu cạnh tranh tăng gắn kết nhưng cũng tăng căng thẳng và hệ quả xã hội tiêu cực, có nguy cơ "kiệt sức vì gamification" [S35, trích đoạn, chưa bình duyệt].
- **Không tìm được nghiên cứu nào** tách riêng tác động của huy hiệu hay XP → mọi nhận định "XP là gimmick" bên dưới là phán đoán [UNVERIFIED].

**Cái có vẻ giữ chân vs cái có vẻ màu mè** (cột phải phần lớn là suy luận):

| Có cơ sở | Dễ thành gimmick |
|---|---|
| Phản hồi từ **người quen** trong nhóm nhỏ (kudos kiểu Strava) [S30] | XP / tiền ảo không đổi được gì có nghĩa [UNVERIFIED] |
| Cạnh tranh nhẹ, chu kỳ ngắn theo tuần [S28, S34] | Bảng xếp hạng theo sức mạnh tuyệt đối trong nhóm chênh trình độ [UNVERIFIED] |
| Ngưỡng tham gia thấp (1 buổi là tính) [S27] | Huy hiệu rải quá dày, không gắn với mốc thật [UNVERIFIED] |
| Mục tiêu chung của nhóm (kiểu Friends Quest) [S29] | Thông báo dày đặc — Duolingo tự giới hạn vì sợ hỏng kênh [S28] |
| Thấy được việc bạn mình vừa tập xong | Feed công khai với người lạ (không cần cho nhóm 2–10 người) |

### 8c. Thiết kế streak cho tập tạ

**Vấn đề:** streak theo ngày xung đột với tập tạ, vì ngày nghỉ là một phần của kế hoạch. Phê bình phổ biến với vòng Activity của Apple: không thể nghỉ 1 ngày mà không mất chuỗi, trong khi lịch tập hợp lý luôn có ngày nghỉ; nỗi sợ mất chuỗi kích hoạt đúng vào ngày mà không tập mới là lựa chọn đúng [S32]. App Gentler Streak được nêu làm ví dụ ngược lại: tính ngày hồi phục là hợp lệ [S32].

**Đề xuất: streak theo tuần, dựa trên số buổi đã hẹn**

| Quy tắc | Chi tiết | Lý do |
|---|---|---|
| Đơn vị là tuần | Tuần đạt = hoàn thành ≥ N buổi, N do mỗi người tự chọn (2–5). Streak = số tuần đạt liên tiếp | Ngày nghỉ không bao giờ bị phạt; không khuyến khích tập 7 ngày/tuần |
| Ngưỡng 1 buổi thấp | 1 buổi được tính khi ghi ≥ 1 bài đủ set (buổi 20 phút lúc mệt vẫn tính) | Tương đương "1 bài là giữ chuỗi" của Duolingo [S27] |
| Có trần | Tập quá N buổi không được thêm điểm streak; không thưởng cho ngày tập thứ 6–7 liên tiếp | Tránh thưởng cho việc tập quá sức |
| Tuần nghỉ có phép (thay cho freeze) | Khai báo trước hoặc trong tuần: ốm / chấn thương / đi xa → tuần đó không tính, streak giữ nguyên. Tự tích 1 "phép" sau mỗi 4 tuần đạt, giữ tối đa 2 | Giống tạm dừng vòng của Apple [S31] và freeze của Duolingo. Con số 4 và 2 là đề xuất, cần thử [UNVERIFIED] |
| Tuần deload vẫn đạt | Buổi nhẹ theo lịch deload tính như buổi thường | Không phạt việc giảm tải đúng kế hoạch |
| Không gắn với tạ/khối lượng | Streak chỉ đo việc **đến tập**. PR và tăng tiến hiển thị riêng | Tránh ép tăng tạ để giữ chuỗi |
| Mất chuỗi nhẹ nhàng | Hiện "kỷ lục: 14 tuần" và tổng số tuần đạt trọn đời bên cạnh chuỗi hiện tại; không dùng biểu tượng "vỡ" | Có phê bình rằng biểu tượng chuỗi vỡ đè lên ngày nghỉ là thông điệp sai [S32] |
| Chọn mục tiêu chủ động | Người dùng tự chọn N thay vì nhận mặc định | Có ghi nhận ở Duolingo rằng tự chọn mục tiêu streak cho retention tốt hơn mặc định [S36, thứ cấp → UNVERIFIED] |

Biến thể cho nhóm: **streak nhóm** = số tuần liên tiếp mà mọi người (hoặc ≥ 80% nhóm) đạt mục tiêu riêng của mình. Cộng tác thay vì đối đầu, công bằng giữa người tập 2 buổi và 5 buổi/tuần.

### 8d. Tính năng xã hội đề xuất: MVP vs sau

| Tính năng | Cần đồng bộ? | Giai đoạn |
|---|---|---|
| Streak tuần + tuần nghỉ có phép | Không | **MVP** |
| Huy hiệu mốc: buổi thứ 10/50/100, PR đầu tiên, 4/12/26 tuần đạt | Không | **MVP** (ít, gắn mốc thật) |
| Thẻ tổng kết buổi tập dạng ảnh → chia sẻ vào nhóm Zalo/Messenger qua Web Share | Không | **MVP** — "feed" miễn phí, dùng luôn nhóm chat có sẵn |
| Bảng tuần của nhóm: ai đạt mấy/mấy buổi, xếp theo % hoàn thành mục tiêu riêng | Có | Giai đoạn 2 |
| Feed hoạt động + thả cổ vũ 1 chạm (kiểu kudos) | Có | Giai đoạn 2 |
| Streak nhóm / thử thách tuần chung (vd "cả nhóm đủ 20 buổi tuần này") | Có | Giai đoạn 2 |
| Nhắc nhau ("chọc" bạn chưa tập) | Có + push | Giai đoạn 3 — push trên iOS đòi cài lên màn hình chính + backend gửi push [S39] |
| Thi đấu 1-1 trong 7 ngày, điểm theo % mục tiêu riêng, có trần (kiểu Apple [S41]) | Có | Giai đoạn 3 |
| XP, cấp độ, league thăng/xuống hạng | Có | Không khuyến nghị cho nhóm ≤ 10 người; cân nhắc lại sau |
| So PR / bảng xếp hạng sức mạnh | Có | Chỉ khi nhóm yêu cầu; nếu làm thì dùng % tiến bộ so với chính mình |

Quyền riêng tư trong nhóm [UNVERIFIED — phán đoán]: mặc định chỉ chia sẻ số buổi, streak, PR mới. Cân nặng và số đo luôn riêng tư trừ khi chủ động bật.

## 9. Kiến trúc đồng bộ cho nhóm nhỏ (2–10 người)

**Yêu cầu:** app phải chạy **đầy đủ offline cho 1 người** — mọi tính năng lõi (check-in, sinh buổi, ghi set, tăng tiến, streak) chỉ dùng IndexedDB trên máy. Đồng bộ là lớp bật thêm.

**Dữ liệu cần chia sẻ thật ra rất nhỏ.** Tính năng xã hội chỉ cần một bản tóm tắt mỗi người mỗi tuần (số buổi, mục tiêu, streak, PR mới) và các sự kiện feed — không cần đồng bộ toàn bộ log set. Log đầy đủ chỉ cần **sao lưu** cho chính chủ. Tách 2 nhu cầu này ra thì backend có thể rất nhẹ.

| Phương án | Vận hành | Chi phí | Ưu | Nhược | Hợp với |
|---|---|---|---|---|---|
| A. Không backend: xuất/nhập JSON; chia sẻ cấu hình phòng tập và thẻ tổng kết qua file / mã QR / Web Share | Không | 0 | Không phụ thuộc gì; riêng tư tuyệt đối | Không có bảng nhóm trực tiếp. QR chỉ chứa được dữ liệu nhỏ, hợp với bản tóm tắt tuần hoặc danh sách thiết bị, không hợp với toàn bộ lịch sử [UNVERIFIED về giới hạn chính xác] | **MVP** |
| B. Mã nhóm + kho key-value tối giản (1 serverless function + KV/blob; người dùng đã có tài khoản Netlify) | Rất thấp | Trong gói miễn phí [UNVERIFIED — chưa tra giới hạn] | Không cần đăng nhập: ai có mã nhóm thì đọc/ghi bản tóm tắt của mình; ít code | Bảo mật chỉ dựa vào độ bí mật của mã; phải tự viết; không realtime | Giai đoạn 2 nếu muốn tối giản |
| C. Firebase Firestore (Spark) | Thấp (dịch vụ quản lý) | 0 ở quy mô này: 1 GiB, 50k đọc + 20k ghi/ngày [S25] | Có cache offline và realtime trong SDK [UNVERIFIED cho bản web — tài liệu tính phí có nhắc offline persistence, chưa đọc tài liệu SDK]; không có cơ chế tạm dừng do ít dùng như Supabase [UNVERIFIED] | Khoá vào Google; vượt hạn mức Spark thì dịch vụ bị ngắt đến hết kỳ [S25]; phải viết security rules cẩn thận | **Giai đoạn 2 — ứng viên chính** |
| D. Supabase (free) | Thấp | 0: 500 MB DB, 2 project [S23] | Postgres/SQL, phân quyền theo dòng, realtime | Project miễn phí bị tạm dừng khi ít hoạt động trong 1 tuần, khôi phục thủ công từ dashboard [S24] — nhóm tập hằng tuần thì ít gặp nhưng vẫn là rủi ro vận hành; phần offline phải tự làm | Nếu thích SQL |
| E. PocketBase (1 file chạy, SQLite, có auth + realtime) | Trung bình: tự host và tự sao lưu | VPS khoảng 4–6 USD/tháng, hoặc PocketHost (gói miễn phí giới hạn 1 project; các nguồn mâu thuẫn về việc gói này có vĩnh viễn không) [S37] | Mã nguồn mở (MIT), dữ liệu trong tay mình, không giới hạn theo số người dùng [S37] | Thêm một máy chủ phải chăm; SQLite một luồng ghi (không thành vấn đề với 10 người) [S37] | Nếu đã có VPS |
| F. Dexie Cloud | Thấp | Gói miễn phí chỉ **3 production user** [S22] → không đủ cho 10 người; gói trả phí khoảng 3 EUR/tháng cho 25 chỗ [S22] | Ít code nhất nếu dùng Dexie; đồng bộ cả log | Tốn phí nhỏ; nhà cung cấp nhỏ | Nếu muốn đồng bộ toàn bộ log giữa nhiều máy |
| G. PouchDB + CouchDB | Cao (tự host CouchDB) | VPS | Giao thức sao chép chín muồi; CouchDB vẫn được bảo trì (3.5.1, 11/2025) [S26] | Nặng vận hành | Không khuyến nghị |
| H. P2P (Yjs + WebRTC) | Chỉ signaling | ~0 | Không lưu dữ liệu trên máy chủ | Các máy phải cùng online mới hội tụ; độ ổn định trên iOS chưa rõ [UNVERIFIED — không tìm được nguồn] | Không khuyến nghị |

**Khuyến nghị theo giai đoạn**
1. **MVP — phương án A.** Mỗi người độc lập, offline hoàn toàn. Xuất/nhập JSON để sao lưu. Chia sẻ cấu hình phòng tập bằng file/QR. Thẻ tổng kết buổi tập gửi vào nhóm chat.
2. **Giai đoạn 2 — phương án C (hoặc B nếu muốn tối giản).** Chỉ đẩy lên **bản tóm tắt tuần + sự kiện feed + cổ vũ**, theo mã nhóm. Log đầy đủ vẫn ở máy. Mất mạng thì app vẫn chạy, bảng nhóm hiện dữ liệu lần cuối.
3. **Giai đoạn 3 (tuỳ chọn).** Sao lưu log đầy đủ lên đám mây cho từng người; push nhắc nhở.

**Thiết kế dữ liệu để gắn đồng bộ sau không phải viết lại**
- ID dạng UUID sinh ở client (không dùng số tự tăng).
- Mỗi bản ghi có `profileId`, `updatedAt`, xoá mềm (`deletedAt`).
- Log chỉ thêm (append), mỗi người chỉ ghi dữ liệu của mình → gần như không có xung đột; "bản ghi mới hơn thắng" là đủ.
- Bản tóm tắt tuần là dữ liệu **suy ra** từ log, tính lại được bất kỳ lúc nào → mất dữ liệu trên máy chủ không gây hại.
- Streak tính ở client theo múi giờ của máy; máy chủ chỉ lưu kết quả.

## 10. Câu hỏi cần chốt với người dùng trước khi thiết kế

1. Nhóm có bao nhiêu người dùng iPhone / Android? (iOS quyết định rủi ro lưu trữ và push.)
2. Mọi người tập cùng một phòng hay nhiều phòng khác nhau? (Quyết định có cần nhiều hồ sơ phòng tập ngay từ đầu.)
3. Mục tiêu và trình độ từng người chênh nhau nhiều không? (Quyết định xếp hạng theo độ đều đặn hay cho phép so PR.)
4. Nhóm đã có nhóm chat chung chưa? Thẻ chia sẻ trong MVP đã đủ "xã hội" chưa, hay cần bảng nhóm trong app sớm?
5. Có chấp nhận đăng nhập (Google/email) ở giai đoạn 2, hay chỉ muốn mã nhóm không tài khoản?
6. Muốn kiểu cộng tác (streak nhóm, mục tiêu chung) hay đối đầu (thi đấu, xếp hạng)?
7. Phòng tập có những thiết bị gì, bước tạ nhỏ nhất bao nhiêu?

## Nguồn

Ghi chú độ tin cậy: **[chính chủ]** = trang của chính app; **[đối thủ]** = blog của app cạnh tranh, có thiên lệch; **[review]** = bên thứ ba, có thể có affiliate; **[trích đoạn]** = chỉ đọc được đoạn trích từ kết quả tìm kiếm, trang gốc trả 403.

- [S1] Fitbod Help — How Fitbod Creates Your Workout [chính chủ, trích đoạn]: https://help.fitbod.me/hc/en-us/articles/360004429814-How-Fitbod-Creates-Your-Workout
- [S2] Android Central — Fitbod review [review]: https://www.androidcentral.com/apps-software/fitbod-favorite-fitness-app-2023
- [S3] Hevy — Track Workouts [chính chủ]: https://www.hevyapp.com/features/track-workouts/
- [S4] JuggernautAI Help — How JuggernautAI is individualized to you [chính chủ]: https://help.jtsstrength.com/en/articles/3-how-juggernautai-is-individualized-to-you
- [S5] Garage Gym Reviews — JuggernautAI review [review]: https://garagegymreviews.com/juggernautai-review
- [S6] JEFIT blog — Fitbod vs Strong vs Jefit vs Hevy (2026) [đối thủ / chính chủ với JEFIT]: https://www.jefit.com/blog/fitbod-vs-strong-vs-jefit-vs-hevy
- [S7] RP Strength — Hypertrophy App [chính chủ]: https://rpstrength.com/hypertrophy-app
- [S8] Alpha Progression blog — Alpha Progression vs JuggernautAI [chính chủ với Alpha, đối thủ với Juggernaut]: https://alphaprogression.com/en/blog/alpha-progression-vs-juggernautai
- [S9] RP Help — How does the app determine when to add weight, reps and sets [chính chủ, trích đoạn]: https://help.rpstrength.com/hc/en-us/articles/32600173777815-How-does-the-app-determine-when-to-add-weight-reps-and-sets
- [S10] Garage Gym Reviews — Boostcamp review [review]: https://www.garagegymreviews.com/boostcamp-review
- [S11] Garage Gym Reviews — Caliber app review [review]: https://www.garagegymreviews.com/caliber-app-review
- [S12] Setgraph — Free Workout Apps on Reddit [đối thủ, tổng hợp lại ý kiến Reddit, trích đoạn]: https://setgraph.app/articles/best-workout-apps-free-reddit ; Boostcamp — JEFIT alternatives [đối thủ, trích đoạn]: https://www.boostcamp.app/alternatives/jefit
- [S13] Kết quả tìm kiếm review Fitbod [review, trích đoạn]: https://www.techradar.com/health-fitness/fitbod-app-review ; https://dr-muscle.com/fitbod-workout-app-review/ ; https://www.sensai.fit/blog/fitbod-review-2026
- [S14] Review người dùng Fitbod về gym profile [tổng hợp review App Store, trích đoạn]: https://justuseapp.com/en/app/1041517543/fitbod-gym-fitness-planner/reviews ; https://www.trustpilot.com/review/fitbod.me ; https://kimola.com/reports/unlock-insights-fitbod-app-customer-feedback-analysis-app-store-us-156948
- [S15] Review Strong [review / đối thủ, trích đoạn]: https://repreturn.com/strong-app-review/ ; https://www.sensai.fit/blog/strong-app-review-2026 ; https://www.boostcamp.app/best/workout-logging
- [S16] HotelGyms — review Hevy và hướng dẫn Alpha Progression [review, trích đoạn]: https://www.hotelgyms.com/blog/hevy-workout-app-review-the-up-and-comer-taking-the-fitness-world-by-storm ; https://www.hotelgyms.com/blog/how-to-use-alpha-progression
- [S17] Volt — How can I replace a movement in my workout [chính chủ, trích đoạn]: https://help.voltathletics.com/how-can-i-replace-a-movement-in-my-workout ; Gymkee — đổi bài trong buổi tập [chính chủ, trích đoạn]: https://gymkee.com/pl/help/athlete/zamiana-wicze-podczas-treningu-na-gymkee/
- [S18] Dr. Muscle — RP Hypertrophy App expert review [đối thủ]: https://dr-muscle.com/rp-hypertrophy-app-for-strength-training-expert-review/
- [S19] WebKit blog — Updates to Storage Policy [sơ cấp]: https://webkit.org/blog/14403/updates-to-storage-policy/
- [S20] WebKit Bugzilla 271401 (persist() luôn trả false) [trích đoạn]: https://lists.webkit.org/pipermail/webkit-unassigned/2024-March/1156201.html ; The Register về giới hạn 7 ngày và web app màn hình chính [trích đoạn]: https://www.theregister.com/2020/03/26/apple_relax_were_not_totally/
- [S21] iOS Safari Limitations [thứ cấp, trích đoạn]: https://swoff.netlify.app/docs/concepts/ios-safari-limitations
- [S22] Dexie Cloud pricing [chính chủ, trích đoạn]: https://dexie.org/cloud/pricing
- [S23] Supabase free tier 2026 [thứ cấp, trích đoạn]: https://dev.to/mahdi_benrhouma_fe1c6005/supabase-free-tier-limits-in-2026-what-you-actually-get-and-when-you-will-hit-them-4mhe
- [S24] Supabase — Do projects pause when inactive? [chính chủ, trích đoạn]: https://supabase.com/kb/faqs/platform/free-project-pausing
- [S25] Firebase — Understand Cloud Firestore billing [chính chủ, trích đoạn]: https://firebase.google.com/docs/firestore/pricing
- [S26] Neighbourhoodie — Offline-first with CouchDB and PouchDB in 2025 [thứ cấp, trích đoạn]: https://neighbourhood.ie/blog/2025/03/26/offline-first-with-couchdb-and-pouchdb-in-2025
- [S27] Duolingo blog — Improving the streak (19/11/2020) [chính chủ]: https://blog.duolingo.com/improving-the-streak
- [S28] Lenny's Newsletter — Jorge Mazal, How Duolingo reignited user growth [lời kể của Jorge Mazal, người trong cuộc ở Duolingo (chức danh chưa kiểm chứng)]: https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth
- [S29] Duolingo blog — Friend Streak, Friends Quests [chính chủ, trích đoạn]: https://blog.duolingo.com/friend-streak/ ; https://blog.duolingo.com/product-lessons-friend-streak/ ; https://blog.duolingo.com/friends-quests/ ; báo cáo lỗi Friends Quest [thứ cấp, trích đoạn]: https://piunikaweb.com/2025/11/05/duolingo-friend-quest-bugged/
- [S30] Nghiên cứu kudos Strava của ĐH Radboud, qua Canadian Running [thứ cấp, trích đoạn]: https://runningmagazine.ca/?p=91520 ; Strava Design — Understanding How Athletes Use the Feed [chính chủ, trích đoạn]: https://medium.com/strava-design/understanding-how-athletes-use-the-feed-aae986eaa818
- [S31] watchOS 11 tạm dừng vòng Activity [báo chí, trích đoạn]: https://www.imore.com/health-fitness/apple-watch/how-to-pause-activity-streaks-in-watchos-11 ; https://9to5mac.com/2024/07/16/close-your-ringsbut-in-watchos-11-its-okay-if-you-dont/ ; https://iphonelife.com/content/pause-activity-rings
- [S32] Phê bình streak trong app thể dục [bình luận, trích đoạn]: https://sixcolors.com/link/2023/06/apples-fitness-streaks-need-more-humanity/ ; https://www.androidauthority.com/fitbit-apple-fitness-rest-days-3163136 ; https://lumenlabs-website.pages.dev/article/rep/the-honest-streak-consistency-that-survives-a-deload/ ; Gentler Streak: https://apps.apple.com/us/app/gentler-streak-fitness-tracker/id1576857102
- [S33] So sánh NTC / Ladder / Future [đối thủ, trích đoạn]: https://www.trainwell.net/blog/best-fitness-accountability-apps-with-real-coaches-2026 ; https://www.corahealth.app/compare/ladder
- [S34] Thử nghiệm STEP UP, Patel và cộng sự, JAMA Internal Medicine 2019 [nghiên cứu bình duyệt, đọc qua bản ghi PubMed]: https://pubmed.ncbi.nlm.nih.gov/31498375/
- [S35] Nghiên cứu gamification trong app vận động [trích đoạn]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6826916 ; https://www.aminer.org/pub/62725cce5aee126c0fae866c/gamification-in-a-physical-activity-app-what-gamification-features-are-being-used ; https://aisel.aisnet.org/icis2015/proceedings/IShealth/14 ; https://eprints.lancs.ac.uk/236648/1/manuscript.pdf (PMC chặn truy cập tự động; chưa đọc được bài gốc nào trong nhóm này)
- [S36] Tổng hợp thí nghiệm streak goal của Duolingo [thứ cấp, trích đoạn]: https://lazyweb.com/research/duolingo-streak-goals-retention
- [S37] PocketBase FAQ và PocketHost FAQ [chính chủ, trích đoạn]: https://pocketbase.io/faq/ ; https://pockethost.io/docs/overview/faq/ ; so sánh chi phí [thứ cấp, trích đoạn]: https://dev.to/tienbuilds/pocketbase-cloud-vs-pockethost-an-honest-pricing-breakdown-5da5
- [S38] Duolingo blog — How the streak builds habit [chính chủ, trích đoạn]: https://blog.duolingo.com/how-duolingo-streak-builds-habit ; hướng dẫn bên thứ ba về Streak Freeze [trích đoạn]: https://duolingoguides.com/duolingo-streak-freeze ; https://techcult.com/how-to-freeze-streak-on-duolingo
- [S39] WebKit blog — Web Push for Web Apps on iOS and iPadOS [sơ cấp]: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/
- [S40] Hevy — Social features, Gym leaderboard, Social guide [chính chủ, trích đoạn]: https://www.hevyapp.com/features/social-features/ ; https://www.hevyapp.com/features/gym-leaderboard/ ; https://help.hevyapp.com/hc/en-us/articles/35688036014231-Hevy-App-Social-Guide-Connect-Follow-and-Share-Your-Workouts ; review [thứ cấp, trích đoạn]: https://www.whistleout.com/CellPhones/Apps/hevy-app-review
- [S41] Apple Support — Share your activity from Apple Watch [chính chủ, trích đoạn]: https://support.apple.com/guide/watch/apd68a69f5c7
