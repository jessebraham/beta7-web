#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    publishconf.py
    ~~~~~~~~~~~~~~

    Configuration for Pelican, a static site generator written in Python.
    Used to generate https://beta7.io/.

        https://github.com/jessebraham/beta7-theme

    :author: Jesse Braham <jesse@beta7.io>.
'''

# Insert the current directory into the system path so that pelicanconf can be
# imported successfully.
import os
import sys

sys.path.insert(0, os.getcwd())


# Import all configuration from our Development Configuration as a starting
# point, since we will be overriding a few values.
from pelicanconf import *  # NOQA


# ----------------------------------------------------------------------------
# Site Information
# ----------------------------------------------------------------------------

SITEURL = 'https://beta7.io'


# ----------------------------------------------------------------------------
# Feed Settings
# ----------------------------------------------------------------------------

# AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
