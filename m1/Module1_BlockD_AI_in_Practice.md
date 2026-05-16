# Module 1 — Block D: AI in Practice (Slides 15–18)

**Block:** D — AI Trong Thực Tế Vận Hành
**Slides:** 15–18
**Status:** Draft — Chờ duyệt
**Sources:** Day1_Lecture_Notes.md, Module1_Source_CSAI2025.md, update_module1.md

---

Slide 15: AI Threat Detection Pipeline — Quy Trình 6 Bước

```markdown
# Đường Ống Phát Hiện Mối Đe Dọa Bằng AI

**1. Data Collection:** Gom log từ mạng, endpoint, hệ thống
**2. Preprocessing:** Làm sạch dữ liệu, chuẩn hóa định dạng
**3. Feature Extraction:** Trích xuất đặc trưng (ví dụ: kích thước file, tần suất IP)
**4. Model Training:** AI học từ dữ liệu để nhận diện pattern
**5. Real-time Analysis:** Phân tích **hàng tỷ sự kiện mỗi giờ** ở chế độ thời gian thực
**6. Response:** Tự động phản ứng (chặn IP, khóa tài khoản) hoặc cảnh báo cho analyst

**Đây là xương sống của mọi hệ thống bảo mật AI hiện đại.**
```

💡 **Note:** Giải thích quy trình này như một nhà máy lọc nước. Data Collection là hút nước từ sông (log thô), Preprocessing là lọc cặn (bỏ log rác), Feature Extraction là kiểm tra các hóa chất (đặc trưng), Analysis là đưa qua cảm biến AI, và Response là đóng van nếu phát hiện độc tố. Từ khóa quan trọng: "Feature Extraction" (sẽ học kỹ ở Module 2).

---

Slide 16: Giải Quyết Nỗi Đau Lớn Nhất — Alert Fatigue

```markdown
# Cảnh Báo Giả (False Positive) & Alert Fatigue

**Nỗi đau của IT Operations:**
- Một SOC analyst xử lý trung bình ~174 cảnh báo/ngày
- Hơn **52% là cảnh báo giả** (False Positive)
- Hậu quả: Bỏ qua cảnh báo thật vì đã quá mệt mỏi (Alert Fatigue)

**Giải pháp từ AI Security Copilots:**
- Giảm False Positive từ >90% xuống dưới **5%**
- Nhờ khả năng phân tích ngữ cảnh (Context-aware)
- Không chỉ đưa ra cảnh báo mà còn cung cấp lý do (Explainable AI)

**Ví dụ:** Thay vì báo "Có IP lạ đăng nhập", AI báo "Người dùng X đăng nhập từ thiết bị mới, nhưng thời gian và quy trình xác thực khớp với chuyến công tác của họ → Bỏ qua."
```

💡 **Note:** Hỏi học viên xem ai đã từng thiết lập rule "gửi email khi server quá tải" rồi sau đó phải tạo một filter riêng để bỏ qua các email đó vì chúng gửi quá nhiều. Đó chính là Alert Fatigue. Nhấn mạnh rằng giá trị thực sự của AI không phải là "tìm ra thêm lỗi", mà là "giảm bớt cảnh báo sai" để con người tập trung vào cảnh báo thật.

---

Slide 17: User Behavior Analytics (UBA)

```markdown
# UBA: Quản Lý Hành Vi Người Dùng

**Định nghĩa "Bình Thường" cho từng người:**
- Giờ đăng nhập và vị trí
- Ứng dụng thường dùng
- Khối lượng và mẫu truy cập dữ liệu

**Khi AI bắt đầu giám sát:**
- Phát hiện rủi ro từ nội bộ (**Insider Threat**)
- Phát hiện việc leo thang đặc quyền
- Phát hiện dấu hiệu rò rỉ dữ liệu (Data Exfiltration)

**Ví dụ thực tế:**
Một nhân viên ngân hàng bình thường không bao giờ tải quá 50MB dữ liệu/ngày. Đột nhiên tải 500MB dữ liệu khách hàng lúc 2 giờ sáng → AI lập tức đóng băng tài khoản trước khi dữ liệu bị tuồn ra ngoài.
```

💡 **Note:** Giới thiệu UBA như một camera giám sát "ảo" theo dõi cách mọi người làm việc, chứ không phải theo dõi nội dung công việc. Liên hệ đến nguyên tắc bảo vệ mới: Vành đai đã chết (như nhắc ở Slide 6), giờ chúng ta bảo vệ Workflow và hành vi.

---

Slide 18: Kỷ Nguyên Của AI Security Copilots

```markdown
# Trợ Lý AI: Sự Chuyển Dịch Sang "Hyper-Scale"

**Từ Rule-based sang AI Copilot:**
- Không còn phải viết hàng ngàn dòng quy tắc tường lửa thủ công
- AI Security Copilots (như Microsoft Security Copilot) hoạt động như một chuyên gia cấp cao hỗ trợ analyst 24/7

**Khả năng "Hyper-scale":**
- Phân tích hàng tỷ log và sự kiện trên toàn cầu trong vài giây
- Tự động săn tìm mối đe dọa (Threat Hunting)
- Tóm tắt sự cố phức tạp thành báo cáo ngôn ngữ tự nhiên

**Kết luận:** Bạn không thể chống lại AI của hacker bằng sức người. Bạn cần AI của riêng mình để tự động hóa và tăng tốc ở mức độ "hyper-scale".
```

💡 **Note:** Nhấn mạnh rằng AI Copilot không thay thế IT Operations, mà nó là công cụ tăng sức mạnh (multiplier). Dùng hình ảnh: Nó giống như Iron Man có J.A.R.V.I.S. Người quyết định vẫn là Tony Stark, nhưng J.A.R.V.I.S xử lý dữ liệu thô và cảnh báo nguy hiểm trong tích tắc.

---
