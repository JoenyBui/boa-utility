from __future__ import absolute_import

import os
import json

__title__ = 'Utility'
__version__ = '1.0'
__author__ = 'Joeny Bui'
__license__ = ''
__copyright__ = 'Copyright'

__all__ = [
    'all_usage',
]

package_folder = os.path.dirname(__file__)
project_folder = os.path.split(package_folder)[0]

SETTING = {}

try:
    with open(os.path.join(project_folder, 'settings.json'), 'r') as data_file:
        SETTING = json.loads(data_file.read(), strict=False)
except IOError as e:
    print(str(e))
