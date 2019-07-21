import smtplib

import config
from email.message import EmailMessage

r_mail='sami.ezzerouali@hotmail.com'
r_subject = 'Python test !'
r_message = 'test 2'

def send(msg):
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(config.EMAIL_ADDRESS, config.PASSWORD)
        smtp.send_message(msg)

def main():
    msg = EmailMessage()
    msg['Subject'] = r_subject
    msg['From'] = config.EMAIL_ADDRESS
    msg['To'] = r_mail
    msg.set_content(r_message)
    send(msg)

main()