Dưới đây là **danh sách mới các bài thực hành** đã được điều chỉnh lại để:

- **Đơn giản, dễ làm cho người mới học AI**,
- **Bám sát lý thuyết và tình huống thực tế thường gặp trong vận hành hệ thống IT**,
- Bao gồm **cả thao tác thủ công lẫn dùng AI để xử lý cùng tình huống**,
- **Tránh lặp lại công cụ**, nhưng vẫn sử dụng **Python là công cụ chính**.

---

## **DAY 1 – Foundational Awareness and AI Threat Detection**

**Thực hành (2–3 giờ):**

- **Tình huống:** Một người dùng nhận được email khả nghi chứa link lạ.
- **Phần 1 – Thủ công:**
  - Xem tiêu đề, địa chỉ gửi, nội dung HTML – xác định dấu hiệu phishing bằng checklist.
- **Phần 2 – Có AI hỗ trợ:**
  - Sử dụng Python để kiểm tra email với từ điển blacklist + các keyword nghi vấn.
  - Áp dụng **TF-IDF + Naïve Bayes** để phát hiện spam/phishing.
- **Công cụ:** `scikit-learn`, `pandas`, `matplotlib`

✅ **Phù hợp hoàn toàn cho người mới, không yêu cầu web hay GAN.**

---

## **DAY 2 – Python & Log-based Attack Detection**

**Thực hành (2–3 giờ):**

- **Tình huống:** Một máy chủ ghi nhận log bất thường truy cập SSH.
- **Phần 1 – Thủ công:**
  - Phân tích log mẫu từ `auth.log` hoặc log SSH – tìm pattern IP sai nhiều lần.
- **Phần 2 – Có AI hỗ trợ:**
  - Dùng Python để parse log, trích xuất địa chỉ IP, tần suất truy cập.
  - Áp dụng **Isolation Forest** để xác định truy cập bất thường.
- **Công cụ:** `pandas`, `re`, `sklearn`

✅ **Phù hợp với nhân sự vận hành, dùng log thật, không yêu cầu kiến thức web.**

---

## **DAY 3 – Anomaly in System Behavior**

**Thực hành (2–3 giờ):**

- **Tình huống:** Một hệ thống dịch vụ nội bộ bị chậm bất thường.
- **Phần 1 – Thủ công:**
  - Vẽ biểu đồ thời gian tải CPU/mạng để xác định khoảng thời gian bất thường.
- **Phần 2 – Có AI hỗ trợ:**
  - Dùng **Time Series Decomposition + Statsmodels** để phát hiện đột biến.
- **Công cụ:** `matplotlib`, `statsmodels`, `seaborn`

✅ **Không yêu cầu ML nâng cao, chỉ cần trực quan hoá và hiểu pattern.**

---

## **DAY 4 – Email and File-based Malware Incidents**

**Thực hành (2–3 giờ):**

- **Tình huống:** Người dùng mở một tập tin `.exe` nghi ngờ bị nhiễm malware.
- **Phần 1 – Thủ công:**
  - Kiểm tra metadata, hash file, dấu hiệu đáng ngờ từ chuỗi trong file (dùng `strings`).
- **Phần 2 – Có AI hỗ trợ:**
  - Áp dụng mô hình **Decision Tree** để phân loại file “tốt/xấu” dựa trên đặc trưng đơn giản (kích thước, entropy, hành vi file...).
- **Công cụ:** `scikit-learn`, `hashlib`, `pandas`, `os`

✅ **Không dùng pentest hay phân tích PE phức tạp, phù hợp IT vận hành.**

---

## **DAY 5 – Network Activity and User Behavior Monitoring**

**Thực hành (2–3 giờ):**

- **Tình huống:** Một người dùng có hoạt động bất thường trên mạng nội bộ.
- **Phần 1 – Thủ công:**
  - Xem traffic log, thống kê lượt truy cập ra ngoài giờ hành chính, truy cập bất thường.
- **Phần 2 – Có AI hỗ trợ:**
  - Gán điểm **Reputation Scoring** cho user dựa trên mô hình chuẩn hành vi.
  - Dùng **k-means hoặc scoring rule** để nhóm user “bình thường” và “khác thường”.
- **Công cụ:** `pandas`, `sklearn`, `matplotlib`

✅ **Giúp IT hiểu cách giám sát hành vi người dùng mà không cần code AI phức tạp.**

---

## **Tổng kết**

| Ngày  | Tình huống mô phỏng | AI áp dụng                | Có thủ công không? | Phù hợp người mới? |
|-------|---------------------|---------------------------|--------------------|--------------------|
| Day 1 | Phishing Email      | Naïve Bayes + TF-IDF      | ✅ Có               | ✅                  |
| Day 2 | SSH brute-force     | Isolation Forest          | ✅ Có               | ✅                  |
| Day 3 | Tăng tải hệ thống   | Time Series Decomposition | ✅ Có               | ✅                  |
| Day 4 | Tập tin độc hại     | Decision Tree             | ✅ Có               | ✅                  |
| Day 5 | Hành vi người dùng  | Scoring + Clustering      | ✅ Có               | ✅                  |

---

Nếu bạn cần, tôi có thể tiếp tục viết các **bộ dữ liệu mẫu cho từng bài** và **lab instruction từng bước** hoặc **notebook mẫu** để giảng viên hoặc học viên sử dụng. Bạn có muốn tôi bắt đầu tạo ví dụ cho bài thực hành Day 1 trước không?