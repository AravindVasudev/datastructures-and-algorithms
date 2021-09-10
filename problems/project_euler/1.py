# https://projecteuler.net/problem=1
UPPER_BOUND = 999

def get_multiple_sum(n: int, bound: int = UPPER_BOUND) -> int:
    num_values = bound // n
    multiple_sum = (num_values * (num_values + 1)) / 2

    return multiple_sum * n

print(get_multiple_sum(3) + get_multiple_sum(5) - get_multiple_sum(15))
