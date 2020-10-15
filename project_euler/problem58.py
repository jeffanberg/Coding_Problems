'''
Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the
bottom right diagonal, but what is more interesting is that
8 out of the 13 numbers lying along both diagonals are prime;
that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed.
If this process is continued, what is the side length of the square spiral
for which the ratio of primes along both diagonals first falls below 10%?
'''
# f(n) = 4(2n+1)^2 - 12n + f(n-1)

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


def findSpiralPrimes():
    prime_count = 3
    spiral_length = 2
    n = 9
    while prime_count / (2 * spiral_length + 1) > 0.1:
        spiral_length += 2
        for _ in range(0, 3):
            n += spiral_length
            if isPrime(n):
                prime_count += 1
        n += spiral_length
    return spiral_length + 1


print(findSpiralPrimes())
