from dataclasses import replace
import pytest
from pydact.functions.replace import Replace

def test_replace():
    out = Replace().transform('Name', 'New Title')
    expected = 'New Title'
    assert out == expected, f'Value returned does not match the user inputted replacing value.'