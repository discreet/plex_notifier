#!/usr/bin/env python3

def get_emails(plex):
    users = plex.myPlexAccount().users()
    user_emails = []

    for user in users:
        user_emails.append(user.email)
    return user_emails

def unsub_emails(unsub_list, email_list):
    excludes = unsub_list.split(',')
    email_list = list(set(email_list)^set(excludes))
    return email_list
