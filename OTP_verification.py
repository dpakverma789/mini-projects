
import string
import random
import time
import smtplib
from email.mime.text import MIMEText


def password_generator():
    password = ''
    for _ in range(6):
        i = random.choice(string.digits)
        password = password + i
    return password 


get_password = password_generator()


try:
    msg = MIMEText("Your OTP is- "+get_password)
    msg["from"] = "dpakverma1234@gmail.com"
    To = input("\nENTER YOUR EMAIL: ")
    msg["to"] = To
    msg["Subject"] = "OTP VERIFICATION"
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("dpakverma1234@gmail.com", "urlove4mine")
    print("\n", "\t"*4, "WAIT FOR A MOMENT")
    server.send_message(msg)
    print("\n", "\t"*3, "=== OTP SENT SUCCESSFULLY ===")
    server.quit()
    time.sleep(2)
    otp = input("\n\nENTER OTP :")
    if otp == get_password:
        print("\n", "\t"*3, "=== EMAIL VERIFIED ===")
    else:
        print("\n", "\t"*3, "=== INVALID OTP ===")
except:
    print("\n", "\t"*3, "=== OTP SENT FAILED ===")
    


























