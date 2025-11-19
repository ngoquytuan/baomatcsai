# 🎯 CHECKLIST & RULES CHO MỌI DỰ ÁN MACHINE LEARNING

**BEST PRACTICES** chung cho hầu hết dự án ML, không riêng gì bài toán security này.

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

