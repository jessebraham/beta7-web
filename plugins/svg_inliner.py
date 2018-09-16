#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    svg_inliner
    ~~~~~~~~~~~

    Scan all generated HTML files for occurances of <img> tags, and replace
    them with the contents of the SVG files specified by their 'src'
    attributes.

    :author: Jesse Braham <jesse@beta7.io>
    :date:   September, 2018
'''

import os

from bs4 import BeautifulSoup
from pelican import signals


# Combine the theme's static path with the path provided by the image's `src`
# attribute.
def static_path(theme_path, image_path):
    img_path = os.path.join(*(image_path.split(os.sep)[2:]))
    return os.path.join(theme_path, 'static', img_path)


def inline_svgs(path, context):
    # Read all text from `path`, passing it to the `BeautifulSoup` constructor.
    with open(path, 'r') as f:
        soup = BeautifulSoup(f.read(), features='html.parser')

    # Find all `<img>` tags within the document; read the contents of the file
    # pointed to by their `src` attributes, and replace the `<img>` tags with
    # `<svg>` tags.
    for img in soup.findAll('img'):
        (_, ext) = os.path.splitext(img['src'])

        # Ignore any raster images.
        if ext != '.svg':
            continue

        with open(static_path(context['THEME'], img['src']), 'r') as f:
            svg = BeautifulSoup(f.read(), features='html.parser')

        img.replace_with(svg)

    # Write out the changes to `path`.
    with open(path, 'w') as f:
        f.write(str(soup))


def register():
    # The `content_written` signal is invoked each time a content file is
    # written; when this happens, call the `inline_svg` function defined above.
    signals.content_written.connect(inline_svgs)
