'''
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result
will always be prime. For example, taking 7 and 109, both 7109 and 1097
are prime. The sum of these four primes, 792, represents the lowest sum for
a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
'''

from isPrime import isPrime
from itertools import combinations


def isPairSet(prime_list):
    for prime in prime_list:
        for i in range(len(prime_list)):
            if prime_list[i] == prime:
                pass
            else:
                if not isPrime(int(str(prime) + str(prime_list[i]))) or \
                        not isPrime(int(str(prime_list[i]) + str(prime))):
                    return False
    return True


def generatePrimes(limit):
    prime_list = []
    for n in range(3, limit, 2):
        if isPrime(n):
            prime_list.append(n)
    return prime_list


def findPairSet(set_length):
    prime_list = generatePrimes(10000)
    for c in combinations(prime_list, set_length):
        if isPairSet(c):
            return c


ans = findPairSet(4)
print(ans)
print(sum(ans))
