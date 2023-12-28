from datetime import datetime
import pandas as pd
from pydact.functions.filter import AllowList, BlockList, NumericFilter, AlphaNumericFilter, RegexFilter
from pydact.functions.date import PreserveDate, ShiftDate

# test allow list, block list, numeric filter

def test_lab_items_allow(lab_items):
    fluids = lab_items['fluid']
    out = []
    expected = ['Urine', 'Urine', 'Urine']
    for value in fluids:
        filtered = AllowList().transform(value, ['Urine'])
        if filtered is not None:
            out.append(filtered)

    assert out == expected, f'Not all allowed values were outputted.'

def test_lab_items_block(lab_items):
    fluids = lab_items['fluid']
    out = []
    expected = [None, None, None]
    for value in fluids:
        blocked = BlockList().transform(value, ['Urine'])
        if blocked is None:
            out.append(blocked)

    assert out == expected, f'Non-blocked values were allowed or not all blocked values returned None (were not blocked).'

def test_lab_items_numeric(lab_items):
    item_ids = lab_items['itemid']
    for value in item_ids:
        value = str(value)
        filtered = NumericFilter().transform(value)
        if filtered is None:
            assert filtered is None, f'Value is non-none type.'
        else:
            assert isinstance(int(filtered), int), f'Numeric filter did not filter integer values correctly.'