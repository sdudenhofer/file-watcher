import configparser
import configparser
import pyodbc
import pandas as pd
import openpyxl
import datetime
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import smtplib
import os

config = configparser.ConfigParser()
config.read('../config.ini')
eserv = config['OUTLOOK']['SERVER']
euser = config['OUTLOOK']['USER']
epass = config['OUTLOOK']['PASS']



def email_log(rec1, rec2, rec3, subject, filename):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    # recipients needs to be edited for each file
    recipients = [rec1 + "," + rec2 + "," + rec3]
    for to in recipients:
          msg['To'] = to

    attachment = MIMEBase('application','octet-stream')
    f = filename

    msg.attach(MIMEText('Report Attached'))
    attachment.set_payload(open(f, 'rb').read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename = os.path.basename(f))
    msg.attach(attachment)
    s = smtplib.SMTP(eserv)
    s.starttls()
    s.login(euser, epass)
    s.sendmail(sender, msg['To'], msg.as_string())
    s.quit()
