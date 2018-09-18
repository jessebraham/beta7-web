#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    pelicanconf.py
    ~~~~~~~~~~~~~~

    Configuration for Pelican, a static site generator written in Python.
    Used to generate https://beta7.io/.

        https://github.com/jessebraham/beta7-theme

    :author: Jesse Braham <jesse@beta7.io>.
'''

# ----------------------------------------------------------------------------
# Language & Regional Settings
# ----------------------------------------------------------------------------

DEFAULT_LANG = 'en'
LOCALE = 'en_US'

TIMEZONE = 'America/Vancouver'


# ----------------------------------------------------------------------------
# Site Information
# ----------------------------------------------------------------------------

SITENAME = 'Beta7'
SITEURL = ''  # Set value in `publishconf.py` for Production

AUTHOR = 'Jesse Braham'
DESCRIPTION = ''  # TODO: write me


# ----------------------------------------------------------------------------
# Social Settings
# ----------------------------------------------------------------------------

SOCIAL = (
    ('at-sign', 'mailto:jesse@beta7.io', 'E-mail Jesse Braham'),
    ('github', 'https://github.com/jessebraham', 'jessebraham on Github'),
    ('gitlab', 'https://gitlab.com/jessebraham', 'jessebraham on GitLab'),
    ('linkedin', 'https://www.linkedin.com/in/jesse-braham-24938a4a/',
     'Jesse Braham on LinkedIn'),
)


# ----------------------------------------------------------------------------
# Feed Settings
# ----------------------------------------------------------------------------

AUTHOR_FEED_ATOM = None
CATEGORY_FEED_ATOM = None
FEED_ATOM = None
FEED_ALL_ATOM = None
TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# ----------------------------------------------------------------------------
# Theme Settings
# ----------------------------------------------------------------------------

PATH = './content'
THEME = './beta7-theme'

RELATIVE_URLS = True
USE_FOLDER_AS_CATEGORY = True

AUTHOR_SAVE_AS = AUTHORS_SAVE_AS = False
TAG_SAVE_AS = TAGS_SAVE_AS = False
CATEGORIES_SAVE_AS = False

ARTICLE_SAVE_AS = ARTICLE_URL = '{category}/{slug}.html'
PAGE_SAVE_AS = PAGE_URL = '{slug}.html'

DEFAULT_PAGINATION = 10


# ----------------------------------------------------------------------------
# Extension & Plugin Settings
# ----------------------------------------------------------------------------

MARKDOWN = {
    'extension_configs': {
        'codehilite': {},
        'markdown.extensions.extra': {},
    },
}

PLUGIN_PATHS = [
    'pelican-plugins',
    'plugins',
]

PLUGINS = [
    'sitemap',
    'svg_inliner',
]

SITEMAP = {
    'format': 'xml',
}
