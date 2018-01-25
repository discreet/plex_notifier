#!/usr/bin/env python

import os
from modules import plex_auth
from modules import plex_media
from modules import plex_users
from modules import plex_email

plex_username = os.environ["PLEX_USERNAME"]
plex_password = os.environ["PLEX_PASSWORD"]
plex_server = os.environ["PLEX_SERVER"]
days_passed = os.environ["PLEX_DAYS_PASSED"]
send_mail = os.environ.get("PLEX_SEND_MAIL")
if send_mail in ['True', 'true']:
    email_username = os.environ["PLEX_EMAIL_USERNAME"]
    email_password = os.environ["PLEX_EMAIL_PASSWORD"]
    unsub_emails = os.environ.get("PLEX_UNSUB_EMAIL")

my_plex = plex_auth.connect_to_plex(plex_username, plex_password, plex_server)

new_movies = plex_media.get_new(my_plex, 'Movies', days_passed)

if not new_movies:
    print 'No new movies added'
    exit()

if send_mail in ['True', 'true']:
    user_emails = plex_users.get_emails(my_plex)
    if unsub_emails:
        email_list = plex_users.unsub_emails(unsub_emails, user_emails)
    else:
        email_list = user_emails
    plex_email.send_mail(email_username, email_password, email_list, plex_server, new_movies)
    exit()
else:
    print new_movies
    exit()
