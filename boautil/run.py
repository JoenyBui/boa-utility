import os
import subprocess
import shutil
import fnmatch

from . import SETTING
from .folder import copy_tree

__author__ = 'joeny'


def run_app_file(script_list):
    """
    Run scripto file.

    :param script_list:
    :return:
    """
    if os.name == 'nt':
        script_list.insert(0, SETTING['anaconda'])

        subprocess.call(script_list)
    else:
        subprocess.call(script_list)


def minify_folder(directory):
    """
    Minify complete folder

    :param directory:
    :return:
    """
    for file in directory:
        # Output folder and output file
        ofolder, ofile = os.path.split(file)

        outfile = os.path.join(ofolder, 'min_' + ofile)

        # Minify file
        minify_file(file, outfile)


def minify_file(srcfile, outfile):
    """
    Minify file

    :param srcfile:
    :param outfile:
    :return:
    """
    env = os.environ.copy()

    subprocess.call(
        [SETTING['pyminifier'], srcfile, '>',  '%s' % (outfile)],
        env=env,
        shell=True
    )


def copy_folder_minify(source, destination, symlinks=False, ignore=None):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)

        if os.path.isdir(s):
            copy_folder_minify(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                if s.lower().endswith('.py'):
                    minify_file(s, d)
