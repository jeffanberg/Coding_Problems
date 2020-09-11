'''
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by
analysis even though it is known that the greatest number that
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers.
'''
import math


def getDivisors(num):
    if num == 1:
        return 1
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while (divisor < n):
        if (num % divisor == 0):
            total += divisor
            total += num // divisor
        divisor += 1
    if n**2 == num:
        total += n
    return total


def listAbundantNums():
    abundantnums = []
    for i in range(1, 28124):
        if getDivisors(i) > i:
            abundantnums.append(i)
    return abundantnums


def calculateTotalSum():
    total = 0
    totalsum = [0]*28124
    abundantnums = listAbundantNums()
    for x in range(0, len(abundantnums)):
        for y in range(x, len(abundantnums)):
            sumoftwoabundants = abundantnums[x] + abundantnums[y]
            if sumoftwoabundants <= 28123:
                if totalsum[sumoftwoabundants] == 0:
                    totalsum[sumoftwoabundants] = sumoftwoabundants
    for i in range(1, len(totalsum)):
        if totalsum[i] == 0:
            total += i
    return total


print(calculateTotalSum())


# A clever list comprehension from the Euler forums:
'''
import functools, itertools

def get_factors_bar_n(n): return [k for k in set(functools.reduce(list.__add__, ([i,n//i] for i in range(1, int(n**0.5)+1) if n%i==0))) if k!=n]
abundants=[n for n in range(1,28124) if sum(get_factors_bar_n(n))>n]
ab_sums=set([x+y for x,y in itertools.product(abundants, abundants)])
print(sum([n for n in range(1,28124) if n not in ab_sums]))
'''
