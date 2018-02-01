#!/usr/bin/env python
"""
This module gets a list of all the email addresses for the subscribed plex users
and can filter out unsubscribed users if needed.
"""

import re

def get_emails(plex):
    """
    Retrieves a list of plex user accounts and returns each of their email
    addresses.
    """
    users = plex.myPlexAccount().users()
    user_emails = [user.email for user in users]

    return user_emails

def unsub_emails(unsub_list, email_list):
    """
    Takes the list of plex user email address and filters out the members of the
    unsubscribe list.
    """
    excludes = re.split(r"(\W|\W\s)", unsub_list)
    email_list = list(set(email_list)^set(excludes))
    return email_list
