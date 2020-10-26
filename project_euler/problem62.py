'''
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly
five permutations of its digits are cube.
'''
import math


def findCubicPermutations(num_of_perms):
    number_of_digits = 2
    while True:
        digit_perms = dict()
        min = math.ceil(pow(pow(10, number_of_digits - 1), 1.0 / 3.0))
        max = math.floor(pow(pow(10, number_of_digits) - 1, 1.0 / 3.0))
        for i in range(min, max):
            cube = i * i * i
            digit_perms.setdefault(str(sorted(str(cube))), []).append(cube)
        for n in digit_perms.items():
            if len(n[1]) == num_of_perms:
                return n[1][0]
        number_of_digits += 1


print(findCubicPermutations(5))
