'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million,
can be written as the sum of the most consecutive primes?
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


def generatePrimes(limit):
    prime_list = [2, 3, 5, 7, 11]
    for n in range(13, (limit // 2), 2):
        if isPrime(n):
            prime_list.append(n)
    return prime_list


def findConsecutivePrimeSum(limit):
    ans = 0
    sum_length = 0
    prime_list = generatePrimes(limit)
    if limit % 2 == 0:
        limit -= 1
    for n in range(limit, 1000, -1):
        if isPrime(n):
            for c in range(0, len(prime_list)):
                count = 0
                while count < len(prime_list):
                    seq = prime_list[c:len(prime_list) - count]
                    if len(seq) > sum_length:
                        if sum(seq) == n:
                            ans = n
                            sum_length = len(seq)
                            print(f'length: {sum_length} prime: {ans}')
                            break
                    count += 1
    return ans


def findLongestPrimeSum(limit):
    prime_list = [2, 3, 5, 7, 11]
    n = 13
    while sum(prime_list) < limit:
        if isPrime(n):
            prime_list.append(n)
        n = n + 2
    seq = []
    p_len = len(prime_list)
    i = p_len
    while i != 0:
        n = 0
        while n + i < p_len + 1:
            temp_seq = prime_list[n: n+i]
            if sum(temp_seq) <= limit:
                if isPrime(sum(temp_seq)):
                    if len(temp_seq) > len(seq):
                        seq = temp_seq
            n = n + 1
        i = i - 1
    return sum(seq)


# print(findConsecutivePrimeSum(1000))
print(findLongestPrimeSum(1000000))
