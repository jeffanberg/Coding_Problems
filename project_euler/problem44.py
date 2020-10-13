'''
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their
sum and difference are pentagonal and D = |Pk − Pj| is minimised;
what is the value of D?
'''
from math import sqrt


def generatePentagonals(max):
    pentagonal_list = []
    for n in range(1, max + 1):
        current_pentagonal = n * (3 * n - 1) / 2
        pentagonal_list.append(current_pentagonal)
    return pentagonal_list


def findDistance():
    pentagonal_list = generatePentagonals(3000)
    for i in range(0, len(pentagonal_list)):
        current = pentagonal_list[i]
        for n in range(i + 1, len(pentagonal_list)):
            compare = pentagonal_list[n]
            if ((sqrt(24 * (current + compare) + 1) + 1) / 6) % 1 == 0:
                if ((sqrt(24 * (compare - current) + 1) + 1) / 6) % 1 == 0:
                    return compare - current


print(findDistance())
