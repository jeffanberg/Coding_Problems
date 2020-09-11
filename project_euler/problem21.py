'''
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import math

def properDivisor(x):
    s = 1
    for num in range(2, int(math.sqrt(x)) + 1):
        if x % num == 0:
            s += num
            s += x / num
    return s


def findAmicableNums(limit):
    amicableNums = set()
    for x in range(limit, 0, -1):
        possibleami = properDivisor(x)
        if x != possibleami and properDivisor(possibleami) == x:
            amicableNums.add(x)
            amicableNums.add(possibleami)
    return amicableNums

ami = findAmicableNums(10000)
print(ami)
print(sum(ami))
