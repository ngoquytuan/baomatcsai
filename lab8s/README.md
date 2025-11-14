# 🤖 Lab 8: TensorFlow GANs Demo

## 📚 Module 8: Generative Adversarial Networks

Demo script đơn giản để giới thiệu GANs với TensorFlow trên MNIST dataset.

---

## 📁 Nội Dung Thư Mục

```
lab8s/
├── TensorFlow_GANs.py       # Script demo chính
├── GPU_SETUP_GUIDE.md       # Hướng dẫn cài đặt GPU
└── README.md                # File này
```

---

## 🚀 Cách Chạy

### Cách 1: Chạy Trực Tiếp
```bash
cd lab8s
python TensorFlow_GANs.py
```

### Cách 2: Chạy từ IDE
- Mở `TensorFlow_GANs.py` trong PyCharm/VSCode
- Run file (F5 hoặc Ctrl+F5)

---

## 📦 Yêu Cầu

### Packages Cần Thiết
```bash
pip install tensorflow numpy matplotlib
```

### GPU Support (Khuyến nghị)
Nếu có GPU NVIDIA, xem hướng dẫn chi tiết trong [GPU_SETUP_GUIDE.md](GPU_SETUP_GUIDE.md)

```bash
pip install tensorflow[and-cuda]
```

---

## 🎯 Script Sẽ Làm Gì?

1. ✅ **Kiểm tra GPU** - Tự động detect và sử dụng GPU nếu có
2. 📥 **Tải MNIST** - Download dataset tự động
3. 🏗️ **Tạo Models** - Generator và Discriminator
4. 🎓 **Training** - 20 epochs (~2 phút với GPU, ~15 phút với CPU)
5. 🖼️ **Tạo Ảnh** - Lưu ảnh generated sau mỗi 5 epochs

---

## 📊 Kết Quả Mong Đợi

Sau khi chạy xong, bạn sẽ thấy:

### Console Output
```
============================================================
🔍 KIỂM TRA GPU
============================================================
✅ Tìm thấy 1 GPU:
   GPU 0: /physical_device:GPU:0
✅ TensorFlow SẼ SỬ DỤNG GPU
============================================================

DEMO: Generative Adversarial Networks (GANs)
Dataset: MNIST (Chữ số viết tay)
============================================================

📥 Đang tải MNIST dataset...
✅ Đã tải 60000 ảnh

...

Epoch 20/20
  Generator Loss: 0.9234
  Discriminator Loss: 1.3456
  Time: 3.45 sec

✅ Training hoàn tất!
```

### Generated Images
Các file ảnh được lưu trong `lab8s/`:
- `image_at_epoch_0005.png`
- `image_at_epoch_0010.png`
- `image_at_epoch_0015.png`
- `image_at_epoch_0020.png`

Mỗi ảnh chứa 16 chữ số được tạo bởi Generator.

---

## 🏗️ Kiến Trúc Mô Hình

### Generator
```
Input (100) → Dense (7×7×256) → Reshape →
Conv2DTranspose (128) → Conv2DTranspose (64) →
Conv2DTranspose (1) → Output (28×28×1)
```

**Chức năng:** Chuyển noise vector thành ảnh chữ số

### Discriminator
```
Input (28×28×1) → Conv2D (64) → Conv2D (128) →
Flatten → Dense (1) → Output (Real/Fake)
```

**Chức năng:** Phân biệt ảnh thật vs ảnh giả

---

## 🎓 Kiến Thức Liên Quan

### 1. Generative Adversarial Networks (GANs)
- **Generator:** Học cách tạo ảnh giả giống ảnh thật
- **Discriminator:** Học cách phân biệt ảnh thật/giả
- **Adversarial Training:** Hai mô hình đấu với nhau để cải thiện

### 2. Loss Functions
- **Generator Loss:** Muốn Discriminator nghĩ ảnh giả là thật
- **Discriminator Loss:** Muốn phân loại đúng cả ảnh thật và giả

### 3. Training Process
```
Epoch 1: Generator tạo ảnh rất tệ → Discriminator dễ dàng phân biệt
Epoch 5: Generator tốt hơn → Discriminator khó phân biệt hơn
Epoch 10: Generator khá tốt → Discriminator phải cố gắng
Epoch 20: Generator rất tốt → Discriminator khó phân biệt
```

---

## 🔧 Customization

### Tăng Số Epochs
Để tạo ảnh đẹp hơn:
```python
EPOCHS = 50  # Thay vì 20
```

### Thay Đổi Batch Size
```python
BATCH_SIZE = 128  # Nhỏ hơn nếu GPU hết RAM
```

### Lưu Ảnh Thường Xuyên Hơn
```python
if (epoch + 1) % 2 == 0:  # Thay vì % 5
    generate_and_save_images(...)
```

---

## ⚠️ Lưu Ý

### GPU vs CPU
- **Với GPU:** ~3-5 giây/epoch → Tổng ~2 phút
- **Với CPU:** ~30-40 giây/epoch → Tổng ~15 phút

Nếu không có GPU, giảm EPOCHS xuống 10 để demo nhanh hơn.

### Memory Usage
- GPU RAM: ~2-3 GB
- System RAM: ~4-5 GB
- Disk Space: ~100 MB (cho MNIST)

---

## 🐛 Troubleshooting

### Lỗi: Không Tìm Thấy GPU
→ Xem [GPU_SETUP_GUIDE.md](GPU_SETUP_GUIDE.md)

### Lỗi: Out of Memory
```python
# Giảm batch size
BATCH_SIZE = 64  # Thay vì 256
```

### Lỗi: Import Error
```bash
# Cài lại packages
pip install --upgrade tensorflow numpy matplotlib
```

### Ảnh Generated Không Đẹp
- Tăng số epochs (50-100)
- Đợi lâu hơn để model học
- Epochs đầu tiên ảnh sẽ rất xấu (bình thường)

---

## 📖 Tài Liệu Tham Khảo

- **TensorFlow GANs Tutorial:** https://www.tensorflow.org/tutorials/generative/dcgan
- **Original GAN Paper:** https://arxiv.org/abs/1406.2661
- **DCGAN Paper:** https://arxiv.org/abs/1511.06434

---

## 👨‍🏫 Demo Trên Lớp

### Trước Khi Demo
1. ✅ Test chạy script trước ở nhà
2. ✅ Đảm bảo GPU đã được cài đặt (nếu có)
3. ✅ Chuẩn bị ảnh generated sẵn để show (nếu máy chậm)

### Trong Lúc Demo
1. Giải thích kiến trúc Generator và Discriminator
2. Chạy script và giải thích output
3. Show ảnh generated qua các epochs
4. Giải thích loss function

### Thời Gian Demo
- Giải thích: 5-10 phút
- Chạy script: 2-15 phút (tùy GPU/CPU)
- Q&A: 5 phút

---

## 🎯 Mục Tiêu Học Tập

Sau lab này, học viên sẽ:
- ✅ Hiểu kiến trúc GANs cơ bản
- ✅ Biết cách implement Generator và Discriminator
- ✅ Hiểu adversarial training process
- ✅ Có thể chạy và customize GANs
- ✅ Biết cách setup TensorFlow GPU

---

**Chúc các bạn học tốt! 🎓**
