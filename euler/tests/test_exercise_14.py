import pytest

from euler.tasks.exercise_14 import collatz_length, collatz_next, longest_collatz_start


def test_next_even():
    assert collatz_next(40) == 20


def test_next_odd():
    assert collatz_next(13) == 40


def test_next_invalid():
    with pytest.raises(ValueError):
        collatz_next(0)


def test_length_of_one():
    assert collatz_length(1) == 1


def test_length_of_two():
    assert collatz_length(2) == 2


def test_example_from_problem():
    assert collatz_length(13) == 10


def test_cache_gives_same_results():
    cache = {}
    with_cache = [collatz_length(n, cache) for n in range(1, 200)]
    without_cache = [collatz_length(n) for n in range(1, 200)]
    assert with_cache == without_cache


def test_cache_is_filled():
    cache = {}
    collatz_length(13, cache)
    assert cache[40] == 9 and cache[2] == 2 and cache[13] == 10


def test_longest_under_ten():
    assert longest_collatz_start(10) == (9, 20)


def test_full_answer():
    assert longest_collatz_start(1_000_000) == (837799, 525)