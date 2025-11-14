# 🚀 Hướng Dẫn Cài Đặt GPU cho TensorFlow

## ❓ Vấn Đề: TensorFlow Không Nhận GPU

Nếu bạn thấy thông báo này khi chạy script:
```
❌ KHÔNG TÌM THẤY GPU!
⚠️  Script sẽ chạy trên CPU (chậm hơn)
```

Mặc dù máy có GPU (kiểm tra bằng `nvidia-smi`), thì vấn đề là TensorFlow chưa được cấu hình đúng.

---

## ✅ Giải Pháp Chi Tiết

### 1️⃣ Kiểm tra Version Compatibility

TensorFlow 2.20.0 yêu cầu:
- **CUDA**: 12.3
- **cuDNN**: 8.9
- **Python**: 3.9 - 3.12

Bạn có CUDA 12.8 (theo `nvidia-smi`) nhưng TensorFlow cần CUDA Toolkit được cài đặt riêng.

### 2️⃣ Cài Đặt CUDA Toolkit 12.3

**Tải CUDA Toolkit:**
1. Vào: https://developer.nvidia.com/cuda-12-3-0-download-archive
2. Chọn:
   - Operating System: Windows
   - Architecture: x86_64
   - Version: Phiên bản Windows của bạn
   - Installer Type: exe (local)
3. Tải và cài đặt

**Sau khi cài:**
```powershell
# Kiểm tra CUDA đã cài thành công
nvcc --version
```

### 3️⃣ Cài Đặt cuDNN 8.9

**Tải cuDNN:**
1. Vào: https://developer.nvidia.com/cudnn
2. Đăng ký tài khoản NVIDIA (miễn phí)
3. Tải cuDNN 8.9 for CUDA 12.x
4. Giải nén file ZIP

**Cài đặt cuDNN:**
1. Copy các file từ thư mục giải nén:
   ```
   cuDNN/bin/*.dll    → C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3\bin\
   cuDNN/include/*    → C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3\include\
   cuDNN/lib/*        → C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3\lib\
   ```

### 4️⃣ Cấu Hình Biến Môi Trường

**Kiểm tra và thêm vào PATH:**

1. Mở "Environment Variables" (Biến môi trường):
   - Win + R → `sysdm.cpl` → Advanced → Environment Variables

2. Kiểm tra PATH có chứa:
   ```
   C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3\bin
   C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3\libnvvp
   ```

3. Thêm biến mới (nếu chưa có):
   ```
   CUDA_PATH = C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3
   CUDA_HOME = C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3
   ```

### 5️⃣ Cài Đặt TensorFlow với GPU Support

**Gỡ TensorFlow cũ (nếu có):**
```powershell
pip uninstall tensorflow tensorflow-gpu
```

**Cài TensorFlow mới với GPU support:**
```powershell
# Cách 1: Cài TensorFlow với CUDA (Recommended)
pip install tensorflow[and-cuda]

# Hoặc Cách 2: Cài TensorFlow thường (sẽ tự detect CUDA)
pip install tensorflow==2.20.0
```

### 6️⃣ Restart và Kiểm Tra

**Restart:**
1. Đóng tất cả terminal/PowerShell
2. Restart máy (khuyến nghị) hoặc ít nhất restart terminal

**Kiểm tra:**
```powershell
python -c "import tensorflow as tf; print('GPUs:', tf.config.list_physical_devices('GPU'))"
```

Kết quả mong đợi:
```
GPUs: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

---

## 🧪 Test GPU Với Script Demo

Chạy lại script:
```powershell
cd lab8s
python TensorFlow_GANs.py
```

Bạn sẽ thấy:
```
🔍 KIỂM TRA GPU
============================================================
✅ Tìm thấy 1 GPU:
   GPU 0: /physical_device:GPU:0
✅ Đã bật GPU memory growth
✅ TensorFlow SẼ SỬ DỤNG GPU
```

---

## 🐛 Troubleshooting

### Lỗi: "Could not load dynamic library 'cudart64_12.dll'"

**Giải pháp:**
- CUDA Toolkit chưa được cài đặt đúng
- Kiểm tra lại PATH có chứa `CUDA\v12.3\bin`
- Restart terminal

### Lỗi: "Could not load dynamic library 'cudnn64_8.dll'"

**Giải pháp:**
- cuDNN chưa được copy đúng vị trí
- Kiểm tra lại bước 3️⃣ ở trên
- Đảm bảo file `cudnn64_8.dll` có trong `CUDA\v12.3\bin`

### GPU vẫn không được detect

**Kiểm tra:**
```powershell
# 1. Kiểm tra CUDA
nvcc --version

# 2. Kiểm tra PATH
echo $env:PATH

# 3. Kiểm tra CUDA_PATH
echo $env:CUDA_PATH

# 4. Test với Python
python -c "import tensorflow as tf; print(tf.config.list_physical_devices())"
```

---

## 📊 So Sánh Tốc Độ CPU vs GPU

| Thiết bị | Thời gian/epoch | Tốc độ |
|----------|-----------------|--------|
| **CPU** | ~30-40 giây | 1x |
| **GPU** (Quadro M5000) | ~3-5 giây | **8-10x nhanh hơn** |

---

## 🔗 Tài Liệu Tham Khảo

- TensorFlow GPU Guide: https://www.tensorflow.org/install/gpu
- CUDA Toolkit: https://developer.nvidia.com/cuda-toolkit
- cuDNN: https://developer.nvidia.com/cudnn
- Compatibility Matrix: https://www.tensorflow.org/install/source#gpu

---

## 💡 Lưu Ý

- Script có thể chạy trên CPU nhưng sẽ **chậm hơn 8-10 lần**
- Với GPU training 20 epochs (~1-2 phút)
- Với CPU training 20 epochs (~10-15 phút)
- Nên setup GPU một lần để dùng lâu dài cho các bài lab sau

---

## 📞 Cần Trợ Giúp?

Nếu vẫn gặp vấn đề:
1. Chụp screenshot thông báo lỗi
2. Chạy: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices())"`
3. Chạy: `nvidia-smi`
4. Gửi kết quả để được hỗ trợ
