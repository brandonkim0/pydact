import pytest
from pydact.functions.perturb import Perturb, UpperLimit, LowerLimit

def test_upper_limit():
    out = UpperLimit().transform(89)
    expected = 91
    assert out == expected, f'Value provided does not change to upper limit value.'

def test_lower_limit():
    out = LowerLimit().transform(16)
    expected = 13
    assert out == expected, f'Value provided does not change to lower limit value.'