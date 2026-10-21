import pytest
from euler.tasks.exercise_4 import largest_palindrome_product, is_palindrome

def test_two_digit_example_from_task():
    assert largest_palindrome_product(2) == 9009


def test_three_digit_answer():
    assert largest_palindrome_product(3) == 906609


def test_one_digit():
    # 9 * 9 = 81 is not a palindrome; 3 * 3 = 9 is the best single-digit... check brute force
    assert largest_palindrome_product(1) == 9


def test_result_is_palindrome():
    assert is_palindrome(largest_palindrome_product(3))


def test_result_is_product_of_two_3_digit_numbers():
    result = largest_palindrome_product(3)
    assert any(
        result % a == 0 and 100 <= result // a <= 999 for a in range(100, 1000)
    )


def test_matches_brute_force_for_two_digits():
    brute = max(
        a * b
        for a in range(10, 100)
        for b in range(10, 100)
        if str(a * b) == str(a * b)[::-1]
    )
    assert largest_palindrome_product(2) == brute


def test_matches_brute_force_for_three_digits():
    brute = max(
        a * b
        for a in range(100, 1000)
        for b in range(a, 1000)
        if str(a * b) == str(a * b)[::-1]
    )
    assert largest_palindrome_product(3) == brute


@pytest.mark.parametrize("n", [0, 1, 7, 11, 121, 9009, 906609])
def test_is_palindrome_true(n):
    assert is_palindrome(n)


@pytest.mark.parametrize("n", [10, 12, 123, 9010, 906608])
def test_is_palindrome_false(n):
    assert not is_palindrome(n)


def test_invalid_digits_raises():
    with pytest.raises(ValueError):
        largest_palindrome_product(0)