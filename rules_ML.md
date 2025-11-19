# 🎯 CHECKLIST & RULES CHO MỌI DỰ ÁN MACHINE LEARNING

Đây là **BEST PRACTICES** chung cho hầu hết dự án ML, không riêng gì bài toán security .

---

## 📋 ML PROJECT CHECKLIST - PHIÊN BẢN ĐẦY ĐỦ

---

## ✅ PHASE 1: HIỂU BÀI TOÁN (PROBLEM UNDERSTANDING)

### **1.1 Xác định loại bài toán**
- [ ] Classification (phân loại)
  - [ ] Binary (2 classes): spam/not spam, fraud/normal
  - [ ] Multiclass (>2 classes): cat/dog/bird
  - [ ] Multilabel (nhiều labels cùng lúc)
- [ ] Regression (dự đoán số): giá nhà, nhiệt độ
- [ ] Clustering (phân nhóm): phân khách hàng
- [ ] Anomaly Detection (phát hiện bất thường)
- [ ] Time Series (dữ liệu theo thời gian)

### **1.2 Xác định success metrics**
- [ ] Chọn metric phù hợp với business:
  - Classification: Accuracy, Precision, Recall, F1, AUC-ROC
  - Regression: MAE, MSE, RMSE, R²
  - Ranking: MAP, NDCG
- [ ] Xác định threshold chấp nhận được (VD: accuracy >90%)
- [ ] Xác định yêu cầu về inference time (<100ms?)
- [ ] Xác định cost của False Positive vs False Negative

### **1.3 Thu thập yêu cầu**
- [ ] Độ chính xác cần thiết
- [ ] Tốc độ inference
- [ ] Kích thước model tối đa
- [ ] Khả năng giải thích (interpretability)
- [ ] Điều kiện deploy (cloud, edge, mobile)

---

## ✅ PHASE 2: THU THẬP & PHÂN TÍCH DỮ LIỆU (DATA COLLECTION)

### **2.1 Thu thập data**
- [ ] Xác định nguồn data: Production logs, APIs, Databases, Public datasets
- [ ] Đảm bảo data đủ lớn (rule of thumb: 10-50 samples/feature tối thiểu)
- [ ] Kiểm tra quyền sử dụng data (privacy, GDPR, licenses)
- [ ] Document data source và collection method

### **2.2 Exploratory Data Analysis (EDA)**
- [ ] Load data và check shape: `df.shape`
- [ ] Check data types: `df.dtypes`
- [ ] Check missing values: `df.isnull().sum()`
- [ ] Check duplicates: `df.duplicated().sum()`
- [ ] Statistical summary: `df.describe()`
- [ ] Visualize distributions: histograms, box plots
- [ ] Check correlations: `df.corr()`
- [ ] Identify outliers

### **2.3 Label Distribution (cho classification)**
- [ ] Check imbalanced data: `df['label'].value_counts()`
- [ ] Nếu imbalanced (<30% minority class):
  - [ ] Consider SMOTE, oversampling, undersampling
  - [ ] Consider class weights
  - [ ] Consider anomaly detection approach
  - [ ] Use stratified split

---

## ✅ PHASE 3: FEATURE ENGINEERING

### **3.1 Feature Selection**
- [ ] Domain expertise: Chọn features có ý nghĩa business
- [ ] Remove low-variance features
- [ ] Remove highly correlated features (>0.95)
- [ ] Feature importance analysis
- [ ] Curse of dimensionality: Không quá nhiều features so với samples

### **3.2 Feature Creation**
- [ ] Tạo interaction features nếu cần
- [ ] Binning/discretization cho continuous features
- [ ] Encoding categorical features:
  - [ ] One-hot encoding (cho nominal)
  - [ ] Label encoding (cho ordinal)
  - [ ] Target encoding (cẩn thận data leakage)
- [ ] Date/time features: hour, day_of_week, month, is_weekend
- [ ] Text features: TF-IDF, word embeddings

### **3.3 Feature Validation**
- [ ] Đảm bảo features có thể thu thập ở production
- [ ] Không dùng features có data leakage
- [ ] Không dùng features vi phạm privacy

---

## ✅ PHASE 4: DATA SPLITTING (QUAN TRỌNG!)

### **4.1 Train/Validation/Test Split**
**RULE 1: Luôn chia data TRƯỚC KHI làm bất cứ điều gì khác!**

```python
# Cách 1: Train/Test split (đơn giản)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,        # RULE 2: Thường 0.2 hoặc 0.3
    random_state=42,      # RULE 3: Luôn set để reproducible
    stratify=y            # RULE 4: Với classification, luôn stratify
)

# Cách 2: Train/Val/Test split (khuyến khích)
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42, stratify=y_temp
)
# Kết quả: 60% train, 20% val, 20% test
```

### **4.2 Split Rules chi tiết**

**RULE 2: test_size phụ thuộc dataset size**
```
Dataset Size         Recommended Split
< 1,000             70/30 hoặc 80/20
1,000 - 10,000      80/20
10,000 - 100,000    85/15 hoặc 90/10
> 100,000           90/10 hoặc 95/5
```

**RULE 3: random_state**
- [ ] Luôn set random_state (VD: 42, 123, 2024)
- [ ] Giúp reproduce kết quả
- [ ] Dùng cùng một giá trị trong suốt project
- [ ] Document giá trị đã chọn

**RULE 4: stratify cho classification**
- [ ] Luôn dùng `stratify=y` với classification
- [ ] Đảm bảo tỷ lệ class giống nhau giữa train/val/test
- [ ] Đặc biệt quan trọng với imbalanced data

**RULE 5: Time-based split cho time series**
```python
# KHÔNG dùng random split với time series!
# Dùng time-based split:
train = df[df['date'] < '2024-01-01']
test = df[df['date'] >= '2024-01-01']
```

### **4.3 Data Leakage Prevention (CỰC KỲ QUAN TRỌNG!)**

**RULE 6: KHÔNG BAO GIỜ để test data "nhìn thấy" trong training!**

```python
# ❌ SAI - Fit scaler trên toàn bộ data
scaler.fit(X)  # Leak test data info!
X_train, X_test = train_test_split(X)

# ✅ ĐÚNG - Fit chỉ trên training data
X_train, X_test = train_test_split(X)
scaler.fit(X_train)  # Chỉ học từ train
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

**RULE 7: Kiểm tra overlap**
```python
train_set = set(map(tuple, X_train.values))
test_set = set(map(tuple, X_test.values))
overlap = train_set & test_set
assert len(overlap) == 0, "Data leakage detected!"
```

---

## ✅ PHASE 5: DATA PREPROCESSING

### **5.1 Handle Missing Values**
- [ ] Identify missing patterns: `df.isnull().sum()`
- [ ] Decide strategy:
  - [ ] Drop rows (nếu <5% missing)
  - [ ] Imputation: mean, median, mode
  - [ ] Advanced: KNN imputer, iterative imputer
  - [ ] Create "missing" indicator feature
- [ ] **RULE 8: Fit imputer chỉ trên training data!**

### **5.2 Handle Outliers**
- [ ] Detect: IQR method, Z-score
- [ ] Decide: Keep, cap, remove, transform
- [ ] Document outlier handling strategy

### **5.3 Feature Scaling**
**RULE 9: Scaling rules theo algorithm**

| Algorithm | Scaling cần? | Method |
|-----------|--------------|--------|
| Logistic Regression | ✅ CẦN | StandardScaler |
| SVM | ✅ CẦN | StandardScaler |
| Neural Networks | ✅ CẦN | StandardScaler hoặc MinMaxScaler |
| KNN | ✅ CẦN | StandardScaler |
| Naive Bayes | ❌ KHÔNG | - |
| Decision Tree | ❌ KHÔNG | - |
| Random Forest | ❌ KHÔNG | - |
| XGBoost | ❌ KHÔNG | - |

**RULE 10: Fit scaler chỉ trên training!**
```python
# ✅ ĐÚNG
scaler = StandardScaler()
scaler.fit(X_train)  # Chỉ học từ train
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ❌ SAI
scaler.fit(pd.concat([X_train, X_test]))  # Leak!
```

**StandardScaler vs MinMaxScaler:**
```
StandardScaler: (x - mean) / std
- Kết quả: mean=0, std=1
- Dùng khi: Data có outliers, distribution tương đối normal

MinMaxScaler: (x - min) / (max - min)
- Kết quả: range [0, 1]
- Dùng khi: Cần bounded range, neural networks với sigmoid/tanh
```

---

## ✅ PHASE 6: MODEL SELECTION & TRAINING

### **6.1 Baseline Model**
**RULE 11: Luôn bắt đầu với baseline đơn giản!**
- [ ] Classification: Dummy classifier (most frequent)
- [ ] Regression: Mean/median predictor
- [ ] Mục đích: Có baseline để so sánh

### **6.2 Chọn Algorithms**
**RULE 12: Chọn algorithm phù hợp với bài toán**

**Cho Classification:**
```
Dataset nhỏ (<10K):
├─ Linear data → Logistic Regression
├─ Non-linear → SVM with RBF kernel
└─ Tree-based → Random Forest, XGBoost

Dataset lớn (>10K):
├─ Deep Learning nếu có: images, text, complex patterns
├─ XGBoost/LightGBM cho tabular data
└─ Ensemble methods
```

**Cho Regression:**
```
├─ Linear Regression (baseline)
├─ Ridge/Lasso (nếu có nhiều features)
├─ Random Forest Regressor
├─ XGBoost/LightGBM
└─ Neural Networks (dataset lớn)
```

### **6.3 Training Strategy**
**RULE 13: Train nhiều models và so sánh**
- [ ] Ít nhất 3-5 algorithms khác nhau
- [ ] So sánh trên validation set
- [ ] Track training time, model size, inference speed

**RULE 14: Cross-validation cho dataset nhỏ**
```python
from sklearn.model_selection import cross_val_score

# K-fold CV (thường k=5 hoặc 10)
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
print(f"CV Accuracy: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")
```

**Khi nào dùng CV:**
- Dataset nhỏ (<5000 samples)
- Cần đánh giá robust
- Có thời gian training

**Khi nào KHÔNG dùng CV:**
- Dataset lớn (>50K) → Chỉ cần train/val/test split
- Time series data → Dùng TimeSeriesSplit
- Production với time constraints

---

## ✅ PHASE 7: MODEL EVALUATION

### **7.1 Evaluation Metrics**
**RULE 15: Dùng nhiều metrics, không chỉ accuracy!**

**Classification:**
```python
from sklearn.metrics import classification_report, confusion_matrix

# Must-have metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(f"TN={cm[0,0]}, FP={cm[0,1]}")
print(f"FN={cm[1,0]}, TP={cm[1,1]}")

# Advanced
roc_auc = roc_auc_score(y_test, y_proba)
```

**RULE 16: Hiểu trade-offs của từng metric**
```
Accuracy: Tổng quan, nhưng sai lệch với imbalanced data
Precision: "Trong các dự đoán positive, có bao nhiêu đúng?"
          → Quan trọng khi False Positive tốn kém
Recall: "Trong các positive thật, bắt được bao nhiêu?"
       → Quan trọng khi False Negative nguy hiểm (security, medical)
F1: Cân bằng Precision và Recall
```

**RULE 17: Chọn metric theo business context**
```
Spam detection: Precision cao (ít xóa nhầm email quan trọng)
Cancer detection: Recall cao (không bỏ sót bệnh nhân)
Fraud detection: F1 hoặc Recall cao (không bỏ sót gian lận)
Recommendation: MAP, NDCG
```

### **7.2 Confusion Matrix Analysis**
**RULE 18: Luôn phân tích confusion matrix chi tiết**
```
                 Predicted
              Negative  Positive
Actual Neg      TN        FP      ← Type I Error
       Pos      FN        TP      ← Type II Error

FP (False Positive): Báo động giả → Làm phiền user
FN (False Negative): Bỏ sót → Nguy hiểm!
```

### **7.3 Learning Curves**
- [ ] Plot training vs validation curves
- [ ] Identify overfitting/underfitting
- [ ] Decide next steps

---

## ✅ PHASE 8: HYPERPARAMETER TUNING

### **8.1 Tuning Strategy**
**RULE 19: Tune trên validation set, KHÔNG phải test set!**

```python
# ❌ SAI - Tune trên test set
best_params = tune_on_test_set()  # Test set leak!

# ✅ ĐÚNG - Tune trên validation set
best_params = tune_on_validation_set()
final_test = evaluate_on_test_set(best_params)
```

### **8.2 Tuning Methods**
**RULE 20: Bắt đầu với Grid Search, sau đó Random Search**

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Grid Search (nhỏ, exhaustive)
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['rbf', 'linear']
}
grid = GridSearchCV(SVM(), param_grid, cv=5)

# Random Search (lớn, faster)
param_dist = {
    'n_estimators': [50, 100, 200, 500],
    'max_depth': [5, 10, 20, None],
    'min_samples_split': [2, 5, 10]
}
random = RandomizedSearchCV(RF(), param_dist, n_iter=20, cv=5)
```

**Advanced: Bayesian Optimization**
- Dùng cho expensive models (deep learning)
- Libraries: Optuna, Hyperopt

### **8.3 Overfitting Prevention**
**RULE 21: Watch out for overfitting signs**
```
Signs:
- Train accuracy >> Test accuracy (>10% gap)
- Model quá phức tạp
- Training loss giảm nhưng val loss tăng

Solutions:
- Regularization (L1, L2, dropout)
- Reduce model complexity
- Get more data
- Data augmentation
- Early stopping
```

---

## ✅ PHASE 9: MODEL COMPARISON

### **9.1 Comparison Criteria**
**RULE 22: So sánh đa chiều, không chỉ accuracy**

| Model | Accuracy | Precision | Recall | F1 | Training Time | Inference Time | Model Size |
|-------|----------|-----------|--------|----|--------------:|---------------:|-----------:|
| LR | 0.85 | 0.83 | 0.87 | 0.85 | 0.1s | 0.001s | 1 KB |
| RF | 0.92 | 0.90 | 0.94 | 0.92 | 5s | 0.05s | 500 KB |
| NN | 0.93 | 0.91 | 0.95 | 0.93 | 300s | 0.02s | 10 MB |

### **9.2 Selection Criteria**
- [ ] Performance metrics (primary)
- [ ] Inference speed (production requirement)
- [ ] Model size (deployment constraint)
- [ ] Interpretability (business requirement)
- [ ] Training time (iteration speed)
- [ ] Maintenance cost

---

## ✅ PHASE 10: FINAL EVALUATION

### **10.1 Test Set Evaluation**
**RULE 23: Test set chỉ dùng MỘT LẦN cuối cùng!**
```python
# ❌ SAI - Test nhiều lần
for model in models:
    test_score = evaluate(model, X_test, y_test)
    if test_score > best:
        best_model = model  # Overfitting to test set!

# ✅ ĐÚNG - Select trên validation, test cuối
best_model = select_on_validation()
final_score = evaluate_once(best_model, X_test, y_test)
```

### **10.2 Final Checks**
- [ ] Evaluate trên test set MỘT LẦN duy nhất
- [ ] Document tất cả metrics
- [ ] Verify model meets requirements
- [ ] Test edge cases
- [ ] Analyze errors (FP, FN cases)

---

## ✅ PHASE 11: MODEL DEPLOYMENT

### **11.1 Model Saving**
**RULE 24: Save model và preprocessing objects**
```python
import pickle

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

# Save scaler (QUAN TRỌNG!)
pickle.dump(scaler, open('scaler.pkl', 'wb'))

# Save feature names
pickle.dump(feature_names, open('features.pkl', 'wb'))
```

### **11.2 Inference Pipeline**
```python
def predict_new_data(new_data):
    # 1. Load model và scaler
    model = pickle.load(open('model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    
    # 2. Preprocessing (giống training!)
    new_data_scaled = scaler.transform(new_data)
    
    # 3. Predict
    prediction = model.predict(new_data_scaled)
    probability = model.predict_proba(new_data_scaled)
    
    return prediction, probability
```

### **11.3 Production Checklist**
- [ ] API endpoint ready
- [ ] Input validation
- [ ] Error handling
- [ ] Logging
- [ ] Monitoring setup
- [ ] A/B testing plan
- [ ] Rollback plan

---

## ✅ PHASE 12: MONITORING & MAINTENANCE

### **12.1 Model Monitoring**
**RULE 25: Luôn monitor model trong production**
- [ ] Track performance metrics daily/weekly
- [ ] Monitor data drift
- [ ] Monitor concept drift
- [ ] Set up alerts for anomalies

### **12.2 Retraining Strategy**
- [ ] Schedule periodic retraining
- [ ] Retrain when performance drops >5%
- [ ] Retrain when data distribution changes
- [ ] Version control for models

---

## 📋 QUICK CHECKLIST - IN RA DÁN TƯỜNG

```
□ Hiểu bài toán & chọn metrics
□ EDA: shape, dtypes, missing, distribution, correlation
□ Split data: train/val/test (stratify nếu classification)
□ Check data leakage: overlap = 0
□ Handle missing values (fit trên train only)
□ Feature engineering & selection
□ Scaling (fit trên train only, theo algorithm)
□ Train baseline model
□ Train multiple models (3-5)
□ Cross-validation (dataset nhỏ)
□ Evaluate với nhiều metrics
□ Phân tích confusion matrix
□ Hyperparameter tuning (trên validation)
□ So sánh models đa chiều
□ Final test evaluation (MỘT LẦN)
□ Save model + scaler + features
□ Deploy với monitoring
□ Set up retraining pipeline
```

---

## 🚨 TOP 10 LỖI THƯỜNG GẶP

1. **Data Leakage** - Fit scaler/imputer trên toàn bộ data
2. **Không stratify** - Class imbalance giữa train/test
3. **Quên set random_state** - Kết quả không reproducible
4. **Overfit to test set** - Test nhiều lần và chọn best
5. **Chỉ nhìn accuracy** - Bỏ qua precision, recall, F1
6. **Không check imbalanced data** - Accuracy giả tạo cao
7. **Scaling sai** - Scale test data độc lập train
8. **Quên save scaler** - Production không scale đúng
9. **Không validate edge cases** - Model fail ở corner cases
10. **Không monitor production** - Performance degradation

---



---

# 📧 PHASE 1: HIỂU BÀI TOÁN - EMAIL THREAT DETECTION

---

## SLIDE 1: BÀI TOÁN CỤ THỂ

**Tên dự án:** Email Threat Detection System

**Mô tả:** 
Xây dựng hệ thống AI tự động phân loại email vào 5 categories:
- Legitimate (Hợp pháp)
- Spam (Thư rác)
- Phishing (Lừa đảo)
- Malware (Chứa mã độc)
- BEC (Business Email Compromise)

**Bối cảnh:**
- Công ty nhận 100,000 emails/ngày
- 30% là threats
- Cần phát hiện tự động trong <1 giây

---

## SLIDE 2: ✅ 1.1 - XÁC ĐỊNH LOẠI BÀI TOÁN

### **Câu hỏi:** Đây là bài toán gì?

**Phân tích:**

**✅ Classification** (Phân loại)
- Đầu vào: Email (text + metadata)
- Đầu ra: 1 trong 5 categories
- Có labeled data để học

**Loại classification:**
- ✅ **Multiclass Classification** (5 classes)
- ❌ Không phải Binary (chỉ có 2 classes)
- ❌ Không phải Multilabel (1 email chỉ thuộc 1 class)
- ❌ Không phải Regression (không dự đoán số)

---

## SLIDE 3: CÁC CLASS CHI TIẾT

| Class | Label | Mô tả | Ví dụ |
|-------|-------|-------|-------|
| **Legitimate** | 0 | Email công việc bình thường | "Meeting at 3 PM" |
| **Spam** | 1 | Quảng cáo, marketing không mong muốn | "Buy cheap viagra now!" |
| **Phishing** | 2 | Giả mạo để đánh cắp thông tin | "Verify your bank account" |
| **Malware** | 3 | Chứa attachment/link độc hại | "Invoice.pdf" (malicious) |
| **BEC** | 4 | Giả mạo CEO/CFO yêu cầu chuyển tiền | "CEO: Wire $50K urgently" |

---

## SLIDE 4: PHÂN BIỆT CÁC LOẠI THREATS

### **Spam vs Phishing vs BEC**

**Spam:**
- Mục tiêu: Quảng cáo, bán hàng
- Gửi hàng loạt (bulk)
- Không nhắm mục tiêu cụ thể
- Ít nguy hiểm (chỉ làm phiền)

**Phishing:**
- Mục tiêu: Đánh cắp credentials
- Giả mạo tổ chức (bank, PayPal)
- Có link giả mạo
- Nguy hiểm trung bình

**BEC:**
- Mục tiêu: Lừa chuyển tiền
- Giả mạo người trong công ty (CEO, CFO)
- Nhắm mục tiêu cụ thể
- RẤT NGUY HIỂM (loss trung bình $50K-$5M)

**Malware:**
- Mục tiêu: Cài đặt virus/ransomware
- Có attachment hoặc link độc hại
- Cực kỳ nguy hiểm

---

## SLIDE 5: VÍ DỤ CỤ THỂ TỪNG LOẠI

### **1. Legitimate Email**
```
From: john@company.com
To: team@company.com
Subject: Q4 Sales Report Ready

Hi Team,

The Q4 sales report has been finalized and uploaded 
to SharePoint. Please review by Friday.

Best regards,
John
```

**Đặc điểm:**
- From internal domain
- Business tone
- Clear purpose
- No urgency pressure
- No suspicious links

---

## SLIDE 6: VÍ DỤ - SPAM

### **2. Spam Email**
```
From: deals@bestoffers2024.com
To: you@company.com
Subject: 🔥 LOSE 20 LBS IN 2 WEEKS! LIMITED OFFER!

CONGRATULATIONS! You've been selected for our 
EXCLUSIVE weight loss program!

✅ Lose weight FAST
✅ No exercise needed
✅ 100% natural ingredients

Click here NOW! Offer expires in 24 hours!
[SUSPICIOUS LINK]

Unsubscribe: [tiny link]
```

**Đặc điểm:**
- External, unknown sender
- Excessive punctuation (!!!)
- CAPITALS và emojis
- Too good to be true claims
- Generic greeting
- Unsubscribe link (but still unwanted)

---

## SLIDE 7: VÍ DỤ - PHISHING

### **3. Phishing Email**
```
From: security@paypa1.com  ← Chú ý: "1" thay "l"
To: victim@company.com
Subject: Urgent: Your PayPal Account Has Been Suspended

Dear Valued Customer,

We have detected unusual activity on your PayPal account.
For your security, we have SUSPENDED your account.

To restore access, please verify your information immediately:

[CLICK HERE TO VERIFY] ← Link giả: http://paypa1-verify.com

If you do not verify within 24 hours, your account will 
be permanently closed.

Thank you,
PayPal Security Team
```

**Đặc điểm:**
- Giả mạo sender (typosquatting: paypa1 vs paypal)
- Urgency + Fear tactics
- Request credentials
- Suspicious link domain
- Generic greeting "Dear Customer"
- Threat of account closure

---

## SLIDE 8: VÍ DỤ - MALWARE

### **4. Malware Delivery Email**
```
From: accounting@suspicious-domain.com
To: finance@company.com
Subject: Invoice #2024-10892

Dear Sir/Madam,

Please find attached the invoice for your recent order.

Payment is due within 7 days.

Attachment: Invoice_Oct_2024.pdf.exe  ← Nguy hiểm!

Regards,
Accounting Department
```

**Đặc điểm:**
- Có attachment đáng ngờ (.exe, .zip, .scr)
- Double extension (.pdf.exe)
- Generic content
- External sender pretending to be business
- No specific details about "order"
- Low IP reputation

---

## SLIDE 9: VÍ DỤ - BEC (Business Email Compromise)

### **5. BEC Email**
```
From: ceo@company.com  ← Email thật hoặc spoofed
To: cfo@company.com
Subject: Urgent Wire Transfer Required

Hi Sarah,

I'm in a meeting with potential investors and we need 
to wire $80,000 immediately to secure the deal.

Please process this transfer ASAP:
Bank: [Details]
Account: [Number]
Reason: Investment deposit

This is time-sensitive and confidential. Don't mention 
this to anyone until I'm back.

Thanks,
Michael Chen
CEO
```

**Đặc điểm:**
- Giả mạo executive (CEO, CFO)
- Urgency + Confidentiality
- Request wire transfer
- Bypass normal approval process
- "Don't tell anyone"
- Time pressure
- Sophisticated language (không như spam)

---

## SLIDE 10: ✅ 1.2 - XÁC ĐỊNH SUCCESS METRICS

### **Câu hỏi:** Metric nào quan trọng nhất?

**Phân tích theo business impact:**

| Threat Type | Business Impact | Primary Metric |
|-------------|-----------------|----------------|
| Spam | Thấp (chỉ phiền) | Precision |
| Phishing | Cao (mất credentials) | Recall |
| Malware | Rất cao (ransomware) | Recall |
| BEC | Cực cao ($50K-$5M loss) | Recall |

**Kết luận:** 
- **Recall** quan trọng hơn Precision
- Không được bỏ sót threats (FN nguy hiểm!)
- Chấp nhận một số FP (block nhầm, có thể recover)

---

## SLIDE 11: METRIC REQUIREMENTS CỤ THỂ

### **Minimum Acceptable Performance:**

**Overall:**
- Accuracy: >95%
- Macro F1-Score: >0.90

**Per-Class Requirements:**

| Class | Recall (Min) | Precision (Min) | Lý do |
|-------|-------------|-----------------|-------|
| Legitimate | 98% | 95% | Không block nhầm email quan trọng |
| Spam | 90% | 95% | OK nếu bỏ sót một số (ít nguy hiểm) |
| Phishing | 95% | 90% | KHÔNG được bỏ sót |
| Malware | 98% | 90% | TUYỆT ĐỐI không bỏ sót |
| BEC | 99% | 85% | Ưu tiên catch tất cả, dù có FP |

**Giải thích:**
- BEC recall 99%: Bỏ sót 1% = $50K-$5M loss!
- Legitimate precision 95%: Block nhầm 5% email = chấp nhận được
- Spam recall 90%: Bỏ sót 10% spam = OK, user có thể delete manually

---

## SLIDE 12: CONFUSION MATRIX ANALYSIS

### **Cost Analysis:**

**False Positive (Loại I Error):**
```
Legitimate → Predicted as Threat
Cost: User annoyance, productivity loss
Severity: Medium
```

**False Negative (Loại II Error):**
```
Spam → Predicted as Legitimate: Low cost
Phishing → Predicted as Legitimate: High cost
Malware → Predicted as Legitimate: Very high cost
BEC → Predicted as Legitimate: CRITICAL cost
```

**Trade-off Decision:**
→ Ưu tiên **Recall** (catch threats) hơn **Precision** (avoid FP)
→ Thiết lập threshold để favor Recall

---

## SLIDE 13: ✅ 1.3 - THU THẬP YÊU CẦU HỆ THỐNG

### **Performance Requirements:**

**1. Inference Time:**
- Requirement: <1 second/email
- Lý do: Real-time filtering cần nhanh
- Giới hạn: Không dùng models quá phức tạp

**2. Model Size:**
- Requirement: <100 MB
- Lý do: Deploy trên email server (limited memory)
- Giới hạn: Không dùng deep learning nặng

**3. Throughput:**
- Requirement: 100 emails/second
- Lý do: Peak time có thể đến 360K emails/hour
- Giải pháp: Cần batch processing hoặc parallel

---

## SLIDE 14: YÊU CẦU HỆ THỐNG (tt)

### **4. Interpretability:**
- Requirement: HIGH
- Lý do: 
  - Cần giải thích tại sao email bị block
  - Compliance/audit requirements
  - User có thể appeal decision
- Giới hạn: 
  - Ưu tiên: Logistic Regression, Tree-based
  - Tránh: Black-box deep learning

**5. Update Frequency:**
- Requirement: Retrain weekly
- Lý do: Threats evolve rapidly
- Cần: Automated training pipeline

**6. Deployment:**
- Environment: On-premise email server
- OS: Linux (Ubuntu 20.04)
- Integration: SMTP gateway
- Fallback: Rule-based backup system

---

## SLIDE 15: YÊU CẦU COMPLIANCE & LEGAL

### **Privacy & Legal:**

**GDPR Compliance:**
- [ ] Không store email content lâu dài
- [ ] Chỉ extract features cần thiết
- [ ] Có consent để analyze emails
- [ ] Right to explanation (interpretability)

**Company Policy:**
- [ ] Không scan personal emails (chỉ work emails)
- [ ] Log tất cả decisions để audit
- [ ] Có manual review process cho disputed cases
- [ ] Encrypt all data in transit và at rest

**Ethical Considerations:**
- [ ] False positives: Có process để unblock
- [ ] Transparency: User biết email được scan
- [ ] No discrimination: Model không bias theo sender

---

## SLIDE 16: STAKEHOLDER REQUIREMENTS

### **Các bên liên quan:**

**1. End Users (Employees):**
- Muốn: Ít false positives (không block nhầm)
- Muốn: Interface để report FP/FN
- Muốn: Nhanh (không delay emails)

**2. IT Security Team:**
- Muốn: High recall (catch all threats)
- Muốn: Dashboard để monitor
- Muốn: Logs để investigate incidents

**3. Management:**
- Muốn: ROI positive (giảm losses từ BEC)
- Muốn: Compliance đảm bảo
- Muốn: Low maintenance cost

**4. Legal/Compliance:**
- Muốn: Audit trail đầy đủ
- Muốn: GDPR compliant
- Muốn: Explainable decisions

---

## SLIDE 17: TÓM TẮT PHASE 1

### **✅ Những gì đã xác định:**

**1. Problem Type:**
- Multiclass Classification (5 classes)
- Supervised Learning
- Text + Metadata input

**2. Success Metrics:**
- Primary: Recall (per-class: 90-99%)
- Secondary: Precision (per-class: 85-95%)
- Overall: Accuracy >95%, Macro F1 >0.90

**3. Constraints:**
- Inference: <1 second/email
- Model size: <100 MB
- Interpretability: HIGH
- Throughput: 100 emails/second

**4. Compliance:**
- GDPR compliant
- Audit trail required
- Privacy-preserving

---

## SLIDE 18: DECISION SUMMARY TABLE

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| **Problem Type** | Multiclass Classification (5 classes) | Clear categories, labeled data available |
| **Primary Metric** | Recall (weighted by severity) | Cost of FN >> Cost of FP in security |
| **Secondary Metric** | Precision, F1-Score | Balance needed for user experience |
| **Minimum Recall** | BEC: 99%, Malware: 98%, Phishing: 95%, Others: 90% | Based on financial impact |
| **Model Complexity** | Medium (not deep learning) | Interpretability + Speed requirements |
| **Update Cadence** | Weekly retraining | Threats evolve rapidly |
| **Deployment** | On-premise email gateway | Data privacy requirements |

---

## SLIDE 19: COMPARISON - EMAIL THREATS

### **Độ nguy hiểm (Severity):**

```
Legitimate ━━━━━━━━━━ 0% risk
    ↓
Spam       ━━━━━━━━━━ 10% risk (annoyance only)
    ↓
Phishing   ━━━━━━━━━━ 60% risk (credential theft)
    ↓
Malware    ━━━━━━━━━━ 80% risk (ransomware, data loss)
    ↓
BEC        ━━━━━━━━━━ 100% risk (direct financial loss $50K-$5M)
```

**Kết luận:**
→ Model phải tập trung detect BEC > Malware > Phishing > Spam

---

## SLIDE 20: NEXT STEPS - PHASE 2

**Chuẩn bị cho Phase 2 (Data Collection):**

**Cần thu thập:**
- [ ] 50,000+ emails đã labeled (10K/class)
- [ ] Cân bằng distribution hoặc có strategy cho imbalance
- [ ] Email headers (From, To, Subject, Date, Reply-To)
- [ ] Email body (text + HTML)
- [ ] Attachments info (filename, type, size)
- [ ] URLs trong email
- [ ] Metadata (IP sender, SPF/DKIM status)

**Sources:**
- Production email logs (with consent)
- Public datasets: Enron, SpamAssassin
- Honeypots để catch threats
- User reports (manual labels)

---

## SLIDE 21: FEATURES PREVIEW (Sẽ DETAIL Ở PHASE 3)

**Categories của features:**

**1. Sender Features:**
- Email domain reputation
- SPF/DKIM/DMARC pass/fail
- Sender trong company whitelist?
- Sender history (first time sender?)

**2. Content Features:**
- Subject line keywords
- Body text (TF-IDF, sentiment)
- Urgency words count
- Money amount mentions
- URL count và reputation
- Attachment presence & type

**3. Behavioral Features:**
- Time of send (work hours?)
- Reply patterns
- Email chain analysis

---

## SLIDE 22: EXPECTED CHALLENGES

**Challenges dự kiến:**

**1. Imbalanced Data:**
- BEC rất hiếm (~0.1% emails)
- Legitimate rất nhiều (~70%)
- Solution: SMOTE, class weights, stratified split

**2. Evolving Threats:**
- Attackers thay đổi tactics liên tục
- Solution: Weekly retraining, continuous monitoring

**3. Sophisticated BEC:**
- Rất giống legitimate emails
- Language professional, no obvious red flags
- Solution: Behavioral features, executive impersonation detection

**4. False Positives Impact:**
- Block nhầm legitimate emails = serious
- Solution: Lower threshold, manual review queue

---

## SLIDE 23: RISK MITIGATION

**Risk Management:**

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| High FP rate | High | Medium | Lower threshold, A/B testing |
| Miss critical BEC | Critical | Low | Prioritize recall, manual review for high-value targets |
| Model drift | High | High | Weekly retraining, performance monitoring |
| Adversarial attacks | Medium | Medium | Ensemble models, anomaly detection backup |
| Privacy violation | Critical | Low | Strict data governance, compliance checks |

---

## SLIDE 24: SUCCESS CRITERIA CHECKLIST

**Project sẽ thành công nếu:**

- [ ] Overall accuracy >95%
- [ ] BEC recall ≥99% (bỏ sót <1%)
- [ ] Malware recall ≥98%
- [ ] Phishing recall ≥95%
- [ ] Legitimate precision ≥95% (FP <5%)
- [ ] Inference time <1s per email
- [ ] Model size <100MB
- [ ] Can explain any decision (interpretability)
- [ ] GDPR compliant
- [ ] ROI positive (losses prevented > system cost)

---

## SLIDE 25: PHASE 1 DELIVERABLES

**Documents đã hoàn thành:**

✅ **Problem Definition Document:**
- Problem type: Multiclass classification
- 5 classes defined with examples
- Use cases và business context

✅ **Metrics Requirement Document:**
- Primary: Recall (per-class thresholds)
- Secondary: Precision, F1, Accuracy
- Business justification cho từng metric

✅ **System Requirements Document:**
- Performance: <1s inference, 100 emails/sec
- Model constraints: <100MB, interpretable
- Deployment: On-premise, Linux
- Compliance: GDPR, audit trail

✅ **Stakeholder Sign-off:**
- Requirements approved by IT Security, Legal, Management

---

## SLIDE 26: APPROVAL CHECKLIST

**Trước khi proceed to Phase 2:**

**Technical Approval:**
- [ ] Data Science Lead: Metrics achievable?
- [ ] ML Engineer: Technical constraints realistic?
- [ ] Security Team: Requirements comprehensive?

**Business Approval:**
- [ ] IT Director: Budget approved?
- [ ] Legal: Compliance requirements clear?
- [ ] CFO: ROI projection acceptable?

**Risk Assessment:**
- [ ] Risk register reviewed
- [ ] Mitigation strategies approved
- [ ] Fallback plan documented

**→ ALL APPROVED? Proceed to Phase 2! 🚀**

---

## SLIDE 27: TÓM TẮT - PHASE 1 COMPLETE

**Phase 1: Hiểu Bài Toán ✅**

```
✅ 1.1 Xác định loại: Multiclass Classification (5 classes)
✅ 1.2 Success Metrics: Recall-focused, per-class thresholds
✅ 1.3 System Requirements: Speed, size, interpretability
✅ Stakeholder alignment: All parties agree
✅ Risk assessment: Identified & mitigated
✅ Go/No-Go decision: GO! 🚀
```

**Next Phase 2: Data Collection & EDA**
- Thu thập 50K+ labeled emails
- Analyze distribution
- Check data quality
- Identify challenges

---

## SLIDE 28: BÀI TẬP

**Exercise: Apply Phase 1 to Your Problem**

Chọn 1 trong các bài toán sau và complete Phase 1:

**Option 1: Credit Card Fraud Detection**
- Binary classification
- Highly imbalanced (0.1% fraud)
- Real-time requirement

**Option 2: Customer Churn Prediction**
- Binary classification
- Balanced data
- Interpretability critical

**Option 3: Product Review Sentiment**
- Multiclass (5 stars)
- Large dataset available
- Speed not critical

**Yêu cầu:** Complete slides 10-16 template for your chosen problem

---



---

# 📊 PHASE 1: HIỂU BÀI TOÁN - MALWARE THREAT DETECTION WITH AI

---

## SLIDE 1: MODULE 5 OVERVIEW

**Welcome to Module 5: Advanced Malware Analysis**

**Focus Areas:**
- AI-driven detection techniques
- Modern malware classification
- Real-time threat response

**Duration:** Comprehensive deep-dive session

**Learning Outcomes:**
- Master modern malware detection
- Build ML models for threat classification
- Deploy production-ready systems

---

## SLIDE 2: BÀI TOÁN THỰC TẾ

**Tình huống:**
Bạn là Security Analyst tại công ty antivirus

**Thực trạng hàng ngày:**
- 450,000+ malware mẫu mới mỗi ngày
- Signature-based detection bị bypass bởi polymorphic malware
- Zero-day malware không có signature
- Phân tích thủ công: 1-2 samples/giờ
- Cần: Phân tích hàng nghìn samples/giờ

**Thách thức:**
→ Làm thế nào phát hiện malware chưa từng thấy?

---

## SLIDE 3: PHASE 1.1 - XÁC ĐỊNH LOẠI BÀI TOÁN

**Câu hỏi 1: Đây là loại bài toán gì?**

**Phân tích:**
- Input: File executable (.exe, .dll, .apk)
- Output: Malware hay Benign?
- Có label sẵn (malware/benign)
- 2 classes

**→ Đây là bài toán BINARY CLASSIFICATION**

---

## SLIDE 4: TẠI SAO LÀ BINARY CLASSIFICATION?

**Binary Classification nghĩa là:**
- Chỉ có 2 classes (categories)
- Class 0: Benign (file an toàn)
- Class 1: Malware (file độc hại)

**So sánh với các loại khác:**
```
Binary:      Malware vs Benign
Multiclass:  Trojan vs Worm vs Virus vs Ransomware
Regression:  Dự đoán risk score (0-100)
Clustering:  Nhóm malware có hành vi tương tự
```

**→ Lab này: Binary Classification**

---

## SLIDE 5: NÂng CAO - MULTICLASS CLASSIFICATION

**Nếu muốn phân loại chi tiết hơn:**

**Multiclass Problem:**
- Class 0: Benign
- Class 1: Trojan
- Class 2: Worm
- Class 3: Virus
- Class 4: Ransomware
- Class 5: Rootkit
- Class 6: Spyware

**Khác biệt:**
- Model phức tạp hơn
- Cần nhiều data hơn mỗi class
- Harder to achieve high accuracy

---

## SLIDE 6: PHASE 1.2 - XÁC ĐỊNH SUCCESS METRICS

**Câu hỏi 2: Làm sao biết model "tốt"?**

**Không chỉ là Accuracy!**

Với antivirus, cần cân nhắc:
- False Positive (FP): File tốt bị nhận nhầm là malware
- False Negative (FN): Malware bị bỏ sót

**→ Cần định nghĩa rõ success metrics**

---

## SLIDE 7: HIỂU FALSE POSITIVE VÀ FALSE NEGATIVE

**False Positive (Type I Error):**
```
Truth: File AN TOÀN
Model dự đoán: MALWARE
Hậu quả: 
- User không dùng được software hợp pháp
- Mất lòng tin vào antivirus
- Tốn thời gian whitelist
```

**False Negative (Type II Error):**
```
Truth: MALWARE
Model dự đoán: An toàn
Hậu quả:
- Malware vào được hệ thống
- Data bị đánh cắp
- Ransomware mã hóa files
- ★ NGUY HIỂM HƠN!
```

---

## SLIDE 8: CHỌN METRICS CHO ANTIVIRUS

**Trong antivirus: False Negative nguy hiểm hơn!**

**Priority Metrics (Theo thứ tự):**

1. **Recall (Sensitivity)** - Cao nhất!
   - "Trong tất cả malware thật, bắt được bao nhiêu?"
   - Target: >95% (bỏ sót <5%)

2. **Precision**
   - "Trong các dự đoán malware, đúng bao nhiêu?"
   - Target: >90% (chấp nhận 10% FP)

3. **F1-Score**
   - Cân bằng Precision và Recall
   - Target: >0.92

4. **Accuracy**
   - Tổng quan
   - Target: >93%

---

## SLIDE 9: CÔNG THỨC METRICS

**Confusion Matrix:**
```
                Predicted
              Benign  Malware
Actual Benign   TN      FP
       Malware  FN      TP
```

**Formulas:**
```
Accuracy  = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)  ← Quan trọng nhất!
F1-Score  = 2 × (Precision × Recall) / (Precision + Recall)
```

---

## SLIDE 10: VÍ DỤ TÍNH METRICS

**Scenario:** Test trên 1000 files
```
True Benign: 700 files
True Malware: 300 files

Model predictions:
- Detected correctly as Benign: 680 (TN)
- Benign wrongly as Malware: 20 (FP)
- Malware wrongly as Benign: 10 (FN) ← Nguy hiểm!
- Detected correctly as Malware: 290 (TP)
```

**Confusion Matrix:**
```
        Benign  Malware
Benign    680     20
Malware    10    290
```

---

## SLIDE 11: TÍNH TOÁN KẾT QUẢ

**Từ confusion matrix trước:**

```
Accuracy  = (680 + 290) / 1000 = 97.0%
Precision = 290 / (290 + 20) = 93.5%
Recall    = 290 / (290 + 10) = 96.7% ★
F1-Score  = 2 × (0.935 × 0.967) / (0.935 + 0.967) = 0.951
```

**Đánh giá:**
- ✅ Recall 96.7% → Tốt! Chỉ bỏ sót 10/300 malware
- ✅ Precision 93.5% → OK, chấp nhận 20 FP
- ✅ F1 0.951 → Excellent
- ✅ Model đạt yêu cầu!

---

## SLIDE 12: TARGET METRICS CHO PROJECT

**Minimum Requirements:**

| Metric | Target | Lý do |
|--------|--------|-------|
| **Recall** | **≥ 95%** | Không được bỏ sót >5% malware |
| Precision | ≥ 90% | Chấp nhận ≤10% false alarms |
| F1-Score | ≥ 0.92 | Cân bằng tốt |
| Accuracy | ≥ 93% | Tổng quan |

**Stretch Goals (Lý tưởng):**
- Recall: 98%
- Precision: 95%
- F1: 0.96

---

## SLIDE 13: PHASE 1.3 - YÊU CẦU VỀ TỐC ĐỘ

**Câu hỏi 3: Model phải nhanh như thế nào?**

**Real-time Scanning Requirements:**
- User scan 1 file: Kết quả trong <1 giây
- Background scan: 1000+ files/phút
- On-access scan: <100ms (không làm chậm system)

**Training Time:**
- Có thể lâu (vài giờ đến vài ngày)
- Chỉ train 1 lần, dùng lại nhiều lần

**→ Inference speed quan trọng hơn training speed!**

---

## SLIDE 14: YÊU CẦU MODEL SIZE

**Deployment Constraints:**

**Desktop Antivirus:**
- Model size: <100 MB
- RAM usage: <500 MB
- CPU only (không có GPU)

**Mobile Antivirus:**
- Model size: <10 MB
- RAM usage: <100 MB
- Battery friendly

**Cloud-based:**
- Model size: Không giới hạn
- Có GPU
- Nhưng cần internet

**→ Lab này: Desktop deployment**

---

## SLIDE 15: YÊU CẦU VỀ INTERPRETABILITY

**Câu hỏi 4: Cần giải thích được không?**

**Hai trường phái:**

**Black-box Models (Deep Learning):**
- ✅ Accuracy cao hơn
- ❌ Không giải thích được
- ❌ Khó debug

**Interpretable Models (Traditional ML):**
- ✅ Hiểu được tại sao dự đoán vậy
- ✅ Dễ debug
- ✅ User tin tưởng hơn
- ❌ Accuracy có thể thấp hơn một chút

**→ Lab này: Traditional ML (interpretable)**

---

## SLIDE 16: TẠI SAO CẦN INTERPRETABILITY?

**Use Cases cần giải thích:**

**1. Security Analyst Review:**
```
File: suspicious.exe
Prediction: MALWARE (95% confidence)
Reasons:
- Packs code with UPX
- Modifies registry keys
- Makes network connections to unknown IPs
- High entropy section (encrypted code)
```

**2. False Positive Analysis:**
```
File: legitimate.exe (Office Software)
Prediction: MALWARE (60% confidence)
Why wrong:
- Legitimate code packer
- Normal registry access
→ Add to whitelist
```

---

## SLIDE 17: DEPLOYMENT ENVIRONMENT

**Câu hỏi 5: Model sẽ chạy ở đâu?**

**3 Options:**

**Option 1: On-device (Endpoint)**
- ✅ Offline, không cần internet
- ✅ Fast, low latency
- ✅ Privacy (data không rời máy)
- ❌ Limited resources

**Option 2: Cloud-based**
- ✅ Powerful, có GPU
- ✅ Dễ update model
- ❌ Cần internet
- ❌ Latency cao

**Option 3: Hybrid**
- Light model on-device
- Heavy analysis in cloud

**→ Lab này: On-device (endpoint)**

---

## SLIDE 18: TÓM TẮT BÀI TOÁN

**Bài toán được định nghĩa rõ:**

```
Problem Type: Binary Classification
Classes: 
  - 0 = Benign (safe files)
  - 1 = Malware (malicious files)

Success Metrics:
  - Recall ≥ 95% (priority #1)
  - Precision ≥ 90%
  - F1-Score ≥ 0.92
  - Accuracy ≥ 93%

Performance Requirements:
  - Inference: <1 second per file
  - Model size: <100 MB
  - CPU only (no GPU)

Deployment: Desktop endpoint
Interpretability: High (need explanations)
```

---

## SLIDE 19: INPUT VÀ OUTPUT

**INPUT: Executable File**
```
File types:
- Windows: .exe, .dll, .sys
- Android: .apk, .dex
- Linux: ELF binaries
- Scripts: .ps1, .bat, .sh

Typical size: 100 KB - 10 MB
```

**OUTPUT: Classification + Confidence**
```
{
  "prediction": "malware",
  "confidence": 0.95,
  "risk_level": "high",
  "detected_behaviors": [...]
}
```

---

## SLIDE 20: BUSINESS CONTEXT

**Stakeholders:**

**1. End Users**
- Muốn: Bảo vệ tốt, ít false positive
- KPI: User satisfaction score

**2. Security Team**
- Muốn: Detect rate cao, analysis tools
- KPI: Malware catch rate

**3. Product Team**
- Muốn: Fast, small size, easy deploy
- KPI: System performance

**4. Business**
- Muốn: Cost-effective, scalable
- KPI: Cost per detection, ROI

---

## SLIDE 21: COST ANALYSIS

**Cost của False Positive:**
- Support ticket: $50
- User frustration
- Potential churn
- Whitelist maintenance

**Cost của False Negative:**
- Data breach: $4.35M average
- Ransomware damage: $1.85M average
- Reputation loss
- Legal liability

**→ FN cost >> FP cost (hàng nghìn lần!)**
**→ Ưu tiên Recall cao!**

---

## SLIDE 22: CONSTRAINTS VÀ ASSUMPTIONS

**Technical Constraints:**
- Chỉ có file binary (không có source code)
- Không thể execute file (sandbox limit)
- Static analysis only
- Limited compute resources

**Assumptions:**
- File format valid (không corrupt)
- Có thể extract features
- Labels reliable (dataset quality)
- Malware behaviors stable (không thay đổi quá nhanh)

---

## SLIDE 23: SUCCESS CRITERIA - CHI TIẾT

**Định nghĩa "Success" rõ ràng:**

**Phase 1: Development (Lab)**
- Recall ≥ 95% trên test set
- F1-Score ≥ 0.92
- Model trains trong <30 phút
- Inference <1s per file

**Phase 2: Production (Real-world)**
- Maintain 95% recall for 90 days
- False positive rate <1% daily
- 99.9% uptime
- Handle 10K files/hour

---

## SLIDE 24: OUT OF SCOPE

**Những gì KHÔNG làm trong lab này:**

❌ Dynamic analysis (không chạy malware)
❌ Sandbox environment
❌ Network behavior analysis
❌ Real-time monitoring
❌ Automatic malware removal
❌ Cross-platform support (chỉ focus 1 platform)
❌ Production deployment pipeline

**→ Focus: Core ML model for static analysis**

---

## SLIDE 25: RELATED PROBLEMS

**Bài toán tương tự:**

**Spam Detection:**
- Binary classification
- Text analysis
- Similar metrics priority

**Fraud Detection:**
- Imbalanced data
- High cost of FN
- Real-time requirements

**Intrusion Detection:**
- Anomaly detection
- Network traffic analysis
- Same security domain

**→ Techniques có thể tái sử dụng!**

---

## SLIDE 26: BASELINE COMPARISON

**So với existing solutions:**

**Signature-based Antivirus:**
- Detection rate: 70-80%
- False positive: <0.1%
- Speed: Very fast
- ❌ Miss zero-day malware

**Behavioral Analysis:**
- Detection rate: 85-90%
- False positive: 5-10%
- Speed: Slow
- ❌ Need execution

**Our ML Approach (Target):**
- Detection rate: 95%+
- False positive: 1-2%
- Speed: Fast
- ✅ Detect unknown malware

---

## SLIDE 27: DATA REQUIREMENTS PREVIEW

**Cần bao nhiêu data?**

**Minimum:**
- 1,000 samples (500 benign + 500 malware)
- 10-50 samples per feature

**Good:**
- 10,000 samples (7,000 benign + 3,000 malware)
- Cover multiple malware families

**Ideal:**
- 100,000+ samples
- Balanced across families
- Recent samples (<1 year old)

**→ Lab này: 10,000 samples**

---

## SLIDE 28: FEATURE TYPES PREVIEW

**Cần extract features gì từ malware?**

**Static Features:**
- File properties (size, entropy, headers)
- PE structure (sections, imports, exports)
- String patterns (URLs, IPs, registry keys)
- Code characteristics (opcodes, API calls)

**→ Chi tiết ở Phase 2 (Feature Engineering)**

---

## SLIDE 29: TIMELINE ESTIMATION

**Project Timeline:**

```
Week 1: Data collection & EDA (2-3 days)
Week 2: Feature engineering (3-4 days)
Week 3: Model training & selection (2-3 days)
Week 4: Evaluation & tuning (2-3 days)
Week 5: Documentation & presentation (1-2 days)

Total: 4-5 weeks for complete project
Lab: 2-3 sessions (6-9 hours)
```

---

## SLIDE 30: RISK ANALYSIS

**Potential Risks:**

**Technical Risks:**
- Imbalanced dataset → Use stratification, class weights
- Feature extraction errors → Robust parsing
- Model overfitting → Cross-validation, regularization
- New malware families → Regular retraining

**Business Risks:**
- High false positive → Careful threshold tuning
- Slow inference → Model optimization
- Large model size → Compression techniques

---

## SLIDE 31: ETHICAL CONSIDERATIONS

**Ethics trong Malware Detection:**

**Privacy:**
- ✅ Analyze file structure only
- ❌ Không scan user documents
- ✅ Local processing (no cloud upload)

**Bias:**
- Avoid bias against:
  - Legitimate crackers/debuggers
  - Open-source tools
  - Security research tools

**Transparency:**
- Clear về false positive possibility
- Give users override option
- Explain detections

---

## SLIDE 32: REGULATORY COMPLIANCE

**Compliance Requirements:**

**GDPR (EU):**
- Data minimization
- User consent
- Right to explanation

**CCPA (California):**
- Privacy notice
- User rights

**Industry Standards:**
- AMTSO (Anti-Malware Testing Standards)
- Common Criteria certification

---

## SLIDE 33: COMPETITIVE LANDSCAPE

**Existing Solutions:**

| Product | Detection Rate | FP Rate | Method |
|---------|----------------|---------|--------|
| Vendor A | 95% | 0.5% | Signature + Cloud |
| Vendor B | 92% | 1.0% | Behavioral |
| Vendor C | 88% | 0.3% | Signature only |
| **Our Target** | **95%** | **1-2%** | **ML-based** |

**Differentiation: Balance accuracy với low FP**

---

## SLIDE 34: USER PERSONAS

**Who will use this?**

**Persona 1: Home User**
- Needs: Easy to use, no false alarms
- Priority: Don't block legitimate software
- Tech level: Low

**Persona 2: Enterprise IT Admin**
- Needs: Detailed reports, configurability
- Priority: Catch all threats
- Tech level: High

**Persona 3: Security Researcher**
- Needs: Explainability, analysis tools
- Priority: Understand detections
- Tech level: Expert

---

## SLIDE 35: CHECKLIST - PHASE 1 HOÀN THÀNH

**✅ Đã xác định:**

- [x] Problem type: Binary Classification
- [x] Classes: Benign (0) vs Malware (1)
- [x] Success metrics: Recall ≥95%, Precision ≥90%, F1 ≥0.92
- [x] Performance: <1s inference, <100MB model
- [x] Deployment: Desktop endpoint
- [x] Interpretability: High (need explanations)
- [x] Stakeholders: Users, Security, Product, Business
- [x] Constraints: Static analysis, no execution
- [x] Risks identified và mitigation plans
- [x] Timeline: 4-5 weeks / 2-3 lab sessions

---

## SLIDE 36: CÂNH BÁO THƯỜNG GẶP

**Common Mistakes trong Phase 1:**

❌ Chỉ nhìn Accuracy
→ ✅ Focus vào Recall cho security

❌ Ignore inference speed
→ ✅ Set clear performance targets

❌ Không xác định deployment environment
→ ✅ Biết model chạy ở đâu

❌ Vague success criteria
→ ✅ Số liệu cụ thể (≥95% recall)

❌ Không tính business cost
→ ✅ Hiểu FN cost >> FP cost

---

## SLIDE 37: BÀI TẬP TƯ DUY

**Câu hỏi 1:**
Nếu model có Recall=99% và Precision=50%, bạn có deploy không? Tại sao?

**Câu hỏi 2:**
Làm thế nào để giảm False Positive mà không làm giảm Recall?

**Câu hỏi 3:**
Nếu phát hiện malware mới mỗi ngày tăng 50%, strategy nào để model vẫn effective?

---

## SLIDE 38: ĐÁP ÁN BÀI TẬP

**Câu 1: Recall=99%, Precision=50%**
```
Phân tích:
- Bắt được 99% malware ✅
- Nhưng 50% detections là false alarms ❌
- 1000 detections → 500 là FP
- User sẽ rất phiền!

Decision: KHÔNG deploy production
→ Cần balance tốt hơn (min Precision 90%)
```

---

## SLIDE 39: ĐÁP ÁN BÀI TẬP (tt)

**Câu 2: Giảm FP mà giữ Recall**

**Strategies:**
- Adjust classification threshold
- Add whitelisting cho known-good software
- Combine multiple models (ensemble)
- Feature engineering tốt hơn
- More training data cho benign samples
- Post-processing rules

---

## SLIDE 40: ĐÁP ÁN BÀI TẬP (tt)

**Câu 3: Malware tăng 50%/ngày**

**Strategies:**
- Active learning: Prioritize labeling new samples
- Online learning: Update model incrementally
- Anomaly detection: Catch unknown patterns
- Regular retraining: Weekly → Daily
- Community threat intelligence feeds
- Automated labeling pipeline

---

## SLIDE 41: PHASE 1 → PHASE 2 TRANSITION

**Đã hoàn thành Phase 1:**
✅ Hiểu rõ bài toán
✅ Định nghĩa success metrics
✅ Xác định constraints

**Tiếp theo - Phase 2: Data Collection**
- Tìm nguồn malware samples
- Build dataset với labels
- Exploratory Data Analysis
- Feature extraction planning

**Preview: Sẽ cần ~10,000 samples!**

---

## SLIDE 42: TÀI LIỆU THAM KHẢO

**Papers:**
- "Deep Learning for Malware Detection" (IEEE 2019)
- "Static Malware Analysis Using Machine Learning Methods" (2020)

**Datasets:**
- VirusShare (millions of samples)
- MalwareBazaar
- EMBER dataset

**Tools:**
- PEiD - PE analysis
- radare2 - Reverse engineering
- YARA - Pattern matching

---

## SLIDE 43: INDUSTRY BENCHMARKS

**State-of-the-art (SOTA) Results:**

| Approach | Dataset | Accuracy | Recall | Precision |
|----------|---------|----------|--------|-----------|
| CNN | EMBER | 96.5% | 95.8% | 97.2% |
| Random Forest | Custom | 95.2% | 94.5% | 95.9% |
| XGBoost | VirusTotal | 97.1% | 96.5% | 97.7% |
| Ensemble | EMBER | 98.2% | 97.8% | 98.5% |

**Our Target: Competitive với Random Forest**

---

## SLIDE 44: LEARNING RESOURCES

**Để hiểu sâu hơn:**

**Courses:**
- Malware Analysis Course (Practical Malware Analysis book)
- Machine Learning for Security (Coursera)

**Blogs:**
- Malwarebytes Labs
- Kaspersky Threatpost
- FireEye Blog

**Communities:**
- r/malware (Reddit)
- MalwareTech forum
- VirusTotal community

---

## SLIDE 45: SUMMARY - PHASE 1 COMPLETED

**Đã học được gì:**
- ✅ Binary Classification problem
- ✅ Recall là metric quan trọng nhất
- ✅ Balance Precision và Recall
- ✅ Inference speed matters
- ✅ Interpretability valuable
- ✅ FN cost >> FP cost
- ✅ Deployment constraints matter

**Key Takeaway:**
> "Trong security, KHÔNG BỎ SÓT (Recall) quan trọng hơn KHÔNG BÁO ĐỘNG GIẢ (Precision), nhưng cần balance!"

---

## SLIDE 46: NEXT SESSION PREVIEW

**Session tiếp theo: Phase 2 - Data Collection & EDA**

**Nội dung:**
- Thu thập malware samples
- Labeling strategy
- Dataset quality checks
- Exploratory Data Analysis
- Feature extraction planning

**Chuẩn bị:**
- Đọc về PE file format
- Install analysis tools
- Review dataset sources

---

## SLIDE 47: BÀI TẬP VỀ NHÀ

**Bài 1: Research (Bắt buộc)**
Tìm hiểu 3 malware families gần đây:
- Tên malware
- Cách lây nhiễm
- Hành vi chính
- Làm sao detect

**Bài 2: Metrics Calculation (Bắt buộc)**
Cho confusion matrix, tính tất cả metrics và quyết định deploy hay không

**Bài 3: Tool Exploration (Optional)**
Cài đặt và thử PE analysis tools

---

## SLIDE 48: THANK YOU!

**Câu hỏi?**

**Next Session:**
- Date: [Ngày]
- Time: [Giờ]
- Topic: Data Collection & Feature Engineering

**Contact:**
- Email: [email]
- Slack: #malware-detection-lab

**Hẹn gặp lại!** 🛡️

---


---


# 📊 PHASE 1: HIỂU BÀI TOÁN - NETWORK ANOMALY DETECTION

## Slides Text cho Module 6

---

## SLIDE 1: PHASE 1 OVERVIEW

**HIỂU BÀI TOÁN - 5 BƯỚC QUAN TRỌNG**

```
Phase 1: Problem Understanding
├─ Bước 1.1: Xác định loại bài toán ML
├─ Bước 1.2: Xác định success metrics
├─ Bước 1.3: Thu thập yêu cầu kỹ thuật
├─ Bước 1.4: Phân tích business context
└─ Bước 1.5: Document toàn bộ requirements
```

**Thời gian:** 2-4 giờ (không bỏ qua!)

**Tại sao quan trọng:** 
- Hiểu sai bài toán → Làm sai hết
- Chọn sai metrics → Model "tốt" nhưng vô dụng
- Thiếu requirements → Deploy thất bại

---

## SLIDE 2: TÌNH HUỐNG THỰC TẾ

**Bạn là Security Engineer tại ngân hàng ABC**

**Email từ CTO:**
```
Subject: Urgent - Need AI for Network Security

Chúng ta đang có vấn đề với network security.
Mỗi ngày có hàng triệu network events, team SOC
không thể theo dõi hết. Cần AI giúp phát hiện
các anomalies tự động.

Deadline: 2 tháng
Budget: 50,000 USD

Có làm được không?
```

**Câu hỏi:** Bạn trả lời thế nào?

---

## SLIDE 3: BƯỚC 1.1 - XÁC ĐỊNH LOẠI BÀI TOÁN

**Câu hỏi phân tích:**

**Q1: Đây là bài toán gì?**
- Classification? (phân loại)
- Regression? (dự đoán số)
- Clustering? (phân nhóm)
- Anomaly Detection? (phát hiện bất thường)

**Q2: Có labels không?**
- Supervised learning (có labels)
- Unsupervised learning (không labels)
- Semi-supervised (một phần có labels)

---

## SLIDE 4: PHÂN TÍCH BÀI TOÁN - NETWORK ANOMALY

**Đặc điểm bài toán:**

✅ **Phát hiện bất thường** (Anomaly Detection)
- Mục tiêu: Tìm network events "lạ"
- Normal traffic: 99%
- Abnormal traffic: 1%

✅ **Binary Classification** (nếu có labels)
- Class 0: Normal traffic
- Class 1: Anomaly/Attack

✅ **Highly Imbalanced**
- Anomaly rất hiếm (1-5%)
- Không thể dùng accuracy đơn thuần

---

## SLIDE 5: QUYẾT ĐỊNH LOẠI BÀI TOÁN

**3 Approaches có thể dùng:**

**Approach 1: Supervised Classification**
- Cần: Labeled data (normal + attack)
- Pros: Accuracy cao, biết attack types
- Cons: Cần nhiều labeled attack samples
- Dùng khi: Có đủ labeled historical data

**Approach 2: Unsupervised Anomaly Detection**
- Cần: Chỉ cần normal traffic data
- Pros: Phát hiện được unknown attacks
- Cons: False positive cao hơn
- Dùng khi: Ít labeled data, nhiều zero-day

**Approach 3: Semi-supervised**
- Cần: Nhiều normal + ít attack samples
- Pros: Cân bằng accuracy và flexibility
- Cons: Phức tạp hơn
- Dùng khi: Dataset thực tế (typical case)

---

## SLIDE 6: LỰA CHỌN CHO BÀI TOÁN CỦA CHÚNG TA

**Quyết định: Supervised Binary Classification**

**Lý do:**
✅ Có historical attack logs (labeled)
✅ Biết rõ attack types cần detect
✅ Business cần giải thích được decisions
✅ Có thể train offline trước khi deploy

**Loại bài toán chính thức:**
```
Binary Classification Problem
- Input: Network traffic features
- Output: {0: Normal, 1: Anomaly/Attack}
- Type: Supervised learning
- Challenge: Highly imbalanced data (99:1)
```

---

## SLIDE 7: BƯỚC 1.2 - XÁC ĐỊNH SUCCESS METRICS

**Câu hỏi quan trọng:**
"Model tốt" được định nghĩa thế nào?

**Metrics có thể dùng:**
- Accuracy?
- Precision?
- Recall?
- F1-Score?
- AUC-ROC?

**Câu hỏi:** Metric nào quan trọng nhất?

---

## SLIDE 8: PHÂN TÍCH COST CỦA LỖI

**False Positive (FP): Model báo attack nhưng thực ra normal**

**Cost:**
- Block legitimate traffic
- Business disruption
- IT team phải investigate (waste time)
- User complaints

**Ước tính:** $500 per false alarm × 100 FP/day = $50,000/day ❌

---

## SLIDE 9: PHÂN TÍCH COST CỦA LỖI (tt)

**False Negative (FN): Model nói normal nhưng thực ra là attack**

**Cost:**
- Attack không được phát hiện
- Data breach
- Financial loss
- Reputation damage
- Regulatory fines

**Ước tính:** $1,000,000 per breach (average) 💥

**Kết luận:** FN nguy hiểm hơn FP (1000x)

---

## SLIDE 10: CHỌN PRIMARY METRIC

**Dựa trên cost analysis:**

**Primary Metric: RECALL (Sensitivity)**
```
Recall = TP / (TP + FN)
       = "Trong các attack thật, bắt được bao nhiêu?"
```

**Yêu cầu:** Recall ≥ 95%
- Bỏ sót tối đa 5% attacks
- Chấp nhận False Positive cao hơn

**Secondary Metrics:**
- Precision ≥ 70% (giảm FP)
- F1-Score (cân bằng)
- AUC-ROC ≥ 0.90

---

## SLIDE 11: ĐỊNH NGHĨA SUCCESS CRITERIA

**Model được coi là "thành công" khi:**

✅ **Performance:**
- Recall ≥ 95% (must-have)
- Precision ≥ 70% (nice-to-have)
- F1-Score ≥ 0.80
- AUC-ROC ≥ 0.90

✅ **Speed:**
- Inference time < 100ms per event
- Can process 10,000 events/second

✅ **Size:**
- Model size < 100MB
- Deployable on edge devices

---

## SLIDE 12: BƯỚC 1.3 - YÊU CẦU KỸ THUẬT

**Thu thập yêu cầu từ stakeholders:**

**From CTO:**
- Deploy trong 2 tháng
- Budget: $50K
- Must integrate với existing SIEM

**From SOC Team:**
- Real-time alerts
- Explain why it's anomaly
- Dashboard với visualizations
- False positive < 100/day

**From IT Ops:**
- High availability (99.9% uptime)
- Scalable (10K events/sec → 100K)
- Easy to update/retrain

---

## SLIDE 13: YÊU CẦU CHỨC NĂNG

**Functional Requirements:**

**FR1: Detection**
- [ ] Detect DDoS attacks
- [ ] Detect port scanning
- [ ] Detect botnet traffic
- [ ] Detect data exfiltration
- [ ] Detect insider threats

**FR2: Alert System**
- [ ] Real-time alerts (<1 second)
- [ ] Severity levels (Low/Medium/High/Critical)
- [ ] Integration với Slack/Email/SMS
- [ ] Incident ticket creation

**FR3: Dashboard**
- [ ] Traffic overview
- [ ] Attack statistics
- [ ] Model performance metrics
- [ ] Feature importance

---

## SLIDE 14: YÊU CẦU PHI CHỨC NĂNG

**Non-Functional Requirements:**

**NFR1: Performance**
```
Throughput:    ≥ 10,000 events/second
Latency:       < 100ms (p95)
Model size:    < 100MB
Memory usage:  < 4GB RAM
```

**NFR2: Reliability**
```
Uptime:        99.9% (8.76 hours downtime/year)
MTBF:          > 720 hours
MTTR:          < 1 hour
Backup:        Daily automated
```

**NFR3: Scalability**
```
Horizontal:    Support 10+ nodes
Vertical:      Up to 32 cores, 128GB RAM
Auto-scaling:  Yes, based on load
```

---

## SLIDE 15: YÊU CẦU PHI CHỨC NĂNG (tt)

**NFR4: Security**
```
Authentication:  RBAC with AD integration
Encryption:      TLS 1.3 in-transit, AES-256 at-rest
Audit logging:   All predictions logged
Compliance:      SOC 2, ISO 27001
```

**NFR5: Maintainability**
```
Monitoring:      Prometheus + Grafana
Logging:         ELK stack
CI/CD:           Jenkins pipeline
Documentation:   Comprehensive docs + runbooks
```

**NFR6: Usability**
```
Training time:   < 4 hours for SOC analysts
UI/UX:           Intuitive dashboard
Explainability:  LIME/SHAP for predictions
```

---

## SLIDE 16: BƯỚC 1.4 - BUSINESS CONTEXT

**Hiểu rõ business domain:**

**Industry:** Financial Services (Banking)
- Highly regulated (PCI-DSS, GDPR)
- 24/7 operations
- Zero-tolerance for breaches
- Customer trust critical

**Current State:**
- Manual SOC monitoring
- 3 analysts × 8-hour shifts
- React to alerts (not proactive)
- Miss ~30% of attacks

**Target State:**
- AI-assisted detection
- Proactive threat hunting
- Reduce analyst workload 80%
- Catch 95%+ of attacks

---

## SLIDE 17: STAKEHOLDER ANALYSIS

**Primary Stakeholders:**

**1. SOC Team (Users)**
- Need: Easy-to-use tools
- Pain: Alert fatigue (500+ alerts/day)
- Success: Reduce alerts to 50/day
- Involvement: Daily users, feedback

**2. CTO (Sponsor)**
- Need: ROI proof
- Pain: Recent breaches ($2M loss)
- Success: No breaches in 6 months
- Involvement: Budget approval, reviews

**3. Compliance Officer**
- Need: Audit trail
- Pain: Regulatory fines risk
- Success: Pass audits
- Involvement: Compliance checks

---

## SLIDE 18: STAKEHOLDER ANALYSIS (tt)

**4. IT Operations (Support)**
- Need: Reliable system
- Pain: Downtime impacts business
- Success: 99.9% uptime
- Involvement: Deployment, maintenance

**5. Network Engineers (Data Source)**
- Need: Non-intrusive monitoring
- Pain: Tools slow down network
- Success: <1% performance impact
- Involvement: Data access, integration

**6. CISO (Decision Maker)**
- Need: Risk reduction
- Pain: Board pressure
- Success: Measurable security improvement
- Involvement: Final approval

---

## SLIDE 19: CONSTRAINTS & ASSUMPTIONS

**Constraints (Limitations):**

**Technical:**
- Must use existing network infrastructure
- Cannot install agents on endpoints
- Data retention: 90 days only
- Processing: On-premise only (no cloud)

**Resource:**
- Budget: $50K (including licenses)
- Team: 1 ML engineer, 1 DevOps
- Timeline: 2 months to MVP
- Compute: 2 servers (32 cores, 128GB each)

**Regulatory:**
- PCI-DSS Level 1 compliance
- GDPR data protection
- No PII in logs
- Audit logs required

---

## SLIDE 20: CONSTRAINTS & ASSUMPTIONS (tt)

**Assumptions (Need validation):**

✓ Network logs are complete and accurate
✓ Attack labels in historical data are correct
✓ Network topology stable (no major changes)
✓ SOC team will provide feedback
✓ IT will support integration
✓ Data quality is sufficient

**Risk if assumptions wrong:**
- Incomplete logs → Poor model
- Wrong labels → Train on bad data
- Topology changes → Model outdated
- No feedback → Can't improve

---

## SLIDE 21: BƯỚC 1.5 - DOCUMENT REQUIREMENTS

**Tạo Requirements Document:**

**1. Problem Statement (1 page)**
```
Background:
- Current state
- Pain points
- Business impact

Proposed Solution:
- ML-based anomaly detection
- Real-time alerts
- Dashboard

Expected Outcomes:
- 95% detection rate
- 80% workload reduction
- ROI within 6 months
```

---

## SLIDE 22: DOCUMENT REQUIREMENTS (tt)

**2. Technical Specifications (2-3 pages)**
```
Input:
- Data source: Network flow logs (NetFlow, sFlow)
- Format: CSV/JSON
- Volume: 1M events/hour
- Features: 50+ fields

Output:
- Prediction: {0: Normal, 1: Anomaly}
- Confidence score: 0-100%
- Explanation: Top 3 contributing factors
- Alert: JSON to SIEM

Model:
- Type: Binary classifier
- Algorithms: Compare 5 (LR, RF, XGBoost, NN, Isolation Forest)
- Training: Weekly retrain
- Validation: 95% recall minimum
```

---

## SLIDE 23: DOCUMENT REQUIREMENTS (tt)

**3. Success Metrics (1 page)**
```
Primary (Must-Have):
✓ Recall ≥ 95%
✓ Inference < 100ms
✓ Uptime ≥ 99.9%

Secondary (Nice-to-Have):
✓ Precision ≥ 70%
✓ F1-Score ≥ 0.80
✓ False alerts < 100/day

Business Metrics:
✓ Breach reduction: 80%
✓ SOC efficiency: 80% improvement
✓ Cost savings: $500K/year
✓ ROI: 6 months payback
```

---

## SLIDE 24: DOCUMENT REQUIREMENTS (tt)

**4. Risks & Mitigation (1 page)**

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Insufficient labeled data | High | Medium | Use semi-supervised learning |
| High false positive rate | High | High | Tune threshold, ensemble methods |
| Concept drift | Medium | High | Weekly retraining pipeline |
| Integration issues | Medium | Low | POC with IT before full deploy |
| Performance degradation | High | Low | Load testing, auto-scaling |

---

## SLIDE 25: REVIEW CHECKLIST

**Phase 1 Complete khi:**

✅ **Problem Definition:**
- [ ] Loại bài toán xác định rõ ràng
- [ ] Input và output được mô tả cụ thể
- [ ] Supervised vs unsupervised đã quyết định

✅ **Success Metrics:**
- [ ] Primary metric đã chọn (Recall)
- [ ] Secondary metrics đã list
- [ ] Threshold requirements đã set
- [ ] Business metrics đã align

✅ **Requirements:**
- [ ] Functional requirements documented
- [ ] Non-functional requirements documented
- [ ] Constraints identified
- [ ] Assumptions listed

---

## SLIDE 26: REVIEW CHECKLIST (tt)

✅ **Stakeholders:**
- [ ] All stakeholders identified
- [ ] Needs and pains understood
- [ ] Success criteria agreed
- [ ] Sign-off obtained

✅ **Documentation:**
- [ ] Requirements doc created
- [ ] Reviewed by stakeholders
- [ ] Approved by sponsor (CTO)
- [ ] Shared with team

✅ **Next Steps:**
- [ ] Phase 2: Data collection plan ready
- [ ] Team briefed
- [ ] Timeline confirmed

---

## SLIDE 27: COMMON MISTAKES - TRÁNH SAI LẦM

**❌ Mistake 1: Bỏ qua Phase 1**
```
"Mình có data rồi, train model luôn đi!"
→ Làm sai bài toán, tốn thời gian

Đúng: Dành 10% thời gian hiểu bài toán
      Tiết kiệm 50% thời gian sau này
```

**❌ Mistake 2: Chỉ nhìn accuracy**
```
"Model đạt 99% accuracy rồi!"
→ Nhưng bỏ sót 50% attacks (vì imbalanced)

Đúng: Chọn metric phù hợp (Recall cho security)
```

---

## SLIDE 28: COMMON MISTAKES (tt)

**❌ Mistake 3: Không hỏi stakeholders**
```
ML engineer tự quyết định requirements
→ Deploy xong, users không dùng

Đúng: Interview users, hiểu pain points thật
```

**❌ Mistake 4: Unrealistic expectations**
```
"AI sẽ detect 100% attacks, 0% false positive"
→ Impossible, stakeholders thất vọng

Đúng: Set realistic goals (95% recall, 70% precision)
      Over-deliver thay vì under-deliver
```

---

## SLIDE 29: COMMON MISTAKES (tt)

**❌ Mistake 5: Thiếu documentation**
```
Nhớ trong đầu, không viết ra
→ 2 tháng sau quên, team mới không hiểu

Đúng: Document everything
      Future you sẽ cảm ơn present you
```

**❌ Mistake 6: Ignore constraints**
```
Train model cần 1TB RAM, 10 GPUs
→ Công ty không có, deploy thất bại

Đúng: Hiểu constraints từ đầu
      Design solution phù hợp
```

---

## SLIDE 30: OUTPUT CỦA PHASE 1

**Deliverables:**

📄 **1. Requirements Document (5-10 pages)**
- Problem statement
- Technical specifications
- Success metrics
- Risks & mitigation

📊 **2. Project Charter (1 page)**
- Objective
- Scope
- Timeline
- Team
- Budget

📋 **3. Stakeholder Sign-off**
- CTO approval
- SOC manager approval
- IT ops approval

---

## SLIDE 31: OUTPUT CỦA PHASE 1 (tt)

📈 **4. Success Metrics Dashboard (mockup)**
- Show how metrics will be tracked
- Set baseline (current state)
- Define targets

🗓️ **5. Project Plan**
```
Phase 1: Requirements     [DONE] ✅
Phase 2: Data Collection  [Week 1-2]
Phase 3: EDA              [Week 3]
Phase 4: Feature Eng      [Week 4]
Phase 5: Modeling         [Week 5-6]
Phase 6: Evaluation       [Week 7]
Phase 7: Deployment       [Week 8]
Phase 8: Monitoring       [Ongoing]
```

---

## SLIDE 32: TÓM TẮT PHASE 1

**5 Bước đã thực hiện:**

✅ **Bước 1.1:** Xác định loại bài toán
- Binary classification
- Supervised learning
- Highly imbalanced

✅ **Bước 1.2:** Xác định success metrics
- Primary: Recall ≥ 95%
- Secondary: Precision ≥ 70%
- Business: Cost savings $500K/year

✅ **Bước 1.3:** Thu thập requirements
- Functional: Detection types
- Non-functional: Performance, reliability

---

## SLIDE 33: TÓM TẮT PHASE 1 (tt)

✅ **Bước 1.4:** Phân tích business context
- Stakeholders identified
- Pain points understood
- Constraints documented

✅ **Bước 1.5:** Document requirements
- Requirements doc created
- Sign-off obtained
- Team aligned

**Thời gian:** 2-4 giờ well spent!

**Kết quả:** Clear direction, aligned expectations, reduced risks

---

## SLIDE 34: TEMPLATE - PROBLEM DEFINITION

**Use this template for any ML project:**

```
1. WHAT?
   - What is the problem?
   - What is the goal?
   - What is success?

2. WHY?
   - Why is this important?
   - Why now?
   - Why ML (not rule-based)?

3. WHO?
   - Who are the users?
   - Who are the stakeholders?
   - Who will maintain it?

4. WHEN?
   - When is the deadline?
   - When will it be deployed?
   - When to retrain?

5. WHERE?
   - Where will it run? (cloud/on-premise)
   - Where is the data?
   - Where are the constraints?

6. HOW?
   - How will success be measured?
   - How will it integrate?
   - How will it be monitored?
```

---

## SLIDE 35: REAL-WORLD EXAMPLE 1

**Case: E-commerce Fraud Detection**

**Problem:**
- Fraud transactions: 0.1%
- Loss: $10M/year
- Manual review: Too slow

**Analysis:**
- Type: Binary classification (fraud/legitimate)
- Primary metric: Recall (catch fraudsters)
- Secondary: Precision (reduce false declines)
- Constraint: Real-time (<200ms)
- Success: 90% fraud caught, <5% false declines

---

## SLIDE 36: REAL-WORLD EXAMPLE 2

**Case: Medical Diagnosis (Cancer Detection)**

**Problem:**
- Radiologist shortage
- Need faster screening
- High stakes (life/death)

**Analysis:**
- Type: Binary classification (cancer/no cancer)
- Primary metric: Recall 99%+ (cannot miss cancer)
- Secondary: Precision 80%+ (reduce unnecessary biopsies)
- Constraint: Explainable (doctors need trust)
- Success: FDA approval, hospital adoption

---

## SLIDE 37: REAL-WORLD EXAMPLE 3

**Case: Predictive Maintenance (Factory)**

**Problem:**
- Unexpected equipment failures
- Downtime: $100K/hour
- Reactive maintenance expensive

**Analysis:**
- Type: Binary classification (will fail/won't fail)
- OR: Regression (remaining useful life prediction)
- Primary metric: Recall 95% (catch failures early)
- Constraint: Edge deployment (no cloud access)
- Success: 50% downtime reduction

---

## SLIDE 38: EXERCISE 1 - PHÂN TÍCH BÀI TOÁN

**Scenario:** Spam Email Detection

**Yêu cầu:** Xác định các thông tin sau:
1. Loại bài toán?
2. Primary metric?
3. False Positive vs False Negative: Cái nào nguy hiểm hơn?
4. Requirements chính?

**Thời gian:** 10 phút thảo luận nhóm

---

## SLIDE 39: EXERCISE 2 - CHỌN METRICS

**Cho các bài toán sau, chọn primary metric:**

**1. Credit Card Approval**
- Approve good customers
- Reject risky customers
- Primary metric: ?

**2. Disease Outbreak Detection**
- Detect outbreak early
- Avoid panic (false alarms)
- Primary metric: ?

**3. Product Recommendation**
- User clicks on recommendations
- Maximize revenue
- Primary metric: ?

---

## SLIDE 40: ĐÁP ÁN EXERCISES

**Exercise 1: Spam Detection**
1. Binary classification (spam/not spam)
2. Primary: Precision (không xóa nhầm email quan trọng)
3. FP nguy hiểm hơn (mất email business critical)
4. Real-time, low FP, explainable

**Exercise 2: Metrics**
1. Credit Card: F1-Score (balance risk & opportunity)
2. Disease Outbreak: Recall (cannot miss outbreaks)
3. Product Recommendation: Precision@K, CTR

---

## SLIDE 41: BEST PRACTICES SUMMARY

**✅ DO:**
- Spend 10% thời gian ở Phase 1
- Interview real users
- Document everything
- Set realistic expectations
- Align with business goals
- Get stakeholder sign-off

**❌ DON'T:**
- Skip to coding immediately
- Assume you know the problem
- Choose metrics arbitrarily
- Ignore constraints
- Work in isolation
- Promise unrealistic results

---

## SLIDE 42: PHASE 1 CHECKLIST

**Print và check off:**

```
□ Loại bài toán xác định
□ Input/Output mô tả rõ
□ Primary metric chọn
□ Secondary metrics list
□ Threshold requirements set
□ Stakeholders interviewed
□ Requirements documented
□ Constraints identified
□ Assumptions listed
□ Risks assessed
□ Timeline agreed
□ Budget confirmed
□ Sign-off obtained
□ Team briefed
□ Ready for Phase 2
```

---

## SLIDE 43: CHUYỂN SANG PHASE 2

**Phase 1 hoàn thành → Phase 2: Data Collection**

**Có trong tay:**
- Requirements document
- Success metrics defined
- Stakeholder buy-in
- Clear direction

**Phase 2 sẽ làm gì:**
- Thu thập network logs
- Exploratory Data Analysis
- Data quality assessment
- Feature identification

**Chuẩn bị:**
- Access to network logs
- Analysis tools ready
- Team availability

---

## SLIDE 44: Q&A - COMMON QUESTIONS

**Q: Phase 1 có thể skip nếu bài toán rõ ràng?**
A: KHÔNG! Luôn làm Phase 1. "Rõ ràng" thường là착illusion.

**Q: Mất bao lâu cho Phase 1?**
A: 2-4 giờ cho small project, 1-2 ngày cho large project.

**Q: Nếu stakeholder không available?**
A: Document assumptions, flag risks, proceed với caution.

**Q: Metrics có thể thay đổi sau?**
A: Có, nhưng cần justify và get approval.

---

## SLIDE 45: TÀI LIỆU THAM KHẢO

**Books:**
- "Machine Learning Yearning" - Andrew Ng
- "Building Machine Learning Powered Applications" - Emmanuel Ameisen

**Templates:**
- ML Canvas: https://www.louisdorard.com/ml-canvas
- Project Charter template

**Tools:**
- JIRA/Trello: Project tracking
- Confluence: Documentation
- Google Docs: Collaborative editing

---

## SLIDE 46: HOMEWORK

**Bài tập về nhà:**

**1. Phân tích bài toán mới (Bắt buộc)**
- Chọn 1 bài toán ML bất kỳ
- Apply Phase 1 framework
- Viết requirements document (2-3 pages)
- Nộp tuần sau

**2. Critique existing project (Nâng cao)**
- Tìm 1 ML project thất bại (news, blog)
- Phân tích: Có thể họ bỏ qua Phase 1 không?
- Present findings (5 phút)

---

## SLIDE 47: KEY TAKEAWAYS

**3 điều quan trọng nhất:**

1. **Hiểu bài toán > Thuật toán fancy**
   - 10% thời gian Phase 1
   - 50% thời gian tiết kiệm sau

2. **Metrics phải align với business**
   - Accuracy không phải lúc nào cũng đúng
   - Chọn metrics theo cost analysis

3. **Documentation is your friend**
   - Requirements doc = roadmap
   - Prevent scope creep
   - Enable communication

---

## SLIDE 48: REMEMBER

> "Hours spent in reconnaissance are seldom wasted."
> - Military proverb

> "Give me six hours to chop down a tree,  
> I will spend the first four sharpening the axe."
> - Abraham Lincoln

**Applied to ML:**
> "Give me two months to build ML system,  
> I will spend first week understanding the problem."

**Phase 1 = Sharpening your axe! 🪓**

---

## SLIDE 49: NEXT CLASS PREVIEW

**Phase 2: Data Collection & EDA**

**Topics:**
- Network log formats (NetFlow, sFlow)
- Data collection strategies
- EDA techniques for network data
- Data quality assessment
- Feature identification

**Chuẩn bị:**
- Review network protocols
- Install Wireshark (optional)
- Read về NetFlow format

---

## SLIDE 50: THANK YOU!

**Phase 1 Complete! 🎉**

**Questions?**

**Contact:**
- Email: [your-email]
- Office hours: [schedule]
- Slack: #module6-questions

**Tài liệu:**
- Slides: [link]
- Requirements template: [link]
- Example projects: [link]

**See you in Phase 2! 🚀**

---





