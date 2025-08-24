# Tài liệu chuẩn hóa: Chuyển tiếp và Kiến thức nền tảng cho khóa học CSAI (Cyber Security Artificial Intelligence)

## Đánh giá kiến thức đầu vào cho học viên

Để tham gia hiệu quả khóa học CSAI kéo dài 5 ngày với 9 module chuyên sâu, học viên nên có những nền tảng sau:

### 1. Kỹ năng bắt buộc
| Kỹ năng | Mô tả |
|--------|------|
| Lập trình Python cơ bản | Biết khai báo biến, cấu trúc điều khiển, xử lý danh sách, từ điển, hàm |
| Hiểu kiến thức cơ bản về AI/ML | Biết các khái niệm như supervised learning, classification, model evaluation |
| Sử dụng thư viện NumPy, Pandas | Đọc, xử lý dữ liệu bảng đơn giản |
| Tư duy phân tích dữ liệu | Biết cách đọc log, phân tích chuỗi hành vi |

### 2. Kỹ năng khuyến khích
| Kỹ năng | Mô tả |
|--------|------|
| Trải nghiệm với bảo mật hệ thống hoặc mạng | Quen với các công cụ như Wireshark, IDS, hoặc log mạng |
| Kiến thức cơ bản về mạng | TCP/IP, các loại tấn công phổ biến, kiến trúc mạng |
| Hiểu cơ bản về học sâu (deep learning) | Biết CNN, RNN là gì, không cần chuyên sâu |

---

## Module 1: Giới thiệu về Cyber Security & AI
### Chuyển tiếp: Mở đầu khóa học
- Làm nền tảng khởi động toàn khóa.
- Giới thiệu khái niệm AI, các kỹ thuật cơ bản trong Machine Learning, Deep Learning, NLP.
- Mục tiêu: học viên hiểu cách AI đang được dùng trong bảo mật hiện đại.

### Kiến thức nền tảng
| Kiến thức | Mức độ | Mục đích |
|----------|---------|----------|
| Tổng quan AI & bảo mật | Bắt buộc | Hiểu khái niệm và định vị AI trong cyber security |
| Machine Learning căn bản | Khuyến khích | Hiểu supervised, unsupervised, classification, clustering |
| NLP cơ bản | Khuyến khích | Chuẩn bị cho xử lý email (module 4) |

---

## Module 2: Lập trình Python cho chuyên gia bảo mật
### Chuyển tiếp từ Module 1
- Ứng dụng kiến thức AI vào lập trình thực tế với Python.
- Làm quen thư viện Pandas, NumPy, Matplotlib.
- Mục tiêu: học viên có nền tảng code để xây mô hình AI sau này.

### Kiến thức nền tảng
| Kiến thức | Mức độ | Mục đích |
|----------|---------|----------|
| Cú pháp Python cơ bản | Bắt buộc | Viết, chạy, kiểm soát luồng chương trình |
| Làm việc với DataFrame (Pandas) | Bắt buộc | Xử lý log, dữ liệu mạng, dữ liệu email |
| Vẽ biểu đồ (Matplotlib) | Khuyến khích | Trực quan hóa bất thường trong log |

---

## Module 3: Ứng dụng Machine Learning trong bảo mật
### Chuyển tiếp từ Module 2
- Học viên đã có kỹ năng Python và xử lý dữ liệu.
- Module này dùng Python để huấn luyện mô hình phát hiện tấn công.

### Kiến thức nền tảng
| Kiến thức | Mức độ | Mục đích |
|----------|---------|----------|
| Thuật toán ML cơ bản | Bắt buộc | Logistic Regression, Decision Tree, XGBoost |
| PCA và giảm chiều | Khuyến khích | Hiểu cách chọn đặc trưng đầu vào |
| Chuỗi thời gian | Khuyến khích | Áp dụng trong log mạng và hành vi |
| NLP cơ bản | Rất khuyến khích | Chuẩn bị cho module 4 |

---

## Module 4: Phát hiện mối đe dọa email bằng AI
### Chuyển tiếp từ Module 3
- Từ dữ liệu số và phân loại thông thường sang dữ liệu văn bản (email).
- Áp dụng NLP, phân loại spam, phishing qua text.

### Kiến thức nền tảng
| Kiến thức | Mức độ | Mục đích |
|----------|---------|----------|
| Xử lý văn bản | Bắt buộc | Tiền xử lý email: BoW, TF-IDF, n-grams |
| Logistic Regression, Naïve Bayes | Bắt buộc | Mô hình phân loại spam/phishing |
| NLP cơ bản | Rất khuyến khích | Hiểu ý nghĩa ngữ cảnh trong nội dung email |
| Đánh giá mô hình | Bắt buộc | Accuracy, F1, Precision, Recall |

---

## Module 5: Phát hiện mã độc bằng AI
### Chuyển tiếp từ Module 4
- Mở rộng từ email sang mã độc – dữ liệu phức tạp hơn.
- Ứng dụng phân tích hành vi, cây quyết định, HMM, deep learning.

### Kiến thức nền tảng
| Kiến thức | Mức độ | Mục đích |
|----------|---------|----------|
| API calls, mã nhị phân | Khuyến khích | Trích xuất đặc trưng malware |
| Học sâu cơ bản (CNN, HMM) | Rất khuyến khích | Phát hiện malware biến thể |
| Kỹ năng trực quan hóa | Bắt buộc | Phân tích kết quả mô hình |

---

## Module 6: Phát hiện bất thường mạng
### Chuyển tiếp từ Module 5
- Từ mã độc chuyển sang log mạng và luồng mạng.
- Dùng unsupervised learning phát hiện DDoS, botnet.

### Kiến thức nền tảng
| Kiến thức | Mức độ | Mục đích |
|----------|---------|----------|
| Log mạng, Netflow, PCAP | Bắt buộc | Hiểu cấu trúc dữ liệu mạng |
| Clustering, anomaly detection | Bắt buộc | Phát hiện hành vi lạ không cần nhãn |
| Chuỗi thời gian | Rất khuyến khích | Dùng cho traffic pattern detection |

---

## Module 7: AI trong xác thực người dùng
### Chuyển tiếp từ Module 6
- Học viên đã biết phát hiện bất thường trên mạng.
- Module 7 thu hẹp vào phân tích hành vi người dùng để xác định gian lận.

### Kiến thức nền tảng
| Kiến thức | Mức độ | Mục đích |
|----------|---------|----------|
| Behavioral analytics | Bắt buộc | Nhận diện login bất thường, credential stuffing |
| Slack/Bot Events | Khuyến khích | Tích hợp AI với hệ thống cảnh báo thực tế |
| Xử lý chuỗi hành vi | Rất khuyến khích | Đánh giá người dùng theo thời gian |

---

## Module 8: GAN trong bảo mật
### Chuyển tiếp từ Module 7
- Học viên biết AI phòng thủ. Giờ học cách AI bị lạm dụng để tấn công.
- GAN tạo mẫu giả, vượt IDS, nhận diện khuôn mặt.

### Kiến thức nền tảng
| Kiến thức | Mức độ | Mục đích |
|----------|---------|----------|
| Deep Learning căn bản | Bắt buộc | Generator, Discriminator |
| CNN, image/text data | Bắt buộc | Dùng cho mô hình sinh dữ liệu |
| IDS/IPS | Khuyến khích | Đánh giá hiệu quả né tránh hệ thống giám sát |

---

## Module 9: Pentest với AI
### Chuyển tiếp từ Module 8
- Kết thúc khóa học bằng ứng dụng AI vào kiểm thử bảo mật.
- Học viên xây công cụ AI để tấn công có kiểm soát.

### Kiến thức nền tảng
| Kiến thức | Mức độ | Mục đích |
|----------|---------|----------|
| Kiểm thử xâm nhập (pentest) | Bắt buộc | Recon, Exploit, Lateral movement |
| Reinforcement learning | Khuyến khích | DeepExploit áp dụng RL |
| Phân tích lỗ hổng | Bắt buộc | Phát hiện web vulns, IoT scan |

---

Tài liệu này dùng để thiết kế lại toàn bộ slide hoặc đề cương giảng dạy, đảm bảo tính logic, mạch lạc và phù hợp với trình độ học viên.

