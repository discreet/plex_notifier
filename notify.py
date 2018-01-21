#!/usr/bin/env python

from plexapi.myplex import MyPlexAccount
import os
import datetime

username = os.environ["PLEX_USERNAME"]
password = os.environ["PLEX_PASSWORD"]
server = os.environ["PLEX_SERVER"]
movie_days = os.environ["PLEX_MOVIES_DAYS"]
send_mail = os.environ["PLEX_SEND_MAIL"]

def connect_to_plex(username, password, server):
    account = MyPlexAccount(username, password)
    return account.resource(server).connect()

my_plex = connect_to_plex(username, password, server)

def get_new(section, days_back):
    new_media_raw = my_plex.library.section(section).recentlyAdded()
    today = datetime.datetime.now()
    days_back = int(days_back)

    media_titles = []
    for new_media in new_media_raw:
        date_added = new_media.addedAt
        time_elapsed = today - date_added
        if time_elapsed.days<days_back:
            media_titles.append(new_media.title)
    return media_titles

new_movies = get_new('Movies', movie_days)
