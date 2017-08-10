#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
luminous.py

Jesse Braham <jesse@beta7.io>
August 2017

A Markdown extension to convert images into figure-wrapped images, including
captions, which use the Luminous lightbox library.

https://github.com/imgix/luminous


Based heavily on the 'figureAltCaption' extension by jdittrich.

https://github.com/jdittrich/figureAltCaption
'''

import re

from markdown import Extension
from markdown.blockprocessors import BlockProcessor
from markdown.inlinepatterns import IMAGE_LINK_RE, IMAGE_REFERENCE_RE
from markdown.util import etree


FIGURES = [r'^\s*' + IMAGE_LINK_RE + r'\s*$',
           r'^\s*' + IMAGE_REFERENCE_RE + r'\s*$']


class LuminousProcessor(BlockProcessor):
    '''
    LuminousProcessor

    Find images within the Markdown, and create the appropriate HTML elements
    to make a responsive, lightboxed image.
    '''

    FIGURES_RE = re.compile('|'.join(f for f in FIGURES))
    SOURCE_RE = re.compile(r'\((.*)\).*$')

    def test(self, parent, block):
        '''
        Determine whether or not the current block is an image, and if it is,
        whether or not it is already nested within a <figure> element.
        '''

        # Determine whether the block in question is indeed an image.
        is_image = bool(self.FIGURES_RE.search(block))

        # Verify that the block is only a single line.
        is_only_one_line = (len(block.splitlines()) == 1)

        # Determine whether or not the image tag is nested within a figure.
        is_in_figure = (parent.tag == 'figure')


        return is_image and is_only_one_line and not is_in_figure

    def run(self, parent, blocks):
        '''
        For each image found, create the appropriate HTML hierarchy, setting
        the appropriate attributes and properties as we go.
        Rather than just an <img> tag, we will next an <img> and <figcaption>
        within a <figure> tag, setting the 'luminous-image' class so that we
        can create a lightbox trigger.
        '''

        # Pop the first block off of the Blocks stack, and store a reference
        # to it. Using the FIGURES_RE and SOURCE_RE regular expressions,
        # extract the caption text and image source from the Markdown tag.
        raw_block = blocks.pop(0)
        caption_text = self.FIGURES_RE.search(raw_block).group(1)
        image_source = self.SOURCE_RE.search(raw_block).group(1)

        # Create the <figure> element, setting its parent as whatever was
        # provided by the `parent` parameter.
        figure = etree.SubElement(parent, 'figure')

        # Create an <a> tag, setting its parent as the above created figure.
        # Set the anchor's `href` attribute to the image's source, and its
        # class to `luminous-image`.
        anchor = etree.SubElement(figure, 'a')
        anchor.set('href', image_source)
        anchor.set('class', 'luminous-image')

        # Set the anchor's text as the raw block we parsed at the beginning of
        # the function, which in turns adds our image.
        anchor.text = raw_block

        # Create the <figcaption> element, setting its parent as the above
        # created figure.
        figcaption_elem = etree.SubElement(figure, 'figcaption')

        # Set the <figcaption> element's text as the caption text parsed from
        # the block, which is the same as the `alt` attribute.
        figcaption_elem.text = caption_text


class LuminousExtension(Extension):
    '''
    LuminousExtension
    '''

    def extendMarkdown(self, md, md_globals):
        '''
        Add an instance of LuminousProcessor to BlockParser.
        '''

        md.parser.blockprocessors.add('luminous',
                                      LuminousProcessor(md.parser),
                                      '<ulist')


def makeExtension(configs={}):  # pylint: disable=C0103,W0102
    '''
    Create the extension, optionally passing in any configuration provided.
    '''

    return LuminousExtension(configs=configs)
