# Thư viện bài tập (02)

Tài liệu nghiên cứu cho app gym cá nhân của hai vợ chồng, tập ở phòng gym bình dân nơi nhiều máy có thể thiếu. Dữ liệu máy đọc nằm ở `exercises.json` cùng thư mục; hai file sinh ra từ cùng một nguồn nên luôn khớp nhau.

## Tóm tắt

- **90 bài tập** chia theo **15 nhóm chuyển động** (9 mẫu chuyển động chính + 6 nhóm isolation).
- Mỗi nhóm là một **thang thay thế** xếp đại thể từ nhiều dụng cụ tới ít dụng cụ: thanh đòn → tạ tay → máy/cáp → dây kháng lực → không dụng cụ. Riêng core xếp theo loại (chống ưỡn, chống xoay, gập bụng); vài nhóm thiếu bậc thanh đòn hoặc bậc không dụng cụ vì không có bài hợp lý.
- Mỗi bài có danh sách bài thay thế theo thứ tự ưu tiên. Đã kiểm bằng script: với **mọi** dụng cụ một bài cần, luôn có ít nhất một bài thay thế không cần dụng cụ đó, và mỗi nhóm đều có bậc cuối chỉ cần dây hoặc không cần gì.
- Độ tin cậy của hướng dẫn kỹ thuật: **18 bài** đã đọc nguồn và đối chiếu; **54 bài** có URL thật nhưng chưa đối chiếu nội dung; **18 bài** chưa có nguồn. Hai loại sau gắn nhãn [UNVERIFIED]: cue viết theo kiến thức huấn luyện phổ thông, nên xem video mẫu trước khi tập. Với bài đã đối chiếu, cue bám theo nguồn; phần lỗi thường gặp và mục "tránh nếu" có chỗ bổ sung theo kiến thức phổ thông khi nguồn không nêu.
- **Mức tạ khởi điểm** và **danh sách dụng cụ phòng gym cỏ** đều là ước lượng [UNVERIFIED], không tìm được nguồn đáng tin.
- ExRx.net và NSCA chặn truy cập tự động (lỗi 403), trang ACE từ chối kết nối, nên ba nguồn này không đối chiếu được. Nguồn thay thế chính là StrengthLog, Stronger By Science và Squat University.

## Quy ước dữ liệu

- `equipment[]` là điều kiện **VÀ**: phải có đủ mọi món trong danh sách. Trường hợp "cái này hoặc cái kia" được tách thành bài riêng. Bộ lọc của app chỉ cần kiểm tra mọi món của bài đều được tick.
- `substitutes[]` xếp bài gần giống nhất trước. **Quy tắc chọn:** lấy bài đầu tiên trong danh sách mà dụng cụ hôm đó đáp ứng được, **bỏ qua** bài có `beginner_ok: false` nếu người tập còn mới, và bỏ qua bài có `avoid_if` trùng với chỗ đau của người tập. Đã kiểm: sau khi lọc theo người mới, bài dành cho người mới vẫn luôn còn phương án thay cho từng dụng cụ.
- `cable_high` và `cable_low` tính cả ròng rọc trên máy kéo xô: phòng chỉ có máy kéo xô vẫn tick được `cable_high` (nếu tháo thanh thay tay cầm được) và `cable_low` (nếu có ròng rọc dưới).
- `single_implement: true` nghĩa là số kg của MỘT quả tạ ôm bằng hai tay, không phải kg mỗi tay.
- `difficulty`: 1 = dễ học, 2 = cần tập kỹ thuật vài buổi, 3 = khó, nên có người hướng dẫn. `beginner_ok` = có nên đưa vào giáo án tuần đầu hay không.
- `avoid_if` và `safer_alternative` là gợi ý chung, không phải tư vấn y khoa. Đau kéo dài thì đi khám.
- `load_type` cho biết app ghi nhận tải bằng đơn vị nào:

| load_type | Ý nghĩa |
|---|---|
| `barbell_kg` | Tổng kg trên thanh đòn (tính cả thanh) |
| `dumbbell_kg_per_hand` | Kg mỗi tay (tạ tay) |
| `kettlebell_kg` | Kg tạ ấm |
| `machine_kg` | Kg trên máy/cáp (số ghi trên chồng tạ, hoặc tổng bánh tạ lắp vào máy) |
| `added_kg` | Kg tạ lắp thêm, KHÔNG tính thanh/khung (Smith, landmine) |
| `band_level` | Mức dây kháng lực (light / medium / heavy) |
| `bodyweight_reps` | Số lần với trọng lượng cơ thể |
| `time_seconds` | Thời gian giữ (giây) |

- `measure`: `reps` (đếm lần), `seconds` (giữ theo giây), `meters` (đi theo quãng đường).

## Dụng cụ ở phòng gym cỏ [UNVERIFIED]

Không tìm được nguồn nào liệt kê thiết bị của phòng gym bình dân ở Việt Nam, nên bảng này là ước lượng theo kinh nghiệm chung. Hai vợ chồng nên đi một vòng phòng tập và tick lại cho đúng; cột "Mặc định" là trạng thái tick sẵn đề xuất cho checklist.

| Dụng cụ | id | Khả năng có | Mặc định | Ghi chú |
|---|---|---|---|---|
| Thanh đòn + bánh tạ | `barbell` | Thường có | tick | Thanh có thể không chuẩn 20 kg (10-15 kg); nên cân thử một lần. |
| Ghế đẩy ngực có giá đỡ | `bench_station` | Thường có | tick | Gần như phòng nào cũng có ít nhất một ghế. |
| Ghế phẳng | `bench_flat` | Thường có | tick |  |
| Tạ tay (tạ đơn) | `dumbbell` | Thường có | tick | Thường thiếu mức nhỏ (1-4 kg) và nhảy cóc 2,5-5 kg. |
| Xà đơn | `pullup_bar` | Thường có | tick |  |
| Máy kéo xô (có đệm chặn đùi) | `lat_pulldown` | Thường có | tick | Thường gộp chung với ròng rọc thấp để kéo ngang. |
| Khung Smith | `smith` | Thường có | tick |  |
| Ghế chỉnh độ dốc | `bench_incline` | Lúc có lúc không | bỏ trống |  |
| Ròng rọc cao (cáp trên) | `cable_high` | Thường có | tick | Tick nếu có máy cáp HOẶC đầu cáp trên của máy kéo xô tháo thanh ra gắn tay cầm khác được. |
| Ròng rọc thấp (cáp dưới) | `cable_low` | Lúc có lúc không | bỏ trống | Tick nếu có máy cáp HOẶC ròng rọc thấp gắn dưới máy kéo xô (chỗ kéo cáp ngang). |
| Máy đạp đùi | `leg_press` | Lúc có lúc không | bỏ trống |  |
| Máy đá đùi | `leg_extension` | Lúc có lúc không | bỏ trống | Hay là máy 2 trong 1 với móc đùi sau. |
| Máy móc đùi sau | `leg_curl` | Lúc có lúc không | bỏ trống |  |
| Máy đẩy ngực / ép ngực | `machine_chest` | Lúc có lúc không | bỏ trống |  |
| Xà kép | `dip_bar` | Lúc có lúc không | bỏ trống |  |
| Giá squat / khung power rack | `rack` | Lúc có lúc không | bỏ trống | Hay chỉ có giá đỡ không thanh an toàn; nhiều phòng không có. |
| Máy kéo ngang (row) | `machine_row` | Thường thiếu | bỏ trống |  |
| Máy đẩy vai | `machine_shoulder` | Thường thiếu | bỏ trống |  |
| Ghế gập lưng 45° | `back_extension` | Thường thiếu | bỏ trống |  |
| Máy nhón bắp chân | `calf_machine` | Thường thiếu | bỏ trống |  |
| Tạ ấm | `kettlebell` | Thường thiếu | bỏ trống |  |
| Dây kháng lực | `band` | Thường thiếu | bỏ trống | Phòng thường không có; nên tự mua mang theo (rẻ, gọn). |

Nên tự mua một bộ dây kháng lực (vài mức) mang theo: gần như nhóm nào cũng có một bài dùng dây làm phương án dự phòng.

## Bằng chứng nghiên cứu đáng chú ý [UNVERIFIED]

- **Hip thrust và squat cho mông:** Contreras 2015 đo EMG mông ở hip thrust cao hơn squat (13 nữ đã tập luyện). Plotkin 2023 (9 tuần, đo MRI) lại thấy mức tăng cơ mông tương đương. EMG cao không bảo đảm tăng cơ nhiều hơn, nên chọn bài theo dụng cụ sẵn có. https://pubmed.ncbi.nlm.nih.gov/26214739/
- **Móc đùi ngồi và nằm:** nghiên cứu PubMed 33009197 (tác giả và năm chưa xác nhận được), móc đùi ngồi tăng thể tích đùi sau nhiều hơn (+14% so với +9%, 12 tuần, 20 người). https://pubmed.ncbi.nlm.nih.gov/33009197/
- **Tay sau, tay qua đầu và tay xuôi:** Maeo 2022, duỗi khuỷu với tay qua đầu tăng cơ nhiều hơn (+19,9% so với +13,9%, 12 tuần, mẫu nhỏ). https://informahealthcare.com/doi/full/10.1080/17461391.2022.2100279
- **Chống đẩy và đẩy ngực:** Calatayud 2015, chống đẩy thêm dây cho EMG và mức tăng sức mạnh tương đương đẩy ngực 6RM (5 tuần, mẫu nhỏ). https://breakingmuscle.com/emg-analysis-of-the-bench-press-and-push-up/
- **Core cho người đau lưng:** bộ McGill Big 3 (curl-up, plank nghiêng, bird dog), giữ 10 giây, tháp giảm 5-3-1. https://squatuniversity.com/2018/06/21/the-mcgill-big-3-for-core-stability/

Các số liệu trên lấy từ tóm tắt kết quả tìm kiếm, chưa đọc toàn văn bài báo (PubMed không trả nội dung cho công cụ).

## Thang thay thế theo nhóm chuyển động

### Squat (gập gối)

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Squat thanh đòn (gánh tạ) | Thanh đòn + bánh tạ + Giá squat / khung power rack | 3 | chưa nên |
| 2 | Squat khung Smith | Khung Smith | 2 | được |
| 3 | Squat ôm tạ trước ngực | Tạ tay (tạ đơn) | 1 | được |
| 4 | Đạp đùi máy | Máy đạp đùi | 1 | được |
| 5 | Đá đùi máy | Máy đá đùi | 1 | được |
| 6 | Squat với dây kháng lực | Dây kháng lực | 1 | được |
| 7 | Squat không tạ (ngồi xuống ghế) | Không cần dụng cụ | 1 | được |

### Hinge (gập hông)

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Deadlift (kéo tạ từ sàn) | Thanh đòn + bánh tạ | 3 | chưa nên |
| 2 | Romanian deadlift thanh đòn | Thanh đòn + bánh tạ | 2 | được |
| 3 | Romanian deadlift tạ tay | Tạ tay (tạ đơn) | 1 | được |
| 4 | Kéo cáp qua háng | Ròng rọc thấp (cáp dưới) | 1 | được |
| 5 | Gập lưng ghế 45° | Ghế gập lưng 45° | 1 | được |
| 6 | Móc đùi sau máy | Máy móc đùi sau | 1 | được |
| 7 | Good morning với dây | Dây kháng lực | 1 | được |
| 8 | Romanian deadlift một chân không tạ | Không cần dụng cụ | 2 | được |

### Lunge / một chân

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Lunge lùi gánh thanh đòn | Thanh đòn + bánh tạ + Giá squat / khung power rack | 3 | chưa nên |
| 2 | Bulgarian split squat tạ tay | Tạ tay (tạ đơn) + Ghế phẳng | 3 | chưa nên |
| 3 | Lunge lùi tạ tay | Tạ tay (tạ đơn) | 2 | được |
| 4 | Bước lên bục với tạ tay | Tạ tay (tạ đơn) + Ghế phẳng | 2 | được |
| 5 | Split squat không tạ | Không cần dụng cụ | 1 | được |
| 6 | Lunge lùi không tạ | Không cần dụng cụ | 1 | được |

### Đẩy ngang

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Đẩy ngực thanh đòn | Thanh đòn + bánh tạ + Ghế đẩy ngực có giá đỡ | 3 | chưa nên |
| 2 | Đẩy ngực tạ tay | Tạ tay (tạ đơn) + Ghế phẳng | 2 | được |
| 3 | Đẩy ngực trên tạ tay (ghế dốc) | Tạ tay (tạ đơn) + Ghế chỉnh độ dốc | 2 | được |
| 4 | Đẩy ngực máy | Máy đẩy ngực / ép ngực | 1 | được |
| 5 | Đẩy ngực với dây | Dây kháng lực | 1 | được |
| 6 | Chống đẩy | Không cần dụng cụ | 2 | được |
| 7 | Chống đẩy kê tay cao | Không cần dụng cụ | 1 | được |

### Đẩy dọc (qua đầu)

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Đẩy vai thanh đòn đứng | Thanh đòn + bánh tạ + Giá squat / khung power rack | 3 | chưa nên |
| 2 | Đẩy vai tạ tay | Tạ tay (tạ đơn) | 2 | được |
| 3 | Đẩy vai máy | Máy đẩy vai | 1 | được |
| 4 | Đẩy landmine (thanh đòn chống góc) | Thanh đòn + bánh tạ | 2 | được |
| 5 | Đẩy vai với dây | Dây kháng lực | 1 | được |
| 6 | Chống đẩy chổng mông (pike) | Không cần dụng cụ | 2 | được |

### Kéo ngang

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Kéo thanh đòn gập người | Thanh đòn + bánh tạ | 3 | chưa nên |
| 2 | Kéo tạ tay một bên | Tạ tay (tạ đơn) + Ghế phẳng | 1 | được |
| 3 | Kéo cáp ngang ngồi | Ròng rọc thấp (cáp dưới) | 1 | được |
| 4 | Kéo ngang máy (tì ngực) | Máy kéo ngang (row) | 1 | được |
| 5 | Kéo người dưới thanh (inverted row) | Khung Smith | 2 | được |
| 6 | Kéo dây ngang | Dây kháng lực | 1 | được |
| 7 | Nằm sấp kéo tay (W raise) | Không cần dụng cụ | 1 | được |

### Kéo dọc

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Hít xà đơn | Xà đơn | 3 | chưa nên |
| 2 | Hít xà có dây trợ lực | Xà đơn + Dây kháng lực | 2 | được |
| 3 | Hít xà chiều xuống (negative) | Xà đơn | 2 | được |
| 4 | Kéo xô máy | Máy kéo xô (có đệm chặn đùi) | 1 | được |
| 5 | Kéo cáp thẳng tay | Ròng rọc cao (cáp trên) | 1 | được |
| 6 | Kéo xô với dây | Dây kháng lực | 1 | được |

### Core (thân giữa)

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Plank · chống ưỡn | Không cần dụng cụ | 1 | được |
| 2 | Dead bug · chống ưỡn | Không cần dụng cụ | 1 | được |
| 3 | Plank nghiêng · chống xoay / nghiêng | Không cần dụng cụ | 1 | được |
| 4 | Bird dog · chống xoay / nghiêng | Không cần dụng cụ | 1 | được |
| 5 | Pallof press với cáp · chống xoay / nghiêng | Ròng rọc cao (cáp trên) | 1 | được |
| 6 | Pallof press với dây · chống xoay / nghiêng | Dây kháng lực | 1 | được |
| 7 | Gập bụng McGill (curl-up) · gập bụng | Không cần dụng cụ | 1 | được |
| 8 | Gập bụng cáp (quỳ) · gập bụng | Ròng rọc cao (cáp trên) | 2 | được |
| 9 | Gập bụng ngược (nâng chân co gối) · gập bụng | Không cần dụng cụ | 1 | được |

### Mang vác

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Đi bộ xách tạ hai tay | Tạ tay (tạ đơn) | 1 | được |
| 2 | Đi bộ xách tạ một tay | Tạ tay (tạ đơn) | 1 | được |
| 3 | Đi bộ ôm tạ ấm trước ngực | Tạ ấm | 1 | được |
| 4 | Bò gấu | Không cần dụng cụ | 2 | được |

### Tay trước (isolation)

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Cuốn tay trước thanh đòn | Thanh đòn + bánh tạ | 1 | được |
| 2 | Cuốn tay trước tạ tay | Tạ tay (tạ đơn) | 1 | được |
| 3 | Cuốn tay kiểu búa | Tạ tay (tạ đơn) | 1 | được |
| 4 | Cuốn tay trước cáp | Ròng rọc thấp (cáp dưới) | 1 | được |
| 5 | Cuốn tay trước với dây | Dây kháng lực | 1 | được |

### Tay sau (isolation)

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Duỗi tay sau nằm (skullcrusher) | Thanh đòn + bánh tạ + Ghế phẳng | 2 | được |
| 2 | Duỗi tay sau qua đầu tạ tay | Tạ tay (tạ đơn) | 1 | được |
| 3 | Đẩy cáp tay sau | Ròng rọc cao (cáp trên) | 1 | được |
| 4 | Chống xà kép | Xà kép | 3 | chưa nên |
| 5 | Đẩy dây tay sau | Dây kháng lực | 1 | được |
| 6 | Chống đẩy tay hẹp | Không cần dụng cụ | 2 | được |

### Vai giữa (isolation)

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Kéo thanh đòn lên cằm (nắm rộng) | Thanh đòn + bánh tạ | 2 | chưa nên |
| 2 | Dang tạ ngang vai | Tạ tay (tạ đơn) | 1 | được |
| 3 | Dang cáp ngang vai | Ròng rọc thấp (cáp dưới) | 1 | được |
| 4 | Dang dây ngang vai | Dây kháng lực | 1 | được |

### Bắp chân (isolation)

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Nhón bắp chân máy đứng | Máy nhón bắp chân | 1 | được |
| 2 | Nhón bắp chân khung Smith | Khung Smith | 1 | được |
| 3 | Nhón bắp chân trên máy đạp đùi | Máy đạp đùi | 1 | được |
| 4 | Nhón bắp chân một chân cầm tạ | Tạ tay (tạ đơn) | 1 | được |
| 5 | Nhón bắp chân một chân không tạ | Không cần dụng cụ | 1 | được |

### Mông / hip thrust

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Hip thrust thanh đòn | Thanh đòn + bánh tạ + Ghế phẳng | 2 | được |
| 2 | Hip thrust tạ tay | Tạ tay (tạ đơn) + Ghế phẳng | 1 | được |
| 3 | Đá mông với cáp | Ròng rọc thấp (cáp dưới) | 1 | được |
| 4 | Cầu mông với dây | Dây kháng lực | 1 | được |
| 5 | Cầu mông một chân | Không cần dụng cụ | 2 | được |
| 6 | Cầu mông | Không cần dụng cụ | 1 | được |

### Vai sau (isolation)

| Bậc | Bài | Dụng cụ | Độ khó | Người mới |
|---|---|---|---|---|
| 1 | Dang tạ vai sau (gập người) | Tạ tay (tạ đơn) | 1 | được |
| 2 | Face pull với cáp | Ròng rọc cao (cáp trên) | 1 | được |
| 3 | Kéo giãn dây ngang ngực | Dây kháng lực | 1 | được |
| 4 | Nằm sấp nâng tay chữ Y | Không cần dụng cụ | 1 | được |

## Chi tiết từng bài

### Squat (gập gối)

#### Squat thanh đòn (gánh tạ) / Barbell Back Squat

- **id:** `barbell_back_squat`
- **Dụng cụ:** Thanh đòn + bánh tạ + Giá squat / khung power rack (`barbell`, `rack`)
- **Cơ chính:** Đùi trước, Mông. **Cơ phụ:** Đùi trong, Cơ dựng sống (lưng dưới), Bụng.
- **Độ khó:** 3/3. **Người mới:** chưa nên, tập bài dễ hơn trong thang trước.
- **Kỹ thuật:** (1) Hít sâu bằng bụng, gồng bụng như sắp bị đấm rồi mới xuống; (2) Chân rộng khoảng bằng vai, mũi chân xoay ra 15-20°; (3) Gối đi cùng hướng mũi chân (qua ngón 1-2); (4) Xuống sâu nhất trong tầm kiểm soát, đứng lên dứt khoát.
- **Lỗi thường gặp:** Đặt thanh đè lên đốt sống cổ thay vì lên cơ cầu vai; Mông bật lên trước, biến thành động tác cúi lưng (good morning); Móc thanh đặt quá cao phải kiễng chân mới nhấc ra.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`); đau lưng dưới → tập Squat ôm tạ trước ngực (`goblet_squat`); đau vai → tập Squat ôm tạ trước ngực (`goblet_squat`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 20 kg (cả thanh), nữ 15 kg (cả thanh). Bắt đầu bằng thanh trống. Nữ nên dùng thanh nhẹ 10-15 kg nếu có; chưa vững thì tập goblet squat trước.
- **Thay thế (theo thứ tự):** Squat khung Smith (`smith_squat`) → Squat ôm tạ trước ngực (`goblet_squat`) → Đạp đùi máy (`leg_press`) → Squat không tạ (ngồi xuống ghế) (`bodyweight_squat`).
- **Nguồn:** https://www.strongerbyscience.com/how-to-squat/ · đã đọc và đối chiếu.

#### Squat khung Smith / Smith Machine Squat

- **id:** `smith_squat`
- **Dụng cụ:** Khung Smith (`smith`)
- **Cơ chính:** Đùi trước, Mông. **Cơ phụ:** Đùi trong.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đặt chân hơi đưa ra trước thanh một chút; (2) Gồng bụng, lưng thẳng tự nhiên; (3) Xuống tới khi đùi ngang hoặc thấp hơn sàn; (4) Gối cùng hướng mũi chân, bàn chân bám phẳng.
- **Lỗi thường gặp:** Nhấc gót khỏi sàn; Để gối đổ vào trong; Quên xoay khóa móc an toàn khi kết thúc.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`); đau lưng dưới → tập Split squat không tạ (`split_squat_bodyweight`).
- **Kiểu tải:** `added_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 10 kg lắp thêm, nữ chưa lắp thêm tạ. Số kg là tạ lắp thêm; thanh Smith tự nặng khoảng 7-20 kg tùy máy.
- **Thay thế (theo thứ tự):** Squat thanh đòn (gánh tạ) (`barbell_back_squat`) → Đạp đùi máy (`leg_press`) → Squat ôm tạ trước ngực (`goblet_squat`) → Squat không tạ (ngồi xuống ghế) (`bodyweight_squat`).
- **Nguồn:** https://www.strengthlog.com/smith-machine-squat/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Squat ôm tạ trước ngực / Goblet Squat

- **id:** `goblet_squat`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Đùi trước, Mông, Đùi trong. **Cơ phụ:** Cơ dựng sống (lưng dưới), Bụng, Bắp chân.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Ôm một quả tạ sát ngực; (2) Chân rộng bằng vai, mũi chân hơi xoay ra; (3) Hít vào, gồng nhẹ bụng, ngồi xuống sâu nhất mà vẫn thoải mái; (4) Mũi chân cùng hướng với đường đi của gối.
- **Lỗi thường gặp:** Để tạ rời xa ngực làm đổ người ra trước; Gối đổ vào trong; Xuống quá nông.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`); đau cổ tay → tập Đạp đùi máy (`leg_press`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 10 kg (một quả tạ), nữ 6 kg (một quả tạ). Chỉ dùng MỘT quả tạ, số kg là của quả tạ đó. Có tạ ấm thì cầm tạ ấm cũng được.
- **Thay thế (theo thứ tự):** Đạp đùi máy (`leg_press`) → Squat khung Smith (`smith_squat`) → Squat với dây kháng lực (`band_squat`) → Squat không tạ (ngồi xuống ghế) (`bodyweight_squat`).
- **Nguồn:** https://www.strengthlog.com/goblet-squat/ · đã đọc và đối chiếu.

#### Đạp đùi máy / Leg Press

- **id:** `leg_press`
- **Dụng cụ:** Máy đạp đùi (`leg_press`)
- **Cơ chính:** Đùi trước, Mông. **Cơ phụ:** Đùi trong, Đùi sau.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Lưng và mông áp sát đệm suốt động tác; (2) Chân rộng bằng vai, đặt giữa bàn đạp; (3) Hạ tới khi gối gập khoảng 90° hoặc sâu hơn mà mông không cuộn lên; (4) Đạp bằng cả bàn chân, không khóa cứng gối ở trên.
- **Lỗi thường gặp:** Hạ quá sâu làm mông cuộn khỏi đệm (tròn lưng dưới); Khóa cứng gối đột ngột; Dùng tay đẩy vào đầu gối.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`); đau lưng dưới → tập Squat ôm tạ trước ngực (`goblet_squat`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 40 kg, nữ 20 kg.
- **Thay thế (theo thứ tự):** Squat khung Smith (`smith_squat`) → Squat ôm tạ trước ngực (`goblet_squat`) → Squat thanh đòn (gánh tạ) (`barbell_back_squat`) → Squat với dây kháng lực (`band_squat`).
- **Nguồn:** https://www.strengthlog.com/leg-press/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Đá đùi máy / Leg Extension

- **id:** `leg_extension`
- **Dụng cụ:** Máy đá đùi (`leg_extension`)
- **Cơ chính:** Đùi trước. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Chỉnh trục máy ngang với khớp gối; (2) Đệm tì ngay trên cổ chân; (3) Duỗi thẳng gối, siết đùi 1 giây; (4) Hạ chậm 2-3 giây.
- **Lỗi thường gặp:** Vung tạ lấy đà; Nhấc mông khỏi ghế; Tạ quá nặng nên chỉ đi nửa biên độ.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 15 kg, nữ 10 kg.
- **Thay thế (theo thứ tự):** Squat ôm tạ trước ngực (`goblet_squat`) → Split squat không tạ (`split_squat_bodyweight`) → Bước lên bục với tạ tay (`step_up_dumbbell`) → Squat với dây kháng lực (`band_squat`).
- **Nguồn:** https://www.strengthlog.com/leg-extension/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Squat với dây kháng lực / Banded Squat

- **id:** `band_squat`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Đùi trước, Mông. **Cơ phụ:** Đùi trong.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Giẫm lên dây bằng hai chân, vòng dây lên vai hoặc cầm ngang vai; (2) Gồng bụng, ngực mở; (3) Ngồi xuống sâu, gối cùng hướng mũi chân; (4) Đứng lên hết tầm, giữ dây căng.
- **Lỗi thường gặp:** Dây tuột khỏi bàn chân; Chùng dây ở đáy nên gần như không có lực cản; Gối đổ vào trong.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây vừa, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Squat ôm tạ trước ngực (`goblet_squat`) → Squat không tạ (ngồi xuống ghế) (`bodyweight_squat`) → Đạp đùi máy (`leg_press`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Squat không tạ (ngồi xuống ghế) / Bodyweight / Box Squat

- **id:** `bodyweight_squat`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Đùi trước, Mông. **Cơ phụ:** Đùi trong.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Chân rộng bằng vai, tay đưa ra trước giữ thăng bằng; (2) Đẩy hông ra sau và gập gối cùng lúc; (3) Chạm nhẹ mông xuống ghế/bục rồi đứng lên; (4) Cả bàn chân bám sàn.
- **Lỗi thường gặp:** Ngồi phịch xuống ghế mất kiểm soát; Nhấc gót; Gối đổ vào trong.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Squat với dây kháng lực (`band_squat`) → Squat ôm tạ trước ngực (`goblet_squat`) → Split squat không tạ (`split_squat_bodyweight`).
- **Nguồn:** https://www.strengthlog.com/air-squat/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

### Hinge (gập hông)

#### Deadlift (kéo tạ từ sàn) / Conventional Deadlift

- **id:** `conventional_deadlift`
- **Dụng cụ:** Thanh đòn + bánh tạ (`barbell`)
- **Cơ chính:** Mông, Đùi sau, Cơ dựng sống (lưng dưới). **Cơ phụ:** Đùi trước, Cầu vai / thang, Xô, Cẳng tay / lực nắm.
- **Độ khó:** 3/3. **Người mới:** chưa nên, tập bài dễ hơn trong thang trước.
- **Kỹ thuật:** (1) Thanh nằm trên giữa bàn chân (ngang dây giày), cách ống chân 2-5 cm; (2) Hít sâu bằng bụng, gồng cứng, giữ hơi suốt lần kéo; (3) Hạ bả vai, siết xô ("nhét bả vai vào túi quần sau"); (4) Căng người trước rồi mới kéo; lưng dưới luôn thẳng và cứng.
- **Lỗi thường gặp:** Giật thanh khỏi sàn làm mông bật lên, lưng tròn; Để thanh trôi ra xa người; Co tay kéo thay vì để tay thẳng như sợi dây.
- **Tránh nếu:** đau lưng dưới → tập Cầu mông (`glute_bridge`); đau gối → tập Romanian deadlift tạ tay (`romanian_deadlift_dumbbell`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 40 kg (cả thanh), nữ 30 kg (cả thanh). Bánh tạ nhỏ làm thanh quá thấp: kê thanh lên bục/bánh tạ để thanh cao ngang giữa ống chân.
- **Thay thế (theo thứ tự):** Romanian deadlift tạ tay (`romanian_deadlift_dumbbell`) → Gập lưng ghế 45° (`back_extension_45`) → Kéo cáp qua háng (`cable_pull_through`) → Good morning với dây (`band_good_morning`).
- **Nguồn:** https://www.strongerbyscience.com/how-to-deadlift/ · đã đọc và đối chiếu.

#### Romanian deadlift thanh đòn / Barbell Romanian Deadlift

- **id:** `romanian_deadlift_barbell`
- **Dụng cụ:** Thanh đòn + bánh tạ (`barbell`)
- **Cơ chính:** Mông, Đùi sau, Cơ dựng sống (lưng dưới). **Cơ phụ:** Đùi trong, Cầu vai / thang, Cẳng tay / lực nắm.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Bắt đầu ở tư thế đứng thẳng cầm thanh; (2) Hít vào, gồng nhẹ bụng, đẩy hông ra sau, gối gần thẳng; (3) Hạ thanh sâu nhất mà lưng vẫn giữ trung tính (không cần chạm sàn); (4) Đẩy hông về trước để đứng lên, thở ra.
- **Lỗi thường gặp:** Tròn lưng; Gập gối nhiều biến thành squat; Không gồng bụng trước mỗi lần.
- **Tránh nếu:** đau lưng dưới → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 30 kg (cả thanh), nữ 20 kg (cả thanh).
- **Thay thế (theo thứ tự):** Romanian deadlift tạ tay (`romanian_deadlift_dumbbell`) → Kéo cáp qua háng (`cable_pull_through`) → Gập lưng ghế 45° (`back_extension_45`) → Good morning với dây (`band_good_morning`).
- **Nguồn:** https://www.strengthlog.com/romanian-deadlift/ · đã đọc và đối chiếu.

#### Romanian deadlift tạ tay / Dumbbell Romanian Deadlift

- **id:** `romanian_deadlift_dumbbell`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Mông, Đùi sau. **Cơ phụ:** Cơ dựng sống (lưng dưới), Cẳng tay / lực nắm.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Hai tạ trước đùi, gối hơi chùng; (2) Đẩy hông ra sau như đóng cửa bằng mông; (3) Tạ trượt sát chân, lưng giữ thẳng; (4) Xuống tới khi căng đùi sau rồi đẩy hông lên.
- **Lỗi thường gặp:** Tròn lưng; Tạ đưa xa người; Ngửa cổ nhìn gương.
- **Tránh nếu:** đau lưng dưới → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 10 kg/tay, nữ 6 kg/tay.
- **Thay thế (theo thứ tự):** Romanian deadlift thanh đòn (`romanian_deadlift_barbell`) → Kéo cáp qua háng (`cable_pull_through`) → Gập lưng ghế 45° (`back_extension_45`) → Good morning với dây (`band_good_morning`) → Romanian deadlift một chân không tạ (`single_leg_rdl_bodyweight`).
- **Nguồn:** https://www.strengthlog.com/dumbbell-romanian-deadlift/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Kéo cáp qua háng / Cable Pull-Through

- **id:** `cable_pull_through`
- **Dụng cụ:** Ròng rọc thấp (cáp dưới) (`cable_low`)
- **Cơ chính:** Mông, Đùi sau. **Cơ phụ:** Cơ dựng sống (lưng dưới).
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Quay lưng về máy, cầm dây thừng giữa hai chân, bước ra cho căng cáp; (2) Đẩy hông ra sau, lưng thẳng; (3) Đẩy hông về trước và siết mông để đứng thẳng; (4) Tay chỉ giữ dây, không kéo bằng tay.
- **Lỗi thường gặp:** Squat xuống thay vì gập hông; Ngả người ra sau quá mức ở trên; Kéo bằng tay và vai.
- **Tránh nếu:** đau lưng dưới → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 15 kg, nữ 10 kg.
- **Thay thế (theo thứ tự):** Romanian deadlift tạ tay (`romanian_deadlift_dumbbell`) → Good morning với dây (`band_good_morning`) → Gập lưng ghế 45° (`back_extension_45`) → Cầu mông (`glute_bridge`).
- **Nguồn:** https://www.strengthlog.com/cable-pull-through/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Gập lưng ghế 45° / 45° Back Extension

- **id:** `back_extension_45`
- **Dụng cụ:** Ghế gập lưng 45° (`back_extension`)
- **Cơ chính:** Cơ dựng sống (lưng dưới), Mông, Đùi sau. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đệm tì dưới nếp gập hông để hông gập tự do; (2) Hạ người với lưng thẳng; (3) Siết mông để nâng lên tới khi thân thẳng hàng với chân; (4) Lên xuống chậm, có kiểm soát.
- **Lỗi thường gặp:** Ưỡn lưng quá mức ở trên; Giật người lấy đà; Đệm đặt quá cao chặn hông.
- **Tránh nếu:** đau lưng dưới → tập Bird dog (`bird_dog`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Romanian deadlift tạ tay (`romanian_deadlift_dumbbell`) → Good morning với dây (`band_good_morning`) → Kéo cáp qua háng (`cable_pull_through`) → Romanian deadlift một chân không tạ (`single_leg_rdl_bodyweight`).
- **Nguồn:** https://www.strengthlog.com/back-extension/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Móc đùi sau máy / Leg Curl (seated / lying)

- **id:** `leg_curl_machine`
- **Dụng cụ:** Máy móc đùi sau (`leg_curl`)
- **Cơ chính:** Đùi sau. **Cơ phụ:** Bắp chân.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Chỉnh trục máy ngang khớp gối; (2) Giữ hông áp sát đệm; (3) Co gối hết tầm, siết 1 giây; (4) Duỗi chậm 2-3 giây tới gần thẳng.
- **Lỗi thường gặp:** Nhấc hông để lấy đà; Thả tạ rơi tự do; Đi nửa biên độ.
- **Tránh nếu:** đau lưng dưới → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 15 kg, nữ 10 kg.
- **Thay thế (theo thứ tự):** Romanian deadlift tạ tay (`romanian_deadlift_dumbbell`) → Gập lưng ghế 45° (`back_extension_45`) → Cầu mông một chân (`single_leg_glute_bridge`) → Good morning với dây (`band_good_morning`).
- **Nghiên cứu:** [UNVERIFIED, theo tóm tắt tìm kiếm] Nghiên cứu PubMed 33009197: móc đùi NGỒI tăng thể tích đùi sau nhiều hơn móc đùi NẰM (+14% so với +9%, 12 tuần, 20 người). Có cả hai máy thì ưu tiên máy ngồi.
- **Nguồn:** https://www.strengthlog.com/seated-leg-curl/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Good morning với dây / Banded Good Morning

- **id:** `band_good_morning`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Đùi sau, Mông, Cơ dựng sống (lưng dưới). **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Giẫm lên dây, vòng đầu kia qua sau cổ/vai; (2) Gối hơi chùng, đẩy hông ra sau; (3) Lưng thẳng, cúi tới khi căng đùi sau; (4) Đẩy hông về trước để đứng lên.
- **Lỗi thường gặp:** Tròn lưng; Gập gối nhiều; Dây tì thẳng lên cổ gây đau (nên đặt trên cầu vai).
- **Tránh nếu:** đau lưng dưới → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây vừa, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Romanian deadlift tạ tay (`romanian_deadlift_dumbbell`) → Kéo cáp qua háng (`cable_pull_through`) → Romanian deadlift một chân không tạ (`single_leg_rdl_bodyweight`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Romanian deadlift một chân không tạ / Bodyweight Single-Leg RDL

- **id:** `single_leg_rdl_bodyweight`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Đùi sau, Mông. **Cơ phụ:** Cơ dựng sống (lưng dưới), Mông nhỡ (dạng hông).
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đứng một chân, gối trụ hơi chùng; (2) Gập hông, chân sau duỗi thẳng ra sau như bập bênh; (3) Hông giữ song song sàn, không xoay mở; (4) Có thể vịn nhẹ tường để giữ thăng bằng.
- **Lỗi thường gặp:** Xoay mở hông; Tròn lưng; Làm quá nhanh nên mất thăng bằng.
- **Tránh nếu:** đau lưng dưới → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Good morning với dây (`band_good_morning`) → Romanian deadlift tạ tay (`romanian_deadlift_dumbbell`) → Cầu mông (`glute_bridge`).
- **Nguồn:** https://www.strengthlog.com/single-leg-romanian-deadlift/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

### Lunge / một chân

#### Lunge lùi gánh thanh đòn / Barbell Reverse Lunge

- **id:** `barbell_reverse_lunge`
- **Dụng cụ:** Thanh đòn + bánh tạ + Giá squat / khung power rack (`barbell`, `rack`)
- **Cơ chính:** Đùi trước, Mông. **Cơ phụ:** Đùi trong, Đùi sau.
- **Độ khó:** 3/3. **Người mới:** chưa nên, tập bài dễ hơn trong thang trước.
- **Kỹ thuật:** (1) Gánh thanh như squat, gồng bụng; (2) Bước lùi một bước dài, hạ gối sau gần chạm sàn; (3) Đạp chân trước để về vị trí cũ; (4) Thân người thẳng, hơi ngả trước nhẹ.
- **Lỗi thường gặp:** Bước quá ngắn làm gót trước nhấc lên; Gối trước đổ vào trong; Đập gối sau xuống sàn.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`); đau lưng dưới → tập Lunge lùi tạ tay (`reverse_lunge_dumbbell`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 20 kg (cả thanh), nữ 15 kg (cả thanh).
- **Thay thế (theo thứ tự):** Lunge lùi tạ tay (`reverse_lunge_dumbbell`) → Bulgarian split squat tạ tay (`bulgarian_split_squat_dumbbell`) → Split squat không tạ (`split_squat_bodyweight`).
- **Nguồn:** https://www.strengthlog.com/barbell-lunge/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Bulgarian split squat tạ tay / Dumbbell Bulgarian Split Squat

- **id:** `bulgarian_split_squat_dumbbell`
- **Dụng cụ:** Tạ tay (tạ đơn) + Ghế phẳng (`dumbbell`, `bench_flat`)
- **Cơ chính:** Đùi trước, Mông, Đùi trong. **Cơ phụ:** không đáng kể.
- **Độ khó:** 3/3. **Người mới:** chưa nên, tập bài dễ hơn trong thang trước.
- **Kỹ thuật:** (1) Đứng cách ghế một bước dài, đặt mu bàn chân sau lên ghế; (2) Hít vào, hạ có kiểm soát tới khi gối sau gần chạm sàn; (3) Thở ra, đạp lên bằng chân trước; (4) Chân sau chỉ để giữ thăng bằng, không dùng để đẩy.
- **Lỗi thường gặp:** Gối trước đổ vào trong; Đổ người ra trước; Dùng chân sau để đẩy.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 5 kg/tay, nữ 2 kg/tay. Tập không tạ cho vững trước rồi mới cầm tạ.
- **Thay thế (theo thứ tự):** Lunge lùi tạ tay (`reverse_lunge_dumbbell`) → Split squat không tạ (`split_squat_bodyweight`) → Lunge lùi không tạ (`reverse_lunge_bodyweight`) → Đạp đùi máy (`leg_press`).
- **Nguồn:** https://www.strengthlog.com/bulgarian-split-squat/ · đã đọc và đối chiếu.

#### Lunge lùi tạ tay / Dumbbell Reverse Lunge

- **id:** `reverse_lunge_dumbbell`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Đùi trước, Mông. **Cơ phụ:** Đùi trong, Đùi sau.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Hai tạ thả hai bên hông; (2) Bước lùi dài, hạ thẳng xuống; (3) Gối trước cùng hướng mũi chân; (4) Đạp gót chân trước để đứng lên.
- **Lỗi thường gặp:** Bước ngắn; Thân đổ ra trước; Gối trước đổ vào trong.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 6 kg/tay, nữ 4 kg/tay.
- **Thay thế (theo thứ tự):** Lunge lùi gánh thanh đòn (`barbell_reverse_lunge`) → Lunge lùi không tạ (`reverse_lunge_bodyweight`) → Split squat không tạ (`split_squat_bodyweight`) → Đạp đùi máy (`leg_press`).
- **Nguồn:** https://www.strengthlog.com/dumbbell-lunge/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Bước lên bục với tạ tay / Dumbbell Step-Up

- **id:** `step_up_dumbbell`
- **Dụng cụ:** Tạ tay (tạ đơn) + Ghế phẳng (`dumbbell`, `bench_flat`)
- **Cơ chính:** Đùi trước, Mông. **Cơ phụ:** Bắp chân.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đặt cả bàn chân lên bục/ghế chắc chắn; (2) Đạp bằng chân trên bục để đứng lên; (3) Hạ xuống chậm bằng chính chân đó; (4) Chọn bục cao ngang gối hoặc thấp hơn.
- **Lỗi thường gặp:** Nhún chân dưới để lấy đà; Gối đổ vào trong; Bục quá cao làm nghiêng hông.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 5 kg/tay, nữ 3 kg/tay.
- **Thay thế (theo thứ tự):** Lunge lùi tạ tay (`reverse_lunge_dumbbell`) → Lunge lùi không tạ (`reverse_lunge_bodyweight`) → Split squat không tạ (`split_squat_bodyweight`).
- **Nguồn:** https://www.strengthlog.com/step-up/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Split squat không tạ / Bodyweight Split Squat

- **id:** `split_squat_bodyweight`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Đùi trước, Mông. **Cơ phụ:** Đùi trong.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đứng tư thế chân trước chân sau, hai chân rộng bằng hông; (2) Hạ thẳng xuống, gối sau gần chạm sàn; (3) Dồn trọng tâm vào chân trước; (4) Vịn tường nếu chưa vững.
- **Lỗi thường gặp:** Hai chân trên một đường thẳng nên mất thăng bằng; Đẩy bằng chân sau; Gối trước đổ vào trong.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Lunge lùi không tạ (`reverse_lunge_bodyweight`) → Squat không tạ (ngồi xuống ghế) (`bodyweight_squat`) → Lunge lùi tạ tay (`reverse_lunge_dumbbell`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Lunge lùi không tạ / Bodyweight Reverse Lunge

- **id:** `reverse_lunge_bodyweight`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Đùi trước, Mông. **Cơ phụ:** Đùi trong, Đùi sau.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Bước lùi một bước dài; (2) Hạ gối sau gần chạm sàn; (3) Thân thẳng, bụng gồng nhẹ; (4) Đạp chân trước để đứng lên.
- **Lỗi thường gặp:** Bước ngắn làm gót trước nhấc; Gối trước đổ vào trong; Đập gối xuống sàn.
- **Tránh nếu:** đau gối → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Split squat không tạ (`split_squat_bodyweight`) → Squat không tạ (ngồi xuống ghế) (`bodyweight_squat`) → Lunge lùi tạ tay (`reverse_lunge_dumbbell`).
- **Nguồn:** https://www.strengthlog.com/reverse-body-weight-lunges/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

### Đẩy ngang

#### Đẩy ngực thanh đòn / Barbell Bench Press

- **id:** `barbell_bench_press`
- **Dụng cụ:** Thanh đòn + bánh tạ + Ghế đẩy ngực có giá đỡ (`barbell`, `bench_station`)
- **Cơ chính:** Ngực, Vai trước. **Cơ phụ:** Tay sau.
- **Độ khó:** 3/3. **Người mới:** chưa nên, tập bài dễ hơn trong thang trước.
- **Kỹ thuật:** (1) Kéo hai bả vai ra sau, ưỡn ngực lên, chân đạp chắc xuống sàn; (2) Nắm rộng hơn vai (khoảng 1,5-2 lần vai), cổ tay thẳng trên khuỷu; (3) Hạ có kiểm soát 2-3 giây, chạm khoảng giữa núm ngực và đáy xương ức; (4) Đẩy lên và hơi ngược về phía mặt, kết thúc thanh trên vai.
- **Lỗi thường gặp:** Vai trượt, mất tư thế siết bả vai; Chạm thanh quá thấp dưới xương ức (dễ căng vai); Bẻ ngửa cổ tay dưới tải.
- **Tránh nếu:** đau vai → tập Chống đẩy kê tay cao (`incline_push_up`); đau cổ tay → tập Đẩy ngực máy (`machine_chest_press`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 20 kg (cả thanh), nữ 15 kg (cả thanh). Thanh trống. Tập nặng phải có người đỡ; không kẹp khóa tạ khi tập một mình.
- **Thay thế (theo thứ tự):** Đẩy ngực tạ tay (`dumbbell_bench_press`) → Đẩy ngực máy (`machine_chest_press`) → Chống đẩy (`push_up`) → Đẩy ngực với dây (`band_chest_press`).
- **Nguồn:** https://www.strongerbyscience.com/how-to-bench/ · đã đọc và đối chiếu.

#### Đẩy ngực tạ tay / Dumbbell Bench Press

- **id:** `dumbbell_bench_press`
- **Dụng cụ:** Tạ tay (tạ đơn) + Ghế phẳng (`dumbbell`, `bench_flat`)
- **Cơ chính:** Ngực, Vai trước. **Cơ phụ:** Tay sau.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Siết bả vai ra sau và xuống; (2) Khuỷu tay mở khoảng 45-60° so với thân; (3) Hạ tạ tới ngang ngực, cẳng tay thẳng đứng; (4) Đẩy lên, hai tạ hơi chụm lại ở trên.
- **Lỗi thường gặp:** Khuỷu mở ngang 90°; Nhấc mông khỏi ghế; Hạ quá nông.
- **Tránh nếu:** đau vai → tập Chống đẩy kê tay cao (`incline_push_up`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 8 kg/tay, nữ 4 kg/tay.
- **Thay thế (theo thứ tự):** Đẩy ngực thanh đòn (`barbell_bench_press`) → Đẩy ngực máy (`machine_chest_press`) → Chống đẩy (`push_up`) → Đẩy ngực với dây (`band_chest_press`).
- **Nguồn:** https://www.strengthlog.com/dumbbell-chest-press/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Đẩy ngực trên tạ tay (ghế dốc) / Incline Dumbbell Press

- **id:** `incline_dumbbell_press`
- **Dụng cụ:** Tạ tay (tạ đơn) + Ghế chỉnh độ dốc (`dumbbell`, `bench_incline`)
- **Cơ chính:** Ngực, Vai trước. **Cơ phụ:** Tay sau.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Ghế dốc khoảng 30-45°; (2) Siết bả vai, ngực ưỡn; (3) Hạ tạ tới ngang ngực trên; (4) Đẩy thẳng lên trên vai.
- **Lỗi thường gặp:** Ghế dốc quá cao biến thành đẩy vai; Khuỷu mở quá rộng; Cong lưng nhấc mông.
- **Tránh nếu:** đau vai → tập Đẩy landmine (thanh đòn chống góc) (`landmine_press`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 7 kg/tay, nữ 4 kg/tay.
- **Thay thế (theo thứ tự):** Đẩy ngực tạ tay (`dumbbell_bench_press`) → Đẩy ngực máy (`machine_chest_press`) → Chống đẩy (`push_up`) → Đẩy landmine (thanh đòn chống góc) (`landmine_press`).
- **Nguồn:** https://www.strengthlog.com/dumbbell-incline-press/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Đẩy ngực máy / Machine Chest Press

- **id:** `machine_chest_press`
- **Dụng cụ:** Máy đẩy ngực / ép ngực (`machine_chest`)
- **Cơ chính:** Ngực, Vai trước. **Cơ phụ:** Tay sau.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Chỉnh ghế để tay cầm ngang giữa ngực; (2) Lưng và bả vai áp sát đệm; (3) Đẩy tới gần thẳng tay, không khóa cứng khuỷu; (4) Về chậm, không để chồng tạ chạm nhau.
- **Lỗi thường gặp:** Ghế quá thấp làm tay cầm ngang vai; Nhô vai ra trước khi đẩy; Thả tạ rơi.
- **Tránh nếu:** đau vai → tập Chống đẩy kê tay cao (`incline_push_up`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 20 kg, nữ 10 kg.
- **Thay thế (theo thứ tự):** Đẩy ngực tạ tay (`dumbbell_bench_press`) → Đẩy ngực thanh đòn (`barbell_bench_press`) → Chống đẩy kê tay cao (`incline_push_up`) → Đẩy ngực với dây (`band_chest_press`).
- **Nguồn:** https://www.strengthlog.com/machine-chest-press/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Đẩy ngực với dây / Banded Chest Press

- **id:** `band_chest_press`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Ngực, Vai trước. **Cơ phụ:** Tay sau.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Vòng dây qua sau lưng ngang bả vai (hoặc buộc vào cột); (2) Đứng chân trước chân sau, gồng bụng; (3) Đẩy thẳng ra trước ngang ngực; (4) Về chậm, giữ dây luôn căng.
- **Lỗi thường gặp:** Nhô vai ra trước; Ưỡn lưng; Dây chùng ở điểm đầu.
- **Tránh nếu:** đau vai → tập Chống đẩy kê tay cao (`incline_push_up`).
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây vừa, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Chống đẩy (`push_up`) → Chống đẩy kê tay cao (`incline_push_up`) → Đẩy ngực tạ tay (`dumbbell_bench_press`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Chống đẩy / Push-Up

- **id:** `push_up`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Ngực, Vai trước. **Cơ phụ:** Tay sau, Bụng.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Tay rộng hơn vai một chút; (2) Giữ thẳng một đường từ đầu tới gót, gồng nhẹ bụng; (3) Hít vào, hạ người sâu nhất có thể; (4) Thở ra, đẩy lên thẳng tay.
- **Lỗi thường gặp:** Võng hông hoặc chổng mông; Chỉ hạ nửa chừng; Khuỷu mở ngang 90°.
- **Tránh nếu:** đau vai → tập Chống đẩy kê tay cao (`incline_push_up`); đau cổ tay → tập Đẩy ngực tạ tay (`dumbbell_bench_press`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Đẩy ngực tạ tay (`dumbbell_bench_press`) → Đẩy ngực với dây (`band_chest_press`) → Chống đẩy kê tay cao (`incline_push_up`).
- **Nghiên cứu:** [UNVERIFIED, theo tóm tắt tìm kiếm] Calatayud 2015: chống đẩy thêm dây kháng lực cho hoạt hóa cơ và mức tăng sức mạnh tương đương đẩy ngực 6RM (5 tuần, mẫu nhỏ). Kê cao chân để tăng độ khó.
- **Nguồn:** https://www.strengthlog.com/push-up/ · đã đọc và đối chiếu.

#### Chống đẩy kê tay cao / Incline (Hands-Elevated) Push-Up

- **id:** `incline_push_up`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Ngực, Vai trước. **Cơ phụ:** Tay sau, Bụng.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đặt tay lên ghế, thanh Smith hoặc mép bàn chắc chắn; (2) Thân thẳng từ đầu tới gót; (3) Hạ ngực chạm gần điểm tựa; (4) Điểm tựa càng thấp càng khó; hạ dần độ cao theo tuần.
- **Lỗi thường gặp:** Võng hông; Đưa cằm ra trước thay vì hạ ngực; Điểm tựa trơn hoặc không chắc.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Chống đẩy (`push_up`) → Đẩy ngực máy (`machine_chest_press`) → Đẩy ngực với dây (`band_chest_press`).
- **Nguồn:** https://www.strengthlog.com/incline-push-up/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

### Đẩy dọc (qua đầu)

#### Đẩy vai thanh đòn đứng / Barbell Overhead Press

- **id:** `overhead_press_barbell`
- **Dụng cụ:** Thanh đòn + bánh tạ + Giá squat / khung power rack (`barbell`, `rack`)
- **Cơ chính:** Vai trước. **Cơ phụ:** Tay sau, Vai giữa, Bụng.
- **Độ khó:** 3/3. **Người mới:** chưa nên, tập bài dễ hơn trong thang trước.
- **Kỹ thuật:** (1) Thanh trên giá ngang ngực, nắm rộng hơn vai một chút; (2) Gồng bụng, nhấc thanh ra, thanh tựa trên vai trước; (3) Đẩy thẳng lên hết tay, thở ra; (4) Hạ có kiểm soát về vai.
- **Lỗi thường gặp:** Ngả lưng ưỡn quá mức; Nhún chân lấy đà (thành push press); Tăng tạ quá nhanh.
- **Tránh nếu:** đau vai → tập Đẩy landmine (thanh đòn chống góc) (`landmine_press`); đau lưng dưới → tập Đẩy landmine (thanh đòn chống góc) (`landmine_press`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 20 kg (cả thanh), nữ 10 kg (cả thanh). Thanh 20 kg thường quá nặng với nữ mới tập: dùng thanh nhẹ hoặc chuyển sang tạ tay.
- **Thay thế (theo thứ tự):** Đẩy vai tạ tay (`dumbbell_shoulder_press`) → Đẩy vai máy (`machine_shoulder_press`) → Đẩy vai với dây (`band_overhead_press`) → Chống đẩy chổng mông (pike) (`pike_push_up`).
- **Nguồn:** https://www.strengthlog.com/overhead-press/ · đã đọc và đối chiếu.

#### Đẩy vai tạ tay / Dumbbell Shoulder Press

- **id:** `dumbbell_shoulder_press`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Vai trước. **Cơ phụ:** Tay sau, Vai giữa.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Ngồi hoặc đứng, tạ ngang tai, cẳng tay thẳng đứng; (2) Khuỷu hơi đưa ra trước thân (không mở ngang hoàn toàn); (3) Đẩy lên tới gần thẳng tay; (4) Hạ chậm về ngang tai.
- **Lỗi thường gặp:** Ưỡn lưng dưới; Hạ quá nông; Hai tạ đập vào nhau ở trên.
- **Tránh nếu:** đau vai → tập Đẩy landmine (thanh đòn chống góc) (`landmine_press`); đau lưng dưới → tập Đẩy landmine (thanh đòn chống góc) (`landmine_press`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 6 kg/tay, nữ 3 kg/tay.
- **Thay thế (theo thứ tự):** Đẩy vai thanh đòn đứng (`overhead_press_barbell`) → Đẩy vai máy (`machine_shoulder_press`) → Đẩy landmine (thanh đòn chống góc) (`landmine_press`) → Đẩy vai với dây (`band_overhead_press`) → Chống đẩy chổng mông (pike) (`pike_push_up`).
- **Nguồn:** https://www.strengthlog.com/dumbbell-shoulder-press/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Đẩy vai máy / Machine Shoulder Press

- **id:** `machine_shoulder_press`
- **Dụng cụ:** Máy đẩy vai (`machine_shoulder`)
- **Cơ chính:** Vai trước. **Cơ phụ:** Tay sau, Vai giữa.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Chỉnh ghế để tay cầm ngang vai; (2) Lưng áp sát đệm; (3) Đẩy lên tới gần thẳng tay; (4) Hạ chậm, không để tạ chạm chồng.
- **Lỗi thường gặp:** Ghế quá thấp; Ưỡn lưng rời đệm; Nhún vai lên tai.
- **Tránh nếu:** đau vai → tập Đẩy landmine (thanh đòn chống góc) (`landmine_press`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 10 kg, nữ 5 kg.
- **Thay thế (theo thứ tự):** Đẩy vai tạ tay (`dumbbell_shoulder_press`) → Đẩy vai thanh đòn đứng (`overhead_press_barbell`) → Đẩy vai với dây (`band_overhead_press`).
- **Nguồn:** https://www.strengthlog.com/machine-shoulder-press/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Đẩy landmine (thanh đòn chống góc) / Landmine Press

- **id:** `landmine_press`
- **Dụng cụ:** Thanh đòn + bánh tạ (`barbell`)
- **Cơ chính:** Vai trước, Ngực. **Cơ phụ:** Tay sau, Bụng.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Chống một đầu thanh vào góc tường (lót khăn), cầm đầu kia ngang vai; (2) Đứng chân trước chân sau hoặc quỳ một gối; (3) Đẩy thanh chéo lên trước, vươn vai ở cuối; (4) Bụng gồng, không ưỡn lưng.
- **Lỗi thường gặp:** Xoay thân lấy đà; Ưỡn lưng; Đầu thanh trượt vì không chèn chắc.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `added_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 5 kg lắp thêm, nữ chưa lắp thêm tạ. Số kg là tạ lắp thêm vào đầu thanh, không tính thanh. Đây là lựa chọn đẩy qua đầu thân thiện với vai.
- **Thay thế (theo thứ tự):** Đẩy vai tạ tay (`dumbbell_shoulder_press`) → Đẩy ngực trên tạ tay (ghế dốc) (`incline_dumbbell_press`) → Đẩy vai với dây (`band_overhead_press`).
- **Nguồn:** https://www.strengthlog.com/landmine-press/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Đẩy vai với dây / Banded Overhead Press

- **id:** `band_overhead_press`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Vai trước. **Cơ phụ:** Tay sau, Vai giữa.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Giẫm lên dây, cầm hai đầu ngang vai; (2) Gồng bụng, siết mông; (3) Đẩy thẳng lên trên đầu; (4) Hạ chậm về ngang vai.
- **Lỗi thường gặp:** Ưỡn lưng; Dây lệch hai bên không đều; Chỉ đẩy nửa biên độ.
- **Tránh nếu:** đau vai → tập Đẩy landmine (thanh đòn chống góc) (`landmine_press`).
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây vừa, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Đẩy vai tạ tay (`dumbbell_shoulder_press`) → Chống đẩy chổng mông (pike) (`pike_push_up`) → Đẩy vai máy (`machine_shoulder_press`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Chống đẩy chổng mông (pike) / Pike Push-Up

- **id:** `pike_push_up`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Vai trước. **Cơ phụ:** Tay sau, Ngực.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Vào tư thế chữ V ngược, mông cao, tay rộng hơn vai; (2) Hạ đỉnh đầu về phía sàn, trước hai tay; (3) Khuỷu chỉ chếch ra sau khoảng 45°; (4) Đẩy lên trở lại chữ V.
- **Lỗi thường gặp:** Biến thành chống đẩy thường (hông hạ thấp); Khuỷu mở ngang; Hạ đầu giữa hai tay thay vì phía trước.
- **Tránh nếu:** đau vai → tập Đẩy landmine (thanh đòn chống góc) (`landmine_press`); đau cổ tay → tập Đẩy vai với dây (`band_overhead_press`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Đẩy vai với dây (`band_overhead_press`) → Đẩy vai tạ tay (`dumbbell_shoulder_press`) → Chống đẩy kê tay cao (`incline_push_up`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

### Kéo ngang

#### Kéo thanh đòn gập người / Barbell Bent-Over Row

- **id:** `barbell_row`
- **Dụng cụ:** Thanh đòn + bánh tạ (`barbell`)
- **Cơ chính:** Xô, Cầu vai / thang, Cơ trám (giữa lưng). **Cơ phụ:** Vai sau, Tay trước, Cơ dựng sống (lưng dưới).
- **Độ khó:** 3/3. **Người mới:** chưa nên, tập bài dễ hơn trong thang trước.
- **Kỹ thuật:** (1) Gập hông, thân nghiêng khoảng 45° hoặc thấp hơn, lưng thẳng; (2) Gồng bụng, gối hơi chùng; (3) Kéo thanh về bụng trên, khuỷu đi ra sau; (4) Hạ có kiểm soát tới thẳng tay.
- **Lỗi thường gặp:** Giật thân lên để lấy đà; Tròn lưng; Đứng thẳng dần lên theo từng lần kéo.
- **Tránh nếu:** đau lưng dưới → tập Kéo dây ngang (`band_row`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 30 kg (cả thanh), nữ 20 kg (cả thanh).
- **Thay thế (theo thứ tự):** Kéo tạ tay một bên (`dumbbell_row`) → Kéo cáp ngang ngồi (`seated_cable_row`) → Kéo ngang máy (tì ngực) (`machine_row`) → Kéo người dưới thanh (inverted row) (`inverted_row`) → Kéo dây ngang (`band_row`).
- **Nguồn:** https://www.strengthlog.com/barbell-row/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Kéo tạ tay một bên / One-Arm Dumbbell Row

- **id:** `dumbbell_row`
- **Dụng cụ:** Tạ tay (tạ đơn) + Ghế phẳng (`dumbbell`, `bench_flat`)
- **Cơ chính:** Xô, Cầu vai / thang, Vai sau. **Cơ phụ:** Tay trước, Cẳng tay / lực nắm, Chóp xoay.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Tay và gối cùng bên chống lên ghế, thân song song sàn; (2) Gồng bụng, lưng trung tính, mắt nhìn xuống sàn; (3) Kéo tạ lên, khuỷu hướng lên trần và đi sát thân; (4) Hạ chậm tới thẳng tay rồi mới kéo lần tiếp.
- **Lỗi thường gặp:** Vung tạ lấy đà; Cắt ngắn biên độ; Khuỷu mở ra ngoài.
- **Tránh nếu:** đau lưng dưới → tập Kéo dây ngang (`band_row`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 10 kg/tay, nữ 6 kg/tay.
- **Thay thế (theo thứ tự):** Kéo cáp ngang ngồi (`seated_cable_row`) → Kéo ngang máy (tì ngực) (`machine_row`) → Kéo thanh đòn gập người (`barbell_row`) → Kéo dây ngang (`band_row`).
- **Nguồn:** https://www.strengthlog.com/dumbbell-row/ · đã đọc và đối chiếu.

#### Kéo cáp ngang ngồi / Seated Cable Row

- **id:** `seated_cable_row`
- **Dụng cụ:** Ròng rọc thấp (cáp dưới) (`cable_low`)
- **Cơ chính:** Xô, Cơ trám (giữa lưng), Cầu vai / thang. **Cơ phụ:** Vai sau, Tay trước.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Ngồi thẳng lưng, gối hơi chùng, chân đạp chắc; (2) Kéo tay cầm về bụng, khuỷu đi sát thân; (3) Siết hai bả vai lại 1 giây; (4) Duỗi tay chậm, để bả vai vươn ra nhưng lưng không tròn.
- **Lỗi thường gặp:** Ngả người ra sau để lấy đà; Nhún vai lên tai; Tròn lưng khi duỗi tay.
- **Tránh nếu:** đau lưng dưới → tập Kéo dây ngang (`band_row`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 25 kg, nữ 15 kg.
- **Thay thế (theo thứ tự):** Kéo ngang máy (tì ngực) (`machine_row`) → Kéo tạ tay một bên (`dumbbell_row`) → Kéo thanh đòn gập người (`barbell_row`) → Kéo dây ngang (`band_row`).
- **Nguồn:** https://www.acefitness.org/resources/everyone/exercise-library/48/seated-row/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Kéo ngang máy (tì ngực) / Chest-Supported Machine Row

- **id:** `machine_row`
- **Dụng cụ:** Máy kéo ngang (row) (`machine_row`)
- **Cơ chính:** Xô, Cơ trám (giữa lưng), Cầu vai / thang. **Cơ phụ:** Vai sau, Tay trước.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Chỉnh ghế để ngực tì vào đệm, tay cầm ngang ngực dưới; (2) Kéo khuỷu ra sau, siết bả vai; (3) Ngực luôn áp vào đệm; (4) Về chậm tới thẳng tay.
- **Lỗi thường gặp:** Rời ngực khỏi đệm để ngả sau; Nhún vai; Kéo nửa biên độ.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 20 kg, nữ 10 kg.
- **Thay thế (theo thứ tự):** Kéo cáp ngang ngồi (`seated_cable_row`) → Kéo tạ tay một bên (`dumbbell_row`) → Kéo dây ngang (`band_row`) → Kéo người dưới thanh (inverted row) (`inverted_row`).
- **Nguồn:** https://www.strengthlog.com/seated-machine-row/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Kéo người dưới thanh (inverted row) / Inverted Row

- **id:** `inverted_row`
- **Dụng cụ:** Khung Smith (`smith`)
- **Cơ chính:** Xô, Cơ trám (giữa lưng), Cầu vai / thang. **Cơ phụ:** Vai sau, Tay trước, Bụng.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Khóa thanh Smith ngang thắt lưng, nằm dưới thanh, nắm rộng hơn vai; (2) Thân thẳng như tấm ván, gót chạm sàn; (3) Kéo ngực chạm thanh; (4) Co gối hoặc nâng thanh cao hơn để dễ hơn.
- **Lỗi thường gặp:** Võng hông; Đưa cằm lên thay vì kéo ngực; Thanh chưa khóa chắc.
- **Tránh nếu:** đau vai → tập Kéo cáp ngang ngồi (`seated_cable_row`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Kéo cáp ngang ngồi (`seated_cable_row`) → Kéo tạ tay một bên (`dumbbell_row`) → Kéo dây ngang (`band_row`) → Nằm sấp kéo tay (W raise) (`prone_row_bodyweight`).
- **Nguồn:** https://www.strengthlog.com/inverted-row/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Kéo dây ngang / Banded Row

- **id:** `band_row`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Xô, Cơ trám (giữa lưng). **Cơ phụ:** Vai sau, Tay trước.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Móc dây vào cột chắc ngang bụng (hoặc ngồi, vòng qua bàn chân); (2) Ngồi/đứng thẳng lưng; (3) Kéo khuỷu ra sau sát thân, siết bả vai; (4) Về chậm, dây luôn căng.
- **Lỗi thường gặp:** Điểm móc không chắc; Ngả người lấy đà; Nhún vai.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây vừa, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Kéo tạ tay một bên (`dumbbell_row`) → Kéo cáp ngang ngồi (`seated_cable_row`) → Kéo người dưới thanh (inverted row) (`inverted_row`) → Nằm sấp kéo tay (W raise) (`prone_row_bodyweight`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Nằm sấp kéo tay (W raise) / Prone Bodyweight Row (W Raise)

- **id:** `prone_row_bodyweight`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Cơ trám (giữa lưng), Cầu vai / thang, Vai sau. **Cơ phụ:** Cơ dựng sống (lưng dưới), Xô.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Nằm sấp, trán gần sàn, tay duỗi trước đầu; (2) Nhấc nhẹ ngực và tay, kéo khuỷu về sườn thành chữ W; (3) Siết bả vai 2 giây; (4) Duỗi tay ra lại mà không chạm sàn.
- **Lỗi thường gặp:** Ngửa cổ; Ưỡn lưng dưới quá mức; Làm nhanh, không siết.
- **Tránh nếu:** đau lưng dưới → tập Kéo dây ngang (`band_row`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể. Chỉ là phương án tạm khi không có gì để kéo; lực cản thấp, không thay hẳn được bài kéo có tạ.
- **Thay thế (theo thứ tự):** Kéo dây ngang (`band_row`) → Kéo người dưới thanh (inverted row) (`inverted_row`) → Kéo tạ tay một bên (`dumbbell_row`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

### Kéo dọc

#### Hít xà đơn / Pull-Up

- **id:** `pull_up`
- **Dụng cụ:** Xà đơn (`pullup_bar`)
- **Cơ chính:** Xô. **Cơ phụ:** Tay trước, Vai sau, Cẳng tay / lực nắm, Chóp xoay.
- **Độ khó:** 3/3. **Người mới:** chưa nên, tập bài dễ hơn trong thang trước.
- **Kỹ thuật:** (1) Nắm sấp, rộng hơn vai một chút; (2) Ngực ưỡn, mắt nhìn xà; (3) Kéo tới khi cằm qua xà hoặc xà chạm ngực trên; hạ bả vai xuống khi kéo; (4) Hạ có kiểm soát tới thẳng tay hoàn toàn.
- **Lỗi thường gặp:** Đá chân lấy đà (kipping); Nắm quá rộng làm ngắn biên độ; Không xuống hết tay.
- **Tránh nếu:** đau vai → tập Kéo xô với dây (`band_lat_pulldown`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể. Nắm ngửa (chin-up) dễ hơn một chút và ăn tay trước nhiều hơn; có thể dùng thay.
- **Thay thế (theo thứ tự):** Hít xà có dây trợ lực (`band_assisted_pull_up`) → Kéo xô máy (`lat_pulldown`) → Kéo xô với dây (`band_lat_pulldown`) → Kéo cáp thẳng tay (`straight_arm_pulldown_cable`).
- **Nguồn:** https://www.strengthlog.com/pull-up/ · đã đọc và đối chiếu.

#### Hít xà có dây trợ lực / Band-Assisted Pull-Up

- **id:** `band_assisted_pull_up`
- **Dụng cụ:** Xà đơn + Dây kháng lực (`pullup_bar`, `band`)
- **Cơ chính:** Xô. **Cơ phụ:** Tay trước, Vai sau, Cẳng tay / lực nắm.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Buộc dây lên xà, đặt gối hoặc bàn chân vào vòng dây; (2) Bắt đầu từ treo thẳng tay; (3) Kéo ngực về phía xà, khuỷu đi xuống; (4) Hạ chậm 2-3 giây; đổi dây mỏng dần theo thời gian.
- **Lỗi thường gặp:** Nảy trên dây để lấy đà; Không xuống hết tay; Dây bật khỏi chân khi xuống xà.
- **Tránh nếu:** đau vai → tập Kéo xô với dây (`band_lat_pulldown`).
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây nặng, nữ dây nặng. Dây càng dày càng trợ lực nhiều (dễ hơn).
- **Thay thế (theo thứ tự):** Hít xà chiều xuống (negative) (`negative_pull_up`) → Kéo xô máy (`lat_pulldown`) → Kéo xô với dây (`band_lat_pulldown`) → Kéo cáp thẳng tay (`straight_arm_pulldown_cable`).
- **Nguồn:** https://www.strengthlog.com/assisted-pull-up/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Hít xà chiều xuống (negative) / Negative Pull-Up

- **id:** `negative_pull_up`
- **Dụng cụ:** Xà đơn (`pullup_bar`)
- **Cơ chính:** Xô. **Cơ phụ:** Tay trước, Cẳng tay / lực nắm.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đứng lên ghế/bục để bắt đầu ở vị trí cằm trên xà; (2) Nhấc chân, hạ người thật chậm 3-5 giây; (3) Xuống tới thẳng tay hoàn toàn; (4) Bước lên bục lại, không cần kéo lên.
- **Lỗi thường gặp:** Rơi tự do; Dừng giữa chừng không xuống hết; Làm quá nhiều lần khi đã mất kiểm soát.
- **Tránh nếu:** đau vai → tập Kéo xô với dây (`band_lat_pulldown`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Hít xà có dây trợ lực (`band_assisted_pull_up`) → Kéo xô máy (`lat_pulldown`) → Kéo xô với dây (`band_lat_pulldown`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Kéo xô máy / Lat Pulldown

- **id:** `lat_pulldown`
- **Dụng cụ:** Máy kéo xô (có đệm chặn đùi) (`lat_pulldown`)
- **Cơ chính:** Xô. **Cơ phụ:** Tay trước, Vai sau, Cẳng tay / lực nắm, Chóp xoay.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Chỉnh đệm chặn sát đùi; (2) Nắm sấp, rộng hơn vai một chút; ngồi cao, ngực ưỡn; (3) Kéo thanh về ngực trên, "kéo bằng khuỷu"; (4) Siết bả vai ở dưới, trả thanh chậm hết tầm.
- **Lỗi thường gặp:** Tạ quá nặng nên phải ngả giật người; Kéo bằng tay trước; Bỏ qua pha siết hoặc không đi hết biên độ.
- **Tránh nếu:** đau vai → tập Kéo cáp thẳng tay (`straight_arm_pulldown_cable`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 25 kg, nữ 15 kg. Không kéo thanh ra sau gáy.
- **Thay thế (theo thứ tự):** Hít xà có dây trợ lực (`band_assisted_pull_up`) → Hít xà chiều xuống (negative) (`negative_pull_up`) → Kéo xô với dây (`band_lat_pulldown`) → Kéo cáp thẳng tay (`straight_arm_pulldown_cable`).
- **Nguồn:** https://www.strengthlog.com/lat-pulldown-with-pronated-grip/ · đã đọc và đối chiếu.

#### Kéo cáp thẳng tay / Straight-Arm Cable Pulldown

- **id:** `straight_arm_pulldown_cable`
- **Dụng cụ:** Ròng rọc cao (cáp trên) (`cable_high`)
- **Cơ chính:** Xô. **Cơ phụ:** Tay sau, Bụng, Vai sau.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đứng trước ròng rọc cao, tay gần thẳng; (2) Hơi gập hông, gồng bụng; (3) Kéo thanh theo cung tròn xuống đùi; (4) Trả chậm lên ngang trán.
- **Lỗi thường gặp:** Co khuỷu biến thành kéo tay sau; Đung đưa thân; Nhún vai.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 10 kg, nữ 5 kg.
- **Thay thế (theo thứ tự):** Kéo xô với dây (`band_lat_pulldown`) → Kéo xô máy (`lat_pulldown`) → Kéo tạ tay một bên (`dumbbell_row`).
- **Nguồn:** https://www.strengthlog.com/straight-arm-lat-pulldown/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Kéo xô với dây / Banded Lat Pulldown

- **id:** `band_lat_pulldown`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Xô. **Cơ phụ:** Tay trước, Vai sau.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Móc dây vào điểm cao chắc chắn (xà, móc tường); (2) Quỳ hoặc ngồi, tay vươn lên; (3) Kéo khuỷu xuống sườn, ngực ưỡn; (4) Trả chậm hết tầm.
- **Lỗi thường gặp:** Điểm móc không chắc; Kéo bằng tay trước; Gập người theo dây.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây vừa, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Kéo xô máy (`lat_pulldown`) → Hít xà chiều xuống (negative) (`negative_pull_up`) → Kéo cáp thẳng tay (`straight_arm_pulldown_cable`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

### Core (thân giữa)

#### Plank / Front Plank

- **id:** `plank` · loại core: Chống ưỡn
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Bụng. **Cơ phụ:** Liên sườn.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Tì cẳng tay và mũi chân, khuỷu ngay dưới vai, chân rộng bằng hông; (2) Gồng bụng, giữ thẳng một đường từ đầu tới gót; (3) Ép cẳng tay xuống sàn để vai không sụp; (4) Dừng trước khi tư thế hỏng.
- **Lỗi thường gặp:** Võng hông hoặc chổng mông; Ưỡn lưng dưới khi mỏi; Sụp vai.
- **Tránh nếu:** đau vai → tập Dead bug (`dead_bug`); đau lưng dưới → tập Dead bug (`dead_bug`).
- **Kiểu tải:** `time_seconds`, tính giây. **Khởi điểm [UNVERIFIED]:** nam 30 giây, nữ 20 giây. Giữ được 60-90 giây thì chuyển sang biến thể khó hơn thay vì giữ lâu thêm.
- **Thay thế (theo thứ tự):** Dead bug (`dead_bug`) → Bird dog (`bird_dog`) → Bò gấu (`bear_crawl`).
- **Nguồn:** https://www.strengthlog.com/plank/ · đã đọc và đối chiếu.

#### Dead bug / Dead Bug

- **id:** `dead_bug` · loại core: Chống ưỡn
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Bụng. **Cơ phụ:** Liên sườn, Gập hông.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Nằm ngửa, tay chỉ lên trần, hông và gối gập 90°; (2) Ép lưng dưới sát sàn; (3) Duỗi chậm tay và chân đối bên ra xa; (4) Thở ra khi duỗi, lưng không rời sàn.
- **Lỗi thường gặp:** Lưng dưới cong rời sàn; Làm quá nhanh; Nín thở.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Plank (`plank`) → Bird dog (`bird_dog`) → Gập bụng McGill (curl-up) (`mcgill_curl_up`).
- **Nguồn:** https://www.strengthlog.com/dead-bugs/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Plank nghiêng / Side Plank

- **id:** `side_plank` · loại core: Chống xoay / nghiêng
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Liên sườn. **Cơ phụ:** Bụng, Mông nhỡ (dạng hông).
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Nằm nghiêng, tì khuỷu; người mới gập gối và tì gối; (2) Nâng hông để chỉ còn gối (hoặc bàn chân) và cẳng tay chạm sàn; (3) Vai, thân và đùi trên thẳng một đường; (4) Giữ 10 giây mỗi lần, nhiều lần ngắn thay vì một lần dài.
- **Lỗi thường gặp:** Hông võng xuống hoặc xoay ra sau; Vai sụp vào tai; Cố giữ lâu khi tư thế đã hỏng.
- **Tránh nếu:** đau vai → tập Pallof press với dây (`pallof_press_band`).
- **Kiểu tải:** `time_seconds`, tính giây. **Khởi điểm [UNVERIFIED]:** nam 10 giây, nữ 10 giây. Theo McGill Big 3: giữ 10 giây, làm kiểu tháp giảm 5-3-1 lần mỗi bên.
- **Thay thế (theo thứ tự):** Pallof press với dây (`pallof_press_band`) → Pallof press với cáp (`pallof_press_cable`) → Đi bộ xách tạ một tay (`suitcase_carry_dumbbell`) → Bird dog (`bird_dog`).
- **Nguồn:** https://squatuniversity.com/2018/06/21/the-mcgill-big-3-for-core-stability/ · đã đọc và đối chiếu.

#### Bird dog / Bird Dog

- **id:** `bird_dog` · loại core: Chống xoay / nghiêng
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Cơ dựng sống (lưng dưới), Mông. **Cơ phụ:** Bụng, Liên sườn.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Chống hai tay hai gối, cột sống trung tính (hơi võng nhẹ tự nhiên); (2) Duỗi một chân ra sau và tay đối bên ra trước, lưng dưới đứng yên; (3) Đẩy gót thẳng ra sau, chân chỉ nhấc thấp; (4) Giữ 10 giây rồi đổi bên.
- **Lỗi thường gặp:** Ưỡn lưng khi nhấc chân; Tròn lưng khi thu tay chân về; Cố làm dù đau hoặc mất thăng bằng (chuyển sang bản chỉ duỗi chân).
- **Tránh nếu:** đau cổ tay → tập Dead bug (`dead_bug`).
- **Kiểu tải:** `time_seconds`, tính giây. **Khởi điểm [UNVERIFIED]:** nam 10 giây, nữ 10 giây. Theo McGill Big 3: giữ 10 giây, tháp giảm 5-3-1 lần mỗi bên.
- **Thay thế (theo thứ tự):** Dead bug (`dead_bug`) → Plank nghiêng (`side_plank`) → Plank (`plank`).
- **Nguồn:** https://squatuniversity.com/2018/06/21/the-mcgill-big-3-for-core-stability/ · đã đọc và đối chiếu.

#### Pallof press với cáp / Cable Pallof Press

- **id:** `pallof_press_cable` · loại core: Chống xoay / nghiêng
- **Dụng cụ:** Ròng rọc cao (cáp trên) (`cable_high`)
- **Cơ chính:** Liên sườn, Bụng. **Cơ phụ:** Mông.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đứng ngang với máy, tay cầm ngang ngực; ròng rọc cố định ở cao thì quỳ hai gối cho gần ngang ngực; (2) Hai tay nắm tay cầm sát ngực, gồng bụng; (3) Đẩy thẳng tay ra trước mà thân không xoay; (4) Giữ 2 giây rồi thu về.
- **Lỗi thường gặp:** Thân xoay theo cáp; Đứng quá gần máy nên cáp chùng; Nhún vai.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 5 kg, nữ 2,5 kg.
- **Thay thế (theo thứ tự):** Pallof press với dây (`pallof_press_band`) → Plank nghiêng (`side_plank`) → Đi bộ xách tạ một tay (`suitcase_carry_dumbbell`).
- **Nguồn:** https://www.strengthlog.com/pallof-press/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Pallof press với dây / Banded Pallof Press

- **id:** `pallof_press_band` · loại core: Chống xoay / nghiêng
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Liên sườn, Bụng. **Cơ phụ:** Mông.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Móc dây ngang ngực vào cột chắc, đứng ngang với dây; (2) Hai tay nắm dây sát ngực, bước ra cho dây căng; (3) Đẩy thẳng tay ra trước, không để dây kéo xoay người; (4) Giữ 2 giây rồi thu về.
- **Lỗi thường gặp:** Thân xoay theo dây; Dây chùng; Hông lệch sang một bên.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây nhẹ, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Pallof press với cáp (`pallof_press_cable`) → Plank nghiêng (`side_plank`) → Bird dog (`bird_dog`).
- **Nguồn:** https://www.strengthlog.com/pallof-press/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Gập bụng McGill (curl-up) / McGill Curl-Up

- **id:** `mcgill_curl_up` · loại core: Gập bụng
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Bụng. **Cơ phụ:** Liên sườn.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Nằm ngửa, một gối co, một chân duỗi; (2) Đặt hai tay dưới lưng dưới để giữ độ cong tự nhiên; (3) Chỉ nhấc đầu và vai lên vài cm; (4) Giữ 10 giây rồi hạ; tăng số lần chứ không tăng thời gian giữ.
- **Lỗi thường gặp:** Nhấc đầu vai quá cao làm tròn lưng dưới; Biến thành gập bụng (crunch) truyền thống; Tập ngay sau khi ngủ dậy.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `time_seconds`, tính giây. **Khởi điểm [UNVERIFIED]:** nam 10 giây, nữ 10 giây. Theo McGill Big 3: giữ 8-10 giây, tháp giảm 5-3-1 lần, nghỉ 20-30 giây.
- **Thay thế (theo thứ tự):** Dead bug (`dead_bug`) → Gập bụng ngược (nâng chân co gối) (`reverse_crunch`) → Plank (`plank`).
- **Nguồn:** https://squatuniversity.com/2018/06/21/the-mcgill-big-3-for-core-stability/ · đã đọc và đối chiếu.

#### Gập bụng cáp (quỳ) / Kneeling Cable Crunch

- **id:** `cable_crunch` · loại core: Gập bụng
- **Dụng cụ:** Ròng rọc cao (cáp trên) (`cable_high`)
- **Cơ chính:** Bụng. **Cơ phụ:** Liên sườn.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Quỳ trước ròng rọc cao, cầm dây thừng hai bên đầu; (2) Giữ hông cố định, cuộn ngực về phía hông; (3) Thở ra và siết bụng ở dưới; (4) Trả chậm, để bụng giãn ra.
- **Lỗi thường gặp:** Ngồi mông xuống gót (thành động tác hông); Kéo bằng tay; Tạ quá nặng.
- **Tránh nếu:** đau lưng dưới → tập Dead bug (`dead_bug`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 20 kg, nữ 10 kg.
- **Thay thế (theo thứ tự):** Gập bụng ngược (nâng chân co gối) (`reverse_crunch`) → Gập bụng McGill (curl-up) (`mcgill_curl_up`) → Plank (`plank`).
- **Nguồn:** https://www.strengthlog.com/cable-crunch/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Gập bụng ngược (nâng chân co gối) / Reverse Crunch / Bent-Knee Leg Raise

- **id:** `reverse_crunch` · loại core: Gập bụng
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Bụng. **Cơ phụ:** Gập hông, Liên sườn.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Nằm ngửa, tay dọc thân, gối co 90°; (2) Cuộn hông khỏi sàn, đưa gối về phía ngực; (3) Hạ chậm, lưng dưới không cong rời sàn; (4) Thở ra khi cuộn lên.
- **Lỗi thường gặp:** Đá chân lấy đà; Lưng dưới ưỡn khi hạ chân; Duỗi thẳng chân quá sớm khi chưa đủ sức.
- **Tránh nếu:** đau lưng dưới → tập Dead bug (`dead_bug`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Gập bụng McGill (curl-up) (`mcgill_curl_up`) → Gập bụng cáp (quỳ) (`cable_crunch`) → Dead bug (`dead_bug`).
- **Nguồn:** https://www.strengthlog.com/lying-leg-raise/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

### Mang vác

#### Đi bộ xách tạ hai tay / Dumbbell Farmer's Carry

- **id:** `farmers_carry_dumbbell`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Cẳng tay / lực nắm, Cầu vai / thang, Liên sườn, Mông. **Cơ phụ:** Bụng, Cơ dựng sống (lưng dưới), Đùi trước, Bắp chân.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Hít vào, gồng nhẹ bụng rồi nhấc tạ lên bằng chân, lưng thẳng; (2) Mắt nhìn thẳng, bước ngắn rồi dài dần; (3) Người thẳng một đường khi đi; (4) Đặt tạ xuống có kiểm soát.
- **Lỗi thường gặp:** Đổ người ra trước; Nhún vai lên tai; Cúi tròn lưng khi nhấc/đặt tạ.
- **Tránh nếu:** đau lưng dưới → tập Dead bug (`dead_bug`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, tính mét. **Khởi điểm [UNVERIFIED]:** nam 14 kg/tay, nữ 8 kg/tay. Đi 20-30 m mỗi hiệp (hoặc 30-40 giây nếu phòng chật).
- **Thay thế (theo thứ tự):** Đi bộ ôm tạ ấm trước ngực (`front_carry_kettlebell`) → Đi bộ xách tạ một tay (`suitcase_carry_dumbbell`) → Bò gấu (`bear_crawl`) → Plank (`plank`).
- **Nguồn:** https://www.strengthlog.com/farmers-walk/ · đã đọc và đối chiếu.

#### Đi bộ xách tạ một tay / Suitcase Carry

- **id:** `suitcase_carry_dumbbell`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Liên sườn, Cẳng tay / lực nắm. **Cơ phụ:** Cầu vai / thang, Mông, Bụng.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Xách tạ một bên như xách vali; (2) Vai hai bên ngang nhau, không nghiêng; (3) Gồng bụng, bước đều; (4) Đổi tay sau mỗi lượt.
- **Lỗi thường gặp:** Nghiêng người về phía tạ hoặc ngược lại; Tạ va vào đùi; Nhún vai bên xách.
- **Tránh nếu:** đau lưng dưới → tập Plank nghiêng (`side_plank`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, tính mét. **Khởi điểm [UNVERIFIED]:** nam 12 kg/tay, nữ 6 kg/tay. Đi 15-20 m mỗi bên.
- **Thay thế (theo thứ tự):** Đi bộ xách tạ hai tay (`farmers_carry_dumbbell`) → Đi bộ ôm tạ ấm trước ngực (`front_carry_kettlebell`) → Plank nghiêng (`side_plank`) → Pallof press với dây (`pallof_press_band`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Đi bộ ôm tạ ấm trước ngực / Kettlebell Goblet Carry

- **id:** `front_carry_kettlebell`
- **Dụng cụ:** Tạ ấm (`kettlebell`)
- **Cơ chính:** Bụng, Cơ dựng sống (lưng dưới). **Cơ phụ:** Cẳng tay / lực nắm, Tay trước, Đùi trước.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Ôm tạ ấm sát ngực, khuỷu khép; (2) Sườn hạ, không ưỡn lưng; (3) Bước ngắn, đều; (4) Thở đều, không nín thở cả lượt.
- **Lỗi thường gặp:** Ngả người ra sau để đỡ tạ; Tạ rời xa ngực; Nín thở.
- **Tránh nếu:** đau lưng dưới → tập Dead bug (`dead_bug`).
- **Kiểu tải:** `kettlebell_kg`, tính mét. **Khởi điểm [UNVERIFIED]:** nam 12 kg, nữ 8 kg. Đi 20-30 m. Không có tạ ấm thì ôm một quả tạ tay dựng đứng.
- **Thay thế (theo thứ tự):** Đi bộ xách tạ hai tay (`farmers_carry_dumbbell`) → Đi bộ xách tạ một tay (`suitcase_carry_dumbbell`) → Bò gấu (`bear_crawl`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Bò gấu / Bear Crawl

- **id:** `bear_crawl`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Bụng, Vai trước. **Cơ phụ:** Đùi trước, Liên sườn, Tay sau.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Chống tay và mũi chân, gối nhấc cách sàn vài cm; (2) Lưng phẳng như mặt bàn; (3) Tay và chân đối bên di chuyển cùng lúc, bước ngắn; (4) Hông không lắc sang hai bên.
- **Lỗi thường gặp:** Chổng mông cao; Bước quá dài làm hông lắc; Nín thở.
- **Tránh nếu:** đau cổ tay → tập Đi bộ xách tạ hai tay (`farmers_carry_dumbbell`); đau vai → tập Đi bộ xách tạ hai tay (`farmers_carry_dumbbell`).
- **Kiểu tải:** `time_seconds`, tính giây. **Khởi điểm [UNVERIFIED]:** nam 20 giây, nữ 15 giây. Phương án không dụng cụ; không thay được phần lực nắm của bài xách tạ.
- **Thay thế (theo thứ tự):** Đi bộ xách tạ hai tay (`farmers_carry_dumbbell`) → Plank (`plank`) → Bird dog (`bird_dog`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

### Tay trước (isolation)

#### Cuốn tay trước thanh đòn / Barbell Curl

- **id:** `barbell_curl`
- **Dụng cụ:** Thanh đòn + bánh tạ (`barbell`)
- **Cơ chính:** Tay trước. **Cơ phụ:** Cẳng tay / lực nắm.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đứng thẳng, nắm ngửa rộng bằng vai; (2) Khuỷu ép sát sườn và đứng yên; (3) Cuốn lên hết tầm, siết; (4) Hạ chậm tới thẳng tay.
- **Lỗi thường gặp:** Ngả lưng vung tạ; Khuỷu trôi ra trước; Không xuống hết tay.
- **Tránh nếu:** đau cổ tay → tập Cuốn tay kiểu búa (`hammer_curl`); đau lưng dưới → tập Cuốn tay trước cáp (`cable_curl`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 15 kg (cả thanh), nữ 10 kg (cả thanh). Dùng thanh ngắn hoặc thanh EZ nếu có; thanh 20 kg quá nặng để bắt đầu.
- **Thay thế (theo thứ tự):** Cuốn tay trước tạ tay (`dumbbell_curl`) → Cuốn tay trước cáp (`cable_curl`) → Cuốn tay trước với dây (`band_curl`).
- **Nguồn:** https://www.strengthlog.com/barbell-curl/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Cuốn tay trước tạ tay / Dumbbell Curl

- **id:** `dumbbell_curl`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Tay trước. **Cơ phụ:** Cẳng tay / lực nắm.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đứng hoặc ngồi, tay thả thẳng, lòng bàn tay hướng trước; (2) Khuỷu đứng yên sát sườn; (3) Cuốn lên, siết 1 giây; (4) Hạ chậm 2-3 giây.
- **Lỗi thường gặp:** Vung người; Nhún vai; Hạ nửa chừng.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 6 kg/tay, nữ 3 kg/tay.
- **Thay thế (theo thứ tự):** Cuốn tay trước thanh đòn (`barbell_curl`) → Cuốn tay trước cáp (`cable_curl`) → Cuốn tay kiểu búa (`hammer_curl`) → Cuốn tay trước với dây (`band_curl`).
- **Nguồn:** https://www.strengthlog.com/dumbbell-curl/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Cuốn tay kiểu búa / Hammer Curl

- **id:** `hammer_curl`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Tay trước, Cẳng tay / lực nắm. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Lòng bàn tay hướng vào nhau suốt động tác; (2) Khuỷu sát sườn; (3) Cuốn lên tới ngang vai; (4) Hạ chậm.
- **Lỗi thường gặp:** Vung tạ; Khuỷu trôi ra trước; Xoay cổ tay giữa chừng.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 6 kg/tay, nữ 3 kg/tay.
- **Thay thế (theo thứ tự):** Cuốn tay trước tạ tay (`dumbbell_curl`) → Cuốn tay trước cáp (`cable_curl`) → Cuốn tay trước với dây (`band_curl`).
- **Nguồn:** https://www.strengthlog.com/hammer-curl/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Cuốn tay trước cáp / Cable Curl

- **id:** `cable_curl`
- **Dụng cụ:** Ròng rọc thấp (cáp dưới) (`cable_low`)
- **Cơ chính:** Tay trước. **Cơ phụ:** Cẳng tay / lực nắm.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Ròng rọc thấp, nắm ngửa thanh ngắn; (2) Đứng cách máy một bước, khuỷu sát sườn; (3) Cuốn lên hết tầm; (4) Hạ chậm, cáp luôn căng.
- **Lỗi thường gặp:** Ngả người ra sau; Khuỷu đưa ra trước; Thả tạ rơi.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 10 kg, nữ 5 kg.
- **Thay thế (theo thứ tự):** Cuốn tay trước tạ tay (`dumbbell_curl`) → Cuốn tay trước thanh đòn (`barbell_curl`) → Cuốn tay trước với dây (`band_curl`).
- **Nguồn:** https://www.strengthlog.com/cable-curl-with-bar/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Cuốn tay trước với dây / Banded Curl

- **id:** `band_curl`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Tay trước. **Cơ phụ:** Cẳng tay / lực nắm.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Giẫm lên dây, nắm ngửa hai đầu; (2) Khuỷu sát sườn; (3) Cuốn lên hết tầm, siết; (4) Hạ chậm, không để dây giật về.
- **Lỗi thường gặp:** Dây chùng ở dưới; Vung người; Khuỷu trôi.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây vừa, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Cuốn tay trước tạ tay (`dumbbell_curl`) → Cuốn tay trước cáp (`cable_curl`) → Cuốn tay trước thanh đòn (`barbell_curl`).
- **Nguồn:** https://www.strengthlog.com/resistance-band-curl/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

### Tay sau (isolation)

#### Duỗi tay sau nằm (skullcrusher) / Lying Barbell Triceps Extension

- **id:** `lying_triceps_extension_barbell`
- **Dụng cụ:** Thanh đòn + bánh tạ + Ghế phẳng (`barbell`, `bench_flat`)
- **Cơ chính:** Tay sau. **Cơ phụ:** không đáng kể.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Nằm ghế, tay thẳng trên vai, nắm hẹp; (2) Gập khuỷu hạ thanh về trán hoặc sau đỉnh đầu; (3) Cánh tay trên gần như đứng yên; (4) Duỗi thẳng tay, siết tay sau.
- **Lỗi thường gặp:** Khuỷu bè rộng ra; Biến thành đẩy ngực hẹp; Tạ quá nặng gây đau khuỷu.
- **Tránh nếu:** đau cổ tay → tập Đẩy cáp tay sau (`triceps_pushdown_cable`); đau vai → tập Đẩy cáp tay sau (`triceps_pushdown_cable`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 15 kg (cả thanh), nữ 10 kg (cả thanh). Dùng thanh ngắn hoặc thanh EZ.
- **Thay thế (theo thứ tự):** Duỗi tay sau qua đầu tạ tay (`overhead_triceps_extension_dumbbell`) → Đẩy cáp tay sau (`triceps_pushdown_cable`) → Chống đẩy tay hẹp (`close_grip_push_up`) → Đẩy dây tay sau (`band_pushdown`).
- **Nguồn:** https://www.strengthlog.com/barbell-lying-triceps-extension/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Duỗi tay sau qua đầu tạ tay / Dumbbell Overhead Triceps Extension

- **id:** `overhead_triceps_extension_dumbbell`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Tay sau. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Hai tay ôm một quả tạ, đưa thẳng lên trên đầu; (2) Khuỷu hướng lên trần, khép vừa phải; (3) Hạ tạ ra sau đầu tới khi tay sau căng; (4) Duỗi thẳng lên, không ưỡn lưng.
- **Lỗi thường gặp:** Khuỷu bè rộng; Ưỡn lưng dưới; Hạ quá nông.
- **Tránh nếu:** đau vai → tập Đẩy cáp tay sau (`triceps_pushdown_cable`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 8 kg (một quả tạ), nữ 4 kg (một quả tạ). Chỉ dùng MỘT quả tạ, hai tay cùng ôm.
- **Thay thế (theo thứ tự):** Duỗi tay sau nằm (skullcrusher) (`lying_triceps_extension_barbell`) → Đẩy cáp tay sau (`triceps_pushdown_cable`) → Đẩy dây tay sau (`band_pushdown`) → Chống đẩy tay hẹp (`close_grip_push_up`).
- **Nghiên cứu:** [UNVERIFIED, theo tóm tắt tìm kiếm] Nhóm Maeo 2022: duỗi khuỷu ở tư thế tay qua đầu tăng cơ tay sau nhiều hơn tư thế tay xuôi (+19,9% so với +13,9%, 12 tuần, mẫu nhỏ). Áp kết quả này sang bài tạ tay là suy rộng.
- **Nguồn:** https://www.strengthlog.com/dumbbell-standing-triceps-extension/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Đẩy cáp tay sau / Cable Triceps Pushdown

- **id:** `triceps_pushdown_cable`
- **Dụng cụ:** Ròng rọc cao (cáp trên) (`cable_high`)
- **Cơ chính:** Tay sau. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Ròng rọc cao, khuỷu ép sát sườn; (2) Thân hơi nghiêng trước; (3) Đẩy xuống tới thẳng tay, siết; (4) Trả chậm tới khi cẳng tay qua mức ngang.
- **Lỗi thường gặp:** Khuỷu trôi ra trước sau; Đè cả người lên thanh; Trả tạ quá nông.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 10 kg, nữ 5 kg.
- **Thay thế (theo thứ tự):** Đẩy dây tay sau (`band_pushdown`) → Duỗi tay sau qua đầu tạ tay (`overhead_triceps_extension_dumbbell`) → Chống đẩy tay hẹp (`close_grip_push_up`).
- **Nguồn:** https://www.strengthlog.com/tricep-pushdown-with-bar/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Chống xà kép / Parallel Bar Dip

- **id:** `dip`
- **Dụng cụ:** Xà kép (`dip_bar`)
- **Cơ chính:** Tay sau, Ngực. **Cơ phụ:** Vai trước.
- **Độ khó:** 3/3. **Người mới:** chưa nên, tập bài dễ hơn trong thang trước.
- **Kỹ thuật:** (1) Chống thẳng tay, vai hạ xuống (không rụt cổ); (2) Hạ tới khi cánh tay trên khoảng song song sàn; (3) Khuỷu hướng ra sau, thân hơi nghiêng trước; (4) Đẩy lên thẳng tay.
- **Lỗi thường gặp:** Hạ quá sâu khi vai chưa quen; Rụt vai lên tai; Đung đưa chân.
- **Tránh nếu:** đau vai → tập Đẩy cáp tay sau (`triceps_pushdown_cable`); đau cổ tay → tập Đẩy cáp tay sau (`triceps_pushdown_cable`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Chống đẩy tay hẹp (`close_grip_push_up`) → Đẩy cáp tay sau (`triceps_pushdown_cable`) → Đẩy ngực tạ tay (`dumbbell_bench_press`).
- **Nguồn:** https://www.strengthlog.com/bar-dip/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Đẩy dây tay sau / Banded Triceps Pushdown

- **id:** `band_pushdown`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Tay sau. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Móc dây lên điểm cao (xà, móc tường); (2) Khuỷu sát sườn; (3) Đẩy xuống tới thẳng tay, siết 1 giây; (4) Trả chậm.
- **Lỗi thường gặp:** Khuỷu trôi; Gập người đè xuống; Dây chùng ở trên.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây vừa, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Đẩy cáp tay sau (`triceps_pushdown_cable`) → Duỗi tay sau qua đầu tạ tay (`overhead_triceps_extension_dumbbell`) → Chống đẩy tay hẹp (`close_grip_push_up`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Chống đẩy tay hẹp / Close-Grip Push-Up

- **id:** `close_grip_push_up`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Tay sau, Ngực. **Cơ phụ:** Vai trước, Bụng.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Tay đặt hẹp hơn vai một chút; (2) Khuỷu đi sát sườn; (3) Thân thẳng, bụng gồng; (4) Kê tay lên ghế nếu chưa đủ sức.
- **Lỗi thường gặp:** Khuỷu bè ra ngoài; Võng hông; Hạ nửa chừng.
- **Tránh nếu:** đau cổ tay → tập Đẩy dây tay sau (`band_pushdown`); đau vai → tập Đẩy dây tay sau (`band_pushdown`).
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Đẩy dây tay sau (`band_pushdown`) → Đẩy cáp tay sau (`triceps_pushdown_cable`) → Duỗi tay sau qua đầu tạ tay (`overhead_triceps_extension_dumbbell`).
- **Nguồn:** https://www.strengthlog.com/close-grip-push-up/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

### Vai giữa (isolation)

#### Kéo thanh đòn lên cằm (nắm rộng) / Wide-Grip Barbell Upright Row

- **id:** `upright_row_barbell`
- **Dụng cụ:** Thanh đòn + bánh tạ (`barbell`)
- **Cơ chính:** Vai giữa, Cầu vai / thang. **Cơ phụ:** Tay trước, Vai trước.
- **Độ khó:** 2/3. **Người mới:** chưa nên, tập bài dễ hơn trong thang trước.
- **Kỹ thuật:** (1) Nắm rộng hơn vai; (2) Kéo khuỷu lên và ra ngoài; (3) Dừng khi khuỷu ngang vai (thanh ngang ngực dưới); (4) Hạ chậm.
- **Lỗi thường gặp:** Nắm hẹp và kéo quá cao (dễ kẹt vai); Vung người; Bẻ gập cổ tay.
- **Tránh nếu:** đau vai → tập Dang dây ngang vai (`band_lateral_raise`); đau cổ tay → tập Dang tạ ngang vai (`dumbbell_lateral_raise`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 15 kg (cả thanh), nữ 10 kg (cả thanh). Dùng thanh ngắn/nhẹ. Bài này dễ gây khó chịu vai; có tạ tay thì ưu tiên dang tạ ngang.
- **Thay thế (theo thứ tự):** Dang tạ ngang vai (`dumbbell_lateral_raise`) → Dang cáp ngang vai (`cable_lateral_raise`) → Dang dây ngang vai (`band_lateral_raise`).
- **Nguồn:** https://www.strengthlog.com/barbell-upright-row/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Dang tạ ngang vai / Dumbbell Lateral Raise

- **id:** `dumbbell_lateral_raise`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Vai giữa. **Cơ phụ:** Vai trước, Cầu vai / thang.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Tạ hai bên hông, khuỷu hơi chùng; (2) Nâng sang hai bên tới khi cánh tay ngang sàn; (3) Không nâng cao quá vai; (4) Hạ chậm có kiểm soát.
- **Lỗi thường gặp:** Tạ quá nặng; Vung người lấy đà; Nhún vai làm cầu vai gánh hết.
- **Tránh nếu:** đau vai → tập Dang dây ngang vai (`band_lateral_raise`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 3 kg/tay, nữ 2 kg/tay. Phòng không có tạ 1-3 kg thì dùng dây, cáp hoặc bánh tạ nhỏ.
- **Thay thế (theo thứ tự):** Dang cáp ngang vai (`cable_lateral_raise`) → Dang dây ngang vai (`band_lateral_raise`) → Kéo thanh đòn lên cằm (nắm rộng) (`upright_row_barbell`).
- **Nguồn:** https://www.strengthlog.com/dumbbell-lateral-raise/ · đã đọc và đối chiếu.

#### Dang cáp ngang vai / Cable Lateral Raise

- **id:** `cable_lateral_raise`
- **Dụng cụ:** Ròng rọc thấp (cáp dưới) (`cable_low`)
- **Cơ chính:** Vai giữa. **Cơ phụ:** Vai trước, Cầu vai / thang.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Ròng rọc thấp (khoảng dưới hông), đứng ngang máy, cầm bằng tay xa máy; (2) Khuỷu hơi chùng; (3) Nâng tay sang bên tới ngang vai; (4) Hạ chậm, cáp luôn căng.
- **Lỗi thường gặp:** Nhún vai; Nghiêng người kéo; Nâng cao quá vai.
- **Tránh nếu:** đau vai → tập Dang dây ngang vai (`band_lateral_raise`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 2,5 kg, nữ 1,25 kg. Dùng nấc nhẹ nhất của máy; nấc đầu vẫn quá nặng thì chuyển sang dây.
- **Thay thế (theo thứ tự):** Dang tạ ngang vai (`dumbbell_lateral_raise`) → Dang dây ngang vai (`band_lateral_raise`).
- **Nguồn:** https://www.strengthlog.com/cable-lateral-raise/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Dang dây ngang vai / Banded Lateral Raise

- **id:** `band_lateral_raise`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Vai giữa. **Cơ phụ:** Cầu vai / thang.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Giẫm lên dây, cầm hai đầu (hoặc tập từng tay); (2) Khuỷu hơi chùng; (3) Nâng sang bên tới ngang vai; (4) Hạ chậm.
- **Lỗi thường gặp:** Dây quá căng nên phải nhún vai; Vung người; Nâng quá vai.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây nhẹ, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Dang tạ ngang vai (`dumbbell_lateral_raise`) → Dang cáp ngang vai (`cable_lateral_raise`).
- **Nguồn:** https://www.strengthlog.com/resistance-band-lateral-raise/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

### Bắp chân (isolation)

#### Nhón bắp chân máy đứng / Standing Calf Raise Machine

- **id:** `standing_calf_raise_machine`
- **Dụng cụ:** Máy nhón bắp chân (`calf_machine`)
- **Cơ chính:** Bắp chân. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đặt nửa trước bàn chân lên bục; (2) Hạ gót xuống thấp hết tầm, dừng 1 giây; (3) Nhón lên cao hết tầm, siết; (4) Gối gần thẳng suốt động tác.
- **Lỗi thường gặp:** Nảy tưng tưng ở dưới; Biên độ ngắn; Gập gối đẩy bằng đùi.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 30 kg, nữ 15 kg.
- **Thay thế (theo thứ tự):** Nhón bắp chân khung Smith (`smith_calf_raise`) → Nhón bắp chân trên máy đạp đùi (`leg_press_calf_raise`) → Nhón bắp chân một chân cầm tạ (`single_leg_calf_raise_dumbbell`) → Nhón bắp chân một chân không tạ (`single_leg_calf_raise_bodyweight`).
- **Nguồn:** https://www.strengthlog.com/standing-calf-raise/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Nhón bắp chân khung Smith / Smith Machine Calf Raise

- **id:** `smith_calf_raise`
- **Dụng cụ:** Khung Smith (`smith`)
- **Cơ chính:** Bắp chân. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Gánh thanh Smith trên cầu vai, mũi chân trên bục hoặc bánh tạ; (2) Hạ gót hết tầm; (3) Nhón cao hết tầm, siết 1 giây; (4) Gối gần thẳng.
- **Lỗi thường gặp:** Nảy ở dưới; Bục kê không chắc; Biên độ ngắn.
- **Tránh nếu:** đau lưng dưới → tập Nhón bắp chân trên máy đạp đùi (`leg_press_calf_raise`).
- **Kiểu tải:** `added_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 20 kg lắp thêm, nữ 10 kg lắp thêm. Số kg là tạ lắp thêm.
- **Thay thế (theo thứ tự):** Nhón bắp chân trên máy đạp đùi (`leg_press_calf_raise`) → Nhón bắp chân một chân cầm tạ (`single_leg_calf_raise_dumbbell`) → Nhón bắp chân một chân không tạ (`single_leg_calf_raise_bodyweight`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Nhón bắp chân trên máy đạp đùi / Leg Press Calf Raise

- **id:** `leg_press_calf_raise`
- **Dụng cụ:** Máy đạp đùi (`leg_press`)
- **Cơ chính:** Bắp chân. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đặt mũi chân ở mép dưới bàn đạp, gối gần thẳng; (2) Để gót hạ về phía mình hết tầm; (3) Đẩy bằng mũi chân hết tầm; (4) KHÔNG mở chốt an toàn của máy.
- **Lỗi thường gặp:** Mở chốt an toàn (chân trượt là bàn đạp sập); Gập gối để đẩy; Biên độ ngắn.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 40 kg, nữ 20 kg.
- **Thay thế (theo thứ tự):** Nhón bắp chân khung Smith (`smith_calf_raise`) → Nhón bắp chân một chân cầm tạ (`single_leg_calf_raise_dumbbell`) → Nhón bắp chân một chân không tạ (`single_leg_calf_raise_bodyweight`).
- **Nguồn:** https://www.strengthlog.com/calf-raise-in-leg-press/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Nhón bắp chân một chân cầm tạ / Single-Leg Dumbbell Calf Raise

- **id:** `single_leg_calf_raise_dumbbell`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Bắp chân. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đứng một chân trên bậc/bánh tạ, tay cùng bên cầm tạ, tay kia vịn; (2) Hạ gót hết tầm; (3) Nhón cao hết tầm, siết; (4) Lên xuống chậm.
- **Lỗi thường gặp:** Nảy lấy đà; Biên độ ngắn; Vịn tay kéo người lên.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 8 kg/tay, nữ 4 kg/tay.
- **Thay thế (theo thứ tự):** Nhón bắp chân khung Smith (`smith_calf_raise`) → Nhón bắp chân trên máy đạp đùi (`leg_press_calf_raise`) → Nhón bắp chân một chân không tạ (`single_leg_calf_raise_bodyweight`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

#### Nhón bắp chân một chân không tạ / Bodyweight Single-Leg Calf Raise

- **id:** `single_leg_calf_raise_bodyweight`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Bắp chân. **Cơ phụ:** không đáng kể.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đứng một chân trên bậc thang, vịn nhẹ; (2) Hạ gót hết tầm, dừng 1 giây; (3) Nhón cao hết tầm; (4) Chưa đủ sức thì làm hai chân.
- **Lỗi thường gặp:** Nảy ở dưới; Biên độ ngắn; Làm quá nhanh.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Nhón bắp chân một chân cầm tạ (`single_leg_calf_raise_dumbbell`) → Nhón bắp chân khung Smith (`smith_calf_raise`) → Nhón bắp chân trên máy đạp đùi (`leg_press_calf_raise`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

### Mông / hip thrust

#### Hip thrust thanh đòn / Barbell Hip Thrust

- **id:** `barbell_hip_thrust`
- **Dụng cụ:** Thanh đòn + bánh tạ + Ghế phẳng (`barbell`, `bench_flat`)
- **Cơ chính:** Mông. **Cơ phụ:** Đùi trong, Đùi trước, Đùi sau.
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Tựa lưng trên (dưới bả vai) vào ghế chắc, lăn thanh lên nếp hông, lót đệm; (2) Chân rộng bằng vai, gối co; (3) Đẩy hông lên tới khi gối gập khoảng 90°, siết mông; (4) Hạ có kiểm soát, tay giữ thanh.
- **Lỗi thường gặp:** Không lót đệm nên đau xương hông; Ưỡn lưng dưới thay vì duỗi hông; Ghế không chắc, bị trượt.
- **Tránh nếu:** đau lưng dưới → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `barbell_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 30 kg (cả thanh), nữ 20 kg (cả thanh).
- **Thay thế (theo thứ tự):** Hip thrust tạ tay (`dumbbell_hip_thrust`) → Cầu mông một chân (`single_leg_glute_bridge`) → Cầu mông với dây (`band_glute_bridge`) → Đá mông với cáp (`cable_kickback`).
- **Nghiên cứu:** [UNVERIFIED, theo tóm tắt tìm kiếm] Contreras 2015: hip thrust cho EMG mông cao hơn squat (13 nữ đã tập luyện). Nhưng Plotkin 2023 (9 tuần, đo MRI) thấy mức tăng cơ mông của squat và hip thrust tương đương. Bài nào cũng được, chọn theo dụng cụ.
- **Nguồn:** https://www.strengthlog.com/hip-thrust/ · đã đọc và đối chiếu.

#### Hip thrust tạ tay / Dumbbell Hip Thrust

- **id:** `dumbbell_hip_thrust`
- **Dụng cụ:** Tạ tay (tạ đơn) + Ghế phẳng (`dumbbell`, `bench_flat`)
- **Cơ chính:** Mông. **Cơ phụ:** Đùi sau, Đùi trước.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Tựa lưng trên vào ghế, đặt một quả tạ nằm ngang trên nếp hông; (2) Chân rộng bằng vai, bàn chân phẳng; (3) Đẩy hông lên tới khi thân song song sàn, siết mông 1 giây; (4) Hạ chậm.
- **Lỗi thường gặp:** Ưỡn lưng dưới; Chân đặt quá xa (ăn đùi sau) hoặc quá gần (ăn đùi trước); Ngửa cổ ra sau.
- **Tránh nếu:** đau lưng dưới → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 12 kg (một quả tạ), nữ 8 kg (một quả tạ). Chỉ dùng MỘT quả tạ đặt trên hông.
- **Thay thế (theo thứ tự):** Hip thrust thanh đòn (`barbell_hip_thrust`) → Cầu mông một chân (`single_leg_glute_bridge`) → Cầu mông với dây (`band_glute_bridge`) → Đá mông với cáp (`cable_kickback`).
- **Nguồn:** https://www.strengthlog.com/hip-thrust/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Đá mông với cáp / Cable Glute Kickback

- **id:** `cable_kickback`
- **Dụng cụ:** Ròng rọc thấp (cáp dưới) (`cable_low`)
- **Cơ chính:** Mông. **Cơ phụ:** Đùi sau.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đeo đai cổ chân vào ròng rọc thấp, vịn máy, thân hơi nghiêng trước; (2) Đá chân thẳng ra sau bằng mông; (3) Dừng khi hông hết tầm, không ưỡn lưng; (4) Về chậm.
- **Lỗi thường gặp:** Ưỡn lưng dưới để đá cao hơn; Vung chân lấy đà; Xoay mở hông.
- **Tránh nếu:** đau lưng dưới → tập Cầu mông (`glute_bridge`).
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 5 kg, nữ 2,5 kg. Cần đai đeo cổ chân; phòng thường không có sẵn.
- **Thay thế (theo thứ tự):** Cầu mông một chân (`single_leg_glute_bridge`) → Cầu mông với dây (`band_glute_bridge`) → Hip thrust tạ tay (`dumbbell_hip_thrust`).
- **Nguồn:** https://www.strengthlog.com/cable-glute-kickback/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Cầu mông với dây / Banded Glute Bridge

- **id:** `band_glute_bridge`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Mông, Mông nhỡ (dạng hông). **Cơ phụ:** Đùi sau.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Đeo dây vòng ngay trên gối, nằm ngửa, gối co; (2) Đẩy gối ra ngoài chống lại dây; (3) Đẩy hông lên, siết mông 2 giây; (4) Hạ chậm.
- **Lỗi thường gặp:** Gối bị dây kéo vào trong; Ưỡn lưng; Đẩy bằng mũi chân.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây vừa, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Cầu mông (`glute_bridge`) → Cầu mông một chân (`single_leg_glute_bridge`) → Hip thrust tạ tay (`dumbbell_hip_thrust`).
- **Nguồn:** https://www.strengthlog.com/glute-bridge/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Cầu mông một chân / Single-Leg Glute Bridge

- **id:** `single_leg_glute_bridge`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Mông. **Cơ phụ:** Đùi sau, Mông nhỡ (dạng hông).
- **Độ khó:** 2/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Nằm ngửa, một chân co đặt sàn, chân kia nhấc lên; (2) Đẩy hông lên bằng gót chân trụ; (3) Hai bên hông ngang nhau; (4) Siết mông 1-2 giây rồi hạ.
- **Lỗi thường gặp:** Hông bên chân nhấc bị rơi xuống; Ưỡn lưng; Chuột rút đùi sau do chân đặt quá xa.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Cầu mông với dây (`band_glute_bridge`) → Hip thrust tạ tay (`dumbbell_hip_thrust`) → Cầu mông (`glute_bridge`).
- **Nguồn:** https://www.strengthlog.com/one-legged-glute-bridge/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Cầu mông / Glute Bridge

- **id:** `glute_bridge`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Mông. **Cơ phụ:** Đùi sau, Bụng.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Nằm ngửa, gối co, bàn chân phẳng trên sàn, tay dọc thân; (2) Gồng nhẹ bụng; (3) Đẩy hông lên bằng cách siết mông tới khi thân thẳng từ vai tới gối; (4) Hạ chậm.
- **Lỗi thường gặp:** Ưỡn lưng dưới thay vì siết mông; Đẩy bằng mũi chân; Lên quá nhanh, không siết.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Cầu mông với dây (`band_glute_bridge`) → Cầu mông một chân (`single_leg_glute_bridge`) → Hip thrust tạ tay (`dumbbell_hip_thrust`).
- **Nguồn:** https://www.acefitness.org/resources/everyone/exercise-library/57/glute-bridge/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

### Vai sau (isolation)

#### Dang tạ vai sau (gập người) / Bent-Over Reverse Dumbbell Fly

- **id:** `reverse_dumbbell_fly`
- **Dụng cụ:** Tạ tay (tạ đơn) (`dumbbell`)
- **Cơ chính:** Vai sau. **Cơ phụ:** Cơ trám (giữa lưng), Cầu vai / thang.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Gập hông, lưng thẳng, thân gần song song sàn; (2) Khuỷu hơi chùng; (3) Dang tạ sang hai bên tới ngang vai; (4) Hạ chậm.
- **Lỗi thường gặp:** Tạ quá nặng nên phải giật; Đứng thẳng dần lên; Kéo khuỷu ra sau thành bài kéo lưng.
- **Tránh nếu:** đau lưng dưới → tập Kéo giãn dây ngang ngực (`band_pull_apart`).
- **Kiểu tải:** `dumbbell_kg_per_hand`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 3 kg/tay, nữ 2 kg/tay.
- **Thay thế (theo thứ tự):** Face pull với cáp (`face_pull_cable`) → Kéo giãn dây ngang ngực (`band_pull_apart`) → Nằm sấp nâng tay chữ Y (`prone_y_raise`).
- **Nguồn:** https://www.strengthlog.com/reverse-dumbbell-flyes/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Face pull với cáp / Cable Face Pull

- **id:** `face_pull_cable`
- **Dụng cụ:** Ròng rọc cao (cáp trên) (`cable_high`)
- **Cơ chính:** Vai sau. **Cơ phụ:** Cầu vai / thang, Cơ trám (giữa lưng), Chóp xoay.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Ròng rọc ngang mặt hoặc cao hơn, dùng dây thừng; (2) Kéo dây về phía mặt, khuỷu cao và mở rộng; (3) Cuối động tác xoay tay ra ngoài (như gồng khoe tay); (4) Trả chậm.
- **Lỗi thường gặp:** Tạ quá nặng nên ngả người; Khuỷu hạ thấp thành bài kéo ngang; Nhún vai.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `machine_kg`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam 10 kg, nữ 5 kg.
- **Thay thế (theo thứ tự):** Kéo giãn dây ngang ngực (`band_pull_apart`) → Dang tạ vai sau (gập người) (`reverse_dumbbell_fly`) → Nằm sấp nâng tay chữ Y (`prone_y_raise`).
- **Nguồn:** https://www.strengthlog.com/face-pull/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Kéo giãn dây ngang ngực / Band Pull-Apart

- **id:** `band_pull_apart`
- **Dụng cụ:** Dây kháng lực (`band`)
- **Cơ chính:** Vai sau. **Cơ phụ:** Cơ trám (giữa lưng), Cầu vai / thang.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Cầm dây trước ngực, tay gần thẳng; (2) Kéo hai tay sang hai bên tới khi dây chạm ngực; (3) Siết bả vai 1 giây; (4) Về chậm.
- **Lỗi thường gặp:** Nhún vai; Ưỡn lưng; Co khuỷu nhiều.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `band_level`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam dây nhẹ, nữ dây nhẹ.
- **Thay thế (theo thứ tự):** Face pull với cáp (`face_pull_cable`) → Dang tạ vai sau (gập người) (`reverse_dumbbell_fly`) → Nằm sấp nâng tay chữ Y (`prone_y_raise`).
- **Nguồn:** https://www.strengthlog.com/band-pull-apart/ · [UNVERIFIED] có URL nhưng chưa đối chiếu nội dung.

#### Nằm sấp nâng tay chữ Y / Prone Y Raise

- **id:** `prone_y_raise`
- **Dụng cụ:** Không cần dụng cụ (`none`)
- **Cơ chính:** Vai sau, Cầu vai / thang. **Cơ phụ:** Cơ trám (giữa lưng), Chóp xoay.
- **Độ khó:** 1/3. **Người mới:** phù hợp.
- **Kỹ thuật:** (1) Nằm sấp trên sàn hoặc ghế, tay duỗi chếch thành chữ Y, ngón cái hướng lên; (2) Nâng tay khỏi sàn bằng cách siết bả vai; (3) Giữ 2 giây; (4) Hạ chậm.
- **Lỗi thường gặp:** Ngửa cổ; Ưỡn lưng dưới để nâng tay; Nhún vai lên tai.
- **Tránh nếu:** không có lưu ý riêng.
- **Kiểu tải:** `bodyweight_reps`, đếm lần. **Khởi điểm [UNVERIFIED]:** nam trọng lượng cơ thể, nữ trọng lượng cơ thể.
- **Thay thế (theo thứ tự):** Kéo giãn dây ngang ngực (`band_pull_apart`) → Dang tạ vai sau (gập người) (`reverse_dumbbell_fly`) → Face pull với cáp (`face_pull_cable`).
- **Nguồn:** [UNVERIFIED] chưa có nguồn.

## Nguồn

Đã đọc nội dung:

- Stronger By Science, How to Squat: https://www.strongerbyscience.com/how-to-squat/
- Stronger By Science, How to Bench: https://www.strongerbyscience.com/how-to-bench/
- Stronger By Science, How to Deadlift: https://www.strongerbyscience.com/how-to-deadlift/
- Squat University, The McGill Big 3: https://squatuniversity.com/2018/06/21/the-mcgill-big-3-for-core-stability/
- StrengthLog, danh mục bài tập (đọc danh mục và 12 trang bài cụ thể, dẫn ở từng bài): https://www.strengthlog.com/exercise-directory/

Chỉ thấy qua kết quả tìm kiếm, chưa đọc được trang:

- ExRx.net (lỗi 403): https://exrx.net/WeightExercises/Quadriceps/BBSquat
- NSCA, Romanian Deadlift (lỗi 403): https://www.nsca.com/education/articles/kinetic-select/romanian-deadlift-rdl/
- ACE, Seated Row và Glute Bridge (từ chối kết nối): https://www.acefitness.org/resources/everyone/exercise-library/48/seated-row/ · https://www.acefitness.org/resources/everyone/exercise-library/57/glute-bridge/
- Contreras 2015: https://pubmed.ncbi.nlm.nih.gov/26214739/
- Nghiên cứu móc đùi ngồi và nằm: https://pubmed.ncbi.nlm.nih.gov/33009197/
- Maeo 2022: https://informahealthcare.com/doi/full/10.1080/17461391.2022.2100279
- Calatayud 2015 (bài tường thuật): https://breakingmuscle.com/emg-analysis-of-the-bench-press-and-push-up/
- Plotkin 2023 (Frontiers in Physiology): chỉ có trong tóm tắt tìm kiếm, chưa có URL.
- Jeff Nippard: không tìm được trang gốc đọc được, chỉ có bài tường thuật lại, nên không dùng làm nguồn cho cue nào.
