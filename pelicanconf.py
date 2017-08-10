#!/usr/bin/env python
# -*- coding: utf-8 -*- #
'''
Development Configuration
'''


# #############################################################################
#  Metadata
# #############################################################################

SITENAME = 'Beta7'
SITEURL = ''

AUTHOR = 'Jesse Braham'
COPYRIGHT = 'Jesse Braham'
DESCRIPTION = ''
SITE_HEADER_TITLE = 'Go away'
GITHUB_USER = 'jessebraham'

TIMEZONE = 'America/Vancouver'
DEFAULT_LANG = 'English'
HTML_LANG = 'en'

MENU_ITEMS = (('Home', ''),
              ('Archives', 'archives.html'),
              ('Categories', 'categories.html'),)


# #############################################################################
#  Configuration
# #############################################################################

PATH = 'content'
THEME = 'beta7-theme'

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 32

RELATIVE_URLS = True

# We will use whatever folder a post is stored in as its category to keep
# things simple and organized.
USE_FOLDER_AS_CATEGORY = True

# Articles should be stored in folders with the name of the category, and the
# URL should match the pattern
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

# Pages should be stored in a 'pages' folder, and the URL should match the
# pattern
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# Do not create the 'author.html', 'authors.html' and 'tag.html' pages.
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
TAG_SAVE_AS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# #############################################################################
#  Plugins, Filters and other Add-Ons
# #############################################################################

PLUGIN_PATHS = [
    'pelican-plugins',
    'plugins',
]

PLUGINS = [
    'assets',
    'human_readable_dates',
    'sitemap',
]

MARKDOWN = {
    'extension_configs': {
        'extensions.luminous': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.tables': {},
        'markdown.extensions.toc': {},
    },
}

SITEMAP = {
    'format': 'xml',
}
