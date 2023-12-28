from datetime import datetime
import pandas as pd
from pydact.functions.filter import AllowList, BlockList, NumericFilter, AlphaNumericFilter, RegexFilter
from pydact.functions.keep import Keep
from pydact.functions.remove import Remove
from pydact.functions.date import PreserveDate, ShiftDate
from pydact.functions.replace import Replace

# test identifier, keep, remove, replace

def test_lab_events_identifier(lab_events):
    identifier = lab_events[['labevent_id', 'mrn', 'fiscal_num', 'specimen_id', 'itemid']]
    for value in identifier:
        # while column is mrn or fiscal_num column
        pass
        # implement identifier deid function and use here.

def test_lab_events_int(lab_events):
    identifier = lab_events[['specimen_id', 'itemid']]
    for value in identifier:
        # while column is mrn or fiscal_num column
        pass
        # implement identifier deid function and use here.

def test_lab_events_keep(lab_events):
    label = lab_events['label'][0]
    label_transformed = Keep().transform(label)
    out = label
    expected = label_transformed

    assert out == expected, f'Value was not kept.'

def test_lab_events_remove(lab_events):
    comment = lab_events['comments'][0]
    out = Remove().transform(comment)
    expected = '___'

    assert out == expected, f'Comment was not removed.'

def test_lab_events_replace(lab_events):
    comment = lab_events['comments'][0]
    out = Replace().transform(comment, 'New comments')
    expected = 'New comments'

    assert out == expected, f'Comment was not replaced.'
