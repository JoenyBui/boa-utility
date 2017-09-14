import inspect

# from exceptions import TypeError, AssertionError

__author__ = 'joeny'


def ensure_keys_exist(*args):
    """
    A decorator used to ensure that a key hierarchy exists.

    :param args: a series of keys to check in tree order
    :return:
    """
    def _ensure_keys_exist_1(fn):
        def _ensure_keys_exist_2(self, value):

            # Check to see if the keys exists inside the class __dict__ structure.
            next_dict = self.__dict__
            for key in args:
                # Check to see if the list exists.
                if not next_dict.get(key):
                    next_dict[key] = {}

                next_dict = next_dict[key]

            fn(self, value)

        return _ensure_keys_exist_2

    return _ensure_keys_exist_1


def accepts(*types):
    """
    A decorator used for class methods.

    :param types:
    :return:
    """
    def check_accepts(f):
        num_args = inspect.getargspec(f)
        assert len(types) == len(num_args.args) - 1

        def new_f(self, *args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), \
                       "arg %r does not match %s" % (a,t)
            return f(self, *args, **kwds)

        # new_f.func_name = f.func_name
        return new_f
    return check_accepts


def test_accepts(self, set_func, ret_func, type):
    """
    Test accepts.

    :param set_func:
    :param ret_func:
    :param type:
    :return:
    """
    # Test Int


    # int
    if type != int:
        with self.assertRaises(AssertionError):
            set_func(999)
    else:
        set_func(999)
        self.assertEqual(ret_func(), 999)

    # float
    if type != float:
        with self.assertRaises(AssertionError):
            set_func(0.001)
    else:
        set_func(0.001)

        self.assertEqual(ret_func(), 0.001)

    # str
    if type != str:
        with self.assertRaises(AssertionError):
            set_func("failed")
    else:
        set_func("succeed")

        self.assertEqual(ret_func(), "succeed")

    #bool
    if type != bool:
        with self.assertRaises(AssertionError):
            set_func(False)
    else:
        set_func(True)

        self.assertTrue(ret_func())

    #list
    if type != list:
        with self.assertRaises(AssertionError):
            set_func([0, 1, 2, 3])
    else:
        set_func([0, 1, 2, 3])

        self.assertEqual(ret_func(), [0, 1, 2, 3])

    #dict
    if type != dict:
        with self.assertRaises(AssertionError):
            set_func({"key": 0})
    else:
        set_func({"key": 1})

        self.assertEqual(ret_func(), {"key": 1})


def isFloat(string):
    """
    Is string a float representation.

    :param string:
    :return:
    """
    try:
        if string is None:
            return False
        else:
            float(string)

        return True
    except ValueError as e:
        return False


def isInt(string):
    """
    Is string an integer representation.

    :param string:
    :return:
    """
    try:
        if string is None:
            return False
        else:
            int(string)

        return True

    except ValueError as e:
        return False


def Float(string):
    """
    Float conversion.

    :param string:
    :return:
    """
    if isFloat(string):
        return float(string)
    else:
        return 0.0


def Int(string):
    """
    Integer conversion.

    :param string:
    :return:
    """
    if isInt(string):
        return int(string)
    else:
        return 0


def convert_to_float(fn):
    """
    Decorate for a function that checks if the value passed in is a float.  If it's string, convert it.
    If it's neither, we pass in a NULL value

    :param fn:
    :return:
    """
    def wrapped(self, *args, **kwargs):
        filter_args = None

        for item in args:
            # If a tuple or a list
            if isinstance(item, tuple) or isinstance(item, list):
                items = []

                for item_args in item:
                    if isFloat(item_args):
                        items.append(Float(item_args))
                    else:
                        items.append(None)

                if isinstance(item, tuple):
                    filter_args = (tuple(items),)
                else:
                    filter_args = (items,)

            else:
                # Single value
                if isFloat(item):
                    filter_args = (Float(item),)
                else:
                    filter_args = (None,)

        return fn(self, *filter_args, **kwargs)

    return wrapped


def convert_to_int(fn):
    """
    Decorator to convert to integer

    :param fn: function
    :return:
    """

    def wrapped(self, *args, **kwargs):
        filter_args = None

        for item in args:
            # If a tuple or a list
            if isinstance(item, tuple) or isinstance(item, list):
                items = []

                for item_args in item:
                    if isInt(item_args):
                        items.append(Int(item_args))
                    else:
                        items.append(None)

                if isinstance(item, tuple):
                    filter_args = (tuple(items),)
                else:
                    filter_args = (items,)

            else:
                # Single value
                if isInt(item):
                    filter_args = (Int(item),)
                else:
                    filter_args = (None,)

        return fn(self, *filter_args, **kwargs)

    return wrapped
