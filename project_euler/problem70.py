''' Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of positive numbers less than or equal to n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number,
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that
87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n
and the ratio n/φ(n) produces a minimum. '''


def findTotientMinimum(limit):
    minimum = 10000
    ans = 0
    for i in range(2, limit):
        if set(str(i)) == set(str(findTotientProduct(i))):
            e = i / findTotientProduct(i)
            if e < minimum:
                minimum = e
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


print(findTotientMinimum(1000000))
