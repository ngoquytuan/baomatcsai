

---

# 🎯 **IDS (Intrusion Detection System) là gì?**

**IDS = Hệ thống phát hiện xâm nhập**
→ Công cụ giám sát mạng hoặc hệ thống để **phát hiện hoạt động bất thường, tấn công, hoặc hành vi trái phép**.

Nó giống như **camera an ninh** trong mạng máy tính:

* Không chặn,
* Nhưng **quan sát – phân tích – cảnh báo**.

---

# 🧩 **IDS làm những việc gì?**

1. **Giám sát lưu lượng mạng (network traffic)**
2. **Phân tích log hệ thống, log ứng dụng**
3. **Phát hiện dấu hiệu tấn công**
4. **Gửi cảnh báo cho SOC / admin**
5. **Ghi log để forensic và điều tra sau này**

---

# 📌 **Có 2 loại IDS chính**

### **1. NIDS – Network IDS**

Giám sát *toàn bộ lưu lượng* mạng.
Ví dụ: Snort, Suricata, Zeek.

Dùng để phát hiện:

* Port scanning
* DDoS
* Malware traffic
* Beaconing của botnet
* Trafffic bất thường

### **2. HIDS – Host IDS**

Giám sát *hoạt động bên trong một máy*.
Ví dụ: OSSEC, Wazuh.

Dùng để phát hiện:

* File bị sửa trái phép
* Process lạ
* Privilege escalation
* Login bất thường

---

# ✔️ **IDS hoạt động bằng hai kỹ thuật**

(đây là phần bạn có thể liên hệ sang Module 6 và Module 8)

### **1. Signature-based**

* So khớp với mẫu tấn công đã biết
* Giống antivirus truyền thống
* Nhanh, chính xác
* Nhưng không phát hiện được tấn công mới

### **2. Anomaly-based**

* Phân tích hành vi bình thường
* Báo động khi có bất thường
* Dùng ML/AI (Isolation Forest, Autoencoder, GAN…)
* Bắt được cả zero-day, unknown attack

---

# 🔥 **Tại sao học viên cần biết IDS trong Module 8 (GAN)?**

Vì trong Module 8 bạn sẽ nói:

* GAN được dùng để **tạo traffic tấn công nhìn giống traffic bình thường**
  → để **bypass IDS**.

* Kết quả nghiên cứu:

  > GAN có thể tạo ra payload giúp né được 60–90% IDS signature-based
  > và thậm chí qua được một số anomaly-based IDS.

→ Đây là dạng **adversarial attack** lên hệ thống an ninh.

---


> **“IDS là hệ thống giám sát và cảnh báo xâm nhập – camera an ninh của mạng máy tính.”**

---

