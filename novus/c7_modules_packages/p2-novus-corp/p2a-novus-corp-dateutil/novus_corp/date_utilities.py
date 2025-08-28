# p2a-novus-corp-dateutil/novus_corp/date_utilities.py

from datetime import datetime


def days_to_novus_day(from_date=None):
    """Return the number of days until World Novus Day (August 14th)."""
    if from_date is None:
        from_date = datetime.now()
    if from_date.month > 8 or (from_date.month == 8 and from_date.day > 14):
        day_of_novus = datetime(from_date.year + 1, 8, 14)
    else:
        day_of_novus = datetime(from_date.year, 8, 14)
    return (day_of_novus - from_date).days
