'''
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''
from itertools import permutations


def findSmallestPermutedMultiple():
    n = 100000
    while True:
        perms = set()
        for perm in permutations(str(n)):
            temp = int(''.join(perm))
            if len(''.join(perm)) == len(str(n)):
                perms.add(temp)
        if n*2 in perms and n*3 in perms and n*4 in perms and n*5 in perms \
                and n*6 in perms:
            return n
        else:
            n += 1


def usingSets():
    n = 100000
    while True:
        if set(str(6*n)) == set(str(5*n)) == set(str(4*n)) == set(str(3*n)) \
                == set(str(2*n)):
            return n
        else:
            n += 1


print(usingSets())
