#!/usr/bin/env python

import datetime

def get_new(plex, section, days_passed):
    new_media_raw = plex.library.section(section).recentlyAdded()
    today = datetime.datetime.now()
    days_elapsed = int(days_passed)
    media_titles = []

    for new_media in new_media_raw:
        date_added = new_media.addedAt
        time_elapsed = today - date_added
        if time_elapsed.days<days_elapsed:
            media_titles.append(new_media.title)
    return media_titles
