import pytest

from euler.tasks.exercise_30 import (
    digit_power_sum,
    max_digits,
    numbers_brute,
    numbers_multisets,
    search_limit,
    sum_of_digit_power_numbers,
)


def test_example_1634():
    assert digit_power_sum(1634, 4) == 1634


def test_zero_digit_adds_nothing():
    assert digit_power_sum(8208, 4) == 8208


def test_bounds_for_fifth_powers():
    assert max_digits(5) == 6
    assert search_limit(5) == 6 * 59049 == 354294


def test_bounds_for_fourth_powers():
    assert max_digits(4) == 5
    assert search_limit(4) == 5 * 6561 == 32805


def test_fourth_powers_from_problem():
    assert numbers_multisets(4) == [1634, 8208, 9474]
    assert sum_of_digit_power_numbers(4) == 19316


def test_third_powers():
    assert numbers_multisets(3) == [153, 370, 371, 407]


def test_fifth_power_numbers():
    assert numbers_multisets(5) == [4150, 4151, 54748, 92727, 93084, 194979]


@pytest.mark.parametrize("power", [2, 3, 4, 5])
def test_both_methods_agree(power):
    brute = numbers_brute(power)
    assert brute == numbers_multisets(power)
    assert all(n >= 10 for n in brute)


def test_invalid_power_raises():
    with pytest.raises(ValueError):
        max_digits(0)


def test_full_answer():
    assert sum_of_digit_power_numbers(5) == 443839