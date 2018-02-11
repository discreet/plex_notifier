#!/usr/bin/env python3
"""
commonly used functions
"""
import datetime
import itertools
import getpass
from crontab import CronTab


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


def schedule(program, interval):
    """
    creates cron job to run program on a schedule
    """
    interval = int(interval) + 1
    cron = CronTab(user=getpass.getuser())
    job = cron.new(command=program, comment="plex_notifier")
    job.day.every(interval)
    cron.write()


def cancel():
    """
    removes the previously created cron job
    """
    cron = CronTab(user=getpass.getuser())
    for job in cron:
        if job.comment == 'plex_notifier':
            cron.remove(job)
            cron.write()
