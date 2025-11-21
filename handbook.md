# CSAI - HANDBOOK 
---

## TÓM TẮT KHÓA HỌC & ỨNG DỤNG THỰC TẾ

### **Bối Cảnh 2025**
- **11.5 Tbps** - Cuộc tấn công DDoS lớn nhất (Cloudflare 9/2025)
- **400%** - Gia tăng tấn công có sử dụng AI
- **450,000** - Mẫu malware mới mỗi ngày
- **$4.35M** - Chi phí trung bình cho một vụ data breach

### **9 Module Cốt Lõi - Kiến Thức Quan Trọng Nhất**

#### **Module 1-2: Nền Tảng AI & Python**
**Kiến thức then chốt:**
- AI = Machine Learning ⊃ Deep Learning
- Supervised (có nhãn) vs Unsupervised (không nhãn)
- Python libraries: NumPy, Pandas, Scikit-learn, TensorFlow

**Áp dụng tại SOC:**
- Tự động hóa phân tích log (Python scripts)
- Tích hợp với SIEM qua API
- Xây dựng data pipeline cho ML models

#### **Module 3: Machine Learning Ứng Dụng**
**Thuật toán quan trọng nhất:**

| Thuật toán | Ứng dụng | Ưu điểm | Khi nào dùng |
|-----------|----------|---------|--------------|
| **Isolation Forest** | Phát hiện anomaly | Không cần nhãn, nhanh | Phát hiện unknown threats |
| **XGBoost** | Phân loại malware | Chính xác cao (95%+) | Khi có dữ liệu labeled |
| **Random Forest** | Network intrusion | Xử lý noise tốt | Phân tích network traffic |
| **Time Series** | Xu hướng tấn công | Phát hiện pattern theo thời gian | DDoS, APT detection |

**Quy trình triển khai ML:**
```
1. Train-Test Split (80/20) → Tránh overfitting
2. Standardization → Cân bằng feature importance
3. Feature Engineering → Trích xuất đặc trưng quan trọng
4. Model Training → XGBoost/Isolation Forest
5. Performance Evaluation → Accuracy >95%, FP <5%
```

#### **Module 4-5: Email & Malware Detection**
**Email Security (2025 Update):**
- **Mối đe dọa mới:** LLM-generated phishing (ChatGPT/Claude)
- **Giải pháp 4 lớp:**
  1. Naïve Bayes (lọc nhanh) → 92% accuracy
  2. SVM (phân tích sâu) → 96% accuracy  
  3. BERT-based NLP (phát hiện AI-generated)
  4. Link analysis + Threat Intelligence

**Malware Detection:**
- **Static Analysis:** Entropy, PE header, strings
- **Dynamic Analysis:** Sandbox, API calls
- **Deep Learning:** CNN cho binary visualization (95%+ accuracy)

#### **Module 6: Network Anomaly Detection**
**Kỹ thuật phát hiện:**
- **Statistical baseline:** Mean/std deviation
- **Behavioral clustering:** K-means, DBSCAN
- **Botnet detection:** DGA domain analysis (80%+ accuracy)

**Triển khai thực tế:**
```
NetFlow/IPFIX → Feature Extraction → ML Model → Alert
                     ↓
            Processing time: <100ms
```

#### **Module 7: Authentication Security**
**AI-Powered Authentication:**
- **Behavioral biometrics:** Keystroke, mouse patterns
- **Risk scoring (0-100):**
  - 80-100: Truy cập bình thường
  - 50-79: Xác thực bổ sung
  - 0-49: Khóa + review thủ công
- **Case study:** 94.5% phishing detection, $12M fraud prevented

**Slack Integration (theo yêu cầu học viên):**
- Real-time security alerts
- Interactive incident response (Lock/Investigate/Safe buttons)
- Automated daily reports

#### **Module 8: GANs & Deepfakes**
**Mối đe dọa 2025:**
- Real-time deepfake video calls
- CEO fraud (+500% năm 2025)
- Facial recognition bypass

**Phòng thủ:**
- Deepfake detection models (90%+ accuracy)
- Multi-factor biometrics
- Out-of-band verification cho giao dịch quan trọng

#### **Module 9: AI Pentesting**
- Neural network fuzzing
- Automated vulnerability discovery
- IoT device fingerprinting
- Malicious URL detection (97% accuracy)

---

## CÔNG CỤ & BEST PRACTICES

### **Essential Tech Stack:**
```python
# ML Frameworks
TensorFlow 2.15, PyTorch 2.2, Scikit-learn 1.4, XGBoost 2.0

# Security Tools
YARA (malware), Suricata (IDS), Zeek (network), Volatility (forensics)

# Open Source SOC
Security Onion, TheHive, MISP, ELK Stack
```

### **Algorithm Selection Guide:**
```
Có dữ liệu labeled?
├─ Yes → XGBoost, Random Forest, SVM
└─ No → Isolation Forest, K-Means, DBSCAN

Cần real-time?
├─ Yes → Naïve Bayes, Isolation Forest
└─ No → Deep Learning (CNN, RNN)

Cần giải thích được?
├─ Yes → Decision Trees, Random Forest
└─ No → Deep Learning OK
```


## CẬP NHẬT MỚI NHẤT 2025

### **Emerging Threats:**
1. **LLM-Powered Attacks:** Tự động tìm lỗ hổng, social engineering quy mô lớn
2. **Deepfake Evolution:** Real-time video manipulation ($25M CEO fraud case)
3. **AI Supply Chain Attacks:** Poisoned models, backdoors
4. **Quantum Threat:** Chuẩn bị cho quantum-resistant crypto (2028-2030)

### **Defense Updates:**
```
✓ Adversarial training cho tất cả models
✓ Multi-factor biometrics (không chỉ password)
✓ Human verification cho critical decisions
✓ Regular model retraining (weekly)
✓ Explainable AI (SHAP/LIME) cho compliance
```

### **Compliance 2025:**
- **EU AI Act:** High-risk AI cần certification
- **GDPR:** Right to explanation cho AI decisions
- **US State Laws:** AI bias auditing

---


---


**Online:**
- Fast.ai - Practical Deep Learning
- Coursera - ML for Cybersecurity
- SANS - AI/ML for Security

**Communities:**
- AI Village (DEF CON)
- r/MachineLearning, r/netsec
- OWASP ML Security Working Group

**Tools:**
- GitHub: 1000+ security AI projects
- TensorFlow, PyTorch documentation
- Scikit-learn tutorials

---

