#!/usr/bin/python3
# -*- coding:utf-8 -*-

# For POSIX standard on this utility,
# see http://pubs.opengroup.org/onlinepubs/9699919799.2018edition/utilities/date.html

import sys, os
import argparse
import time
from datetime import datetime, timedelta, timezone


def get_cur_date(UTC=False):
    lc_time_env = os.getenv('LC_TIME')
    tz_env = os.getenv('TZ')

    if UTC:
        tz_name = 'UTC'
        utc_offset = timedelta(0)
        daylight = False
    elif tz_env:
        time.tzset()
        utc_offset = timedelta(seconds=-time.altzone)
        daylight = time.daylight
        if daylight:
            tz_name = time.tzname[1]
        else:
            tz_name = time.tzname[0]
    else:
        time.tzset()
        utc_offset = timedelta(seconds=-time.altzone)
        daylight = time.daylight
        if daylight:
            tz_name = time.tzname[1]
        else:
            tz_name = time.tzname[0]

    tz = timezone(utc_offset, name=tz_name)
    current_datetime = datetime.now(tz)

    return current_datetime


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
        'Display the current time in the given FORMAT, or set the system date.')
    parser.add_argument('format', action='store', type=str,
                        default='+%a %b %e %H:%M:%S %Z %Y')
    parser.add_argument('-u', action='store_false')
    args = parser.parse_args()
    print(get_cur_date(args.u).strftime(args.format[1:]))

    
