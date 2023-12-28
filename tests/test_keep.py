import pytest
from pydact.functions.keep import Keep

def test_keep():
    out = Keep().transform('Name')
    expected = 'Name'
    assert out == expected, f'Value returned is not the same as the value inputted.'