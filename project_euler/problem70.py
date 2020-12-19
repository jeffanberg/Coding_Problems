''' Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of positive numbers less than or equal to n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number,
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that
87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n
and the ratio n/φ(n) produces a minimum. '''
from math import sqrt


def eratostenes(n):
    multiples = set()
    primes = set()
    for i in range(2, n+1):
        if i not in multiples:
            primes.add(i)
            multiples.update(range(i*i, n+1, i))
    return primes


def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))


limit = 10 ** 7
primes = sorted(list(eratostenes(int(1.2 * sqrt(limit)))))
del primes[:int(0.6 * len(primes))]


def findPhiPerm(limit):
    min_q, min_n, i = 2, 0, 0
    for p1 in primes:
        i += 1
        for p2 in primes[i:]:
            if (p1 + p2) % 9 != 1:
                continue
            n = p1 * p2
            if n > limit:
                return min_n
            phi = (p1 - 1) * (p2 - 1)
            q = n / float(phi)
            if is_perm(phi, n) and min_q > q:
                min_q = q
                min_n = n
    return "Nothing found :("


print(findPhiPerm(limit))


'''def findTotientMinimum(limit):
    minimum = 10000
    ans = 0
    for i in range(2, limit):
        if set(str(i)) == set(str(findTotientProduct(i))):
            e = i / findTotientProduct(i)
            if e < minimum:
                minimum = e
                ans = i
    return ans


def findTotientProduct(num):
    result = num
    p = 2
    while p * p <= num:
        if num % p == 0:
            while num % p == 0:
                num = num // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
    if num > 1:
        result = result * (1.0 - (1.0 / float(num)))
    return int(result)


print(findTotientMinimum(1000000))
'''
