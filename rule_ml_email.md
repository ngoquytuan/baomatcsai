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

