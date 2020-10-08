'''
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as
the sum of a prime and twice a square?
'''
from collections import defaultdict
from itertools import count


def findSmallestNonGoldbach():
    factors = defaultdict(list)
    witness = {}
    primes = set()
    for n in count(2):
        if factors[n]:
            for m in factors.pop(n):
                factors[n+m].append(m)
            if n % 2:
                for k in range(1, int((n / 2) ** .5) + 1):
                    p = n - 2 * k ** 2
                    if p in primes:
                        witness[n] = k
                        break
                if n not in witness:
                    break
        else:
            factors[n * n].append(n)
            primes.add(n)
    return n


print(findSmallestNonGoldbach())
