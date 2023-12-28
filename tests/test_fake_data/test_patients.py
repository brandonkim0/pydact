from datetime import datetime
import pandas as pd
from pydact.functions.filter import AllowList, BlockList, NumericFilter, AlphaNumericFilter, RegexFilter
from pydact.functions.date import PreserveDate, ShiftDate

# test identifier, regex filter

def test_patients_identifier(patients):
    identifier = patients[['mrn', 'mrn10', 'ssn']]
    for value in identifier:
        # while column is mrn or fiscal_num column
        pass
        # implement identifier deid function and use here.

def test_patients_search(patients):
    first_names = patients['first_name'] # first_name column
    out = []
    expected = ['Joann']

    for value in first_names:
        filtered = RegexFilter().transform('Joann', value)
        if filtered is not None:
            out.append(filtered)

    assert out == expected, f'Other values expected as filter output.'