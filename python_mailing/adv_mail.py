import smtplib
import imghdr
import config
import codecs
from email.message import EmailMessage

#r_mail='sami.ezzerouali@hotmail.com'
r_contacts = ['sami.ezzerouali@hotmail.com','scrapper137@gmail.com']
r_subject = 'Python test !'
r_message = f'Hello Sami,\n\nPlease find attached some confidentiel documents.\nKind regards,\nA. Zeus'
r_joint_src = './ressources/1.png'
m_html = './ressources/mail.html'


def send(msg):
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(config.EMAIL_ADDRESS, config.PASSWORD)
        smtp.send_message(msg)

def attach_img(msg,r_joint_src):
    with open(r_joint_src,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
        #print(file_type)
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

def attach_file(msg,r_joint_src):
    with open(r_joint_src,'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

def add_html(msg,html_file):
    f=codecs.open(html_file,'r')
    #print(f.read())
    msg.add_alternative(f.read(),subtype='html')

def main():
    msg = EmailMessage()
    msg['Subject'] = r_subject
    msg['From'] = config.EMAIL_ADDRESS
    msg['To'] = ', '.join(r_contacts)
    #msg.set_content(r_message)
    add_html(msg,m_html)
    attach_img(msg,r_joint_src)
    #attach_file(msg,'./ressources/cpumemory.pdf')
    send(msg)

main()