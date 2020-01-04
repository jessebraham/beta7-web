#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""
Pelican configuration for https://beta7.io. Any values that need to be changed
in production should be set in `publishconf.py`.
"""


# General Site Configuration

AUTHOR = "Jesse Braham"
SITENAME = "Beta7"
SITEURL = ""

DEFAULT_LANG = "en"
TIMEZONE = "America/Vancouver"

PATH = "content"
THEME = "theme"


# Meta Description & Social

DESCRIPTION = (
    "The personal blog of Jesse Braham. Consists of mostly technical topics "
    "including software development, electronics, and science/mathematics."
)

SOCIAL = {
    "email": "jesse@beta7.io",
    "github": "jessebraham",
    "linkedin": "jessebraham",
}


# Feed Generation (usually not desired when developing)

FEED_ALL_ATOM = ""

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Static Files

STATIC_PATHS = ["extra", "images"]

EXTRA_PATH_METADATA = {
    "extra/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extra/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extra/robots.txt": {"path": "robots.txt"},
}


# Extensions

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}


# Plugins

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "header_ids",
    "html_minifier",
    "pelican_javascript",
    "series",
    "sitemap",
    "stylesheet_hashes",
]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    },
}


# Miscellaneous Configuration (generally not to be fiddled with)

DEFAULT_PAGINATION = 8

DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = True
USE_FOLDER_AS_CATEGORY = True

ARCHIVES_SAVE_AS = ""
AUTHOR_SAVE_AS = AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = TAGS_SAVE_AS = ""

ARTICLE_SAVE_AS = ARTICLE_URL = "{category}/{slug}.html"
PAGE_SAVE_AS = PAGE_URL = "{slug}.html"

CATEGORY_REGEX_SUBSTITUTIONS = [("blog posts", "posts")]
