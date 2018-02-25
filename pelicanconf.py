#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    pelicanconf.py
    ~~~~~~~~~~~~~~

    :copyright: (c)2017 by Jesse Braham <jesse@beta7.io>.
    :license: MIT, see LICENSE for more details.
'''


# #############################################################################
#  Site Information & Metadata
# #############################################################################

DEFAULT_LANG = 'en'
TIMEZONE = 'America/Vancouver'

SITENAME = 'Beta7'
SITEURL = ''

AUTHOR = 'Jesse Braham'
GITHUB_USER = 'jessebraham'

DESCRIPTION = 'The personal blog of Jesse Braham. A range of topics, most ' \
              'of which technical in nature. Software development, ' \
              'electronics, engineering and more.'


# #############################################################################
#  Site Configuration
# #############################################################################

# Define the number of articles per page (if pagination is enabled).
DEFAULT_PAGINATION = 8

# For development, use relative URLs.
RELATIVE_URLS = True

# We will use whatever folder a post is stored in as its category to keep
# things simple and organized.
USE_FOLDER_AS_CATEGORY = True


# #############################################################################
#  File Path Configuration
# #############################################################################

# Define the relative path to the content and theme directories.
PATH = './content'
THEME = './beta7-theme'

# Do not create the 'author.html', 'authors.html', 'tag.html' and 'tags.html'
# pages.
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
TAG_SAVE_AS = False
TAGS_SAVE_AS = False

# Do not create the 'archives.html' page.
ARCHIVES_SAVE_AS = False

# Do not create the 'categories.html' or specific category pages.
CATEGORY_SAVE_AS = False
CATEGORIES_SAVE_AS = False

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

# For development, all RSS and Atom feeds are disabled.
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
    'gzip_cache',
    'neighbors',
    'optimize_images',
    'pelican-ert',
    'readable_dates',
    'series',
    'sitemap',
]

# Use the default Sitemap settings. The plugin requires at minimum we set the
# format, even though the default value is already 'xml'.
SITEMAP = {
    'format': 'xml',
}

# Configure the Estimated Reading Time plugin. Set the "Words Per Minute" and
# "Format" configuration variables to reasonable values.
ERT_WPM = 220
ERT_FORMAT = '{time}'
