'''Find the two entries that sum to 2020;
what do you get if you multiply them together?'''

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'day1_input.txt')) as number_file:
    numbers = number_file.read().split('\n')

# Part 1 Solution:
for n in numbers:
    for i in range(len(numbers) - 1):
        if int(n) + int(numbers[i]) == 2020:
            print(f'{n} * {numbers[i]} = {int(n) * int(numbers[i])}')


#Part 2 Solution
for n in numbers:
    for x in range(len(numbers) - 1):
        for y in range(len(numbers) - 1):
            if x == y:
                break
            if int(n) + int(numbers[x]) + int(numbers[y]) == 2020:
                print(f'{n} * {numbers[x]} * {numbers[y]} = \
                {int(n) * int(numbers[x]) * int(numbers[y])}')