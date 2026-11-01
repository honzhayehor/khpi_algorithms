import datetime

import pytest

from euler.tasks.exercise_19 import count_first_sundays, days_in_month, is_leap_year

def count_with_datetime(start_year, end_year):
    return sum(
        1
        for year in range(start_year, end_year + 1)
        for month in range(1, 13)
        if datetime.date(year, month, 1).weekday() == 6
    )


@pytest.mark.parametrize("year, expected", [
    (1900, False),
    (2000, True),
    (1904, True),
    (1901, False),
    (2100, False),
])
def test_is_leap_year(year, expected):
    assert is_leap_year(year) is expected


@pytest.mark.parametrize("month", [4, 6, 9, 11])
def test_thirty_day_months(month):
    assert days_in_month(1950, month) == 30


@pytest.mark.parametrize("month", [1, 3, 5, 7, 8, 10, 12])
def test_thirty_one_day_months(month):
    assert days_in_month(1950, month) == 31


def test_february_leap_and_non_leap():
    assert days_in_month(1900, 2) == 28
    assert days_in_month(1904, 2) == 29
    assert days_in_month(2000, 2) == 29


def test_days_in_month_invalid_month():
    with pytest.raises(ValueError):
        days_in_month(2000, 13)
    with pytest.raises(ValueError):
        days_in_month(2000, 0)


def test_days_in_a_year_add_up():
    assert sum(days_in_month(1999, m) for m in range(1, 13)) == 365
    assert sum(days_in_month(2000, m) for m in range(1, 13)) == 366


def test_single_year_1900():
    assert count_first_sundays(1900, 1900) == 2


def test_matches_datetime_for_many_ranges():
    for start in (1900, 1901, 1950, 1999):
        for end in (start, start + 1, start + 10, 2050):
            assert count_first_sundays(start, end) == count_with_datetime(start, end)


def test_invalid_year_ranges():
    with pytest.raises(ValueError):
        count_first_sundays(1899, 1950)
    with pytest.raises(ValueError):
        count_first_sundays(1950, 1949)


def test_full_answer():
    assert count_first_sundays(1901, 2000) == 171