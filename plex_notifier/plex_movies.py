#!/usr/bin/env python
"""
This module will query the plex server for recently added media within the
specified timeframe
"""
from plex_notifier import plex_utils

def __get_movies(plex, section):
    """
    Takes the plex server, library section and timeframe to query the plex
    library for the requested media.
    """
    return plex.library.section(section).recentlyAdded()

def return_movies(plex, section, days_passed):
    """
    Based on the section given retrieves all recently added media for that
    section and then calls the appropriate format function allowing human
    readable output.
    """
    days_elapsed = int(days_passed)
    new_movies = __get_movies(plex, section)
    filtered_media = plex_utils.date_filter(new_movies, days_elapsed)
    return [obj.title for obj in filtered_media]
