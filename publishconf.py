#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    publishconf.py
    ~~~~~~~~~~~~~~

    :copyright: (c)2017 by Jesse Braham <jesse@beta7.io>.
    :license: MIT, see LICENSE for more details.
'''

# Import all configuration from our Development Configuration as a starting
# point, since we will be overriding a few values.
from pelicanconf import *  # NOQA


# #############################################################################
#  Site Information & Metadata
# #############################################################################

SITEURL = 'https://www.beta7.io'


# #############################################################################
#  Site Configuration
# #############################################################################

# In production, do not use relative URLs.
RELATIVE_URLS = False


# #############################################################################
#  Feed Configuration
# #############################################################################

# In production, the Atom 'ALL' feed is enabled.
FEED_ALL_ATOM = 'feeds/all.atom.xml'
