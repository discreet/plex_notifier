#!/usr/bin/env python3

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

def send_mail(username, password, email_list, media):
    for email in email_list:
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = email
        msg['Subject'] = 'Plex Update: New Media Added'

        body = "Recently Added to Plex\n"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)
        text = ms.as_string()
        server.sendmail(username, email, text)
        server.quit()

        print 'Email sent to %s' % (email)

