#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Pelican Production Configuration for beta7.io
'''

# Insert the current directory into the system path so that pelicanconf can be
# imported successfully.
import os
import sys

sys.path.insert(0, os.getcwd())


# Import all configuration from our Development Configuration as a starting
# point, since we will be overriding a few values.
from pelicanconf import *  # pylint: disable=W0401,W0614


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
