from euler.tasks.exercise_5 import gcd, lcm, smallest_common
from typing import Generator

def test_smallest_common():
    assert (smallest_common(1, 20) == 232792560)