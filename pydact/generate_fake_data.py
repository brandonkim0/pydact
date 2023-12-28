from datetime import datetime, date, timedelta
from pathlib import Path
import warnings

from faker import Faker
import pandas as pd

# formats for converting date/datetime into string
CHOICES = {
    # admissions
    'admission_type': ('TBD'),
    'admission_location': ('TBD'),
    'discharge_location': ('TBD'),
    'insurance': ('TBD'),
    'religion': ('TBD'),
    'marital_status': ('TBD'),
    'race': ('TBD'),
    'diagnosis': ('TBD'),
    # transfers
    'eventtype': ('admit', 'transfer', 'discharge'),
    'careunit': ('NICU', 'SICU', 'Step down ward'),
    'ward': ('F9', 'R9', 'CCU7', 'CCC3'),
    'rm': ('101', '102', '103', '104'),
    'bed': ('1', '2', '3', '4'),
    # d_labitems
    'fluid': ('Blood', 'Urine'),
    'category': ('Hematology', 'Blood Gas'),
    # labevents
    'flag': (None, 'abnormal'),
    'priority': ('STAT', 'Routine'),
    'valueuom': ('mmHg', 'mg/dl', 'mmol/L')
}

def convert_values(d: dict, date_format: str='%Y-%m-%d', datetime_format: str='%Y-%m-%d %H:%M:%S') -> dict:
    """Convert data values using pre-specified formats, e.g. date to string."""
    for k, v in d.items():
        if isinstance(v, datetime):
            d[k] = v.strftime(datetime_format)
        elif isinstance(v, date):
            d[k] = v.strftime(date_format)
    return d

def optional(fake, val: any) -> any:
    """50% chance the returned value is None."""
    if fake.pybool():
        return val
    else:
        return None


if __name__ == '__main__':
    fake = Faker()
    Faker.seed(102)

    # default output to the test directory
    output_path = Path(__file__).parent.resolve()
    output_path = output_path / '..' / 'tests' / 'data'

    tables = {
        'patients': [],
        'admissions': [],
        'transfers': [],
        'd_labitems': [],
        'labevents': [],
        'microbiologyevents': [],
        'prescriptions': [],
        'emar': [],
        'emar_detail': [],
    }

    # generate fake data in one loop, so values are shared across tables
    for i in range(10):
        # decide on gender
        if i < 4:
            gender = 'F'
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()
        elif i < 8:
            gender = 'M'
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()
        else:
            gender = 'N'
            first_name = fake.first_name_nonbinary()
            last_name = fake.last_name_nonbinary()

        # patients data
        mrn = f'{fake.pyint(0, 10000000):07d}'
        mrn10 = '000' + mrn
        fiscal_num = f'0 {fake.pyint(0, 1e6):07d}'

        row = {
            'mrn': mrn,
            'mrn10': mrn10,
            'ssn': fake.ssn(),
            'gender': gender,
            'first_name': first_name,
            'last_name': last_name,
            'dob': fake.date_of_birth(),
            'dod': fake.date_between(date(2020, 1, 1), date(2030, 1, 1))
        }
        # convert datatypes (mostly date to string)
        row = convert_values(row)
        tables['patients'].append(row)

        admittime = fake.date_time_between(datetime(2000, 1, 1), datetime(2021, 1, 1))
        dischtime = fake.date_time_between(admittime, admittime + timedelta(days=30))
        # 50% chance of dying
        if fake.pybool():
            # 50% chance of dying in hospital
            if fake.pybool():
                deathtime = dischtime
            else:
                deathtime = fake.date_time_between(dischtime, dischtime + timedelta(days=300))
        else:
            deathtime = None

        # ed times
        # 50% chance of admitted from ED
        edregtime = optional(fake, fake.date_time_between(admittime - timedelta(hours=12), admittime - timedelta(hours=2)))
        edouttime = optional(fake, fake.date_time_between(admittime - timedelta(hours=2), admittime + timedelta(hours=2)))

        # admissions data
        row = {
            'mrn': mrn,
            'fiscal_num': fiscal_num,
            'admittime': admittime,
            'dischtime': dischtime,
            'deathtime': deathtime,
            'admission_type': 'TBD',
            'admission_location': 'TBD',
            'discharge_location': 'TBD',
            'insurance': 'TBD',
            'language': fake.language_name(),
            'religion': 'TBD',
            'marital_status': 'TBD',
            'race': 'TBD',
            'edregtime': edregtime,
            'edouttime': edouttime,
            'diagnosis': 'TBD',
            'hospital_expire_flag': deathtime is not None,
        }
        row = convert_values(row)
        tables['admissions'].append(row)

        # transfers
        intime = fake.date_time_between(admittime, admittime + timedelta(days=5))
        outtime = fake.date_time_between(intime, intime + timedelta(days=5))
        row = {
            'mrn': mrn,
            'fiscal_num': fiscal_num,
            'transfer_num': fake.pyint(0, 1000),
            'transfer_id': fake.pyint(0, 1000),
            'eventtype': fake.random_element(CHOICES['eventtype']),
            'careunit': fake.random_element(CHOICES['careunit']),
            'intime': intime,
            'ward': fake.random_element(CHOICES['ward']),
            'rm': fake.random_element(CHOICES['rm']),
            'bed': fake.random_element(CHOICES['bed']),
            'outtime': outtime,
        }
        row = convert_values(row)
        tables['transfers'].append(row)

        # d_labitems data
        itemid = fake.pyint(50000, 60000)
        label = fake.pystr()
        row = {
            'itemid': itemid,
            'label': label,
            'fluid': fake.random_element(CHOICES['fluid']),
            'category': fake.random_element(CHOICES['category']),
        }
        row = convert_values(row)
        tables['d_labitems'].append(row)

        charttime = fake.date_time_between(admittime, dischtime)
        storetime = fake.date_time_between(charttime, charttime + timedelta(hours=6))
        valuenum = fake.pydecimal(3, 1, positive=True)
        # lab data
        row = {
            'labevent_id': fake.pyint(1e6, 9e6),
            'mrn': mrn,
            'fiscal_num': fiscal_num,
            'specimen_id': fake.pyint(1e4, 3e4),
            'itemid': itemid,
            'label': label,
            'charttime': charttime,
            'storetime': storetime,
            'value': str(valuenum),
            'valuenum': valuenum,
            'valueuom': fake.random_element(CHOICES['valueuom']),
            'ref_range_lower': None,
            'ref_range_upper': None,
            'flag': fake.random_element(CHOICES['flag']),
            'priority': fake.random_element(CHOICES['priority']),
            'comments': fake.pystr(),
        }
        row = convert_values(row)
        tables['labevents'].append(row)

        continue
        # microbiology
        row = {
            'microevent_id': None,
            'subject_id': None,
            'mrn': None,
            'hadm_id': None,
            'fiscal_num': None,
            'micro_specimen_id': None,
            'micro_specimen_id_phi': None,
            'lab_number_suffix': None,
            'lab_number': None,
            'chartdate': None,
            'charttime': None,
            'spec_itemid': None,
            'spec_type_cd': None,
            'spec_type_desc': None,
            'test_seq': None,
            'storedate': None,
            'storetime': None,
            'test_itemid': None,
            'test_cd': None,
            'test_name': None,
            'org_itemid': None,
            'org_cd': None,
            'org_name': None,
            'isolate_num': None,
            'quantity': None,
            'ab_itemid': None,
            'ab_cd': None,
            'ab_name': None,
            'dilution_text': None,
            'dilution_comparison': None,
            'dilution_value': None,
            'interpretation': None,
            'comments': None,
        }
        print('=== microbiologyevents ===')
        print(row)

        # prescriptions
        row = {
            'subject_id': None,
            'mrn': None,
            'hadm_id': None,
            'fiscal_num': None,
            'pharmacy_id_phi': None,
            'pharmacy_id': None,
            'poe_id_phi': None,
            'poe_id': None,
            'poe_seq_phi': None,
            'poe_seq': None,
            'starttime': None,
            'stoptime': None,
            'drug_type': None,
            'drug': None,
            'drug_name_generic': None,
            'formulary_drug_cd': None,
            'gsn': None,
            'ndc': None,
            'prod_strength': None,
            'form_rx': None,
            'dose_val_rx': None,
            'dose_unit_rx': None,
            'form_val_disp': None,
            'form_unit_disp': None,
            'dose_val_disp': None,
            'dose_val_disp_txt': None,
            'dose_unit_disp': None,
            'doses_per_24_hrs': None,
            'route': None,
            'dose_range_override': None,
        }
        print('=== prescriptions ===')
        print(row)

        # emar
        row = {
            'subject_id': None,
            'mrn': None,
            'hadm_id': None,
            'fiscal_num': None,
            'ccc_id': None,
            'emar_id_phi': None,
            'emar_id': None,
            'emar_seq_phi': None,
            'emar_seq': None,
            'poe_id_phi': None,
            'poe_id': None,
            'pharmacy_id_phi': None,
            'pharmacy_id': None,
            'charttime': None,
            'medication': None,
            'event_txt': None,
            'event_detail': None,
            'scheduletime': None,
            'enter_prov_num': None,
            'enter_name': None,
            'storetime': None,
        }
        print('=== emar ===')
        print(row)

        # emar_detail
        row = {
            'subject_id': None,
            'mrn': None,
            'ccc_id': None,
            'emar_id_phi': None,
            'emar_id': None,
            'emar_seq_phi': None,
            'emar_seq': None,
            'parent_field_ordinal': None,
            'administration_type': None,
            'pharmacy_id_phi': None,
            'pharmacy_id': None,
            'pharmacy_order_note': None,
            'ip_address': None,
            'ward': None,
            'patient_location': None,
            'barcode_id': None,
            'barcode_type': None,
            'reason_for_no_barcode': None,
            'complete_dose_not_given': None,
            'dose_due': None,
            'dose_due_unit': None,
            'dose_given': None,
            'dose_given_unit': None,
            'will_remainder_of_dose_be_given': None,
            'product_amount_given': None,
            'product_unit': None,
            'product_code': None,
            'product_description': None,
            'product_description_other': None,
            'prior_infusion_rate': None,
            'infusion_rate': None,
            'infusion_rate_adjustment': None,
            'infusion_rate_adjustment_amount': None,
            'infusion_rate_unit': None,
            'route': None,
            'infusion_complete': None,
            'completion_interval': None,
            'new_iv_bag_hung': None,
            'continued_infusion_in_other_location': None,
            'reason_for_unscheduled_stop_or_removal': None,
            'restart_interval': None,
            'side': None,
            'site': None,
            'non_formulary_visual_verification': None,
            'comments': None,
        }
        print('=== emar_detail ===')
        print(row)


    for table_name, table_data in tables.items():
        if len(table_data) == 0:
            warnings.warn(f'No data found for {table_name}. Skipping.')
            continue
        # convert to pandas dataframe
        df = pd.DataFrame.from_dict(table_data)

        # overwrite original entry
        tables[table_name] = df

        # output to file
        df.to_csv(output_path / f'fake_data_{table_name}.csv', index=False)