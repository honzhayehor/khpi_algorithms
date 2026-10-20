import pytest
from euler.tasks.exercise_3 import largest_prime_factor

def test_example_from_task():
    assert largest_prime_factor(13195) == 29

def test_project_euler_number():
    assert largest_prime_factor(600851475143) == 6857

def test_prime_number_returns_itself():
    assert largest_prime_factor(97) == 97

def test_large_prime_returns_itself():
    assert largest_prime_factor(1_000_000_007) == 1_000_000_007

def test_power_of_two():
    assert largest_prime_factor(1024) == 2

def test_prime_squared():
    assert largest_prime_factor(49) == 7

def test_product_of_two_primes():
    assert largest_prime_factor(11 * 13) == 13

def test_smallest_prime():
    assert largest_prime_factor(2) == 2

def test_repeated_factors():
    # 360 = 2^3 * 3^2 * 5
    assert largest_prime_factor(360) == 5

@pytest.mark.parametrize(
    "n, expected",
    [
        (6, 3),
        (15, 5),
        (100, 5),
        (81, 3),
        (2 * 3 * 5 * 7 * 11, 11),
    ],
)
def test_parametrized_small_values(n, expected):
    assert largest_prime_factor(n) == expected