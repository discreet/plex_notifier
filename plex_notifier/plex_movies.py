#!/usr/bin/env python
"""
This module will query the plex server for recently added media within the
specified timeframe
"""
from collections import defaultdict
from plex_notifier import plex_utils

def __get_movies(plex, section):
    """
    Takes the plex server, library section and timeframe to query the plex
    library for the requested media.
    """
    return plex.library.section(section).recentlyAdded()

def __format_movies(movies):
    """
    """
    rec_dd = lambda: defaultdict(rec_dd)
    movie_dict = rec_dd()

    for movie in movies:
        title = movie.title
        year = movie.year
        summary = movie.summary
        movie_dict[title]['Year'] = year
        movie_dict[title]['Summary'] = summary

    return movie_dict

def return_movies(plex, section, days_passed):
    """
    Based on the section given retrieves all recently added media for that
    section and then calls the appropriate format function allowing human
    readable output.
    """
    days_elapsed = int(days_passed)
    recently_added = __get_movies(plex, section)
    new_movies = plex_utils.date_filter(recently_added, days_elapsed)

    return __format_movies(new_movies)
