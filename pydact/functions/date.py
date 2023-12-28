from pandas import timedelta_range
from pydact.functions.base import DeidFunction
from datetime import datetime, date
from datetime import timedelta
from pydact.functions.base import DeidFunction
from collections import namedtuple

# namedtuple instance for readability in class ShiftDate
Season = namedtuple('Season', ['winter', 'spring', 'summer', 'autumn'])
season_tuple = Season('winter', 'spring', 'summer', 'autumn')

class PreserveDate(DeidFunction):
    """Day of the week preservation class.

    User inputs date value in datetime format, the
    day of the week of the value is returned.

    Typical usage example:

    >>> PreserveDate().transform(date(2022, 1, 15))
    'Saturday'
    """
    def __init__(self) -> None:
        super().__init__()

    def transform(self, value: datetime) -> str:
    # retrieve day of the week
        day_oftw = value.strftime('%A')
        return day_oftw

class ShiftDate(DeidFunction):
    """Shift date class designed to transform dates.

    Shift date by static value of days; ensuring the day of
    the week and season of the shifted day is the same as
    the initial date.
    Additionally, year_set method sets any date in datetime
    format to arbitrary static year value; 2199.

    Typical usage example:

    >>> original = date(2019,  1, 15))
    >>> ShiftDate().transform(original)
    """
    def __init__(self, Y=2000) -> None: # dummy leap year to allow input X-02-29 (leap day)
        self.Y = Y
        self.seasons_end = Season(
            date(self.Y,  3, 20), # mar 20
            date(self.Y,  6, 20), # jun 20
            date(self.Y,  9, 22), # sep 22
            date(self.Y, 12, 20), # dec 20
            )
        self.seasons = (('winter', (date(self.Y,  1,  1),  date(self.Y,  3, 20))), # Jan 1 -> Mar 20
        ('spring', (date(self.Y,  3, 21),  date(self.Y,  6, 20))), # Mar 21 -> Jun 20
        ('summer', (date(self.Y,  6, 21),  date(self.Y,  9, 22))), # Jun 21 -> Sep 22
        ('autumn', (date(self.Y,  9, 23),  date(self.Y, 12, 20))), # Sep 23 -> Dec 20
        ('winter', (date(self.Y, 12, 21),  date(self.Y, 12, 31)))) # Dec 21 -> Dec 31 (to support any year)

    def get_season(self, value: date) -> str:
        if isinstance(value, datetime):
            value = value.date()
        value = value.replace(2000)
        return next(season for season, (start, end) in self.seasons if start <= value <= end)

    def transform(self, value: date) -> date:
        # shift date by (x) days // (y) weeks...
        # ensure day of the week, season are the same.
        # check season, then add days according to the time distance away from the last day of their respective season;
        # so the shifted date stays in the same season as original.
        season = self.get_season(value)
        value = value.replace(2000)
        index = season_tuple.index(season)
        delta = abs(self.seasons_end[index] - value)
        value += timedelta(delta.days)
        return value
        
    def date_shift(self, value: date, days_shift: int) -> date:
        # shift date by user given days; days_shift.
        value += timedelta(days_shift)
        return value
    
    def year_set(self, value: date) -> None:
        # set year to arbitrary static value; example used, (year = 2199)
        month = value.month
        day = value.day
        difference = abs(date(2199, month, day) - value)
        # add difference of days to value to set year value to 2199.
        value += timedelta(difference.days)
        return value