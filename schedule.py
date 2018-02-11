#!/usr/bin/env python3
"""
This script is used to configure the cron job necessary to run plex_notifier on
the desired schedule.
"""

import os
from crontab import CronTab

INTERVAL = int(os.environ["PLEX_DAYS_PASSED"]) + 1
CRON = CronTab(user='root')

JOB = CRON.new(command='<path/to/main.py')
JOB.day.every(INTERVAL)
CRON.write()
