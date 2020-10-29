'''
Odd period square roots
https://projecteuler.net/problem=64

How many continued fractions for sqrt(N) <= 10,000 have an odd period?
'''
from math import sqrt


def continuedFraction(num):
    r = int(sqrt(num))
    i = r
    k = 1
    period = 0
    while k != 1 or period == 0:
        k = (num - r * r) // k
        r = (i + r) // k * k - r
        period += 1
    return period


def findOddPeriods(limit):
    odd_periods = 0
    for num in range(2, limit + 1):
        if int(sqrt(num)) ** 2 == num:
            continue
        if continuedFraction(num) % 2 == 1:
            odd_periods += 1
    return odd_periods


print(findOddPeriods(10000))


# Previous attempt:
'''
def continuedFraction(num):
    notation = []
    r = num
    i = int(num)
    limit = i
    fractional = fractions.Fraction(r - i).limit_denominator()
    while fractional != 0 or len(notation) == 0:
        notation.append(i)
        r = (1 / fractional)
        i = (limit + i) // r * r - i
        fractional = fractions.Fraction(r - i).limit_denominator()
    return notation
'''
