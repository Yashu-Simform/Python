import smtplib
from dotenv import load_dotenv
import os

load_dotenv('prac.env')

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
USER_PASS = os.getenv('EMAIL_PASS')
print(EMAIL_ADDRESS)