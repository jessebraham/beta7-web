#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
human_readable_dates.py

<<<<<<< HEAD
Jesse Braham <jesse@beta7.io>
August 2017

=======
>>>>>>> e0d043674b2de5a37ba901338b5a42af9e4fe4c5
A simple module to convert timestamps to a human-readable format. Uses the
Arrow module.

https://arrow.readthedocs.io/en/latest/
'''

import arrow

from pelican import signals


def format_time(timestamp):
    '''
    Parse the provided timestamp into an Arrow object, then return the
    formatted string.

    MMMM - long month      (August)
    Do   - day with suffix (1st)
    YYYY - full year       (2017)
    '''

    return arrow.get(timestamp).format('MMMM Do, YYYY')

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
