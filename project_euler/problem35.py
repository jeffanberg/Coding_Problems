'''
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from itertools import product
from random import randrange


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


def findCircularPrimes(digits):
    count = 4
    final_numbers = {'1', '3', '7', '9'}
    for n in range(2, digits + 1):
        for p in product(final_numbers, repeat=n):
            p_int = int(''.join(p))
            perm = {int(''.join(p[i:]+p[:i])) for i in range(len(p))}
            if p_int == min(perm) and all(isPrime(x) for x in perm):
                print(p, len(perm))
                count += len(perm)
    return count


print(findCircularPrimes(9))
