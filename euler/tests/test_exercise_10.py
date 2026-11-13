import pytest

from euler.tasks.exercise_10 import sum_of_primes_below


def test_problem_statement_example():
    # 2 + 3 + 5 + 7 = 17
    assert sum_of_primes_below(10) == 17


def test_limit_30():
    # 2+3+5+7+11+13+17+19+23+29
    assert sum_of_primes_below(30) == 129


@pytest.mark.parametrize("limit", [0, 1, 2])
def test_no_primes_below_two(limit):
    assert sum_of_primes_below(limit) == 0


def test_negative_limit_returns_zero():
    assert sum_of_primes_below(-5) == 0


def test_limit_3_includes_only_two():
    assert sum_of_primes_below(3) == 2


@pytest.mark.parametrize("limit, expected", [(7, 10), (11, 17), (13, 28)])
def test_limit_that_is_prime_is_excluded(limit, expected):
    # "below" is strict: 7 -> 2+3+5, 11 -> 2+3+5+7, 13 -> 2+3+5+7+11
    assert sum_of_primes_below(limit) == expected


def test_limit_just_above_a_prime_includes_it():
    # 11 is now below the limit: 2+3+5+7+11
    assert sum_of_primes_below(12) == 28


def test_limit_100():
    assert sum_of_primes_below(100) == 1060


def test_limit_1000():
    assert sum_of_primes_below(1000) == 76127


def test_matches_trial_division_for_limits_up_to_300():
    def is_prime(n):
        return n >= 2 and all(n % d for d in range(2, int(n ** 0.5) + 1))

    for limit in range(0, 301):
        expected = sum(n for n in range(limit) if is_prime(n))
        assert sum_of_primes_below(limit) == expected, f"limit={limit}"