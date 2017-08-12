#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
image_optimizer.py

Jesse Braham <jesse@beta7.io>
August 2017

A Pelican plugin that optimizes images by re-saving them with a different
quality setting, and additionally creates thumbnails for each image.
'''

import os

import pelican

from PIL import Image


IMAGE_MAX_WIDTH = 800
IMAGE_QUALITY = 80


class ImageOptimizer(object):
    '''
    ImageOptimizer

    Optimize images included in blogposts, and create thumbnails for each.
    '''

    def __init__(self, path, config={}):  # pylint: disable=W0102
        '''
        Initialize the default configuration values, then update the config
        dict with any passed in values.
        '''

        # Start by creating the default config dict. The image source path is
        # a folder named 'images' located directly in the provided path. The
        # image destination path is simply 'output/images'. The default
        # maximum width and image quality values are also set to their
        # respective values.
        self.config = {
            'image_src': os.sep.join([path, 'images']),
            'image_dest': os.sep.join(['output', 'images']),
            'max_width': IMAGE_MAX_WIDTH,
            'quality': IMAGE_QUALITY,
            'output_format': 'PNG'}

        # Update the default config dict, inserting any key-value pairs which
        # are not present, and updating any that are, if necessary.
        self.config.update(config)

    def __full_path_and_name(self, source_path):
        '''
        Given a source path, return the absolute path and filename.
        '''

        # Get the full path to the source file, as well as the file name.
        full_path = os.path.abspath(source_path)
        file_name = os.path.basename(full_path)

        # If the path provided does not exist, or is not a file, raise
        # FileNotFoundError.
        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            raise FileNotFoundError

        # Return a Tuple containing the full path and the file name.
        return (full_path, file_name)

    def __full_dest_path(self, dest_path):
        '''
        Given the destination path, get the absolute path to the specified
        directory, creating it if it does not exist. Return the absolute path.
        '''

        # Get the full path of the destination directory.
        full_dest_path = os.path.abspath(dest_path)

        # If the destination path provided is for some reason a file, strip the
        # file name from the path.
        if os.path.isfile(full_dest_path):
            full_dest_path = os.path.dirname(full_dest_path)

        # If the destination path does not exist, attempt to create it.
        if not os.path.exists(full_dest_path):
            os.makedirs(full_dest_path)

        # Return the full path to the specified location.
        return full_dest_path

    def __compress_image(self, source_path):
        '''
        Give the source path to an image, re-save an optimized version of that
        image in the configured output directory. Additionally, generate a
        thumbnail and save it in the configured directory.
        '''

        # Get the full path to the source file, as well as the file name.
        (full_path, file_name) = self.__full_path_and_name(source_path)

        # Get the full path of the destination directory.
        dest_path = self.config.get('image_dest')
        full_dest_path = self.__full_dest_path(dest_path)


        # Now that we have determined the full path to the image and its file
        # format, create the Image object by opening the full path to the source
        # file.
        image = Image.open(full_path)

        # Save the image to the specified destination directory, using the same
        # file name as provided, in the specified quality.
        file_format = self.config.get('file_format')
        quality = self.config.get('quality')

        image.save(os.path.join(full_dest_path, file_name),
                   format=file_format, quality=quality)


        # Create a thumbnail of the maximum specified dimensions.
        max_thumb_dim = self.config.get('max_width')

        image.thumbnail([max_thumb_dim, max_thumb_dim], Image.ANTIALIAS)

        # The final destination path for the thumbnails will be a directory
        # called 'thumbs', located in the above assigned destination directory.
        full_thumbs_dest_path = self.__full_dest_path(
            os.path.join(full_dest_path, 'thumbs'))

        # Save the thumbnail image.
        image.save(os.path.join(full_thumbs_dest_path, file_name),
                   format=file_format, quality=quality)

    def process(self):
        '''
        For each image in the source directory, re-save it in the specified
        format at the specified quality. Additionally, create a scaled-down
        "thumbnail" version of the image.
        '''

        # Read the source image directory from the configuration dict.
        src = self.config.get('image_src')

        # Iterate through the files in the source directory, and for each image
        # attempt to compress it and create a thumbnail in the specified
        # directories.
        for root, _, files in os.walk(os.path.abspath(src)):
            for file_ in files:
                try:
                    self.__compress_image(os.path.join(root, file_))
                except Exception as e:  #pylint: disable=C0103,W0703
                    print(e)


def run_optimizer(pel):
    '''
    Read the `PATH` and `IMAGE_OPTIMIZER` configuration values from the Pelican
    configuration. Instantiate a new ImageOptimizer object, passing in the
    above values to the constructor. Call the `process` method to run the
    optimizer and create thumbnails.
    '''

    path = pel.settings.get('PATH')
    config = pel.settings.get('IMAGE_OPTIMIZER')

    optimizer = ImageOptimizer(path, config)
    optimizer.process()

def register():
    '''
    Register the filter to run on the 'initialized' signal.
    '''

    pelican.signals.initialized.connect(run_optimizer)
