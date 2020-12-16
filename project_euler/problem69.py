''' Euler Problem 69. Nice.
Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are relatively
prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and
relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''
# from math import gcd


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def findTotients(num):
    totients = 0
    for i in range(1, num):
        if gcd(i, num) == 1:
            totients += 1
    return totients


def findTotientMaximum(limit):
    maximum = 0
    for i in range(2, limit + 1):
        if (i / findTotients(i)) > maximum:
            maximum = i
    return maximum


print(findTotientMaximum(1000000))
