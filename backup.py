import os
import shutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv
import schedule
import time

#Tai bien moi truong
load_dotenv()

#email nguoi gui
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
#mat khau app cua gmail
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
#email nguoi nhan
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

def send_email(sender, receiver, subject, body, password):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        text = message.as_string()
        server.sendmail(sender, receiver, text)
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

def backup_database():
    try:
        #kiem tra folder backup co ton tai khong
        if not os.path.exists('backup'):
            #neu khong tao folder backup
            os.makedirs('backup')
        
        #tao list luu tru ten cac files da backup thanh cong neu co nhieu hon 1 files can backup
        success_files = []

        #duyet qua tat ca file trong root folder cua project de tim file sql
        for filename in os.listdir('.'):
            if filename.endswith('.sql') or filename.endswith('.sqlite3'):
                src_path = os.path.join('.', filename)
                timestamp = datetime.now().strftime("%H%M%S_%Y%m%d")
                #ten file
                file_name = os.path.splitext(filename)[0] 
                #phan duoi file(extension)
                extension_name = os.path.splitext(filename)[1]
                backup_file_name = f"{filename}{timestamp}{extension_name}"
                backup_file_path = os.path.join('backup', backup_file_name)

                shutil.copy2(src_path, backup_file_path)
                success_files.append(backup_file_name)

            if success_files:
                body = "Backup thành công các file:" + '\n'.join(success_files)
                send_email(EMAIL_SENDER, EMAIL_RECEIVER,"Backup Thành Công", body, EMAIL_PASSWORD)
            else:
                body = "Không tìm thấy file .sql hoặc .sqlite3 để backup."
                send_email(EMAIL_SENDER, EMAIL_RECEIVER, "Backup Thất Bại", body, EMAIL_PASSWORD)
    except Exception as e:
        send_email(EMAIL_SENDER, EMAIL_RECEIVER, "Backup Thất Bại", f"Lỗi: {str(e)}", EMAIL_PASSWORD)

schedule.every().day.at("00:00").do(backup_database)

print("dang chay")

while True:
    schedule.run_pending()
    time.sleep(1)