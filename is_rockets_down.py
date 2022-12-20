import smtplib, ssl
import os
from dotenv import load_dotenv
load_dotenv()

import requests

def send_email(site):
    port = 465  # For SSL
    password = os.getenv('EMAIL_PASSWORD')

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("isrocketsdown@gmail.com", password)
        subject = "Site Rockets"
        text = "Le site Rockets {} est down.".format(site)
        message = 'Subject: {}\n\n{}'.format(subject, text)

        server.sendmail("isrocketsdown@gmail.com", "justin.lague.jl@gmail.com", message)
        print("email")

if __name__ == '__main__':
    url = 'https://clubrockets.com/'
    r = requests.get(url)

    if(r.status_code != 200):
        send_email(".com")

    url = 'https://clubrockets.ca/'
    r = requests.get(url)

    if(r.status_code != 200):
        send_email(".ca")
