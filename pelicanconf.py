#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    pelicanconf.py
    ~~~~~~~~~~~~~~

    Configuration for Pelican, a static site generator. Used to generate
    https://beta7.io/.

    :copyright: (c)2018 by Jesse Braham <jesse@beta7.io>.
    :license: MIT, see LICENSE for more details.
'''


import datetime


# ----------------------------------------------------------------------------
#  Site Information & Metadata
# ----------------------------------------------------------------------------

DEFAULT_LANG = 'en'
TIMEZONE = 'America/Vancouver'

SITENAME = 'Beta7'
SITEURL = ''

AUTHOR = 'Jesse Braham'
GITHUB_USER = 'jessebraham'

DESCRIPTION = 'The personal blog of Jesse Braham. A range of topics, most ' \
              'of which technical in nature. Software development, ' \
              'electronics, engineering and more.'
CURRENT_YEAR = datetime.datetime.utcnow().year


# ----------------------------------------------------------------------------
#  Site Configuration
# ----------------------------------------------------------------------------

# In development, use relative URLs.
RELATIVE_URLS = True

# Links to be displayed in the main navigation; each Tuple contains the Title
# and URL for each navigation item.
LINKS = (
    ('Home',     ''),
    # ('Projects', 'projects.html'),
    ('About',    'about.html'),
)

# We will use whatever folder a post is stored in as its category to keep
# things simple and organized.
USE_FOLDER_AS_CATEGORY = True

# Define the number of articles per page for the paginator.
DEFAULT_PAGINATION = 10

# ?????
# PAGINATION_PATTERNS = (
#     (1, '{base_name}/',
#         '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}/',
#         '{base_name}/page/{number}/index.html'),
# )


# ----------------------------------------------------------------------------
#  File Path Configuration
# ----------------------------------------------------------------------------

# Define the relative path to the content and theme directories.
PATH = './content'
THEME = './beta7-theme'

# Do not create the following pages:
#   - 'author.html', 'authors.html'
#   - 'tag.html', 'tags.html'
#   - 'archives.html'
#   - 'categories.html'
AUTHOR_SAVE_AS = AUTHORS_SAVE_AS = False
TAG_SAVE_AS = TAGS_SAVE_AS = False
ARCHIVES_SAVE_AS = False
CATEGORIES_SAVE_AS = False

# Articles should be stored in folders with the name of the category, and the
# URL should match the pattern
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

# ?????
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'


# ----------------------------------------------------------------------------
#  Feed Configuration
# ----------------------------------------------------------------------------

# For development, all RSS and Atom feeds are disabled.
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# ----------------------------------------------------------------------------
#  Extension Configuration
# ----------------------------------------------------------------------------

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
    },
}


# ----------------------------------------------------------------------------
#  Plugin Configuration
# ----------------------------------------------------------------------------

PLUGIN_PATHS = [
    'pelican-plugins',
]

PLUGINS = [
    'assets',
    # 'gzip_cache',
    'neighbors',
    # 'optimize_images',
    # 'series',
    'sitemap',
]

# Use the default Sitemap settings. The plugin requires at minimum we set the
# format, even though the default value is already 'xml'.
SITEMAP = {
    'format': 'xml',
}
