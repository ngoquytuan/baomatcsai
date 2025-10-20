# Module 7: User Authentication Security With Artificial Intelligence

## 50 Slides with Image Suggestions




---

# Mermaid Diagrams cho Module 7: User Authentication Security With AI

## 1. Risk-Based Authentication Flow (Quy trình xác thực dựa trên rủi ro)

```mermaid
flowchart TD
    Start([👤 User Login Attempt]) --> Collect[📊 Collect Data<br/>- Credentials<br/>- Device info<br/>- Location<br/>- Time]
    
    Collect --> Analyze[🤖 AI Analysis<br/>Behavioral Biometrics]
    
    Analyze --> Behavioral{Keystroke &<br/>Mouse Patterns}
    Analyze --> Context{Location &<br/>Device Check}
    Analyze --> History{Historical<br/>Behavior}
    
    Behavioral --> Score[📈 Calculate Risk Score<br/>0-100]
    Context --> Score
    History --> Score
    
    Score --> Decision{Risk Level?}
    
    Decision -->|0-49<br/>Low Risk| Allow[✅ Allow Access<br/>Minimal friction]
    Decision -->|50-79<br/>Medium Risk| MFA[🔐 Require MFA<br/>Additional verification]
    Decision -->|80-100<br/>High Risk| Block[🚫 Block & Alert<br/>Security team notified]
    
    Allow --> Monitor[👁️ Continuous Monitoring<br/>During session]
    MFA --> CheckMFA{MFA Success?}
    CheckMFA -->|Yes| Allow
    CheckMFA -->|No| Block
    
    Block --> Alert[📢 Send Alert<br/>to Slack/Teams]
    Alert --> Human[👮 Security Team<br/>Investigation]
    
    Monitor --> Anomaly{Anomaly<br/>Detected?}
    Anomaly -->|Yes| Escalate[⚠️ Escalate Risk]
    Anomaly -->|No| Continue[Continue Session]
    
    Escalate --> Alert
    
    style Start fill:#e3f2fd,stroke:#1565c0,stroke-width:3px
    style Allow fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Block fill:#ffebee,stroke:#c62828,stroke-width:2px
    style Score fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style Alert fill:#fce4ec,stroke:#c2185b,stroke-width:2px
```

---

## 2. Account Reputation Scoring System

```mermaid
flowchart LR
    subgraph Input["📥 Input Factors"]
        H[🕰️ Historical Behavior<br/>40%<br/>- Login consistency<br/>- Transaction patterns<br/>- Account age<br/>- Past incidents]
        C[🌍 Current Context<br/>35%<br/>- Location/Time<br/>- Device consistency<br/>- Network reputation]
        S[🔒 Security Posture<br/>25%<br/>- Password strength<br/>- 2FA enabled<br/>- Security settings]
    end
    
    H --> Calculate[🧮 Reputation Score<br/>Calculation Engine]
    C --> Calculate
    S --> Calculate
    
    Calculate --> Score{📊 Final Score<br/>0-100}
    
    Score -->|80-100| High[⭐ High Reputation<br/>✅ Seamless login<br/>✅ Minimal friction<br/>✅ Express checkout]
    Score -->|50-79| Medium[🔔 Medium Reputation<br/>⚠️ Standard verification<br/>⚠️ Periodic challenges<br/>⚠️ Transaction limits]
    Score -->|0-49| Low[❌ Low Reputation<br/>🚫 Enhanced verification<br/>🚫 Account restrictions<br/>🚫 Manual review required]
    
    subgraph Dynamic["🔄 Dynamic Adjustments"]
        P1[✅ Successful login → +2]
        P2[❌ Failed login → -1]
        P3[🔑 Password change → +3]
        P4[🚨 Security incident → -10]
        P5[🔐 2FA activation → +5]
    end
    
    Score -.-> Dynamic
    Dynamic -.-> Score
    
    style Calculate fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style High fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Medium fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style Low fill:#ffebee,stroke:#c62828,stroke-width:2px
    style Score fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px
```

---

## 3. Authentication Abuse Types và AI Detection

```mermaid
mindmap
  root((🛡️ Authentication<br/>Attacks & Defense))
    🔓 Credential Stuffing
      📊 AI Detection
        Velocity analysis
        Behavioral inconsistency
        Geographic anomalies
        Device fingerprinting
      💥 Attack Method
        Leaked credentials
        Automated bots
        High volume, low success
    
    🔨 Brute Force
      📊 AI Detection
        Attempt velocity
        Pattern analysis
        Source reputation
        Composite risk score
      💥 Attack Method
        Trial and error
        Dictionary attacks
        Account lockout bypass
    
    👤 Account Takeover
      📊 AI Detection
        Behavior change detection
        Device/location anomalies
        Transaction patterns
        Usage timing analysis
      💥 Attack Method
        Phishing credentials
        Session hijacking
        Social engineering
    
    🔐 Session Hijacking
      📊 AI Detection
        Continuous validation
        Network pattern analysis
        Session consistency check
        Real-time risk scoring
      💥 Attack Method
        Token theft
        Man-in-the-middle
        XSS attacks
        Session fixation
    
    🌧️ Password Spraying
      📊 AI Detection
        Cross-account correlation
        Temporal pattern analysis
        IP reputation
        Common password detection
      💥 Attack Method
        Common passwords
        Multiple accounts
        Slow, distributed
```

---

## 4. Slack Integration Architecture

```mermaid
graph TB
    subgraph User["👤 User Layer"]
        U1[User Login Attempt]
    end
    
    subgraph Auth["🔐 Authentication System"]
        A1[Credential Verification]
        A2[Behavioral Analysis]
        A3[Risk Scoring Engine]
    end
    
    subgraph AI["🤖 AI Risk Engine"]
        ML1[Machine Learning Models]
        ML2[Anomaly Detection]
        ML3[Pattern Recognition]
    end
    
    subgraph Alert["📢 Alert System"]
        S1[Alert Manager]
        S2[Rule Engine]
        S3[Event Formatter]
    end
    
    subgraph Slack["💬 Slack Integration"]
        SL1[Slack Bot Service]
        SL2[Event Subscriptions]
        SL3[Interactive Messages]
        SL4[Action Handlers]
    end
    
    subgraph Security["👮 Security Team"]
        ST1[Security Analysts]
        ST2[Incident Response]
        ST3[Manual Review]
    end
    
    subgraph Storage["💾 Data Layer"]
        DB1[(Authentication DB)]
        DB2[(Audit Logs)]
        DB3[(User Profiles)]
    end
    
    U1 --> A1
    A1 --> A2
    A2 --> A3
    A3 --> ML1
    
    ML1 --> ML2
    ML2 --> ML3
    ML3 --> S1
    
    S1 --> S2
    S2 --> S3
    S3 --> SL1
    
    SL1 --> SL2
    SL2 --> SL3
    SL3 --> SL4
    
    SL4 --> ST1
    ST1 --> ST2
    ST2 --> ST3
    ST3 -.->|Feedback| A3
    
    A3 --> DB1
    S1 --> DB2
    ML1 --> DB3
    
    style Auth fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style AI fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Alert fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style Slack fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style Security fill:#fce4ec,stroke:#c2185b,stroke-width:2px
```

---

## 5. Behavioral Biometrics Analysis

```mermaid
flowchart TD
    Start[🖥️ User Interaction] --> Collect{📊 Data Collection}
    
    Collect --> Keystroke[⌨️ Keystroke Dynamics<br/>- Dwell time<br/>- Flight time<br/>- Pressure patterns<br/>- Typing rhythm]
    
    Collect --> Mouse[🖱️ Mouse Movement<br/>- Trajectory patterns<br/>- Click accuracy<br/>- Scroll behavior<br/>- Hesitation points]
    
    Collect --> Touch[📱 Touch Patterns<br/>- Swipe speed<br/>- Pressure<br/>- Multi-touch gestures<br/>- Screen contact area]
    
    Collect --> Navigation[🧭 Navigation Behavior<br/>- Page visit sequence<br/>- Time spent per page<br/>- Click patterns<br/>- Form filling speed]
    
    Keystroke --> Extract[🔬 Feature Extraction<br/>ML Preprocessing]
    Mouse --> Extract
    Touch --> Extract
    Navigation --> Extract
    
    Extract --> Profile[👤 User Profile Creation<br/>Unique behavioral signature]
    
    Profile --> Compare{🔍 Real-time Comparison}
    
    Compare -->|Match| Normal[✅ Normal Behavior<br/>Score: +5]
    Compare -->|Deviation| Anomaly[⚠️ Behavioral Anomaly<br/>Score: -10]
    Compare -->|Significant<br/>Difference| Imposter[🚨 Potential Imposter<br/>Score: -50]
    
    Normal --> Update[🔄 Update Profile<br/>Continuous learning]
    Anomaly --> Alert[📢 Generate Alert<br/>Risk score increase]
    Imposter --> Block[🚫 Block Session<br/>Immediate action]
    
    Alert --> Review[👁️ Security Review]
    Block --> Investigate[🔎 Deep Investigation]
    
    style Start fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style Normal fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Anomaly fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style Imposter fill:#ffebee,stroke:#c62828,stroke-width:2px
    style Profile fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
```

---

## 6. Escalation Procedures

```mermaid
flowchart TD
    Detect[🔍 Threat Detected] --> Score{📊 Risk Score?}
    
    Score -->|40-59<br/>Level 1| L1[📝 Level 1: Low Priority<br/>✅ Log event<br/>✅ Increase monitoring<br/>✅ No immediate action]
    
    Score -->|60-79<br/>Level 2| L2[⚠️ Level 2: Medium Priority<br/>🔔 Additional verification required<br/>🔔 Notify security team<br/>🔔 Email alert]
    
    Score -->|80-89<br/>Level 3| L3[🚨 Level 3: High Priority<br/>📢 Immediate Slack alert<br/>📢 Account restriction<br/>📢 Human review required<br/>⏱️ Response time: <15 min]
    
    Score -->|90-100<br/>Level 4| L4[🔴 Level 4: Critical<br/>🚫 Emergency response<br/>🚫 Automatic account lock<br/>🚫 Executive notification<br/>⏱️ Response time: <5 min]
    
    L1 --> Monitor1[👁️ Continuous Monitoring]
    L2 --> Review2[👮 Security Analyst Review]
    L3 --> Action3[⚡ Immediate Action Required]
    L4 --> Emergency4[🆘 Emergency Protocol]
    
    Monitor1 --> Check{Score<br/>Increased?}
    Check -->|Yes| Score
    Check -->|No| Continue1[Continue Monitoring]
    
    Review2 --> Decision2{Legitimate?}
    Decision2 -->|Yes| Allow2[✅ Allow with conditions]
    Decision2 -->|No| Escalate2[⬆️ Escalate to Level 3]
    
    Action3 --> Investigate3[🔎 Deep Investigation]
    Investigate3 --> Remediate3[🛠️ Remediation Actions]
    
    Emergency4 --> Lockdown4[🔒 System Lockdown]
    Lockdown4 --> Forensics4[🕵️ Digital Forensics]
    Forensics4 --> Report4[📋 Executive Report]
    
    style L1 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style L2 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style L3 fill:#ffccbc,stroke:#d84315,stroke-width:2px
    style L4 fill:#ffebee,stroke:#c62828,stroke-width:3px
    style Score fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
```

---

## 7. ML Model Selection for Authentication

```mermaid
graph TD
    Problem[🎯 Authentication Security Problem] --> Type{Problem Type?}
    
    Type -->|Known Attack<br/>Patterns| Supervised[📚 Supervised Learning]
    Type -->|Unknown<br/>Anomalies| Unsupervised[🔍 Unsupervised Learning]
    Type -->|Sequential<br/>Behavior| Sequential[⏰ Time-Series Models]
    
    Supervised --> SVM[🎯 Support Vector Machine<br/>✅ High accuracy<br/>✅ Works with small data<br/>❌ Slow training]
    Supervised --> RF[🌲 Random Forest<br/>✅ Feature importance<br/>✅ Handles missing data<br/>❌ Can overfit]
    Supervised --> NN[🧠 Neural Networks<br/>✅ Complex patterns<br/>✅ Automatic features<br/>❌ Needs lots of data]
    
    Unsupervised --> ISO[🌳 Isolation Forest<br/>✅ Fast anomaly detection<br/>✅ No training labels<br/>❌ Parameter tuning needed]
    Unsupervised --> OCSVM[⭕ One-Class SVM<br/>✅ Novelty detection<br/>✅ Robust outliers<br/>❌ Computational cost]
    Unsupervised --> AE[🔄 Autoencoders<br/>✅ Learns normal patterns<br/>✅ Dimensionality reduction<br/>❌ Complex architecture]
    
    Sequential --> RNN[🔁 RNN/LSTM<br/>✅ Sequence memory<br/>✅ Temporal patterns<br/>❌ Slow training]
    Sequential --> Markov[⛓️ Markov Chains<br/>✅ State transitions<br/>✅ Probabilistic<br/>❌ Simple assumptions]
    
    SVM --> Ensemble[🎼 Ensemble Methods]
    RF --> Ensemble
    ISO --> Ensemble
    
    Ensemble --> Final[🏆 Final Authentication System<br/>Multiple models voting<br/>Better accuracy & robustness]
    
    style Supervised fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style Unsupervised fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Sequential fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style Ensemble fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style Final fill:#ffccbc,stroke:#d84315,stroke-width:3px
```

---

## 8. Complete System Architecture (End-to-End)

```mermaid
graph TB
    subgraph Client["💻 Client Side"]
        U1[👤 User Device]
        U2[🌐 Browser/App]
        U3[📊 Client-side Telemetry]
    end
    
    subgraph Gateway["🚪 API Gateway"]
        G1[🔐 Authentication Endpoint]
        G2[⚡ Rate Limiting]
        G3[🛡️ WAF/Firewall]
    end
    
    subgraph AuthService["🔑 Authentication Service"]
        A1[📝 Credential Validation]
        A2[🎫 Session Management]
        A3[🔄 Token Generation]
    end
    
    subgraph AIEngine["🤖 AI Risk Engine"]
        AI1[🧠 ML Models]
        AI2[📈 Feature Engineering]
        AI3[🎯 Risk Scorer]
        AI4[🔍 Anomaly Detector]
    end
    
    subgraph Biometrics["👆 Behavioral Biometrics"]
        B1[⌨️ Keystroke Analysis]
        B2[🖱️ Mouse Tracking]
        B3[📱 Device Fingerprinting]
        B4[🌍 Geolocation]
    end
    
    subgraph Reputation["⭐ Reputation System"]
        R1[📊 Score Calculator]
        R2[🕰️ Historical Analysis]
        R3[🔄 Dynamic Updates]
    end
    
    subgraph Alerting["📢 Alert & Response"]
        AL1[🚨 Alert Manager]
        AL2[💬 Slack Integration]
        AL3[📧 Email Notifications]
        AL4[📞 SMS/Phone]
    end
    
    subgraph Response["👮 Security Operations"]
        SO1[👤 Security Analysts]
        SO2[🔎 Investigation Tools]
        SO3[⚡ Incident Response]
        SO4[📋 Reporting Dashboard]
    end
    
    subgraph Data["💾 Data & Storage"]
        DB1[(🗄️ User Database)]
        DB2[(📝 Audit Logs)]
        DB3[(📊 Analytics DB)]
        DB4[(🎯 ML Training Data)]
    end
    
    subgraph Monitoring["📊 Monitoring & Metrics"]
        M1[📈 Performance Metrics]
        M2[🎯 Detection Rate]
        M3[⚠️ False Positives]
        M4[⏱️ Response Time]
    end
    
    %% Client to Gateway
    U1 --> U2
    U2 --> U3
    U3 --> G1
    
    %% Gateway to Auth Service
    G1 --> G2
    G2 --> G3
    G3 --> A1
    
    %% Auth Service flows
    A1 --> A2
    A2 --> A3
    A1 --> AI1
    
    %% AI Engine processing
    AI1 --> AI2
    AI2 --> AI3
    AI3 --> AI4
    
    %% Biometrics to AI
    U3 --> B1
    U3 --> B2
    U3 --> B3
    U3 --> B4
    B1 --> AI2
    B2 --> AI2
    B3 --> AI2
    B4 --> AI2
    
    %% Reputation System
    AI3 --> R1
    R1 --> R2
    R2 --> R3
    R3 -.-> AI3
    
    %% Alerting flow
    AI4 --> AL1
    AL1 --> AL2
    AL1 --> AL3
    AL1 --> AL4
    
    %% Security Operations
    AL2 --> SO1
    AL3 --> SO1
    SO1 --> SO2
    SO2 --> SO3
    SO3 --> SO4
    
    %% Data connections
    A2 --> DB1
    AI4 --> DB2
    R1 --> DB3
    AI1 --> DB4
    
    %% Monitoring
    A2 --> M1
    AI4 --> M2
    AL1 --> M3
    SO3 --> M4
    
    %% Feedback loops
    SO4 -.->|Feedback| AI1
    M2 -.->|Tuning| AI3
    DB4 -.->|Retraining| AI1
    
    style AIEngine fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style Biometrics fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Reputation fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style Alerting fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style Response fill:#ffccbc,stroke:#d84315,stroke-width:2px
```

---

## 9. Geographic Anomaly Detection (Impossible Travel)

```mermaid
flowchart TD
    Start[🌍 Login Event Received] --> GetLoc[📍 Get Current Location<br/>IP: 203.0.113.45<br/>Location: Tokyo, Japan<br/>Time: 2:00 PM JST]
    
    GetLoc --> CheckHist{Check<br/>Login History}
    
    CheckHist --> LastLogin[⏰ Last Login<br/>IP: 198.51.100.23<br/>Location: New York, USA<br/>Time: 9:00 AM EST<br/>30 minutes ago]
    
    LastLogin --> Calculate[🧮 Calculate Distance & Time]
    
    Calculate --> Distance[📏 Distance: 10,850 km<br/>6,740 miles]
    
    Distance --> Required[✈️ Required Travel Time<br/>Minimum: 13-14 hours<br/>by fastest commercial flight]
    
    Required --> Compare{Actual Time<br/>vs Required Time}
    
    Compare -->|30 min << 13 hrs| Impossible[🚨 IMPOSSIBLE TRAVEL<br/>Physical impossibility detected]
    
    Impossible --> RiskHigh[📈 Risk Score: +50<br/>Confidence: 99%]
    
    RiskHigh --> Actions{Automated Actions}
    
    Actions --> Block[🚫 Block Current Session<br/>Require additional verification]
    Actions --> Alert[📢 Send Alert to Security<br/>High-priority Slack notification]
    Actions --> Log[📝 Log Suspicious Activity<br/>Forensics data collected]
    
    Block --> MFA[🔐 Require MFA<br/>+ Security Questions<br/>+ Device Verification]
    
    Alert --> Human[👮 Security Team Review<br/>Investigation initiated]
    
    Compare -->|Time >= Required| PossibleTravel{Plausible<br/>Travel?}
    
    PossibleTravel -->|Yes, but unusual| Monitor[👁️ Elevated Monitoring<br/>Risk Score: +10<br/>Continue with caution]
    PossibleTravel -->|Yes, normal pattern| Allow[✅ Allow Access<br/>Normal risk score]
    
    Monitor --> SessionWatch[🔍 Watch Session Activity<br/>Enhanced logging]
    
    style Impossible fill:#ffebee,stroke:#c62828,stroke-width:3px
    style RiskHigh fill:#ffccbc,stroke:#d84315,stroke-width:2px
    style Block fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    style Allow fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Calculate fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
```

---

## 10. Feature Engineering Pipeline

```mermaid
flowchart LR
    subgraph Raw["📥 Raw Data Collection"]
        R1[⌨️ Keystroke Events]
        R2[🖱️ Mouse Events]
        R3[🌐 Network Logs]
        R4[📱 Device Info]
        R5[⏰ Timestamp Data]
    end
    
    subgraph Extract["🔬 Feature Extraction"]
        E1[⏱️ Temporal Features<br/>- Hour of day<br/>- Day of week<br/>- Time since last login<br/>- Session duration]
        
        E2[👆 Behavioral Features<br/>- Typing speed avg<br/>- Typing variance<br/>- Mouse velocity<br/>- Click patterns]
        
        E3[🌍 Contextual Features<br/>- IP geolocation<br/>- Device type<br/>- Browser/OS<br/>- Network type]
        
        E4[📊 Statistical Features<br/>- Mean, median, std<br/>- Percentiles<br/>- Frequency counts<br/>- Anomaly scores]
    end
    
    subgraph Transform["⚙️ Transformation"]
        T1[📏 Normalization<br/>StandardScaler<br/>Min-Max Scaling]
        
        T2[🔢 Encoding<br/>One-Hot Encoding<br/>Label Encoding<br/>Binary Encoding]
        
        T3[🎯 Feature Selection<br/>Correlation analysis<br/>Feature importance<br/>PCA reduction]
    end
    
    subgraph Output["📤 ML-Ready Features"]
        O1[🧮 Numerical Vector<br/>50-100 dimensions]
        O2[🏷️ Feature Names<br/>Interpretable labels]
        O3[📊 Feature Metadata<br/>Types, ranges, stats]
    end
    
    R1 --> E1
    R1 --> E2
    R2 --> E2
    R3 --> E3
    R4 --> E3
    R5 --> E1
    
    R1 --> E4
    R2 --> E4
    R3 --> E4
    
    E1 --> T1
    E2 --> T1
    E3 --> T2
    E4 --> T1
    
    T1 --> T3
    T2 --> T3
    
    T3 --> O1
    T3 --> O2
    T3 --> O3
    
    O1 --> ML[🤖 ML Models]
    O2 --> ML
    O3 --> ML
    
    style Extract fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style Transform fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Output fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style ML fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
```

---

## Cách Sử Dụng Các Diagrams

### 📚 **Gợi ý áp dụng vào slides:**

1. **Diagram 1 (Risk-Based Auth Flow)** → Slide 10
2. **Diagram 2 (Reputation Scoring)** → Slide 20-21
3. **Diagram 3 (Attack Types)** → Slide 11-15
4. **Diagram 4 (Slack Integration)** → Slide 24-34
5. **Diagram 5 (Behavioral Biometrics)** → Slide 6-8
6. **Diagram 6 (Escalation)** → Slide 33
7. **Diagram 7 (ML Models)** → **New slides** về ML (theo đề xuất review)
8. **Diagram 8 (Full Architecture)** → Slide 34
9. **Diagram 9 (Impossible Travel)** → Slide 17
10. **Diagram 10 (Feature Engineering)** → **New slide** về feature engineering

### 💡 **Tips khi dùng trong giảng dạy:**

- **In slides:** Copy code Mermaid vào Markdown slides (reveal.js, Marp, hoặc convert sang PNG)
- **Interactive:** Dùng live Mermaid editor để demo cho students
- **Handouts:** Export các diagrams thành PDF để students tham khảo

Bạn có muốn tôi:
1. Tạo thêm diagrams cho các concepts khác?
2. Simplify một số diagrams quá phức tạp?
3. Thêm annotations/explanations cho từng diagram?

---


## Slide 1: Module 7 Overview

**Title:** User Authentication Security With Artificial Intelligence

**Content:**

- What is Authentication Detection
- Identification and Prevention of Authentication Abuse
- Account Reputation Scoring
- Subscribe to Slack Events
- Subscribe to Bot Events
- Post Deployment Verification: Slack Bot

**Suggested Image:** Digital fingerprint with AI neural network overlay, cybersecurity shield with binary code

---

## Slide 2: Learning Objectives

**By the end of this module, you will be able to:**

- Understand AI-enhanced authentication mechanisms
- Implement behavioral biometric analysis
- Design account reputation scoring systems
- Integrate authentication systems with Slack
- Deploy and monitor AI authentication bots
- Evaluate authentication system performance

**Suggested Image:** Target/bullseye icon with AI brain, checklist with cybersecurity icons

---

## Slide 3: Traditional vs AI Authentication

**Traditional Authentication:**

- Static credentials (username/password)
- Binary decision (allow/deny)
- No behavioral analysis
- High false positive rates

**AI-Enhanced Authentication:**

- Dynamic behavioral analysis
- Risk-based scoring
- Continuous monitoring
- Adaptive responses

**Suggested Image:** Split screen showing old lock vs modern biometric scanner, traditional key vs digital fingerprint

---

## Slide 4: The Evolution of Authentication

**Timeline:**

- 1960s: Passwords introduced
- 1990s: Two-factor authentication
- 2000s: Biometric authentication
- 2010s: Multi-factor authentication
- 2020s: AI-powered behavioral authentication

**Suggested Image:** Timeline infographic with authentication methods evolution, historical progression chart

---

## Slide 5: What is Authentication Detection?

**Definition:** Authentication detection is an AI-powered process that analyzes user behavior patterns to determine if an authentication attempt is legitimate, going beyond traditional credential verification.

**Key Components:**

- Behavioral biometrics
- Contextual analysis
- Pattern recognition
- Risk assessment

**Suggested Image:** Magnifying glass over user silhouette with data points, detective investigating digital footprints

---

## Slide 6: Behavioral Biometrics

**What AI Analyzes:**

- Typing rhythm and cadence
- Mouse movement patterns
- Touchscreen pressure and swipe patterns
- Navigation behavior
- Time spent on pages
- Click patterns

**Suggested Image:** Hands typing with data visualization overlay, fingerprint made of typing patterns

---

## Slide 7: Keystroke Dynamics

**How It Works:**

- Measures time between keystrokes (dwell time)
- Analyzes pressure applied to keys
- Studies typing rhythm patterns
- Creates unique user profiles

**Example:** User types "password" in consistent 0.8 seconds
Attacker types same word in 1.3 seconds → Red flag

**Suggested Image:** Keyboard with wave patterns showing timing, graph showing keystroke timing patterns

---

## Slide 8: Mouse Movement Analysis

**Behavioral Indicators:**

- Cursor trajectory patterns
- Click accuracy and hesitation
- Scroll wheel usage patterns
- Double-click timing
- Mouse acceleration preferences

**Detection Method:** AI creates movement "fingerprints" unique to each user

**Suggested Image:** Mouse cursor trail with analytics overlay, heat map of mouse movements on screen

---

## Slide 9: Contextual Analysis Factors

**Location-Based:**

- IP address geolocation
- GPS coordinates (mobile)
- Network characteristics
- Timezone consistency

**Device-Based:**

- Browser fingerprinting
- Operating system details
- Screen resolution and specs
- Installed fonts and plugins

**Suggested Image:** World map with connection points, device icons with data points

---

## Slide 10: Risk-Based Authentication Flow

**Process:**

1. User initiates login
2. AI analyzes behavioral patterns
3. System calculates risk score
4. Determines authentication requirements
5. Applies appropriate security measures
6. Continuous monitoring during session

**Suggested Image:** Flowchart with decision points, traffic light system showing risk levels

# Slides Bổ Sung cho Module 7: Machine Learning & Feature Engineering

## **Insert these slides after Slide 10 (Risk-Based Authentication Flow)**

---

## Slide 10A: Introduction to ML for Authentication

**Title:** Why Machine Learning for Authentication?

**Content:**

**Traditional Rule-Based Approach:**
- Fixed rules: "Block after 5 failed attempts"
- Cannot adapt to new attack patterns
- High false positives
- Manual threshold tuning

**AI/Machine Learning Approach:**
- Learns patterns from data automatically
- Adapts to new threats
- Personalized risk assessment
- Continuous improvement

**Key Benefit:** ML can detect **subtle behavioral differences** that humans cannot see!

**Example:**
- Traditional: "Is password correct? Yes/No"
- ML: "Does typing pattern match user's history? 87% match → Medium risk"

**Suggested Image:** Side-by-side comparison of rule-based system vs ML system, brain with neural connections, adaptive vs static security

---

## Slide 10B: Machine Learning Models for Authentication

**Title:** Three Main Types of ML Models

**Content:**

**1. Supervised Learning** 🎯
- **When to use:** You have labeled data (normal vs attack)
- **Models:** Random Forest, SVM, Neural Networks
- **Example:** Training on 10,000 labeled login attempts

**2. Unsupervised Learning** 🔍
- **When to use:** No labels, find anomalies
- **Models:** Isolation Forest, One-Class SVM, Autoencoders
- **Example:** Detecting unusual behavior without knowing attack types

**3. Semi-Supervised Learning** 🎭
- **When to use:** Small labeled data + large unlabeled data
- **Models:** Self-training, Co-training
- **Example:** 1,000 labeled + 100,000 unlabeled logins

**Decision Guide:**
```
Have labeled attack data? → Supervised Learning
Only normal data? → Unsupervised Learning
Little labeled data? → Semi-Supervised Learning
```

**Suggested Image:** Three paths diagram, model selection decision tree, classification vs anomaly detection illustration

---

## Slide 10C: Random Forest for Authentication

**Title:** Random Forest: Ensemble of Decision Trees

**How It Works:**

**Concept:** Multiple decision trees vote together for better accuracy

**Example Decision Tree:**
```
Is typing speed > 100 WPM? 
├─ Yes → Is location same as yesterday?
│   ├─ Yes → Low Risk (0.2)
│   └─ No → Check IP reputation...
└─ No → Is this a new device?
    └─ ...
```

**Random Forest = 100+ trees voting together**

**Advantages for Authentication:**
✅ **Feature Importance:** Shows which features matter most
✅ **Handles Missing Data:** Works even if some features unavailable
✅ **Non-linear Patterns:** Captures complex behaviors
✅ **Robust:** Less overfitting than single tree

**Disadvantages:**
❌ Slower prediction time (100+ trees)
❌ Harder to interpret than single tree

**Simple Implementation:**
```python
from sklearn.ensemble import RandomForestClassifier

# Features: typing_speed, location_change, time_of_day, etc.
model = RandomForestClassifier(
    n_estimators=100,  # 100 trees
    max_depth=10,      # Prevent overfitting
    random_state=42
)

model.fit(X_train, y_train)  # y: 0=normal, 1=attack
risk_score = model.predict_proba(X_test)[:, 1]  # Probability of attack
```

**Real-World Performance:**
- Accuracy: 94-97%
- False Positive Rate: 2-5%
- Training Time: 5-10 minutes on 100K samples

**Suggested Image:** Forest of decision trees illustration, feature importance bar chart, voting mechanism diagram

---

## Slide 10D: Support Vector Machine (SVM)

**Title:** SVM: Finding the Optimal Boundary

**How It Works:**

**Concept:** Find the best line/surface that separates normal vs attack patterns

**Visual Example:**
```
        Normal Logins ●●●
                        |  <-- Decision Boundary
                        |
Attack Logins ✖✖✖       |
```

**SVM finds the boundary with maximum margin (safety distance)**

**Advantages for Authentication:**
✅ **Effective with High-Dimensional Data:** Works well with 50-100 features
✅ **Memory Efficient:** Only stores support vectors (boundary points)
✅ **Works with Small Datasets:** Can train with 1,000-10,000 samples
✅ **Kernel Trick:** Handles non-linear patterns

**Disadvantages:**
❌ Slow training on large datasets (>100K samples)
❌ Sensitive to feature scaling
❌ Hard to interpret (black box)

**Implementation:**
```python
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# IMPORTANT: SVM requires feature scaling!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

model = SVC(
    kernel='rbf',      # Radial Basis Function for non-linear
    C=1.0,             # Regularization
    gamma='scale',     # Kernel coefficient
    probability=True   # Enable probability estimates
)

model.fit(X_train_scaled, y_train)
risk_score = model.predict_proba(X_test_scaled)[:, 1]
```

**When to Use SVM:**
- Small to medium datasets (1K - 50K samples)
- High-dimensional feature space
- Clear separation between classes
- Need mathematical guarantee of optimality

**Suggested Image:** SVM decision boundary illustration, support vectors highlighted, 2D scatter plot with separating hyperplane, margin visualization

---

## Slide 10E: Neural Networks for Authentication

**Title:** Neural Networks: Deep Learning Approach

**How It Works:**

**Architecture Example:**
```
Input Layer        Hidden Layers        Output Layer
(Features)         (Learning)           (Risk Score)

[Typing Speed] ●
[Mouse Pattern] ● → [●●●] → [●●●] → [● Risk: 0.85]
[Location]      ●
[Time]          ●
[Device Info]   ●
```

**Each layer learns increasingly complex patterns**

**Types for Authentication:**

**1. Feedforward Neural Network (FNN)**
- Simple, fast
- Good for static features
- Example: 50 input features → 2 hidden layers → risk score

**2. Recurrent Neural Network (RNN/LSTM)**
- For sequence data
- Remembers previous events
- Example: Analyzing last 10 login attempts as sequence

**3. Autoencoder**
- Unsupervised anomaly detection
- Learns "normal" behavior
- Flags anything different as anomaly

**Advantages:**
✅ **Automatic Feature Learning:** No manual feature engineering
✅ **Complex Patterns:** Captures subtle behavioral nuances
✅ **Scalable:** Works with millions of samples
✅ **Flexible:** Can combine different data types

**Disadvantages:**
❌ **Data Hungry:** Needs 10K-1M+ samples
❌ **Computational Cost:** Requires GPU for training
❌ **Black Box:** Hard to explain decisions
❌ **Overfitting Risk:** Can memorize training data

**Simple Implementation:**
```python
from tensorflow import keras
from tensorflow.keras import layers

# Build a simple feedforward neural network
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(50,)),  # 50 features
    layers.Dropout(0.3),  # Prevent overfitting
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid')  # Risk score 0-1
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy', 'precision', 'recall']
)

model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)
risk_score = model.predict(X_test)
```

**Real-World Performance:**
- Accuracy: 96-99% (with enough data)
- Training Time: 30 min - 2 hours
- Inference: <1ms per prediction

**Suggested Image:** Neural network architecture diagram, neurons and connections, deep learning layers visualization, brain-inspired network

---

## Slide 10F: Model Comparison & Selection Guide

**Title:** Which Model Should You Choose?

**Comparison Table:**

| Criteria | Random Forest | SVM | Neural Networks |
|----------|--------------|-----|-----------------|
| **Dataset Size** | 1K - 100K ✅ | 1K - 50K ✅ | 10K - 1M+ ✅ |
| **Training Speed** | Fast ⚡ | Medium ⏱️ | Slow 🐌 |
| **Prediction Speed** | Medium ⏱️ | Fast ⚡ | Fast ⚡ |
| **Interpretability** | High 👍 | Low 👎 | Very Low 👎 |
| **Feature Engineering** | Some needed | Required | Automatic |
| **Overfitting Risk** | Low ✅ | Low ✅ | High ⚠️ |
| **Handles Missing Data** | Yes ✅ | No ❌ | No ❌ |

**Decision Guide:**

```
Start with small dataset (1K-10K)? → Random Forest
  ├─ Need interpretability? → Random Forest
  └─ Want best accuracy? → SVM

Medium dataset (10K-50K)? → SVM or Random Forest
  ├─ Need fast training? → Random Forest
  └─ Want optimal boundary? → SVM

Large dataset (>50K)? → Neural Networks
  ├─ Have GPU? → Deep Neural Network
  └─ CPU only? → Random Forest
```

**Recommended Approach: Ensemble!**
```python
# Combine multiple models for best results
from sklearn.ensemble import VotingClassifier

ensemble = VotingClassifier(
    estimators=[
        ('rf', random_forest_model),
        ('svm', svm_model),
        ('nn', neural_network_model)
    ],
    voting='soft'  # Use probability averaging
)

# Final prediction = weighted average of all models
risk_score = ensemble.predict_proba(X_test)
```

**Industry Best Practices:**
- Start with Random Forest (easiest to debug)
- Add SVM for comparison
- Use Neural Networks only if you have >50K samples
- Combine all three for production systems

**Suggested Image:** Decision tree for model selection, comparison matrix heatmap, ensemble voting illustration

---

## Slide 10G: Training Data Requirements

**Title:** How Much Data Do You Need?

**Minimum Dataset Sizes:**

**For Different Models:**
- **Random Forest:** 1,000 - 5,000 samples minimum
- **SVM:** 1,000 - 10,000 samples minimum
- **Neural Networks:** 10,000 - 100,000+ samples minimum

**For Authentication Specifically:**
- **Per User Profiling:** 50-100 login sessions per user
- **General Anomaly Detection:** 10,000+ normal logins
- **Attack Detection:** 1,000+ labeled attack examples

**Data Quality > Data Quantity!**

**The Label Problem:**

**Where to Get Labeled Data?**

**1. Historical Security Incidents** 🔍
```
Source: Security logs from past 6-12 months
Labels: Known attacks flagged by security team
Challenge: Only ~0.1-1% of data is labeled attacks
```

**2. Simulated Attacks** 🧪
```
Method: Red team creates fake attacks in test environment
Labels: All simulated attacks are labeled
Challenge: May not represent real-world attacks
```

**3. Honeypot Data** 🍯
```
Method: Deploy decoy systems to attract attackers
Labels: All traffic to honeypot = malicious
Challenge: Limited diversity of attacks
```

**4. Crowdsourced/Public Datasets** 🌐
```
Examples: 
- KDD Cup 99
- NSL-KDD
- CICIDS2017
Challenge: May not match your specific environment
```

**5. Semi-Supervised Approach** 🎭
```
Method: Label small set manually, use ML to label rest
Steps:
1. Manually label 1,000 samples
2. Train initial model
3. Model suggests labels for remaining data
4. Human reviews high-confidence predictions
5. Iteratively improve
```

**Practical Data Collection Strategy:**

**Phase 1: Bootstrap (Month 1-2)**
```
Collect: 10,000 normal logins (unlabeled)
Action: Deploy unsupervised model (Isolation Forest)
Goal: Start detecting obvious anomalies
```

**Phase 2: Label Building (Month 3-6)**
```
Collect: Security team investigates anomalies
Action: Build labeled dataset of 1,000-5,000 samples
Goal: Train supervised model
```

**Phase 3: Production (Month 6+)**
```
Collect: Continuous data collection
Action: Regular model retraining (monthly)
Goal: Adapt to evolving threats
```

**Data Balance Issue:**

**Imbalanced Classes Problem:**
```
Typical Distribution:
├─ Normal Logins: 99.5% (99,500 samples)
└─ Attacks: 0.5% (500 samples)

Problem: Model learns to always predict "normal"
```

**Solutions:**
1. **SMOTE** (Synthetic Minority Over-sampling)
2. **Class Weights** (penalize misclassifying attacks more)
3. **Anomaly Detection** instead of classification

**Code Example:**
```python
from imblearn.over_sampling import SMOTE

# Original: 99,500 normal + 500 attacks
X_resampled, y_resampled = SMOTE().fit_resample(X_train, y_train)
# After SMOTE: 99,500 normal + 99,500 synthetic attacks

# Or use class weights
model = RandomForestClassifier(
    class_weight={0: 1, 1: 200}  # Attacks weighted 200x more
)
```

**Data Storage & Privacy:**

**Storage Requirements:**
```
Per login event: ~1KB (features only)
Per day (10K logins): 10MB
Per year: 3.65GB
With raw data: 10-50x more (36-180GB/year)
```

**Privacy Considerations:**
- ⚠️ Store only aggregated behavioral features, not raw keystrokes
- ⚠️ Anonymize user IDs
- ⚠️ Comply with GDPR/CCPA
- ⚠️ Regular data purging (keep only 6-12 months)

**Suggested Image:** Data collection funnel, labeled vs unlabeled data pie chart, data balance before/after SMOTE, timeline for data collection phases

---

## Slide 10H: Feature Engineering for Behavioral Biometrics

**Title:** Extracting Features from Raw Behavior Data

**What is Feature Engineering?**

**Raw Data → Features → ML Model**

**Example:**
```
Raw: User types "password123" 
     Keystroke times: [0ms, 120ms, 240ms, 280ms, ...]

Features:
├─ Average dwell time: 85ms
├─ Average flight time: 120ms
├─ Typing speed: 94 WPM
├─ Variance in timing: 15ms
└─ Error rate: 0% (no backspace)
```

**Feature Engineering = Converting raw behavior into numbers that ML can understand**

---

**1. Keystroke Dynamics Features** ⌨️

**Temporal Features:**
```python
def extract_keystroke_features(keystroke_events):
    features = {}
    
    # Dwell time: how long key is pressed
    dwell_times = [event.key_up_time - event.key_down_time 
                   for event in keystroke_events]
    features['dwell_time_mean'] = np.mean(dwell_times)
    features['dwell_time_std'] = np.std(dwell_times)
    
    # Flight time: time between releasing one key and pressing next
    flight_times = [keystroke_events[i+1].key_down_time - 
                    keystroke_events[i].key_up_time
                    for i in range(len(keystroke_events)-1)]
    features['flight_time_mean'] = np.mean(flight_times)
    features['flight_time_std'] = np.std(flight_times)
    
    # Typing speed (Words Per Minute)
    total_time = keystroke_events[-1].timestamp - keystroke_events[0].timestamp
    num_chars = len(keystroke_events)
    features['typing_speed_wpm'] = (num_chars / 5) / (total_time / 60)
    
    # Rhythm (timing between specific key pairs)
    features['th_digraph_time'] = get_digraph_time('t', 'h', keystroke_events)
    features['er_digraph_time'] = get_digraph_time('e', 'r', keystroke_events)
    
    return features
```

**Common Features (20-30 total):**
- Mean/Std of dwell times
- Mean/Std of flight times
- Typing speed (WPM)
- Error rate (backspace frequency)
- Pause patterns (long pauses > 2 seconds)
- Digraph timings (specific letter pairs)

---

**2. Mouse Movement Features** 🖱️

**Trajectory & Speed Features:**
```python
def extract_mouse_features(mouse_events):
    features = {}
    
    # Extract coordinates
    x_coords = [event.x for event in mouse_events]
    y_coords = [event.y for event in mouse_events]
    
    # Movement distance
    distances = [
        np.sqrt((x_coords[i+1] - x_coords[i])**2 + 
                (y_coords[i+1] - y_coords[i])**2)
        for i in range(len(x_coords)-1)
    ]
    features['total_distance'] = np.sum(distances)
    features['avg_distance_per_move'] = np.mean(distances)
    
    # Velocity and acceleration
    timestamps = [event.timestamp for event in mouse_events]
    velocities = [distances[i] / (timestamps[i+1] - timestamps[i])
                  for i in range(len(distances)-1)]
    features['avg_velocity'] = np.mean(velocities)
    features['max_velocity'] = np.max(velocities)
    
    # Movement patterns
    features['num_direction_changes'] = count_direction_changes(x_coords, y_coords)
    features['movement_curvature'] = calculate_curvature(x_coords, y_coords)
    
    # Click patterns
    click_events = [e for e in mouse_events if e.type == 'click']
    features['click_duration_mean'] = np.mean([e.duration for e in click_events])
    features['double_click_speed'] = calculate_double_click_speed(click_events)
    
    return features
```

**Common Features (25-35 total):**
- Total movement distance
- Average velocity
- Direction changes
- Curvature (straightness vs curves)
- Click duration
- Double-click timing
- Scroll wheel usage patterns

---

**3. Contextual Features** 🌍

**Location & Device Features:**
```python
def extract_contextual_features(login_event, user_history):
    features = {}
    
    # Geographic features
    features['is_new_country'] = (login_event.country not in user_history.countries)
    features['is_new_city'] = (login_event.city not in user_history.cities)
    features['distance_from_last_login'] = calculate_distance(
        login_event.location, user_history.last_login.location
    )
    
    # Time-based features
    features['hour_of_day'] = login_event.timestamp.hour
    features['day_of_week'] = login_event.timestamp.weekday()
    features['is_weekend'] = (features['day_of_week'] >= 5)
    features['is_business_hours'] = (9 <= features['hour_of_day'] <= 17)
    
    # Device features
    features['is_new_device'] = (login_event.device_id not in user_history.devices)
    features['is_new_browser'] = (login_event.browser not in user_history.browsers)
    features['is_new_os'] = (login_event.os not in user_history.os_list)
    
    # Network features
    features['is_vpn'] = detect_vpn(login_event.ip)
    features['is_tor'] = detect_tor(login_event.ip)
    features['ip_reputation_score'] = get_ip_reputation(login_event.ip)
    
    return features
```

**Common Features (15-25 total):**
- IP geolocation (country, city, lat/lon)
- Time of day, day of week
- Device fingerprint
- Browser/OS information
- VPN/Proxy detection
- IP reputation score

---

**4. Historical/Sequential Features** 📊

**User Behavior History:**
```python
def extract_historical_features(user_id, current_event, lookback_days=30):
    features = {}
    
    # Get user's recent activity
    recent_logins = get_recent_logins(user_id, lookback_days)
    
    # Login frequency
    features['logins_per_day'] = len(recent_logins) / lookback_days
    features['days_since_last_login'] = (current_event.timestamp - 
                                         recent_logins[-1].timestamp).days
    
    # Consistency scores (how similar is current event to history?)
    features['location_consistency'] = calculate_location_consistency(
        current_event, recent_logins
    )
    features['time_consistency'] = calculate_time_consistency(
        current_event, recent_logins
    )
    features['device_consistency'] = calculate_device_consistency(
        current_event, recent_logins
    )
    
    # Anomaly indicators
    features['num_failed_logins_last_24h'] = count_failed_logins(user_id, hours=24)
    features['num_different_ips_last_7d'] = count_unique_ips(user_id, days=7)
    
    return features
```

**Common Features (10-20 total):**
- Login frequency patterns
- Time since last login
- Number of unique locations/devices
- Failed login attempts
- Consistency scores

---

## Slide 10I: Feature Engineering Example

**Title:** Complete Example: From Raw Data to Features

**Scenario: User Login Event**

**Raw Data Collected:**
```json
{
  "user_id": "user123",
  "timestamp": "2025-10-20 14:30:00",
  "ip_address": "203.0.113.45",
  "device_id": "iPhone_13_Safari",
  "keystrokes": [
    {"key": "p", "down": 0, "up": 85},
    {"key": "a", "down": 120, "up": 195},
    {"key": "s", "down": 245, "up": 330},
    ...
  ],
  "mouse_movements": [
    {"x": 100, "y": 200, "t": 0},
    {"x": 150, "y": 210, "t": 50},
    ...
  ]
}
```

**Step 1: Extract Basic Features**
```python
# Keystroke features
typing_speed = 94.5  # WPM
dwell_time_avg = 85  # ms
flight_time_avg = 120  # ms

# Mouse features
total_distance = 1250  # pixels
avg_velocity = 450  # pixels/second

# Contextual features
hour_of_day = 14  # 2 PM
is_new_location = False
is_new_device = True  # First time from iPhone
```

**Step 2: Historical Comparison**
```python
# Compare with user's history (last 30 days)
user_profile = {
    'typical_typing_speed': 92.3,
    'typical_dwell_time': 88,
    'typical_login_time': 9,  # Usually logs in at 9 AM
    'typical_location': 'New York'
}

# Calculate deviations
typing_speed_deviation = abs(94.5 - 92.3) / 92.3  # 2.4% difference
time_deviation = abs(14 - 9)  # 5 hours different
```

**Step 3: Create Feature Vector**
```python
feature_vector = [
    # Behavioral biometrics (normalized 0-1)
    0.945,  # typing_speed_normalized
    0.85,   # dwell_time_normalized
    1.20,   # flight_time_normalized
    0.78,   # mouse_velocity_normalized
    
    # Temporal
    14,     # hour_of_day
    1,      # is_weekday (boolean)
    
    # Contextual
    0,      # is_new_location (boolean)
    1,      # is_new_device (boolean)
    0.82,   # ip_reputation_score
    
    # Historical deviation
    0.024,  # typing_speed_deviation
    5.0,    # time_deviation_hours
    0.95,   # location_consistency_score
    
    # ... 40 more features ...
]

# Total: 50-100 features ready for ML model
```

**Step 4: Feed to ML Model**
```python
# Model predicts risk score
risk_score = ml_model.predict_proba(feature_vector)[0][1]
# Output: risk_score = 0.35 (35% probability of attack)

# Decision
if risk_score < 0.4:
    action = "Allow"
elif risk_score < 0.7:
    action = "Require MFA"
else:
    action = "Block and Alert"
```

**Feature Engineering Best Practices:**

✅ **Do:**
- Normalize/scale features to same range
- Handle missing values (use mean/median imputation)
- Remove highly correlated features
- Test feature importance
- Document feature meanings

❌ **Don't:**
- Include user PII (names, emails) as features
- Use raw timestamps (convert to hour/day)
- Ignore outliers without investigation
- Forget to version your features
- Mix different scales without normalization

**Suggested Image:** Data flow diagram from raw data to feature vector, feature extraction pipeline, before/after normalization comparison

---

## Slide 10J: Summary - ML Pipeline for Authentication

**Title:** Putting It All Together

**Complete ML Authentication Pipeline:**

```
1. DATA COLLECTION
   ├─ Raw behavior data (keystrokes, mouse, etc.)
   ├─ Contextual data (IP, device, time)
   └─ Historical data (past logins)
          ↓
2. FEATURE ENGINEERING
   ├─ Extract 50-100 features
   ├─ Normalize/scale
   └─ Handle missing values
          ↓
3. MODEL TRAINING
   ├─ Choose model (RF/SVM/NN)
   ├─ Train on labeled data (1K-100K samples)
   └─ Validate on test set
          ↓
4. MODEL DEPLOYMENT
   ├─ Real-time prediction (<100ms)
   ├─ Risk score calculation
   └─ Decision making (allow/MFA/block)
          ↓
5. MONITORING & IMPROVEMENT
   ├─ Track performance (accuracy, FP rate)
   ├─ Collect feedback
   └─ Retrain monthly
```

**Key Takeaways:**

1️⃣ **Start Simple:** Begin with Random Forest on 5,000 samples
2️⃣ **Feature Engineering is Key:** 80% of success comes from good features
3️⃣ **Data Quality > Quantity:** 1,000 clean samples > 10,000 noisy samples
4️⃣ **Continuous Improvement:** Retrain regularly as behaviors evolve
5️⃣ **Combine Approaches:** Use ensemble for best results

**Realistic Expectations:**

**First 3 Months:**
- Accuracy: 85-90%
- False Positive Rate: 5-10%
- Detection Rate: 70-80%

**After 6-12 Months:**
- Accuracy: 94-97%
- False Positive Rate: 2-5%
- Detection Rate: 85-95%

**Required Resources:**
- Data Scientists: 1-2 FTE
- Infrastructure: $1K-5K/month (cloud compute)
- Training Data: 6-12 months of logs
- Development Time: 3-6 months to production

**Next Steps:**
- Module 7 continues: Slack integration for alerts
- Module 8: Using GANs for adversarial testing
- Hands-on Exercise: Build your own auth ML model!

**Suggested Image:** Complete pipeline visualization, timeline showing improvement over time, resource requirements infographic, success metrics dashboard

---

## 📚 How to Use These Slides

### **Recommended Flow:**

```
Slide 10  (Risk-Based Auth Flow - existing)
    ↓
Slide 10A (Why ML for Auth?)
Slide 10B (ML Model Types Overview)
Slide 10C (Random Forest)
Slide 10D (SVM)
Slide 10E (Neural Networks)
Slide 10F (Model Comparison)
Slide 10G (Training Data Requirements)
Slide 10H (Feature Engineering)
Slide 10I (Feature Engineering Example)
Slide 10J (ML Pipeline Summary)
    ↓
Slide 11  (Authentication Abuse Types - existing)
```

### **Teaching Tips:**

1. **Slide 10A-10B (15 mins):** Motivate why ML is needed, overview
2. **Slide 10C-10F (30 mins):** Deep dive into each model, show demos
3. **Slide 10G (15 mins):** Data requirements - critical discussion
4. **Slide 10H-10I (20 mins):** Feature engineering with live coding
5. **Slide 10J (10 mins):** Wrap-up, Q&A

**Total time added: ~90 minutes (1.5 hours)**

### **Hands-On Exercise Suggestion:**

After Slide 10J, add a 60-minute exercise:
- Provide a small dataset (CSV with 1000 login samples)
- Students extract features and train Random Forest
- Compare results across groups
- Discuss what worked and what didn't

Bạn có muốn tôi:
1. Tạo code examples chi tiết hơn cho hands-on exercise?
2. Thêm quiz questions để test hiểu biết?
3. Tạo thêm visual diagrams cho các slides này?

---

## Slide 11: Authentication Abuse Types

**Common Attack Vectors:**

- Credential stuffing attacks
- Brute force attempts
- Account takeover (ATO)
- Session hijacking
- Password spraying
- Social engineering attacks

**Suggested Image:** Hacker silhouette with multiple attack method icons, warning signs with different threat types

---

## Slide 12: Credential Stuffing Explained

**Attack Method:**

- Automated use of leaked username/password pairs
- Exploits password reuse across multiple sites
- High volume, low success rate attacks
- Often uses botnets for distribution

**AI Detection:**

- Velocity analysis
- Behavioral inconsistencies
- Geographic anomalies
- Device fingerprint analysis

**Suggested Image:** Data breach graphic with credentials flowing to multiple sites, botnet visualization

---

## Slide 13: Brute Force Attack Detection

**Traditional Approach:**

- Count failed attempts
- Lock account after threshold
- High false positives

**AI-Enhanced Detection:**

```python
def detect_brute_force(attempts):
    velocity_score = analyze_attempt_velocity(attempts)
    pattern_score = analyze_attempt_patterns(attempts)
    source_score = analyze_source_reputation(attempts)

    return calculate_composite_risk_score(
        velocity_score, pattern_score, source_score
    )
```

**Suggested Image:** Code snippet visualization, graph showing attack pattern detection

---

## Slide 14: Account Takeover (ATO) Prevention

**ATO Indicators:**

- Sudden behavior changes
- New device/location combinations
- Unusual transaction patterns
- Modified account settings
- Different usage timings

**AI Response:**

- Real-time behavioral monitoring
- Anomaly detection algorithms
- Automatic session termination
- Multi-layered verification

**Suggested Image:** Account being protected by AI shield, before/after user behavior comparison

---

## Slide 15: Session Hijacking Detection

**Attack Characteristics:**

- Session token theft
- Man-in-the-middle attacks
- Cross-site scripting (XSS)
- Session fixation

**AI Detection Methods:**

- Continuous behavioral validation
- Network pattern analysis
- Session consistency checks
- Real-time risk scoring

**Suggested Image:** Network connection being intercepted, session security visualization

---

## Slide 16: Velocity Analysis Implementation

**Code Example:**

```python
class VelocityAnalyzer:
    def __init__(self, time_window=300):  # 5 minutes
        self.time_window = time_window
        self.max_attempts = 5

    def is_suspicious_velocity(self, login_attempts):
        recent_attempts = self.filter_recent_attempts(
            login_attempts, self.time_window
        )
        return len(recent_attempts) > self.max_attempts
```

**Suggested Image:** Speedometer showing attack velocity, graph with time-based attempt analysis

---

## Slide 17: Geographic Anomaly Detection

**Impossible Travel Detection:**

- User in New York at 9 AM
- Same user in Tokyo at 9:30 AM
- Physical impossibility → High risk

**Geolocation Factors:**

- Distance calculation
- Time zone analysis
- Travel time feasibility
- Historical location patterns

**Suggested Image:** World map showing impossible travel paths, airplane with speed calculations

---

## Slide 18: Device Fingerprinting

**Browser Fingerprint Components:**

- User agent string
- Screen resolution
- Installed fonts
- Timezone settings
- Language preferences
- Plugin details
- Canvas fingerprinting

**Uniqueness:** Modern fingerprints can identify devices with 99.5% accuracy

**Suggested Image:** Device with unique fingerprint pattern, browser characteristics visualization

---

## Slide 19: Account Reputation Scoring Overview

**Concept:** Account reputation scoring assigns numerical values (0-100) to user accounts based on historical behavior, current context, and risk indicators.

**Benefits:**

- Dynamic risk assessment
- Personalized security measures
- Reduced false positives
- Improved user experience

**Suggested Image:** Credit score visualization adapted for accounts, gauge showing reputation levels

---

## Slide 20: Reputation Scoring Factors

**Historical Behavior (40%):**

- Login consistency
- Transaction patterns
- Account age
- Past security incidents

**Current Context (35%):**

- Location/time patterns
- Device consistency
- Network reputation

**Security Posture (25%):**

- Password strength
- 2FA usage
- Security settings

**Suggested Image:** Pie chart showing factor weights, scale balancing different reputation elements

---

## Slide 21: Reputation Score Calculation

**Implementation:**

```python
class ReputationScorer:
    def calculate_score(self, user_data):
        base_score = 50

        historical_score = self.analyze_history(
            user_data.login_history,
            user_data.transaction_history
        )

        context_score = self.analyze_context(
            user_data.current_location,
            user_data.device_info
        )

        security_score = self.analyze_security(
            user_data.password_strength,
            user_data.two_factor_enabled
        )

        return min(100, base_score + historical_score + 
                  context_score + security_score)
```

**Suggested Image:** Calculator with security metrics, algorithm flowchart

---

## Slide 22: Dynamic Score Adjustment

**Real-time Updates:**

- Successful authentic logins → +2 points
- Failed login attempts → -1 point
- Password change → +3 points
- Security incident → -10 points
- Suspicious activity → -5 points
- 2FA activation → +5 points

**Score Recovery:** Gradual improvement over time with positive behavior

**Suggested Image:** Graph showing score changes over time, thermometer showing reputation temperature

---

## Slide 23: Risk-Based Actions by Score

**High Reputation (80-100):**

- Seamless authentication
- Minimal friction
- Express checkout
- Reduced monitoring

**Medium Reputation (50-79):**

- Standard verification
- Periodic challenges
- Transaction limits

**Low Reputation (0-49):**

- Enhanced verification
- Account restrictions
- Manual review required

**Suggested Image:** Traffic light system with different security levels, pyramid showing privilege levels

---

## Slide 24: Slack Integration Overview

**Why Slack for Security?**

- Real-time team communication
- Instant alert distribution
- Interactive response capabilities
- Audit trail maintenance
- Integration with security tools
- Mobile accessibility

**Use Cases:**

- Security incident alerts
- Authentication anomaly notifications
- Team collaboration on threats

**Suggested Image:** Slack interface with security alerts, team collaboration around security dashboard

---

## Slide 25: Slack Events API

**Event Types for Security:**

- `message` events for commands
- `app_mention` for bot interactions
- `team_join` for new user monitoring
- `user_change` for profile modifications

**Authentication Events to Monitor:**

- Suspicious login attempts
- Account lockouts
- Password reset requests
- Multi-factor authentication failures

**Suggested Image:** API connection diagram, webhook notification flow

---

## Slide 26: Setting Up Slack Bot

**Bot Configuration:**

```python
import slack_sdk
from slack_bolt import App

app = App(
    token="xoxb-your-bot-token",
    signing_secret="your-signing-secret"
)

@app.event("app_mention")
def handle_app_mention(event, say):
    user_id = event['user']
    say(f"Hello <@{user_id}>! I'm your security bot.")

if __name__ == "__main__":
    app.start(port=3000)
```

**Suggested Image:** Slack bot configuration screen, code editor with bot setup

---

## Slide 27: Security Alert Message Format

**Alert Structure:**

```python
def create_security_alert(user_id, risk_score, details):
    return {
        "text": f"🚨 Security Alert: User {user_id}",
        "blocks": [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": "Security Alert"}
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*User:* {user_id}"},
                    {"type": "mrkdwn", "text": f"*Risk Score:* {risk_score}/100"}
                ]
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*Details:* {details}"}
            }
        ]
    }
```

**Suggested Image:** Slack message mockup with security alert, formatted notification example

---

## Slide 28: Interactive Security Actions

**Action Buttons:**

```python
{
    "type": "actions",
    "elements": [
        {
            "type": "button",
            "text": {"type": "plain_text", "text": "🔒 Lock Account"},
            "value": f"lock_{user_id}",
            "action_id": "lock_account",
            "style": "danger"
        },
        {
            "type": "button", 
            "text": {"type": "plain_text", "text": "🔍 Investigate"},
            "value": f"investigate_{user_id}",
            "action_id": "investigate"
        },
        {
            "type": "button",
            "text": {"type": "plain_text", "text": "✅ Mark Safe"},
            "value": f"safe_{user_id}", 
            "action_id": "mark_safe",
            "style": "primary"
        }
    ]
}
```

**Suggested Image:** Interactive Slack message with buttons, security team response interface

---

## Slide 29: Handling Button Interactions

**Action Handler:**

```python
@app.action("lock_account")
def handle_lock_account(ack, body, logger):
    ack()  # Acknowledge the action

    user_id = body["actions"][0]["value"].split("_")[1]

    # Lock the account in your system
    lock_user_account(user_id)

    # Update the Slack message
    update_message_with_action_taken(
        body, f"Account {user_id} has been locked"
    )

    logger.info(f"Account {user_id} locked via Slack")
```

**Suggested Image:** Action handler flowchart, security response workflow diagram

---

## Slide 30: Real-Time Monitoring Dashboard

**Bot Commands:**

- `/security-status [user_id]` - Check user security status
- `/threat-summary` - Daily threat summary
- `/lock-account [user_id]` - Emergency account lock
- `/reputation-score [user_id]` - Check account reputation

**Dashboard Metrics:**

- Active threats
- Authentication success rate
- False positive rate
- Response time metrics

**Suggested Image:** Slack slash commands interface, security metrics dashboard

---

## Slide 31: Bot Event Subscriptions

**Critical Events to Subscribe:**

```python
# Authentication events
app.event("login_attempt")
app.event("login_failure") 
app.event("password_reset")
app.event("account_locked")

# Behavioral anomalies
app.event("location_anomaly")
app.event("device_anomaly")
app.event("velocity_anomaly")
app.event("reputation_drop")

# Security incidents
app.event("potential_takeover")
app.event("suspicious_transaction")
```

**Suggested Image:** Event subscription flowchart, webhook configuration interface

---

## Slide 32: Automated Response Rules

**Rule Engine:**

```python
class SecurityRuleEngine:
    def __init__(self):
        self.rules = {
            'high_risk_login': self.handle_high_risk_login,
            'account_takeover': self.handle_account_takeover,
            'brute_force': self.handle_brute_force_attempt
        }

    def handle_high_risk_login(self, event):
        if event.risk_score > 80:
            self.lock_account(event.user_id)
            self.notify_security_team(event)
            self.require_additional_verification(event.user_id)
```

**Suggested Image:** Rule engine diagram, automated security response flowchart

---

## Slide 33: Escalation Procedures

**Escalation Levels:**

**Level 1 (Risk Score 40-59):**

- Log event
- Increase monitoring

**Level 2 (Risk Score 60-79):**

- Additional verification required
- Notify security team

**Level 3 (Risk Score 80-89):**

- Immediate Slack alert
- Account restriction
- Human review required

**Level 4 (Risk Score 90-100):**

- Emergency response
- Automatic account lock
- Executive notification

**Suggested Image:** Escalation pyramid, emergency response levels visualization

---

## Slide 34: Integration Architecture

**System Components:**

1. Authentication System
2. AI Risk Engine
3. Slack Bot Service
4. Database Layer
5. Logging System
6. Alert Manager

**Data Flow:** User Login → Risk Analysis → Alert Generation → Slack Notification → Human Response → System Update

**Suggested Image:** System architecture diagram, data flow visualization with components

---

## Slide 35: Post-Deployment Verification

**Why Verification is Critical:**

- Ensure AI models perform as expected
- Identify false positives/negatives
- Optimize detection thresholds
- Maintain system accuracy
- Validate business impact

**Verification Methods:**

- A/B testing
- Performance metrics monitoring
- User feedback analysis
- Security incident correlation

**Suggested Image:** Quality assurance checklist, performance monitoring dashboard

---

## Slide 36: Key Performance Indicators (KPIs)

**Security Effectiveness:**

- Threat detection rate (%)
- False positive rate (%)
- False negative rate (%)
- Mean time to detection (MTTD)
- Mean time to response (MTTR)

**User Experience:**

- Authentication success rate
- Average login time
- User complaint rate
- Support ticket volume

**System Performance:**

- Response time (ms)
- System availability (%)
- Processing capacity

**Suggested Image:** KPI dashboard, metrics visualization with gauges and charts

---

## Slide 37: Monitoring Framework Implementation

**Monitoring Bot:**

```python
class AuthenticationMonitor:
    def __init__(self, slack_bot):
        self.bot = slack_bot
        self.metrics_collector = MetricsCollector()

    def daily_health_check(self):
        metrics = self.metrics_collector.get_daily_metrics()

        report = self.generate_daily_report(metrics)

        self.bot.send_message(
            channel="#security-ops",
            message=report
        )

        if metrics.false_positive_rate > 0.05:  # 5%
            self.bot.send_alert("High false positive rate detected")
```

**Suggested Image:** Monitoring system architecture, health check dashboard

---

## Slide 38: Daily Security Report Format

**Automated Report:**

```
📊 Daily Authentication Security Report
Date: 2025-08-29

🔐 Authentication Summary:
• Total Attempts: 12,450
• Successful Logins: 12,201 (98.0%)
• Blocked Attempts: 249 (2.0%)

🛡️ Threat Detection:
• Credential Stuffing: 156 attempts blocked
• Brute Force: 67 attempts blocked
• Account Takeover: 12 attempts blocked
• Geographic Anomalies: 14 detected

⚡ Performance:
• Average Response Time: 0.2s
• System Uptime: 99.98%
• False Positive Rate: 0.8%

🎯 Top Risk Users:
1. user123@company.com (Score: 25)
2. user456@company.com (Score: 30)
```

**Suggested Image:** Daily report mockup, executive summary dashboard

---

## Slide 39: A/B Testing for Authentication

**Testing Framework:**

- Group A: Current AI model
- Group B: Updated AI model
- Metrics comparison over 30 days

**Test Parameters:**

```python
ab_test_config = {
    'group_a_percentage': 50,
    'group_b_percentage': 50,
    'test_duration_days': 30,
    'success_metrics': [
        'false_positive_rate',
        'detection_accuracy',
        'user_satisfaction'
    ]
}
```

**Suggested Image:** A/B testing split diagram, comparison charts showing test results

---

## Slide 40: False Positive Analysis

**Impact of False Positives:**

- User frustration
- Productivity loss
- Support costs
- Business reputation damage

**Reduction Strategies:**

- Machine learning model refinement
- User behavior learning
- Contextual analysis improvement
- Feedback loop integration

**Analysis Tools:**

- User journey mapping
- Error pattern identification
- Behavioral clustering

**Suggested Image:** User frustration visualization, false positive impact analysis chart

---

## Slide 41: Model Performance Tuning

**Optimization Techniques:**

- Feature selection refinement
- Threshold adjustment
- Ensemble model implementation
- Continuous learning integration

**Performance Metrics:**

```python
model_metrics = {
    'accuracy': 0.97,
    'precision': 0.95,
    'recall': 0.93,
    'f1_score': 0.94,
    'auc_roc': 0.96
}
```

**Tuning Process:**

1. Analyze current performance
2. Identify improvement areas
3. Adjust model parameters
4. Validate improvements
5. Deploy updates

**Suggested Image:** Model performance graphs, ROC curve visualization

---

## Slide 42: Security Incident Response Workflow

**Incident Response Steps:**

1. **Detection**: AI identifies threat
2. **Alert**: Slack notification sent
3. **Assessment**: Security team evaluates
4. **Response**: Immediate action taken
5. **Investigation**: Deeper analysis
6. **Recovery**: System restoration
7. **Lessons Learned**: Process improvement

**Response Times:**

- Critical: < 5 minutes
- High: < 15 minutes
- Medium: < 1 hour
- Low: < 24 hours

**Suggested Image:** Incident response flowchart, response time visualization

---

## Slide 43: Compliance and Audit Trail

**Regulatory Requirements:**

- GDPR data protection
- SOX financial compliance
- HIPAA healthcare security
- PCI DSS payment security

**Audit Trail Components:**

- Authentication attempts
- Risk score calculations
- Security decisions
- Human interventions
- System modifications

**Log Format:**

```json
{
  "timestamp": "2025-08-29T10:30:00Z",
  "user_id": "user123",
  "event_type": "high_risk_login",
  "risk_score": 85,
  "action_taken": "account_locked",
  "decision_maker": "AI_system",
  "reviewer": "security_analyst_jane"
}
```

**Suggested Image:** Compliance checklist, audit trail visualization

---

## Slide 44: Cost-Benefit Analysis

**Implementation Costs:**

- AI model development: $50,000
- Slack integration: $10,000
- Infrastructure: $20,000/year
- Training: $15,000
- Maintenance: $30,000/year

**Benefits:**

- Fraud prevention: $500,000/year saved
- Reduced support costs: $100,000/year
- Improved user experience: $200,000/year value
- Compliance adherence: $50,000/year saved

**ROI Calculation:** 650% return on investment

**Suggested Image:** Cost-benefit analysis chart, ROI calculation visualization

---

## Slide 45: Real-World Case Study: Banking

**Scenario:** Major bank implements AI authentication

**Before Implementation:**

- 15% false positive rate
- $2M annual fraud losses
- 500 daily support tickets
- 30-second average login time

**After Implementation:**

- 2% false positive rate
- $200K annual fraud losses
- 150 daily support tickets
- 5-second average login time

**Key Success Factors:**

- Gradual rollout strategy
- Extensive user training
- Continuous model refinement

**Suggested Image:** Banking security visualization, before/after comparison charts

---

## Slide 46: Implementation Best Practices

**Development Phase:**

- Start with pilot program
- Use historical data for training
- Implement gradual rollout
- Monitor performance closely

**Deployment Phase:**

- Comprehensive testing
- User training programs
- Clear escalation procedures
- Regular performance reviews

**Maintenance Phase:**

- Continuous model updates
- Regular security assessments
- User feedback integration
- Technology stack updates

**Suggested Image:** Best practices checklist, implementation timeline

---

## Slide 47: Common Implementation Challenges

**Technical Challenges:**

- Data quality issues
- Model accuracy concerns
- Integration complexity
- Performance optimization

**Business Challenges:**

- User acceptance
- Change management
- Budget constraints
- Regulatory compliance

**Solutions:**

- Thorough planning
- Stakeholder engagement
- Incremental improvements
- Regular communication

**Suggested Image:** Challenge and solution matching diagram, obstacle course visualization

---

## Slide 48: Future Trends in AI Authentication

**Emerging Technologies:**

- Continuous authentication
- Zero-trust architecture
- Quantum-resistant cryptography
- Behavioral prediction models
- Federated learning systems

**Market Predictions:**

- 40% growth in AI security market
- Passwordless authentication adoption
- Real-time risk scoring standard
- Cross-platform identity verification

**Innovation Areas:**

- Voice pattern recognition
- Gait analysis authentication
- Emotional state detection

**Suggested Image:** Future technology visualization, trending authentication methods

---

## Slide 49: Hands-On Exercise

**Build Your Own Authentication Bot:**

**Exercise Steps:**

1. Set up Slack workspace
2. Create basic authentication bot
3. Implement risk scoring algorithm
4. Add alert functionality
5. Test with sample data
6. Monitor performance metrics

**Provided Resources:**

- Sample code templates
- Test dataset
- Configuration guides
- Troubleshooting tips

**Expected Outcomes:**

- Working Slack bot
- Risk scoring implementation
- Performance metrics dashboard

**Suggested Image:** Coding exercise layout, step-by-step tutorial visualization

---

## Slide 50: Module 7 Summary and Next Steps

**Key Learning Points:** ✅ AI-enhanced authentication goes beyond passwords
✅ Behavioral analysis provides powerful security insights
✅ Account reputation scoring enables dynamic security
✅ Slack integration enables real-time security operations
✅ Continuous monitoring ensures system effectiveness

**Next Module Preview:** **Module 8: Generative Adversarial Networks (GANs) for Cyber Security**

- GAN fundamentals for security
- Network attack simulation
- IDS evasion techniques
- Facial recognition attacks

**Action Items:**

- Complete hands-on exercise
- Review provided code examples
- Prepare for Module 8

**Suggested Image:** Achievement badges, graduation cap with cybersecurity symbols, arrow pointing to next module

---

## Additional Image Suggestions for General Use:

- AI brain with security shield
- Lock and key with digital elements
- Network security diagrams
- Hacker vs defender illustrations
- Data flow visualizations
- Risk meter/gauge graphics
- Team collaboration images
- Code snippet screenshots
- Dashboard mockups
- Mobile security interfaces
- Biometric authentication visuals
- Alert notification graphics

These slides provide comprehensive coverage of Module 7 with practical examples, code implementations, and real-world applications. Each slide includes specific image suggestions to help visualize the concepts and make the content more engaging for students.

