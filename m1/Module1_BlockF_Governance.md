# Module 1 — Block F: Governance & Ethics (Slides 23–24)

**Block:** F — Quản Trị & Khung Pháp Lý AI
**Slides:** 23–24
**Status:** Draft — Chờ duyệt
**Sources:** update_module1.md

---

Slide 23: Tuân Thủ Pháp Lý & Tiêu Chuẩn Vận Hành AI

```markdown
# AI Security: Từ Tự Nguyện Sang Bắt Buộc

**Kỷ nguyên tự do phát triển AI đã kết thúc. 2026 là năm của tuân thủ:**

**1. EU AI Act (Đạo luật AI Châu Âu)**
→ Phân loại rủi ro AI (Cấm hoàn toàn, Nguy cơ cao, Tiêu chuẩn).
→ Bắt buộc với mọi tổ chức có liên kết với dữ liệu công dân EU.

**2. NIST AI Risk Management Framework (AI RMF)**
→ Khung quản lý rủi ro AI của Mỹ.
→ Tiêu chuẩn vận hành thực tế cho các hệ thống AI an toàn, minh bạch.

**3. MITRE ATLAS v5.1.0**
→ Ma trận chiến thuật tấn công dành riêng cho AI (Tương tự MITRE ATT&CK).
→ Bắt buộc phải dùng để Threat Modeling (mô hình hóa mối đe dọa) cho AI.
```

💡 **Note:** Nhấn mạnh sự chuyển dịch: Trước đây bảo mật AI là "Nice to have" (có thì tốt), bây giờ nó là "Must have" (bắt buộc theo luật). Nếu công ty triển khai AI mà không rà soát theo MITRE ATLAS, họ có thể vi phạm pháp luật nếu xảy ra rò rỉ dữ liệu.

---

Slide 24: OWASP Top 10 for Agentic Apps

```markdown
# Các Lỗ Hổng Phổ Biến Nhất Của AI Agent

Dự án OWASP đã cập nhật bộ tiêu chuẩn dành riêng cho AI tự hành (Agentic Apps):

**Nguy cơ số 1: Agent Goal Hijacking (Đánh cắp mục tiêu)**
→ Hacker dùng Prompt Injection để thay đổi mục tiêu ban đầu của Agent.
→ Ví dụ: Chuyển từ "Hỗ trợ khách hàng" sang "Lấy cắp thông tin thẻ tín dụng của khách hàng".

**Các nguy cơ cốt lõi khác:**
- **Data Leakage:** AI học dữ liệu nhạy cảm và vô tình tiết lộ cho người dùng khác.
- **Insecure Output Handling:** Hệ thống mù quáng thực thi mã lệnh do AI tạo ra mà không có cơ chế kiểm duyệt (Sandbox).

**Bảo mật AI là bảo vệ sự trung thành của AI đối với chủ nhân.**
```

💡 **Note:** OWASP Top 10 là tiêu chuẩn mà mọi dân IT đều biết. Khi OWASP ra mắt phiên bản riêng cho Agentic Apps, điều đó chứng tỏ rủi ro từ AI đã trở thành một nhánh bảo mật độc lập. Khuyên học viên tìm hiểu tài liệu này nếu tổ chức sắp build Chatbot nội bộ.

---
