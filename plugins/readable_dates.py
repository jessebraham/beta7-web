#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    plugins/readable_dates.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c)2017 by Jesse Braham <jesse@beta7.io>.
    :license: MIT, see LICENSE for more details.
'''

import pendulum

from pelican import signals


def format_time(timestamp):
    '''
    Parse the provided timestamp into a Pendulum object, then return the
    formatted string.

    MMMM - long month      (January)
    Do   - day with suffix (1st)
    YYYY - full year       (1970)
    '''

    date = pendulum.parse(str(timestamp))
    return date.format('MMMM Do, YYYY')


def add_filter(pelican):
    '''
    Add the filter to the global list of filters in the Pelican Environment
    object.
    '''

    pelican.env.filters.update({'human_readable': format_time})


def register():
    '''
    Register the filter to run on the 'generator_init' signal.
    '''

    signals.generator_init.connect(add_filter)
