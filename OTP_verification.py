import os
import string
import random
import smtplib
from email.mime.text import MIMEText

try:
    otp_password = int(''.join(random.sample(string.digits, 6)))
    mail_body = f"Your OTP is - {otp_password}"
    mail = MIMEText(mail_body)
    mail["from"] = os.environ['EMAIL_HOST_USER']
    mail["to"] = input("\nENTER YOUR EMAIL: ")
    mail["Subject"] = "OTP VERIFICATION"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.environ['EMAIL_HOST_USER'], os.environ['EMAIL_HOST_PASSWORD'])
    print("\n", "\t"*4, "WAIT FOR A MOMENT")
    server.send_message(mail)
    print("\n", "\t"*3, "=== OTP SENT SUCCESSFULLY ===")
    server.quit()
    input_otp = int(input("\n\nENTER OTP :"))
    mail = "=== EMAIL VERIFIED ===" if input_otp == otp_password else "=== INVALID OTP ==="
    print("\n", "\t"*3, mail)
except:
    print("\n", "\t"*3, "=== OTP SENT FAILED ===")
