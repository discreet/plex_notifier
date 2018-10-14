#!/usr/bin/env python3
"""
This is the main module that executes the program. It holds all the parameters
and logic used to get the desired behavior.
"""

import os
import json
from argparse import ArgumentParser
from collections import namedtuple
import plex_notifier


PARSER = ArgumentParser()
PARSER.add_argument('-U', '--username', required=False,
                    help="Plex username. Required if environmental variable is not set")
PARSER.add_argument('-P', '--password', required=False,
                    help="Plex password. Required if environmental variable is not set")
PARSER.add_argument('-S', '--server', required=False,
                    help="Plex server. Required if environmental variable is not set")
PARSER.add_argument('-D', '--passed', required=False,
                    help="The number of days to go back to find recently added media. "
                         "Required if environmental variable are not set")
PARSER.add_argument('-s', '--send_mail', required=False, type=bool, default=False,
                    help="Whether or not to send the update email. True/False. Default is False")
PARSER.add_argument('-e', '--email', required=False,
                    help="The username for the email address sending the mail. "
                         "Required if --send_mail is True")
PARSER.add_argument('-p', '--epass', required=False,
                    help="The password for the email address sending the mail. "
                         "Required if --send_mail is True")
PARSER.add_argument('-u', '--unsub', required=False,
                    help="Comma separated string of emails to omit from sending. "
                         "Must be passed as a .txt file")

ARGS = PARSER.parse_args()
if ARGS.send_mail and None in [ARGS.email, ARGS.epass, ]:
    PARSER.error(" --send_mail requires --email and --epass to be set")


PLEX_USERNAME = ARGS.username
PLEX_PASSWORD = ARGS.password
PLEX_SERVER = ARGS.server
DAYS_PASSED = ARGS.passed
SEND_MAIL = ARGS.send_mail
EMAIL_USERNAME = ARGS.email
EMAIL_PASSWORD = ARGS.epass
UNSUB_EMAILS = ARGS.unsub
if ARGS.unsub:
    try:
        with open(ARGS.unsub) as file:
            UNSUB_EMAILS = file.read()
    except FileNotFoundError:
        PARSER.error("--unsub requires a relative filename. "
                     "Absolute path can be used if surrounded by quotes.")

ENVIRONMENT_DICT = {'PLEX_USERNAME': PLEX_USERNAME,
                    'PLEX_PASSWORD': PLEX_PASSWORD,
                    'PLEX_SERVER': PLEX_SERVER,
                    'DAYS_PASSED': DAYS_PASSED,
                    'SEND_MAIL': SEND_MAIL,
                    'EMAIL_USERNAME': EMAIL_USERNAME,
                    'EMAIL_PASSWORD': EMAIL_PASSWORD,
                    'UNSUB_EMAIL':  UNSUB_EMAILS, }

for key in ENVIRONMENT_DICT:
    if ENVIRONMENT_DICT[key] is None and key in os.environ:
        ENVIRONMENT_DICT[key] = os.environ[key]
    elif ENVIRONMENT_DICT[key] is None and key not in os.environ:
        if key in ['EMAIL_USERNAME', 'EMAIL_PASSWORD', 'UNSUB_EMAIL']:
            continue
        else:
            quit(print("{} environmental variable is missing. "
                       "Please add the appropriate flag to cli command "
                       "or add the appropriate environment variable. "
                       "Use -h flag for cli help".format(key)))


MY_PLEX = plex_notifier.connect_to_plex(PLEX_USERNAME, PLEX_PASSWORD, PLEX_SERVER)

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
