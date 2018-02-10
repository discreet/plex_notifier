#!/usr/bin/env python3
"""
This module formats the returned plex media and builds a proper email message.
It will then send an email to all of the subscribed plex users.
"""
import re
import yagmail
import jinja2

def __format_body(media):
    """
    foo
    """
    loader = jinja2.FileSystemLoader(searchpath='templates')
    template_env = jinja2.Environment(loader=loader)
    template = template_env.get_template('email')

    return template.render(media=media)

def send_mail(email_attrs, plex_server, new_media):
    """
    Takes the email username and password, list of email recipients, plex server
    name and formatted media to compose and send the email to the subscribed
    users.
    """
    yag = yagmail.SMTP(email_attrs.username, email_attrs.password)
    body = __format_body(new_media)
    subject = 'Plex Update: New Media Added to %s' % (plex_server)
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    for obj in email_attrs.mailing_list:
        if re.match(email_regex, obj):
            yag.send(to=obj, subject=subject, contents=body)
            print('Email sent to %s' % (obj))
        else:
            recipient = email_attrs.username
            subject = 'Invalid Email Address'
            contents = '%s is NOT a valid email address' % (obj)
            print(contents)
            yag.send(to=recipient, subject=subject, contents=contents)
