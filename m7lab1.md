# 📊 BÀI THỰC HÀNH: XÂY DỰNG MÔ HÌNH ML PHÁT HIỆN HÀNH VI BẤT THƯỜNG

---

## SLIDE 1: THÔNG TIN BÀI HỌC

**Module:** 7 - User Authentication Security With AI

**Bài Lab:** Lab 1 - Risk Score Prediction

**Thời lượng:** 90 phút

**Mục tiêu:**
- Hiểu cách xác định features cho bài toán security
- Biết cách thu thập và xử lý dữ liệu raw
- Tạo được dataset training và test set chất lượng
- Tránh được data leakage
- Huấn luyện và so sánh các thuật toán ML

---

## SLIDE 2: TÌNH HUỐNG THỰC TẾ

**Bạn là Security Engineer tại công ty fintech**

**Thực trạng:**
- Hàng triệu lần đăng nhập mỗi ngày
- 99% là người dùng thật
- 1% là hacker cố gắng xâm nhập

**Vấn đề:**
- Không thể kiểm tra thủ công từng login
- Rule-based system quá cứng nhắc, dễ bypass
- Cần hệ thống AI tự động phát hiện

**Yêu cầu:**
- Độ chính xác cao (>90%)
- Nhanh (dưới 100ms)
- Ít false positive (không làm phiền user)
- Không bỏ sót hacker (recall cao)

---

## SLIDE 3: BƯỚC 1 - XÁC ĐỊNH FEATURES

**Câu hỏi đầu tiên:**
"Làm thế nào BẠN nhận biết login bất thường?"

**Ví dụ thực tế:**
Facebook thông báo: "Có người đăng nhập tài khoản bạn từ Nga lúc 3h sáng"

→ Bạn biết ngay đó không phải mình!

**Tại sao?**

---

## SLIDE 4: PHÂN TÍCH TƯ DUY CON NGƯỜI

**1. Thời gian (Temporal)**
- Giờ nào trong ngày?
- Ngày thường hay cuối tuần?
- Có phải giờ làm việc không?

**Ví dụ:**
- ✅ Bình thường: Login lúc 9h sáng thứ 2
- ❌ Bất thường: Login lúc 3h sáng Chủ nhật

---

## SLIDE 5: PHÂN TÍCH TƯ DUY CON NGƯỜI (tt)

**2. Địa điểm (Location)**
- IP từ đâu?
- Quốc gia nào?
- Có đổi vị trí đột ngột không?

**Ví dụ:**
- ✅ Bình thường: Hà Nội → Hà Nội
- ❌ Bất thường: Hà Nội → Nga trong 5 phút

---

## SLIDE 6: PHÂN TÍCH TƯ DUY CON NGƯỜI (tt)

**3. Thiết bị (Device)**
- Thiết bị cũ hay mới?
- Trình duyệt gì?
- Hệ điều hành gì?

**Ví dụ:**
- ✅ Bình thường: Dùng iPhone như mọi khi
- ❌ Bất thường: Đột ngột chuyển sang Android lạ

---

## SLIDE 7: PHÂN TÍCH TƯ DUY CON NGƯỜI (tt)

**4. Hành vi (Behavior)**
- Tốc độ gõ phím?
- Pattern di chuột?
- Cách tương tác?

**Ví dụ:**
- ✅ Bình thường: Gõ 60-80 ký tự/phút
- ❌ Bất thường: Gõ 150 ký tự/phút (bot?)

---

## SLIDE 8: PHÂN TÍCH TƯ DUY CON NGƯỜI (tt)

**5. Lịch sử (Historical)**
- Đã đăng nhập sai mấy lần?
- Bao lâu chưa đăng nhập?
- Login bao nhiêu lần/ngày?

**Ví dụ:**
- ✅ Bình thường: 0 lần sai, login 3-5 lần/ngày
- ❌ Bất thường: 10 lần sai liên tiếp

---

## SLIDE 9: 8 FEATURES CHO BÀI TOÁN

| Feature | Loại | Giá trị | Ý nghĩa |
|---------|------|---------|---------|
| hour | Temporal | 0-23 | Giờ đăng nhập |
| device_change | Device | 0/1 | Có thay thiết bị? |
| country_change | Location | 0/1 | Có thay quốc gia? |
| failed_attempts | Historical | 0-10 | Số lần sai trước đó |
| typing_speed | Behavior | 20-150 | Tốc độ gõ (char/min) |
| session_duration | Behavior | 1-300 | Thời gian session trước (phút) |
| ip_reputation | Location | 0-100 | Điểm uy tín IP |
| login_frequency | Historical | 1-50 | Số lần login trong 24h |

**Label:** 0 = Bình thường, 1 = Bất thường

---

## SLIDE 10: TẠI SAO CHỌN NHỮNG FEATURES NÀY?

**✅ Ưu điểm:**

**1. Dễ thu thập**
- Hầu hết hệ thống đều có sẵn
- Lấy từ logs, headers, database

**2. Có ý nghĩa business rõ ràng**
- Mỗi feature trả lời một câu hỏi cụ thể
- Dễ giải thích cho stakeholders

**3. Khó giả mạo**
- IP reputation: IP xấu đã bị blacklist
- Typing speed: Bot gõ quá nhanh/chậm
- Thời gian: Hacker khó kiểm soát timezone

**4. Không vi phạm privacy**
- Không dùng nội dung chat
- Không dùng thông tin cá nhân nhạy cảm

---

## SLIDE 11: HẠN CHẾ VÀ CÁCH KHẮC PHỤC

| Hạn chế | Giải pháp |
|---------|-----------|
| User đi du lịch → country_change=1 | Thêm "travel mode" hoặc xem khoảng cách |
| User mua máy mới → device_change=1 | Cho phép xác nhận thiết bị mới |
| Gõ phím chậm vì già → typing_speed thấp | Học profile riêng cho từng user |
| VPN/Proxy → IP thay đổi liên tục | Whitelist các VPN hợp pháp |

---

## SLIDE 12: BÀI TẬP TƯ DUY 1

**Câu hỏi:**
Hacker có thể bypass features nào dễ nhất?

**Gợi ý suy nghĩ:**
- hour → Bot có thể chạy đúng giờ làm việc
- typing_speed → Bot có thể simulate
- ip_reputation → Khó bypass (đã bị blacklist)
- country_change → Khó bypass (phải có server ở đó)

---

## SLIDE 13: BÀI TẬP TƯ DUY 2

**Câu hỏi:**
Feature nào quan trọng nhất? Tại sao?

**Trả lời:**
- Không có feature nào "quan trọng nhất"
- ML học **tổ hợp** của các features
- Ví dụ: hour=3 HOẶC country_change=1 → có thể OK
- Nhưng: hour=3 VÀ country_change=1 VÀ device_change=1 VÀ failed_attempts=5 → RẤT NGUY HIỂM!

---

## SLIDE 14: BƯỚC 2 - THU THẬP DỮ LIỆU

**3 nguồn dữ liệu trong thực tế:**

**1. Production Logs (Dữ liệu thật)**
- ✅ Dữ liệu thật, đại diện cho user
- ✅ Volume lớn (hàng triệu records)
- ❌ Cần quyền truy cập
- ❌ Vấn đề privacy/GDPR
- ❌ Ít attack samples (1%)

---

## SLIDE 15: THU THẬP DỮ LIỆU (tt)

**2. Honeypot Data (Bẫy hacker)**
- Hệ thống "giả" để thu hút hacker
- ✅ Nhiều attack samples
- ✅ An toàn (không ảnh hưởng real users)
- ❌ Không có legitimate user data
- ❌ Cần setup và maintain

---

## SLIDE 16: THU THẬP DỮ LIỆU (tt)

**3. Synthetic Data (Dữ liệu tổng hợp)**

**Dùng khi nào?**
- Lab/Training
- Không có quyền truy cập production
- Cần data nhanh để prototype

**Cho lab này:**
→ Chúng ta sẽ dùng Synthetic Data
- Dễ kiểm soát quality
- Reproducible
- Đủ để minh họa concept

---

## SLIDE 17: LOGIC TẠO SAFE LOGIN

**Safe Login Pattern:**
- Giờ: 8AM-6PM (giờ hành chính)
- Device change: 0 (không đổi)
- Country change: 0 (không đổi)
- Failed attempts: 0-1 lần
- Typing speed: 60-85 char/min (bình thường)
- Session duration: 30-120 phút
- IP reputation: 70-100 (IP tốt)
- Login frequency: 1-10 lần/ngày

**Label:** 0 (SAFE)

---

## SLIDE 18: LOGIC TẠO RISKY LOGIN

**Risky Login Pattern:**
- Giờ: 2-5AM, 10PM-midnight (giờ lạ)
- Device change: 80% có đổi
- Country change: 70% có đổi
- Failed attempts: 3-10 lần
- Typing speed: <40 hoặc >120 (bất thường)
- Session duration: 1-20 phút (ngắn)
- IP reputation: 0-30 (IP xấu)
- Login frequency: 20-50 lần/ngày

**Label:** 1 (RISKY)

---

## SLIDE 19: TẠI SAO SAFE LOGIN CÓ PATTERN NHƯ VẬY?

**Giờ: 8AM-6PM**
- Người làm việc login trong giờ hành chính
- Hiếm ai login lúc 2-5h sáng

**Typing speed: 60-85**
- Con người gõ trung bình 60-80 char/min
- Quá nhanh (>120) → bot
- Quá chậm (<40) → không quen thiết bị

**IP reputation: 70-100**
- User thật từ IP nhà/công ty
- IP này có reputation tốt
- Không từ botnet/proxy

---

## SLIDE 20: TẠI SAO RISKY LOGIN KHÁC?

**Giờ: 2-5AM, 10PM-midnight**
- Hacker hoạt động đêm khuya
- Ít người kiểm tra, dễ trốn

**Failed attempts: 3-10**
- Brute-force attack
- Thử nhiều password
- User thật hiếm sai >2 lần

**Login frequency: 20-50**
- Bot login hàng chục lần/ngày
- User thật chỉ 3-5 lần

---

## SLIDE 21: DATASET VỪA TẠO

**Tổng quan:**
- 1000 login records
- 700 Safe (70%)
- 300 Risky (30%)
- 8 features + 1 label

**Files được tạo:**
- logins.csv (1000 records) - Full dataset
- train_split.csv (800 records) - Training
- test_split.csv (200 records) - Testing
- test.csv (20 records) - Demo với mô tả

---

## SLIDE 22: BƯỚC 3 - XÂY DỰNG DATASET

**Dataset gồm 3 phần:**

```
Raw Data (1000 records)
    ↓
├─ Training Set (800 records) → Model HỌC
├─ Validation Set (100 records) → TUNE parameters  
└─ Test Set (100 records) → ĐÁNH GIÁ cuối
```

**Hoặc đơn giản cho lab:**
```
Raw Data (1000 records)
    ↓
├─ Training Set (800 records) → HỌC
└─ Test Set (200 records) → ĐÁNH GIÁ
```

---

## SLIDE 23: NGUYÊN TẮC VÀNG - TRÁNH DATA LEAKAGE!

**Data Leakage là gì?**

**❌ SAI:**
```
Training Set: Sample 1, 2, 3, ..., 800
Test Set:     Sample 1, 2, 3, ..., 200  ← TRÙNG!

→ Model đã "thấy" test data
→ Accuracy giả tạo cao
→ Production sẽ thất bại!
```

**✅ ĐÚNG:**
```
Raw Data (1000): Shuffle random
    ↓
Training: Sample 234, 765, 12, ... (800 unique)
Test:     Sample 999, 3, 456, ...  (200 unique, KHÔNG TRÙNG)

→ Model chưa bao giờ thấy test data
→ Accuracy đáng tin cậy
```

---

## SLIDE 24: CHIA DATASET ĐÚNG CÁCH

**Sử dụng train_test_split**

**Các tham số quan trọng:**
- test_size=0.2 → 20% test, 80% train
- random_state=42 → Reproducible (kết quả giống nhau mỗi lần chạy)
- stratify=y → Giữ tỷ lệ class giống nhau

**Kết quả:**
- Training: 800 samples (70% safe, 30% risky)
- Test: 200 samples (70% safe, 30% risky)
- Overlap: 0 samples ✅

---

## SLIDE 25: TẠI SAO CẦN test_size?

**Rule of thumb:**

| Dataset Size | Split Ratio |
|--------------|-------------|
| Nhỏ (<1K) | 80/20 |
| Trung bình (1K-10K) | 80/20 hoặc 70/30 |
| Lớn (>10K) | 90/10 |

**Lý do:**
- Dataset nhỏ: Cần nhiều data để train
- Dataset lớn: 10% vẫn đủ samples để test

---

## SLIDE 26: TẠI SAO CẦN random_state?

**Không set random_state:**
- Mỗi lần chạy khác nhau
- Không reproduce được
- Khó debug
- Không so sánh công bằng

**Set random_state=42:**
- Luôn giống nhau
- Reproducible
- Debug dễ dàng
- So sánh công bằng giữa models

---

## SLIDE 27: TẠI SAO CẦN stratify?

**Không dùng stratify:**
```
Dataset gốc: 70% safe, 30% risky

Có thể bị:
Training: 75% safe, 25% risky
Test:     60% safe, 40% risky  ← Không cân bằng!
```

**Dùng stratify=y:**
```
Dataset gốc: 70% safe, 30% risky

Đảm bảo:
Training: 70% safe, 30% risky  ← Giống gốc
Test:     70% safe, 30% risky  ← Giống gốc
```

---

## SLIDE 28: KIỂM TRA DATA LEAKAGE

**Bước quan trọng:**
1. Convert train và test thành sets
2. Tìm giao của 2 sets
3. Kiểm tra xem có overlap không

**Kết quả:**
- Training unique: 800 samples
- Test unique: 200 samples
- Overlap: 0 samples
- ✅ KHÔNG CÓ DATA LEAKAGE!

---

## SLIDE 29: TẠO TEST SET ĐẶC BIỆT

**Ngoài test set tự động, tạo thêm test set thủ công**

**Lý do:**
1. ✅ Demo rõ ràng từng scenario
2. ✅ Có mô tả chi tiết
3. ✅ Edge cases được cover
4. ✅ Dễ giải thích cho học viên

**test.csv:**
- 20 test cases được chọn kỹ
- 10 Safe + 10 Risky (cân bằng 50/50)
- Mỗi case có description rõ ràng

---

## SLIDE 30: VÍ DỤ TEST CASES THỦ CÔNG

**Safe Login Examples:**
- "Morning office login - typical"
- "Afternoon login - normal pattern"
- "End of day - longer session"

**Risky Login Examples:**
- "2 AM - device changed, suspicious typing"
- "3 AM - both device AND country changed"
- "10 PM - late night suspicious pattern"

---

## SLIDE 31: SO SÁNH 2 LOẠI TEST SET

| Tiêu chí | test_split.csv | test.csv |
|----------|----------------|----------|
| Số lượng | 200 samples | 20 samples |
| Tạo như thế nào | Tự động (random) | Thủ công (chọn kỹ) |
| Mô tả | Không | Có chi tiết |
| Mục đích | Đánh giá statistical | Demo, giảng dạy |
| Edge cases | Random | Được chọn kỹ |

**Kết luận:** Dùng cả 2!
- test.csv → Demo trong class
- test_split.csv → Đánh giá thực tế

---

## SLIDE 32: TÓM TẮT QUY TRÌNH

```
BƯỚC 1: XÁC ĐỊNH FEATURES
├─ Phân tích tư duy con người
├─ Chọn 8 features quan trọng
└─ Đảm bảo: dễ thu thập, có ý nghĩa, khó giả mạo

BƯỚC 2: THU THẬP DỮ LIỆU
├─ 3 nguồn: Production, Honeypot, Synthetic
├─ Chọn Synthetic cho lab
└─ Generate 1000 samples (700 safe, 300 risky)

BƯỚC 3: XÂY DỰNG DATASET
├─ Split 80/20 với train_test_split
├─ Dùng stratify=y và random_state=42
├─ Kiểm tra data leakage → 0 overlap ✅
└─ Tạo thêm test set thủ công (20 cases)
```

---

## SLIDE 33: KẾT QUẢ ĐẠT ĐƯỢC

**Files đã tạo:**
- ✅ logins.csv (1000 records) - Full training dataset
- ✅ train_split.csv (800 records) - Training subset
- ✅ test_split.csv (200 records) - Test subset
- ✅ test.csv (20 records) - Demo test cases

**Chất lượng:**
- ✅ Không có data leakage (0 overlap)
- ✅ Tỷ lệ labels cân bằng (stratified)
- ✅ Reproducible (random_state=42)
- ✅ Có mô tả chi tiết (test.csv)

---

## SLIDE 34: CÂU HỎI KIỂM TRA HIỂU BÀI

**Câu 1:**
Tại sao phải shuffle data trước khi split?

**Câu 2:**
Nếu không dùng stratify=y, chuyện gì có thể xảy ra?

**Câu 3:**
Tại sao cần test.csv riêng khi đã có test_split.csv?

---

## SLIDE 35: ĐÁP ÁN CÂU HỎI 1

**Tại sao phải shuffle?**

Nếu không shuffle:
- Data gốc có thể sorted theo label
- Train có thể toàn safe
- Test có thể toàn risky
- Model học sai → Fail!

Sau shuffle:
- Data trộn lẫn
- Train có cả 2 loại
- Test có cả 2 loại
- Model học đúng!

---

## SLIDE 36: ĐÁP ÁN CÂU HỎI 2

**Không dùng stratify:**

Có thể unlucky:
- Train: 62% safe / 38% risky
- Test: 100% safe / 0% risky

→ Model không biết nhận diện risky
→ Test accuracy giả tạo cao

**Dùng stratify:**
- Train: 70% safe / 30% risky
- Test: 70% safe / 30% risky
→ Model học cân bằng

---

## SLIDE 37: ĐÁP ÁN CÂU HỎI 3

**test_split.csv (200 records tự động):**
- ✅ Đủ lớn để statistical significant
- ✅ Random, không bias
- ❌ Không có mô tả
- ❌ Khó giải thích

**test.csv (20 records thủ công):**
- ✅ Có mô tả chi tiết
- ✅ Dễ demo
- ✅ Cover edge cases
- ❌ Nhỏ, không đủ đánh giá production

**→ Dùng cả 2!**

---

## SLIDE 38: BÀI TẬP VỀ NHÀ - BÀI 1

**Phân tích Dataset (Bắt buộc)**

**Yêu cầu:**
1. Feature nào có correlation cao nhất với label?
2. Giờ nào có nhiều risky login nhất?
3. Có bao nhiêu % risky logins có device_change=1?

**Câu hỏi:**
1. Feature nào quan trọng nhất? Tại sao?
2. Giờ nào cần cảnh giác nhất?
3. Nếu user đổi device, có nên block ngay không?

---

## SLIDE 39: BÀI TẬP VỀ NHÀ - BÀI 2

**Tạo Features Mới (Nâng cao)**

Hãy nghĩ ra 3 features mới có thể cải thiện model

**Ví dụ:**
- is_weekend (0/1) - Login cuối tuần?
- distance_from_last_login (km) - Khoảng cách di chuyển
- time_since_last_login (hours) - Bao lâu chưa login

**Yêu cầu:**
- Giải thích tại sao feature đó hữu ích
- Feature đó detect loại attack nào
- Làm thế nào thu thập feature đó

---

## SLIDE 40: BÀI TẬP VỀ NHÀ - BÀI 3

**Edge Cases (Sáng tạo)**

Tạo 5 test cases khó mà model có thể sai

**Ví dụ:**
- CEO đi công tác nước ngoài
- Login từ khách sạn lúc 22h
- Đổi cả device và country
- Nhưng thực ra là safe!

**Challenge:**
Nhiều risk factors nhưng legitimate use case

---

## SLIDE 41: ĐIỂM NHẤN QUAN TRỌNG

> **"Garbage in, garbage out"**  
> Model tốt bắt đầu từ data tốt!

**3 điều QUAN TRỌNG NHẤT:**

1. ⚠️ KHÔNG BAO GIỜ để test data lẫn vào training
2. 📊 Hiểu DATA trước khi train model
3. 🎯 Features tốt > Algorithms phức tạp

---

## SLIDE 42: CÂU HỎI THƯỜNG GẶP - Q1

**Q: Tại sao không dùng Deep Learning?**

**A:**
- Dataset nhỏ (1000 samples)
- Deep Learning cần 10K-100K+ samples
- Features ít (8 features)
- Traditional ML đơn giản, nhanh, đủ tốt
- Nếu có 1M samples + 100 features → Cân nhắc DL

---

## SLIDE 43: CÂU HỎI THƯỜNG GẶP - Q2

**Q: Làm sao biết 1000 samples đủ chưa?**

**A:**
- Rule of thumb: 10-50 samples/feature
- 8 features → Cần 80-400 samples (minimum)
- 1000 samples → OK cho lab
- Production → Cần 10K-100K để robust
- Phụ thuộc độ phức tạp bài toán

---

## SLIDE 44: CÂU HỎI THƯỜNG GẶP - Q3

**Q: Nếu production có 99% safe, 1% risky thì sao?**

**A:**
- Đó là **imbalanced dataset**
- Cần techniques đặc biệt:
  - SMOTE (oversampling)
  - Class weights
  - Anomaly detection (1-class SVM)
- Sẽ học ở module sau!

---

## SLIDE 45: BƯỚC TIẾP THEO

**Buổi học tiếp theo:**

```
BƯỚC 4: DATA PREPROCESSING
├─ Standardization/Normalization
├─ Feature scaling
└─ Handle missing values

BƯỚC 5: MODEL TRAINING
├─ Logistic Regression
├─ Decision Tree
├─ Random Forest
└─ Naive Bayes

BƯỚC 6: MODEL EVALUATION
├─ Accuracy, Precision, Recall, F1
├─ Confusion Matrix
└─ So sánh các models

BƯỚC 7: MODEL DEPLOYMENT
└─ Save models và predict
```

---

## SLIDE 46: TÓM TẮT BÀI HỌC

**Những gì đã học:**
- ✅ Cách xác định features từ tư duy con người
- ✅ Thu thập dữ liệu (3 nguồn)
- ✅ Tạo synthetic data theo logic
- ✅ Chia train/test đúng cách
- ✅ Tránh data leakage
- ✅ Tạo test set cho demo

**Kỹ năng đạt được:**
- Phân tích bài toán security
- Thiết kế features
- Xây dựng dataset chất lượng

---

## SLIDE 47: CHUẨN BỊ CHO BUỔI SAU

**Học viên cần:**
1. ✅ Hoàn thành 3 bài tập về nhà
2. ✅ Đọc về các thuật toán:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - Naive Bayes
3. ✅ Chuẩn bị câu hỏi

**Files cần có:**
- logins.csv
- test.csv
- train_split.csv
- test_split.csv

---

## SLIDE 48: THANK YOU!

**Câu hỏi?**

**Liên hệ:**
- Email: [your-email]
- Slack: [your-channel]

**Tài liệu tham khảo:**
- Course materials trên LMS
- GitHub repository
- Documentation

**Hẹn gặp lại buổi sau!** 🚀
