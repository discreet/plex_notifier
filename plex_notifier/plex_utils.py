#!/usr/bin/env python3
"""
commonly used functions
"""
import datetime
import itertools

def date_filter(media, days_elapsed):
    """
    filter media by date range
    """
    today = datetime.datetime.now()
    filtered_media = [
        obj for obj in media
        if (today - obj.addedAt).days < days_elapsed
    ]
    return filtered_media

def flatten(list2d):
    """
    flatten nested lists into a single list
    """
    return list(itertools.chain.from_iterable(list2d))
