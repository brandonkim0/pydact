from datetime import datetime
from pydact.functions.filter import AllowList, BlockList, NumericFilter, AlphaNumericFilter, RegexFilter
from pydact.functions.date import PreserveDate, ShiftDate
import pytest
import os
import csv
import pandas as pd

@pytest.fixture(scope='session')
def test_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path

@pytest.fixture(scope='session')
def admissions(test_path):
    """
    Load fake admissions data.
    """

    admissions = os.path.join(test_path, 'data', 'fake_data_admissions.csv')

    with open(admissions, 'r') as csv_file:
        df = pd.read_csv(csv_file)

    return df

@pytest.fixture(scope='session')
def lab_items(test_path):
    """
    Load fake lab items data.
    """

    lab_items = os.path.join(test_path, 'data', 'fake_data_d_labitems.csv')

    with open(lab_items, 'r') as csv_file:
        df = pd.read_csv(csv_file)

    return df

@pytest.fixture(scope='session')
def lab_events(test_path):
    """
    Load fake lab events data.
    """

    lab_events = os.path.join(test_path, 'data', 'fake_data_labevents.csv')

    with open(lab_events, 'r') as csv_file:
        df = pd.read_csv(csv_file)

    return df

@pytest.fixture(scope='session')
def patients(test_path):
    """
    Load fake patients data.
    """

    patients = os.path.join(test_path, 'data', 'fake_data_patients.csv')

    with open(patients, 'r') as csv_file:
        df = pd.read_csv(csv_file)
    
    return df

@pytest.fixture(scope='session')
def transfers(test_path):
    """
    Load fake transfers data.
    """

    transfers = os.path.join(test_path, 'data', 'fake_data_transfers.csv')

    with open(transfers, 'r') as csv_file:
        df = pd.read_csv(csv_file)

    return df

# TEST KEEP, REMOVE, REPLACE ON VALUES.

# mrn - 'identifier'
# fiscal_num - 'identifier'
# admittime - 'shift_date, preserve_date'
# dischtime - 'shift_date, preserve_date'
# deathtime - 'shift_date, preserve_date'
# admission_type - 'filter'
# admission_location - 'filter, remove'
# discharge_location - 'filter, remove'
# insurance - 'filter'
# language - 'filter'
# religion - 'filter'
# marital_status - 'filter'
# race - 'filter'
# edregtime - 'shift_date, preserve_date'
# edouttime - 'shift_date, preserve_date'
# diagnosis - 'filter'
# hospital_expire_flag - 'filter'
