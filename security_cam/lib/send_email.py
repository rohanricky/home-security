import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime

def email(frame):
    msg=MIMEMultipart()
    msg.preamble='donga'
    msg['Subject'] = str(datetime.datetime.now())
    msg['From'] = 'rohanricky0609@gmail.com'
    msg['To'] = 'rohanricky0609@gmail.com'
    part = MIMEBase('application', "octet-stream")
    fo=open(frame,"rb")
    part.set_payload(fo.read())
    part.add_header('Content-Disposition', 'attachment; filename='+str(datetime.datetime.now())+'')
    encoders.encode_base64(part)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com',port=587)
    server.starttls()
    server.login('rohanricky0609@gmail.com','suckmycock')
    server.send_message(msg)
    server.quit()
