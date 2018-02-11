#!/usr/bin/env python3
"""
This is the main module that executes the program. It holds all the parameters
and logic used to get the desired behavior.
"""

import os
import json
import argparse
from collections import namedtuple
import plex_notifier

PARSER = argparse.ArgumentParser()
PARSER.add_argument("--schedule", help="create scheduled execution",
                    action="store_true")
PARSER.add_argument("--cancel", help="cancel scheduled execution",
                    action="store_true")
ARGS = PARSER.parse_args()

PLEX_USERNAME = os.environ["PLEX_USERNAME"]
PLEX_PASSWORD = os.environ["PLEX_PASSWORD"]
PLEX_SERVER = os.environ["PLEX_SERVER"]
DAYS_PASSED = os.environ["PLEX_DAYS_PASSED"]
SEND_MAIL = os.environ.get("PLEX_SEND_MAIL")
if SEND_MAIL in ['True', 'true']:
    EMAIL_USERNAME = os.environ["PLEX_EMAIL_USERNAME"]
    EMAIL_PASSWORD = os.environ["PLEX_EMAIL_PASSWORD"]
    UNSUB_EMAILS = os.environ.get("PLEX_UNSUB_EMAIL")

if ARGS.schedule:
    plex_notifier.schedule(os.path.abspath(__file__), DAYS_PASSED)
    exit()

if ARGS.cancel:
    plex_notifier.cancel()
    exit()

MY_PLEX = plex_notifier.connect_to_plex(PLEX_USERNAME, PLEX_PASSWORD,
                                        PLEX_SERVER)

NEW_MOVIES = plex_notifier.return_movies(MY_PLEX, 'Movies', DAYS_PASSED)
NEW_TELEVISION = plex_notifier.return_tv(MY_PLEX, 'TV Shows', DAYS_PASSED)

if not NEW_MOVIES and not NEW_TELEVISION:
    print('No new movies or television added')
    exit()

if not NEW_MOVIES:
    print('No new movies added')

if not NEW_TELEVISION:
    print('No new television added')

NEW_MEDIA = {
    "movies": NEW_MOVIES,
    "tv": NEW_TELEVISION,
}

if SEND_MAIL in ['True', 'true']:
    USER_EMAILS = plex_notifier.get_emails(MY_PLEX)
    if UNSUB_EMAILS:
        EMAIL_LIST = plex_notifier.unsub_emails(UNSUB_EMAILS, USER_EMAILS)
    else:
        EMAIL_LIST = USER_EMAILS
    Email = namedtuple('Email', 'username password mailing_list')
    EMAIL_ATTRS = Email(EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_LIST)
    plex_notifier.send_mail(EMAIL_ATTRS, PLEX_SERVER, NEW_MEDIA)
    exit()
else:
    print(json.dumps(NEW_MEDIA, indent=2))
    exit()
