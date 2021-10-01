''' Project Euler Problem 80

It is well known that if the square root of a natural number is not an integer,
then it is irrational. The decimal expansion of such square roots is infinite
without any repeating pattern at all.

The square root of two is 1.41421356237309504880...,
and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers,
find the total of the digital sums of the first one hundred decimal digits
for all the irrational square roots.
'''

from math import sqrt
from decimal import *


def sum_of_square_root(square_root, digits):
    getcontext().prec = 102
    s = str(Decimal(square_root).sqrt())
    ans = 0
    for i in range(0, digits + 1):
        if s[i] == '.':
            pass
        else:
            ans += int(s[i])
    return ans


def sums_of_irrational_roots(limit, digits):
    overall = 0
    for n in range(2, limit + 1):
        if sqrt(n) % 1 == 0:
            pass
        else:
            overall += sum_of_square_root(n, digits)
    return overall


print(sums_of_irrational_roots(99, 100))
