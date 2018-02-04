#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    publishconf.py
    ~~~~~~~~~~~~~~

    :copyright: (c)2017 by Jesse Braham <jesse@beta7.io>.
    :license: MIT, see LICENSE for more details.
'''

# Insert the current directory into the system path so that pelicanconf can be
# imported successfully.
import os
import sys

sys.path.insert(0, os.getcwd())


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

RELATIVE_URLS = False


# #############################################################################
#  Feed Configuration
# #############################################################################

FEED_ALL_ATOM = 'feeds/all.atom.xml'
