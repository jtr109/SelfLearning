# !/usr/bin/python
# -*- coding: utf-8 -*-

import re

from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_map = re.match(r'^UTC([\+|\-]\d{1,2}):00$', tz_str)
    tz = timezone(timedelta(hours=int(tz_map.group(1))))
    dt_tz = dt.replace(tzinfo=tz)
    return dt_tz.timestamp()

if __name__ == '__main__':
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2

    print('Pass')