import os


def find_html_files(pelican):
    """
    Find and return all HTML files within the configured output directory.

    :param pelican: the Pelican instance
    """
    matching_files = []
    for root, _, files in os.walk(pelican.settings["OUTPUT_PATH"]):
        matching_files += [
            os.path.join(root, name) for name in files if name.endswith(".html")
        ]

    return matching_files
