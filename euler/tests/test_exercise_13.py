import pytest

from euler.tasks.exercise_13 import (
    first_n_digits,
    large_sum,
    sum_of_numbers,
)

FIFTY_DIGIT_NUMBER = "37107287533902102798797998220837590246510135740250"


def test_first_n_digits_truncates_long_number():
    assert first_n_digits(3, 123456) == 123


def test_first_n_digits_returns_number_if_shorter_than_n():
    assert first_n_digits(10, 123) == 123


def test_first_n_digits_returns_number_if_exactly_n_digits():
    assert first_n_digits(5, 12345) == 12345


def test_first_n_digits_truncates_instead_of_rounding():
    assert first_n_digits(3, 129999) == 129


def test_first_n_digits_single_digit():
    assert first_n_digits(1, 987654321) == 9


def test_sum_of_numbers_with_ints():
    assert sum_of_numbers([1, 2, 3, 4]) == 10


def test_sum_of_numbers_with_strings_and_mixed_types():
    assert sum_of_numbers(["10", 20, "30"]) == 60


def test_sum_of_numbers_empty_list_is_zero():
    assert sum_of_numbers([]) == 0


def test_large_sum_small_example():
    # 1234 + 8766 = 10000 -> first 3 digits are 100
    assert large_sum([1234, 8766], 3) == 100


@pytest.mark.parametrize("copies", [1, 10, 100])
def test_large_sum_handles_50_digit_numbers(copies):
    numbers = [FIFTY_DIGIT_NUMBER] * copies
    expected = int(str(int(FIFTY_DIGIT_NUMBER) * copies)[:10])
    assert large_sum(numbers, 10) == expected