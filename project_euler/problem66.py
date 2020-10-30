'''
Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions
in positive integers when D is square.

By finding minimal solutions in
x for D = {2, 3, 5, 6, 7},
we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7,
the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x
for which the largest value of x is obtained.
'''
from fractions import Fraction
from decimal import Decimal
from decimal import getcontext
from math import sqrt

getcontext().prec = 80


def returnPeriods(num, limit):
    periods = []
    r = Decimal(num).sqrt()
    i = int(r)
    fractional = Decimal(r - i)
    for _ in range(0, limit):
        periods.append(i)
        r = Decimal(1 / fractional)
        i = int(r)
        fractional = Decimal(r - i)
    return periods


def returnConvergent(num, convergent):
    periods = returnPeriods(num, convergent)
    twoago_convergent = Fraction(periods[0], 1)
    if convergent == 1:
        return twoago_convergent
    previous_convergent = Fraction(periods[1] * periods[0] + 1, periods[1])
    if convergent == 2:
        return previous_convergent
    else:
        for n in range(2, convergent):
            current_convergent = Fraction(periods[n]
                                          * previous_convergent.numerator
                                          + twoago_convergent.numerator,
                                          periods[n]
                                          * previous_convergent.denominator
                                          + twoago_convergent.denominator)
            twoago_convergent = previous_convergent
            previous_convergent = current_convergent
    return current_convergent


def findLargestX(limit):
    largest_x = 0
    res = 0
    for d in range(2, limit + 1):
        if sqrt(d) % 1 == 0:
            continue
        i = 1
        ans = 0
        while ans != 1:
            currentConvergent = returnConvergent(d, i)
            numerator = currentConvergent.numerator
            denominator = currentConvergent.denominator
            if (numerator ** 2) - (d * (denominator ** 2)) == 1:
                if numerator > largest_x:
                    largest_x = numerator
                    res = d
                ans = 1
            else:
                i += 1
    return res


print(findLargestX(1000))
