from pytest import mark, raises

import pyflantic


@mark.parametrize("x,y", [("", "")])
def test_xy(x, y):
    with raises(AssertionError):
        assert False
