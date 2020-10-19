'''
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result
will always be prime. For example, taking 7 and 109, both 7109 and 1097
are prime. The sum of these four primes, 792, represents the lowest sum for
a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
'''

from random import randrange


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
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


def isPair(prime1, prime2):
    if not isPrime(int(str(prime1) + str(prime2))) or \
            not isPrime(int(str(prime2) + str(prime1))):
        return False
    return True


def generatePrimes(limit):
    prime_list = []
    for n in range(3, limit, 2):
        if isPrime(n):
            prime_list.append(n)
    return prime_list


def findPairSet():
    prime_list = generatePrimes(10000)
    for a in prime_list:
        for b in prime_list:
            if b < a:
                continue
            if isPair(a, b):
                for c in prime_list:
                    if c < b:
                        continue
                    if isPair(a, c) and isPair(b, c):
                        for d in prime_list:
                            if d < c:
                                continue
                            if isPair(a, d) and isPair(b, d) and isPair(c, d):
                                for e in prime_list:
                                    if e < d:
                                        continue
                                    if isPair(a, e) and isPair(b, e) and \
                                            isPair(c, e) and isPair(d, e):
                                        return [a, b, c, d, e]


ans = findPairSet()
print(ans)
print(sum(ans))
