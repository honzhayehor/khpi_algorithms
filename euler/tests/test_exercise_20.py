import math

import pytest

from euler.tasks.exercise_20 import factorial, factorial_digit_sum, sum_of_digits


@pytest.mark.parametrize("n, expected", [
    (0, 1), (1, 1), (2, 2), (5, 120), (10, 3628800),
])
def test_factorial_known_values(n, expected):
    assert factorial(n) == expected


def test_factorial_matches_math_module():
    for n in range(0, 200):
        assert factorial(n) == math.factorial(n)


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize("n, expected", [
    (0, 0), (7, 7), (10, 1), (123, 6), (9999, 36),
])
def test_sum_of_digits_known_values(n, expected):
    assert sum_of_digits(n) == expected


def test_sum_of_digits_negative_raises():
    with pytest.raises(ValueError):
        sum_of_digits(-5)


def test_sum_of_digits_large_number():
    assert sum_of_digits(10**50) == 1
    assert sum_of_digits(10**50 - 1) == 9 * 50


def test_example_from_problem():
    assert factorial_digit_sum(10) == 27


def test_factorial_digit_sum_small_values():
    assert factorial_digit_sum(0) == 1
    assert factorial_digit_sum(1) == 1
    assert factorial_digit_sum(5) == 3


def test_hundred_factorial_has_158_digits():
    assert len(str(factorial(100))) == 158


def test_full_answer():
    assert factorial_digit_sum(100) == 648