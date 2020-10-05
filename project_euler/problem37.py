'''
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

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


def ifTruncatablePrime(num):
    stillprime = True
    if isPrime(num):
        temp = str(num)[1:]
        while len(temp) > 1:
            if isPrime(int(temp)) is False:
                stillprime = False
                break
            else:
                temp = temp[1:]
        tempRight = str(num)[:-1]
        while len(tempRight) > 1:
            if isPrime(int(tempRight)) is False:
                stillprime = False
                break
            else:
                tempRight = tempRight[:-1]
    else:
        stillprime = False
    return stillprime


def findTruncatablePrimes():
    count = 0
    num = 11
    truncatableprimes = []
    first_primes = ['2', '3', '5', '7']
    while count < 11:
        if str(num)[0] not in first_primes or \
                str(num)[-1] not in first_primes:
            pass
        elif ifTruncatablePrime(num):
            truncatableprimes.append(num)
            count += 1
        num += 2
    return truncatableprimes


ans = findTruncatablePrimes()
print(ans)
print(sum(ans))
