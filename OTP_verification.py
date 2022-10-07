import os
import string
import random
import time
import smtplib
from email.mime.text import MIMEText

try:
    otp_password = int(''.join(random.sample(string.digits, 6)))
    body = f"Your OTP is - {otp_password}"
    msg = MIMEText(body)
    msg["from"] = os.environ['EMAIL_HOST_USER']
    msg["to"] = input("\nENTER YOUR EMAIL: ")
    msg["Subject"] = "OTP VERIFICATION"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.environ['EMAIL_HOST_USER'], os.environ['EMAIL_HOST_PASSWORD'])
    print("\n", "\t"*4, "WAIT FOR A MOMENT")
    server.send_message(msg)
    print("\n", "\t"*3, "=== OTP SENT SUCCESSFULLY ===")
    server.quit()
    time.sleep(2)
    input_otp = int(input("\n\nENTER OTP :"))
    if input_otp == otp_password:
        print("\n", "\t"*3, "=== EMAIL VERIFIED ===")
    else:
        print("\n", "\t"*3, "=== INVALID OTP ===")
except:
    print("\n", "\t"*3, "=== OTP SENT FAILED ===")
    


























