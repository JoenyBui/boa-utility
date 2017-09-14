import os
import re
import fnmatch
import shutil

from tempfile import TemporaryFile, tempdir

from functools import reduce

__author__ = 'joeny'


def add_escape_clause(value):
    """
    Add escape clause

    :param value:
    :return:
    """
    new_string = []
    for j in value:
        new_string.append(j)

        if j in ["\\"]:
            new_string.append("\\")

    return "".join(new_string)


def split_folder_path(filename):
    """
    Split folder path

    :param filename:
    :return:
    """
    if os.path.isabs(filename):
        filepath = filename
        filename = os.path.split(filepath)[1]
        root_folder = os.path.split(filepath)[0]
    else:
        filepath = os.path.join(os.getcwd(), filename)
        root_folder = os.getcwd()

    return root_folder, filepath, filename


def check_folder(path):
    """
    Check if folder exists, if folder doesn't exist then we create it.

    :param path:
    :return:
    """

    try:
        if not os.path.isdir(path):
            os.mkdir(path)
    except IOError:
        return 0
    finally:
        return 1


def check_filename(filename):
    """
    Check if the filename.

    :param filename:
    :return:
    """
    folder, file = os.path.split(filename)

    return check_folder(folder)


def get_path_file_folder(folder_path, folder_name, file_name, **kwargs):
    """
    Get path file folder

    :param folder_path:
    :param folder_name:
    :param file_name:
    :param kwargs:
    :return:
    """
    output_folders = []
    output_files = []

    if kwargs.get('--folder'):
        output_folders.append(kwargs.get('--folder'))
    else:
        output_folders.append(os.path.join(folder_path, folder_name))

    if kwargs.get('--path'):
        output_files.append(kwargs.get('--path'))
    else:
        output_files.append(os.path.join(output_folders[-1], file_name))

    return output_folders, output_files


def get_new_file_name(file_path, file_name):
    """
    Get the next available file_name by indexing the increment.

    :param file_path:
    :param file_name:
    :return:
    """

    def join_path(path, file_name, file_ext):
        return os.path.join(path, file_name + file_ext)

    save_file_name, save_file_ext = os.path.splitext(file_name)

    if os.path.exists(os.path.join(file_path, file_name)):
        i = 1

        name = save_file_name
        while os.path.exists(join_path(file_path, save_file_name, save_file_ext)):
            save_file_name = '%s_%s' % (name, i)
            i += 1

    return join_path(file_path, save_file_name, save_file_ext)


def get_file(file):
    """
    Get the file path.

    :param file:
    :return:
    """
    if file:
        if os.path.isfile(file):
            return file
        else:
            if os.path.isfile(os.path.join(os.getcwd(), file)):
                return os.path.join(os.getcwd(), file)
            else:
                return None
    else:
        return None


def get_directory_structure(root):
    """
    Creates a nested dictionary that represents the folder structure of rootdir

    :param root: root directory
    :return:
    """
    dir = {}
    root = root.rstrip(os.sep)
    start = root.rfind(os.sep) + 1

    for path, dirs, files in os.walk(root):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir

    return dir


def get_directory_list(root):
    """
    Get a directory list

    :param root:
    :return:
    """
    dir_list = []
    for dirName, subdirList, fileList in os.walk(root):
        print('Found directory: %s' % dirName)

        for fname in fileList:
            print('\t%s' % fname)
            dir_list.append(os.path.join(dirName, fname))

    return dir_list


def copy_tree(source, destination, symlinks=False, ignore=None, pattern=None):
    """
    Copy tree directory

    :param source: source folder
    :param destination: destination folder
    :param symlinks:
    :param ignore:
    :return:
    """
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)

        if os.path.isdir(s):
            copy_tree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                if pattern is None:
                    shutil.copy2(s, d)
                else:
                    if fnmatch.fnmatch(s, pattern):
                        shutil.copy2(s, d)
