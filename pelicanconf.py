#!/usr/bin/env python
# -*- coding: utf-8 -*- #
'''
Development Configuration for Pelican
'''


# #############################################################################
#  Site Information & Metadata
# #############################################################################

SITENAME = 'Beta7'
SITEURL = ''

AUTHOR = 'Jesse Braham'
COPYRIGHT = 'Jesse Braham'

SITE_HEADER_TITLE = 'Go away'
DESCRIPTION = 'Adventures in software development, system administration, ' \
              + ' networking, engineering and more. Viewer discretion is ' \
              + 'advised.'

DEFAULT_LANG = 'en'
TIMEZONE = 'America/Vancouver'
GITHUB_URL = 'https://github.com/jessebraham'


# #############################################################################
#  Site Configuration
# #############################################################################

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 32

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

# We will use whatever folder a post is stored in as its category to keep
# things simple and organized.
USE_FOLDER_AS_CATEGORY = True

# Items to display in the main navigation, with their respective URLs.
MENU_ITEMS = (('Home', ''),
              ('Archives', 'archives.html'),
              ('Categories', 'categories.html'),)


# #############################################################################
#  File Path Configuration
# #############################################################################

PATH = './content'
THEME = './beta7-theme'

# Copy any extra required files to the output directory.
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/robots.txt': {'path': 'robots.txt'},}

# Do not create the 'author.html', 'authors.html' and 'tag.html' pages.
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
TAG_SAVE_AS = False

# Articles should be stored in folders with the name of the category, and the
# URL should match the pattern
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

# Pages should be stored in a 'pages' folder, and the URL should match the
# pattern
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'


# #############################################################################
#  Feed Configuration
# #############################################################################

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# #############################################################################
#  Extension Configuration
# #############################################################################

MARKDOWN = {
    'extension_configs': {
        'extensions.luminous': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.tables': {},
        'markdown.extensions.toc': {},
    },
}


# #############################################################################
#  Plugin Configuration
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

SITEMAP = {
    'format': 'xml',
}
