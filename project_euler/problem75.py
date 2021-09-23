''' Project Euler Problem 75 '''
import math


''' # Too long of a compute, needs to be optimized
def divisors(n):
    for divisor in range(1, int(n**0.5) + 1):
        if n % divisor == 0:
            yield divisor, n // divisor


def findRightSquare(num):
    count = 0
    for r in range(2, num, 2):
        if count > 1:
            return False
        st = r*r // 2
        for s, t in divisors(st):
            x = (r+s) + (r+t) + (r+s+t)
            if x == num:
                count += 1
    if count == 1:
        return True
    if count != 1:
        return False


def findLimit(limit):
    count = 0
    for i in range(2, limit, 2):
        if findRightSquare(i):
            count += 1
    return count
'''

# Using sets and the Euclidean algorithm.


def pe75(limit):
    maybe = set()
    nope = set()
    for m in range(2, int(math.sqrt(limit / 2))):
        for n in range(m-1, 0, -2):
            if math.gcd(m, n) == 1:
                s = 2 * (m*m + m*n)
                for k in range(1, int(limit / s + 1)):
                    nope.add(k*s) if k*s in maybe else maybe.add(k*s)
    return len(maybe - nope)


print(pe75(1.5 * (10 ** 6)))
