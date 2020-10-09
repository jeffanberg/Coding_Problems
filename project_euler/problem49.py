'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms
in this sequence?
'''
from random import randrange
from itertools import permutations


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


def findPrimePermutations():
    prime_list = []
    for n in range(1001, 10000):
        if isPrime(n):
            prime_list.append(n)
    prime_sequence = []
    for x in prime_list:
        possible_seq = [str(x)]
        for p in [''.join(perm) for perm in permutations(str(x))]:
            if int(p) in prime_list:
                possible_seq.append(p)
        if len(possible_seq) >= 3:
            diff = dict()
            for i in range(len(possible_seq)):
                for n in range(i + 1, len(possible_seq)):
                    current_diff = int(possible_seq[n]) - int(possible_seq[i])
                    print(f'current_diff: {current_diff} = {possible_seq[n]} - {possible_seq[i]}')
                    if current_diff in diff.values():
                        prime_sequence.append(str(list(diff.keys())[list(diff.values()).index(current_diff)]) + str(possible_seq[n]) + str(possible_seq[i]))
                    else:
                        diff.update({possible_seq[i]:(int(possible_seq[n]) - int(possible_seq[i]))})
        return prime_sequence


print(findPrimePermutations())