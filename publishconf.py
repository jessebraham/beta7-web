#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Pelican Production Configuration for beta7.io
'''


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

DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = False


# #############################################################################
#  Feed Configuration
# #############################################################################

FEED_ALL_ATOM = 'feeds/all.atom.xml'
