SUNDAY = 6
ANCHOR_YEAR = 1900
DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    """Divisible by 4, but not by 100 unless also divisible by 400."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12")
    if month == 2 and is_leap_year(year):
        return 29
    return DAYS_IN_MONTH[month - 1]


def count_first_sundays(start_year, end_year):
    if start_year < ANCHOR_YEAR:
        raise ValueError(f"start_year must be >= {ANCHOR_YEAR}")
    if end_year < start_year:
        raise ValueError("end_year must be >= start_year")

    weekday = 0
    count = 0
    for year in range(ANCHOR_YEAR, end_year + 1):
        for month in range(1, 13):
            if year >= start_year and weekday == SUNDAY:
                count += 1
            weekday = (weekday + days_in_month(year, month)) % 7
    return count
