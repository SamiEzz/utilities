import smtplib
import imghdr
import config
from email.message import EmailMessage

r_mail='sami.ezzerouali@hotmail.com'
r_subject = 'Python test !'
r_message = 'test 2'
r_joint_src = './ressources/1.png'

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
    
    with open(r_joint_src,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
        print(file_type)
        #msg.set_content(r_message)
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
    send(msg)

main()