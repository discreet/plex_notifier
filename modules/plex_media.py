#!/usr/bin/env python
"""
This module will query the plex server for recently added media within the
specified timeframe
"""
import datetime

def __get_new(plex, section):
    """
    Takes the plex server, library section and timeframe to query the plex
    library for the requested media.
    """
    return plex.library.section(section).recentlyAdded()

def __format_movies(new_media, today, days_elapsed):
    """
    Takes the raw media for movies and parses through it to return an array of
    movie titles that fall within the elapsed timeframe specified.
    """
    media_titles = []
    for media in new_media:
        date_added = media.addedAt
        time_elapsed = today - date_added
        if time_elapsed.days < days_elapsed:
            media_titles.append(media.title)
    return media_titles

def return_media(plex, section, days_passed):
    """
    Based on the section given retrieves all recently added media for that
    section and then calls the appropriate format function allowing human
    readable output.
    """
    today = datetime.datetime.now()
    days_elapsed = int(days_passed)

    new_media = __get_new(plex, section)
    return __format_movies(new_media, today, days_elapsed)
