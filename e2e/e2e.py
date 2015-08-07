#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

def change_time(time):
    time_in_minute = 0
    time_list = time.split(" ")
    if len(a) == 4:
        time_in_minute = int(time_list[0])*60 + int(time_list[2])
    if len(time_list) == 2:
        if a[1] == "hours":
            time_in_minute = int(time_list[0])*60
        if a[1] == "minutes":
            time_in_minute = int(tim_list[0])
    return time_in_minute

def compare_time(time_start, time_end):
    crash_begin = datetime.datetime.strptime(time_start, "%d.%m.%Y %H:%M:%S")
    crash_close = datetime.datetime.strptime(time_end, "%d.%m.%Y %H:%M:%S")
    crash_close_compare = datetime.datetime.strptime(time_start[:10] + time_end[10:], "%d.%m.%Y %H:%M:%S")
    business_start = datetime.datetime.strptime(time_start[:10] + " 8:00:00", "%d.%m.%Y %H:%M:%S")
    business_end = datetime.datetime.strptime(time_start[:10] + " 23:00:00", "%d.%m.%Y %H:%M:%S")
    time_in_business_time = 0
    time_not_in_business_time = 0
    day_business = 900
    if crash_begin < business_start:
        if crash_close_compare < business_start:
            time_not_in_business_time += (crash_close_compare - crash_begin).seconds / 60
        if crash_close >= business_start:
            if crash_close < business_end:
                time_not_in_business_time += (business_start - crash_begin).seconds / 60
                time_in_business_time += (crash_close_compare - business_start).seconds / 60
            if crash_close >= business_end:
                time_not_in_business_time += (business_start - crash_begin).seconds / 60 + (crash_close_compare - business_end) / 60
                time_in_business_time += day_business
    if crash_begin >= business_start:
        if crash_begin < business_end:
            if crash_close_compare < business_end:
                time_in_business_time += (crash_close_compare - crash_begin).seconds / 60
            if crash_close_compare >= business_end:
                time_in_business_time += (business_end - crash_begin).seconds / 60
                time_not_in_business_time += (crash_close_compare - business_end).seconds / 60
    if crash_begin >= business_end:
        time_not_in_business_time += (crash_close_compare - crash_begin).seconds / 60
    return time_in_business_time, time_not_in_business_time


def time_period(time_start, time_end):
    crash_begin = datetime.datetime.strptime(time_start, "%d.%m.%Y %H:%M:%S")
    crash_close = datetime.datetime.strptime(time_end, "%d.%m.%Y %H:%M:%S")
    crash_close_compare = datetime.datetime.strptime(time_start[:10] + time_end[10:], "%d.%m.%Y %H:%M:%S")
    time_end_compare = time_start[:10] + time_end[10:]
    after_midnight = time_start[:10] + " 00:00:00"
    midnight = time_start[:10] + " 23:59:00"
    time_in_business_time = 0
    time_not_in_business_time = 0
    day_business = 900
    day_not_in_business = 540
    crash_time = crash_close - crash_begin
    if crash_begin <= crash_close_compare:
        time = compare_time(time_start, time_end)
        if crash_time.days > 0:

            time_in_business_time += day_business * crash_time.days + time[0]
            time_not_in_business_time += day_not_in_business * crash_time.days + time[1]

        if crash_time.days == 0:
            time_in_business_time += time[0]
            time_not_in_business_time += time[1]

    if crash_begin > crash_close_compare:
        time_after_midnight = compare_time(after_midnight, time_end_compare)
        time_midnight = compare_time(time_start, midnight)
        if crash_time.days > 0:
            time_in_business_time += day_business * crash_time.days + time_after_midnight[0] + time_midnight[0]
            time_not_in_business_time += day_not_in_business * crash_time.days + time_after_midnight[1] + time_midnight[1] + 1

        if crash_time.days == 0:
            time_in_business_time += time_after_midnight[0] + time_midnight[0]
            time_not_in_business_time += time_after_midnight[1] + time_midnight[1] + 1
    time_all = time_in_business_time + time_not_in_business_time

    return time_in_business_time, time_not_in_business_time, time_all


c = time_period("02.06.2015 21:00:00", "09.06.2015 21:00:00")
print c
c = time_period("02.06.2015 23:59:00", "03.06.2015 00:01:00")
print c
c = time_period("02.06.2015 07:59:00", "02.06.2015 08:01:00")
print c
c = time_period("02.06.2015 22:59:00", "02.06.2015 23:01:00")
print c


