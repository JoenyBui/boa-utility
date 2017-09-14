import os
import sys
import subprocess


def open_file(filepath):
    """
    Open file

    :param filepath:
    :return:
    """
    if sys.platform.startswith('linux2'):
        subprocess.call(["xdg-open", filepath])
    else:
        os.startfile(filepath)
