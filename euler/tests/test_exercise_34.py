import pytest

from euler.tasks.exercise_34 import (
    FACTORIALS,
    curious_numbers_brute,
    curious_numbers_multisets,
    digit_factorial_sum,
    max_digits,
    search_limit,
    sum_of_curious_numbers,
)


def test_example_145():
    assert digit_factorial_sum(145) == 145


def test_zero_digit_counts_as_one():
    assert digit_factorial_sum(10) == 2


def test_maximum_digit_count_is_seven():
    assert max_digits() == 7


def test_search_limit_is_seven_times_nine_factorial():
    assert search_limit() == 7 * 362880 == 2540160


def test_eight_or_more_digits_are_impossible():
    for n in range(8, 15):
        assert 10 ** (n - 1) > n * FACTORIALS[9]


def test_brute_force_up_to_ten_thousand():
    assert curious_numbers_brute(10_000) == [145]


def test_multiset_method_finds_both_numbers():
    assert curious_numbers_multisets() == [145, 40585]


def test_single_digits_are_excluded():
    result = curious_numbers_multisets()
    assert 1 not in result and 2 not in result
    assert all(n >= 10 for n in curious_numbers_brute(100))


def test_both_methods_agree_over_the_whole_range():
    assert curious_numbers_brute(search_limit()) == curious_numbers_multisets()


def test_full_answer():
    assert sum_of_curious_numbers() == 40730