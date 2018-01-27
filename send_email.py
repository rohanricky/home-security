import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart



def email(frame):
    msg=MIMEMultipart()
    msg.preamble='donga'
    msg['Subject'] = 'donga na koduku'
    msg['From'] = 'rohanricky0609@gmail.com'
    msg['To'] = 'rohanricky0609@gmail.com'
    with open(frame,'rb') as fp:
        img=MIMEImage(fp.read())
    msg.attach(img)
    server = smtplib.SMTP('smtp.gmail.com',port=587)
    server.starttls()
    server.login('rohanricky0609@gmail.com','suckmycock')
    server.send_message(msg)
    server.quit()
