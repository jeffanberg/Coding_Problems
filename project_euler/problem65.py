'''
Convergents of e
https://projecteuler.net/problem=65
'''
from fractions import Fraction
from numpy import e


def returnPeriods(num, limit):
    if num == e:
        return returnEuler(limit)
    periods = []
    r = num
    i = int(num)
    fractional = r - i
    for _ in range(0, limit):
        periods.append(i)
        r = 1 / fractional
        print(r)
        i = int(r)
        fractional = r - i
    return periods


def returnEuler(limit):
    periods = [2 * (i+1) // 3 if i % 3 == 2 else 1 for i in range(limit)]
    periods[0] += 1
    return periods


def returnConvergent(num, convergent):
    periods = returnPeriods(num, convergent)
    twoago_convergent = Fraction(periods[0], 1)
    previous_convergent = Fraction(periods[1] * periods[0] + 1, periods[1])
    for n in range(2, convergent):
        current_convergent = Fraction(periods[n]
                                      * previous_convergent.numerator
                                      + twoago_convergent.numerator, periods[n]
                                      * previous_convergent.denominator
                                      + twoago_convergent.denominator)
        twoago_convergent = previous_convergent
        previous_convergent = current_convergent
    return current_convergent


print(sum([int(n) for n in str(returnConvergent(e, 100).numerator)]))
