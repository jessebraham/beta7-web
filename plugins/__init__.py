# -*- coding: utf-8 -*-

import os


def list_files(directory, extension):
    """
    Given a directory, recursively search for all files contained within it
    whose extension matches the provided paramater of the same name.

    :param str directory: The directory to walk.
    :param str extension: The file extension to search for.
    """
    matching_files = []

    for root, _, files in os.walk(directory):
        matching_files += [
            os.path.join(root, name)
            for name in files
            if name.endswith(extension)
        ]

    return matching_files
