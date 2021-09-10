# https://projecteuler.net/problem=2
UPPER_BOUND = 4000000

total = 0
a, b = 0, 1

valid = True
while valid:
    a, b = b, a + b

    if not (b & 1):
        total += b

    valid = b < UPPER_BOUND

print(total)
