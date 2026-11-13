from itertools import islice
from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    current, following = 1, 1
    while True:
        yield current
        current, following = following, current + following


def get_number_length(number: int) -> int:
    return len(str(number))


def find_index_of_element(number_of_digits: int) -> int:
    if number_of_digits < 1:
        raise ValueError("number_of_digits must be >= 1")

    for index, fib_num in enumerate(fibonacci(), start=1):
        if get_number_length(fib_num) >= number_of_digits:
            return index

