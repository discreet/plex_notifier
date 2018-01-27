#!/usr/bin/env python
"""
This module formats the returned plex media and builds a proper email message.
It will then send an email to all of the subscribed plex users.
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import re

def __format_media(media):
    """
    Takes the array of recently added media and converts it to a string using a
    newline character as a delimeter.
    """
    return '\n'.join(media)

def send_mail(username, password, email_list, plex_server, media):
    """
    Takes the email username and password, list of email recipients, plex server
    name and formatted media to compose and send the email to the subscribed
    users.
    """
    media = __format_media(media)
    unsub = 'To Unsubscribe from this list please reply with the word "Unsubscribe".'
    email_body = 'Recently Added to Plex\n\n%s\n\n%s' % (media, unsub)
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    for email in email_list:
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = email
        msg['Subject'] = 'Plex Update: New Media Added to %s' % (plex_server)

        body = email_body
        msg.attach(MIMEText(body, 'plain'))

        if re.match(email_regex, email):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            text = msg.as_string()
            server.sendmail(username, email, text)
            server.quit()

            print 'Email sent to %s' % (email)
