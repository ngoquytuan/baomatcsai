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

