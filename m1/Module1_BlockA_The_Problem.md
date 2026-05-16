# Module 1 — Block A: The Problem (Slides 1–5)

**Block:** A — Tại sao cần AI?
**Slides:** 1–5
**Status:** Draft — Chờ duyệt
**Sources:** Day1_Lecture_Notes.md, Module1_Source_CSAI2025.md, update_module1.md

---

Slide 1: Giới thiệu Module 1


# Module 1: Tổng quan về AI trong An ninh mạng & Bức tranh Mối đe dọa 2026

**Khóa học:** Cyber Security Artificial Intelligence (CSAI) 2026
**Đối tượng:** Chuyên viên vận hành IT, Quản trị hệ thống, Kỹ sư mạng

**Bạn sẽ nắm được sau Module này:**
- Tại sao bảo mật truyền thống không còn đủ mạnh
- AI đang thay đổi cuộc chiến an ninh mạng như thế nào
- Những mối đe dọa mới nhất của năm 2026 mà bạn PHẢI biết


💡 **Note:** Chào mừng học viên, tạo không khí thoải mái. Nhấn mạnh rằng khóa học không yêu cầu nền tảng AI/ML — mục tiêu là giúp IT Operations *sử dụng* AI như một công cụ, không phải trở thành nhà nghiên cứu. Hỏi nhanh: "Ai trong phòng đang phải đọc log thủ công mỗi ngày?" để khởi động thảo luận.

---

Slide 2: Case Study Mở Đầu — Vụ Lừa Đảo Deepfake $25.6 Triệu USD

```markdown
# 🚨 Chuyện Thật Xảy Ra: Hồng Kông, 2024

**Công ty:** Arup — Tập đoàn kỹ thuật đa quốc gia hàng đầu thế giới

**Chuyện gì đã xảy ra?**
- Một nhân viên tài chính nhận lệnh từ "CFO" qua video call
- Cuộc họp có đủ mặt: CFO, đồng nghiệp — tất cả trông và nghe rất thật
- Nhân viên chuyển khoản **$25.6 triệu USD** theo lệnh

**Sự thật:** Toàn bộ "đồng nghiệp" là **Deepfake** — AI tạo sinh giả mạo
theo thời gian thực (real-time audio & video cloning)

**Bài học cốt lõi:**
- Xác thực bằng mắt và tai của con người đã **thất bại hoàn toàn**
- Quy trình thủ công không thể chống lại AI tấn công
```

💡 **Note:** Đây là "The Hook" — hãy kể câu chuyện này như một tình huống thực, không vội đưa ra giải pháp ngay. Mục tiêu là tạo cảm giác "điều này CÓ THỂ xảy ra tại tổ chức của tôi". Hỏi học viên: "Nếu CFO của bạn gọi video và yêu cầu chuyển tiền gấp — bạn sẽ làm gì để xác minh?" Để câu hỏi treo lơ lửng, trả lời ở cuối module.

---

Slide 3: Bức Tranh Mối Đe Dọa 2026 — Quy Mô Chóng Mặt

```markdown
# Thực Tế Của Chiến Trường An Ninh Mạng

**Khối lượng tấn công (Volume):**
- Doanh nghiệp lớn tạo ra hàng **tỷ sự kiện bảo mật mỗi giờ**
- 450,000 mẫu **Malware** mới được phát hiện mỗi ngày
- Mỗi SOC analyst xử lý ~174 cảnh báo/ngày — 52% là **False Positive**

**Tốc độ tấn công (Speed):**
- **Malware** lan truyền: tính bằng **mili-giây**
- Phát hiện thủ công: tính bằng **giờ đến ngày**

**Độ phức tạp (Complexity):**
- Kẻ tấn công dùng **AI** để tạo ra các cuộc tấn công chưa từng có
- **Polymorphic Malware** tự thay đổi mã để qua mặt chữ ký (signature)
```

💡 **Note:** Nhấn mạnh sự bất cân xứng giữa tốc độ tấn công và tốc độ phản ứng của con người. Hỏi học viên: "Nếu mỗi ngày có 174 cảnh báo, và một nửa là báo động giả — bạn có còn tin tưởng vào từng cảnh báo không?" Đây là "Alert Fatigue" — vấn đề thực tế mà phần lớn IT Operations đang gặp phải.

---

Slide 4: Tại Sao Bảo Mật Truyền Thống Không Còn Đủ Mạnh?

```markdown
# Hai Thế Giới: Truyền Thống vs. AI

| Tiêu chí | Bảo mật Truyền thống | Bảo mật với AI |
|----------|----------------------|----------------|
| **Cơ chế** | Dựa trên quy tắc (Rule-based) | Dựa trên hành vi (Behavior-based) |
| **Phản ứng** | Thụ động — đợi tấn công xảy ra | Chủ động — phát hiện trước |
| **Phát hiện** | Chỉ biết mối đe dọa **đã biết** | Phát hiện mối đe dọa **chưa từng thấy** |
| **Khả năng mở rộng** | Giới hạn bởi số lượng analyst | Không giới hạn — tự động hóa |
| **Xử lý log** | ~100 sự kiện/ngày/người | Hàng tỷ sự kiện/giờ |

**Kết luận:** Kẻ tấn công đã dùng AI từ lâu.
Câu hỏi không phải là "Có nên dùng AI không?" mà là "Dùng AI như thế nào?"
```

💡 **Note:** Dùng phép so sánh quen thuộc với IT Operations: "Bảo mật chữ ký (Signature) giống như kiểm tra CCCD — chỉ hiệu quả nếu giấy tờ chưa bị làm giả. Bảo mật hành vi (Behavior) giống như quan sát người đó hành xử trong văn phòng — dù họ có giấy tờ thật, nhưng nếu lẻn vào phòng server lúc 3 giờ sáng thì vẫn bị gắn cờ."

---

Slide 5: CIA Triad — Nền Tảng Của Mọi Tư Duy Bảo Mật

```markdown
# Ba Trụ Cột: Confidentiality — Integrity — Availability

**🔒 Confidentiality (Bảo mật thông tin)**
Thông tin chỉ được truy cập bởi người có thẩm quyền
→ Ví dụ: Mã hóa dữ liệu, phân quyền truy cập

**✅ Integrity (Toàn vẹn dữ liệu)**
Dữ liệu không bị thay đổi trái phép trong quá trình lưu trữ hoặc truyền tải
→ Ví dụ: Hash verification, digital signature

**⚡ Availability (Tính sẵn sàng)**
Hệ thống luôn hoạt động khi được cần đến
→ Ví dụ: Chống DDoS, backup & recovery

**Kẻ tấn công luôn nhắm vào ít nhất một trong ba trụ cột này.**
AI giúp chúng ta bảo vệ cả ba cùng một lúc.
```

💡 **Note:** CIA Triad là ngôn ngữ chung của toàn ngành — học viên sẽ nghe lại bộ ba này suốt 5 ngày. Lấy ví dụ vụ Arup ở Slide 2 để phân tích: tấn công đó vi phạm trụ cột nào? (Đáp án: Confidentiality — tiền bị chuyển cho người không có thẩm quyền; Integrity — danh tính CFO bị giả mạo). Điều này giúp học viên thấy CIA Triad không chỉ là lý thuyết.

---
