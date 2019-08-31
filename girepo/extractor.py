#!/usr/bin/env python
from datetime import datetime
from collections import OrderedDict


def calculate_star_per(created_at, updated_at, star_count, day_duration=1, round_n=2):
    """

    :param created_at: e.g. 2014-09-18T16:12:01Z
    :param updated_at: e.g. 2014-09-19T16:12:01Z
    :param star_count:
    :param day_duration: if 1, it means per day. if 7, it means per week.
    :param round_n:
    :return:  day_duration * start / (days + 1)
    """
    created_at_tz = created_at.replace('Z', '+00:00')
    updated_at_tz = updated_at.replace('Z', '+00:00')
    delta = datetime.fromisoformat(updated_at_tz) - datetime.fromisoformat(created_at_tz)
    offset_for_zero_division = 1
    return day_duration * round(star_count / (delta.days + offset_for_zero_division), round_n)


def date_format(name):
    return lambda x: x[name].split('T')[0]


default_mapper = OrderedDict([
    ('owner', lambda x: x['owner']['login']),
    ('name', lambda x: x['name']),
    ('star', lambda x: x['stargazers_count']),
    ('star/day', lambda x: calculate_star_per(
        x['created_at'], x['updated_at'], x['stargazers_count'], day_duration=1)
     ),
    ('created_at', date_format('created_at')),
    ('updated_at', date_format('updated_at')),
    ('license', lambda x: x['license']['name']),
    ('language', lambda x: x['language']),
    ('description', lambda x: x['description']),
    ('url', lambda x: x['html_url']),
])


def extract(data, mapper):
    return [func(data) for _, func in mapper.items()]
