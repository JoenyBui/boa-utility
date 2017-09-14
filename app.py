#!/usr/bin/python
"""
Usage: utility
    boautil minifier <SOURCE> <DESTINATION>

Arguments:
    SOURCE          Source Folder Directory
    DESTINATION     Destination Folder Directory

"""
import os
import sys

import docopt

import pecutil.run as run

__author__ = 'jbui'


if __name__ == '__main__' and __package__ is None:
    package_name = 'boautil'
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    opt = docopt.docopt(__doc__, sys.argv[1:])

    if opt.get('minifier'):
        src_folder = opt.get('<SOURCE>')
        dest_folder = opt.get('<DESTINATION>')

        if src_folder is not dest_folder:
            run.copy_folder_minify(src_folder, dest_folder)
