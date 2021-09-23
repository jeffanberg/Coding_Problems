''' Project Euler Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written
as a sum of at least two positive integers?
'''


def differentWays(num):
    ways = [1] + [0] * num
    for n in range(1, num):
        for i in range(n, num + 1):
            ways[i] += ways[i - n]
    return ways[num]


print(differentWays(100))
