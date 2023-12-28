from datetime import datetime, date
from unittest import expectedFailure
from pydact.functions.date import PreserveDate, ShiftDate
from pydact.functions.filter import RegexFilter
import pandas as pd
from pyparsing import Regex
from typing import List
from dateutil import parser

# test identifier, shfit_date, regex filter.

def test_admissions_identifier(admissions):
    identifier = admissions[['mrn', 'fiscal_num']]
    for value in identifier:
        # while column is mrn or fiscal_num column
        pass
        # implement identifier deid function and use here.

def test_admissions_shift_date(admissions):
    date_shifting = parser.parse(admissions['admittime'].iloc[0]).date() # 2009-12-17 19:56:22
    out = ShiftDate().year_set(date_shifting)
    expected = date(2100, 1, 1)
    assert out > expected, f'Shifted date year is not greater than year 2100.'

def test_regex_filter(admissions):
    language = admissions['language'].iloc[1] # second row
    out = RegexFilter().transform('Chuvash', language)
    expected = 'Chuvash'
    
    assert out == expected, f'Other value expected as filter output.'

def test_regex_filter_all(admissions):
    languages = admissions['language'] # all rows
    for value in languages:
        filtered = RegexFilter().transform(r'^N', value)
        if isinstance(filtered, str):
            assert filtered.startswith('N'), f'Value does not start with "N".'
        else:
            assert filtered is None, f'Value is non-none type.'