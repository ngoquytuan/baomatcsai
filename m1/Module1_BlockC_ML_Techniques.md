# Module 1 — Block C: ML Techniques Survey (Slides 11–14)

**Block:** C — Các Kỹ Thuật ML Chính Trong Bảo Mật
**Slides:** 11–14
**Status:** Draft — Chờ duyệt
**Sources:** Day1_Lecture_Notes.md, Module1_Source_CSAI2025.md, update_module1.md

> Block C là khảo sát nhanh 4 nhóm kỹ thuật chính — mỗi nhóm sẽ được học sâu hơn
> trong các module tương ứng (Day 2–5). Mục tiêu ở đây là học viên nhận ra tên và
> biết ứng dụng bảo mật, không cần hiểu toán học.

---

Slide 11: NLP & Transformers — Khi AI Đọc Hiểu Ngôn Ngữ Con Người

```markdown
# NLP: Vũ Khí Chống Phishing & Threat Intelligence

**Natural Language Processing (NLP) là gì?**
Giúp máy tính đọc hiểu ngôn ngữ con người — email, log, lệnh command line

**Ứng dụng bảo mật thực tế:**
→ **Phát hiện Phishing:** Phân tích từ ngữ đáng ngờ ("khẩn cấp", "xác minh ngay")
→ **Threat Intelligence:** AI đọc 10,000 báo cáo bảo mật mỗi ngày, tự trích xuất IOC
→ **Dark Web Monitoring:** Theo dõi các diễn đàn hacker tự động

**Transformers (BERT, CodeBERT) — Thế hệ NLP hiện đại:**
Hiểu được **ngữ cảnh** của từng từ — phát hiện các biến thể Phishing tinh vi
mà bộ lọc từ khóa thông thường bỏ qua

**Lab 1 của khóa này sẽ dùng kỹ thuật này để phân loại email Phishing.**
```

💡 **Note:** Kết nối trực tiếp với Lab 1 (Day 1 chiều) để học viên thấy lý do thực hành. Ví dụ minh họa: bộ lọc từ khóa cũ sẽ bị qua mặt khi hacker viết "V-E-R-I-F-Y a-c-c-o-u-n-t" thay vì "VERIFY account" — trong khi Transformer hiểu ngữ cảnh nên vẫn phát hiện được. Hỏi: "Bộ lọc email của tổ chức bạn đang dùng phương pháp nào?"

---

Slide 12: Decision Tree & Random Forest — AI Có Thể Giải Thích

```markdown
# Decision Tree: AI "Nói Cho Bạn Biết Tại Sao"

**Decision Tree (Cây Quyết Định):**
Chuỗi câu hỏi Yes/No dẫn đến kết luận — giống sơ đồ luồng xử lý

```
Số lần đăng nhập thất bại > 5?
├─ Có → Từ nhiều quốc gia khác nhau?
│       ├─ Có → 🚨 CẢNH BÁO: Brute Force
│       └─ Không → 👀 Theo dõi thêm
└─ Không → ✅ Cho qua
```

**Tại sao quan trọng với IT Operations?**
→ Kết quả **có thể giải thích** — bạn biết rõ AI quyết định dựa trên gì
→ Dễ kiểm tra và tinh chỉnh khi có false positive

**Random Forest:** Kết hợp hàng trăm Decision Tree — độ chính xác >95%
trong phát hiện xâm nhập mạng (Network Intrusion Detection)
```

💡 **Note:** Nhấn mạnh giá trị "Explainable AI" — trong môi trường doanh nghiệp, bộ phận bảo mật cần giải thích với quản lý tại sao một tài khoản bị chặn. Decision Tree cho phép làm điều đó. Hỏi: "Nếu AI chặn tài khoản của CEO lúc 6 giờ sáng — bạn cần giải thích gì với sếp?" Đây là lý do Explainable AI quan trọng hơn độ chính xác thuần túy.

---

Slide 13: Anomaly Detection — Phát Hiện Bất Thường Không Cần Nhãn

```markdown
# Anomaly Detection: Tìm "Cái Gì Đó Khác Thường"

**Vấn đề cốt lõi:**
Với các mối đe dọa mới (Zero-day, Insider Threat) — không có nhãn "tốt/xấu"
→ Không thể dùng Supervised Learning
→ Cần AI tự định nghĩa "bình thường" rồi phát hiện sai lệch

**Cách hoạt động:**
1. AI học hành vi bình thường trong 2–4 tuần (baseline)
2. Mọi hoạt động sau đó được so sánh với baseline
3. Độ lệch vượt ngưỡng → Cảnh báo

**Ví dụ thực tế:**
→ Nhân viên thường làm việc 8:00–17:00 → Đăng nhập lúc 3:00 sáng = **Bất thường**
→ Server thường dùng 20% CPU → Đột ngột 95% liên tục = **Bất thường (Cryptomining?)**

**Isolation Forest** là thuật toán phổ biến nhất — Lab 2 (Day 2) sẽ dùng kỹ thuật này.
```

💡 **Note:** Kỹ thuật này trực tiếp liên quan đến công việc hàng ngày của IT Operations — monitoring CPU, network traffic, login patterns. Hỏi: "Bạn có ngưỡng cảnh báo CPU không? Ngưỡng đó được đặt dựa trên gì — cảm tính hay dữ liệu lịch sử?" AI thay thế "cảm tính" bằng baseline thống kê tự động. Không cần giải thích Isolation Forest chi tiết — Day 2 sẽ có lab thực hành.

---

Slide 14: Clustering — Nhóm Hành Vi, Phát Hiện Kẻ Lạ

```markdown
# Clustering: Khi AI Tự Phân Nhóm Không Cần Chỉ Dẫn

**Clustering (Phân cụm) là gì?**
AI tự nhóm các đối tượng tương tự nhau lại — không cần nhãn trước

**Ứng dụng bảo mật:**

**User Behavior Analytics (UBA):**
→ Nhóm nhân viên theo hành vi: giờ làm việc, lượng dữ liệu tải về, ứng dụng dùng
→ Người nằm ngoài nhóm của mình = **Nghi vấn Insider Threat**

**Network Traffic Clustering:**
→ Nhóm các luồng mạng theo pattern
→ Luồng không thuộc nhóm nào = **Nghi vấn Command & Control (C2)**

**Thuật toán phổ biến:**
- **K-Means:** Chia thành K nhóm cố định — Lab 5 (Day 5) sẽ dùng
- **DBSCAN:** Tự tìm nhóm theo mật độ — phát hiện outlier tốt hơn

**Không cần biết trước "mối đe dọa là gì" — chỉ cần phát hiện "cái khác biệt".**
```

💡 **Note:** Dùng ví dụ nhân sự quen thuộc: "Hãy tưởng tượng 100 nhân viên được phân thành 5 nhóm theo giờ làm việc và lượng email gửi. Nếu một người trong nhóm 'nhân viên văn phòng bình thường' đột ngột hành xử như nhóm 'quản lý cấp cao với quyền truy cập rộng' — AI sẽ gắn cờ ngay." Kết nối với Lab 5 để học viên biết kỹ thuật này sẽ được thực hành ở cuối khóa.

---
