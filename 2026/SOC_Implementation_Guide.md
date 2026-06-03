# Hướng Dẫn Triển Khai SOC Từ Đầu

---

"Khảo sát trước, biết mình có gì và yếu chỗ nào — rồi mới xây. Bắt đầu nhỏ, làm chắc cái cốt lõi, mở rộng dần."

---

## Phần 1 — SOC Là Gì? Tại Sao Cần?

**SOC** = **S**ecurity **O**perations **C**enter — **Trung tâm Vận hành An ninh**

Hình dung dễ nhất: SOC giống một **phòng bảo vệ** cho hệ thống máy tính:

| Phòng bảo vệ tòa nhà | SOC |
|----------------------|-----|
| Camera khắp nơi | Thu thập log (nhật ký hoạt động) từ mọi thiết bị |
| Màn hình tổng hợp tất cả camera | SIEM — gom hết log về một chỗ để xem chung |
| Bảo vệ nhìn màn hình | Tier 1 Analyst — người ngồi xem cảnh báo |
| Sổ tay "thấy X thì làm Y" | Playbook — quy trình xử lý sự cố |
| Trợ lý tự khoanh camera có chuyển động bất thường | AI/ML — lọc nhiễu, chỉ đánh dấu cảnh báo đáng xem |

### Ba trụ cột của mọi SOC

```
        PEOPLE              PROCESS            TECHNOLOGY
    (Con người)            (Quy trình)          (Công nghệ)
   ─────────────        ──────────────        ─────────────
   Tier 1 Analyst       IR Playbook           SIEM
   Tier 2 Analyst       NIST IR Framework     EDR
   Tier 3 / Threat      Escalation Rules      IDS
   Hunter               On-call Schedule      Threat Intel
   SOC Manager          Tuning Reviews        SOAR
   Security Engineer    Threat Hunting Plan   Dashboards
```

> **Ý tưởng cốt lõi:** Xây SOC không phải là đi mua công cụ, mà là một bài toán về **thứ tự (sequencing)** — làm đúng chiến lược trước, rồi mới đến con người, quy trình, công nghệ, và xây dần theo kiểu lặp (iterative).

---

## Phần 2 — Bảng Thuật Ngữ Cần Biết

Trước khi đọc tiếp, hãy hiểu các viết tắt sau:

| Viết tắt | Viết đầy đủ | Nghĩa tiếng Việt đơn giản |
|----------|-------------|---------------------------|
| **Log** | *(không viết tắt)* | Nhật ký — mọi việc máy làm đều được ghi lại (ai đăng nhập, lúc nào, từ đâu) |
| **SIEM** | Security Information and Event Management | Màn hình tổng hợp — gom hết nhật ký từ mọi máy về một chỗ để xem chung |
| **EDR** | Endpoint Detection and Response | Camera gắn trên từng máy (laptop, server) — theo dõi máy đó có bị làm điều bất thường không |
| **IDS** | Intrusion Detection System | Camera ở cổng mạng — phát hiện tấn công qua đường mạng |
| **MSSP** | Managed Security Service Provider | Thuê công ty ngoài làm bảo vệ giùm |
| **WAF** | Web Application Firewall | Tường lửa cho ứng dụng web — lọc yêu cầu độc hại trước khi tới máy chủ |
| **NGFW** | Next-Generation Firewall | Tường lửa thế hệ mới — chốt chặn chính, chia vùng và lọc lưu lượng |
| **SOAR** | Security Orchestration, Automation and Response | Tự động hóa các bước phản ứng lặp đi lặp lại |
| **ZTNA** | Zero Trust Network Access | Truy cập mạng không tin cậy mặc định — mỗi lần đều phải xác thực lại |
| **MTTD** | Mean Time To Detect | Thời gian trung bình để *phát hiện* sự cố (càng nhỏ càng tốt) |
| **MTTA** | Mean Time To Acknowledge | Thời gian trung bình để *tiếp nhận* cảnh báo |
| **MTTR** | Mean Time To Respond | Thời gian trung bình để *xử lý xong* sự cố (càng nhỏ càng tốt) |
| **KPI** | Key Performance Indicator | Chỉ số hiệu suất chính — dùng để đánh giá SOC đang làm tốt cỡ nào |
| **DMZ** | Demilitarized Zone | Vùng đệm mạng — chứa các dịch vụ công khai (web server) để tách khỏi mạng nội bộ |
| **VLAN** | Virtual Local Area Network | Mạng nội bộ ảo — chia mạng vật lý thành nhiều vùng tách biệt |
| **TAP** | Test Access Point | Thiết bị "soi" lưu lượng mạng, đặt giữa switch và cảm biến IDS |
| **EPS** | Events Per Second | Số sự kiện log mỗi giây — chỉ số dùng để ước lượng kích cỡ SIEM cần thiết |
| **NTP** | Network Time Protocol | Giao thức đồng bộ thời gian — đảm bảo đồng hồ trên mọi máy khớp nhau |

---

## Phần 3 — 7 Bước Xây SOC (Phiên Bản Đơn Giản)

Dành cho người bắt đầu — làm theo đúng thứ tự này:

### Bước 0 — Khảo sát hiện trạng mạng *(làm đầu tiên)*

Trả lời 3 câu hỏi:

1. **Đang có những thiết bị CNTT gì?** Liệt kê hết: máy chủ (server), máy trạm (laptop/PC), router, switch, firewall, thiết bị mạng, dịch vụ đám mây (cloud), camera, IoT... Vẽ một sơ đồ mạng đơn giản.
2. **Mức độ an toàn hiện tại đến đâu?** Kiểm tra: đã có tường lửa chưa? Có phần mềm diệt virus chưa? Máy có ghi nhật ký (log) không? Mật khẩu có mạnh không?
3. **Có cần đầu tư thiết bị mới không?** So sánh "cái đang có" với "cái cần có". Tận dụng lại được thì giữ, thiếu mới mua.

> *Kết quả của Bước 0:* Một bức tranh rõ ràng — **mình có gì, yếu chỗ nào, cần thêm gì**.

---

### Bước 1 — Biết tài sản & dữ liệu quan trọng nhất

Trong số thiết bị đã kiểm kê ở Bước 0, chọn ra: **cái nào mà mất là chết?** (dữ liệu khách hàng, hệ thống thanh toán, email nội bộ...). Đây là những thứ cần bảo vệ trước nhất.

*(Phân biệt: Bước 0 là "có cái gì trong mạng"; Bước 1 là "trong số đó, cái nào quý nhất". Khảo sát trước, chọn ưu tiên sau.)*

---

### Bước 2 — Bật ghi nhật ký (log) khắp nơi

Cho các máy ghi lại hoạt động — đây là bước **"lắp camera"**. Không có log thì không nhìn thấy gì khi có sự cố.

---

### Bước 3 — Gom nhật ký về một chỗ (dựng SIEM)

Để ngồi một chỗ xem được tất cả. Công cụ gợi ý: **Wazuh** (miễn phí, mã nguồn mở).

---

### Bước 4 — Lắp giám sát cho máy và mạng (EDR + IDS)

- **EDR** (Wazuh agent): cài trên từng máy, thấy được bất thường ở từng thiết bị.
- **IDS** (Suricata/Zeek): đặt tại đường mạng, phát hiện và phân tích lưu lượng đáng ngờ.

---

### Bước 5 — Viết sổ tay xử lý sự cố (Playbook)

Quy định rõ: thấy dấu hiệu lạ → ai làm gì → báo cho ai. Tham chiếu khung **NIST SP 800-61** gồm 4 pha:

```
Chuẩn bị → Phát hiện & Phân tích → Khống chế / Dọn sạch / Khôi phục → Rút kinh nghiệm
(Preparation)  (Detection & Analysis)  (Containment / Eradication / Recovery)  (Post-Incident)
```

> ⚠️ **Pha Chuẩn bị (Preparation) là pha quan trọng nhất** — bao gồm thiết lập playbook, đào tạo đội ngũ, kiểm tra công cụ trước khi sự cố xảy ra. Không chuẩn bị thì khi có chuyện sẽ loạn.

---

### Bước 6 — Canh, đo, và cải tiến

Có người ngồi xem cảnh báo, đo **MTTD/MTTR**, cái nào báo nhầm nhiều thì chỉnh lại cho đỡ nhiễu.

---

### ✅ Checklist 7 Bước (in ra tự tick)

- [ ] Đã liệt kê toàn bộ thiết bị CNTT đang có
- [ ] Đã vẽ sơ đồ mạng đơn giản
- [ ] Đã đánh giá mức an toàn hiện tại (firewall, antivirus, log, mật khẩu...)
- [ ] Đã xác định thiếu gì, cần đầu tư mua mới gì
- [ ] Đã chọn ra tài sản/dữ liệu quan trọng nhất cần bảo vệ
- [ ] Đã bật ghi nhật ký (log) trên các máy
- [ ] Đã gom nhật ký về một chỗ (SIEM)
- [ ] Đã lắp giám sát cho từng máy (EDR)
- [ ] Đã lắp giám sát cho mạng (IDS)
- [ ] Đã viết sổ tay xử lý khi có sự cố (4 pha NIST)
- [ ] Đã phân công ai canh, ai xử lý
- [ ] Đã chỉnh bớt cảnh báo báo nhầm
- [ ] Đã bắt đầu đo thời gian phát hiện (MTTD) và xử lý (MTTR)

---

## Phần 4 — Vòng Đời 6 Giai Đoạn (Phiên Bản Production)

Đây là quy trình đầy đủ cho tổ chức muốn xây SOC theo chuẩn production.

### Giai đoạn 1 — Xác định yêu cầu (Requirements)

Trả lời trước khi làm bất cứ gì:
- **Mục tiêu:** SOC để làm gì? (tuân thủ luật, giám sát liên tục, phản ứng nhanh hơn)
- **Phạm vi:** bảo vệ hệ thống nào, ở mức nào
- **Kỳ vọng đầu ra:** ví dụ "phát hiện sự cố nghiêm trọng trong 30 phút", "trực giờ hành chính + cảnh báo ngoài giờ"
- **Ngân sách & nhân lực:** có bao nhiêu tiền, mấy người

> *Kết quả:* Một bản yêu cầu rõ ràng để mọi quyết định sau bám theo.

---

### Giai đoạn 2 — Khảo sát hiện trạng (Assessment)

- Kiểm kê toàn bộ thiết bị CNTT (máy chủ, máy trạm, router, switch, firewall, cloud, IoT)
- Vẽ **sơ đồ mạng** (vật lý + luận lý) để thấy dữ liệu chạy đường nào
- Đánh giá mức an toàn hiện tại (gap analysis): đã có firewall/antivirus/log chưa, hở chỗ nào
- Chọn ra tài sản & dữ liệu **quan trọng nhất** (mất là chết)

> *Kết quả:* Bức tranh "đang có gì – yếu chỗ nào – cần thêm gì".

---

### Giai đoạn 3 — Thiết kế & Kế hoạch nâng cấp

So sánh "cái cần có" (Giai đoạn 1) với "cái đang có" (Giai đoạn 2), chỉ mua **đúng thứ thực sự thiếu**.

**Thiết bị tối thiểu cần đầu tư:**

| Thiết bị | Mục đích | Lựa chọn tiết kiệm |
|----------|----------|--------------------|
| 1 Firewall thế hệ mới (NGFW) | Chốt chặn chính, chia vùng, lọc lưu lượng | pfSense / OPNsense trên phần cứng tốt |
| 1–2 Switch quản lý được (managed switch, hỗ trợ VLAN) | Chia mạng thành nhiều vùng | Switch tầm trung có VLAN support |
| 1 Máy chủ cho SIEM | Nhiều RAM, nhiều đĩa SSD | Xem Phần 8 — cần ước lượng EPS trước khi chọn cấu hình |
| 1 Network TAP hoặc cổng SPAN | "Soi" lưu lượng cho cảm biến IDS | Cổng SPAN trên switch sẵn có |
| UPS + ổ cứng backup | Giữ SOC luôn sống và có dữ liệu dự phòng | UPS tầm trung |

**Phân chia lại mạng (Network Segmentation) — chia thành các VLAN:**

```
┌──────────────────────────────────────────────────────────────┐
│                          Internet                             │
└──────────────────────────┬───────────────────────────────────┘
                           │
                     [ NGFW / Firewall ]
         ┌──────────┬──────┴──────┬──────────┬─────────────────┐
         │          │             │          │                  │
      [DMZ]    [Vùng Người   [Vùng Máy  [Vùng Quản       [Vùng SOC /
   Dịch vụ    dùng nhân     chủ nội    trị Admin]         Giám sát]
   công khai] viên]          bộ]       (interface          (interface
                                        riêng)              riêng)
```

> ⚠️ **Lỗi kiến trúc thường gặp:** Vùng Quản trị và Vùng SOC phải kết nối **trực tiếp vào firewall** qua interface riêng — **không** được đặt sau DMZ. DMZ là vùng kém tin cậy nhất (phơi ra Internet); nếu DMZ bị chiếm mà Admin/SOC nằm sau nó, kẻ tấn công có đường thẳng tới trái tim của hệ thống giám sát.

- **Vùng người dùng:** máy nhân viên
- **Vùng máy chủ:** server nội bộ
- **DMZ:** dịch vụ công khai (web server) — ít tin cậy nhất
- **Vùng quản trị (Management):** chỉ admin vào, tách riêng port SSH
- **Vùng SOC/giám sát:** đặt SIEM và cảm biến — tách biệt, tin cậy nhất trong hạ tầng

> *Chia vùng giúp:* một máy bị nhiễm không lây sang cả mạng, và đặt "camera" (IDS) đúng chỗ.

---

### Giai đoạn 4 — Triển khai dần từng bước (Phased Deployment)

Không ôm hết một lúc. Mỗi bước phải "chạy ổn" rồi mới sang bước sau:

```
Bước 1 → Bật log + cài agent lên máy quan trọng → có log tập trung
Bước 2 → Dựng SIEM (Wazuh)
Bước 3 → Thêm cảm biến mạng (Suricata/Zeek)
Bước 4 → Viết luật phát hiện (Sigma) + ánh xạ MITRE ATT&CK
Bước 5 → Thêm quản lý ca (TheHive) + làm giàu (Cortex/MISP)
Bước 6 → Cuối cùng mới tự động hóa (SOAR — Shuffle)
```

---

### Giai đoạn 5 — Vận hành, Bảo trì & KPI

**Workflow vận hành chuẩn (mỗi ca trực):**

```
Cảnh báo → Triage (phân loại) → Điều tra → Phản ứng
         → Khôi phục → Đóng ca + Ghi bài học
```

Kèm theo: phân ca trực, quy tắc leo thang (escalation), trực ngoài giờ (on-call).

**Bộ Metrics & KPI để đánh giá SOC:**

| KPI | Ý nghĩa | Mục tiêu |
|-----|---------|---------|
| **MTTD** | Thời gian trung bình để *phát hiện* sự cố | Càng nhỏ càng tốt |
| **MTTA** | Thời gian trung bình để *tiếp nhận* cảnh báo | Càng nhỏ càng tốt |
| **MTTR** | Thời gian trung bình để *xử lý xong* sự cố | Càng nhỏ càng tốt |
| **Tỉ lệ false positive** | Tỉ lệ cảnh báo báo nhầm | Càng giảm càng tốt |
| **Độ phủ MITRE ATT&CK** | Đang phát hiện được bao nhiêu % kỹ thuật tấn công | Càng tăng càng tốt |
| **% nguồn log được thu thập** | Đã "lắp camera" đủ chưa | Mục tiêu 100% nguồn quan trọng |
| **Uptime hệ thống SOC** | SOC có đang sống không | ≥ 99% |
| **Số ca xử lý / số ca tồn đọng** | Nhịp độ xử lý hàng ngày | Tồn đọng → 0 |

**Bảo trì định kỳ:**
- Vá lỗi phần mềm (patch management)
- Backup và kiểm tra khôi phục
- Quản lý dung lượng log: ví dụ 90 ngày "nóng" (online) → nén/lưu trữ "lạnh" (offline/archive)
- Cập nhật luật phát hiện (rules) & threat intelligence định kỳ

---

### Giai đoạn 6 — Review, Tinh chỉnh & Lặp lại

- Định kỳ (hàng tuần/tháng) họp xem KPI: MTTD/MTTR có giảm không? False positive còn cao không?
- Tinh chỉnh luật, bổ sung phát hiện cho chỗ còn hở (theo MITRE)
- Làm **threat hunting** & **purple team**
- Phát hiện thiếu sót → quay lại điều chỉnh thiết kế hoặc quy trình → chạy lại vòng

> **Điểm mấu chốt:** SOC **không bao giờ "xong"** — nó là một vòng lặp sống, đo bằng số (KPI) và cải tiến liên tục.

**Tóm tắt vòng lặp (1 câu):**

> *"Hỏi rõ yêu cầu → khảo sát biết mình có gì → mua đúng thứ cần & chia lại mạng → triển khai từng bước → đo bằng KPI và vận hành theo workflow → review rồi lặp lại để tốt dần."*

---

## Phần 5 — Bộ Công Cụ Mã Nguồn Mở

**Triết lý:** Mã nguồn mở thay cho phần mềm bản quyền đắt đỏ. Chi phí thật sự nằm ở **công sức vận hành nội bộ**, không phải ở thiết bị.

### Bộ công cụ chia theo lớp chức năng

**Lớp 1 — Thu thập (Collection)**

| Công cụ | Chức năng | Ghi chú |
|---------|-----------|---------|
| **Wazuh agent** | Cài trên từng máy (Windows/Linux) — làm EDR, gửi log về SIEM | Miễn phí |
| **Sysmon** | Ghi chi tiết hoạt động hệ thống Windows | Miễn phí (Microsoft) |
| **Suricata** | IDS dựa trên chữ ký — phát hiện lưu lượng khớp với mẫu tấn công đã biết | Miễn phí |
| **Zeek** | Khung phân tích & giám sát lưu lượng mạng — bổ sung cho Suricata ở tầng giao thức sâu hơn | Miễn phí |

> 📌 **Phân biệt Suricata và Zeek:** Suricata là IDS thuần túy — so khớp lưu lượng với chữ ký (signature-based). Zeek không phải IDS mà là công cụ *phân tích giao thức mạng* — nó ghi lại metadata chi tiết (ai kết nối với ai, dùng giao thức gì, bao nhiêu dữ liệu) để điều tra sau sự cố. Hai công cụ bổ sung cho nhau, không thay thế nhau.

**Lớp 2 — Lưu trữ & Phân tích (SIEM)**

| Công cụ | Chức năng | Ghi chú |
|---------|-----------|---------|
| **Wazuh** (lõi OpenSearch) | SIEM + EDR all-in-one — trái tim của SOC mã nguồn mở | Phổ biến nhất |
| **Security Onion** | Đóng gói sẵn Suricata + Zeek + Elastic + công cụ điều tra | Lựa chọn thay thế |

**Lớp 3 — Phát hiện (Detection Engineering)**

| Công cụ | Chức năng |
|---------|-----------|
| **Sigma rules** | Luật phát hiện dạng chuẩn, dịch ra cho Wazuh/OpenSearch |
| **MITRE ATT&CK** | Bản đồ kỹ thuật tấn công — ánh xạ luật phát hiện vào đây để biết đang phủ được những gì |

**Lớp 4 — Xử lý & Tự động hóa (Case Management + SOAR)**

| Công cụ | Chức năng |
|---------|-----------|
| **TheHive** | Quản lý vụ việc — mỗi cảnh báo thành một "ca" để điều tra, ghi chép |
| **Cortex** | Chạy phân tích tự động (tra IP, file hash...) |
| **Shuffle** | SOAR mã nguồn mở — tự động hóa các bước lặp đi lặp lại |

**Lớp 5 — Làm giàu thông tin (Threat Intelligence)**

| Công cụ / Nguồn | Loại |
|-----------------|------|
| **MISP** | Nền tảng chia sẻ threat intel (self-hosted) |
| **OpenCTI** | Threat intel platform mã nguồn mở |
| AbuseIPDB, AlienVault OTX | Nguồn danh sách IP độc hại miễn phí |
| URLhaus, ThreatFox, Feodo Tracker | Nguồn malware/C2 miễn phí |

**Lớp 6 — Hiển thị & Cảnh báo**

| Công cụ | Chức năng |
|---------|-----------|
| **Grafana / Kibana** | Bảng theo dõi trực quan (dashboard) |
| **Telegram / Email / Slack** | Cảnh báo realtime đến analyst |

> ⚠️ **Lưu ý bảo mật cho cảnh báo qua Telegram (hay Slack):** Trong môi trường lab và home lab, Telegram tiện và phù hợp. Tuy nhiên, cảnh báo SOC thường chứa thông tin nhạy cảm (IP nội bộ, tên máy, dấu hiệu tấn công, log xác thực). Gửi dữ liệu này qua dịch vụ của bên thứ ba nằm ngoài tầm kiểm soát là điều nhiều doanh nghiệp không chấp nhận về mặt chính sách. Trong môi trường production thật, cần đánh giá: dữ liệu nào được phép gửi ra ngoài, và thay thế bằng hệ thống nhắn tin nội bộ (self-hosted) nếu chính sách không cho phép.

---

### Kiến trúc luồng dữ liệu

```
Máy đầu cuối          Cảm biến mạng
(Wazuh agent)  +    (Suricata / Zeek)
      │                     │
      └─────────┬───────────┘
                ▼
    Wazuh/OpenSearch (SIEM)
    [Luật Sigma + ánh xạ MITRE ATT&CK]
                │
           Cảnh báo
                │
         TheHive (ca điều tra)
                │
     ┌──────────┴──────────┐
     ▼                     ▼
  Cortex               MISP
  (làm giàu            (threat intel)
  tự động)
     │
     ▼
  Shuffle (SOAR)
  [tự động hóa phản ứng]
     │
     ▼
  Grafana/Kibana + Cảnh báo
  [hiển thị + thông báo]
```

---

### Chi phí thực tế

| Hạng mục | Chi phí |
|----------|---------|
| **Phần mềm (license)** | ~0 đồng (toàn mã nguồn mở) |
| **Thiết bị (CapEx)** | Từ 0 (tái sử dụng) đến vài nghìn USD (1 máy chủ) |
| **Vận hành (OpEx)** | Chủ yếu là **lương nhân sự nội bộ** + điện + có thể chút cloud |

> ⚠️ **"Miễn phí" không có nghĩa là không tốn kém.** Mã nguồn mở miễn phí license, nhưng bạn tự chịu công cài đặt, vá lỗi, nâng cấp, xử lý sự cố. Chi phí thật chuyển sang **thời gian con người**.

---

### Mô hình vận hành nội bộ (đội nhỏ)

- Khởi đầu chỉ cần **2–3 người:** 1 người thiên về hệ thống/engineer (dựng & bảo trì), 1–2 người làm analyst (xem cảnh báo, điều tra)
- Chưa đủ người trực 24/7? → đặt cảnh báo tự động, ưu tiên trực giờ hành chính, các cảnh báo nghiêm trọng thì gọi ngoài giờ
- Quy trình bắt buộc: playbook xử lý sự cố, ánh xạ MITRE, tinh chỉnh giảm cảnh báo nhiễu định kỳ, đo MTTD/MTTR

---

### Lưu ý cần nói thẳng

> ⚠️ **OpenSearch/Elastic ăn đĩa rất nhanh.** Phải lên kế hoạch giữ log bao lâu (ví dụ 90 ngày nóng, sau đó nén/lưu trữ lạnh) kẻo đầy đĩa.

> ⚠️ **Phải có backup & kế hoạch khôi phục** cho chính hệ thống SOC — SOC mà sập thì mù.

> ⚠️ **Đừng nhầm "dựng xong công cụ" với "có SOC".** Công cụ chỉ là 1/3. Không có người canh và quy trình thì đống dashboard chỉ để trưng bày.

---

## Phần 6 — Bảo Mật Lớp Mạng

### Nguyên tắc vàng

> Doanh nghiệp **gần như không bao giờ phơi port thẳng ra Internet**. Họ luôn đặt một lớp trung gian ở giữa.

### Port web (80 = HTTP, 443 = HTTPS) — port phục vụ người dùng

Chuỗi chuẩn:
```
Người dùng → CDN/WAF → Reverse Proxy/Load Balancer → Máy chủ thật
```

| Lớp | Công cụ | Chức năng |
|-----|---------|-----------|
| **CDN / Edge** | Cloudflare | Đứng ở rìa Internet, hứng tải và chặn tấn công. Dùng mô hình reverse proxy và Anycast, chỉ chuyển lưu lượng sạch về máy chủ gốc |
| **WAF** | Cloudflare WAF, ModSecurity | Lọc SQL injection, XSS và các yêu cầu độc hại |
| **Reverse Proxy** | Nginx, HAProxy | Nhận hết yêu cầu từ ngoài, chuyển vào máy chủ thật — máy chủ thật được giấu đi |
| **Load Balancer** | Nginx, HAProxy | Chia đều khách cho nhiều máy chủ, tránh quá tải |

### Port quản trị (22 = SSH) — port cho admin đăng nhập máy chủ

> Port 22 là port **nguy hiểm nhất** — tuyệt đối không mở thẳng ra Internet.

*(Dữ liệu honeypot thực tế cho thấy port 22 bị quét và dò mật khẩu liên tục.)*

| Phương pháp | Công cụ | Cơ chế |
|-------------|---------|--------|
| **VPN** | WireGuard, OpenVPN | Admin phải "chui vào đường hầm riêng" mới thấy được máy chủ. Bên ngoài không nhìn thấy port 22 |
| **Bastion Host / Jump Host** | SSH ProxyJump | Chỉ 1 máy duy nhất được phép vào. Admin phải qua "chốt gác" đó rồi mới nhảy tiếp vào máy bên trong |
| **ZTNA** | Cloudflare Tunnel/Access, Tailscale, Teleport | Mô hình hiện đại nhất: không tin ai mặc định. Máy chủ **không mở port nào ra Internet** — nó tự "gọi ra ngoài" tạo đường hầm, kẻ tấn công không có cổng để quét |

Luôn kèm theo, dù dùng phương pháp nào:
- Đăng nhập bằng **khóa SSH** thay vì mật khẩu
- **MFA** (Multi-Factor Authentication — xác thực nhiều lớp)
- **Danh sách IP cho phép** (chỉ vài IP văn phòng được kết nối)

**Câu chốt dễ nhớ:**
> *"Port web thì đặt 'lễ tân' (Reverse Proxy + WAF + CDN) đứng chắn phía trước. Port SSH thì không bao giờ mở thẳng — phải đi qua VPN, Bastion, hoặc Zero Trust Tunnel."*

---

## Phần 7 — AI Trong SOC (Kết Nối Khóa CSAI)

AI/ML **không thay thế SOC** — mà gắn vào các **Giai đoạn 4–6** để hỗ trợ con người:

| Ứng dụng AI/ML | Vị trí trong SOC | Module CSAI tương ứng |
|---------------|-----------------|----------------------|
| **Anomaly detection** (phát hiện bất thường) | Lớp Detection Engineering | Module 3 — Isolation Forest |
| **Alert prioritization** (ưu tiên cảnh báo) | Triage — giảm quá tải Tier 1 | Module 4, 5 — Classifier |
| **Threat intel enrichment** (làm giàu threat intel) | Lớp Threat Intelligence | Module 5, 6 — Feature Engineering |
| **User Behavior Analytics — UBA** (phân tích hành vi người dùng) | Lớp Detection nâng cao | Module 7 — K-Means Clustering |
| **Malware detection** (phát hiện mã độc) | Lớp EDR | Module 5 — Malware Classifier |

**Triết lý "thử thủ công thất bại trước, rồi AI cứu":**

1. Cho học viên thử correlate log thủ công → ngợp vì quá nhiều
2. Thấy ML lọc nhiễu, phân loại, và đánh dấu bất thường giúp thế nào
3. Hiểu AI không tự làm thay người — AI giúp **giảm tải và ưu tiên**, để analyst tập trung vào những cảnh báo thực sự đáng điều tra

---

## Phần 8 — Những Yếu Tố Không Được Bỏ Qua Khi Xây SOC Production

Đây là những yếu tố một SOC production thật bắt buộc phải có, nhưng thường bị bỏ qua khi lần đầu triển khai.

---

### 8.1 Ước Lượng Dung Lượng Log Trước Khi Chọn Phần Cứng (Sizing theo EPS)

**Vấn đề:** "Mua máy 64GB RAM" là câu trả lời sai nếu chưa biết lượng log của hệ thống. Mạng 20 máy và mạng 2.000 máy cần phần cứng khác nhau hàng chục lần — con số RAM/đĩa vô nghĩa nếu không gắn với lượng log.

**Cách ước lượng đơn giản theo EPS:**

```
EPS (Events Per Second) = số sự kiện log mỗi giây toàn hệ thống

Ước lượng sơ bộ:
  - Máy chủ Linux/Windows: 50–200 EPS/máy (tùy cấu hình log)
  - Firewall/Router lớn: 500–2.000 EPS
  - Web server bận: 1.000+ EPS

Quy đổi sang dung lượng:
  - 1 EPS ≈ 1–5 KB/giây (tùy loại log)
  - Ví dụ: 500 EPS × 2 KB = 1 MB/giây = ~86 GB/ngày
  - Giữ 90 ngày nóng → cần ~7.7 TB chỉ riêng storage
```

**Cách tiếp cận thực tế:**

| Bước | Hành động |
|------|-----------|
| 1 | Bật log thử trên 1–2 máy đại diện trong 24 giờ |
| 2 | Đo dung lượng log thực tế (GB/ngày/máy) |
| 3 | Nhân với số máy, cộng với log firewall/IDS |
| 4 | Nhân hệ số dự phòng × 1.5–2 (log có thể tăng đột biến khi bị tấn công) |
| 5 | Từ đó suy ra RAM, CPU, và dung lượng đĩa cần thiết |

> 💡 **Quy tắc ngón tay cái cho Wazuh/OpenSearch:** Cần khoảng 1 GB RAM per 10 EPS duy trì (tùy version và cấu hình). Với mạng nhỏ (~500 EPS), 16–32 GB RAM là đủ khởi đầu. Với mạng lớn hơn thì phải đo thực tế.

---

### 8.2 Đồng Bộ Thời Gian (NTP) — Bắt Buộc Cho Mọi Nguồn Log

**Vấn đề:** Nếu đồng hồ các máy lệch nhau — dù chỉ vài phút — việc ghép log từ nhiều nguồn để dựng lại dòng thời gian tấn công sẽ sai hoàn toàn. Đây là cái bẫy kinh điển và dễ bị bỏ qua.

**Ví dụ:** Hacker xâm nhập lúc 14:00:05. Máy firewall ghi đúng giờ. Máy endpoint lệch 8 phút → log ghi 14:08. Analyst nhìn log thấy "firewall cảnh báo TRƯỚC khi endpoint bị xâm nhập" — dòng thời gian vô nghĩa.

**Giải pháp:**

- Cấu hình **NTP** (Network Time Protocol) cho **toàn bộ nguồn log** — máy chủ, máy trạm, firewall, switch, cảm biến IDS.
- Đặt 1 NTP server nội bộ, đồng bộ ra NTP pool bên ngoài (pool.ntp.org), các máy trong mạng đồng bộ vào NTP server nội bộ.
- Kiểm tra định kỳ: `timedatectl` (Linux) hoặc `w32tm /query /status` (Windows).

> ✅ **Checklist NTP:** Trước khi đưa SIEM vào vận hành, xác nhận mọi nguồn log đang đồng bộ NTP và độ lệch (offset) < 1 giây.

---

### 8.3 Bảo Vệ Tính Toàn Vẹn Của Log (Log Integrity)

**Vấn đề:** Việc đầu tiên kẻ tấn công làm khi chiếm được máy là **xóa log** để xóa dấu vết. Nếu log chỉ nằm trên chính máy bị chiếm, chứng cứ biến mất.

**Nguyên tắc:** Log phải được **đẩy ra ngoài ngay lập tức** (forward) đến SIEM, trước khi kẻ tấn công kịp xóa.

**Các lớp bảo vệ:**

| Lớp | Cơ chế | Ghi chú |
|-----|--------|---------|
| **Forward ngay** | Wazuh agent đẩy log về SIEM liên tục (near real-time) | Ngay cả khi máy bị chiếm, log đã ra ngoài |
| **Immutable storage** | Lưu log vào hệ thống không cho sửa/xóa (S3 Object Lock, WORM storage) | Đảm bảo log dùng được trong điều tra pháp lý |
| **Mã hóa log trong transit** | TLS giữa agent và SIEM | Chống chặn/sửa log trên đường truyền |
| **Kiểm tra tính toàn vẹn** | Hash log định kỳ (Wazuh có tính năng File Integrity Monitoring) | Phát hiện nếu log bị sửa |

> ⚠️ **Lưu ý:** "Thu thập log" và "bảo vệ log" là hai việc khác nhau. Thu thập mà không bảo vệ thì log vẫn có thể bị xóa/sửa sau khi thu thập, hoặc bị mất nếu SIEM không có redundancy.

---

### 8.4 Dự Phòng — "1 Máy Chạy Tất Cả" Không Phải Production-Resilient

**Vấn đề:** Phương án "1 máy chủ chạy mọi thứ qua Docker" là cách khởi đầu hợp lý về chi phí, nhưng đây là một **điểm chết đơn lẻ (Single Point of Failure — SPOF)**. Máy đó hỏng (nguồn điện, đĩa, RAM) → SOC mù hoàn toàn.

**Sự đánh đổi cần nói thẳng:**

| Phương án | Ưu điểm | Hạn chế |
|-----------|---------|---------|
| **1 máy, Docker** | Chi phí thấp, dễ khởi đầu | SPOF — hỏng là mù, không phải production-resilient |
| **2 máy (active + standby)** | Có dự phòng cơ bản | Phức tạp hơn, cần sync dữ liệu |
| **Cluster (≥ 3 node)** | Thực sự production-resilient | Chi phí và độ phức tạp cao hơn đáng kể |

**Khuyến nghị thực tế cho tổ chức nhỏ:**

- Bắt đầu với 1 máy, nhưng **đừng gọi nó là production-resilient**.
- Đảm bảo có **UPS** để chống mất điện đột ngột.
- Backup SIEM configuration và snapshot định kỳ ra thiết bị khác.
- Lên kế hoạch rõ: "Nếu máy SIEM này chết, mất bao lâu để khôi phục? Ai làm?" — và thực hành khôi phục ít nhất 1 lần/năm.
- Khi tổ chức phát triển, lộ trình lên ít nhất 2 node.

---

### 8.5 Khía Cạnh Pháp Lý — Giám Sát & Lưu Trữ Log

**Vấn đề thường bị bỏ quên:** Việc giám sát hoạt động người dùng và lưu trữ log có ràng buộc pháp lý. Xây SOC mà không quan tâm đến pháp lý có thể dẫn đến vi phạm quyền riêng tư hoặc không đủ căn cứ pháp lý khi cần dùng log làm bằng chứng.

**Những câu hỏi pháp lý cần trả lời trước khi vận hành:**

| Câu hỏi | Ý nghĩa |
|---------|---------|
| Đã có chính sách sử dụng CNTT (Acceptable Use Policy) không? | Người dùng cần biết họ đang được giám sát — thông báo trước là yêu cầu pháp lý ở nhiều quốc gia |
| Lưu log bao lâu? | Một số quy định bắt buộc lưu tối thiểu X tháng/năm; một số quy định về riêng tư lại giới hạn thời gian lưu |
| Ai được phép truy cập log? | Log chứa thông tin cá nhân (IP, tài khoản, hoạt động). Phân quyền truy cập phải được kiểm soát và ghi lại |
| Log có thể dùng làm bằng chứng pháp lý không? | Cần đảm bảo tính toàn vẹn (xem 8.3) và chuỗi custody (chain of custody) nếu muốn dùng trong tố tụng |

**Bối cảnh Việt Nam:** Tham chiếu Luật An toàn thông tin mạng, Luật Bảo vệ Dữ liệu Cá nhân (khi có hiệu lực), và các quy định của Bộ TT&TT về lưu trữ log. Với tổ chức trong lĩnh vực tài chính, y tế, hoặc hạ tầng quan trọng, có thể có yêu cầu riêng về thời gian lưu trữ và báo cáo sự cố.

> 💡 **Thực hành tốt nhất:** Soạn một trang "Chính sách giám sát và lưu trữ log" nội bộ — ai được giám sát, giám sát cái gì, lưu bao lâu, ai được xem — và đưa vào quy trình onboarding nhân viên.

---

## Checklist Tổng Hợp (Production-Ready)

In ra tự tick khi xây SOC thực tế:

**Giai đoạn Requirements & Assessment**
- [ ] Đã xác định mục tiêu & phạm vi SOC
- [ ] Đã kiểm kê toàn bộ thiết bị CNTT
- [ ] Đã vẽ sơ đồ mạng (vật lý + luận lý)
- [ ] Đã đánh giá mức an toàn hiện tại (gap analysis)
- [ ] Đã xác định tài sản & dữ liệu quan trọng nhất
- [ ] Đã ước lượng EPS và dung lượng log cần lưu trữ (Phần 8.1)
- [ ] Đã xác định yêu cầu pháp lý về giám sát & lưu trữ log (Phần 8.5)

**Giai đoạn Design & Deployment**
- [ ] Đã chọn mô hình vận hành (in-house / MSSP / hybrid)
- [ ] Đã phân chia mạng thành các VLAN — Admin & SOC nối thẳng vào firewall, không qua DMZ
- [ ] Đã triển khai SIEM phù hợp với EPS thực tế
- [ ] Đã triển khai EDR cho endpoint
- [ ] Đã triển khai IDS cho mạng (Suricata) + phân tích lưu lượng (Zeek)
- [ ] Đã tích hợp Threat Intelligence (MISP/OTX/AbuseIPDB)
- [ ] Đã viết luật phát hiện (Sigma), ánh xạ MITRE ATT&CK
- [ ] Đã bảo mật port 22 (VPN/Bastion/ZTNA — không phơi thẳng)
- [ ] Đã cấu hình NTP cho toàn bộ nguồn log, độ lệch < 1 giây (Phần 8.2)
- [ ] Đã cấu hình forward log realtime về SIEM (không chỉ lưu cục bộ) (Phần 8.3)
- [ ] Đã đánh giá rủi ro Single Point of Failure và có kế hoạch dự phòng (Phần 8.4)

**Giai đoạn Operations & Improvement**
- [ ] Đã phân vai trò nhân sự cốt lõi (Tier 1/2/3, Manager, Engineer)
- [ ] Đã có IR Playbook (4 pha NIST: Chuẩn bị → Phát hiện → Khống chế/Khôi phục → Rút kinh nghiệm)
- [ ] Đã giảm false positive (tuning luật)
- [ ] Đã thiết lập chỉ số đo lường (MTTD, MTTA, MTTR)
- [ ] Đã có lịch tinh chỉnh & threat hunting định kỳ
- [ ] Đã có kế hoạch backup + **thực hành khôi phục** cho hệ thống SOC
- [ ] Đã có kế hoạch quản lý dung lượng log (hot/cold storage, thời hạn lưu)
- [ ] Đã ban hành chính sách giám sát & lưu trữ log, thông báo tới người dùng

---

> **"Công cụ không tự chạy — SOC sống được nhờ con người và quy trình. Bắt đầu nhỏ, làm chắc phần cốt lõi, rồi mới mở rộng."**

---

*Nguồn: `D:\CSAI\ref\soc_diy.md` — Tài liệu nội bộ CSAI 2026*
*Phiên bản: 1.1 — 2026-06-03 (cập nhật: sơ đồ VLAN, NIST 4 pha, Zeek, NTP, EPS sizing, log integrity, redundancy, pháp lý)*
