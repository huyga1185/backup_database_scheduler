# Backup database scheduler
Đây là bài tập chương 3 môn tự động hoá

## Features

Tự động backup các file `.sql` hoặc `.sql3` vào folder backup lúc `00:00` mỗi ngày và gửi email báo cáo kết quả đến đích

## Requirements

- `python`
- `python-dotenv`
- `schedule`

## Installation

1.  Clone repo:
```bash
    git clone https://github.com/huyga1185/backup_database_scheduler
```

2. Cài đặt thư viện

```bash
    pip install python-dotenv schedule
```

3.Mở folder repo
```bash
    cd backup_database_scheduler
```

## Usage

- Bước 1: clone repo và cài đặt lib cần thiết
- Bước 2: Tạo file `.env` có nội dung sau:

```bash
    #email gửi
    EMAIL_SENDER = your_email_sender eg:example@gmail.com
    #app password email gửi
    EMAIL_PASSWORD= your_app_password eg:abcd-asdjk-asdlla....
    #email nhận
    EMAIL_RECEIVER= your_target_email eg:example@gmail.com
```

- Bước 4: Sao chép file `.sql` hoặc `.sqlite3` của bạn vào thư mục gốc của project

- Bước 3: Khởi chạy
```bash
    python backup.py
```


