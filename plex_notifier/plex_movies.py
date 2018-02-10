#!/usr/bin/env python3
"""
This module will query the plex server for recently added movies within the
specified timeframe
"""
from collections import defaultdict
from plex_notifier import plex_utils

def __get_movies(plex, section):
    """
    Takes the plex server, and movies library section to return recently added
    movies.
    """
    return plex.library.section(section).recentlyAdded()

def __format_movies(movies):
    """
    This function creates a defaultdict of defaultdicts to build the data
    structure of the relevent information.
    """
    rec_dd = lambda: defaultdict(rec_dd)
    movie_dict = rec_dd()

    for movie in movies:
        title = movie.title
        year = movie.year
        rating = movie.contentRating
        stars = movie.rating
        release_date = movie.originallyAvailableAt.strftime("%Y-%m-%d")
        summary = movie.summary
        movie_dict[title]['Rating'] = rating
        movie_dict[title]['Stars'] = stars
        movie_dict[title]['Year'] = year
        movie_dict[title]['Release_Date'] = release_date
        movie_dict[title]['Summary'] = summary

    return movie_dict

def return_movies(plex, section, days_passed):
    """
    Retrieves all recently added movies and calls the format function returning
    human readable output.
    """
    days_elapsed = int(days_passed)
    recently_added = __get_movies(plex, section)
    new_movies = plex_utils.date_filter(recently_added, days_elapsed)

    return __format_movies(new_movies)
