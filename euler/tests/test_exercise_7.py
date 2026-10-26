import pytest

from euler.tasks.exercise_7 import nth_prime_trial


def test_first_prime_is_two():
    assert nth_prime_trial(1) == 2


def test_sixth_prime_matches_problem_example():
    assert nth_prime_trial(6) == 13


@pytest.mark.parametrize(
    "n, expected",
    [(1, 2), (2, 3), (3, 5), (4, 7), (5, 11), (10, 29), (25, 97)],
)
def test_known_small_primes(n, expected):
    assert nth_prime_trial(n) == expected


def test_hundredth_prime():
    assert nth_prime_trial(100) == 541


def test_thousandth_prime():
    assert nth_prime_trial(1000) == 7919