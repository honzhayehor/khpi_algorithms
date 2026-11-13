import pytest

from euler.tasks.exercise_48 import last_digits_of_series, last_digits_text, series_sum


def test_example_series_up_to_ten():
    assert series_sum(10) == 10405071317


def test_last_ten_digits_of_example():
    assert last_digits_of_series(10) == 405071317


def test_leading_zero_is_kept_in_text():
    assert last_digits_text(10) == "0405071317"


def test_single_term():
    assert last_digits_of_series(1) == 1


def test_one_digit_only():
    assert last_digits_of_series(10, digits=1) == 7

def test_modular_version_matches_exact_sum():
    for limit in range(1, 51):
        for digits in (1, 3, 10):
            assert last_digits_of_series(limit, digits) == series_sum(limit) % 10 ** digits


def test_result_is_always_below_modulus():
    for digits in (1, 5, 10):
        assert 0 <= last_digits_of_series(200, digits) < 10 ** digits


def test_invalid_limit_raises():
    with pytest.raises(ValueError):
        last_digits_of_series(0)
    with pytest.raises(ValueError):
        series_sum(0)


def test_invalid_digits_raises():
    with pytest.raises(ValueError):
        last_digits_of_series(10, digits=0)


def test_full_answer():
    assert last_digits_text(1000) == "9110846700"
    assert series_sum(1000) % 10 ** 10 == 9110846700