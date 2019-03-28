#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from bs4 import BeautifulSoup
from pelican import signals

from plugins import list_files


def add_header_ids(pelican):
    """
    Find all headers (h1-h6) within elements with the "post" class, and set
    their `id` attributes to a slugified version of the header text.

    Checks for a `HEADER_IDS` configuration entry in the Pelican settings,
    which in turn should contain an `enabled` flag value. If the configuration
    is not provided, the plugin defaults to enabled.

    :param pelican: The Pelican instance.
    """
    options = pelican.settings.get("HEADER_IDS", {})
    enabled = options.get("enabled", True)
    if not enabled:
        return

    html_files = list_files(pelican.settings["OUTPUT_PATH"], ".html")
    for filename in html_files:
        with open(filename, "r") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        post = soup.find(attrs={"class": "post"})
        if not post:
            continue

        headers = post.find_all(re.compile("^h[1-6]$"))
        for header in headers:
            # If the header's class list contains 'title' or 'subtitle', skip
            # it.
            if set(header.get("class", [])) & {"title", "subtitle"}:
                continue
            header["id"] = slugify(header.text)

        with open(filename, "w") as f:
            f.write(str(soup))


def slugify(text):
    """
    Remove any invalid characters from the text, de-duplicate spaces, and then
    replace any remaining spaces with dashes. Return the resulting string.

    :param str text: The text in which to slugify.

    :return str: The resulting slug.
    """
    slug = re.sub(r"[^a-z0-9\s\-]", "", text.lower())
    slug = re.sub(r"\s+", " ", slug)
    slug = re.sub(r"\s", "-", slug.strip())

    return slug


def register():
    """
    Find all occurrances of header elements (h1-h6) within `.post` elements,
    and add an "id" attribute consisting of the slug of the header's text.
    """
    signals.finalized.connect(add_header_ids)
