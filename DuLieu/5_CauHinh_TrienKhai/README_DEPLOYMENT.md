# Hướng Dẫn Triển Khai Máy Chủ VietVoice AI (vietvoice-ai.online)

Tài liệu hướng dẫn cấu hình và triển khai hệ thống VietVoice AI bao gồm Pipeline tiền xử lý, Engine viXTTS, RVC Feature Extraction và Web Interface.

---

## 1. Yêu Cầu Môi Trường (System Requirements)

- **OS**: Ubuntu 22.04 LTS / Windows Server
- **Python**: Version 3.10+
- **GPU**: NVIDIA GPU (RTX 3060/4090 hoặc A100/T4) hỗ trợ CUDA 11.8 / 12.1 (khuyến nghị cho viXTTS & RVC)
- **RAM**: Tối thiểu 16 GB (khuyến nghị 32 GB)
- **Web Server**: Nginx / Apache XAMPP

---

## 2. Các Phương Thức Triển Khai

### Phương thức 1: Triển khai qua Docker (Khuyên dùng)

1. **Build Docker Image**:
   ```bash
   cd 5_CauHinh_TrienKhai
   docker build -t vietvoice-app:latest -f Dockerfile .
   ```

2. **Chạy qua Docker Compose**:
   ```bash
   docker-compose up -d
   ```

### Phương thức 2: Triển khai với Nginx Reverse Proxy (Máy chủ Linux Production)

1. Cài đặt Nginx & Certbot SSL:
   ```bash
   sudo apt update && sudo apt install -y nginx certbot python3-certbot-nginx
   ```

2. Copy tệp cấu hình Nginx:
   ```bash
   sudo cp nginx_vietvoice.conf /etc/nginx/sites-available/vietvoice-ai.online
   sudo ln -s /etc/nginx/sites-available/vietvoice-ai.online /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl reload nginx
   ```

3. Thường trực cấp chứng chỉ SSL HTTPS:
   ```bash
   sudo certbot --nginx -d vietvoice-ai.online -d www.vietvoice-ai.online
   ```

### Phương thức 3: Triển khai qua Apache (XAMPP Windows Server)

1. Mở file `C:\xampp\apache\conf\extra\httpd-vhosts.conf`
2. Thêm nội dung trong tệp `apache_config.conf`
3. Khởi động Flask Server bằng `start_web.bat` hoặc `run_gpu.bat`
4. Khởi động lại Apache trong XAMPP Control Panel.

---

## 3. Khởi Động Ứng Dụng Hàng Ngày

- **Windows**: Chạy `start_web.bat` hoặc `start_server.bat`
- **Linux**: Chạy `bash start_web.sh` hoặc sử dụng systemd service `/etc/systemd/system/vietvoice.service`.
