import pytest
from pydact.functions.remove import Remove

def test_remove():
    out = Remove().transform('Name')
    expected = '___'
    assert out == expected, f'Value inputted was not replaced with "___"'