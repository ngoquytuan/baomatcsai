# Danh sách Bài thực hành: Khóa học Trí tuệ nhân tạo trong An ninh mạng

Mỗi ngày bao gồm 2–3 giờ thực hành, chia đều cho hai ca, tập trung vào phân tích các tình huống thực tế không an toàn, tạo tình huống giả lập, thực hiện thủ công và sử dụng AI (chủ yếu với Python), sử dụng các công cụ khác nhau để tránh trùng lặp. Các bài thực hành được thiết kế đơn giản, dễ thực hiện, phù hợp cho nhân viên IT vận hành và bảo trì hệ thống.

### Ngày 1: Module 1 - Giới thiệu về An ninh mạng và Trí tuệ nhân tạo
- **Bài thực hành**: Phân tích email lừa đảo (phishing) giả lập.
  - **Mô tả**: Sử dụng tập dữ liệu email giả lập (cung cấp sẵn), học viên phân tích thủ công các dấu hiệu lừa đảo (ví dụ: liên kết đáng ngờ, lỗi chính tả). Sau đó, sử dụng Python với thư viện Scikit-learn để xây dựng một mô hình phân loại đơn giản (Logistic Regression) để phát hiện email lừa đảo.
  - **Công cụ**: Python (Scikit-learn), trình soạn thảo văn bản (Notepad++), Jupyter Notebook.
  - **Thời lượng**: 2–3 giờ.
  - **Mục tiêu**: Hiểu cách phân biệt email lừa đảo thủ công và tự động hóa quy trình bằng AI.

### Ngày 2: Module 2 - Lập trình Python cho An ninh mạng
- **Bài thực hành**: Phân tích nhật ký hệ thống (log) để phát hiện truy cập trái phép.
  - **Mô tả**: Sử dụng tập dữ liệu nhật ký hệ thống giả lập (ví dụ: log đăng nhập server), học viên phân tích thủ công các mẫu truy cập bất thường (ví dụ: nhiều lần đăng nhập thất bại). Sau đó, dùng Python với Pandas để lọc và trực quan hóa dữ liệu, và Matplotlib để vẽ biểu đồ số lần đăng nhập theo thời gian.
  - **Công cụ**: Python (Pandas, Matplotlib), Jupyter Notebook, Excel (cho phân tích thủ công).
  - **Thời lượng**: 2–3 giờ.
  - **Mục tiêu**: Làm quen với Python để phân tích và trực quan hóa dữ liệu an ninh mạng.

### Ngày 3: Module 3 - Ứng dụng Học máy trong An ninh mạng
- **Bài thực hành**: Phát hiện bất thường trong lưu lượng mạng.
  - **Mô tả**: Sử dụng tập dữ liệu lưu lượng mạng giả lập (ví dụ: NSL-KDD), học viên kiểm tra thủ công các mẫu lưu lượng bất thường (ví dụ: lưu lượng tăng đột biến). Sau đó, dùng Python với Isolation Forest (Scikit-learn) để tự động phát hiện bất thường và so sánh kết quả.
  - **Công cụ**: Python (Scikit-learn, Pandas), Wireshark (cho phân tích thủ công), Jupyter Notebook.
  - **Thời lượng**: 2–3 giờ.
  - **Mục tiêu**: Hiểu cách áp dụng học máy để phát hiện bất thường và so sánh với phân tích thủ công.

### Ngày 4: Module 4 - Phát hiện mối đe dọa email bằng AI
- **Bài thực hành**: Phân loại email spam và hợp lệ.
  - **Mô tả**: Sử dụng tập dữ liệu email giả lập (spam và hợp lệ), học viên phân loại thủ công dựa trên các tiêu chí như từ khóa, tiêu đề, hoặc nguồn email. Sau đó, dùng Python với Scikit-learn để xây dựng mô hình Naïve Bayes kết hợp TF-IDF để tự động phân loại email và đánh giá độ chính xác.
  - **Công cụ**: Python (Scikit-learn, NLTK), Jupyter Notebook, trình duyệt email (cho phân tích thủ công).
  - **Thời lượng**: 2–3 giờ.
  - **Mục tiêu**: Làm quen với kỹ thuật NLP đơn giản (TF-IDF) và Naïve Bayes để phát hiện email spam.

### Ngày 4: Module 5 - Phát hiện mối đe dọa phần mềm độc hại
- **Bài thực hành**: Phân tích hành vi phần mềm đáng ngờ.
  - **Mô tả**: Sử dụng tập dữ liệu hành vi phần mềm giả lập (ví dụ: log hệ thống bị ảnh hưởng), học viên kiểm tra thủ công các dấu hiệu của phần mềm độc hại (ví dụ: thay đổi file hệ thống). Sau đó, dùng Python với Decision Tree (Scikit-learn) để phân loại phần mềm độc hại và hợp lệ.
  - **Công cụ**: Python (Scikit-learn), Process Explorer (cho phân tích thủ công), Jupyter Notebook.
  - **Thời lượng**: 2–3 giờ.
  - **Mục tiêu**: Hiểu cách phân tích hành vi phần mềm độc hại thủ công và tự động hóa với AI.

### Ngày 5: Module 6 - Phát hiện bất thường mạng
- **Bài thực hành**: Phát hiện cuộc tấn công DDoS giả lập.
  - **Mô tả**: Sử dụng tập dữ liệu lưu lượng mạng giả lập, học viên phân tích thủ công các dấu hiệu của cuộc tấn công DDoS (ví dụ: lưu lượng bất thường từ một nguồn). Sau đó, dùng Python với Random Forest (Scikit-learn) để tự động phát hiện các mẫu tấn công DDoS.
  - **Công cụ**: Python (Scikit-learn, Pandas), Wireshark (cho phân tích thủ công), Jupyter Notebook.
  - **Thời lượng**: 2–3 giờ.
  - **Mục tiêu**: Hiểu cách phát hiện tấn công DDoS và áp dụng học máy để tự động hóa.

### Ngày 5: Module 7 - Bảo mật xác thực người dùng bằng AI
- **Bài thực hành**: Phát hiện hành vi đăng nhập bất thường.
  - **Mô tả**: Sử dụng tập dữ liệu đăng nhập giả lập, học viên kiểm tra thủ công các mẫu đăng nhập đáng ngờ (ví dụ: đăng nhập từ vị trí bất thường). Sau đó, dùng Python với K-Means Clustering (Scikit-learn) để phân cụm và phát hiện hành vi bất thường.
  - **Công cụ**: Python (Scikit-learn), Excel (cho phân tích thủ công), Jupyter Notebook.
  - **Thời lượng**: 2–3 giờ.
  - **Mục tiêu**: Hiểu cách sử dụng AI để giám sát và bảo vệ xác thực người dùng.

### Ngày 5: Module 8 - Mạng đối kháng tạo sinh (GAN) trong An ninh mạng
- **Bài thực hành**: Mô phỏng dữ liệu tấn công mạng bằng GAN.
  - **Mô tả**: Sử dụng tập dữ liệu giả lập, học viên phân tích thủ công các mẫu dữ liệu tấn công mạng. Sau đó, dùng Python với TensorFlow để tạo dữ liệu giả lập bằng GAN đơn giản, mô phỏng các mẫu tấn công để kiểm tra hệ thống bảo mật.
  - **Công cụ**: Python (TensorFlow), Jupyter Notebook, trình soạn thảo văn bản (cho phân tích thủ công).
  - **Thời lượng**: 2–3 giờ.
  - **Mục tiêu**: Làm quen với GAN và ứng dụng trong việc mô phỏng dữ liệu tấn công.

### Ngày 5: Module 9 - Kiểm thử xâm nhập bằng AI
- **Bài thực hành**: Phát hiện URL độc hại bằng AI.
  - **Mô tả**: Sử dụng tập dữ liệu URL giả lập (hợp lệ và độc hại), học viên phân loại thủ công dựa trên các đặc điểm của URL (ví dụ: độ dài, ký tự đặc biệt). Sau đó, dùng Python với Logistic Regression (Scikit-learn) để tự động phát hiện URL độc hại.
  - **Công cụ**: Python (Scikit-learn), trình duyệt (cho phân tích thủ công), Jupyter Notebook.
  - **Thời lượng**: 2–3 giờ.
  - **Mục tiêu**: Hiểu cách sử dụng AI để phát hiện URL độc hại và so sánh với phân tích thủ công.

**Tổng thời lượng thực hành**: 10–15 giờ trong 5 ngày (2–3 giờ mỗi ngày).  
**Ghi chú**: Các bài thực hành sử dụng Python làm công cụ chính, kết hợp với các công cụ như Wireshark, Excel, Process Explorer, và trình duyệt để đa dạng hóa và phù hợp với nhân viên IT vận hành hệ thống. Các tập dữ liệu giả lập được cung cấp sẵn để đảm bảo tính đơn giản và dễ tiếp cận.