#!/usr/bin/env python

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

def format_media(media):
    return '\n'.join(media)

def send_mail(username, password, email_list, plex_server, media):
    media = format_media(media)
    unsub = 'To Unsubscribe from this list please reply with the word "Unsubscribe".'
    email_body = 'Recently Added to Plex\n\n%s\n\n%s' % (media, unsub)

    for email in email_list:
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = email
        msg['Subject'] = 'Plex Update: New Media Added to %s' % (plex_server)

        body = email_body
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)
        text = msg.as_string()
        server.sendmail(username, email, text)
        server.quit()

        print 'Email sent to %s' % (email)

