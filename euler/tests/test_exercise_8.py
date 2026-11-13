import random
from math import prod

from euler.tasks.exercise_8 import largest_product


def test_window_of_one_returns_largest_digit():
    assert largest_product("3141592", 1) == 9


def test_window_equal_to_length_returns_product_of_all_digits():
    assert largest_product("2345", 4) == 120


def test_best_window_at_start():
    # 9*8 = 72 beats every other adjacent pair
    assert largest_product("987654", 2) == 72


def test_best_window_at_end():
    # 8*9 = 72 beats every other adjacent pair
    assert largest_product("123489", 2) == 72


def test_zero_in_middle_blocks_windows_that_contain_it():
    # windows "90" and "09" give 0, so the best pair is "99" = 81
    assert largest_product("9909", 2) == 81


def test_all_zeros_returns_zero():
    assert largest_product("00000", 3) == 0


def test_no_zero_free_window_returns_zero():
    # every window of 3 contains a zero
    assert largest_product("99099", 3) == 0


def test_window_longer_than_digits_returns_zero():
    assert largest_product("123", 5) == 0


def test_problem_statement_example_snippet():
    # 9 * 9 * 8 * 9 = 5832, as in the problem description
    assert largest_product("1239989123", 4) == 5832


def test_matches_brute_force_on_random_digits():
    rng = random.Random(42)
    digits = "".join(rng.choice("0123456789") for _ in range(200))
    window = 5
    expected = max(
        prod(int(d) for d in digits[i : i + window])
        for i in range(len(digits) - window + 1)
    )
    assert largest_product(digits, window) == expected