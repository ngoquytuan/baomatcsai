# Báo Cáo Định Danh Nhóm Tấn Công — Dữ Liệu Thực Tế Honeypot
*Nguồn: MikroTik Home Network SOC — Cowrie + OpenCanary + YARA*
*Cập nhật: 2026-06-02 (v2 — thêm ML Lab results) | Dùng cho: CSAI2026 Module M2, M3, M5, M7*

---

## 1. Tổng Quan Tấn Công

| Chỉ số | Giá trị |
|--------|---------|
| Tổng IP tấn công | **1,879+** (7 ngày gần nhất) |
| Tổng phiên Cowrie | **230,000+** |
| Nhóm đã định danh (TA) | **10** |
| IP chưa định danh | **~1,870** |
| Malware đã thu thập | **28+ file** |
| Patterns phát hiện | **15 patterns** |

---

## 2. Danh Sách 10 Nhóm Đã Định Danh

| ID | Tên | Mục tiêu | Công cụ chính | Cơ sở định danh |
|----|-----|---------|--------------|----------------|
| TA-01 | **RedTail** | Cryptominer | Go ELF, UPX packed | YARA + binary (c3pool killer) |
| TA-02 | MikroTik Recon | Router fingerprint | SSH-2.0-Go | TTP đặc trưng (`/ip cloud print`) |
| TA-03 | Go-Botnet sshd | sshd backdoor | Go ELF | YARA + PAM module |
| TA-04 | Vietnamese Recon | Recon mở rộng | Go SSH | HASSH + IP ASN Vietnam |
| TA-05 | RedTail Korea | Botnet spread | Go ELF | YARA + infra link TA-01 |
| TA-06 | **DutchGo Stealth** | Internet-wide recon | Go SSH | HASSH 68/68 ngày + 0 command |
| TA-07 | Lithuania Proxy | SSH proxy harvest | SSH-2.0-Go | 0 cmd + DIRECT-TCPIP event |
| TA-08 | **Krane IoT Botnet** | DDoS + PAM | Go ELF multi-arch | YARA Go_PAM_Backdoor |
| TA-09 | Robben IoT Dropper | IoT DDoS | Shell + 9-arch ELF | Script pattern `kla.sh` |
| TA-10 | **"Beary" DDoS** | DDoS-for-hire | Go ELF 8 methods | Binary: `c2c/methods` package |

---

## 3. Nhóm Chưa Định Danh — Phân Loại

### 3.1 Generic Brute Force (~1,800 IP)
- Dùng Mirai, Hydra, Medusa có sẵn
- Không đủ đặc điểm riêng để tạo TA
- Credential: `root/admin/123456` — wordlist phổ biến
- **Tại sao không tạo TA?** Giống nhau về tool, khác nhau về operator

### 3.2 Credential Scanner (~50 IP)
- Pattern: Login OK + 0 commands + nhiều SSH client strings
- Ví dụ: `185.246.128.133` — 449 sessions, 55 client strings, 437 OK, 0 cmd
- **Cơ sở nhận biết:** HASSH cố định dù client string thay đổi
- Chưa đủ để tạo TA riêng — hành vi giống PATTERN-10

### 3.3 Unknown Single-Event (~20 IP)
- 1–2 lần xuất hiện, hành vi bất thường nhưng không lặp lại
- Cần monitor thêm trước khi kết luận

---

## 4. Sáu Cơ Sở Định Danh (6 Attribution Criteria)

### Cơ sở 1: HASSH Fingerprint
**HASSH = hash của KEX algorithm list trong SSH handshake**

```
SSH kết nối:
  Client gửi: "kex_algorithms = curve25519-sha256,ecdh-sha2-nistp256,..."
  HASSH = MD5(kex_algos + enc_algos + mac_algos + comp_algos)
  
  ≠ Client version string (có thể giả mạo)
  ✓ Khó giả vì phải thay đổi SSH library thật
```

**Ví dụ thực tế:**
- TA-10 "Beary": HASSH `16443846...` → liên kết 20 IP thành 1 botnet
- 185.246.128.133: HASSH `57e4cc8e...` → cố định dù dùng 55 client strings khác nhau

**Dùng cho module:** M7 (K-Means clustering theo HASSH)

---

### Cơ sở 2: YARA / Binary Analysis
**Chữ ký malware = đặc điểm không đổi dù file được sửa nhẹ**

```
YARA rule: Go_PAM_Backdoor_eba3282b_v2_2
→ Bắt được 3 variant khác nhau (SHA256 khác nhau)
→ Vì rule nhắm vào LOGIC, không phải byte-for-byte
```

**Ví dụ thực tế (hôm nay):**
```
6453246f...  ←┐
6aa5d769...  ←┤ Cùng rule, SHA256 khác = variant của cùng family
01baaef0...  ←┘
```

**Dùng cho module:** M2 (Threat Intel), M5 (Decision Tree features)

---

### Cơ sở 3: TTP — Chuỗi Hành Vi
**Tactics, Techniques, Procedures = "chữ ký hành vi"**

```
TA-01 RedTail (đặc trưng):
  cd /tmp → wget redtail → chmod +x → ./redtail → systemctl stop c3pool_miner

TA-10 Beary (đặc trưng):
  ulimit -n 1020000 → wget+curl fallback → modzmodz chpasswd → useradd admin1

TA-06 DutchGo (đặc trưng):
  login → NGAY LẬP TỨC disconnect → không có command nào
```

**Nguyên tắc:** TTP thay đổi chậm hơn IP và tool — đây là lớp attribution bền nhất

**Dùng cho module:** M5 (features: command_count, has_persistence, uses_wget)

---

### Cơ sở 4: Infrastructure Clustering
**Nhóm IP dùng cùng hạ tầng = cùng operator**

```
TA-10 Beary cluster:
  157.66.144.16   (Viettel VN — 2,084 sessions)  ┐
  35.233.220.227  (GCP Oregon — 14 sessions)      ├── Cùng HASSH
  103.61.122.229  (13,748 sessions)               ┘
  → 20 IP tổng, cùng botnet operator
  
TA-01 RedTail cluster:
  213.209.159.158 (DE) + 130.12.180.51 (US)
  → Cùng payload host, cùng chiến dịch
```

**Dùng cho module:** M7 (Graph clustering), M3 (Isolation Forest theo IP cluster)

---

### Cơ sở 5: Build Artifacts (Binary Developer Fingerprint)
**Dấu tay developer trong file binary — chỉ có khi phân tích binary**

```
TA-10 Beary:
  strings meow_x86_64 → "C:/Users/beary/go/pkg/mod/"
  → Developer tên "beary", build trên Windows, cross-compile Linux

TA-08 Krane:
  GitHub module path trong binary → linked to public Go repo
```

**Độ tin cậy:** Cao nhất trong các cơ sở — developer thường không ý thức được điều này

**Dùng cho module:** M5 (feature: developer_os = Windows → targeted cross-platform)

---

### Cơ sở 6: Timing Pattern
**Lịch hoạt động phản ánh loại operator**

```
TA-06 DutchGo:   24/7 đều đặn, 68 ngày liên tiếp    → Infrastructure server
185.246.128.133: 3 ngày burst, nghỉ 4 tuần, lặp lại → Campaign scanner
TA-09 Robben:    1 event duy nhất                    → Test/probe
```

**Phân biệt người thật vs bot:**
- Bot: flat distribution 24 giờ, không có "buổi trưa nghỉ"
- Người thật: giờ hoạt động theo múi giờ, nghỉ ban đêm

**Dùng cho module:** M7 (UBA — User Behavior Analytics), M3 (Isolation Forest timing features)

---

## 5. Ví Dụ Phân Tích Hoàn Chỉnh: 185.246.128.133

**Tin nhắn Telegram nhận lúc 06:50:**
```
🟠 HIGH INCIDENT — 185.246.128.133
69 sess | 0 cmd | ✅67 ❌0
SSH-2.0-PuTTY_Release_0.58, SSH-2.0-OpenSSH_3.9p1, SSH-2.0-paramiko_1.7.7.1 ...
```

**Phân tích 5 tín hiệu:**

| Tín hiệu | Giá trị quan sát | Kết luận |
|----------|-----------------|---------|
| Client strings | 55 loại khác nhau | Giả mạo client để tránh detection |
| HASSH | `57e4cc8e...` — cố định | 1 tool duy nhất phía sau |
| Command count | 0 / 437 sessions | Chỉ validate credential, không exploit |
| Hourly rate | 17–22/giờ đều đặn | Automated, không phải người |
| Temporal pattern | 3-day burst × 3 đợt | Campaign định kỳ |

**Kết luận:** Credential Validation Scanner — PATTERN-10, không tạo TA mới

---

## 6. Bài Học

> **Threat Intelligence không phải là biết tên hacker.**
> Threat Intelligence là **nhóm hành vi giống nhau lại** để:
> - Phát hiện sớm khi IP mới xuất hiện với cùng HASSH
> - Ưu tiên phản ứng (TA-08 nguy hiểm hơn generic brute force)
> - Dự đoán bước tiếp theo (biết TTP → biết sẽ làm gì sau khi vào)

**Attribution không cần 100% chắc chắn** — "với xác suất cao là cùng operator" đã đủ để phản ứng.

---

*Nguồn dữ liệu: Cowrie honeypot, DietPi 192.168.1.88, YARA v2.2, Ghidra 12.1*
*File liên quan: `docs/ATTACK-LOG.md`, `pm/results/MALWARE_MEOW_DDOS_BOTNET_20260602.md`*

---

## 7. ML Lab Results — K-Means + Isolation Forest trên Dữ Liệu Thực

*Script: `labs/attacker_clustering_lab.py` | Output: `labs/attacker_clusters.png`*
*Dataset: 4,492 IPs (≥3 sessions), 8 features, 72 ngày Cowrie data*

### 7.1 K-Means kết quả (k=7, Silhouette=0.388)

| Cluster | Tên tự động | Số IP | Avg Sessions | Avg Cmds | Avg Clients | Known TAs |
|---------|------------|-------|-------------|---------|------------|---------|
| C0 | Low-volume generic | 1,984 | 8 | 0.1 | 0.9 | TA-10 MEOW dropper |
| C1 | Low-volume generic | 915 | 154 | 84.7 | 1.1 | — |
| **C2** | **Multi-client scanner** | **17** | **56** | **0** | **13.6** | **185.246.128.133** ✅ |
| C3 | Low-volume generic | 91 | 8 | 30.3 | 1.1 | — |
| C4 | Low-volume generic | 581 | 132 | 64.3 | 1.4 | TA-10 Beary (scanner+deployer) |
| C5 | Low-volume generic | 882 | 4 | 2.3 | 1.1 | — |
| **C6** | **Deployer (cmds cao)** | **22** | **1,689** | **129.9** | **1.3** | **TA-01 RedTail, TA-06 DutchGo** ✅ |

**Quan sát:**
- C2 (17 IP) = Multi-client scanner cluster → `185.246.128.133` rơi đúng vào đây mà không cần nhãn
- C6 (22 IP) = Deployer cluster → TA-01 RedTail và TA-06 DutchGo tự động vào cùng nhóm
- K-Means **không biết** về YARA hay HASSH — chỉ dựa vào 8 features hành vi

### 7.2 Isolation Forest kết quả (contamination=5%, 4,492 IPs)

**Top anomalies — IF tự phát hiện không cần nhãn:**

| Rank | IP | Sessions | Cmds | Clients | Nhận dạng thực | IF Score |
|------|-----|---------|-----|--------|--------------|---------|
| #1 | 185.246.128.133 | 518 | 0 | **55** | Cred Scanner ✅ | -0.745 |
| #2 | 160.191.88.19 | 1,076 | 1,062 | 1 | Unknown (high cmd) | -0.731 |
| #3 | 80.66.66.10 | 4,351 | 0 | 1 | Unknown (high vol) | -0.725 |
| #8 | 157.66.144.16 | 18,902 | **17,822** | 1 | TA-10 Beary deployer ✅ | -0.693 |
| #9 | 130.12.181.254 | 20,342 | 992 | 1 | TA-09 GoRecon ✅ | -0.694 |

**Kết quả quan trọng: 5/6 known TAs bị flag là anomaly** — model tự nhận ra mà không cần ground truth.

> 💡 **Insight cho M3:** Isolation Forest đặc biệt hiệu quả khi anomaly có combo bất thường.
> `185.246.128.133` bất thường vì: 55 clients + 0 commands (không IP nào khác có combo này).
> `157.66.144.16` bất thường vì: 17,822 commands (cực kỳ cao so với 99% còn lại).

### 7.3 Feature Importance (PCA PC1)

| Rank | Feature | PC1 Loading | Ý nghĩa |
|------|---------|------------|---------|
| 1 | `log_cmds` | 0.626 | Số lệnh thực thi — phân biệt deployer vs scanner |
| 2 | `log_sessions` | 0.454 | Khối lượng tấn công |
| 3 | `login_ok_rate` | 0.441 | Tỷ lệ đăng nhập thành công |
| 4 | `active_days` | — | Thời gian hoạt động |
| 5 | `unique_clients` | — | Số client strings → cred scanner |

### 7.4 Phát Hiện Mới Từ Dữ Liệu

**103.61.122.229 — Temporal Pattern (không hoạt động 24h qua):**
```
2026-04-01  11,131  ████████████████████████
2026-04-02  22,315  ████████████████████████████████████████ ← đỉnh
2026-04-03  11,985  █████████████████████████
            [nghỉ 7 tuần]
2026-05-26   1,565  ███
2026-05-27   7,907  ████████████████
2026-05-28  10,770  █████████████████████
2026-05-29   3,087  ██████
            [offline 4 ngày đến nay]
```
Pattern: burst 3–4 ngày → nghỉ vài tuần → burst lại. Cùng pattern với 185.246.128.133.

**Botnet cluster TA-10 lớn hơn dự kiến:**
- HASSH `16443846...` liên kết **130+ IP** (không phải 20 IP như ban đầu)
- Hoạt động từ **2026-03-24** (trước khi MEOW binary bị phát hiện)
- Phase 1 (scan) → Phase 2 (deploy MEOW) là cùng 1 chiến dịch liên tục

### 7.5 Thông điệp

```
Trước ML:  Analyst đọc từng IP, so sánh thủ công → chậm, bỏ sót nhiều
Sau ML:    K-Means tự nhóm 4,492 IP thành 7 clusters trong < 5 giây
           Isolation Forest tự flag top 5% bất thường mà không cần nhãn

Điều quan trọng: Model KHÔNG thay thế analyst.
Model làm công việc lọc 4,492 → 17 (C2) hoặc 22 (C6).
Analyst phân tích 17–22 IP thay vì 4,492 → nhanh hơn 200x.
```

**Lab script:** `labs/attacker_clustering_lab.py` — chạy được trên dataset này luôn.
