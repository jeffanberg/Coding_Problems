''' Euler Problem 69. Nice.
Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are relatively
prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and
relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''
# Using Euler's product formula, could be better optimized filtering for primes


def findTotientMaximum(limit):
    maximum = 0
    ans = 0
    for i in range(2, limit + 1):
        e = i / findTotientProduct(i)
        if e > maximum:
            maximum = e
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


print(findTotientMaximum(1000000))
