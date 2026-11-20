# 08 — Danh sách màn hình và kế hoạch xây app Ba Vía

Ngày: 2026-11-20. Bản máy đọc: [screens.json](screens.json) (cùng nội dung, dùng để theo dõi tiến độ).

Đọc cùng: [00-plan.md](../research/00-plan.md), [01-programming.md](../research/01-programming.md), [03-app-patterns.md](../research/03-app-patterns.md), [06-avatar-wardrobe.md](06-avatar-wardrobe.md), [07-cast-pitches.md](07-cast-pitches.md) mục C, [screens-v2.html](screens-v2.html).

## 0. Tóm tắt

- App có **96 màn** (tính cả tấm trượt và thông báo có nội dung riêng), chia 7 luồng. **79 màn thuộc MVP**, 14 màn để bản 1.1, 3 màn để về sau.
- **6 màn đã thiết kế** ở bản v2 và đã được duyệt hướng; cả 6 đều còn thiếu trạng thái (ghi ở từng màn). Còn **90 màn chưa thiết kế**, trong đó 73 màn thuộc MVP.
- Việc lớn nhất chưa có lời giải không nằm ở màn hình mà ở hình: **vía đúng giống, đúng màu, mặc đúng đồ phải hiện được ở mọi màn** (quyết định D2). Bản v2 mới chỉ vẽ một con Khăn màu mint.
- Lộ trình: chốt quyết định → 4 đợt thiết kế → hình và spec chạy song song → 3 lát cắt code (một người, tổ, tủ đồ) → thử với nhóm thật.

| Luồng | Tổng | MVP | v1.1 | Về sau | Đã thiết kế |
|---|---|---|---|---|---|
| 0. Lần đầu mở app và onboarding | 19 | 18 | 1 | 0 | 0 |
| 1. Vòng lặp hằng ngày | 19 | 19 | 0 | 0 | 4 |
| 2. Nhóm (tổ) | 14 | 9 | 3 | 2 | 1 |
| 3. Tủ đồ | 6 | 3 | 2 | 1 | 1 |
| 4. Tiến độ | 9 | 6 | 3 | 0 | 0 |
| 5. Tôi và cài đặt | 13 | 11 | 2 | 0 | 0 |
| 6. Hệ thống và tình huống đặc biệt | 16 | 13 | 3 | 0 | 0 |
| **Cộng** | **96** | **79** | **14** | **3** | **6** |

## 1. Các quyết định đã khoá mà tài liệu này tuân theo

| Quyết định | Hệ quả trong danh sách màn |
|---|---|
| Không chia sẻ ra ngoài | "Thẻ chia sẻ Zalo/Messenger" của kế hoạch gốc thành bài đăng vào bảng tin của tổ (1.6, 2.1). Mời bạn bằng mã sao chép được (2.6) |
| Tổ có ngay trong MVP (Firebase) | Luồng 2 thuộc MVP. Các chỗ trong 03-app-patterns ghi "giai đoạn 2" cho bảng nhóm, feed, streak nhóm không còn đúng |
| Mỗi người nhiều phòng tập | 0.10–0.12, 5.4, 5.4a, chọn phòng ở check-in (1.2) |
| PWA cho iPhone và Android | 0.2 cài lên màn hình chính, 5.6 sao lưu, 6.10 máy mất dữ liệu đều thuộc MVP |
| 1 mảnh mỗi buổi, N mảnh ra 1 món, tối đa 1 món mỗi tuần | 1.6, 1.6a, 1.6b; trạng thái "tuần này đủ rồi" |
| Đồ phải mặc thật lên vía bằng mesh 3D | Mọi cột "hình cần làm" của món đồ tính theo cả ba giống |
| Hình làm mẫu là bóng trong gương | 1.4, 1.4a. Người que SVG của Q4 cũ đã bỏ |
| Chưa duyệt thiết kế thì chưa code | Các giai đoạn code có giao diện đứng sau các đợt thiết kế tương ứng |

Quy ước mã màn: `N.M` là một màn đầy đủ; thêm chữ cái (`1.4b`) là tấm trượt, thông báo hoặc khoảnh khắc mở từ màn `N.M`. Trạng thái đơn thuần (ngày nghỉ, mất mạng, trống) nằm trong mục "trạng thái" của màn chủ; luồng 6 chỉ giữ các tình huống cắt ngang nhiều màn.

## 2. Bảng theo dõi

Đánh dấu vào ô khi màn được người dùng duyệt thiết kế.

### Luồng 0: Lần đầu mở app và onboarding

| Duyệt | Mã | Màn | Ưu tiên | Trạng thái | Mục đích |
|---|---|---|---|---|---|
| ☐ | 0.1 | Chào mừng: hộp đồ bỏ quên | MVP | Chưa thiết kế | Giới thiệu thế giới Ba Vía trong một màn và mời bắt đầu. |
| ☐ | 0.2 | Cài lên màn hình chính | MVP | Chưa thiết kế | Đưa app ra màn hình chính trước khi nhập dữ liệu, để dữ liệu nằm đúng chỗ và ít bị iOS xoá. |
| ☐ | 0.3 | Nhận vía: chọn giống | MVP | Chưa thiết kế | Người dùng chọn một trong ba giống vía làm bạn tập và làm avatar. |
| ☐ | 0.4 | Đặt tên và chọn màu vía | MVP | Chưa thiết kế | Biến con vía thành của riêng người dùng: tên và màu. |
| ☐ | 0.5 | Hồ sơ: về người dùng | MVP | Chưa thiết kế | Lấy thông tin cơ bản để tính mức tạ khởi điểm và bước tăng tạ. |
| ☐ | 0.6 | Mục tiêu và trình độ | MVP | Chưa thiết kế | Chọn mục tiêu tập và trình độ để chọn khung tuần, khoảng rep và thuật toán tăng tạ. |
| ☐ | 0.7 | Lời hứa tuần và thời lượng | MVP | Chưa thiết kế | Người dùng tự chọn số buổi mỗi tuần (N) và số phút mặc định mỗi buổi. |
| ☐ | 0.8 | Sàng lọc sức khoẻ | MVP | Chưa thiết kế | Hỏi các câu sàng lọc trước khi tập (kiểu PAR-Q+) để biết ai cần hỏi bác sĩ trước. |
| ☐ | 0.8a | Khuyên hỏi bác sĩ trước | MVP | Chưa thiết kế | Báo cho người có câu trả lời "Có" rằng nên hỏi bác sĩ, và cho họ dùng app ở chế độ nhẹ trong lúc chờ. |
| ☐ | 0.9 | Vùng hay đau hoặc chấn thương cũ | MVP | Chưa thiết kế | Khai vùng cơ thể cần tránh để app chọn bài an toàn hơn. |
| ☐ | 0.10 | Phòng tập đầu tiên | MVP | Chưa thiết kế | Tạo hồ sơ phòng tập đầu tiên: tên và điểm xuất phát. |
| ☐ | 0.11 | Checklist dụng cụ của phòng | MVP | Chưa thiết kế | Đánh dấu phòng này có những dụng cụ gì, để app chỉ ra bài tập làm được. |
| ☐ | 0.12 | Bước tạ của phòng | MVP | Chưa thiết kế | Khai thanh đòn nặng bao nhiêu, đĩa nhỏ nhất, tạ tay nhảy mấy kg, để gợi ý tăng tạ đúng với tạ thật. |
| ☐ | 0.13 | Dụng cụ cá nhân | MVP | Chưa thiết kế | Khai dụng cụ người dùng luôn mang theo, coi là có sẵn ở mọi phòng. |
| ☐ | 0.14 | Tổ: tạo hoặc vào | MVP | Chưa thiết kế | Đưa người dùng vào nhóm bạn ngay từ đầu, hoặc cho bỏ qua. |
| ☐ | 0.14a | Lập tổ mới | MVP | Chưa thiết kế | Tạo một tổ và nhận mã để mời bạn. |
| ☐ | 0.14b | Vào tổ bằng mã | MVP | Chưa thiết kế | Nhập mã tổ bạn gửi để vào nhóm. |
| ☐ | 0.15 | Bộ khởi đầu và tuần đầu tiên | MVP | Chưa thiết kế | Kết thúc onboarding: tặng bộ khởi đầu và cho thấy tuần đầu trông thế nào. |
| ☐ | 0.16 | Bật thông báo | v1.1 | Chưa thiết kế | Xin quyền gửi thông báo, chỉ sau khi người dùng bấm nút. |

### Luồng 1: Vòng lặp hằng ngày

| Duyệt | Mã | Màn | Ưu tiên | Trạng thái | Mục đích |
|---|---|---|---|---|---|
| ☐ | 1.1 | Hôm nay | MVP | Đã thiết kế (v2) | Màn chính: hôm nay tập gì, tuần này đến đâu, một nút vào tập. |
| ☐ | 1.2 | Check-in | MVP | Đã thiết kế (v2) | Hỏi nhanh tình trạng hôm nay để chỉnh buổi tập; ngày bình thường chỉ cần một chạm. |
| ☐ | 1.2a | Hôm nay đau chỗ nào? (tấm trượt) | MVP | Chưa thiết kế | Khai vùng đang đau hôm nay và mức đau, để app tránh hoặc giảm bài chạm vùng đó. |
| ☐ | 1.2b | Hôm nay vùng đỏ: chọn cách tập | MVP | Chưa thiết kế | Khi rất mệt, cho chọn buổi rút gọn, đi bộ, hoặc nghỉ, và nói rõ cả ba đều ổn. |
| ☐ | 1.3 | Buổi tập hôm nay (xem trước) | MVP | Chưa thiết kế | Cho xem cả buổi trước khi tập: bài nào, mấy set, vì sao khác mọi khi. |
| ☐ | 1.4 | Đang tập | MVP | Đã thiết kế (v2) | Ghi từng set bằng một chạm, có bóng trong gương làm mẫu và đồng hồ nghỉ. |
| ☐ | 1.4a | Hướng dẫn động tác | MVP | Chưa thiết kế | Xem kỹ một bài: bóng trong gương chạy chậm, các ý chính và lỗi hay gặp. |
| ☐ | 1.4b | Báo đau giữa buổi (tấm trượt) | MVP | Chưa thiết kế | Báo đau ngay trong lúc tập và nhận cách xử lý ngay. |
| ☐ | 1.4c | Hỏi bước tạ lần đầu dùng dụng cụ (tấm trượt) | MVP | Chưa thiết kế | Lần đầu gặp một dụng cụ chưa khai bước tạ, hỏi đúng một câu rồi nhớ cho phòng đó. |
| ☐ | 1.4d | Sửa số và ghi chú bài (tấm trượt) | MVP | Chưa thiết kế | Nhập tạ hoặc số lần bằng bàn phím số khi lệch nhiều, và ghim ghi chú cho bài. |
| ☐ | 1.4e | Kỷ lục mới tại chỗ (thông báo nổi) | MVP | Chưa thiết kế | Báo ngay khi set vừa xong là kỷ lục cá nhân của bài đó. |
| ☐ | 1.4f | App tự chỉnh giữa buổi (thông báo) | MVP | Chưa thiết kế | Nói rõ khi app hạ tạ hoặc hạ vùng vì set đầu hụt nhiều, hoặc nâng lại khi làm dư. |
| ☐ | 1.4g | Dừng buổi giữa chừng (xác nhận) | MVP | Chưa thiết kế | Cho thoát buổi mà không mất những gì đã ghi. |
| ☐ | 1.5 | Buổi này thế nào? | MVP | Chưa thiết kế | Một câu hỏi sau buổi, bỏ qua được, làm dữ liệu cho lần tăng tạ sau. |
| ☐ | 1.6 | Xong buổi | MVP | Đã thiết kế (v2) | Khen buổi tập trước, rồi mới tới mảnh đồ; mời gửi vào tổ. |
| ☐ | 1.6a | Nhận món: thanh đầy | MVP | Chưa thiết kế | Khoảnh khắc mở khoá khi mảnh cuối làm đầy thanh: món đồ về tủ và vía mặc ngay. |
| ☐ | 1.6b | Chọn món kế tiếp (1 trong 3) | MVP | Chưa thiết kế | Sau khi nhận món, chọn món sẽ gom ở chu kỳ tới trong 3 món đang bày. |
| ☐ | 1.6c | Chạm mốc | MVP | Chưa thiết kế | Ăn mừng mốc thật: streak 4/12/26 tuần, buổi thứ 10/50/100, số tuần đạt cộng dồn. |
| ☐ | 1.7 | Buổi đi bộ | MVP | Chưa thiết kế | Ghi một buổi đi bộ 20–30 phút thay cho buổi tạ ở ngày vùng đỏ hoặc ngày cardio. |

### Luồng 2: Nhóm (tổ)

| Duyệt | Mã | Màn | Ưu tiên | Trạng thái | Mục đích |
|---|---|---|---|---|---|
| ☐ | 2.1 | Nhóm (bảng tổ) | MVP | Đã thiết kế (v2) | Một màn cho cả tổ: tuần này ai giữ lời hứa đến đâu, thử thách chung, bảng tin. |
| ☐ | 2.1a | Cho vía (khoảnh khắc) | MVP | Chưa thiết kế | Phản hồi một chạm khi cổ vũ bài của bạn, và phía người nhận thấy mình được cho vía. |
| ☐ | 2.2 | Chi tiết bài đăng | v1.1 | Chưa thiết kế | Xem đầy đủ một bài trong bảng tin: buổi tập, kỷ lục, ai đã cho vía. |
| ☐ | 2.3 | Thử thách tuần của tổ | MVP | Chưa thiết kế | Chi tiết mục tiêu chung tuần này và ai đã góp bao nhiêu buổi. |
| ☐ | 2.3a | Tổ làm được rồi (ăn mừng) | MVP | Chưa thiết kế | Ăn mừng khi cả tổ đủ buổi: phòng tập đổi khác và cả tổ cùng nhận thưởng. |
| ☐ | 2.4 | Streak của tổ | v1.1 | Chưa thiết kế | Lịch sử các tuần cả tổ cùng giữ lời hứa. |
| ☐ | 2.5 | Thành viên | MVP | Chưa thiết kế | Danh sách người trong tổ và vía của họ. |
| ☐ | 2.5a | Hồ sơ bạn tập | v1.1 | Chưa thiết kế | Xem vía của một người bạn: đồ đang mặc, streak, huy hiệu. |
| ☐ | 2.6 | Mời vào tổ | MVP | Chưa thiết kế | Lấy mã tổ để gửi cho bạn. |
| ☐ | 2.7 | Cài đặt tổ | MVP | Chưa thiết kế | Đổi tên tổ, rời tổ, và (về sau) đặt tên, màu cho áo đội. |
| ☐ | 2.8 | Phòng tập của tổ | MVP | Chưa thiết kế | Lấy hồ sơ phòng tập bạn đã nhập, để khỏi nhập lại dụng cụ và bước tạ. |
| ☐ | 2.9 | Chưa có tổ | MVP | Chưa thiết kế | Tab Nhóm khi người dùng đang tập một mình: mời lập hoặc vào tổ. |
| ☐ | 2.10 | Mảnh ký ức (mùa truyện "Ai để quên?") | Về sau | Chưa thiết kế | Mỗi mốc của tổ mở một mảnh chuyện về ba người chủ cũ. |
| ☐ | 2.11 | Chọc bạn và thi 1-1 | Về sau | Chưa thiết kế | Nhắc bạn chưa tập và thi đấu 7 ngày theo % mục tiêu riêng. |

### Luồng 3: Tủ đồ

| Duyệt | Mã | Màn | Ưu tiên | Trạng thái | Mục đích |
|---|---|---|---|---|---|
| ☐ | 3.1 | Tủ đồ | MVP | Đã thiết kế (v2) | Xem vía đang mặc gì, các món đã có, món đang gom và món chưa mở. |
| ☐ | 3.2 | Chi tiết món | MVP | Chưa thiết kế | Xem kỹ một món: chuyện của nó, cách mở, bản màu. |
| ☐ | 3.3 | Mặc thử | MVP | Chưa thiết kế | Thay đồ toàn màn hình theo từng ô trang bị. |
| ☐ | 3.3a | Bộ phối sẵn | v1.1 | Chưa thiết kế | Lưu tối đa 3 bộ phối để đổi nhanh. |
| ☐ | 3.4 | Bộ sưu tập và các bộ đồ | v1.1 | Chưa thiết kế | Thấy tiến độ sưu tập và các bộ theo chủ đề; đủ bộ thì có dáng ăn mừng riêng. |
| ☐ | 3.5 | Đồ theo mùa | Về sau | Chưa thiết kế | Món theo dịp (Tết, hè, Trung thu) mở trong 4 tuần và năm nào cũng quay lại. |

### Luồng 4: Tiến độ

| Duyệt | Mã | Màn | Ưu tiên | Trạng thái | Mục đích |
|---|---|---|---|---|---|
| ☐ | 4.1 | Tiến độ (tổng quan) | MVP | Chưa thiết kế | Một màn thấy mình đã đều đến đâu: streak, số tuần đạt, kỷ lục gần đây. |
| ☐ | 4.2 | Lịch sử buổi tập | MVP | Chưa thiết kế | Danh sách các buổi đã tập, mới nhất ở trên. |
| ☐ | 4.3 | Chi tiết một buổi | MVP | Chưa thiết kế | Xem lại một buổi: từng bài, từng set. |
| ☐ | 4.4 | Chi tiết bài tập | MVP | Chưa thiết kế | Theo dõi tiến bộ của một bài: biểu đồ, kỷ lục, các lần gần đây. |
| ☐ | 4.5 | Cân nặng | MVP | Chưa thiết kế | Ghi và xem cân nặng theo thời gian, riêng tư. |
| ☐ | 4.6 | Tổng kết tuần | v1.1 | Chưa thiết kế | Đầu tuần mới, tóm tắt tuần vừa qua và lời hứa tuần này. |
| ☐ | 4.7 | Huy hiệu | MVP | Chưa thiết kế | Các mốc thật đã chạm và sắp chạm. |
| ☐ | 4.8 | Số set theo nhóm cơ | v1.1 | Chưa thiết kế | Xem tuần này mỗi nhóm cơ được tập bao nhiêu set so với khoảng nên có. |
| ☐ | 4.9 | Thư viện bài tập | v1.1 | Chưa thiết kế | Duyệt 90 bài theo kiểu chuyển động và dụng cụ, ngoài giờ tập. |

### Luồng 5: Tôi và cài đặt

| Duyệt | Mã | Màn | Ưu tiên | Trạng thái | Mục đích |
|---|---|---|---|---|---|
| ☐ | 5.1 | Tôi | MVP | Chưa thiết kế | Trang cá nhân: vía của mình, tiến độ, và mọi cài đặt. |
| ☐ | 5.2 | Sửa hồ sơ | MVP | Chưa thiết kế | Đổi tên, mục tiêu, trình độ, cân nặng. |
| ☐ | 5.3 | Sửa lịch tập | MVP | Chưa thiết kế | Đổi số buổi mỗi tuần (lời hứa N) và thời lượng mặc định. |
| ☐ | 5.4 | Phòng tập của tôi | MVP | Chưa thiết kế | Quản lý nhiều hồ sơ phòng tập. |
| ☐ | 5.4a | Chi tiết phòng tập | MVP | Chưa thiết kế | Sửa dụng cụ, bước tạ của một phòng và chia sẻ phòng cho tổ. |
| ☐ | 5.5 | Vía của tôi | MVP | Chưa thiết kế | Đổi tên và màu vía; xem giống vía của mình. |
| ☐ | 5.6 | Sao lưu | MVP | Chưa thiết kế | Xuất toàn bộ dữ liệu ra file và nhập lại, vì iOS có thể tự xoá dữ liệu của web app. |
| ☐ | 5.6a | Khôi phục từ file | MVP | Chưa thiết kế | Nhập file sao lưu trên máy mới hoặc sau khi mất dữ liệu. |
| ☐ | 5.7 | Sức khoẻ và vùng đau | MVP | Chưa thiết kế | Xem và sửa câu trả lời sàng lọc, vùng hay đau, và nhật ký đau. |
| ☐ | 5.8 | Cài đặt | MVP | Chưa thiết kế | Các tuỳ chọn chung của app. |
| ☐ | 5.9 | Thông báo | v1.1 | Chưa thiết kế | Chọn loại thông báo muốn nhận. |
| ☐ | 5.10 | Giới thiệu và lưu ý y tế | MVP | Chưa thiết kế | Thông tin app, lưu ý y tế, nguồn của các luật tập. |
| ☐ | 5.11 | Bài ưa dùng và bài đã loại | v1.1 | Chưa thiết kế | Xem và gỡ các lựa chọn "từ giờ về sau" khi đổi bài. |

### Luồng 6: Hệ thống và tình huống đặc biệt

| Duyệt | Mã | Màn | Ưu tiên | Trạng thái | Mục đích |
|---|---|---|---|---|---|
| ☐ | 6.1 | Dừng ngay: dấu hiệu nguy hiểm | MVP | Chưa thiết kế | Màn dừng buổi khi có dấu hiệu nguy hiểm toàn thân, có nút gọi cấp cứu. |
| ☐ | 6.2 | Nên đi khám | MVP | Chưa thiết kế | Khuyên đi khám khi đau kéo dài quá 14 ngày hoặc có dấu hiệu cảnh báo theo vùng. |
| ☐ | 6.3 | Xin tuần nghỉ có phép | MVP | Chưa thiết kế | Khai báo ốm, chấn thương hoặc đi xa để tuần đó không tính, mọi bộ đếm đứng yên. |
| ☐ | 6.4 | Quay lại sau khi vắng | MVP | Chưa thiết kế | Đón người dùng quay lại sau tuần hụt hoặc vài tuần vắng, và nói rõ buổi hôm nay nhẹ hơn thế nào. |
| ☐ | 6.5 | Gợi ý tuần giảm tải | v1.1 | Chưa thiết kế | Khi nhiều bài cùng chững hoặc mệt kéo dài, đề nghị một tuần tập nhẹ. |
| ☐ | 6.6 | Bắt đầu lại sau nghỉ dài | v1.1 | Chưa thiết kế | Sau hơn 8 tuần vắng, bắt đầu lại từ 50–60% mức tạ cũ với 2–4 tuần làm quen. |
| ☐ | 6.7 | Gợi ý giảm số buổi | v1.1 | Chưa thiết kế | Khi hơn nửa số buổi trong 3 tuần là vàng hoặc đỏ, gợi ý xem lại giấc ngủ, ăn uống hoặc bớt số buổi. |
| ☐ | 6.8 | Hết giai đoạn học kỹ thuật | MVP | Chưa thiết kế | Báo khi người mới xong 4 tuần đầu và cách tập sẽ đổi thế nào. |
| ☐ | 6.9 | Mất mạng và đồng bộ | MVP | Chưa thiết kế | Cho thấy app vẫn chạy khi mất mạng và phần nào của tổ đang chờ gửi. |
| ☐ | 6.10 | Máy mất dữ liệu | MVP | Chưa thiết kế | Khi app mở ra thấy máy trống dù từng có dữ liệu, dẫn người dùng khôi phục. |
| ☐ | 6.11 | Nhắc sao lưu | MVP | Chưa thiết kế | Nhắc định kỳ xuất file sao lưu, đặt ở chỗ không cản việc tập. |
| ☐ | 6.12 | Buổi dở dang | MVP | Chưa thiết kế | Khôi phục buổi đang tập khi app bị tắt hoặc điện thoại khoá lâu. |
| ☐ | 6.13 | Bộ trạng thái trống | MVP | Chưa thiết kế | Mẫu chung cho mọi màn chưa có dữ liệu. |
| ☐ | 6.14 | Bộ thông báo lỗi | MVP | Chưa thiết kế | Mẫu chung cho lỗi: không lưu được, không vào được tổ, file hỏng, hết chỗ lưu. |
| ☐ | 6.15 | Có bản mới | MVP | Chưa thiết kế | Báo khi app có bản cập nhật và cho tải lại. |
| ☐ | 6.16 | Màn chờ mở app | MVP | Chưa thiết kế | Hình đầu tiên khi mở app từ màn hình chính, trong lúc tải. |

## 3. Chi tiết từng màn

### Luồng 0: Lần đầu mở app và onboarding

#### 0.1 · Chào mừng: hộp đồ bỏ quên

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Giới thiệu thế giới Ba Vía trong một màn và mời bắt đầu.
- **Nội dung:** Hình hộp các-tông "ĐỒ BỎ QUÊN" ở quầy lễ tân, ba vía ló ra; Một câu chuyện nền: "Bỏ tập là để quên vía ở phòng gym. Trong hộp có ba con vía đang chờ chủ."; Nút chính "Mở hộp"; Dòng phụ "Đã dùng app rồi? Khôi phục dữ liệu".
- **Trạng thái và biến thể:** Mở lần đầu trong trình duyệt; Mở từ màn hình chính (đã cài); Máy trống nhưng từng có dữ liệu: dẫn sang 5.6a.
- **Vào từ:** Mở app lần đầu. **Đi tới:** → 0.2 nếu chưa cài lên màn hình chính, nếu đã cài thì → 0.3; hoặc → 5.6a.
- **Khoảnh khắc của vía:** Ba vía chồng lên nhau đẩy nắp hộp (luật "ba vía mới bằng một người").
- **Hình cần làm:** Có sẵn: k3_box, k3_trio. Cần mới: hộp các-tông có chữ "ĐỒ BỎ QUÊN" ở góc rộng hơn (1 render).
- **Phụ thuộc:** không.
- **Ghi chú:** Không hỏi gì ở màn này. Không nhắc chuyện bỏ tập theo giọng trách móc.

#### 0.2 · Cài lên màn hình chính

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Đưa app ra màn hình chính trước khi nhập dữ liệu, để dữ liệu nằm đúng chỗ và ít bị iOS xoá.
- **Nội dung:** iPhone: 3 bước có hình (nút Chia sẻ → "Thêm vào MH chính" → mở lại từ biểu tượng); Android: nút "Cài app" gọi hộp thoại cài của trình duyệt; Một câu lý do: "Cài rồi thì hộp của chủ mới không bị dọn mất."; Nút phụ "Để sau".
- **Trạng thái và biến thể:** iPhone Safari; iPhone mở bằng trình duyệt khác hoặc trong Zalo/Messenger: hướng dẫn mở bằng Safari; Android Chrome; Đã cài: bỏ qua màn này; Máy tính: chỉ hiện gợi ý mở trên điện thoại.
- **Vào từ:** 0.1, hoặc mục "Cài app" trong 5.1. **Đi tới:** → 0.3.
- **Khoảnh khắc của vía:** Vía chỉ tay lên nút Chia sẻ.
- **Hình cần làm:** Cần mới: 1 dáng "chỉ tay" cho ba vía chung (diễn bằng cả người vì bàn tay không có ngón); 3 hình minh hoạ bước cài iOS vẽ bằng giao diện, không cần Blender.
- **Phụ thuộc:** 0.1.
- **Ghi chú:** Thứ tự màn này phụ thuộc phép thử trên iPhone thật ở giai đoạn B0: nếu dữ liệu của bản mở trong Safari không đi theo bản cài, màn này phải đứng trước mọi bước nhập liệu trên iPhone, và lời mời vào tổ phải là mã gõ tay chứ không phải đường link.

#### 0.3 · Nhận vía: chọn giống

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Người dùng chọn một trong ba giống vía làm bạn tập và làm avatar.
- **Nội dung:** Ba vía đứng cạnh nhau, vuốt ngang để xem từng con; Tên giống + một dòng tính cách + một câu thoại mẫu; Nút "Nhận vía này".
- **Trạng thái và biến thể:** Đang xem Khăn / Bình / Găng; Đã chọn.
- **Vào từ:** 0.2. **Đi tới:** → 0.4.
- **Khoảnh khắc của vía:** Con đang xem bước lên một bước và diễn món nhận diện: Khăn hất mép khăn, Bình bật nắp, Găng giơ ngón cái.
- **Hình cần làm:** Có sẵn: hero.png, expr_*.png của cả ba (blender/out/via/khan|binh|gang). Cần mới: 1 dáng "bước lên chào" cho mỗi giống (3 render).
- **Phụ thuộc:** 0.1.
- **Ghi chú:** Không gắn giống vía với giới tính hay trình độ. Bốn người cùng chọn một giống vẫn khác nhau nhờ tên và màu (0.4).

#### 0.4 · Đặt tên và chọn màu vía

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Biến con vía thành của riêng người dùng: tên và màu.
- **Nội dung:** Vía đứng giữa, đổi màu ngay khi chọn; Ô nhập tên (gợi ý sẵn: Khăn Mây, Bình Chanh, Găng Lì…); Bảng màu; Nút "Xong".
- **Trạng thái và biến thể:** Chưa nhập tên (dùng tên gợi ý); Tên quá dài; Tên trùng với bạn trong tổ: vẫn cho, chỉ báo nhẹ.
- **Vào từ:** 0.3. **Đi tới:** → 0.5.
- **Khoảnh khắc của vía:** Vía xoay một vòng ngắm màu mới; đặt tên xong thì reo "Chủ đặt tên rồi!".
- **Hình cần làm:** Có sẵn: colors.png và stand_<màu>.png (3 màu mỗi giống). Cần mới: đủ bảng màu đã chốt cho cả ba giống (xem quyết định D2); nếu chọn bảng 6 màu thì thêm 9 render đứng.
- **Phụ thuộc:** 0.3.
- **Ghi chú:** Số màu và cách màu đi vào máy (render sẵn hay tô trên máy) là quyết định D2; màn này không thiết kế được trước khi chốt.

#### 0.5 · Hồ sơ: về người dùng

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Lấy thông tin cơ bản để tính mức tạ khởi điểm và bước tăng tạ.
- **Nội dung:** Tên gọi hiển thị trong tổ; Giới tính (nam / nữ / không muốn nói); Tuổi; Cân nặng (kg), ghi rõ "chỉ mình chủ thấy".
- **Trạng thái và biến thể:** Bỏ trống cân nặng (cho phép); Giá trị ngoài khoảng hợp lý: hỏi lại.
- **Vào từ:** 0.4. **Đi tới:** → 0.6.
- **Khoảnh khắc của vía:** Vía cầm sổ ghi, nói một câu: "Khăn hỏi mấy câu thôi, chủ nhé.".
- **Hình cần làm:** Cần mới: 1 dáng "cầm sổ hỏi" dùng chung cho 0.5–0.9 (3 render, mỗi giống 1).
- **Phụ thuộc:** 0.4.
- **Ghi chú:** Giới tính chỉ dùng cho mức tạ khởi điểm và bước tăng tạ thân trên (1,25 kg). Giáo án nam nữ như nhau.

#### 0.6 · Mục tiêu và trình độ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Chọn mục tiêu tập và trình độ để chọn khung tuần, khoảng rep và thuật toán tăng tạ.
- **Nội dung:** Mục tiêu: giảm mỡ / tăng cơ / sức mạnh / khoẻ tổng quát (thẻ chọn, mỗi thẻ một dòng giải thích); Trình độ: mới (dưới 6 tháng tập đều) / đã tập (6 tháng trở lên).
- **Trạng thái và biến thể:** Chưa chọn; Đã chọn.
- **Vào từ:** 0.5. **Đi tới:** → 0.7.
- **Khoảnh khắc của vía:** Vía gật đầu sau mỗi lựa chọn, không bình phẩm mục tiêu.
- **Hình cần làm:** Dùng lại dáng "cầm sổ hỏi". 4 biểu tượng nỉ nhỏ cho 4 mục tiêu (4 render dùng chung).
- **Phụ thuộc:** 0.5.
- **Ghi chú:** Người mới ở mọi mục tiêu đều qua 4 tuần học kỹ thuật (8–12 rep). Nói điều này bằng một dòng để họ không ngạc nhiên.

#### 0.7 · Lời hứa tuần và thời lượng

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Người dùng tự chọn số buổi mỗi tuần (N) và số phút mặc định mỗi buổi.
- **Nội dung:** Số buổi/tuần: 2–6; Thời lượng mặc định: 30 / 45 / 60 / 75 / 90 phút; Xem trước khung tuần: "3 buổi → Toàn thân A / B / A"; Một dòng: "Đây là lời hứa của chủ. Streak và mảnh đồ tính theo số này.".
- **Trạng thái và biến thể:** Người mới chọn 5–6 buổi: gợi ý 3–4 buổi tạ, ngày còn lại đi bộ; Chọn 2 buổi: báo trước là tiến bộ chậm hơn một chút, vẫn ổn.
- **Vào từ:** 0.6. **Đi tới:** → 0.8.
- **Khoảnh khắc của vía:** Vía giơ số buổi bằng cách đặt từng viên nỉ lên bàn.
- **Hình cần làm:** Cần mới: bộ viên nỉ đánh dấu buổi (đã có ở tab Nhóm: k3_icon_balls), 1 render hàng 2–6 viên.
- **Phụ thuộc:** 0.6.
- **Ghi chú:** N quyết định streak tuần, nhịp mảnh đồ (1/N món mỗi buổi) và thứ hạng trong tổ. Đổi N sau này không lách được trần 1 món/tuần.

#### 0.8 · Sàng lọc sức khoẻ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Hỏi các câu sàng lọc trước khi tập (kiểu PAR-Q+) để biết ai cần hỏi bác sĩ trước.
- **Nội dung:** Nhóm câu a: bệnh tim, huyết áp, tiểu đường, thận đã được chẩn đoán; Nhóm câu b: đau ngực, khó thở bất thường, chóng mặt hoặc ngất khi gắng sức; Nhóm câu c: đang mang thai hoặc sau sinh; Nhóm câu d: chấn thương hoặc phẫu thuật gần đây; Mỗi câu trả lời Có / Không.
- **Trạng thái và biến thể:** Tất cả "Không": đi tiếp; Có ít nhất một "Có" ở a–c: → 0.8a; Chỉ "Có" ở d: → 0.9 và mở sẵn vùng liên quan.
- **Vào từ:** 0.7. **Đi tới:** → 0.9 hoặc → 0.8a.
- **Khoảnh khắc của vía:** Vía nghiêm túc, không đùa ở màn này.
- **Hình cần làm:** Cần mới: 1 biểu cảm "nghiêm túc, chăm chú" cho mỗi giống (3 render), dùng lại ở 0.8a, 6.1, 6.2.
- **Phụ thuộc:** 0.7.
- **Ghi chú:** Nguyên văn 7 câu PAR-Q+ chưa trích được từ nguồn chính thức; phải lấy bản chính thức và dịch trước khi thiết kế chữ.

#### 0.8a · Khuyên hỏi bác sĩ trước

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Báo cho người có câu trả lời "Có" rằng nên hỏi bác sĩ, và cho họ dùng app ở chế độ nhẹ trong lúc chờ.
- **Nội dung:** Lời khuyên gặp bác sĩ hoặc chuyên gia vận động trước khi tập nặng; Nút "Tôi đã hỏi bác sĩ, được tập"; Nút "Tập ở chế độ nhẹ" (chỉ cường độ nhẹ đến vừa).
- **Trạng thái và biến thể:** Chế độ nhẹ đang bật; Đã xác nhận được tập: tắt chế độ nhẹ.
- **Vào từ:** 0.8. **Đi tới:** → 0.9.
- **Khoảnh khắc của vía:** Vía nghiêm túc, đứng yên bên cạnh; không doạ.
- **Hình cần làm:** Dùng lại biểu cảm "nghiêm túc" của 0.8.
- **Phụ thuộc:** 0.8.
- **Ghi chú:** Chế độ nhẹ là một cờ trong hồ sơ, sửa được ở 5.7. Không chặn hẳn người dùng.

#### 0.9 · Vùng hay đau hoặc chấn thương cũ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Khai vùng cơ thể cần tránh để app chọn bài an toàn hơn.
- **Nội dung:** Hình cơ thể đơn giản với 4 vùng: gối, lưng dưới, vai, cổ tay; Bật tắt từng vùng; Nút "Không đau chỗ nào".
- **Trạng thái và biến thể:** Không chọn vùng nào; Chọn nhiều vùng: báo một số ô bài có thể bị bỏ.
- **Vào từ:** 0.8 hoặc 0.8a. **Đi tới:** → 0.10.
- **Khoảnh khắc của vía:** Vía sờ vào đúng chỗ trên người mình khi người dùng chạm một vùng.
- **Hình cần làm:** Cần mới: hình cơ thể trung tính kiểu "bóng trong gương" đứng thẳng với 4 vùng sáng lên (1 render nền + 4 lớp vùng).
- **Phụ thuộc:** 0.8.
- **Ghi chú:** Dùng chính hình bóng trong gương để không phải vẽ một cơ thể nam hay nữ.

#### 0.10 · Phòng tập đầu tiên

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Tạo hồ sơ phòng tập đầu tiên: tên và điểm xuất phát.
- **Nội dung:** Tên phòng (ví dụ "Gym Thành Công"); Chọn mẫu: phòng gym đầy đủ / phòng chung cư / tập ở nhà; Hoặc "Lấy phòng bạn trong tổ đã nhập" (nếu đã vào tổ).
- **Trạng thái và biến thể:** Bắt đầu từ mẫu; Nhận hồ sơ phòng từ tổ; Chưa có tổ: ẩn lựa chọn nhận từ tổ.
- **Vào từ:** 0.9. **Đi tới:** → 0.11.
- **Khoảnh khắc của vía:** Vía đứng trước cửa kính phòng tập.
- **Hình cần làm:** Cần mới: 3 biểu tượng nỉ cho 3 mẫu phòng (cửa phòng gym, toà chung cư, tấm thảm ở nhà).
- **Phụ thuộc:** 0.9.
- **Ghi chú:** Mỗi người giữ nhiều phòng (5.4). Nếu chốt D7 theo hướng chia sẻ qua tổ, nên cân nhắc đưa bước vào tổ (0.14) lên trước màn này.

#### 0.11 · Checklist dụng cụ của phòng

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Đánh dấu phòng này có những dụng cụ gì, để app chỉ ra bài tập làm được.
- **Nội dung:** Danh sách 22 loại dụng cụ theo nhóm: tạ tự do, giá và ghế, máy, cáp, xà; Mỗi dòng một ô tích, có hình nhỏ; Mẫu đã chọn ở 0.10 tích sẵn; Số bài tập làm được với lựa chọn hiện tại.
- **Trạng thái và biến thể:** Tích rất ít: báo ô chuyển động nào sẽ trống và gợi ý dây kháng lực; Đủ cả.
- **Vào từ:** 0.10, hoặc 5.4a. **Đi tới:** → 0.12.
- **Khoảnh khắc của vía:** Vía ôm thử từng món khi được tích (chỉ ở vài món chính).
- **Hình cần làm:** Cần mới: biểu tượng nỉ cho dụng cụ. Tối thiểu 8 nhóm (thanh đòn, tạ tay, ghế, giá squat, máy, cáp, xà, dây); đầy đủ là 22.
- **Phụ thuộc:** 0.10.
- **Ghi chú:** Danh sách dụng cụ lấy từ exercises.json (22 loại, không tính "none"). Danh sách "gym cỏ" Việt Nam là ước lượng, cần chỉnh theo phòng thật.

#### 0.12 · Bước tạ của phòng

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Khai thanh đòn nặng bao nhiêu, đĩa nhỏ nhất, tạ tay nhảy mấy kg, để gợi ý tăng tạ đúng với tạ thật.
- **Nội dung:** Thanh đòn: 10 / 15 / 20 kg; Đĩa nhỏ nhất: 1,25 / 2,5 / 5 kg; Tạ tay nhảy: 1 / 2 / 2,5 kg; Máy: mỗi nấc bao nhiêu kg (hỏi sau cũng được); Nút "Chưa biết, hỏi sau".
- **Trạng thái và biến thể:** Bỏ qua: app hỏi lần đầu dùng từng dụng cụ (1.4c); Đã điền.
- **Vào từ:** 0.11, hoặc 5.4a. **Đi tới:** → 0.13.
- **Khoảnh khắc của vía:** Vía nhấc thử cái đĩa nhỏ nhất.
- **Hình cần làm:** Cần mới: 3 hình nỉ (thanh đòn, đĩa tạ, tạ tay) dùng lại ở 1.4c.
- **Phụ thuộc:** 0.11.
- **Ghi chú:** Bước tạ là cài đặt của từng phòng, không ghi cứng. Số liệu phòng tập Việt Nam chưa có nguồn nên bắt buộc hỏi.

#### 0.13 · Dụng cụ cá nhân

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Khai dụng cụ người dùng luôn mang theo, coi là có sẵn ở mọi phòng.
- **Nội dung:** Dây kháng lực (khuyên dùng), găng, đai… dạng ô tích; Một dòng lý do: có dây thì ô bài nào cũng có bài thay thế.
- **Trạng thái và biến thể:** Không có gì; Có dây kháng lực.
- **Vào từ:** 0.12. **Đi tới:** → 0.14.
- **Khoảnh khắc của vía:** Vía kéo thử sợi dây.
- **Hình cần làm:** Cần mới: 1 hình nỉ dây kháng lực.
- **Phụ thuộc:** 0.12.
- **Ghi chú:** Có thể gộp vào cuối 0.11 khi thiết kế nếu thấy luồng quá dài.

#### 0.14 · Tổ: tạo hoặc vào

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Đưa người dùng vào nhóm bạn ngay từ đầu, hoặc cho bỏ qua.
- **Nội dung:** Hai lựa chọn lớn: "Lập tổ mới" và "Vào tổ của bạn"; Nút phụ "Tập một mình trước".
- **Trạng thái và biến thể:** Không có mạng: chỉ cho bỏ qua, nhắc vào tổ sau; QUYẾT ĐỊNH MỞ D1: nếu chọn đăng nhập Google thì màn này có thêm bước đăng nhập.
- **Vào từ:** 0.13. **Đi tới:** → 0.14a, 0.14b, hoặc → 0.15.
- **Khoảnh khắc của vía:** Ba vía đứng cạnh hai cái hộp của nhà khác.
- **Hình cần làm:** Có sẵn: k3_trio. Cần mới: 1 cảnh "nhiều hộp cạnh nhau" (1 render).
- **Phụ thuộc:** 0.13.
- **Ghi chú:** QUYẾT ĐỊNH MỞ (D1): mã nhóm không tài khoản hay đăng nhập Google. Ảnh hưởng cả việc lấy lại danh tính sau khi máy mất dữ liệu.

#### 0.14a · Lập tổ mới

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Tạo một tổ và nhận mã để mời bạn.
- **Nội dung:** Tên tổ; Mã tổ sinh tự động, nút sao chép; Một dòng: gửi mã này cho bạn qua bất kỳ đâu.
- **Trạng thái và biến thể:** Đang tạo; Tạo xong; Lỗi mạng: thử lại.
- **Vào từ:** 0.14, hoặc 2.9. **Đi tới:** → 0.15 (lần đầu) hoặc → 2.1.
- **Khoảnh khắc của vía:** Vía dán nhãn tên tổ lên hộp.
- **Hình cần làm:** Cần mới: 1 render hộp có nhãn trống để chèn tên tổ bằng chữ.
- **Phụ thuộc:** 0.14.
- **Ghi chú:** Cần mạng. Mã là thứ duy nhất bảo vệ tổ nếu không có đăng nhập.

#### 0.14b · Vào tổ bằng mã

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Nhập mã tổ bạn gửi để vào nhóm.
- **Nội dung:** Ô nhập mã; Xem trước: tên tổ, số thành viên, vía của họ; Nút "Vào tổ".
- **Trạng thái và biến thể:** Mã sai; Tổ đã đầy (10 người); Không có mạng; Vào thành công.
- **Vào từ:** 0.14, hoặc 2.9. **Đi tới:** → 0.15 (lần đầu) hoặc → 2.1.
- **Khoảnh khắc của vía:** Các vía trong tổ vẫy chào vía mới.
- **Hình cần làm:** Dùng avatar đã có của các thành viên; không cần render riêng.
- **Phụ thuộc:** 0.14.
- **Ghi chú:** Mã gõ tay, không dựa vào đường link (xem ghi chú 0.2).

#### 0.15 · Bộ khởi đầu và tuần đầu tiên

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Kết thúc onboarding: tặng bộ khởi đầu và cho thấy tuần đầu trông thế nào.
- **Nội dung:** Vía nhận món khởi đầu; Tóm tắt: khung tuần, phòng tập, lời hứa N buổi; Món đầu tiên đang chờ trong hộp + thanh mảnh 0/N; Nút "Vào Hôm nay".
- **Trạng thái và biến thể:** Có tổ / chưa có tổ; Đang ở chế độ nhẹ (0.8a).
- **Vào từ:** 0.14 / 0.14a / 0.14b. **Đi tới:** → 1.1.
- **Khoảnh khắc của vía:** Vía mặc món đầu tiên và khoe: khoảnh khắc mặc đồ đầu tiên.
- **Hình cần làm:** Có sẵn: băng cổ tay (cotay), tất (tat), băng đô (bando) trong wardrobe.py. Cần mới: 1 dáng "khoe đồ" cho mỗi giống (3 render) và danh sách bộ khởi đầu theo thế giới Ba Vía (quyết định D3).
- **Phụ thuộc:** 0.4, 0.7, 0.10.
- **Ghi chú:** Tài liệu 06 ghi bộ khởi đầu 4 món kiểu quần áo người; phải viết lại cho thân hình vía và hộp đồ bỏ quên (D3).

#### 0.16 · Bật thông báo

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Xin quyền gửi thông báo, chỉ sau khi người dùng bấm nút.
- **Nội dung:** Giải thích app sẽ báo gì: bạn cho vía, tổ đủ buổi; Nút "Bật" và "Không cần".
- **Trạng thái và biến thể:** iOS: chỉ xin được khi app đã cài lên màn hình chính; Bị từ chối: không hỏi lại, để mục trong 5.9.
- **Vào từ:** 5.9, hoặc lời mời sau lần đầu được cho vía. **Đi tới:** → quay lại màn trước.
- **Khoảnh khắc của vía:** Vía ghé tai nghe ngóng.
- **Hình cần làm:** Cần mới: 1 dáng "ghé tai" (3 render) nếu làm.
- **Phụ thuộc:** 0.2.
- **Ghi chú:** Push cần máy chủ gửi và không có trong MVP. Không bao giờ có thông báo nhắc món đồ đang dở hay nhắc ngày nghỉ.

### Luồng 1: Vòng lặp hằng ngày

#### 1.1 · Hôm nay

- **Ưu tiên / trạng thái:** MVP · Đã thiết kế (v2)
- **Mục đích:** Màn chính: hôm nay tập gì, tuần này đến đâu, một nút vào tập.
- **Nội dung:** Ngày, streak "6 tuần liền"; Vía chào một câu; Thẻ buổi hôm nay: tên buổi, phòng tập, số bài, số phút; Tiến độ tuần 2/3 buổi với các ngày đã tập; Nút "Vào tập"; Thanh tab: Hôm nay / Nhóm / Tủ đồ / Tôi.
- **Trạng thái và biến thể:** Ngày tập theo lịch; Ngày nghỉ: vía nghỉ, không có lời nhắc, vẫn cho "Tập thêm hôm nay"; Đã tập xong hôm nay; Tuần đã đủ N buổi: nói rõ tập thêm không có mảnh; Có buổi dở dang: nút "Tập tiếp" (6.12); Vừa quay lại sau khi vắng: lời chào "Hú vía!" (6.4); Tuần nghỉ có phép đang bật (6.3); Đến hạn sao lưu: một dải nhắc nhỏ (6.11); Mất mạng: không đổi gì, chỉ tab Nhóm báo; Tuần đầu tiên, chưa có streak.
- **Vào từ:** Mở app; tab Hôm nay. **Đi tới:** → 1.2 (Vào tập); → các tab khác.
- **Khoảnh khắc của vía:** Check-in của thế giới: vía đẩy nắp hộp chui ra "Chủ đến!".
- **Hình cần làm:** Có sẵn (Khăn màu mint): kh_box, kh_ready, kh_sleepy, k3_icon_*. Cần mới: cùng các dáng đó cho Bình và Găng và cho các màu khác (theo D2); dáng ngày nghỉ (ngủ trong hộp đắp tất) đã có kh_sleepy.
- **Phụ thuộc:** không.
- **Ghi chú:** Thiếu ở bản v2: ngày nghỉ, đã tập xong, tuần đủ rồi, buổi dở dang, quay lại sau khi vắng, dải nhắc sao lưu. Bản v2 chỉ vẽ Khăn Mây; chưa có Bình và Găng.

#### 1.2 · Check-in

- **Ưu tiên / trạng thái:** MVP · Đã thiết kế (v2)
- **Mục đích:** Hỏi nhanh tình trạng hôm nay để chỉnh buổi tập; ngày bình thường chỉ cần một chạm.
- **Nội dung:** Thẻ tóm tắt "Như mọi khi": phòng, sức, giấc ngủ, thời gian, dụng cụ; Nút "Như mọi khi" và "Hôm nay khác"; 5 câu: tập ở đâu, thấy thế nào (rất tệ / mệt / bình thường / sung), ngủ (hơn 6 tiếng / 6 tiếng trở xuống), bao nhiêu phút (30–90), phòng thiếu gì; Kết quả: vùng + một dòng app sẽ chỉnh gì; Nút "Vào tập", "Trả lời lại".
- **Trạng thái và biến thể:** Một chạm "Như mọi khi"; Trả lời từng câu; Vùng xanh; Vùng vàng: bớt set, giữ tạ; Vùng đỏ → 1.2b; Ốm có sốt: khuyên nghỉ → 6.3; Hôm qua có báo đau: hỏi thêm "chỗ đau hôm qua giờ thế nào?"; Có vùng đau đang theo dõi → mở sẵn 1.2a; Lần đầu, chưa có "mọi khi"; Phòng mới: → 5.4a để thêm phòng.
- **Vào từ:** 1.1. **Đi tới:** → 1.3.
- **Khoảnh khắc của vía:** Vía hỏi nhỏ nhẹ; vùng là một chấm nhỏ trên chip, không đổi màu cả màn.
- **Hình cần làm:** Có sẵn: kh_ready, kh_expr_tired, k3_shy. Cần mới: cùng dáng cho Bình, Găng.
- **Phụ thuộc:** 1.1.
- **Ghi chú:** Thiếu ở bản v2: câu hỏi đau (1.2a), kết quả vùng vàng và đỏ, đường "ốm có sốt", câu hỏi đau của sáng hôm sau, check-in lần đầu. "Thiếu dụng cụ hôm nay" chỉ lưu cho buổi này, không sửa hồ sơ phòng.

#### 1.2a · Hôm nay đau chỗ nào? (tấm trượt)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Khai vùng đang đau hôm nay và mức đau, để app tránh hoặc giảm bài chạm vùng đó.
- **Nội dung:** 4 vùng: gối, lưng dưới, vai, cổ tay; Mức đau 0–10 bằng thanh trượt có 3 mốc chữ; Kiểu đau: âm ỉ / nhói, buốt, tê, lan (kiểu sau dẫn sang 6.2).
- **Trạng thái và biến thể:** Không đau; Đau 3–4: giảm tải, giảm biên độ; Đau từ 5: đổi bài hoặc bỏ ô; Đau nhói, tê, lan → 6.2.
- **Vào từ:** 1.2 (mục "thêm"), hoặc tự mở khi hôm qua có báo đau. **Đi tới:** → 1.2.
- **Khoảnh khắc của vía:** Vía lo lắng nhẹ, tay đặt lên đúng vùng.
- **Hình cần làm:** Dùng lại hình cơ thể của 0.9. Cần mới: biểu cảm "lo" cho mỗi giống (3 render).
- **Phụ thuộc:** 1.2, 0.9.
- **Ghi chú:** Đau cơ sau tập (ê mỏi hai bên, 1–3 ngày) không phải là "đau" ở đây; cần một dòng phân biệt.

#### 1.2b · Hôm nay vùng đỏ: chọn cách tập

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Khi rất mệt, cho chọn buổi rút gọn, đi bộ, hoặc nghỉ, và nói rõ cả ba đều ổn.
- **Nội dung:** Lựa chọn 1: buổi rút gọn (3 bài chính, nửa số set, tạ −10%); Lựa chọn 2: đi bộ 20–30 phút (→ 1.7); Lựa chọn 3: nghỉ hôm nay; Một dòng: buổi nào ghi được cũng tính là đến tập.
- **Trạng thái và biến thể:** Vùng đỏ do "rất tệ"; Vùng đỏ do thiếu ngủ hai đêm liền.
- **Vào từ:** 1.2. **Đi tới:** → 1.3, → 1.7, hoặc → 1.1.
- **Khoảnh khắc của vía:** Vía mệt theo người dùng, ngồi xuống cạnh hộp; không khuyên cố.
- **Hình cần làm:** Có sẵn: kh_expr_tired, k3_tired. Cần mới: Bình, Găng mệt ở cùng khung hình.
- **Phụ thuộc:** 1.2.
- **Ghi chú:** QUYẾT ĐỊNH MỞ (D9): buổi đi bộ vùng đỏ có được tính là buổi đạt và cho mảnh không. Tài liệu 06 đề xuất có.

#### 1.3 · Buổi tập hôm nay (xem trước)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Cho xem cả buổi trước khi tập: bài nào, mấy set, vì sao khác mọi khi.
- **Nội dung:** Tên buổi, phòng, tổng thời gian ước tính; Danh sách bài: tên, set × rep, mức tạ gợi ý, dụng cụ; Dòng giải thích điều chỉnh: "Hôm nay vùng vàng nên bớt 1 set mỗi bài"; Trên mỗi bài: Đổi bài, Để sau; Nút "Bắt đầu".
- **Trạng thái và biến thể:** Buổi đủ; Buổi đã cắt theo thời gian; Có ô mượn kiểu chuyển động khác vì thiếu dụng cụ: báo rõ; Có ô bị bỏ vì vùng đau; Nhóm cơ rơi dưới sàn volume tuần: báo nhẹ; Tuần deload (6.5); Giai đoạn học kỹ thuật (4 tuần đầu); Mở giữa buổi làm danh sách bài: bài đã xong, đang tập, để sau.
- **Vào từ:** 1.2. **Đi tới:** → 1.4.
- **Khoảnh khắc của vía:** Vía xếp dụng cụ cho bài đầu tiên.
- **Hình cần làm:** Cần mới: 15 ảnh nhỏ "bóng trong gương" cho 15 kiểu chuyển động làm hình đại diện bài (lấy khung giữa của mỗi chuỗi ở 1.4a).
- **Phụ thuộc:** 1.2.
- **Ghi chú:** Bản v2 có thẻ kết quả vùng với nút "Vào tập" nhưng chưa có danh sách bài. Đây là màn ưu tiên số một của đợt thiết kế tiếp theo.

#### 1.4 · Đang tập

- **Ưu tiên / trạng thái:** MVP · Đã thiết kế (v2)
- **Mục đích:** Ghi từng set bằng một chạm, có bóng trong gương làm mẫu và đồng hồ nghỉ.
- **Nội dung:** Bóng trong gương làm mẫu động tác, vía bắt chước bên ngoài; Tên bài, chấm set 1-2-3; Tạ (kg) và số lần đã điền sẵn mục tiêu, có số lần trước và khoảng đích 8–12; Nút + / − theo bước tạ của phòng; Nút "Xong set"; Để sau, Đổi bài; Nghỉ giữa set: đồng hồ tự chạy, −15s / +15s, bỏ qua, xem trước set tới; Tấm trượt Đổi bài: 3 bài cùng kiểu, "Chỉ hôm nay" / "Từ giờ về sau".
- **Trạng thái và biến thể:** Set khởi động (không tính volume); Set chính; Đang nghỉ; Set cuối của bài; Bài tính bằng giây (plank); Bài không tạ; Bài một bên (trái/phải); Bài cuối của buổi: nút thành "Xong buổi"; Bài đang "để sau" quay lại; Màn hình luôn sáng (Wake Lock); Thanh đòn: hiện "mỗi bên: 5 + 2,5" (v1.1).
- **Vào từ:** 1.3. **Đi tới:** → 1.5 khi hết bài; → 1.4a–1.4g.
- **Khoảnh khắc của vía:** Vía bắt chước bóng trong gương: "Chủ xuống, Khăn xuống!".
- **Hình cần làm:** Có sẵn: mir_0.0–1.0 (squat, 5 khung), carry_0–2, kh_copy. Cần mới: chuỗi khung bóng trong gương cho các kiểu chuyển động còn lại (xem 1.4a và quyết định D4); dáng bắt chước cho Bình, Găng.
- **Phụ thuộc:** 1.3.
- **Ghi chú:** Thiếu ở bản v2: set khởi động, bài tính giây, bài một bên, sửa số bằng bàn phím (1.4d), báo đau (1.4b), nút mở hướng dẫn đầy đủ (1.4a), kỷ lục tại chỗ (1.4f), thoát giữa buổi (1.4g). Bản v2 gồm cả trạng thái nghỉ và tấm Đổi bài.

#### 1.4a · Hướng dẫn động tác

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Xem kỹ một bài: bóng trong gương chạy chậm, các ý chính và lỗi hay gặp.
- **Nội dung:** Bóng trong gương lặp lại động tác, có nhãn pha "XUỐNG · hít vào"; 3–4 ý chính (cues_vi); 2–3 lỗi hay gặp (mistakes_vi); Mức tạ nên bắt đầu và ghi chú; Dụng cụ cần; Ghi chú ghim của chính mình ("ghế nấc 4").
- **Trạng thái và biến thể:** Bài có hướng dẫn đã đối chiếu nguồn; Bài chưa đối chiếu: vẫn hiện, nhưng phải qua lượt kiểm nội dung trước khi phát hành; Mở từ thư viện (4.9), không trong buổi.
- **Vào từ:** 1.4, 1.3, 4.4, 4.9. **Đi tới:** → quay lại màn trước.
- **Khoảnh khắc của vía:** Cảm xúc ngoài gương, kỹ thuật trong gương: vía đứng ngoài bắt chước vụng về.
- **Hình cần làm:** Cần mới: chuỗi khung bóng trong gương. Tối thiểu 15 kiểu chuyển động × 4–5 khung = 60–75 khung; đầy đủ 90 bài × 4–5 khung = 360–450 khung. Đã có 2 chuỗi (squat, carry).
- **Phụ thuộc:** 1.4.
- **Ghi chú:** Hướng dẫn chữ mới đối chiếu nguồn được 18/90 bài. Q4 cũ (người que SVG) đã bỏ; thay bằng bóng trong gương dựng Blender.

#### 1.4b · Báo đau giữa buổi (tấm trượt)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Báo đau ngay trong lúc tập và nhận cách xử lý ngay.
- **Nội dung:** Đau ở đâu, mức 0–10, kiểu đau; Kết quả theo luật: 3–4 giảm tải 10–20% và chậm lại; từ 5 đổi sang bài không đau cùng ô, không có thì bỏ ô; Dòng luôn có: "Đau ngực, chóng mặt, nghe rắc?" → 6.1.
- **Trạng thái và biến thể:** Đau nhẹ 0–2: ghi lại, tập tiếp; Đau 3–4; Đau từ 5 hoặc tăng dần qua từng set; Dấu hiệu nguy hiểm → 6.1 hoặc 6.2.
- **Vào từ:** 1.4 (nút "Thấy đau"). **Đi tới:** → 1.4 với bài đã chỉnh; → 6.1; → 6.2.
- **Khoảnh khắc của vía:** Vía dừng bắt chước, quay sang nhìn người dùng, lo.
- **Hình cần làm:** Dùng lại hình cơ thể 0.9 và biểu cảm "lo" của 1.2a.
- **Phụ thuộc:** 1.4, 1.2a.
- **Ghi chú:** Buổi hụt rep vì đau không tính là thất bại khi tính tăng tạ. Bảng đau nên được vợ người dùng (học vật lý trị liệu) rà lại.

#### 1.4c · Hỏi bước tạ lần đầu dùng dụng cụ (tấm trượt)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Lần đầu gặp một dụng cụ chưa khai bước tạ, hỏi đúng một câu rồi nhớ cho phòng đó.
- **Nội dung:** Câu hỏi theo dụng cụ: "Tạ tay ở đây nhảy mấy kg?", "Thanh đòn nặng bao nhiêu?", "Máy này mỗi nấc mấy kg?"; 3–4 lựa chọn nhanh + ô nhập.
- **Trạng thái và biến thể:** Tạ tay; Thanh đòn và đĩa; Máy; Bỏ qua: dùng giá trị mặc định, hỏi lại lần sau.
- **Vào từ:** 1.4, khi 0.12 còn bỏ trống. **Đi tới:** → 1.4.
- **Khoảnh khắc của vía:** Vía ôm cái đĩa tạ, nghiêng đầu hỏi.
- **Hình cần làm:** Dùng lại 3 hình nỉ của 0.12.
- **Phụ thuộc:** 1.4, 0.12.
- **Ghi chú:** Bước nhảy lớn hơn 10% mức đang tập thì app nới khoảng rep thay vì ép tăng tạ; nên giải thích bằng một dòng.

#### 1.4d · Sửa số và ghi chú bài (tấm trượt)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Nhập tạ hoặc số lần bằng bàn phím số khi lệch nhiều, và ghim ghi chú cho bài.
- **Nội dung:** Bàn phím số cho kg và số lần; Sửa lại set đã ghi; Thêm hoặc bớt một set; Ghi chú ghim theo bài, hiện mỗi lần gặp bài này.
- **Trạng thái và biến thể:** Sửa set hiện tại; Sửa set cũ trong buổi; Thêm ghi chú.
- **Vào từ:** 1.4 (chạm vào con số hoặc set đã xong). **Đi tới:** → 1.4.
- **Khoảnh khắc của vía:** Không có vía (màn công cụ).
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 1.4.
- **Ghi chú:** Ghi xuống máy ngay sau mỗi set để không mất dữ liệu khi app bị tắt.

#### 1.4e · Kỷ lục mới tại chỗ (thông báo nổi)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Báo ngay khi set vừa xong là kỷ lục cá nhân của bài đó.
- **Nội dung:** Dải nổi 2 giây: "Kỷ lục mới: 12,5 kg × 12"; Không chặn nút tiếp theo.
- **Trạng thái và biến thể:** Kỷ lục về tạ; Kỷ lục về số lần ở cùng mức tạ; Kỷ lục đầu tiên trong đời dùng app (mở món đồ hiếm, báo ở 1.6).
- **Vào từ:** 1.4, tự hiện. **Đi tới:** → tự tắt.
- **Khoảnh khắc của vía:** Vía nhảy lên một nhịp; Găng giơ ngón cái.
- **Hình cần làm:** Có sẵn: kh_cheer. Cần mới: dáng reo cho Bình, Găng (2 render).
- **Phụ thuộc:** 1.4.
- **Ghi chú:** Kỷ lục chỉ có lời khen. Chỉ kỷ lục đầu tiên mới gắn với một món đồ.

#### 1.4f · App tự chỉnh giữa buổi (thông báo)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Nói rõ khi app hạ tạ hoặc hạ vùng vì set đầu hụt nhiều, hoặc nâng lại khi làm dư.
- **Nội dung:** Một dòng lý do: "Set đầu hụt 2 lần so với lần trước, Khăn hạ 5% cho các set sau."; Nút "Giữ nguyên tạ" để từ chối.
- **Trạng thái và biến thể:** Hạ tạ 5–10% và hạ một bậc vùng; Nâng từ vàng lên xanh vì làm dư; Người dùng từ chối.
- **Vào từ:** 1.4, sau set đầu của bài chính. **Đi tới:** → 1.4.
- **Khoảnh khắc của vía:** Vía nói nhỏ, không báo động.
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 1.4.
- **Ghi chú:** Số rep thực tế đáng tin hơn cảm giác lúc check-in.

#### 1.4g · Dừng buổi giữa chừng (xác nhận)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Cho thoát buổi mà không mất những gì đã ghi.
- **Nội dung:** "Dừng ở đây?" kèm số set đã ghi; Nút "Xong buổi tại đây" (vẫn tính nếu đã đủ 1 bài); Nút "Tạm dừng, lát tập tiếp"; Nút "Tập tiếp".
- **Trạng thái và biến thể:** Đã đủ ít nhất 1 bài: tính là buổi đạt; Chưa đủ 1 bài: lưu nháp, không tính.
- **Vào từ:** 1.4 (nút đóng). **Đi tới:** → 1.5, → 1.1, hoặc → 1.4.
- **Khoảnh khắc của vía:** Vía không tỏ ra thất vọng.
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 1.4.
- **Ghi chú:** Buổi ngắn lúc mệt vẫn tính: đây là ngưỡng thấp có chủ ý.

#### 1.5 · Buổi này thế nào?

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Một câu hỏi sau buổi, bỏ qua được, làm dữ liệu cho lần tăng tạ sau.
- **Nội dung:** Ba lựa chọn: nhẹ / vừa / quá sức; Nút "Bỏ qua".
- **Trạng thái và biến thể:** Trả lời; Bỏ qua.
- **Vào từ:** 1.4 (hết bài) hoặc 1.4g. **Đi tới:** → 1.6.
- **Khoảnh khắc của vía:** Vía lau mồ hôi, nhìn người dùng và chờ.
- **Hình cần làm:** Cần mới: 1 dáng "thở, lau mồ hôi" cho mỗi giống (3 render); Khăn có thể dùng chính góc khăn ướt.
- **Phụ thuộc:** 1.4.
- **Ghi chú:** Có thể gộp vào đầu 1.6 khi thiết kế để bớt một bước.

#### 1.6 · Xong buổi

- **Ưu tiên / trạng thái:** MVP · Đã thiết kế (v2)
- **Mục đích:** Khen buổi tập trước, rồi mới tới mảnh đồ; mời gửi vào tổ.
- **Nội dung:** Lời khen gắn với buổi vừa tập: "Đủ tuần rồi, chủ ơi!"; Kỷ lục mới nếu có; Streak "6 tuần liền" và các ngày đã tập; Mảnh: món đang gom, "+1 mảnh", thanh 2/3; Một dòng chuyện của món đồ; Nút "Gửi vào nhóm"; Tấm xem trước bài đăng vào tổ, nút "Đăng".
- **Trạng thái và biến thể:** Buổi thường: +1 mảnh; Buổi làm đủ tuần; Buổi vượt N: không có mảnh, nói rõ "tuần này đủ rồi"; Có kỷ lục / không có; Mảnh cuối: thanh đầy → 1.6a; Chạm mốc → 1.6c; Buổi vùng đỏ hoặc đi bộ; Chưa có tổ: ẩn nút gửi, mời lập tổ; Mất mạng: bài đăng xếp hàng chờ gửi; Tủ đồ đang tắt: chỉ có lời khen và streak; Buổi thứ hai trong ngày: không có mảnh.
- **Vào từ:** 1.5. **Đi tới:** → 1.6a, → 1.6c, hoặc → 1.1; đăng xong → 2.1.
- **Khoảnh khắc của vía:** Vía nhảy ăn mừng; Khăn hất mũ trùm thành áo choàng (lần duy nhất bỏ mũ trùm). Vía sáng dần theo lời hứa tuần.
- **Hình cần làm:** Có sẵn: kh_win, kh_win2, headband (băng đô). Cần mới: dáng ăn mừng của Bình (nắp bật) và Găng (mào nắm đấm); hình "mảnh" của từng món.
- **Phụ thuộc:** 1.5.
- **Ghi chú:** Thiếu ở bản v2: buổi vượt N, buổi không có kỷ lục, buổi vùng đỏ, chưa có tổ, mất mạng, tủ đồ tắt. Chia sẻ ra Zalo/Messenger đã bỏ: "gửi" nghĩa là đăng vào bảng tin của tổ.

#### 1.6a · Nhận món: thanh đầy

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Khoảnh khắc mở khoá khi mảnh cuối làm đầy thanh: món đồ về tủ và vía mặc ngay.
- **Nội dung:** Các mảnh ghép lại thành món; Vía mặc món lên người; Tên món + mẩu chuyện về người để quên; Nút "Mặc luôn" và "Cất vào tủ"; Nút phụ "Khoe với tổ".
- **Trạng thái và biến thể:** Món thường của lộ trình tuần; Món hiếm do chạm mốc; Món cả tổ cùng nhận (từ 2.3a); Bản màu của món đã có.
- **Vào từ:** 1.6 (thanh đầy), 1.6c, 2.3a. **Đi tới:** → 1.6b (nếu là món lộ trình) hoặc → 1.1.
- **Khoảnh khắc của vía:** Vía lôi món đồ từ hộp ra, mặc vào, xoay một vòng khoe.
- **Hình cần làm:** Cần mới cho MỖI món: mesh nỉ 3D gắn rig của cả ba giống + render mặc trên người (không dùng lớp 2D dán đè). Dáng "khoe đồ" dùng chung với 0.15.
- **Phụ thuộc:** 1.6, 3.1.
- **Ghi chú:** Đây là khoảnh khắc cần hoạt ảnh riêng, đáng đầu tư nhất sau màn Đang tập.

#### 1.6b · Chọn món kế tiếp (1 trong 3)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Sau khi nhận món, chọn món sẽ gom ở chu kỳ tới trong 3 món đang bày.
- **Nội dung:** 3 món chưa có nằm trong hộp, mỗi món một dòng chuyện; Xem thử trên vía trước khi chọn; Nút "Gom món này".
- **Trạng thái và biến thể:** Còn từ 3 món thường trở lên; Còn ít hơn 3 món; Hết món thường: bày bản màu; Đang trong mùa: có thêm món mùa (về sau).
- **Vào từ:** 1.6a; lần đầu sau 0.15. **Đi tới:** → 1.1.
- **Khoảnh khắc của vía:** Vía bới hộp, giơ từng món lên.
- **Hình cần làm:** Dùng render món đứng riêng (kiểu item_bando_only) cho mỗi món: 1 render/món.
- **Phụ thuộc:** 1.6a.
- **Ghi chú:** Không may rủi: người dùng luôn thấy trước món sắp nhận. Phần bất ngờ duy nhất là 3 món nào được bày.

#### 1.6c · Chạm mốc

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Ăn mừng mốc thật: streak 4/12/26 tuần, buổi thứ 10/50/100, số tuần đạt cộng dồn.
- **Nội dung:** Tên mốc và con số lớn; Huy hiệu; Nếu mốc có đồ: dẫn sang 1.6a; Nút "Gửi vào nhóm".
- **Trạng thái và biến thể:** Mốc streak; Mốc số buổi (chỉ huy hiệu, không có đồ); Mốc tuần đạt cộng dồn; Kỷ lục đầu tiên.
- **Vào từ:** 1.6. **Đi tới:** → 1.6a hoặc → 1.1.
- **Khoảnh khắc của vía:** Ba vía chồng lên nhau ăn mừng; mốc lớn thì vía sáng hết cỡ.
- **Hình cần làm:** Có sẵn: k3_win, k3_trio. Cần mới: bộ huy hiệu nỉ, khoảng 8–10 cái (1 render mỗi cái).
- **Phụ thuộc:** 1.6.
- **Ghi chú:** Con số mốc chưa thống nhất: tài liệu 06 ghi 4/12/26 tuần, bản v2 ghi "Đủ 8 tuần liền" (quyết định D3).

#### 1.7 · Buổi đi bộ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Ghi một buổi đi bộ 20–30 phút thay cho buổi tạ ở ngày vùng đỏ hoặc ngày cardio.
- **Nội dung:** Đồng hồ đếm phút hoặc nhập số phút đã đi; Nút "Xong".
- **Trạng thái và biến thể:** Đang đếm; Nhập tay sau khi đi; Dưới 20 phút: vẫn ghi, có tính buổi đạt hay không theo D9.
- **Vào từ:** 1.2b; hoặc 1.1 ngày nghỉ. **Đi tới:** → 1.6.
- **Khoảnh khắc của vía:** Vía đi bộ bên cạnh, khăn vắt vai.
- **Hình cần làm:** Cần mới: 1 dáng "đi bộ" cho mỗi giống (3 render).
- **Phụ thuộc:** 1.2b.
- **Ghi chú:** Không đếm bước, không dùng GPS.

### Luồng 2: Nhóm (tổ)

#### 2.1 · Nhóm (bảng tổ)

- **Ưu tiên / trạng thái:** MVP · Đã thiết kế (v2)
- **Mục đích:** Một màn cho cả tổ: tuần này ai giữ lời hứa đến đâu, thử thách chung, bảng tin.
- **Nội dung:** Tên tổ, streak tổ "Cả tổ đủ 3 tuần liền"; Thử thách tuần: "Góp vía mở quạt trần 13/17 buổi"; Bảng tuần xếp theo % lời hứa của mỗi người, kèm avatar vía đang mặc đồ; Bảng tin: bài đăng buổi tập, kỷ lục, món mới; Nút "Cho vía" trên mỗi bài.
- **Trạng thái và biến thể:** Có dữ liệu mới; Mất mạng: hiện dữ liệu lần cuối + giờ cập nhật; Tổ chỉ có 1 người: mời bạn (2.6); Đầu tuần, chưa ai tập; Bảng tin trống; Thành viên đang nghỉ có phép: hiện nhãn "nghỉ có phép", không tính vào xếp hạng; Chưa có tổ → 2.9; Đồng hạng.
- **Vào từ:** Tab Nhóm; sau khi đăng ở 1.6. **Đi tới:** → 2.2, 2.3, 2.4, 2.5, 2.6, 2.7.
- **Khoảnh khắc của vía:** Cho vía: giọt vía nỉ vàng bay từ hộp nhà này sang hộp nhà kia. Vía của ai sáng nhất là người giữ lời hứa đều nhất.
- **Hình cần làm:** Có sẵn: k3_icon_drop (giọt vía), av_* (avatar có đồ), avatar.png mỗi giống. Cần mới: avatar của mọi tổ hợp giống × màu × đồ đang mặc (theo D2).
- **Phụ thuộc:** 0.14.
- **Ghi chú:** Thiếu ở bản v2: mất mạng, tổ một người, bảng tin trống, nhãn nghỉ có phép, bài đăng "món mới". Xếp hạng theo độ đều, không bao giờ so mức tạ. Cân nặng không bao giờ hiện.

#### 2.1a · Cho vía (khoảnh khắc)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Phản hồi một chạm khi cổ vũ bài của bạn, và phía người nhận thấy mình được cho vía.
- **Nội dung:** Giọt vía bay từ nút sang avatar của bạn, số vía tăng; Phía người nhận: lần mở app sau, vía ôm các giọt vía được cho.
- **Trạng thái và biến thể:** Cho vía; Rút lại; Mất mạng: xếp hàng gửi sau; Người nhận xem lại ai đã cho vía.
- **Vào từ:** 2.1, 2.2. **Đi tới:** → ở lại màn đang xem.
- **Khoảnh khắc của vía:** "Cho vía" là kudos của thế giới này. Vía người nhận phồng lên một nhịp.
- **Hình cần làm:** Có sẵn: k3_icon_drop. Cần mới: 1 dáng "ôm vía được cho" cho mỗi giống (3 render).
- **Phụ thuộc:** 2.1.
- **Ghi chú:** Không có bình luận chữ ở MVP (quyết định D10).

#### 2.2 · Chi tiết bài đăng

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Xem đầy đủ một bài trong bảng tin: buổi tập, kỷ lục, ai đã cho vía.
- **Nội dung:** Avatar + tên người đăng và tên vía; Tóm tắt buổi: tên buổi, số phút, kỷ lục; Câu thoại của vía người đăng; Danh sách người đã cho vía.
- **Trạng thái và biến thể:** Bài buổi tập; Bài kỷ lục; Bài món mới; Bài mốc của tổ; Bài của chính mình: có nút xoá.
- **Vào từ:** 2.1. **Đi tới:** → 2.1, → 2.5a.
- **Khoảnh khắc của vía:** Vía của người đăng ở dáng ăn mừng, mặc đúng đồ lúc đăng.
- **Hình cần làm:** Dùng avatar và dáng ăn mừng đã có.
- **Phụ thuộc:** 2.1.
- **Ghi chú:** Ở MVP, thẻ bài đăng trong 2.1 đã đủ thông tin; màn chi tiết để sau.

#### 2.3 · Thử thách tuần của tổ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Chi tiết mục tiêu chung tuần này và ai đã góp bao nhiêu buổi.
- **Nội dung:** Tên thử thách theo thế giới: "Góp vía mở quạt trần"; Thanh 13/17 buổi; Mỗi thành viên góp mấy buổi (không xếp hạng); Phần thưởng cả tổ cùng nhận; Còn mấy ngày trong tuần (ghi bằng thứ, không đồng hồ đếm ngược).
- **Trạng thái và biến thể:** Đang chạy; Đã đủ → 2.3a; Hết tuần chưa đủ: "hoãn sang tuần sau", không có chữ thua; Mất mạng.
- **Vào từ:** 2.1. **Đi tới:** → 2.3a, → 2.1.
- **Khoảnh khắc của vía:** "Ba vía bằng một người": cả tổ đủ vía thì làm được một việc lớn trong phòng tập.
- **Hình cần làm:** Cần mới: mỗi thử thách một cảnh phòng tập trước và sau (quạt trần, tấm rèm, cửa kho). MVP: 3 thử thách × 2 cảnh = 6 render.
- **Phụ thuộc:** 2.1.
- **Ghi chú:** QUYẾT ĐỊNH MỞ (D11): mục tiêu thử thách do app tự đặt (theo tổng lời hứa) hay do tổ tự đặt.

#### 2.3a · Tổ làm được rồi (ăn mừng)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Ăn mừng khi cả tổ đủ buổi: phòng tập đổi khác và cả tổ cùng nhận thưởng.
- **Nội dung:** Cảnh việc lớn xảy ra: quạt trần quay; Danh sách cả tổ, ai cũng được ghi tên; Món thưởng cả tổ cùng nhận, kể cả người góp ít.
- **Trạng thái và biến thể:** Xem lần đầu; Xem lại từ bảng tin; Mở khi thử thách xong lúc mình vắng.
- **Vào từ:** 2.3, hoặc tự hiện khi mở app sau khi tổ đủ buổi. **Đi tới:** → 1.6a (nếu có món) hoặc → 2.1.
- **Khoảnh khắc của vía:** Tất cả vía của tổ chồng lên nhau với tới công tắc.
- **Hình cần làm:** Cần mới: 1 cảnh "nhiều vía chồng nhau" có thể ghép từ avatar từng người; cảnh "sau" của thử thách (đã tính ở 2.3).
- **Phụ thuộc:** 2.3.
- **Ghi chú:** Không có món "người đứng đầu bảng". Thưởng nhóm phát cho cả nhóm.

#### 2.4 · Streak của tổ

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Lịch sử các tuần cả tổ cùng giữ lời hứa.
- **Nội dung:** Số tuần liền hiện tại và kỷ lục; Lưới các tuần: tuần nào đủ, tuần nào ai nghỉ có phép; Luật một dòng: tuần đạt khi mọi người (hoặc từ 80% tổ) đạt mục tiêu riêng.
- **Trạng thái và biến thể:** Đang có streak; Vừa đứt: hiện kỷ lục, không có biểu tượng vỡ; Tổ mới.
- **Vào từ:** 2.1. **Đi tới:** → 2.1.
- **Khoảnh khắc của vía:** Vía các nhà sáng đèn cùng lúc.
- **Hình cần làm:** Không cần hình mới ngoài avatar.
- **Phụ thuộc:** 2.1.
- **Ghi chú:** Ở MVP con số streak tổ nằm ngay trên 2.1. Ngưỡng 100% hay 80% là quyết định D12.

#### 2.5 · Thành viên

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Danh sách người trong tổ và vía của họ.
- **Nội dung:** Mỗi dòng: avatar vía đang mặc đồ, tên người dùng, tên vía, lời hứa N buổi/tuần, streak; Nút "Mời bạn".
- **Trạng thái và biến thể:** Tổ đầy (10 người); Có người mới vào; Có người đang nghỉ có phép.
- **Vào từ:** 2.1. **Đi tới:** → 2.5a, → 2.6.
- **Khoảnh khắc của vía:** Các vía đứng thành hàng, mỗi con một màu.
- **Hình cần làm:** Dùng avatar có sẵn theo D2.
- **Phụ thuộc:** 2.1.
- **Ghi chú:** Chỉ hiện số buổi, streak, kỷ lục mới. Không hiện cân nặng, số đo, vùng đau.

#### 2.5a · Hồ sơ bạn tập

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Xem vía của một người bạn: đồ đang mặc, streak, huy hiệu.
- **Nội dung:** Vía toàn thân mặc đồ; Streak, số tuần đạt, huy hiệu; Kỷ lục gần đây nếu bạn đó cho hiện; Nút "Cho vía".
- **Trạng thái và biến thể:** Bạn bật / tắt chia sẻ kỷ lục.
- **Vào từ:** 2.5, 2.2. **Đi tới:** → 2.5.
- **Khoảnh khắc của vía:** Vía của bạn vẫy chào.
- **Hình cần làm:** Cần render toàn thân có đồ cho vía của người khác: cùng bộ ảnh với 3.3.
- **Phụ thuộc:** 2.5.

#### 2.6 · Mời vào tổ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Lấy mã tổ để gửi cho bạn.
- **Nội dung:** Mã tổ cỡ lớn; Nút "Sao chép mã"; Hướng dẫn 2 dòng cho người được mời: cài app → nhập mã.
- **Trạng thái và biến thể:** Tổ còn chỗ; Tổ đầy; Mất mạng: vẫn xem được mã đã lưu.
- **Vào từ:** 2.1, 2.5, 5.1. **Đi tới:** → màn trước.
- **Khoảnh khắc của vía:** Vía giơ tấm bìa có mã.
- **Hình cần làm:** Cần mới: 1 render vía giơ tấm bìa trống (chèn mã bằng chữ), 3 render.
- **Phụ thuộc:** 2.1.
- **Ghi chú:** Sao chép mã để người dùng tự dán vào đâu tuỳ họ; app không có nút chia sẻ ra mạng xã hội.

#### 2.7 · Cài đặt tổ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Đổi tên tổ, rời tổ, và (về sau) đặt tên, màu cho áo đội.
- **Nội dung:** Tên tổ; Rời tổ (có xác nhận); Đổi mã tổ (người lập tổ); Áo đội: tên và màu do tổ đặt (v1.1).
- **Trạng thái và biến thể:** Người lập tổ; Thành viên; Xác nhận rời tổ.
- **Vào từ:** 2.1. **Đi tới:** → 2.1 hoặc → 2.9.
- **Khoảnh khắc của vía:** Vía cầm bút dạ viết lại nhãn hộp.
- **Hình cần làm:** Không cần hình mới ở MVP.
- **Phụ thuộc:** 2.1.
- **Ghi chú:** Rời tổ không xoá nhật ký tập trên máy.

#### 2.8 · Phòng tập của tổ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Lấy hồ sơ phòng tập bạn đã nhập, để khỏi nhập lại dụng cụ và bước tạ.
- **Nội dung:** Danh sách phòng các thành viên đã chia sẻ: tên, người nhập, số dụng cụ; Nút "Lấy về máy"; Sau khi lấy: là bản riêng, sửa không ảnh hưởng bạn.
- **Trạng thái và biến thể:** Chưa ai chia sẻ phòng nào; Đã có phòng trùng tên trên máy; Mất mạng.
- **Vào từ:** 5.4, 0.10. **Đi tới:** → 5.4a.
- **Khoảnh khắc của vía:** Vía chuyền một tờ sơ đồ phòng cho vía khác.
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 2.1, 5.4.
- **Ghi chú:** QUYẾT ĐỊNH MỞ (D7): chia sẻ phòng qua tổ (Firebase) thay cho file/QR trong kế hoạch gốc, vì đã bỏ chia sẻ ra ngoài.

#### 2.9 · Chưa có tổ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Tab Nhóm khi người dùng đang tập một mình: mời lập hoặc vào tổ.
- **Nội dung:** Một câu: "Ba vía mới bằng một người. Rủ thêm bạn nhé."; Nút "Lập tổ mới" và "Vào tổ của bạn".
- **Trạng thái và biến thể:** Chưa từng có tổ; Vừa rời tổ; Mất mạng.
- **Vào từ:** Tab Nhóm. **Đi tới:** → 0.14a, → 0.14b.
- **Khoảnh khắc của vía:** Vía ngồi một mình trên nắp hộp, nhìn sang các hộp trống bên cạnh; không buồn.
- **Hình cần làm:** Cần mới: 1 dáng "ngồi trên nắp hộp" cho mỗi giống (3 render).
- **Phụ thuộc:** 0.14.

#### 2.10 · Mảnh ký ức (mùa truyện "Ai để quên?")

- **Ưu tiên / trạng thái:** Về sau · Chưa thiết kế
- **Mục đích:** Mỗi mốc của tổ mở một mảnh chuyện về ba người chủ cũ.
- **Nội dung:** Thẻ truyện: hình + 2–3 câu; Bộ sưu tập các mảnh đã mở.
- **Trạng thái và biến thể:** Mảnh mới; Xem lại; Chưa mở: bóng mờ.
- **Vào từ:** 2.1 khi tổ chạm mốc. **Đi tới:** → 2.1.
- **Khoảnh khắc của vía:** Tờ biên lai combo ba người; chiếc găng bên phải; ba bóng người ngoài cửa kính.
- **Hình cần làm:** Cần mới: 3 cảnh truyện cho mùa một, mỗi cảnh 1–2 render.
- **Phụ thuộc:** 2.3a.
- **Ghi chú:** Viết khéo, không giải thích nhiều. Vía không bao giờ nhắc chuyện người dùng vắng mặt.

#### 2.11 · Chọc bạn và thi 1-1

- **Ưu tiên / trạng thái:** Về sau · Chưa thiết kế
- **Mục đích:** Nhắc bạn chưa tập và thi đấu 7 ngày theo % mục tiêu riêng.
- **Nội dung:** Nút "Gọi vía" trên dòng thành viên; Thi 1-1 trong 7 ngày, điểm có trần mỗi ngày.
- **Trạng thái và biến thể:** Cần thông báo đẩy.
- **Vào từ:** 2.5. **Đi tới:** → 2.1.
- **Khoảnh khắc của vía:** Vía gõ lên nắp hộp nhà bạn.
- **Hình cần làm:** Chưa cần.
- **Phụ thuộc:** 0.16, 2.5.
- **Ghi chú:** Giai đoạn 2 trong kế hoạch gốc. Cần push và máy chủ gửi.

### Luồng 3: Tủ đồ

#### 3.1 · Tủ đồ

- **Ưu tiên / trạng thái:** MVP · Đã thiết kế (v2)
- **Mục đích:** Xem vía đang mặc gì, các món đã có, món đang gom và món chưa mở.
- **Nội dung:** Vía toàn thân mặc đồ thật, tên vía, "Đang mặc 2 món"; Nút "Mặc thử"; Món đã có (nhãn "Của chủ"): chạm để mặc hoặc cởi; Món đang gom với thanh mảnh 2/3; Món chưa có: bóng mờ + một câu điều kiện; "Một món, ba dáng người": cùng món trên Khăn, Bình, Găng.
- **Trạng thái và biến thể:** Mới có bộ khởi đầu; Có món vừa nhận (chấm mới); Món mùa chưa tới mùa: "Quay lại vào dịp Tết" (về sau); Hết món thường: bày bản màu; Tủ đồ đang tắt trong cài đặt: tab vẫn có, chỉ để mặc đồ đã có.
- **Vào từ:** Tab Tủ đồ. **Đi tới:** → 3.2, → 3.3.
- **Khoảnh khắc của vía:** Hộp đồ bỏ quên là tủ đồ: món nào quá ba mươi ngày không ai nhận thì thuộc về vía.
- **Hình cần làm:** Có sẵn: bando, cotay, tat (3 món đã dựng), binh_bando, gang_bando, item_bando_only, wear_test. Cần mới: mọi món còn lại của danh mục MVP, mỗi món cho cả ba giống (xem giai đoạn A3).
- **Phụ thuộc:** 0.15.
- **Ghi chú:** Thiếu ở bản v2: chia theo ô trang bị, bộ đồ, bản màu, chấm "mới". Điều kiện mở món trong bản v2 ("Đủ 8 tuần liền", "Cả tổ mở được quạt", "Mùa mưa mới có") chưa khớp tài liệu 06 (D3).

#### 3.2 · Chi tiết món

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Xem kỹ một món: chuyện của nó, cách mở, bản màu.
- **Nội dung:** Món xoay trên vía hoặc đứng riêng; Mẩu chuyện về người để quên; Bậc: thường / hiếm / huyền thoại và cách lấy; Bản màu đã có và chưa có; Nút "Mặc" / "Cởi".
- **Trạng thái và biến thể:** Đã có; Đang gom: thanh mảnh; Chưa có: điều kiện mở; Món cả tổ cùng nhận.
- **Vào từ:** 3.1, 1.6a. **Đi tới:** → 3.1, → 3.3.
- **Khoảnh khắc của vía:** Vía kể chuyện món đồ bằng một câu.
- **Hình cần làm:** Mỗi món: 1 render đứng riêng + render trên ba giống (đã tính ở 3.1).
- **Phụ thuộc:** 3.1.
- **Ghi chú:** Bậc đồ nói cách lấy, không phải xác suất. Không có món nào gắn với mức tạ, cân nặng hay ngoại hình.

#### 3.3 · Mặc thử

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Thay đồ toàn màn hình theo từng ô trang bị.
- **Nội dung:** Vía lớn ở giữa, đổi đồ ngay khi chạm; Các ô: đầu (ô riêng thay mũ), mặt, thân, chân, phụ kiện, nền; Nút "Mặc bộ này".
- **Trạng thái và biến thể:** Mặc thử món chưa có (chỉ xem); Hai phụ kiện khác điểm gắn; Mũ kín đầu: bản riêng cho từng giống.
- **Vào từ:** 3.1, 3.2. **Đi tới:** → 3.1.
- **Khoảnh khắc của vía:** Mỗi giống diễn món nhận diện với đồ mới: mép khăn vẫn kéo sụp được, nắp vẫn bật, mào ngón vẫn đeo được nhẫn.
- **Hình cần làm:** Đây là màn tốn hình nhất: vía × màu × tổ hợp đồ. Cách hình tới được máy là quyết định D2.
- **Phụ thuộc:** 3.1.
- **Ghi chú:** MVP có thể chỉ cần mặc/cởi ngay trong 3.1; màn riêng này cần khi số món vượt quá một màn.

#### 3.3a · Bộ phối sẵn

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Lưu tối đa 3 bộ phối để đổi nhanh.
- **Nội dung:** 3 ô lưu; Nút "Lưu bộ đang mặc"; Chạm để mặc lại.
- **Trạng thái và biến thể:** Chưa lưu bộ nào; Đủ 3 bộ: ghi đè.
- **Vào từ:** 3.3. **Đi tới:** → 3.3.
- **Khoảnh khắc của vía:** Vía treo bộ đồ lên móc.
- **Hình cần làm:** Ảnh thu nhỏ của bộ: dùng lại avatar.
- **Phụ thuộc:** 3.3.

#### 3.4 · Bộ sưu tập và các bộ đồ

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Thấy tiến độ sưu tập và các bộ theo chủ đề; đủ bộ thì có dáng ăn mừng riêng.
- **Nội dung:** Đã có X/Y món; Các bộ: món nào đã có, món nào còn thiếu; Dáng ăn mừng riêng của bộ đã đủ.
- **Trạng thái và biến thể:** Chưa đủ bộ nào; Vừa đủ một bộ: ăn mừng.
- **Vào từ:** 3.1. **Đi tới:** → 3.2.
- **Khoảnh khắc của vía:** Mặc đủ bộ thì vía có dáng ăn mừng riêng của bộ đó.
- **Hình cần làm:** Mỗi bộ: 1 dáng ăn mừng × 3 giống.
- **Phụ thuộc:** 3.1.
- **Ghi chú:** Cần danh mục Ba Vía chốt trước (D3).

#### 3.5 · Đồ theo mùa

- **Ưu tiên / trạng thái:** Về sau · Chưa thiết kế
- **Mục đích:** Món theo dịp (Tết, hè, Trung thu) mở trong 4 tuần và năm nào cũng quay lại.
- **Nội dung:** Món mùa trong danh sách 1 trong 3; Ghi "Quay lại vào dịp Tết" khi ngoài mùa.
- **Trạng thái và biến thể:** Trong mùa; Ngoài mùa; Nghỉ có phép trong mùa: giữ chỗ tới tuần quay lại.
- **Vào từ:** 1.6b, 3.1. **Đi tới:** → 3.2.
- **Khoảnh khắc của vía:** Hộp đồ bỏ quên có thêm đồ sau mỗi dịp lễ.
- **Hình cần làm:** Mỗi mùa 1–2 món × 3 giống.
- **Phụ thuộc:** 1.6b.
- **Ghi chú:** Không đồng hồ đếm ngược, không "chỉ còn 2 ngày".

### Luồng 4: Tiến độ

#### 4.1 · Tiến độ (tổng quan)

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Một màn thấy mình đã đều đến đâu: streak, số tuần đạt, kỷ lục gần đây.
- **Nội dung:** Streak hiện tại, kỷ lục streak, tổng số tuần đạt; Lịch các tuần gần đây; Kỷ lục mới nhất; Lối vào: lịch sử, bài tập, cân nặng, huy hiệu.
- **Trạng thái và biến thể:** Tuần đầu, chưa có gì; Vừa đứt streak: hiện kỷ lục và tổng tuần đạt, không có biểu tượng vỡ; Đang nghỉ có phép.
- **Vào từ:** 5.1 (mục Tiến độ). **Đi tới:** → 4.2, 4.4, 4.5, 4.7.
- **Khoảnh khắc của vía:** Vía sáng theo tuần này; chỉ đếm ngày người dùng đến, không đếm ngày vắng.
- **Hình cần làm:** Dùng dáng đứng có sẵn.
- **Phụ thuộc:** 1.6.
- **Ghi chú:** QUYẾT ĐỊNH MỞ (D5): Tiến độ nằm trong tab Tôi hay là tab thứ năm. Bản v2 có 4 tab và không có tab Tiến độ.

#### 4.2 · Lịch sử buổi tập

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Danh sách các buổi đã tập, mới nhất ở trên.
- **Nội dung:** Mỗi dòng: ngày, tên buổi, phòng, số phút, vùng, có kỷ lục không; Nhóm theo tuần, kèm đạt mấy/mấy buổi.
- **Trạng thái và biến thể:** Trống; Có buổi đi bộ; Có tuần nghỉ có phép.
- **Vào từ:** 4.1. **Đi tới:** → 4.3.
- **Khoảnh khắc của vía:** Không có vía (màn dữ liệu).
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 4.1.

#### 4.3 · Chi tiết một buổi

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Xem lại một buổi: từng bài, từng set.
- **Nội dung:** Tên buổi, ngày, phòng, thời lượng, vùng check-in; Từng bài: set, tạ, số lần, kỷ lục; Câu trả lời nhẹ/vừa/quá sức; Sửa hoặc xoá buổi.
- **Trạng thái và biến thể:** Buổi thường; Buổi rút gọn; Buổi có báo đau; Xác nhận xoá (xoá mềm).
- **Vào từ:** 4.2. **Đi tới:** → 4.4, → 4.2.
- **Khoảnh khắc của vía:** Không có vía.
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 4.2.
- **Ghi chú:** Sửa buổi cũ phải tính lại gợi ý tạ của các bài liên quan.

#### 4.4 · Chi tiết bài tập

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Theo dõi tiến bộ của một bài: biểu đồ, kỷ lục, các lần gần đây.
- **Nội dung:** Một biểu đồ đường: tạ tốt nhất theo thời gian; Kỷ lục: tạ nặng nhất, nhiều lần nhất, 1RM ước tính; Các lần tập gần đây; Lần tới app sẽ gợi ý gì và vì sao; Ghi chú ghim; Nút mở hướng dẫn (1.4a).
- **Trạng thái và biến thể:** Mới tập 1 lần: chưa có đường; Bài không tạ: biểu đồ theo số lần hoặc giây; Đang chững: nói app sẽ làm gì.
- **Vào từ:** 4.1, 4.3, 1.4a. **Đi tới:** → 1.4a.
- **Khoảnh khắc của vía:** Bóng trong gương nhỏ ở đầu màn làm hình đại diện bài.
- **Hình cần làm:** Dùng lại ảnh đại diện bài của 1.3.
- **Phụ thuộc:** 4.3.
- **Ghi chú:** Chỉ một biểu đồ. Không có điểm sức mạnh tổng hợp.

#### 4.5 · Cân nặng

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Ghi và xem cân nặng theo thời gian, riêng tư.
- **Nội dung:** Nút ghi cân hôm nay; Biểu đồ đường; Dòng "Chỉ mình chủ thấy".
- **Trạng thái và biến thể:** Chưa có số nào; Có ít hơn 2 điểm.
- **Vào từ:** 4.1, 5.2. **Đi tới:** → 4.1.
- **Khoảnh khắc của vía:** Không có vía bình phẩm cân nặng.
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 4.1.
- **Ghi chú:** Cân nặng không bao giờ lên tổ và không gắn với phần thưởng nào.

#### 4.6 · Tổng kết tuần

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Đầu tuần mới, tóm tắt tuần vừa qua và lời hứa tuần này.
- **Nội dung:** Tuần trước: đạt mấy/mấy buổi, kỷ lục, mảnh đã gom; Tổ: cả tổ đủ hay chưa; Tuần này: khung buổi, lời hứa N.
- **Trạng thái và biến thể:** Tuần đạt; Tuần hụt: không trách, chỉ nói phần đã gom vẫn còn đó; Tuần nghỉ có phép.
- **Vào từ:** 1.1 vào thứ Hai. **Đi tới:** → 1.1.
- **Khoảnh khắc của vía:** Vía lật trang sổ.
- **Hình cần làm:** Cần mới: 1 dáng "lật sổ" (3 render).
- **Phụ thuộc:** 4.1.

#### 4.7 · Huy hiệu

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Các mốc thật đã chạm và sắp chạm.
- **Nội dung:** Lưới huy hiệu: buổi thứ 10/50/100, kỷ lục đầu tiên, 4/12/26 tuần đạt; Huy hiệu chưa có: bóng mờ + điều kiện.
- **Trạng thái và biến thể:** Chưa có huy hiệu nào; Có huy hiệu mới.
- **Vào từ:** 4.1, 1.6c. **Đi tới:** → 4.1.
- **Khoảnh khắc của vía:** Huy hiệu là hình nỉ ghim lên nắp hộp.
- **Hình cần làm:** Bộ huy hiệu nỉ đã tính ở 1.6c.
- **Phụ thuộc:** 1.6c.
- **Ghi chú:** Ít huy hiệu, gắn với mốc thật. Mốc số buổi chỉ có huy hiệu, không có đồ.

#### 4.8 · Số set theo nhóm cơ

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Xem tuần này mỗi nhóm cơ được tập bao nhiêu set so với khoảng nên có.
- **Nội dung:** Thanh ngang cho từng nhóm cơ: sàn, mục tiêu, trần; Tuần này so với tuần trước.
- **Trạng thái và biến thể:** Nhóm cơ dưới sàn; Đủ.
- **Vào từ:** 4.1. **Đi tới:** → 4.1.
- **Khoảnh khắc của vía:** Không có vía.
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 4.1.
- **Ghi chú:** Bộ máy vẫn đếm volume từ MVP; chỉ màn hiển thị là để sau.

#### 4.9 · Thư viện bài tập

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Duyệt 90 bài theo kiểu chuyển động và dụng cụ, ngoài giờ tập.
- **Nội dung:** Lọc theo kiểu chuyển động (15 kiểu) và theo phòng tập; Mỗi bài: ảnh bóng trong gương, tên, dụng cụ.
- **Trạng thái và biến thể:** Lọc theo phòng đang chọn; Tìm theo tên.
- **Vào từ:** 5.1. **Đi tới:** → 1.4a, → 4.4.
- **Khoảnh khắc của vía:** Bóng trong gương cho từng bài.
- **Hình cần làm:** Cần ảnh đại diện cho cả 90 bài nếu không dùng chung theo kiểu chuyển động.
- **Phụ thuộc:** 1.4a.

### Luồng 5: Tôi và cài đặt

#### 5.1 · Tôi

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Trang cá nhân: vía của mình, tiến độ, và mọi cài đặt.
- **Nội dung:** Vía + tên người dùng + streak; Lối vào Tiến độ (4.1); Hồ sơ, Lịch tập, Phòng tập, Vía của tôi, Sức khoẻ; Sao lưu (kèm ngày sao lưu gần nhất); Cài đặt, Giới thiệu; "Cài app lên màn hình chính" nếu chưa cài.
- **Trạng thái và biến thể:** Chưa sao lưu lần nào: chấm nhắc; Chưa cài lên màn hình chính; Đang ở chế độ nhẹ.
- **Vào từ:** Tab Tôi. **Đi tới:** → 4.1, 5.2–5.10.
- **Khoảnh khắc của vía:** Biểu tượng tab là mặt Khăn (theo bản v2); nên đổi thành mặt vía của chính người dùng.
- **Hình cần làm:** Cần mới: mặt vía cỡ biểu tượng cho Bình và Găng (2 render), theo màu của D2.
- **Phụ thuộc:** 0.15.
- **Ghi chú:** Tab Tôi có trong thanh tab của bản v2 nhưng chưa có màn nào.

#### 5.2 · Sửa hồ sơ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Đổi tên, mục tiêu, trình độ, cân nặng.
- **Nội dung:** Các trường của 0.5 và 0.6; Đổi mục tiêu: nói rõ khoảng rep và thời gian nghỉ sẽ đổi thế nào.
- **Trạng thái và biến thể:** Đổi mục tiêu; Đổi trình độ: xác nhận, vì đổi cả khung tuần và thuật toán tăng tạ.
- **Vào từ:** 5.1. **Đi tới:** → 5.1.
- **Khoảnh khắc của vía:** Vía cầm sổ ghi lại.
- **Hình cần làm:** Dùng lại dáng "cầm sổ hỏi".
- **Phụ thuộc:** 5.1, 0.6.

#### 5.3 · Sửa lịch tập

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Đổi số buổi mỗi tuần (lời hứa N) và thời lượng mặc định.
- **Nội dung:** N và số phút; Khung tuần mới; Điều gì giữ nguyên: mảnh đã gom, streak, nhịp 1 món/tuần; Đổi có hiệu lực từ tuần sau.
- **Trạng thái và biến thể:** Tăng N; Giảm N: nói rõ không mất gì; Đổi giữa tuần.
- **Vào từ:** 5.1, 6.7. **Đi tới:** → 5.1.
- **Khoảnh khắc của vía:** Vía xếp lại các viên nỉ đánh dấu buổi.
- **Hình cần làm:** Dùng lại hình viên nỉ của 0.7.
- **Phụ thuộc:** 5.1, 0.7.
- **Ghi chú:** Tiến độ món đồ lưu theo phần của một món, nên đổi N không lách được trần.

#### 5.4 · Phòng tập của tôi

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Quản lý nhiều hồ sơ phòng tập.
- **Nội dung:** Danh sách phòng: tên, số dụng cụ, lần tập gần nhất; Nút "Thêm phòng"; Nút "Lấy phòng từ tổ" (2.8); Phòng mặc định là phòng lần trước.
- **Trạng thái và biến thể:** Một phòng; Nhiều phòng; Xoá phòng (không xoá được phòng duy nhất).
- **Vào từ:** 5.1, 1.2 (chọn "phòng khác"). **Đi tới:** → 5.4a, → 2.8.
- **Khoảnh khắc của vía:** Vía đứng trước cửa từng phòng.
- **Hình cần làm:** Dùng lại 3 biểu tượng mẫu phòng của 0.10.
- **Phụ thuộc:** 5.1, 0.10.
- **Ghi chú:** Bài học từ Fitbod: các hồ sơ phòng tuyệt đối không ghi đè nhau.

#### 5.4a · Chi tiết phòng tập

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Sửa dụng cụ, bước tạ của một phòng và chia sẻ phòng cho tổ.
- **Nội dung:** Tên phòng; Checklist dụng cụ (dùng lại 0.11); Bước tạ (dùng lại 0.12); Nút "Chia sẻ cho tổ"; Xoá phòng.
- **Trạng thái và biến thể:** Phòng tự nhập; Phòng lấy từ tổ (bản riêng); Đã chia sẻ; Chưa có tổ: ẩn nút chia sẻ.
- **Vào từ:** 5.4, 2.8, 1.2. **Đi tới:** → 5.4.
- **Khoảnh khắc của vía:** Không có vía riêng.
- **Hình cần làm:** Dùng lại biểu tượng dụng cụ của 0.11.
- **Phụ thuộc:** 5.4, 0.11, 0.12.

#### 5.5 · Vía của tôi

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Đổi tên và màu vía; xem giống vía của mình.
- **Nội dung:** Tên vía; Màu; Giống vía; Đổi giống (nếu cho phép).
- **Trạng thái và biến thể:** Đổi tên; Đổi màu; Đổi giống: tủ đồ đi theo người, không đi theo vía.
- **Vào từ:** 5.1. **Đi tới:** → 5.1.
- **Khoảnh khắc của vía:** Vía soi gương ngắm màu mới.
- **Hình cần làm:** Dùng lại ảnh của 0.3 và 0.4.
- **Phụ thuộc:** 5.1, 0.4.
- **Ghi chú:** QUYẾT ĐỊNH MỞ (D6): có cho đổi giống vía sau khi đã nhận không.

#### 5.6 · Sao lưu

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Xuất toàn bộ dữ liệu ra file và nhập lại, vì iOS có thể tự xoá dữ liệu của web app.
- **Nội dung:** Ngày sao lưu gần nhất; Nút "Xuất file sao lưu" (JSON); Nút "Nhập từ file"; Giải thích một dòng vì sao cần; Tần suất nhắc: 2 tuần / 1 tháng.
- **Trạng thái và biến thể:** Chưa sao lưu lần nào; Vừa xuất xong; Trình duyệt không cho lưu file: hướng dẫn cách khác.
- **Vào từ:** 5.1, 6.11. **Đi tới:** → 5.6a, → 5.1.
- **Khoảnh khắc của vía:** Vía cất một bản sao của hộp lên kệ cao.
- **Hình cần làm:** Cần mới: 1 render "hộp nhỏ trên kệ".
- **Phụ thuộc:** 5.1.
- **Ghi chú:** Bắt buộc có trong MVP. Nhật ký tập chi tiết chỉ nằm trên máy, không lên Firebase.

#### 5.6a · Khôi phục từ file

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Nhập file sao lưu trên máy mới hoặc sau khi mất dữ liệu.
- **Nội dung:** Chọn file; Xem trước: tên người dùng, vía, số buổi, ngày sao lưu; Lựa chọn: thay toàn bộ / gộp; Nút "Khôi phục".
- **Trạng thái và biến thể:** File hợp lệ; File hỏng hoặc sai phiên bản; Máy đang có dữ liệu: cảnh báo trước khi thay; Khôi phục xong: nối lại với tổ.
- **Vào từ:** 0.1, 5.6, 6.10. **Đi tới:** → 1.1.
- **Khoảnh khắc của vía:** "Hú vía! Tưởng mất." Vía chui ra từ hộp mới.
- **Hình cần làm:** Dùng kh_box và bản của Bình, Găng.
- **Phụ thuộc:** 5.6.
- **Ghi chú:** Nối lại danh tính trong tổ sau khi khôi phục phụ thuộc quyết định D1.

#### 5.7 · Sức khoẻ và vùng đau

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Xem và sửa câu trả lời sàng lọc, vùng hay đau, và nhật ký đau.
- **Nội dung:** Câu trả lời sàng lọc, trạng thái chế độ nhẹ; Vùng hay đau (0.9); Nhật ký đau: vùng, mức, ngày; Vùng đang theo dõi và số ngày.
- **Trạng thái và biến thể:** Không có gì; Đang theo dõi một vùng; Đau quá 14 ngày → 6.2.
- **Vào từ:** 5.1. **Đi tới:** → 0.8, 0.9, 6.2.
- **Khoảnh khắc của vía:** Vía nghiêm túc.
- **Hình cần làm:** Dùng lại hình cơ thể 0.9.
- **Phụ thuộc:** 5.1, 0.8, 0.9.
- **Ghi chú:** Dữ liệu này không bao giờ lên tổ.

#### 5.8 · Cài đặt

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Các tuỳ chọn chung của app.
- **Nội dung:** Đơn vị (kg; lb để sau); Âm thanh và rung khi hết giờ nghỉ; Giữ màn hình sáng khi tập; Thời gian nghỉ mặc định; Bật/tắt tủ đồ; Ẩn/hiện kỷ lục của mình với tổ.
- **Trạng thái và biến thể:** Tắt tủ đồ: streak và huy hiệu vẫn chạy; Máy không hỗ trợ rung hoặc Wake Lock: ẩn mục đó.
- **Vào từ:** 5.1. **Đi tới:** → 5.1.
- **Khoảnh khắc của vía:** Không có vía.
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 5.1.
- **Ghi chú:** MVP chỉ có kg.

#### 5.9 · Thông báo

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Chọn loại thông báo muốn nhận.
- **Nội dung:** Được cho vía; Tổ đủ buổi; Nhắc sao lưu.
- **Trạng thái và biến thể:** Chưa cấp quyền → 0.16; iOS chưa cài lên màn hình chính.
- **Vào từ:** 5.1. **Đi tới:** → 0.16.
- **Khoảnh khắc của vía:** Không có vía.
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 0.16.
- **Ghi chú:** Không có loại thông báo nào nhắc ngày nghỉ hay món đồ đang dở.

#### 5.10 · Giới thiệu và lưu ý y tế

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Thông tin app, lưu ý y tế, nguồn của các luật tập.
- **Nội dung:** Phiên bản; Lưu ý: app không thay bác sĩ; số cấp cứu 115; Nguồn chính của luật tập; Chuyện Ba Vía (đọc lại).
- **Trạng thái và biến thể:** Có bản mới.
- **Vào từ:** 5.1. **Đi tới:** → 5.1.
- **Khoảnh khắc của vía:** Ba vía đứng cạnh nhau.
- **Hình cần làm:** Có sẵn: k3_trio.
- **Phụ thuộc:** 5.1.

#### 5.11 · Bài ưa dùng và bài đã loại

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Xem và gỡ các lựa chọn "từ giờ về sau" khi đổi bài.
- **Nội dung:** Danh sách ô chuyển động và bài đang được ưu tiên; Nút gỡ.
- **Trạng thái và biến thể:** Trống.
- **Vào từ:** 5.1. **Đi tới:** → 5.1.
- **Khoảnh khắc của vía:** Không có vía.
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 1.4.
- **Ghi chú:** Ở MVP, lựa chọn "từ giờ về sau" vẫn được lưu; chỉ thiếu màn để xem lại.

### Luồng 6: Hệ thống và tình huống đặc biệt

#### 6.1 · Dừng ngay: dấu hiệu nguy hiểm

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Màn dừng buổi khi có dấu hiệu nguy hiểm toàn thân, có nút gọi cấp cứu.
- **Nội dung:** Chữ lớn "Dừng tập ngay"; Đau ngực bóp nghẹt, đau lan ra tay, cổ, hàm, kèm vã mồ hôi hoặc khó thở: nút gọi 115; Chóng mặt, sắp ngất, tim đập loạn: dừng, ngồi nghỉ, không hết thì đi khám; Nghe "rắc", sưng nhanh, biến dạng khớp: dừng và đi khám; Nút "Kết thúc buổi" (vẫn lưu những gì đã ghi).
- **Trạng thái và biến thể:** Mở từ báo đau; Mở từ nút luôn có trong 1.4; Sau khi kết thúc: lần mở app sau hỏi thăm một câu.
- **Vào từ:** 1.4b, 1.4, 1.2. **Đi tới:** → gọi 115; → 1.1.
- **Khoảnh khắc của vía:** Vía nghiêm túc, đứng sát cạnh; không đùa, không hoạt ảnh.
- **Hình cần làm:** Dùng biểu cảm "nghiêm túc" của 0.8. Màn này được phép phá quy tắc màu: chữ rõ, tương phản cao.
- **Phụ thuộc:** 1.4b.
- **Ghi chú:** Số 115 là thông tin phổ thông, chưa tra nguồn riêng. Buổi dừng vì lý do này không tính là thất bại.

#### 6.2 · Nên đi khám

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Khuyên đi khám khi đau kéo dài quá 14 ngày hoặc có dấu hiệu cảnh báo theo vùng.
- **Nội dung:** Vùng và lý do: "Vai đau 15 ngày chưa đỡ"; Dấu hiệu cần khám khẩn theo vùng (lưng dưới, gối, vai); App sẽ làm gì trong lúc chờ: khoá các ô liên quan ở biến thể nhẹ; Nút "Đã đi khám, được tập lại".
- **Trạng thái và biến thể:** Đau quá 14 ngày không cải thiện; Kiểu đau nhói, tê, lan, khớp kẹt hoặc sụm; Dấu hiệu cấp cứu của lưng dưới (tê hai chân, rối loạn tiểu tiện): chuyển sang 6.1.
- **Vào từ:** 1.2a, 1.4b, 5.7. **Đi tới:** → màn trước.
- **Khoảnh khắc của vía:** Vía nghiêm túc.
- **Hình cần làm:** Dùng lại hình cơ thể 0.9.
- **Phụ thuộc:** 1.2a.
- **Ghi chú:** Nội dung theo NHS trong tài liệu 01 mục 9.6; cần người có chuyên môn rà lại (D16).

#### 6.3 · Xin tuần nghỉ có phép

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Khai báo ốm, chấn thương hoặc đi xa để tuần đó không tính, mọi bộ đếm đứng yên.
- **Nội dung:** Lý do: ốm / chấn thương / đi xa; Số phép đang có (tối đa 2); Điều gì đứng yên: streak, mảnh đồ, thử thách cá nhân; Nút "Nghỉ tuần này".
- **Trạng thái và biến thể:** Còn phép; Hết phép: vẫn nghỉ được, streak dừng lại nhưng mảnh đã gom không mất; Ốm có sốt từ check-in; Huỷ nghỉ vì khoẻ lại.
- **Vào từ:** 1.2 (ốm có sốt), 1.1, 5.1. **Đi tới:** → 1.1.
- **Khoảnh khắc của vía:** Vía ngủ trong hộp, đắp cái tất. Không mờ đi, không buồn.
- **Hình cần làm:** Có sẵn: kh_sleepy, k3_sleepy. Cần mới: Bình và Găng ngủ đứng riêng (2 render).
- **Phụ thuộc:** 1.1.
- **Ghi chú:** Tích 1 phép sau mỗi 4 tuần đạt, giữ tối đa 2: con số chưa kiểm chứng (D15). Tổ thấy nhãn "nghỉ có phép", không thấy lý do.

#### 6.4 · Quay lại sau khi vắng

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Đón người dùng quay lại sau tuần hụt hoặc vài tuần vắng, và nói rõ buổi hôm nay nhẹ hơn thế nào.
- **Nội dung:** Lời chào: "Hú vía! Tưởng ai. Chủ đấy à."; Phần đã gom vẫn còn: mảnh, tủ đồ, kỷ lục streak; Buổi hôm nay: giữ tạ (trễ 4–10 ngày) hoặc −10% (trễ 11–21 ngày); Một dòng: nghỉ ngắn không làm mất thành quả.
- **Trạng thái và biến thể:** Trễ 4–10 ngày; Trễ 11–21 ngày; Trễ 22–56 ngày: 1–2 tuần làm quen lại; Vắng từ 3 tuần: nhận món "Tái xuất".
- **Vào từ:** 1.1 khi mở app sau khi vắng. **Đi tới:** → 1.2.
- **Khoảnh khắc của vía:** Luật của thế giới: "vía không đếm ngày chủ vắng, chỉ đếm ngày chủ đến".
- **Hình cần làm:** Có sẵn: kh_box. Cần mới: 1 dáng "giật mình mừng rỡ" cho mỗi giống (3 render).
- **Phụ thuộc:** 1.1.
- **Ghi chú:** Không bao giờ có số ngày vắng trên màn. Không có biểu tượng streak vỡ.

#### 6.5 · Gợi ý tuần giảm tải

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Khi nhiều bài cùng chững hoặc mệt kéo dài, đề nghị một tuần tập nhẹ.
- **Nội dung:** Lý do: "2 bài chính chững 2 tuần"; Tuần giảm tải là gì: nửa số set, dừng xa giới hạn hơn; Nút "Tập nhẹ tuần này" và "Chưa cần"; Dòng: tuần giảm tải vẫn tính là tuần đạt và vẫn có mảnh.
- **Trạng thái và biến thể:** Gợi ý; Đang trong tuần giảm tải (nhãn ở 1.3); Người dùng tự báo kiệt sức.
- **Vào từ:** 1.1 hoặc 1.3. **Đi tới:** → 1.3.
- **Khoảnh khắc của vía:** Vía nằm dài trên nắp hộp, thong thả.
- **Hình cần làm:** Cần mới: 1 dáng "nằm thong thả" (3 render).
- **Phụ thuộc:** 1.3.
- **Ghi chú:** Người mới không giảm tải theo lịch, chỉ khi chững. Trong 4–8 tuần thử đầu khó xảy ra, nên để v1.1.

#### 6.6 · Bắt đầu lại sau nghỉ dài

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Sau hơn 8 tuần vắng, bắt đầu lại từ 50–60% mức tạ cũ với 2–4 tuần làm quen.
- **Nội dung:** Lời chào như 6.4; Kế hoạch làm quen: tạ khởi điểm, 2–3 set mỗi bài, bao lâu; Hỏi lại nhanh: lịch, phòng tập, vùng đau có đổi không.
- **Trạng thái và biến thể:** Vắng hơn 56 ngày; Người mới: làm lại giai đoạn học kỹ thuật.
- **Vào từ:** 1.1 khi mở app sau hơn 8 tuần. **Đi tới:** → 5.3, 5.4, hoặc → 1.2.
- **Khoảnh khắc của vía:** Găng là vía hiểu chuyện này nhất: "Hôm nay chủ đẩy bao nhiêu, Găng đếm bấy nhiêu.".
- **Hình cần làm:** Dùng lại dáng của 6.4.
- **Phụ thuộc:** 6.4.
- **Ghi chú:** Bộ máy phải xử lý luật này từ MVP (hạ tạ đúng mức); màn giải thích riêng để v1.1.

#### 6.7 · Gợi ý giảm số buổi

- **Ưu tiên / trạng thái:** v1.1 · Chưa thiết kế
- **Mục đích:** Khi hơn nửa số buổi trong 3 tuần là vàng hoặc đỏ, gợi ý xem lại giấc ngủ, ăn uống hoặc bớt số buổi.
- **Nội dung:** Con số: "7 trong 10 buổi gần đây chủ đều mệt"; Ba gợi ý: ngủ, ăn, bớt buổi; Nút "Đổi lịch" → 5.3, nút "Giữ nguyên"; Dòng: giảm N không mất mảnh, không chậm nhịp nhận đồ.
- **Trạng thái và biến thể:** Gợi ý lần đầu; Đã từ chối: không hỏi lại trong 3 tuần.
- **Vào từ:** 1.2 hoặc 1.1. **Đi tới:** → 5.3 hoặc → 1.1.
- **Khoảnh khắc của vía:** Bình là vía hợp nhất: "Kế hoạch sai chứ chủ không sai.".
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** 1.2, 5.3.
- **Ghi chú:** Bộ máy ngừng giảm tiếp từ MVP; màn gợi ý để v1.1.

#### 6.8 · Hết giai đoạn học kỹ thuật

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Báo khi người mới xong 4 tuần đầu và cách tập sẽ đổi thế nào.
- **Nội dung:** "4 tuần đầu xong rồi"; Từ tuần sau: khoảng rep theo mục tiêu, hai bài đầu buổi tăng tạ mỗi buổi; Nút "Hiểu rồi" và "Cho thêm 2 tuần nữa".
- **Trạng thái và biến thể:** Hết 4 tuần; Kéo dài (tối đa 8 tuần); Về sau: gợi ý chuyển sang khung 4 buổi thân trên/thân dưới sau 3–6 tháng.
- **Vào từ:** 1.1 đầu tuần thứ 5. **Đi tới:** → 1.1.
- **Khoảnh khắc của vía:** Vía đội mũ tốt nghiệp bằng cái nắp chai.
- **Hình cần làm:** Cần mới: 1 render vui cho mốc này (dùng chung, 1–3 render).
- **Phụ thuộc:** 1.1.
- **Ghi chú:** Nhóm thử sẽ chạm mốc này ngay trong đợt thử đầu, nên phải có trong MVP.

#### 6.9 · Mất mạng và đồng bộ

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Cho thấy app vẫn chạy khi mất mạng và phần nào của tổ đang chờ gửi.
- **Nội dung:** Dải nhỏ trên tab Nhóm: "Chưa có mạng. Số liệu lúc 18:40."; Bài đăng và vía đang chờ gửi: nhãn "chờ gửi"; Tự gửi khi có mạng hoặc khi mở lại app.
- **Trạng thái và biến thể:** Mất mạng; Đang gửi lại; Gửi lỗi nhiều lần: nút thử lại; Vượt hạn mức Firebase: báo tổ tạm nghỉ đồng bộ.
- **Vào từ:** Tự hiện ở 2.1, 1.6, 2.3. **Đi tới:** → tự tắt khi có mạng.
- **Khoảnh khắc của vía:** Giọt vía nằm chờ trên nắp hộp.
- **Hình cần làm:** Không cần hình mới ngoài giọt vía có sẵn.
- **Phụ thuộc:** 2.1.
- **Ghi chú:** Check-in, sinh buổi, ghi set, tăng tạ, streak chạy hoàn toàn trên máy. iOS không có đồng bộ nền: chỉ đồng bộ khi mở app.

#### 6.10 · Máy mất dữ liệu

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Khi app mở ra thấy máy trống dù từng có dữ liệu, dẫn người dùng khôi phục.
- **Nội dung:** Giải thích ngắn: hệ điều hành đã dọn dữ liệu; Nút "Khôi phục từ file sao lưu"; Nút "Bắt đầu lại"; Nếu còn dấu vết trong tổ: hiện tên và vía cũ.
- **Trạng thái và biến thể:** Có file sao lưu; Không có file: lấy lại tên, vía, streak từ bản tóm tắt trên tổ (tuỳ D1); Bắt đầu lại hẳn.
- **Vào từ:** 0.1 khi phát hiện máy trống. **Đi tới:** → 5.6a hoặc → 0.3.
- **Khoảnh khắc của vía:** Hộp trống; vía ló ra từ sau hộp: chưa đi đâu cả.
- **Hình cần làm:** Cần mới: 1 render hộp trống.
- **Phụ thuộc:** 5.6a.
- **Ghi chú:** Rủi ro này là lý do sao lưu bắt buộc có trong MVP. Mức lấy lại được từ tổ phụ thuộc D1.

#### 6.11 · Nhắc sao lưu

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Nhắc định kỳ xuất file sao lưu, đặt ở chỗ không cản việc tập.
- **Nội dung:** Dải nhỏ trên 1.1 hoặc sau 1.6: "Lần sao lưu gần nhất: 16 ngày trước"; Nút "Sao lưu ngay" và "Để sau".
- **Trạng thái và biến thể:** Chưa sao lưu lần nào sau buổi thứ 3; Quá hạn nhắc; Vừa sao lưu xong.
- **Vào từ:** 1.1, 1.6. **Đi tới:** → 5.6.
- **Khoảnh khắc của vía:** Vía chỉ lên cái kệ cao.
- **Hình cần làm:** Dùng lại hình "hộp nhỏ trên kệ" của 5.6.
- **Phụ thuộc:** 5.6.
- **Ghi chú:** Không nhắc trong lúc đang tập.

#### 6.12 · Buổi dở dang

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Khôi phục buổi đang tập khi app bị tắt hoặc điện thoại khoá lâu.
- **Nội dung:** "Chủ đang tập dở Toàn thân B, xong 3/6 bài"; Nút "Tập tiếp"; Nút "Kết thúc tại đây"; Nút "Bỏ buổi này".
- **Trạng thái và biến thể:** Dở trong cùng ngày; Dở từ hôm trước: mặc định kết thúc tại đó; Đồng hồ nghỉ đang chạy khi app bị tắt.
- **Vào từ:** 1.1 khi mở app. **Đi tới:** → 1.4, → 1.6, hoặc → 1.1.
- **Khoảnh khắc của vía:** Vía vẫn đứng cạnh gương giữ chỗ.
- **Hình cần làm:** Có sẵn: kh_ready.
- **Phụ thuộc:** 1.4.
- **Ghi chú:** Nhờ ghi xuống máy sau mỗi set nên không mất set nào.

#### 6.13 · Bộ trạng thái trống

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Mẫu chung cho mọi màn chưa có dữ liệu.
- **Nội dung:** Một hình vía + một câu + một nút; Áp cho: lịch sử, bảng tin, tủ đồ, huy hiệu, cân nặng, phòng tập của tổ.
- **Trạng thái và biến thể:** Mỗi nơi một câu riêng.
- **Vào từ:** Tự hiện. **Đi tới:** → hành động chính của màn đó.
- **Khoảnh khắc của vía:** Vía ngồi chờ, không buồn.
- **Hình cần làm:** Dùng lại dáng "ngồi trên nắp hộp" của 2.9.
- **Phụ thuộc:** không.
- **Ghi chú:** Thiết kế một lần thành mẫu, không vẽ riêng từng màn.

#### 6.14 · Bộ thông báo lỗi

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Mẫu chung cho lỗi: không lưu được, không vào được tổ, file hỏng, hết chỗ lưu.
- **Nội dung:** Một câu nói chuyện gì xảy ra và làm gì tiếp; Nút thử lại hoặc lối thoát.
- **Trạng thái và biến thể:** Lỗi ghi dữ liệu trên máy; Máy hết dung lượng; Lỗi Firebase; Dữ liệu sai phiên bản sau khi cập nhật.
- **Vào từ:** Tự hiện. **Đi tới:** → thử lại hoặc màn trước.
- **Khoảnh khắc của vía:** Vía gãi đầu; lỗi là của app, không phải của người dùng.
- **Hình cần làm:** Cần mới: 1 dáng "gãi đầu" (3 render).
- **Phụ thuộc:** không.
- **Ghi chú:** Lỗi ghi dữ liệu là lỗi nghiêm trọng nhất: phải báo ngay, không im lặng.

#### 6.15 · Có bản mới

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Báo khi app có bản cập nhật và cho tải lại.
- **Nội dung:** Dải nhỏ: "Có bản mới" + nút "Cập nhật"; Không hiện trong lúc đang tập.
- **Trạng thái và biến thể:** Có bản mới; Đang cập nhật; Cập nhật xong: một dòng có gì mới.
- **Vào từ:** Tự hiện ở 1.1 hoặc 5.1. **Đi tới:** → tải lại app.
- **Khoảnh khắc của vía:** Không có vía.
- **Hình cần làm:** Không cần hình mới.
- **Phụ thuộc:** không.
- **Ghi chú:** Service worker phải không bao giờ thay bản giữa buổi tập.

#### 6.16 · Màn chờ mở app

- **Ưu tiên / trạng thái:** MVP · Chưa thiết kế
- **Mục đích:** Hình đầu tiên khi mở app từ màn hình chính, trong lúc tải.
- **Nội dung:** Nền của app + hộp đồ bỏ quên đóng nắp; Biểu tượng app trên màn hình chính.
- **Trạng thái và biến thể:** iOS (ảnh chờ theo từng cỡ máy); Android (màu nền + biểu tượng).
- **Vào từ:** Mở app. **Đi tới:** → 1.1 hoặc → 0.1.
- **Khoảnh khắc của vía:** Hộp đóng nắp; nắp hé ra khi tải xong.
- **Hình cần làm:** Cần mới: biểu tượng app (hộp + vía ló ra) ở các cỡ, và ảnh chờ: 1 render gốc, cắt ra nhiều cỡ.
- **Phụ thuộc:** không.
- **Ghi chú:** Tên app, biểu tượng và màu nền khai trong manifest.

## 4. Chỗ các tài liệu nguồn chưa khớp nhau

Những điểm dưới đây đã được xử lý trong danh sách màn theo hướng ghi ở cột phải; điểm nào cần người dùng quyết thì có mã quyết định.

| Điểm lệch | Xử lý trong tài liệu này |
|---|---|
| 03-app-patterns xếp bảng nhóm, feed, streak nhóm vào "giai đoạn 2" và nhiều phòng tập vào "sau" | Theo 00-plan mục 8 và các quyết định mới: tất cả thuộc MVP |
| 00-plan và 06 nói về thẻ chia sẻ ra Zalo/Messenger | Đã bỏ. Thành bài đăng trong tổ |
| 00-plan nói chia sẻ hồ sơ phòng bằng file hoặc QR | Đề xuất chia sẻ qua tổ trong app (D7) |
| 00-plan Q4 chốt người que SVG làm hình mẫu | Đã thay bằng bóng trong gương dựng Blender. Khối lượng hình tăng nhiều (D4) |
| Danh mục 36 món của 06 viết trước khi có Ba Vía (quần áo người); bản v2 dùng đồ bỏ quên với mốc khác ("Đủ 8 tuần liền") | Chỉ luật mảnh là đã khoá. Danh mục và mốc cần viết lại (D3) |
| 06 chia ô trang bị theo người (đầu, áo, quần, giày); 07 nói vía cần ô riêng thay cho mũ | Ô trang bị của vía phải định nghĩa lại cùng danh mục (D3) |
| Check-in ở 00-plan có câu "đau chỗ nào" ẩn; bản v2 chưa có | Thêm 1.2a |
| 00-plan có nút "Như mọi khi" bỏ qua mọi câu; bản v2 có thêm bước chọn phòng | Giữ như bản v2: phòng nằm trong thẻ "Như mọi khi" |
| Bản v2 có 4 tab, không có chỗ cho lịch sử và biểu đồ | Đề xuất đặt Tiến độ trong tab Tôi (D5) |
| Thông báo đẩy: kế hoạch để giai đoạn 2; 06 cấm nhắc món đang dở | 0.16 và 5.9 để v1.1; cài lên màn hình chính (0.2) vẫn là MVP |

## 5. Kế hoạch hình (Blender)

### 5.1 Đã có gì

| Nhóm | File (trong `blender/out/via/`) | Ghi chú |
|---|---|---|
| Ba giống đã duyệt | `khan/`, `binh/`, `gang/`: hero, 4 biểu cảm, avatar, 3 màu mỗi giống | Găng dùng mặt C |
| Dáng cho màn hình, chỉ Khăn màu mint | `screens/kh_*`: box, ready, sleepy, stand, cheer, copy, win, win2, 3 biểu cảm | Bình và Găng chưa có các dáng này |
| Cảnh ba vía | `screens/k3_*`: box, ok, ready, shy, sleepy, tired, trio, win | |
| Biểu tượng nỉ | `screens/k3_icon_box`, `k3_icon_balls`, `k3_icon_drop`, `headband` | Tab và giọt vía |
| Bóng trong gương | `screens/mir_0.0` đến `mir_1.0` (squat, 5 khung), `carry_0` đến `carry_2` | 2 trên 15 kiểu chuyển động |
| Đồ mặc thật | `wardrobe.py`: băng đô, băng cổ tay, tất; `wear/`: thử trên Bình, Găng và 4 avatar có đồ | 3 món |

### 5.2 Số render cần thêm: công thức, không phải một con số

Số render phụ thuộc hai quyết định (D2 và D4), nên ghi theo công thức:

- **Thân vía** = 3 giống × số dáng × số màu render sẵn. Số dáng cho MVP khoảng 24 (11 dáng Khăn đã có + 13 dáng mới).
  - Tô màu trên máy từ một ảnh trung tính: 3 × 24 × 1 = **khoảng 72**.
  - Bảng 6 màu render sẵn: 3 × 24 × 6 = **khoảng 430**.
- **Lớp đồ** = số món × 3 giống × số dáng có mặc đồ. Với 12 món và 4 dáng (avatar, đứng trong tủ đồ, ăn mừng, khoe đồ): **144**, cộng 12 render món đứng riêng. Nếu muốn đồ hiện ở mọi dáng thì nhân với 24 thay vì 4, tức khoảng 860.
- **Bóng trong gương** = số chuỗi × 5 khung. 15 kiểu chuyển động: **75** (đã có 8). Cả 90 bài: 450.
- **Đồ vật phụ và biểu tượng**: **45–60**.

Tổng cho MVP theo các đề xuất ở mục 8: thấp nhất khoảng **340 render** (tô màu trên máy), khoảng **700** nếu render sẵn 6 màu. Chưa đo thời gian render mỗi ảnh, nên chưa quy được ra giờ máy; việc đo nằm trong giai đoạn A1.

Điều không làm được: render sẵn mọi tổ hợp đồ. Với 12 món, mỗi vía ở mỗi dáng đã có hàng nghìn tổ hợp. Vì vậy D2 phải chốt trước khi làm hàng loạt.

### 5.3 Thứ tự làm hình

1. A1: một ca thử trọn đường ống trên điện thoại thật.
2. A2: dáng của Bình và Găng cho 6 màn v2 trước, rồi tới dáng của các màn mới theo thứ tự đợt thiết kế.
3. A3: món đồ, bắt đầu từ các món đã xuất hiện trong bản v2 (băng đô len, tất lệch đôi, dép tổ ong, kính bơi, áo mưa giấy).
4. A4: bóng trong gương theo thứ tự các ô của khung Toàn thân A/B (squat, hinge, đẩy ngang, kéo ngang, đẩy dọc, kéo dọc), rồi các kiểu còn lại.

Mỗi lô hình mới đều qua cổng duyệt của người dùng trước khi render hàng loạt, như đã làm với ba giống vía.

## 6. Lộ trình

Công sức tính bằng **buổi làm việc** (một phiên làm việc liền mạch với Claude, có người dùng duyệt ở cuối). Đây là ước lượng thô, không phải hẹn ngày.

| Mã | Giai đoạn | Mục tiêu | Công sức (buổi làm việc) | Cần xong trước |
|---|---|---|---|---|
| G0 | Chốt các quyết định mở | Người dùng trả lời các quyết định chặn việc để thiết kế, hình và spec không phải làm lại. | 1 | — |
| TK1 | Thiết kế đợt 1: trọn một buổi tập | Người dùng đi được trọn một buổi tập trên bản thiết kế, kể cả các ca khó, cùng những màn mà lát cắt code đầu tiên cần (lịch sử, phòng tập, sao lưu). | 5–6 | G0 |
| TK2 | Thiết kế đợt 2: lần đầu mở app | Người mới đi từ mở app đến buổi tập đầu tiên mà không cần ai giải thích. | 3–4 | G0, TK1 |
| TK3 | Thiết kế đợt 3: Nhóm và Tủ đồ | Đủ màn cho tổ và cho phần thưởng ở mức MVP. | 3 | TK1 |
| TK4 | Thiết kế đợt 4: Tiến độ, Tôi, tình huống đặc biệt | Hết toàn bộ màn MVP còn lại; chốt bộ mẫu trống và lỗi. | 3–4 | TK1 |
| A1 | Hình: đường ống avatar và thử nghiệm kỹ thuật | Chứng minh trên điện thoại rằng vía đúng giống, đúng màu, mặc đúng đồ hiện ra được ở mọi màn, theo cách đã chọn ở D2. | 2–3 | G0 |
| A2 | Hình: dáng và biểu cảm cho cả ba giống | Bình và Găng có đủ bộ dáng mà Khăn đã có, cộng các dáng mới của các màn chưa thiết kế. | 4–6 | A1 |
| A3 | Hình: danh mục đồ MVP | Đủ đồ cho 8–10 tuần dùng thử: mỗi món là mesh nỉ gắn rig của cả ba giống. | 5–7 | A1, G0 |
| A4 | Hình: bóng trong gương và đồ vật phụ | Mỗi bài tập trong buổi có hình làm mẫu; các biểu tượng nỉ của onboarding và huy hiệu có đủ. | 5–8 | G0 |
| T1 | Spec kỹ thuật | Một bộ tài liệu đủ để code mà không phải đoán: dữ liệu, luật, lưu trữ, đồng bộ, cài đặt. | 3–4 | G0 |
| T2 | Rà nội dung an toàn và hướng dẫn | Nội dung y tế và kỹ thuật được người có chuyên môn xem trước khi vào app. | 2–3 | — |
| B0 | Khung PWA và thử trên iPhone thật | Trả lời bằng máy thật các câu hỏi về iOS trước khi xây gì lớn. | 1–2 | G0 |
| B1 | Rules engine (chưa có giao diện) | Bộ máy ra bài chạy đúng trên các ca kiểm thử, tách hẳn khỏi giao diện. | 4–5 | T1 |
| B2 | Lát cắt 1: một người tập trọn vòng trên điện thoại | Một người tự dùng được hằng ngày: onboarding → check-in → tập → xong buổi → lịch sử → sao lưu, không cần mạng. | 8–10 | TK1, TK2, B0, B1 |
| B3 | Lát cắt 2: tổ | Cả nhóm thấy nhau: bảng tuần, bảng tin, cho vía, thử thách, streak tổ. | 5–6 | TK3, B2, T1 |
| B4 | Lát cắt 3: vía và tủ đồ đầy đủ | Mỗi người có vía đúng giống, đúng màu, mặc đồ thật ở mọi màn; nhận món và chọn món chạy trọn. | 4–5 | TK3, A2, A3, B2 |
| B5 | Hoàn thiện MVP | Hết các màn MVP còn lại và các ca đặc biệt. | 5–6 | TK4, B3, B4, A4, T2 |
| U1 | Thử với nhóm thật | Cả nhóm dùng thật và các con số thiết kế được chỉnh theo thực tế. | 3–4 | B5 |
| V1 | Bản 1.1 | Các màn đã hoãn, làm theo phản hồi của nhóm. | 8–10 | U1 |

Cộng lại cho tới khi cả nhóm dùng được bản MVP: thiết kế 14–17 buổi, hình 16–24 buổi, spec và rà nội dung 5–7 buổi, code 27–34 buổi, thử nghiệm 3–4 buổi. Tổng khoảng **66–87 buổi làm việc**. Nhiều giai đoạn chạy song song được (xem mục 6.2).

### 6.1 Chi tiết từng giai đoạn

**G0 · Chốt các quyết định mở** (1 buổi)

- Bắt buộc trước khi làm tiếp: D1 (vào tổ), D2 (đường đi của avatar), D3 (danh mục đồ), D4 (bóng trong gương), D14 (có code phần không giao diện song song không)
- Nên trả lời luôn: D5, D6, D7
- Ghi kết quả vào bộ nhớ dự án và cập nhật screens.json

**TK1 · Thiết kế đợt 1: trọn một buổi tập** (5–6 buổi)

- Màn mới (23): 1.2a, 1.2b, 1.3, 1.4a, 1.4b, 1.4c, 1.4d, 1.4e, 1.4f, 1.4g, 1.5, 1.6a, 1.6b, 1.6c, 1.7, 6.1, 6.12, 4.2, 4.3, 5.4, 5.4a, 5.6, 5.6a
- Vá chỗ thiếu của màn v2: 1.1, 1.2, 1.4, 1.6 (các trạng thái ghi ở mục ghi chú của từng màn)
- Mỗi đợt thiết kế: dựng HTML như screens-v2, một tác tử độc lập so mù với ảnh tham khảo, rồi người dùng duyệt

**TK2 · Thiết kế đợt 2: lần đầu mở app** (3–4 buổi)

- Màn mới (18): 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.8a, 0.9, 0.10, 0.11, 0.12, 0.13, 0.14, 0.14a, 0.14b, 0.15
- Lấy nguyên văn PAR-Q+ chính thức trước khi viết chữ cho 0.8
- Thử luồng với một người chưa biết app: bấm giờ, mục tiêu dưới 4 phút

**TK3 · Thiết kế đợt 3: Nhóm và Tủ đồ** (3 buổi)

- Màn mới (11): 2.1a, 2.3, 2.3a, 2.5, 2.6, 2.7, 2.8, 2.9, 6.9, 3.2, 3.3
- Vá chỗ thiếu của màn v2: 2.1, 3.1 (các trạng thái ghi ở mục ghi chú của từng màn)

**TK4 · Thiết kế đợt 4: Tiến độ, Tôi, tình huống đặc biệt** (3–4 buổi)

- Màn mới (21): 4.1, 4.4, 4.5, 4.7, 5.1, 5.2, 5.3, 5.5, 5.7, 5.8, 5.10, 6.2, 6.3, 6.4, 6.8, 6.10, 6.11, 6.13, 6.14, 6.15, 6.16

**A1 · Hình: đường ống avatar và thử nghiệm kỹ thuật** (2–3 buổi)

- Làm thử một ca đầy đủ: Bình màu cam mặc băng đô + tất ở 3 dáng, hiện trên điện thoại thật
- Đo thời gian render một ảnh ở cỡ dùng thật, để quy khối lượng ở mục 5 ra giờ máy
- Chốt quy cách xuất: cỡ ảnh, định dạng (WebP có trong suốt), tên file, dung lượng tối đa của cả app
- Viết trình xuất hàng loạt trên nền render_all.py và wear_run.py

**A2 · Hình: dáng và biểu cảm cho cả ba giống** (4–6 buổi)

- Khoảng 11 dáng Khăn đã có trong blender/out/via/screens cần dựng cho Bình và Găng
- Khoảng 13 dáng mới cho cả ba giống (chào, cầm sổ, nghiêm túc, khoe đồ, lo, lau mồ hôi, đi bộ, ôm vía, giơ bìa, ngồi nắp hộp, giật mình mừng, gãi đầu, chỉ tay)
- Ước lượng: 3 giống × khoảng 24 dáng × số màu render sẵn. Tô màu trên máy: khoảng 72 render. Render sẵn 6 màu: khoảng 430 render
- Mỗi giống qua cổng duyệt của người dùng trước khi render hàng loạt

**A3 · Hình: danh mục đồ MVP** (5–7 buổi)

- Viết lại danh mục cho thế giới Ba Vía (D3). Đề xuất MVP 12 món: 3 món khởi đầu, 6 món lộ trình tuần, 3 món mốc và tổ
- Đã dựng 3 món: băng đô, băng cổ tay, tất. Còn khoảng 9 món
- Mỗi món: điểm neo cho 3 giống, 1 render đứng riêng, render trên người ở 4 dáng (avatar, đứng trong tủ đồ, ăn mừng, khoe đồ)
- Ước lượng: 12 món × 3 giống × 4 dáng = 144 render lớp đồ, cộng 12 render đứng riêng
- Món kín đầu phải thiết kế riêng cho từng giống: để sau MVP

**A4 · Hình: bóng trong gương và đồ vật phụ** (5–8 buổi)

- Bóng trong gương: tối thiểu 15 kiểu chuyển động × 5 khung = 75 khung (đã có squat và carry). Đầy đủ 90 bài × 5 khung = 450 khung
- Đề xuất MVP: 15 chuỗi theo kiểu chuyển động, sau đó thêm biến thể theo dụng cụ cho các bài hay gặp nhất
- Đồ vật phụ khoảng 45–60 render: 4 mục tiêu, 3 mẫu phòng, 8–22 dụng cụ, 3 loại tạ, 8–10 huy hiệu, các cảnh hộp, 6 cảnh thử thách, biểu tượng app, hình cơ thể 4 vùng

**T1 · Spec kỹ thuật** (3–4 buổi)

- Mô hình dữ liệu: hồ sơ, vía, phòng tập, buổi, set, tiến độ từng bài, streak, phép nghỉ, mảnh và món, nhật ký đau. UUID, profileId, updatedAt, xoá mềm, log chỉ ghi thêm
- Rules engine: bảng tham số từ 01-programming mục 10; hàm thuần sinh buổi, tăng tạ (3 thuật toán), vùng check-in, cắt theo thời gian, đếm volume, luật đau, luật nghỉ; danh sách ca kiểm thử
- Lưu trữ trên máy: IndexedDB, ghi sau mỗi set, phiên bản và nâng cấp dữ liệu, định dạng file sao lưu
- Firebase: cấu trúc tổ, bản tóm tắt tuần, sự kiện bảng tin, vía, hồ sơ phòng chia sẻ; security rules; hàng chờ gửi khi mất mạng; danh tính theo D1
- PWA: manifest, service worker (không thay bản giữa buổi), cài trên iOS và Android, Wake Lock, kiểm tra storage.persist()
- Luật thưởng: mảnh lưu theo phần của một món, trần 1 mảnh/ngày và 1 món/tuần, cách bày 3 món

**T2 · Rà nội dung an toàn và hướng dẫn** (2–3 buổi)

- Đối chiếu nguồn cho 72/90 bài chưa kiểm (mới đạt 18/90)
- Vợ người dùng (học vật lý trị liệu) rà bảng đau, màn 6.1 và 6.2
- Lấy bản PAR-Q+ chính thức và dịch
- Kiểm số liệu phòng tập thật của nhóm: thanh đòn, đĩa nhỏ nhất, bước tạ tay

**B0 · Khung PWA và thử trên iPhone thật** (1–2 buổi)

- Một PWA rỗng trên Netlify, cài lên iPhone và Android của nhóm (là code không giao diện: cần D14 đồng ý)
- Thử: dữ liệu IndexedDB có giữ được qua 2 tuần không mở; bản Safari và bản cài có chung dữ liệu không; storage.persist() trả gì; Wake Lock; xuất và nhập file
- Kết quả quyết định thứ tự màn 0.2 và cách mời vào tổ

**B1 · Rules engine (chưa có giao diện)** (4–5 buổi)

- Code các hàm thuần theo spec T1, chạy bằng kiểm thử tự động
- Giả lập 12 tuần cho vài hồ sơ mẫu (người mới 3 buổi, người đã tập 4 buổi, người có đau gối) và đọc kết quả bằng mắt
- Kiểm độ phủ ô bài với từng hồ sơ phòng mẫu

**B2 · Lát cắt 1: một người tập trọn vòng trên điện thoại** (8–10 buổi)

- Màn (36): 0.1, 0.2, 0.5, 0.6, 0.7, 0.8, 0.8a, 0.9, 0.10, 0.11, 0.12, 0.13, 1.1, 1.2, 1.2a, 1.2b, 1.3, 1.4, 1.4a, 1.4b, 1.4c, 1.4d, 1.4e, 1.4f, 1.4g, 1.5, 1.6, 1.7, 6.1, 6.12, 4.2, 4.3, 5.4, 5.4a, 5.6, 5.6a
- Vía ở mức tối thiểu: một giống mặc định, thanh mảnh chạy đúng luật nhưng chưa có màn nhận món
- Vòng thử 1 (thuộc U1) chạy ngay sau giai đoạn này: người dùng và vợ tập thật 2 tuần

**B3 · Lát cắt 2: tổ** (5–6 buổi)

- Màn (13): 0.14, 0.14a, 0.14b, 2.1, 2.1a, 2.3, 2.3a, 2.5, 2.6, 2.7, 2.8, 2.9, 6.9
- Firebase theo spec T1
- Thử mất mạng giữa chừng và hai máy cùng lúc

**B4 · Lát cắt 3: vía và tủ đồ đầy đủ** (4–5 buổi)

- Màn (9): 0.3, 0.4, 0.15, 1.6a, 1.6b, 1.6c, 3.1, 3.2, 3.3
- Ráp toàn bộ hình từ A2 và A3 theo đường ống A1

**B5 · Hoàn thiện MVP** (5–6 buổi)

- Màn (21): 4.1, 4.4, 4.5, 4.7, 5.1, 5.2, 5.3, 5.5, 5.7, 5.8, 5.10, 6.2, 6.3, 6.4, 6.8, 6.10, 6.11, 6.13, 6.14, 6.15, 6.16
- Ráp bóng trong gương từ A4 và nội dung đã rà từ T2
- Soát lại hiệu năng và dung lượng app trên máy yếu nhất của nhóm

**U1 · Thử với nhóm thật** (3–4 buổi)

- Vòng 1: 2 người (người dùng và vợ), 2 tuần, chạy sớm ngay sau B2 chứ không chờ B5
- Vòng 2: cả nhóm, 4 tuần, sau B5: đủ để chạm mốc hết giai đoạn học kỹ thuật và streak 4 tuần
- Theo dõi: check-in mất bao lâu, bao nhiêu lần đổi bài, mức tạ gợi ý có sát không, ai mất dữ liệu trên iPhone, tổ có dùng cho vía không
- Chỉnh các con số còn là giả định: phép nghỉ 4 tuần/1 phép, ngưỡng streak tổ, mốc đồ, mức tạ khởi điểm
- Công sức chỉ tính các buổi sửa sau mỗi vòng, không tính thời gian nhóm dùng thử

**V1 · Bản 1.1** (8–10 buổi)

- Màn v1.1: 0.16, 2.2, 2.4, 2.5a, 3.3a, 3.4, 4.6, 4.8, 4.9, 5.9, 5.11, 6.5, 6.6, 6.7
- Sau đó: 2.10, 2.11, 3.5 (mùa truyện, chọc bạn và thi 1-1, đồ theo mùa)


### 6.2 Cái gì chạy song song được

- Sau G0, ba mạch chạy song song: thiết kế (TK1 rồi TK2, TK3, TK4), hình (A1 rồi A2, A3; A4 riêng) và spec (T1 rồi B1).
- T2 không phụ thuộc gì, làm được ngay. B0 làm được ngay sau G0 nếu D14 được đồng ý.
- B1 (rules engine, không giao diện) chỉ cần spec; có code trước khi duyệt hết thiết kế hay không là quyết định D14.
- Vòng thử đầu tiên với 2 người diễn ra ngay sau B2, không chờ tổ và tủ đồ.

### 6.3 Ba lát cắt code và cái gì chứng minh là xong

| Lát cắt | Chứng minh là xong |
|---|---|
| B2: một người | Người dùng và vợ tập thật 2 tuần chỉ bằng app, không mất set nào, mức tạ gợi ý dùng được, check-in ngày thường dưới 10 giây |
| B3: tổ | Ba điện thoại (ít nhất một iPhone) thấy cùng một bảng tuần; tắt mạng giữa buổi rồi bật lại, bài đăng và vía tự lên |
| B4: vía và tủ đồ | Ba người chọn ba giống, màu khác nhau, mặc đồ khác nhau; cả ba hiện đúng trên bảng tổ của nhau; nhận món cuối tuần chạy trọn |

### 6.4 Rủi ro chính

| Rủi ro | Cách giảm |
|---|---|
| iOS xoá dữ liệu web app | B0 thử trên máy thật; sao lưu và nhắc sao lưu trong MVP; D1 để lấy lại danh tính |
| Khối lượng hình vượt sức | D2 và D4 chốt sớm; A1 đo thời gian render thật trước khi nhận khối lượng |
| Hướng dẫn kỹ thuật mới kiểm 18/90 bài | T2; ưu tiên bài mà phòng của nhóm thật sự dùng |
| Các con số của bộ máy phần lớn là mặc định thiết kế | Để hết trong file cấu hình; vòng thử 4 tuần để chỉnh |
| Thiết kế bị chê "rẻ tiền" lần nữa | Giữ quy trình đã qua được ở bản v2: hệ thống thiết kế chung, mỗi màn một hình nỉ làm tâm, so mù độc lập, duyệt từng đợt nhỏ |
| Giọng của vía trượt thành trách móc | Luật viết: vía không đếm ngày vắng, không nhắc món dở, không bình phẩm cân nặng; rà chữ cùng lúc với rà thiết kế |

## 7. Spec kỹ thuật cần viết (giai đoạn T1)

| Tài liệu | Nội dung chính | Nguồn đã có |
|---|---|---|
| Mô hình dữ liệu | Các bảng trên máy và phần đẩy lên Firebase; quy ước UUID, `profileId`, `updatedAt`, xoá mềm, log chỉ ghi thêm | 00-plan mục 5; 03 mục 9 |
| Rules engine | Tham số, hàm, thứ tự ưu tiên luật, ca kiểm thử | 00-plan mục 3; 01 mục 4–6, 9, 10; exercises.json (90 bài, 15 kiểu chuyển động, 22 loại dụng cụ) |
| Luật động lực | Streak tuần, phép nghỉ, mảnh và món, huy hiệu, thử thách và streak tổ | 03 mục 8c; 06 mục 3–4 |
| Lưu trữ và sao lưu | IndexedDB, ghi sau mỗi set, nâng cấp phiên bản, định dạng file sao lưu, phát hiện máy trống | 03 mục 7 (iOS) |
| Đồng bộ tổ | Cấu trúc Firestore, security rules, hàng chờ gửi, hạn mức gói miễn phí, danh tính theo D1 | 03 mục 9 |
| PWA | Manifest, service worker, cài đặt iOS và Android, Wake Lock, cập nhật không cắt ngang buổi tập | 03 mục 4 và 7 |
| Đường ống hình | Quy cách ảnh, tên file, cách ghép lớp đồ, dung lượng | Kết quả A1 |

Những gì chỉ đẩy lên Firebase: bản tóm tắt tuần của mỗi người, sự kiện bảng tin, vía đã cho, hồ sơ vía (giống, tên, màu, đồ đang mặc), hồ sơ phòng tập được chia sẻ. Nhật ký tập chi tiết, cân nặng, câu trả lời sức khoẻ và nhật ký đau chỉ nằm trên máy.

## 8. Quyết định cần người dùng chốt

Xếp theo mức chặn việc: D1–D4 chặn thiết kế và hình; D5–D12 chặn từng màn; D13–D17 là việc cần hỏi hoặc cho phép.

**D1. Vào tổ bằng mã nhóm không tài khoản, hay đăng nhập Google?**

- Mã nhóm, không tài khoản: nhanh, không cần email; mất dữ liệu máy là mất luôn danh tính trong tổ, phải vào lại như người mới
- Đăng nhập Google: thêm một bước lúc đầu; lấy lại được tên, vía, streak sau khi máy mất dữ liệu; security rules chặt hơn
- Mã nhóm + đăng nhập ẩn danh của Firebase, cho nối Google sau trong mục Tôi
- **Đề xuất:** Phương án thứ ba: vào bằng mã cho nhanh, nối Google là tuỳ chọn để giữ danh tính. Lý do chính là rủi ro iOS xoá dữ liệu.

**D2. Vía mặc đồ đến được điện thoại bằng cách nào, và màu vía là bảng cố định hay tự do?**

- Render sẵn theo lớp: thân vía theo giống × dáng × màu, mỗi món là một lớp render 3D riêng có che khuất đúng, ghép trên máy. Số ảnh tính bằng phép cộng
- Render sẵn mọi tổ hợp: không khả thi khi có trên 6 món (số tổ hợp nhân đôi theo mỗi món)
- Dựng 3D thật trên máy (three.js): linh hoạt nhất, nhưng mất chất nỉ của Cycles và nặng với máy yếu
- Màu: bảng cố định 6–8 màu mỗi giống, hoặc màu tự do tô trên máy từ một ảnh render trung tính
- **Đề xuất:** Render sẵn theo lớp + bảng 6 màu cố định mỗi giống. Cần người dùng xác nhận rằng lớp đồ render 3D riêng rồi ghép vẫn đúng yêu cầu "mặc thật, không dán 2D". Thử trong giai đoạn A1 trước khi làm hàng loạt.

**D3. Danh mục đồ và các mốc mở đồ theo thế giới Ba Vía là gì?**

- Giữ danh mục 36 món của tài liệu 06 (quần áo người: áo ba lỗ, quần đùi, giày)
- Viết lại thành đồ bỏ quên vừa thân hình vía (băng đô len, tất lệch đôi, dép tổ ong, kính bơi, áo mưa giấy), giữ nguyên luật mảnh và ba bậc
- Mốc streak: 4/12/26 tuần như tài liệu 06, hay 8 tuần như bản v2
- **Đề xuất:** Viết lại theo đồ bỏ quên, MVP 12 món. Giữ mốc 4/12/26 tuần của tài liệu 06 và sửa chữ trong bản v2.

**D4. Bóng trong gương làm mẫu cho 90 bài bằng cách nào?**

- Mỗi kiểu chuyển động một chuỗi (15 chuỗi, khoảng 75 khung), các bài cùng kiểu dùng chung
- Mỗi bài một chuỗi riêng (90 chuỗi, khoảng 450 khung)
- 15 chuỗi cho MVP, thêm biến thể theo dụng cụ cho khoảng 20 bài hay gặp nhất sau
- Vía bắt chước nằm trong ảnh (phải render theo giống) hay là một hình riêng đặt cạnh gương
- **Đề xuất:** Phương án thứ ba, và vía là hình riêng đặt cạnh gương để ảnh gương dùng chung cho mọi giống.

**D5. Tiến độ (lịch sử, biểu đồ, cân nặng) nằm ở đâu?**

- Trong tab Tôi, giữ 4 tab như bản v2
- Thêm tab thứ năm "Tiến độ"
- **Đề xuất:** Trong tab Tôi. Bốn tab đã được duyệt, và tiến độ không phải việc hằng ngày.

**D6. Có cho đổi giống vía sau khi đã nhận không?**

- Không cho đổi
- Cho đổi tự do; tủ đồ đi theo người
- Cho đổi nhưng có xác nhận, không giới hạn
- **Đề xuất:** Cho đổi có xác nhận. Tài liệu 06 đã quy định tủ đồ đi theo người.

**D7. Chia sẻ hồ sơ phòng tập bằng cách nào sau khi đã bỏ chia sẻ ra ngoài?**

- Qua tổ trong app (Firebase): bạn bấm "Lấy về máy"
- File hoặc mã QR như kế hoạch gốc
- Cả hai
- **Đề xuất:** Qua tổ trong app. File sao lưu vẫn chứa hồ sơ phòng nên không mất gì. Nếu chọn hướng này, bước vào tổ (0.14) nên chuyển lên trước bước tạo phòng (0.10) để người vào sau lấy được phòng ngay lần đầu.

**D8. Một người có được ở nhiều tổ cùng lúc không?**

- Một tổ
- Nhiều tổ
- **Đề xuất:** Một tổ ở MVP. Mô hình dữ liệu vẫn để tổ là danh sách để mở rộng sau.

**D9. Buổi đi bộ 20–30 phút ở ngày vùng đỏ có tính là buổi đạt và cho mảnh không?**

- Có, tính như buổi thường
- Tính cho streak nhưng không cho mảnh
- Không tính
- **Đề xuất:** Có. Nếu không, người mệt sẽ cố tập tạ để khỏi thiệt, ngược với luật chống tập quá sức.

**D10. Bài đăng trong tổ: có lời tự viết và bình luận không?**

- Chỉ thẻ tự sinh + cho vía
- Thêm một dòng lời tự viết
- Thêm bình luận
- **Đề xuất:** MVP chỉ thẻ tự sinh + cho vía. Nhóm đã có chỗ nói chuyện riêng; bình luận kéo theo việc kiểm duyệt và thông báo.

**D11. Ai đặt mục tiêu thử thách tuần của tổ?**

- App tự đặt theo tổng lời hứa của cả tổ (ví dụ 85%)
- Người lập tổ tự đặt
- Tổ bỏ phiếu
- **Đề xuất:** App tự đặt. Con số phần trăm chỉnh sau khi thử với nhóm thật.

**D12. Streak tổ tính tuần đạt khi nào?**

- Mọi người đều đạt mục tiêu riêng
- Từ 80% số người đạt
- Người nghỉ có phép không tính vào mẫu số
- **Đề xuất:** Từ 80% số người đạt, và người nghỉ có phép không tính. Tổ 3 người thì nghĩa là cả ba.

**D13. Trong nhóm có ai kiêng chuyện hồn vía không?**

- Giữ tên "vía"
- Đổi tên gọi ("bóng", "hơi") nhưng giữ nguyên chuyện
- **Đề xuất:** Hỏi cả nhóm trước khi viết chữ cho onboarding. Chỉ cần một người thấy gở là đổi tên gọi.

**D14. Có cho code phần không có giao diện (B0 thử iPhone, B1 rules engine) song song với thiết kế không?**

- Có: tiết kiệm thời gian, không đụng đến giao diện
- Không: chờ duyệt hết thiết kế rồi mới code
- **Đề xuất:** Có. Quy tắc "chưa duyệt thiết kế thì chưa code" vẫn giữ cho mọi thứ có giao diện.

**D15. Các con số còn là giả định của hệ thống động lực**

- Phép nghỉ: tích 1 phép sau 4 tuần đạt, giữ tối đa 2
- Món "Tái xuất" sau 3 tuần vắng
- Mốc 10/25/50 tuần đạt cộng dồn
- **Đề xuất:** Giữ các con số của tài liệu, ghi vào file cấu hình, chỉnh sau vòng thử 4 tuần.

**D16. Ai rà nội dung an toàn và hướng dẫn kỹ thuật?**

- Vợ người dùng rà bảng đau và các màn 6.1, 6.2
- Tự đối chiếu nguồn cho 72 bài còn lại
- Phát hành trước với 18 bài đã kiểm, bài chưa kiểm ghi nhãn
- **Đề xuất:** Vợ người dùng rà phần đau; đối chiếu nguồn ưu tiên các bài mà hồ sơ phòng của nhóm thật sự dùng tới.

**D17. Thông báo đẩy có trong bản đầu không?**

- Không, để v1.1
- Có, chỉ cho "được cho vía"
- **Đề xuất:** Để v1.1. Push cần máy chủ gửi, và trên iOS chỉ chạy khi đã cài lên màn hình chính.


## 9. Giới hạn của tài liệu này

- Danh sách màn dựng từ tài liệu nghiên cứu và bản v2, chưa qua một lần dùng thử nào. Số màn sẽ đổi khi thiết kế thật.
- Số render là phép tính trên giả định (24 dáng, 12 món, 5 khung mỗi chuỗi), chưa đo.
- Công sức theo buổi làm việc là ước lượng thô.
- Hành vi lưu trữ của iOS với web app cài lên màn hình chính chưa được thử trên máy của nhóm; thứ tự màn 0.2 và cách mời vào tổ phụ thuộc phép thử đó.
- Nguyên văn PAR-Q+ và số cấp cứu 115 chưa được đối chiếu nguồn chính thức.
