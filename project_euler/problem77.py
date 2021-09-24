'''
It is possible to write ten as the sum of primes in exactly five different ways

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five
thousand different ways?
'''

from isPrime import isPrime


def primeWays(primes, i, num):
    if num == 0:
        return 1
    if num < 0:
        return 0
    if i <= 0 and num >= 1:
        return 0
    return primeWays(primes, i - 1, num) + primeWays(primes, i,
                                                     num - primes[i - 1])


def generatePrimes(limit):
    prime_list = [2, 3, 5, 7, 11]
    for n in range(13, (limit // 2), 2):
        if isPrime(n):
            prime_list.append(n)
    return prime_list


def findAnswer(limit):
    ways = 0
    number = 2
    while ways < limit:
        number += 1
        primes = generatePrimes(number * 100)
        ways = primeWays(primes, len(primes), number)
    return number


print(findAnswer(5000))
