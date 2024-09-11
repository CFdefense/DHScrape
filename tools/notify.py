from data_objs.meal import Meal
import sys
import smtplib
from dotenv import load_dotenv
import os

'''
    Function for notifying saved users
'''
def sendNotification(scraped_data: list[Meal], user_info: dict[str,str]) -> bool:
    # load keys
    load_dotenv()
    email_user = os.getenv("EMAIL_USER")
    email_key = os.getenv("EMAIL_APPKEY")

    # open secure smtp server and login with credentials
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(email_user, email_key)

        # send message -> TODO iterate built dict param and build recipiant
        smtp_server.sendmail(email_user,recipiant,"hello")
    return True