from boautil.refmt import get_number_fmt, parse_number

__author__ = 'jbui'


def test_fmt():
    assert get_number_fmt() == '(?:[0-9]\d*)'
    assert get_number_fmt(signs=True) == '[+\-]?(?:[0-9]\d*)'
    assert get_number_fmt(decimal=True) == '(?:[0-9]\d*)(?:\.\d*)?'
    assert get_number_fmt(exponential=True) == '(?:[0-9]\d*)(?:[eE][+\-]?(?:0|[1-9]\d*)?)?'


def test_parse_number_fmt():
    text = 's="four digits 1234 five digits 56789 six digits 012345"'

    data, src = parse_number(text, '[0-9]{5}')
    assert data == [56789, 1234]


def test_exponential_fmt():
    text = '-128.3e-10'

    data, src = parse_number(text, get_number_fmt())
    assert data == [128, 3, 10]

    data, src = parse_number(text, get_number_fmt(signs=True))
    assert data == [-128, 3, -10]

    data, src = parse_number(text, get_number_fmt(decimal=True))
    assert data == [128.3, 10]

    data, src = parse_number(text, get_number_fmt(signs=True, decimal=True, exponential=True))
    assert data == [-128.3e-10]

    data, src = parse_number('000', get_number_fmt(signs=True, decimal=True, exponential=True))
    assert data == [0]

    data, src = parse_number('001', get_number_fmt(signs=True, decimal=True, exponential=True))
    assert data == [1]


def test_exponential_fmt_integer():
    fmt = '[+\-]?(?:[0-9]\d*)'

    data, src = parse_number('0', fmt)
    assert data == [0]

    data, src = parse_number('00', fmt)
    assert data == [0]

    data, src = parse_number('001', fmt)
    assert data == [1]

    data, src = parse_number('001e23', fmt)
    assert data[0] == 1
    assert data[1] == 23

    data, src = parse_number('-01', fmt)
    assert data == [-1]
