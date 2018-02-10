#!/usr/bin/env python3
"""
This module will query the plex server for recently added media within the
specified timeframe
"""
from collections import namedtuple
from collections import defaultdict
from plex_notifier import plex_utils

def __get_tv(plex, section):
    """
    This function fetches all of the recently added episodes, seasons and shows
    and returns a namedtuple with the data
    """
    episodes = plex.library.section(section).recentlyAdded(libtype='episode')
    shows = plex.library.section(section).recentlyAdded(libtype='show')
    seasons = plex.library.section(section).recentlyAdded(libtype='season')
    television = namedtuple('Television', 'shows seasons episodes')
    return television(shows, seasons, episodes)

def __get_show_episodes(plex, section, days_elapsed, new_shows):
    """
    This function retrieves a list of episodes for each new show and filters
    them based on the date range provided
    """
    show_episodes = []
    for show in new_shows:
        episodes = plex.library.section(section).get(show.title).episodes()
        show_episodes.append(plex_utils.date_filter(episodes, days_elapsed))
    show_episodes = plex_utils.flatten(show_episodes)

    return show_episodes

def __get_season_episodes(plex, section, days_elapsed, new_seasons):
    """
    This function retrieves a list of episodes for each new season and filters
    them based on the date range provided
    """
    season_episodes = []
    for season in new_seasons:
        episodes = plex.library.section(section).get(season.parentTitle).episodes()
        season_episodes.append(plex_utils.date_filter(episodes, days_elapsed))
    season_episodes = plex_utils.flatten(season_episodes)

    return season_episodes

def __format_shows(episodes):
    """
    This function takes a list of episodes and creates a JSON structure with all
    of the information to be used in the email newsletter
    """
    rec_dd = lambda: defaultdict(rec_dd)
    episode_dict = rec_dd()

    for episode in episodes:
        show = episode.grandparentTitle
        season = episode.parentTitle
        title = episode.title
        air_date = episode.originallyAvailableAt.strftime("%Y-%m-%d")
        summary = episode.summary
        episode_dict[show][season][title]['Air_Date'] = air_date
        episode_dict[show][season][title]['Summary'] = summary

    return episode_dict

def return_tv(plex, section, days_passed):
    """
    Based on the section given retrieves all recently added media for that
    section and then calls the appropriate format function allowing human
    readable output
    """
    days_elapsed = int(days_passed)
    recently_added = __get_tv(plex, section)

    new_episodes = plex_utils.date_filter(recently_added.episodes, days_elapsed)
    new_seasons = plex_utils.date_filter(recently_added.seasons, days_elapsed)
    new_shows = plex_utils.date_filter(recently_added.shows, days_elapsed)

    new_show_episodes = __get_show_episodes(plex, section, days_elapsed, new_shows)
    new_season_episodes = __get_season_episodes(plex, section, days_elapsed, new_seasons)

    all_episodes = new_episodes + new_show_episodes + new_season_episodes

    return __format_shows(all_episodes)
