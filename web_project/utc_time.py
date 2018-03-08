# -*- coding:utf-8 -*-
import time

import arrow

from daisy.utils import datetimeutil
from functools import partial
import pytz

from dateutil import tz
from dateutil.tz import tzlocal
from datetime import datetime

utc = pytz.utc

PRC_TZ_STR = 'Asia/Shanghai'
prc = pytz.timezone(PRC_TZ_STR)

now = arrow.now

utcnow = arrow.utcnow

prc_tz = 'prc'


def prcnow():
    utcnow().to(prc_tz)


def prctoday():
    return prcnow().date()


def span_range(start, end, frame, tz=None):
    return arrow.Arrow.span_range(frame, start, end, tz=tz)

def time_range(start, end, frame, tz=None):
    return arrow.Arrow.range(frame, start, end, tz=tz)


span_range_by_minute = partial(span_range, frame='minute')
span_range_by_hour = partial(span_range, frame='hour')
span_range_by_day = partial(span_range, frame='day')

prc_span_range_by_minute = partial(span_range, frame='minute', tz=prc_tz)
prc_span_range_by_hour = partial(span_range, frame='hour', tz=prc_tz)
prc_span_range_by_day = partial(span_range, frame='day', tz=prc_tz)

prc_range_by_minute = partial(time_range, frame='minute', tz=prc_tz)
prc_range_by_hour = partial(time_range, frame='hour', tz=prc_tz)
prc_range_by_day = partial(time_range, frame='day', tz=prc_tz)


def utc_today_int():
    return int(arrow.utcnow().format('%Y%m%d'))


def prc_today_int():
    return int(prcnow().format('%Y%m%d'))


def utc_from_today_int(date_int):
    return arrow.Arrow.strptime(str(date_int), '%Y%m%d')


def prc_from_today_int(date_int):
    return arrow.Arrow.strptime(str(date_int), '%Y%m%d', tzinfo=prc_tz)


def timestamp(is_float=False):
    if is_float:
        return arrow.utcnow().float_timestamp
    else:
        return arrow.utcnow().timestamp


def utc_from_timestamp(ts):
    return arrow.Arrow.utcfromtimestamp(ts)


def prc_from_timestamp(ts):
    return arrow.Arrow.fromtimestamp(ts, prc_tz)


def format_iso8601(d):
    return arrow.Arrow.fromdatetime(d).isoformat()


def from_iso8601(s):
    return arrow.get(s).naive


def format_date_int(d):
    a = arrow.get(d)
    return int(a.strftime('%Y%m%d'))


def format_data_str(s):
    if not s:
        return ''
    print s,"101"
    rn = s.split('T')
    start_date = rn[0]
    end_date = rn[1][:8]
    ret = datetimeutil.parse_utc_from_str('{0} {1}'.format(start_date, end_date), 'UTC')
    ret = datetimeutil.format_prc(ret)
    return ret

def format_date_timestamp(s):
    if not s:
        return ''
    rn = s.split('T')
    start_date = rn[0]
    end_date = rn[1][:8]
    ret = datetimeutil.parse_utc_from_str('{0} {1}'.format(start_date, end_date), 'UTC')
    ret = datetimeutil.utc2timestamp(ret)
    return ret


def sjc_zfc(formula="%Y-%m-%d %H:%M:%S", sjc=time.time()):
    return time.strftime(formula, time.localtime(sjc))


print datetime.now(tzlocal()).tzname()


def utc_prc(utc_date):
    from_zone = tz.gettz('UTC')
    utc = utc_date
    utc = utc.replace(tzinfo=from_zone)
    to_zone = tz.gettz('CST')
    return utc.astimezone(to_zone)
