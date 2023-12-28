from pyparsing import Regex
import pytest
from pydact.functions.filter import AllowList, BlockList, NumericFilter, AlphaNumericFilter, RegexFilter

def test_filter_allow_list_allowed_value():
    out = AllowList().transform('Name', ['Name'])
    expected = 'Name'
    assert out == expected, f'Inputted value is allowed.'

def test_filter_allow_list_not_allowed_value():
    out = AllowList().transform('Apple', ['Name'])
    expected = None
    assert out == expected, f'Inputted value is not allowed'

def test_filter_block_list_blocked_value():
    out = BlockList().transform('Name', ['Name'])
    expected = None
    assert out == expected, f'Inputted value is blocked.'

def test_filter_block_list_not_blocked_value():
    out = BlockList().transform('Apple', ['Name'])
    expected = 'Apple'
    assert out == expected, f'Inputted value is not blocked.'

def test_numeric_filter_is_numeric():
    out = NumericFilter().transform('123')
    expected = '123'
    assert out == expected, f'Inputted value is numeric.'
def test_numeric_filter_is_not_numeric():
    out = NumericFilter().transform('1z2y3')
    expected = None
    assert out == expected, f'Inputted value is not numeric.'

def test_alpha_num_filter_is_alpha_num():
    out = AlphaNumericFilter().transform('1k34po')
    expected = '1k34po'
    assert out == expected, f'Inputted value is  alphanumeric.'

def test_alpha_num_filter_is_not_alpha_num():
    out = AlphaNumericFilter().transform('1k3+=4po~')
    expected = None
    assert out == expected, f'Inputted value is not alpha numeric.'

def test_regex_filter_is_regex_matching():
    out = RegexFilter().transform('123', '123')
    expected = '123'
    assert out == expected, f'Inputted value matches regex pattern provided.'

def test_regex_filter_is_not_regex_matching():
    out = RegexFilter().transform('[0-9]', 'zdcd]2')
    expected = None
    assert out == expected, f'Inputted value does not match regex pattern provided.'