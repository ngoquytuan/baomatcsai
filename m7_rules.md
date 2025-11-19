# 📊 PHASE 1: HIỂU BÀI TOÁN - MODULE 7 USER AUTHENTICATION SECURITY

## Áp dụng ML Checklist vào bài toán thực tế

---

## SLIDE 1: PHASE 1 OVERVIEW

**Phase 1: Problem Understanding**

**Mục tiêu:**
- Xác định chính xác bài toán cần giải quyết
- Chọn approach phù hợp
- Định nghĩa success metrics
- Thu thập requirements từ stakeholders

**Thời gian:** 1-2 ngày (20% tổng thời gian project)

**Output:** Problem Statement Document

---

## SLIDE 2: BÀI TOÁN THỰC TẾ

**Scenario:**
Bạn là Security Engineer tại VietBank - ngân hàng số với 5 triệu khách hàng

**Vấn đề hiện tại:**
- 10 triệu login attempts/ngày
- Hacker tấn công credential stuffing
- Rule-based system chặn 60% attacks
- 40% attacks bypass thành công
- 1000+ fraud cases/tháng = 5 tỷ VNĐ thiệt hại
- 500 legitimate users bị block nhầm/ngày (false positive)

**Yêu cầu từ CEO:**
"Giảm fraud 80% trong 3 tháng, không làm phiền khách hàng!"

---

## SLIDE 3: CHECKLIST 1.1 - XÁC ĐỊNH LOẠI BÀI TOÁN

**□ Classification (phân loại)** ✅
- **□ Binary (2 classes)** ✅ CHỌN
  - Class 0: Safe login (Hợp lệ)
  - Class 1: Risky login (Nguy hiểm)
- □ Multiclass (>2 classes) ❌
- □ Multilabel (nhiều labels) ❌

**□ Regression** ❌ Không phải
**□ Clustering** ❌ Không phải
**□ Anomaly Detection** ⚠️ Có thể dùng bổ sung
**□ Time Series** ⚠️ Có thể phân tích trends

---

## SLIDE 4: TẠI SAO CHỌN BINARY CLASSIFICATION?

**Phân tích:**

**Binary Classification phù hợp vì:**
- ✅ Có 2 outcomes rõ ràng: Safe hoặc Risky
- ✅ Có historical labeled data
- ✅ Cần decision nhanh (allow/block/MFA)
- ✅ Nhiều algorithms mature và tested

**Không phải Multiclass vì:**
- Không cần phân loại chi tiết (VD: bot, insider, stolen credentials)
- Chỉ cần biết: Nguy hiểm hay Không?

**Không phải Regression vì:**
- Không dự đoán số (VD: probability là số nhưng kết quả cuối là class)

---

## SLIDE 5: ALTERNATIVE APPROACHES

**Approach 1: Binary Classification** ✅ CHỌN
```
Login → Model → [Safe (0) | Risky (1)]
                     ↓           ↓
                  Allow      Block/MFA
```
**Pros:** Đơn giản, interpretable, fast
**Cons:** Mất thông tin chi tiết

---

**Approach 2: Risk Score (0-100)** ⚠️
```
Login → Model → Risk Score: 0-100
                     ↓
         0-30: Allow
        31-70: MFA
       71-100: Block
```
**Pros:** Flexible thresholds, gradual response
**Cons:** Phức tạp hơn, cần tune thresholds

---

**Approach 3: Anomaly Detection** ⚠️
```
Login → Model → [Normal | Anomaly]
```
**Pros:** Detect unknown attacks
**Cons:** Cần nhiều normal data, high false positive

---

## SLIDE 6: QUYẾT ĐỊNH FINAL APPROACH

**Chọn: Binary Classification với Risk Score**

**Lý do:**
1. Train binary classifier (simple baseline)
2. Use `predict_proba()` để lấy probability
3. Convert probability → risk score 0-100
4. Set thresholds linh hoạt

**Best of both worlds:**
```python
# Binary prediction
prediction = model.predict(X)  # 0 or 1

# Risk score
probability = model.predict_proba(X)[:, 1]  # 0.0-1.0
risk_score = probability * 100  # 0-100

# Flexible decision
if risk_score < 30:
    action = "ALLOW"
elif risk_score < 70:
    action = "MFA"
else:
    action = "BLOCK"
```

---

## SLIDE 7: CHECKLIST 1.2 - SUCCESS METRICS

**□ Xác định business metrics** ✅

**Primary Metrics (Quan trọng nhất):**
1. **Fraud Reduction Rate**
   - Hiện tại: 1000 cases/tháng
   - Mục tiêu: <200 cases/tháng (80% reduction)
   - Metric: `(Current - New) / Current × 100%`

2. **False Positive Rate**
   - Hiện tại: 500 users bị block nhầm/ngày
   - Mục tiêu: <50 users/ngày (90% reduction)
   - Metric: `FP / (FP + TN)`

---

## SLIDE 8: SUCCESS METRICS (tt)

**Secondary Metrics:**

3. **Detection Accuracy**
   - Mục tiêu: >95% accuracy
   - Metric: `(TP + TN) / Total`

4. **Recall (Catch Rate)**
   - Mục tiêu: >90% (bắt được 9/10 hackers)
   - Metric: `TP / (TP + FN)`
   - **Critical:** Không bỏ sót hacker!

5. **Precision (Accuracy of Alerts)**
   - Mục tiêu: >80% (8/10 alerts là thật)
   - Metric: `TP / (TP + FP)`
   - Quan trọng: Không làm phiền user

---

## SLIDE 9: BUSINESS METRICS vs ML METRICS

| Business Metric | ML Metric | Target | Priority |
|----------------|-----------|--------|----------|
| Fraud reduction | Recall | >90% | 🔴 Critical |
| Customer satisfaction | Precision, FPR | >80%, <0.5% | 🔴 Critical |
| Operational cost | False Positive count | <50/day | 🟡 High |
| Response time | Inference latency | <100ms | 🟡 High |
| System uptime | Availability | >99.9% | 🟢 Medium |

**Trade-off chính:**
```
High Recall ←→ Low False Positive
(Bắt nhiều hacker) (Ít làm phiền user)
```

---

## SLIDE 10: ĐỊNH NGHĨA CONFUSION MATRIX

**Trong context Authentication Security:**

```
                    Predicted by ML
                 Safe (0)    Risky (1)
Actual  Safe     TN          FP
        Risky    FN          TP
```

**Giải thích cụ thể:**

**True Negative (TN):** 
- User thật login bình thường
- ML dự đoán đúng: Safe
- → ✅ Allow login

**False Positive (FP):**
- User thật login bình thường
- ML dự đoán SAI: Risky
- → ❌ Block nhầm user thật (WORST UX!)

---

## SLIDE 11: CONFUSION MATRIX (tt)

**False Negative (FN):**
- Hacker đang tấn công
- ML dự đoán SAI: Safe
- → ❌ Để lọt hacker (WORST SECURITY!)

**True Positive (TP):**
- Hacker đang tấn công
- ML dự đoán đúng: Risky
- → ✅ Block thành công

**Business Impact:**
```
FP: Mất khách hàng, bad UX, support cost
FN: Mất tiền, bad reputation, legal issues
```

---

## SLIDE 12: COST ANALYSIS

**Chi phí của từng loại error:**

| Error | Business Cost | Ví dụ |
|-------|---------------|-------|
| **FP** | 50,000 VNĐ/case | User gọi hotline, mất 30 phút support |
| **FN** | 5,000,000 VNĐ/case | Hacker đánh cắp 5 triệu từ tài khoản |

**Total Cost Formula:**
```
Total Cost = (FP × 50K) + (FN × 5M)
```

**Ví dụ:**
```
Scenario 1: FP=100, FN=10
Cost = (100 × 50K) + (10 × 5M) = 55M VNĐ/ngày

Scenario 2: FP=20, FN=5
Cost = (20 × 50K) + (5 × 5M) = 26M VNĐ/ngày
→ Tiết kiệm 29M VNĐ/ngày!
```

---

## SLIDE 13: CHỌN OPTIMAL METRIC

**Dựa vào cost analysis:**

**Option 1: Optimize Accuracy** ❌
```
Accuracy = (TP + TN) / Total
→ Treat FP và FN như nhau
→ KHÔNG phù hợp (FN đắt hơn FP 100 lần!)
```

**Option 2: Optimize F1-Score** ⚠️
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
→ Cân bằng Precision và Recall
→ OK nhưng chưa tối ưu
```

**Option 3: Optimize Custom Cost Function** ✅
```
Cost = (FP × w_FP) + (FN × w_FN)
where w_FP = 50K, w_FN = 5M
→ Minimize total business cost
```

---

## SLIDE 14: FINAL SUCCESS CRITERIA

**Phase 1 Outcome: Định nghĩa Success**

```
PROJECT SUCCESS = 
    Recall ≥ 90% (bắt ít nhất 90% hackers)
    AND
    FP Rate ≤ 0.5% (block nhầm <0.5% users)
    AND
    Inference time ≤ 100ms
    AND
    Total cost reduction ≥ 50%
```

**Measurement:**
- Baseline: Current rule-based system
- Target: ML model sau 3 tháng
- Review: Weekly metrics tracking

---

## SLIDE 15: CHECKLIST 1.3 - YÊU CẦU KỸ THUẬT

**□ Độ chính xác cần thiết** ✅
- Accuracy: >95%
- Recall: >90% (Critical)
- Precision: >80%
- F1-Score: >0.85

**□ Tốc độ inference** ✅
- Requirement: <100ms per prediction
- Reason: Không làm chậm login flow
- Test condition: 95th percentile latency

---

## SLIDE 16: YÊU CẦU KỸ THUẬT (tt)

**□ Kích thước model tối đa** ✅
- Requirement: <50MB
- Reason: Deploy trên edge servers
- Constraint: Limited memory

**□ Khả năng giải thích** ✅
- Requirement: Medium interpretability
- Reason: 
  - Cần giải thích với compliance team
  - Cần debug false positives
  - Không cần explain từng prediction với user

**Acceptable models:**
- ✅ Logistic Regression (high interpretability)
- ✅ Random Forest (medium interpretability)
- ⚠️ XGBoost (medium-low interpretability)
- ❌ Deep Neural Networks (low interpretability)

---

## SLIDE 17: YÊU CẦU DEPLOY

**□ Điều kiện deploy** ✅

**Environment:**
- Platform: AWS EC2 + Lambda
- Traffic: 10M requests/day = 115 req/sec
- Availability: 99.9% uptime
- Scaling: Auto-scale based on traffic

**Constraints:**
- Memory: 2GB per instance
- CPU: 4 cores per instance
- Cold start: <500ms
- Cost: <$500/month

---

## SLIDE 18: STAKEHOLDER REQUIREMENTS

**Đã thu thập requirements từ:**

**1. Security Team (CISO)**
- ✅ Giảm fraud cases 80%
- ✅ Real-time blocking
- ✅ Audit trail đầy đủ
- ✅ Comply với PCI-DSS

**2. Product Team (CPO)**
- ✅ Không ảnh hưởng UX
- ✅ FP rate <0.5%
- ✅ Login latency <100ms
- ✅ A/B testing capability

---

## SLIDE 19: STAKEHOLDER REQUIREMENTS (tt)

**3. Engineering Team (CTO)**
- ✅ Easy to deploy & maintain
- ✅ Model size <50MB
- ✅ Monitoring & alerting
- ✅ Rollback capability

**4. Compliance Team (General Counsel)**
- ✅ Explainable decisions
- ✅ GDPR compliant
- ✅ No bias against demographics
- ✅ Audit logs

**5. Customer Support (Head of CS)**
- ✅ Clear rejection reasons
- ✅ Appeal process
- ✅ <50 FP cases/day

---

## SLIDE 20: CONSTRAINTS & ASSUMPTIONS

**Constraints:**
- ⏰ Timeline: 3 tháng (12 weeks)
- 💰 Budget: $20K (tools + cloud)
- 👥 Team: 2 ML engineers + 1 security analyst
- 📊 Data: 6 tháng historical logs
- 🖥️ Infrastructure: Existing AWS setup

**Assumptions:**
- ✅ Có quyền truy cập production logs
- ✅ Data quality tốt (>95% complete)
- ✅ Labels có sẵn (từ fraud team)
- ✅ Support team available for validation
- ⚠️ Attack patterns không thay đổi đột ngột

---

## SLIDE 21: RISK ANALYSIS

**Technical Risks:**

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Imbalanced data (<1% fraud) | High | High | SMOTE, class weights |
| Data drift sau deploy | High | Medium | Monitoring, auto-retrain |
| Model latency >100ms | Medium | Low | Model optimization |
| Adversarial attacks | High | Medium | Ensemble models |

**Business Risks:**
- High FP → Customer churn
- Low Recall → Fraud losses continue
- Project delay → Miss deadline

---

## SLIDE 22: OUT OF SCOPE

**Rõ ràng những gì KHÔNG làm:**

❌ **Không làm:**
- Phát hiện fraud SAU KHI login (transaction monitoring)
- Bot detection (CAPTCHA)
- Device fingerprinting (dùng sẵn có)
- Social engineering detection
- Mobile app security

✅ **Chỉ focus:**
- Login authentication risk scoring
- Real-time decision (allow/block/MFA)
- Based on behavioral patterns

---

## SLIDE 23: PHASE 1 DELIVERABLES

**Document cần hoàn thành:**

**1. Problem Statement (1 trang)**
```
Business Problem: 1000 fraud cases/month = 5B VNĐ loss
Technical Problem: Binary classification of login attempts
Success Criteria: 90% recall, <0.5% FPR, <100ms latency
```

**2. Requirements Document (2-3 trang)**
- Functional requirements
- Non-functional requirements
- Constraints
- Assumptions

---

## SLIDE 24: PHASE 1 DELIVERABLES (tt)

**3. Metrics Definition**
```python
# Primary metrics
recall = TP / (TP + FN)  # Target: >0.90
fpr = FP / (FP + TN)     # Target: <0.005
latency_p95 = ...        # Target: <100ms

# Secondary metrics
precision = TP / (TP + FP)  # Target: >0.80
f1_score = 2*P*R / (P+R)    # Target: >0.85
total_cost = FP*50K + FN*5M # Minimize
```

**4. Project Plan**
- Week 1-2: Data collection & EDA
- Week 3-4: Feature engineering
- Week 5-8: Model development
- Week 9-10: Testing & validation
- Week 11-12: Deployment & monitoring

---

## SLIDE 25: SIGN-OFF CHECKLIST

**Trước khi chuyển sang Phase 2:**

- [x] ✅ Problem type confirmed: Binary Classification
- [x] ✅ Success metrics defined và agreed
- [x] ✅ Requirements từ tất cả stakeholders
- [x] ✅ Constraints và assumptions documented
- [x] ✅ Risks identified với mitigation plans
- [x] ✅ Out of scope rõ ràng
- [x] ✅ Timeline và milestones agreed
- [x] ✅ Budget approved
- [x] ✅ Sign-off từ CISO, CPO, CTO

---

## SLIDE 26: BÀI TẬP THỰC HÀNH

**Exercise 1: Metric Selection**

Với các scenarios sau, chọn metric nào quan trọng nhất?

**Scenario A:** Banking - detect credit card fraud
- a) Accuracy
- b) Precision
- c) Recall ✅
- d) F1-Score

**Tại sao?** Bỏ sót fraud (FN) nguy hiểm hơn nhiều so với alert nhầm (FP)

---

## SLIDE 27: BÀI TẬP THỰC HÀNH (tt)

**Exercise 2: Cost Analysis**

Given:
- FP cost: 50K VNĐ
- FN cost: 5M VNĐ
- Model A: FP=50, FN=10
- Model B: FP=100, FN=5

Chọn model nào?

**Đáp án:**
```
Model A: (50×50K) + (10×5M) = 52.5M
Model B: (100×50K) + (5×5M) = 30M
→ Chọn Model B ✅
```

---

## SLIDE 28: BÀI TẬP THỰC HÀNH (tt)

**Exercise 3: Requirements Gathering**

Bạn đang họp với CEO. CEO nói:
"Tôi muốn hệ thống AI bảo mật tốt nhất!"

**Câu hỏi bạn cần hỏi?** (Chọn 3 quan trọng nhất)

a) "Tốt nhất" nghĩa là gì? (Accuracy? Cost reduction?)
b) Budget bao nhiêu?
c) Timeline khi nào?
d) Có chấp nhận block nhầm user không?
e) Algorithm nào muốn dùng?

**Đáp án:** a, c, d (e là technical detail, chưa cần hỏi CEO)

---

## SLIDE 29: COMMON MISTAKES - PHASE 1

**❌ Lỗi thường gặp:**

**1. Không định nghĩa rõ success**
```
❌ "Model phải tốt"
✅ "Recall ≥90%, FPR ≤0.5%, latency <100ms"
```

**2. Chỉ focus ML metrics, quên business**
```
❌ "Accuracy 95%"
✅ "Giảm fraud từ 1000 → 200 cases/tháng"
```

**3. Không thu thập requirements đầy đủ**
```
❌ Chỉ hỏi Security team
✅ Hỏi Security, Product, Engineering, Compliance, Support
```

---

## SLIDE 30: COMMON MISTAKES (tt)

**4. Không analyze trade-offs**
```
❌ "Muốn cả recall cao VÀ precision cao"
✅ "Ưu tiên recall (safety), chấp nhận precision thấp hơn"
```

**5. Bắt đầu code ngay**
```
❌ "Thử Logistic Regression xem sao"
✅ "Understand problem → Choose approach → Design solution"
```

**6. Quên constraints thực tế**
```
❌ Train model 10GB không care
✅ Model <50MB vì deploy constraint
```

---

## SLIDE 31: PHASE 1 CHECKLIST FINAL

```
✅ PHASE 1: PROBLEM UNDERSTANDING
├─ [x] Xác định loại bài toán: Binary Classification
├─ [x] Chọn approach: Classification + Risk Score
├─ [x] Định nghĩa success metrics:
│   ├─ Recall ≥90%
│   ├─ FPR ≤0.5%
│   └─ Latency <100ms
├─ [x] Thu thập requirements:
│   ├─ Security: Fraud reduction 80%
│   ├─ Product: UX not affected
│   ├─ Engineering: Easy to deploy
│   └─ Compliance: Explainable
├─ [x] Identify constraints:
│   ├─ Timeline: 3 months
│   ├─ Budget: $20K
│   ├─ Model size: <50MB
│   └─ Data: 6 months logs
├─ [x] Risk analysis completed
├─ [x] Out of scope defined
└─ [x] Stakeholder sign-off obtained
```

---

## SLIDE 32: NEXT STEPS

**Phase 1 hoàn thành! ✅**

**Chuyển sang Phase 2: Data Collection & EDA**

**Preview Phase 2:**
- Load và explore 6 tháng production logs
- Data quality assessment
- Missing value analysis
- Label distribution check
- Feature correlation analysis
- Outlier detection
- Initial insights

**Chuẩn bị:**
- Access to production logs
- Jupyter notebook setup
- EDA libraries ready

---

## SLIDE 33: TEMPLATE - PROBLEM STATEMENT

**Problem Statement Template:**

```
PROBLEM STATEMENT: User Authentication Security

1. BUSINESS PROBLEM
   Current situation: 1000 fraud cases/month
   Impact: 5B VNĐ loss, reputation damage
   Root cause: Rule-based system inadequate

2. TECHNICAL PROBLEM
   Task: Binary classification of login attempts
   Input: User behavior features (8 features)
   Output: Safe (0) or Risky (1)

3. SUCCESS CRITERIA
   - Recall ≥90% (catch 9/10 hackers)
   - FPR ≤0.5% (block <0.5% legit users)
   - Latency <100ms (no UX impact)
   - Cost reduction ≥50%

4. CONSTRAINTS
   - Timeline: 12 weeks
   - Team: 2 ML engineers
   - Budget: $20K
   - Model size: <50MB
```

---

## SLIDE 34: TEMPLATE - REQUIREMENTS DOC

**Requirements Document Template:**

```
FUNCTIONAL REQUIREMENTS
FR1: System shall classify login as Safe/Risky in <100ms
FR2: System shall provide risk score 0-100
FR3: System shall provide explanation for risky logins
FR4: System shall log all predictions for audit

NON-FUNCTIONAL REQUIREMENTS
NFR1: 99.9% availability
NFR2: Handle 115 req/sec
NFR3: Auto-scale based on load
NFR4: GDPR compliant

CONSTRAINTS
- Deploy on AWS
- Model <50MB
- Python 3.8+
- Scikit-learn preferred

ASSUMPTIONS
- Historical data available
- Labels accurate
- Attack patterns stable
```

---

## SLIDE 35: KẾT LUẬN PHASE 1

**Những gì đã hoàn thành:**
✅ Hiểu rõ business problem
✅ Chọn technical approach đúng
✅ Định nghĩa success metrics rõ ràng
✅ Thu thập requirements đầy đủ
✅ Identify constraints & risks
✅ Stakeholder alignment

**Tại sao Phase 1 quan trọng:**
- 20% effort, 80% impact
- Sai ở Phase 1 → Fail toàn bộ project
- Rõ ràng từ đầu → Ít rework sau này
- Stakeholder buy-in → Support tốt hơn

**Time well spent!** 🎯

---

