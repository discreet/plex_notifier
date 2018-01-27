#!/usr/bin/env python
"""
This is the main module that executes the program. It holds all the parameters
and logic used to get the desired behavior.
"""

import os
from modules import plex_auth
from modules import plex_media
from modules import plex_users
from modules import plex_email

PLEX_USERNAME = os.environ["PLEX_USERNAME"]
PLEX_PASSWORD = os.environ["PLEX_PASSWORD"]
PLEX_SERVER = os.environ["PLEX_SERVER"]
DAYS_PASSED = os.environ["PLEX_DAYS_PASSED"]
SEND_MAIL = os.environ.get("PLEX_SEND_MAIL")
if SEND_MAIL in ['True', 'true']:
    EMAIL_USERNAME = os.environ["PLEX_EMAIL_USERNAME"]
    EMAIL_PASSWORD = os.environ["PLEX_EMAIL_PASSWORD"]
    UNSUB_EMAILS = os.environ.get("PLEX_UNSUB_EMAIL")

MY_PLEX = plex_auth.connect_to_plex(PLEX_USERNAME, PLEX_PASSWORD, PLEX_SERVER)

NEW_MOVIES = plex_media.return_media(MY_PLEX, 'Movies', DAYS_PASSED)

if not NEW_MOVIES:
    print 'No new movies added'
    exit()

if SEND_MAIL in ['True', 'true']:
    USER_EMAILS = plex_users.get_emails(MY_PLEX)
    if UNSUB_EMAILS:
        EMAIL_LIST = plex_users.unsub_emails(UNSUB_EMAILS, USER_EMAILS)
    else:
        EMAIL_LIST = USER_EMAILS
    plex_email.send_mail(EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_LIST, PLEX_SERVER, NEW_MOVIES)
    exit()
else:
    for movie in NEW_MOVIES:
        print movie
    exit()
