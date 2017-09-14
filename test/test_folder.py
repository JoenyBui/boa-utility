import os
from unittest import TestCase

from boautil.folder import copy_tree, get_directory_list
from boautil.run import copy_folder_minify

__author__ = 'joeny'


class TestFolder(TestCase):

    def setUp(self):
        self.test_folder = os.path.dirname(__file__)
        self.project_folder = os.path.split(self.test_folder)[0]

    def test_temp_folder(self):
        source_folder = os.path.join(self.project_folder, 'boautil')
        destination_folder = os.path.join(self.test_folder, 'tmp')

        # Copy Source Folder
        copy_tree(source_folder, destination_folder, pattern='*.py')
        self.assertTrue(os.path.isdir(destination_folder))

    def test_minify_folder(self):
        source_folder = os.path.join(self.project_folder, 'boautil')
        destination_folder = os.path.join(self.test_folder, 'min', 'boautil')

        copy_folder_minify(source_folder, destination_folder)
