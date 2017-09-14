import os
import threading

__author__ = 'joeny'


def threaded(fn):
    """
    Threaded function.

    :param fn: function
    :return:
    """
    def wrapper(*args, **kwargs):
        DEBUG_THREAD = os.getenv('DEBUG_THREAD', False)

        if DEBUG_THREAD:
            # To debug threaded function call, we pass the function inside the thread.
            return fn(*args, **kwargs)
        else:
            threading.Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapper


def wait_dlg(function, *args, **kwargs):
    """
    Wait dialog

    :param function:
    :param args:
    :param kwargs:
    :return:
    """
    import wx

    msg = 'Please wait while we process your request..'
    dlg = wx.BusyInfo(msg)
    ret = function(*args, **kwargs)
    dlg = None
