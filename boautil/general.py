
__author__ = 'joeny'


def check_empty(value):
    import numpy as np

    if isinstance(value, np.ndarray):
        return value.any()
    else:
        return value is not []
