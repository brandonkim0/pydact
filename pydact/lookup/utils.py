from datetime import dt
import numpy as np

# generating a date shift in days
#   - preserve day of the week
#   - preserve month
#   - preserve season: shift it by year, then randomly pick a week in the season

# preserve day of the week + season **OR** preserve year, but not both

def generate_day_shift(mrn, anchor_date, centered_date, max_days_shift, seed):
    """
    Generates a day shift for a single patient. Randomly shifts data, preserving no attributes.

    args:
        mrn (int): patient medical record number.
        anchor_date (str): minimum admission date for each mrn. This is the earliest admission date per patient as that should not change in future data extractions.
        centered_date (str): reference date for anchor date. This is to ensure that the anchor date is centered around a date in the future.
        max_days_shift (int): number of days backward or forward into the future added to the difference between anchor date and centered date.
        seed (int): value for seed to generate the random days added to the difference between anchor date and centered date.
    returns:
        A dict mapping string keys of the value names to the actual values including mrn, anchor_year, anchor_date_shifted and days_shift.
    """
    rs = np.random.RandomState(seed=seed)
    random_integer = rs.randint(
        low=-abs(max_days_shift), high=max_days_shift)

    # Get number of days between centered date and anchor date.
    # Centered date, e.g. 2130 is chosen to ensure the date is between 2100 and 2200 which would not be confused with a real date.
    # The final "days_shift" will be the centered date +/- a random number of days.
    format_date = "%Y-%m-%d"
    date_diff_days = (dt.datetime.strptime(
        centered_date, format_date) - dt.datetime.strptime(
            anchor_date, format_date)).days

    # Add the random number, the random integer is the offset from the centered date, e.g. 2130.
    # The number can be chosen arbitrarily, e.g. 30.
    # The only consideration was that most software libraries don't understand dates beyond 2215 or so.
    days_shift = date_diff_days + random_integer
    anchor_date_shifted = dt.datetime.strptime(
        anchor_date, format_date) + dt.timedelta(days=days_shift)

    # Anchor date (the earliest admission date per patient is selected), and the actual year is extracted from this date.
    # Anchor date is selected as the earliest encounter since it should not change in future data extractions.
    anchor_year = anchor_date_shifted.year

    return {"mrn": mrn, "anchor_year": anchor_year, "anchor_date_shifted": anchor_date_shifted, "days_shift": days_shift}

