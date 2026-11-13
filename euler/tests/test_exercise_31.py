import pytest

from euler.tasks.exercise_31 import COINS, count_ways


def brute_force(target, coins):
    if target == 0:
        return 1
    if target < 0 or not coins:
        return 0
    return brute_force(target - coins[0], coins) + brute_force(target, coins[1:])


def test_small_example_by_hand():
    assert count_ways(5, [1, 2, 5]) == 4


def test_zero_target_has_one_way():
    assert count_ways(0) == 1


def test_only_one_penny_coin():
    assert count_ways(7, [1]) == 1


def test_two_coin_types():
    assert count_ways(4, [1, 2]) == 3


def test_unreachable_amount():
    assert count_ways(3, [2]) == 0


def test_coin_order_does_not_matter():
    assert count_ways(50, [1, 2, 5, 10, 20]) == count_ways(50, [20, 10, 5, 2, 1])


def test_matches_brute_force_on_small_amounts():
    for target in range(0, 41):
        assert count_ways(target, COINS) == brute_force(target, COINS)


def test_negative_target_raises():
    with pytest.raises(ValueError):
        count_ways(-1)


def test_invalid_coin_raises():
    with pytest.raises(ValueError):
        count_ways(10, [1, 0, 5])


def test_full_answer():
    assert count_ways(200) == 73682