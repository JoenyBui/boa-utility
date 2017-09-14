import numpy as np

__author__ = 'joeny'


def check_empty(value):
    if isinstance(value, np.ndarray):
        return value.any()
    else:
        return value is not []
