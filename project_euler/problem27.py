# Quadratic Primes
# https://projecteuler.net/problem=27

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


# Main quadratic function


def quadraticSearch(a, b):
    primecount = 0
    leader = []
    for i in range((-1 * a), a + 1):
        for x in range((-1 * b), b + 1):
            n = 0
            while True:
                possibleprime = (n * n) + (i * n) + x
                if isPrime(possibleprime):
                    n += 1
                else:
                    if n > primecount:
                        primecount = n
                        leader = [i, x]
                    break
    return leader


a = quadraticSearch(1000, 1000)
print(a)
print(a[0] * a[1])
