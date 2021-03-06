#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""
This file is only used if you use `make publish` or explicitly specify it as
your config file. It is intended to configure the site for use in production.
"""

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # NOQA


# If your site is available via HTTPS, make sure SITEURL begins with https://

SITEURL = "https://beta7.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"

MINIFY = {"enabled": True}
STYLESHEET_HASHES = {"enabled": True, "manifest": "theme/manifest.json"}
