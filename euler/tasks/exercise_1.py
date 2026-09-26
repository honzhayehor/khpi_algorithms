def sum_of_elements(elemets_to_sum: list[int]):
    return sum(elemets_to_sum)

def get_all_divisible(diviser: int | list[int], starting_number: int, ending_number: int):
    if starting_number >= ending_number:
        raise ValueError("Starting number cannot be bigger or be equal to ending number.")
    
    if isinstance(diviser, int):
        return [i for i in range(starting_number, ending_number) if i % diviser == 0]
    elif isinstance(diviser, list):
        return [i for i in range(starting_number, ending_number)
        if any(i % d == 0 for d in diviser)]
    else:
        raise ValueError(
            f"Method accepts list of integer or single integer as diviser, but unsupported type has been provided: {type(diviser)}"
        )

def get_sum_of_divisible(starting_from: int, ending_at: int, divisers: int | list[int]) -> int:
    return sum_of_elements(
        get_all_divisible(
            diviser=divisers,
            starting_number=starting_from,
            ending_number=ending_at
        )
    )