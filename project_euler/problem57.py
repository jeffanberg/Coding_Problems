'''
https://projecteuler.net/problem=57
In the first one-thousand expansions, how many fractions contain a numerator
with more digits than the denominator?
'''


def expand(iteration):
    numerator = 1
    denominator = 1
    for _ in range(1, iteration + 1):
        tempnum = numerator
        numerator = numerator + (2 * denominator)
        denominator = tempnum + denominator
    return [numerator, denominator]


def findBiggerNumerators(limit):
    count = 0
    for i in range(1, limit + 1):
        fraction = expand(i)
        if len(str(fraction[0])) > len(str(fraction[1])):
            count += 1
    return count


print(findBiggerNumerators(1000))
