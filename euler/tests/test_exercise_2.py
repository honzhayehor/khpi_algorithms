from euler.tasks.exercise_2 import fibonacci, fib_even_elements
from typing import Generator

def test_fibonacci_is_generator():
    assert isinstance(fibonacci(1), Generator)

def test_first_ten_elements_of_fibonacci():
    perfect = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # ceiling is 90, since we need up to 89 (included)
    fib = [num for num in fibonacci(90)]
    assert perfect == fib

def test_for_task_2_correct_output():
    correct = 4613732
    my_method = fib_even_elements(ceiling=4_000_000, provider=fibonacci)
    assert correct == my_method

    