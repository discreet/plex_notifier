#!/usr/bin/env python
"""
This module will query the plex server for recently added media within the
specified timeframe
"""
import datetime

def get_new(plex, section, days_passed):
    """
    Takes the plex server, library section and timeframe to query the plex
    library for the requested media.
    """
    new_media_raw = plex.library.section(section).recentlyAdded()
    today = datetime.datetime.now()
    days_elapsed = int(days_passed)
    media_titles = []

    for new_media in new_media_raw:
        date_added = new_media.addedAt
        time_elapsed = today - date_added
        if time_elapsed.days < days_elapsed:
            media_titles.append(new_media.title)
    return media_titles
