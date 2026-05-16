# Module 1 — Block B: AI Foundations (Slides 6–10)

**Block:** B — AI Là Gì & Tại Sao Nó Mạnh?
**Slides:** 6–10
**Status:** Draft — Chờ duyệt
**Sources:** Day1_Lecture_Notes.md, Module1_Source_CSAI2025.md, update_module1.md

---

Slide 6: Hành Trình Của An Ninh Mạng — Từ Khóa Cổng Đến AI

```markdown
# An Ninh Mạng Đã Tiến Hóa Như Thế Nào?

| Thập kỷ | Công nghệ | Giới hạn |
|---------|-----------|----------|
| **1970s** | Mật khẩu cơ bản | Dễ đoán, không mã hóa |
| **1990s** | Firewall & Antivirus | Chỉ chặn mối đe dọa đã biết |
| **2000s** | Intrusion Detection System (IDS) | Tạo quá nhiều cảnh báo giả |
| **2010s** | Advanced Threat Protection | Vẫn phụ thuộc vào chuyên gia phân tích thủ công |
| **2020s** | **AI-powered Security Operations** | ✅ Tự động hóa, phát hiện hành vi bất thường |

**Xu hướng 2026:** Vành đai bảo mật truyền thống đã chết.
Cuộc chiến đã chuyển sang bảo vệ **Workflow, Prompt và Trust Chain**.
```

💡 **Note:** Dùng bảng timeline này để học viên thấy rõ mỗi thế hệ công nghệ giải quyết được vấn đề của thế hệ trước nhưng lại tạo ra lỗ hổng mới. Nhấn mạnh câu cuối — "Vành đai truyền thống đã chết" — đây là thông điệp cốt lõi mới của 2026. Hỏi: "Firewall của bạn có chặn được một email lừa đảo mà CFO gửi không?" (Câu trả lời: Không — vì email đến từ tài khoản hợp lệ bị chiếm quyền).

---

Slide 7: AI Là Gì? — Phân Cấp Quan Trọng Nhất Bạn Cần Biết

```markdown
# AI ⊃ Machine Learning ⊃ Deep Learning

**🤖 Artificial Intelligence (AI — Trí tuệ nhân tạo)**
Hệ thống máy tính thực hiện các tác vụ thường đòi hỏi trí tuệ con người
→ Nhận diện mẫu, ra quyết định, học từ kinh nghiệm

**📊 Machine Learning (ML — Học máy)** ← Tập con của AI
Thuật toán tự cải thiện thông qua dữ liệu — không cần lập trình từng rule
→ Ví dụ: Cho AI xem 10,000 email spam → AI tự học cách nhận diện spam mới

**🧠 Deep Learning (Học sâu)** ← Tập con của ML
Mạng nơ-ron nhân tạo nhiều lớp — cực mạnh với dữ liệu phức tạp
→ Ví dụ: Nhận diện khuôn mặt, phân tích giọng nói, phân tích mã độc

**Tất cả cùng phục vụ một mục tiêu: Bảo vệ hệ thống của bạn.**
```

💡 **Note:** Tránh đi sâu vào toán học. Hãy dùng ví dụ trực quan: ML giống như dạy một nhân viên mới nhận diện email đáng ngờ bằng cách cho họ xem hàng ngàn ví dụ — thay vì viết sổ tay quy trình dày 200 trang. Deep Learning là phiên bản nhân viên đó sau 10 năm kinh nghiệm, tự nhận ra các dấu hiệu mà ngay cả quản lý cũng không để ý.

---

Slide 8: Ba Cách Máy Tính Học — Tổng Quan Nhanh

```markdown
# Ba Phương Pháp Machine Learning Chính

**1️⃣ Supervised Learning (Học có giám sát)**
Học từ dữ liệu đã được gán nhãn
→ Ứng dụng: Phát hiện **Malware**, lọc **Spam**, phân loại **Phishing**

**2️⃣ Unsupervised Learning (Học không giám sát)**
Tự tìm ra các nhóm và pattern ẩn — không cần nhãn có sẵn
→ Ứng dụng: Phát hiện hành vi bất thường, insider threat

**3️⃣ Reinforcement Learning (Học tăng cường)**
Học qua thử và sai — nhận "phần thưởng" khi hành động đúng
→ Ứng dụng: Tự động phản ứng sự cố, tối ưu chiến lược phòng thủ

**Cả 3 đang được dùng trong các hệ thống bảo mật hiện đại.**
```

💡 **Note:** Dùng ví dụ đời thường cho từng loại: (1) Supervised = học sinh ôn thi từ đề mẫu có đáp án; (2) Unsupervised = thám tử tự nhóm các manh mối lạ mà không có hướng dẫn; (3) Reinforcement = game thủ luyện tập đến khi thành thạo bằng cách thất bại và rút kinh nghiệm. Không cần học viên hiểu chi tiết kỹ thuật ở đây — mục tiêu là nhận ra ứng dụng bảo mật của mỗi loại.

---

Slide 9: Generative AI — Bước Đột Phá Làm Thay Đổi Cuộc Chơi

```markdown
# AI Không Chỉ "Phân Loại" — Nó Còn Có Thể "Tạo Ra"

**AI Truyền thống (Phân loại — Discriminative):**
Nhìn vào email → Phán: "Đây là Phishing" ✓ hoặc ✗

**Generative AI — AI Tạo Sinh (MỚI 2026):**
→ Tự tạo ra email **Phishing** thuyết phục hơn bao giờ hết
→ Tự viết mã **Malware** chưa từng tồn tại trước đó
→ Tạo giọng nói, khuôn mặt **Deepfake** theo thời gian thực

**Phía phòng thủ — AI Security Copilots:**
- **Microsoft Security Copilot** — phân tích hàng tỷ sự kiện bảo mật mỗi giờ
- **Google Security AI Workbench** — tự động tóm tắt và ưu tiên hóa cảnh báo

**⚠️ Cùng một công nghệ — phục vụ cả tấn công lẫn phòng thủ.**
```

💡 **Note:** Đây là slide then chốt để học viên hiểu tại sao 2026 khác với 2020. Nhấn mạnh: trước đây AI chỉ "nhận diện", nay AI còn "sáng tạo" — điều đó có nghĩa kẻ tấn công không còn cần kỹ năng lập trình cao. Một prompt đơn giản có thể tạo ra email lừa đảo cá nhân hóa hoàn hảo cho từng nạn nhân. Hỏi: "Nếu AI có thể viết email lừa đảo nghe như sếp bạn — bộ lọc spam truyền thống có chặn được không?"

---

Slide 10: Agentic AI — Khi AI Tự Mình Hành Động

```markdown
# Agentic AI (AI Tự Hành) — Mối Đe Dọa & Cơ Hội Mới Nhất

**Agentic AI là gì?**
AI không chỉ trả lời câu hỏi — nó **tự lập kế hoạch và thực hiện hành động**
→ Đọc email → Tìm kiếm web → Gửi email trả lời → Tạo báo cáo... tự động

**Ứng dụng phòng thủ (tốt):**
→ AI Agent tự điều tra cảnh báo → tóm tắt → đề xuất hành động khắc phục
→ Giảm thời gian phản ứng từ hàng giờ xuống còn vài phút

**⚠️ Rủi ro bảo mật (nguy hiểm — Prompt Injection):**
→ Kẻ tấn công nhúng lệnh độc hại vào nội dung AI đọc
→ AI Agent bị "bắt cóc" — thực hiện lệnh của hacker thay vì chủ nhân

**Ví dụ thực chiến 2026 — EchoLeak (CVE-2025-32711):**
Microsoft 365 Copilot tự đọc email chứa prompt độc hại
và tự tuồn dữ liệu ra ngoài — không cần người dùng click gì cả.
```

💡 **Note:** Đây là ví dụ "zero-click attack" đầu tiên nhắm vào AI Agent — CVE-2025-32711 là lỗ hổng thực, đã được vá. Nhấn mạnh: đây không phải khoa học viễn tưởng. Hỏi học viên: "Tổ chức của bạn có đang dùng Microsoft 365 Copilot hoặc công cụ AI tương tự không?" — nếu có, đây là rủi ro cần được hiểu rõ ngay hôm nay.

---
