
import re

__author__ = 'joeny'


num_fmt = '[0-9]{d}'
exp_fmt = '[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?(?:0|[1-9]\d*)?)?'


def get_number_fmt(**kwargs):
    """
    Get the number of format.

    :param kwargs:
    :return:
    """
    fmt = ''

    if kwargs.get('signs'):
        fmt += '[+\-]?'

    if kwargs.get('decimal'):
        # fmt += '(?:0|[0-9]\d*)(?:\.\d*)?'
        fmt += '(?:[0-9]\d*)(?:\.\d*)?'
        # fmt += '([0-9]\d*)(?:\.\d*)?'
    else:
        fmt += '(?:[0-9]\d*)'
        # fmt += '(?:0|[0-9]\d*)'
        # fmt += r'([0-9]\d*)'

    if kwargs.get('exponential'):
        fmt += '(?:[eE][+\-]?(?:0|[1-9]\d*)?)?'

    return fmt


def parse_number(text, fmt):
    """
    Parse number.

    :param text: text value
    :param fmt: regex format
    """
    data = []
    src = re.findall(fmt, text)

    for item in src:
        try:
            if item.isdigit():
                data.append(int(item))
            else:
                data.append(float(item))

        except ValueError as e:
            print(e)

    return data, src
