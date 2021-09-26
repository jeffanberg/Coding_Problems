'''
Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into piles
in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
'''


def divisibleBy(num):
    k = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 250)], [])
    sign = [1, 1, -1, -1]
    p, n = [1], 0
    while p[n] > 0:
        n += 1
        px, i = 0, 0
        while k[i] <= n:
            px += p[int(n - k[i])] * sign[i % 4]
            i += 1
        p.append(px % num)
    return n


print(divisibleBy(1000000))
