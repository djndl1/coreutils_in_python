#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import os
from datetime import datetime, date, time
import time
# from dateutil import *

def date(UTC, fmt):
    lc_time_env = os.getenv('LC_TIME')
    tz_env = os.getenv('TZ')

    if UTC:
        tz = 'UTC0'
        utc_offset = timedelta(0)
        daylight = 0
    elif tz_env:
        tz = tz_env
        time.tzset()
        utc_offset =  



    
