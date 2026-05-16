# Module 1 — Block E: 2026 Threat Update (Slides 19–22)

**Block:** E — Cập Nhật Bức Tranh Mối Đe Dọa 2026
**Slides:** 19–22
**Status:** Draft — Chờ duyệt
**Sources:** Day1_Lecture_Notes.md, update_module1.md

---

Slide 19: Adversarial AI — Khi Hacker Tấn Công Bằng AI

```markdown
# Adversarial AI: Cuộc Chạy Đua Vũ Trang

**Kẻ tấn công không chịu thua — chúng dùng chính AI để tấn công lại hệ thống AI:**

**1. Data Poisoning (Đầu độc dữ liệu)**
→ Can thiệp vào quá trình huấn luyện của AI
→ Mục tiêu: Làm cho AI nhận diện sai (ví dụ: gán nhãn malware thành file sạch)

**2. Adversarial Examples (Ví dụ đối kháng)**
→ Chỉnh sửa mã độc ở mức cực nhỏ (mắt thường không thấy)
→ Mục tiêu: Đánh lừa mô hình phân loại (ví dụ: DeepLocker malware tự ẩn mình cho đến khi gặp đúng mục tiêu)

**3. AI-Powered Attacks**
→ Tự động quét lỗ hổng nhanh hơn con người
→ Sử dụng AI để tự động đoán mật khẩu (Password cracking)
```

💡 **Note:** Giải thích "Data Poisoning" bằng ví dụ: Nếu bạn dạy một đứa trẻ (AI) rằng quả táo gọi là "quả cam" liên tục trong 1 năm, nó sẽ học sai. Hacker làm điều tương tự với dữ liệu log hệ thống để AI bảo mật bỏ qua các hành vi độc hại.

---

Slide 20: Phishing Thế Hệ Mới & Deepfake BEC

```markdown
# Lừa Đảo Siêu Cá Nhân Hóa & Giả Mạo Danh Tính

**Từ Spam đại trà đến lừa đảo "đo ni đóng giày":**
- Hacker dùng Large Language Models (LLMs) tự động viết email chuẩn giọng điệu của đối tác/sếp.
- Cào dữ liệu từ LinkedIn, mạng xã hội để tạo bối cảnh tin cậy tuyệt đối.

**Deepfake BEC (Business Email Compromise):**
- Trở lại **Vụ án Arup $25.6M** (Hồng Kông, 2024)
- Không chỉ giả email, AI tạo sinh nhân bản cả **Giọng nói (Voice cloning)** và **Hình ảnh (Video Deepfake)** theo thời gian thực.
- Xác thực bằng "gọi điện thoại xác nhận lại" không còn an toàn 100%.

**Bài học:** Yêu cầu xác thực đa yếu tố (MFA) và quy trình duyệt chi độc lập (Out-of-band confirmation).
```

💡 **Note:** Nối lại câu chuyện "The Hook" ở Slide 2. Trả lời câu hỏi: Làm sao để ngăn chặn vụ Arup? Giải pháp không nằm ở việc "nhìn kỹ hơn" vì Deepfake sẽ ngày càng hoàn hảo. Giải pháp nằm ở "Out-of-band confirmation" (xác nhận qua một kênh khác độc lập) và quy trình nội bộ chặt chẽ.

---

Slide 21: Prompt Injection & Zero-Click Attack

```markdown
# Prompt Injection: Tấn Công Trực Tiếp Vào "Não" AI

**Prompt Injection (Tiêm lệnh) là gì?**
→ Kẻ tấn công lồng ghép chỉ thị độc hại vào dữ liệu đầu vào.
→ Thay vì hack hệ thống, hacker "thuyết phục" AI tự làm việc xấu.

**Sự cố EchoLeak (CVE-2025-32711) — Zero-click attack:**
- Nạn nhân đang dùng **Microsoft 365 Copilot**.
- Kẻ tấn công gửi một email chứa mã lệnh ẩn (Indirect Prompt Injection).
- Copilot tự động tóm tắt email → "vô tình" đọc trúng mã lệnh độc.
- Copilot tự động gửi dữ liệu nhạy cảm của nạn nhân ra ngoài.
- **Nạn nhân KHÔNG CẦN click vào bất kỳ link nào.**
```

💡 **Note:** Slide cực kỳ quan trọng cho bối cảnh 2026. "Zero-click" là từ khóa làm IT Operations sợ nhất vì người dùng không hề mắc lỗi (không click link lạ) mà vẫn bị hack do AI tự động đọc thay. Đây là rủi ro của việc tích hợp AI Copilots vào Workflow.

---

Slide 22: "Bộ Ba Chết Chóc" (Lethal Trifecta)

```markdown
# Quy Tắc Thiết Kế AI An Toàn: The Lethal Trifecta

Theo nguyên tắc của Simon Willison, tuyệt đối không để một AI Agent **đồng thời** sở hữu cả 3 quyền sau:

1. 📩 **Quyền đọc dữ liệu không tin cậy** (Ví dụ: Email từ Internet, nội dung Website)
2. 🔑 **Quyền truy cập dữ liệu nhạy cảm** (Ví dụ: Tài liệu nội bộ, quyền quản trị)
3. 🚀 **Quyền thực hiện hành động ra bên ngoài** (Ví dụ: Gửi email, gọi API)

**Nếu AI Agent có đủ cả 3:**
→ Kẻ tấn công chỉ cần gửi 1 email độc hại (1)
→ AI sẽ đọc, bị chiếm quyền, tự lấy dữ liệu nhạy cảm (2)
→ Và tự động tuồn dữ liệu đó ra ngoài (3) (Giống hệt vụ EchoLeak).
```

💡 **Note:** Đây là kiến thức "must-have" (bắt buộc) khi triển khai AI nội bộ. Yêu cầu học viên ghi nhớ "Bộ ba chết chóc" này. Nếu tổ chức của họ muốn làm một AI Chatbot đọc email khách hàng, họ phải ngắt quyền (2) hoặc (3) để đảm bảo an toàn. 

---
