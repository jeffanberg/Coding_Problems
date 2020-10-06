'''
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
from random import randrange
from itertools import permutations


def isPrime(n):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    return millerTest(n)


def millerTest(num):
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1

    for _ in range(5):
        a = randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != num - 1:
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = (v ** 2) % num
    return True


def findPandigitalPrimes():
    largest_pandigital = 0
    for n in range(1, 10):
        current_pandigital = ''
        for x in range(1, n + 1):
            current_pandigital = current_pandigital + str(x)
        for p in [''.join(perm) for perm in permutations(current_pandigital)]:
            if isPrime(int(p)):
                if int(p) > largest_pandigital:
                    largest_pandigital = int(p)
    return largest_pandigital


print(findPandigitalPrimes())
