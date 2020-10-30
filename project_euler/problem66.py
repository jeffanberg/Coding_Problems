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
from math import sqrt
from fractions import Fraction


def returnPeriods(num, limit):
    periods = []
    r = sqrt(num)
    i = int(r)
    fractional = r - i
    for _ in range(0, limit):
        periods.append(i)
        r = 1 / fractional
        i = int(r)
        fractional = r - i
    return periods


def returnConvergent(num, convergent):
    periods = returnPeriods(num, convergent)
    twoago_convergent = Fraction(periods[0], 1)
    previous_convergent = Fraction(periods[1] * periods[0] + 1, periods[1])
    for n in range(1, convergent):
        current_convergent = Fraction(periods[n]
                                      * previous_convergent.numerator
                                      + twoago_convergent.numerator, periods[n]
                                      * previous_convergent.denominator
                                      + twoago_convergent.denominator)
        twoago_convergent = previous_convergent
        previous_convergent = current_convergent
    return current_convergent


def findLargestX(limit):
    largest_x = 0
    for d in range(2, limit + 1):
        if sqrt(d) % 1 == 0:
            continue
        i = 2
        ans = 0
        while ans != 1:
            print(f'd: {d} i: {i}')
            currentConvergent = returnConvergent(d, i)
            numerator = currentConvergent.numerator
            denominator = currentConvergent.denominator
            if (numerator ** 2) - ((7 * denominator) ** 2) == 1:
                if numerator > largest_x:
                    largest_x = numerator
                print(f'd: {d} x: {numerator}')
                ans = 1
            else:
                i += 1
    return largest_x


print(findLargestX(7))


'''
def bruteForceFindLargestX(limit):
    largest_x = 0
    for d in range(2, limit + 1):
        if sqrt(d) % 1 == 0:
            continue
        x = 2
        ans = 0
        while ans != 1:
            y = 1
            while d * (y**2) < x**2:
                if (x**2) - (d * (y**2)) == 1:
                    if x > largest_x:
                        largest_x = x
                    print(f'd: {d} x: {x}')
                    ans = 1
                y += 1
            x += 1
    return largest_x


print(findLargestX(1000))
'''