from pyparsing import Regex
import pytest
from pydact.functions.date import PreserveDate, ShiftDate
from datetime import datetime, date

def test_preserve_day_of_the_week():
    out = PreserveDate().transform(date(2022, 1, 15)) # January 15, 2022. (Saturday)
    expected = 'Saturday'
    assert out == expected, f'Day of the week returned does not match the day of the week of the date provided.'

def test_shift_date():
    out = ShiftDate().transform(date(2022, 1, 15)) # January 15, 2022.
    expected = date(2000, 3, 20) # March 20, 2022; end of winter.
    assert out == expected, f'Date was not shifted to the same season as original date and/or not shifted at all.'

def test_year_set():
    out = ShiftDate().year_set(date(2007, 8, 19)) # August 19, 2007.
    expected = date(2199, 8, 19) # August 19, 2199; same month and day, 2199 set as year.
    assert out == expected, f'Year was not set to 2199 and/or the month and day is not the same as original.'

def test_date_shift():
    out = ShiftDate().date_shift(date(2005, 4, 16), 30) # April 16, 2005, shift by 30 days.
    expected = date(2005, 5, 16)
    assert out == expected, f'Date was not correctly shifted by days_shift user inputted value.'
