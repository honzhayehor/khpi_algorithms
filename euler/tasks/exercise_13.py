def first_n_digits(number_of_digits: int, number: int) -> int:
    number_str = str(number)
    if len(number_str) <= number_of_digits:
        return number
    return int(number_str[:number_of_digits])

def sum_of_numbers(list_of_numbers: list[int | str]): 
    return sum(int(n) for n in list_of_numbers)

def large_sum(list_of_numbers: list[int | str], number_of_digits: int):
    numbers_sum = sum_of_numbers(list_of_numbers)
    return first_n_digits(number_of_digits, numbers_sum)