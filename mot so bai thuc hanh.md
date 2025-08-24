Dưới đây là chi tiết về các bài thực hành được yêu cầu, mô tả cụ thể nội dung, mục tiêu, công cụ sử dụng và kết quả mong đợi trong 1 giờ thực hành cho mỗi bài. Tôi đảm bảo các bài thực hành được thiết kế phù hợp với thời lượng 1 giờ, tập trung vào tính thực tế và áp dụng kiến thức từ các module lý thuyết trong khóa học.

### 1. Thực hành: Viết script Python cơ bản để phân tích dữ liệu (1 giờ)

**Mục tiêu**: Làm quen với Python và các thư viện cơ bản (NumPy, Pandas, Matplotlib) để xử lý và trực quan hóa dữ liệu an ninh mạng.  
**Nội dung**:

- **Bước 1 (15 phút)**: Tải một tập dữ liệu mẫu (ví dụ: nhật ký truy cập mạng hoặc danh sách email với nhãn spam/không spam). Học viên sử dụng Pandas để đọc file CSV và thực hiện các thao tác cơ bản như lọc dữ liệu, tính thống kê (mean, max, min).
- **Bước 2 (20 phút)**: Sử dụng NumPy để xử lý dữ liệu số (ví dụ: tính tỷ lệ các loại yêu cầu HTTP trong nhật ký mạng).
- **Bước 3 (20 phút)**: Tạo biểu đồ trực quan bằng Matplotlib (ví dụ: biểu đồ cột cho tần suất các loại yêu cầu HTTP hoặc biểu đồ phân tán cho thời gian truy cập).
- **Kết quả**: Một script Python hiển thị thống kê cơ bản và biểu đồ trực quan hóa dữ liệu.  
  **Công cụ**: Python, Jupyter Notebook, Pandas, NumPy, Matplotlib.  
  **Yêu cầu**: Học viên cần chạy script và giải thích ý nghĩa của biểu đồ được tạo.

### 2. Thực hành: Xây dựng mô hình học máy để phát hiện bất thường (1 giờ)

**Mục tiêu**: Áp dụng thuật toán Isolation Forest để phát hiện bất thường trong dữ liệu an ninh mạng.  
**Nội dung**:

- **Bước 1 (15 phút)**: Tải tập dữ liệu mẫu (ví dụ: nhật ký mạng với các đặc trưng như lưu lượng, thời gian, địa chỉ IP). Sử dụng Pandas để tiền xử lý dữ liệu (loại bỏ giá trị null, chuẩn hóa dữ liệu).
- **Bước 2 (25 phút)**: Sử dụng thư viện scikit-learn để xây dựng mô hình Isolation Forest. Huấn luyện mô hình trên dữ liệu và dự đoán các điểm bất thường.
- **Bước 3 (15 phút)**: Trực quan hóa kết quả bằng Matplotlib (ví dụ: biểu đồ phân tán đánh dấu các điểm bất thường).
- **Kết quả**: Một mô hình Isolation Forest xác định các điểm bất thường trong tập dữ liệu và một biểu đồ thể hiện kết quả.  
  **Công cụ**: Python, scikit-learn, Pandas, Matplotlib, Jupyter Notebook.  
  **Yêu cầu**: Học viên trình bày các điểm bất thường được phát hiện và lý do chúng được coi là bất thường.

### 3. Thực hành: Xây dựng mô hình phân loại email spam/phishing (1 giờ)

**Mục tiêu**: Xây dựng mô hình phân loại email spam/phishing bằng thuật toán Naïve Bayes.  
**Nội dung**:

- **Bước 1 (15 phút)**: Tải tập dữ liệu email mẫu (ví dụ: tập Enron hoặc tập dữ liệu spam/phishing công khai). Tiền xử lý dữ liệu bằng cách chuyển đổi văn bản email thành đặc trưng số (sử dụng CountVectorizer hoặc TF-IDF).
- **Bước 2 (25 phút)**: Huấn luyện mô hình Naïve Bayes (GaussianNB hoặc MultinomialNB từ scikit-learn) trên tập dữ liệu đã xử lý. Đánh giá hiệu suất mô hình bằng độ chính xác (accuracy) và ma trận nhầm lẫn (confusion matrix).
- **Bước 3 (15 phút)**: Thử nghiệm mô hình với một vài email mẫu và hiển thị kết quả phân loại (spam hoặc không spam).
- **Kết quả**: Một mô hình Naïve Bayes phân loại email và báo cáo hiệu suất.  
  **Công cụ**: Python, scikit-learn, Pandas, Jupyter Notebook.  
  **Yêu cầu**: Học viên giải thích cách mô hình phân biệt email spam/phishing dựa trên đặc trưng văn bản.

### 4. Thực hành: Phân tích và phát hiện malware cơ bản (1 giờ)

**Mục tiêu**: Sử dụng cây quyết định để phát hiện malware dựa trên các đặc trưng cơ bản.  
**Nội dung**:

- **Bước 1 (15 phút)**: Tải tập dữ liệu mẫu về malware (ví dụ: tập dữ liệu chứa đặc trưng hành vi như số lần gọi API, kích thước file). Tiền xử lý dữ liệu (chuẩn hóa, mã hóa các đặc trưng phân loại).
- **Bước 2 (25 phút)**: Huấn luyện mô hình cây quyết định (DecisionTreeClassifier từ scikit-learn) trên tập dữ liệu. Đánh giá hiệu suất bằng độ chính xác và ma trận nhầm lẫn.
- **Bước 3 (15 phút)**: Thử nghiệm mô hình với một số mẫu dữ liệu mới và trực quan hóa cây quyết định bằng thư viện graphviz hoặc Matplotlib.
- **Kết quả**: Một mô hình cây quyết định phân loại malware và trực quan hóa cấu trúc cây.  
  **Công cụ**: Python, scikit-learn, Pandas, Matplotlib, graphviz (tùy chọn), Jupyter Notebook.  
  **Yêu cầu**: Học viên giải thích cách cây quyết định đưa ra dự đoán dựa trên các đặc trưng.

### 5. Thực hành: Xây dựng mô hình phát hiện bất thường mạng (1 giờ)

**Mục tiêu**: Áp dụng thuật toán học máy để phát hiện các cuộc tấn công mạng (như botnet) dựa trên lưu lượng mạng.  
**Nội dung**:

- **Bước 1 (15 phút)**: Tải tập dữ liệu mạng mẫu (ví dụ: tập NSL-KDD hoặc tập lưu lượng mạng với nhãn botnet). Tiền xử lý dữ liệu (chuẩn hóa, mã hóa các đặc trưng như giao thức, số gói tin).
- **Bước 2 (25 phút)**: Huấn luyện mô hình học máy (ví dụ: Random Forest từ scikit-learn) để phân loại lưu lượng mạng bình thường và bất thường. Đánh giá hiệu suất bằng độ chính xác và F1-score.
- **Bước 3 (15 phút)**: Thử nghiệm mô hình với dữ liệu mới và trực quan hóa kết quả bằng biểu đồ phân tán hoặc ma trận nhầm lẫn.
- **Kết quả**: Một mô hình Random Forest phát hiện lưu lượng mạng bất thường và báo cáo hiệu suất.  
  **Công cụ**: Python, scikit-learn, Pandas, Matplotlib, Jupyter Notebook.  
  **Yêu cầu**: Học viên giải thích các đặc trưng quan trọng nhất ảnh hưởng đến việc phát hiện bất thường.

### 6. Thực hành: Thử nghiệm mô hình GAN cơ bản (1 giờ)

**Mục tiêu**: Làm quen với GAN thông qua việc xây dựng một mô hình GAN đơn giản để tạo dữ liệu giả lập (ví dụ: dữ liệu mạng).  
**Nội dung**:

- **Bước 1 (15 phút)**: Tải tập dữ liệu đơn giản (ví dụ: tập dữ liệu lưu lượng mạng hoặc dữ liệu số cơ bản). Tiền xử lý dữ liệu để phù hợp với đầu vào của GAN.
- **Bước 2 (25 phút)**: Sử dụng thư viện TensorFlow hoặc PyTorch để xây dựng một mô hình GAN cơ bản (gồm Generator và Discriminator). Huấn luyện GAN để tạo dữ liệu giả lập tương tự dữ liệu gốc.
- **Bước 3 (15 phút)**: Trực quan hóa dữ liệu giả lập được tạo bởi GAN và so sánh với dữ liệu gốc bằng biểu đồ phân tán.
- **Kết quả**: Một mô hình GAN cơ bản tạo dữ liệu giả lập và biểu đồ so sánh dữ liệu thật/giả.  
  **Công cụ**: Python, TensorFlow/PyTorch, Matplotlib, Jupyter Notebook.  
  **Yêu cầu**: Học viên giải thích vai trò của Generator và Discriminator trong GAN.

### 7. Thực hành: Thực hiện kiểm tra xâm nhập cơ bản với AI (1 giờ)

**Mục tiêu**: Sử dụng công cụ AI để thực hiện kiểm tra xâm nhập cơ bản, tập trung vào phát hiện lỗ hổng web hoặc URL độc hại.  
**Nội dung**:

- **Bước 1 (15 phút)**: Cài đặt công cụ AI hỗ trợ kiểm tra xâm nhập (ví dụ: một script Python sử dụng mô hình học sâu đơn giản để phát hiện URL độc hại hoặc quét lỗ hổng web). Tải tập dữ liệu URL mẫu.
- **Bước 2 (25 phút)**: Chạy script để phân loại URL (an toàn/độc hại) hoặc quét một trang web mẫu để tìm lỗ hổng (ví dụ: SQL injection, XSS). Đánh giá kết quả dựa trên đầu ra của công cụ.
- **Bước 3 (15 phút)**: Trình bày kết quả và thảo luận về cách cải thiện công cụ AI để tăng độ chính xác.
- **Kết quả**: Báo cáo danh sách URL độc hại hoặc lỗ hổng được phát hiện trên trang web mẫu.  
  **Công cụ**: Python, scikit-learn/TensorFlow, công cụ quét như OWASP ZAP (tích hợp AI), Jupyter Notebook.  
  **Yêu cầu**: Học viên giải thích cách công cụ AI xác định URL độc hại hoặc lỗ hổng dựa trên đặc trưng.

### Ghi Chú

- Mỗi bài thực hành được thiết kế để hoàn thành trong 1 giờ, với sự phân bổ thời gian hợp lý giữa tiền xử lý, xây dựng mô hình và đánh giá kết quả.
- Các bài thực hành sử dụng dữ liệu mẫu công khai hoặc giả lập để đảm bảo tính khả thi trong môi trường học tập.
- Học viên cần lưu ý ghi lại các bước thực hiện và kết quả để thảo luận với giảng viên.

Nếu bạn cần điều chỉnh thêm hoặc muốn tôi cung cấp mã Python mẫu cho bất kỳ bài thực hành nào, hãy cho tôi biết!