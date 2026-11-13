import pytest

from euler.tasks.exercise_36 import (
    decimal_palindromes_below,
    double_base_numbers_brute,
    double_base_numbers_smart,
    is_double_base_palindrome,
    is_palindrome,
    sum_of_double_base_palindromes,
)


def test_example_585():
    assert bin(585)[2:] == "1001001001"
    assert is_double_base_palindrome(585)


def test_is_palindrome():
    assert is_palindrome("12321")
    assert is_palindrome("7")
    assert not is_palindrome("1232")


def test_leading_zeros_are_not_allowed():
    assert not is_double_base_palindrome(10)
    assert not is_double_base_palindrome(4)
    assert all(not is_double_base_palindrome(n) for n in range(2, 10_000, 2))


def test_small_known_list():
    assert double_base_numbers_smart(1000) == [1, 3, 5, 7, 9, 33, 99, 313, 585, 717]


def test_below_ten():
    assert double_base_numbers_smart(10) == [1, 3, 5, 7, 9]
    assert sum_of_double_base_palindromes(10) == 25


def test_palindrome_generator_matches_plain_filter():
    expected = [n for n in range(1, 20_000) if is_palindrome(str(n))]
    assert decimal_palindromes_below(20_000) == expected


def test_palindrome_counts():
    assert len(decimal_palindromes_below(1000)) == 108
    assert len(decimal_palindromes_below(1_000_000)) == 1998


@pytest.mark.parametrize("limit", [10, 100, 1000, 100_000])
def test_smart_matches_brute_force(limit):
    assert double_base_numbers_smart(limit) == double_base_numbers_brute(limit)


def test_invalid_limit_raises():
    with pytest.raises(ValueError):
        double_base_numbers_brute(0)
    with pytest.raises(ValueError):
        decimal_palindromes_below(0)


def test_full_answer():
    assert sum_of_double_base_palindromes(1_000_000) == 872187
    assert sum(double_base_numbers_brute(1_000_000)) == 872187