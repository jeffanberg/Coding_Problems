'''
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among
the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
'''

from random import randrange


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
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


def findPrimeFamily(size):
    if size == 6:
        num = 13
    elif size == 7:
        num = 10001
    else:
        num = 100001
    prime_family = []
    while True:
        if isPrime(num):
            for list_of_perms in replaceDigits(num):
                for n in list_of_perms:
                    if isPrime(n):
                        prime_family.append(n)
                    if len(prime_family) >= size:
                        return sorted(prime_family)
                prime_family = []
        num += 2


def replaceDigits(num):
    num_string = str(num)
    last_digit = ['1', '3', '7', '9']
    permutations = []
    ans = []
    if num_string[-1] not in last_digit:
        return []
    for i in range(0, 5):
        for r in range(0, 5):
            if r == i:
                pass
            else:
                for x in range(0, 10):
                    num_list = list(num_string)
                    for n in range(len(num_list) - 1):
                        if n == i or n == r:
                            pass
                        else:
                            num_list[n] = str(x)
                    replace_num = int(''.join(num_list))
                    if len(str(replace_num)) == len(num_string) and \
                            replace_num not in permutations:
                        permutations.append(replace_num)
                if permutations not in ans:
                    ans.append(permutations)
                permutations = []
    return ans


print(findPrimeFamily(8))
