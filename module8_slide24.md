
1. HTTP bình thường
2. SQL Injection
3. Brute force SSH

Mỗi ví dụ có:

* Dạng hiển thị như trong Wireshark
* Giải thích từng feature (IP, Port, Size, Payload, Timing)

---

# 1. Ví dụ 1 – HTTP request bình thường

(giả lập giống Wireshark)

```
Frame 128: 450 bytes on wire
Ethernet II, Src: 192.168.1.50, Dst: 93.184.216.34
Internet Protocol Version 4
    Source IP: 192.168.1.50
    Destination IP: 93.184.216.34
Transmission Control Protocol
    Source Port: 51522
    Destination Port: 80
Hypertext Transfer Protocol
    GET /products?page=2 HTTP/1.1
    Host: example.com
```

## Hướng dẫn giải thích cho học viên

* Source IP: 192.168.1.50 → máy tính trong LAN
* Destination IP: 93.184.216.34 → web server
* Port 80 → HTTP (bình thường)
* Payload: GET /products?page=2 → người dùng đang mở trang web
* Size 450 bytes → nhỏ, hợp lý
* Timing: chỉ 1 request → hoàn toàn bình thường

---

# 2. Ví dụ 2 – SQL Injection 

```
Frame 219: 612 bytes on wire
Ethernet II, Src: 192.168.1.50, Dst: 93.184.216.34
IP
    Source IP: 192.168.1.50
    Destination IP: 93.184.216.34
TCP
    Src Port: 51540
    Dst Port: 80
HTTP
    GET /login?user=admin' OR 1=1--&pass=abc HTTP/1.1
    Host: example.com
```

## Giải thích

* IP và port giống HTTP bình thường
* Nhưng Payload có chuỗi rất đáng ngờ:

  * admin' OR 1=1--
  * Đây chính là SQL injection cơ bản
* Size lớn hơn bình thường do payload dài
* Timing:

  * Không phải một request đơn → kẻ tấn công sẽ gửi *rất nhiều* request tương tự

**=> Chỉ nhìn payload là đủ biết nguy hiểm.**

---

# 3. Ví dụ 3 – Brute Force SSH

(brute force là nhiều request liên tục → timing quan trọng nhất)

```
Frame 512: 78 bytes
IP
    Source IP: 203.0.113.44
    Destination IP: 192.168.1.10
TCP
    Src Port: 49012
    Dst Port: 22
Payload:
    SSH-2.0-libssh_0.9.5

Frame 513: 78 bytes
...
Frame 514: 78 bytes
...
Frame 515: 78 bytes
...
Frame 516: 78 bytes
...
(50 kết nối trong vòng 5 giây)
```

## Giải thích

* Destination Port: 22 → SSH login
* Source IP: 203.0.113.44 → IP nước ngoài lạ
* Payload: luôn lặp lại cùng mẫu → brute force
* Size: nhỏ
* Timing: **50 lần trong 5 giây** → truy cập bất thường

**=> brute force không nằm trong payload, mà nằm trong hành vi (timing).**

---

# Tóm lại

* HTTP bình thường: **payload sạch, số request ít**
* SQL injection: **payload chứa mã nguy hiểm**
* SSH brute force: **payload nhỏ nhưng số lượng kết nối rất nhiều và rất nhanh**

---

