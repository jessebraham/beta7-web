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


# Meta Description, Profile & Social

DESCRIPTION = ""  # 150 chars or less

PROFILE = (
    (
        "Systems Developer residing in Kelowna, BC, Canada. Proficient in "
        "Python, C, JavaScript, Rust, .NET, and some others."
    ),
    (
        "Interests include networking & security, automation, engineering & "
        "manufacturing, comic books, and physics. Occassionally tinker with "
        "electronics and other hardware."
    ),
)

SOCIAL = {
    "email": "jesse@beta7.io",
    "github": "jessebraham",
    "linkedin": "jesse-braham-24938a4a",
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
    "extra/favicon.ico": {"path": "favicon.ico"},
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
PLUGINS = ["html_minifier", "sitemap", "stylesheet_hashes"]

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

DEFAULT_PAGINATION = 10
NUM_PREVIEW_LINKS = 3

DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = True
USE_FOLDER_AS_CATEGORY = True

ARCHIVES_SAVE_AS = ""
AUTHOR_SAVE_AS = AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = TAGS_SAVE_AS = ""

ARTICLE_SAVE_AS = ARTICLE_URL = "{category}/{slug}.html"
CATEGORY_SAVE_AS = CATEGORY_URL = "{slug}.html"

CATEGORY_REGEX_SUBSTITUTIONS = [("blog posts", "posts")]
