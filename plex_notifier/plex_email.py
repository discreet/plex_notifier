#!/usr/bin/env python3
"""
This module formats the returned plex media and builds a proper email message.
It will then send an email to all of the subscribed plex users.
"""
import re
import yagmail
import jinja2

def __format_body(media, template):
    """
    This function loads the email body template and renders the contents using
    the dictionary passed to it.
    """
    loader = jinja2.FileSystemLoader(searchpath='templates')
    template_env = jinja2.Environment(loader=loader)
    template = template_env.get_template(template)

    return template.render(media=media)

def send_mail(email_attrs, plex_server, new_media):
    """
    Takes the namedtuple of email attributes, plex server, and dictionary of new
    media. The media will be formatted and the email composed and sent to the
    subscribed users.
    """
    yag = yagmail.SMTP(email_attrs.username, email_attrs.password)
    body = __format_body(new_media, 'email')
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
