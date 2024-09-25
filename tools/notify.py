from data_objs.meal import Meal
import sys
import smtplib
from dotenv import load_dotenv
import os
import time

'''
    Function for notifying saved users
'''
def send_notification(scraped_data: list[Meal], user_info: dict[str,str]) -> bool:
    # load keys
    load_dotenv()
    email_user = os.getenv("EMAIL_USER")
    email_key = os.getenv("EMAIL_APPKEY")

    try:
        # open secure smtp server and login with credentials
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
            smtp_server.login(email_user, email_key)

            for name, address in user_info.items():
                smtp_server.sendmail(email_user, address, (f"Hello my friend {name}"))
        return True
    
    except Exception:
        return False