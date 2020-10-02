'''
Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
'''
# f(n) = 4(2n+1)^2 - 12n + f(n-1)


def sumOfDiagonalCorners(x):
    x = (x - 1) // 2
    currentSum = 1
    for n in range(x, 0, -1):
        currentSum += 4 * ((2 * n + 1) ** 2) - 12 * n
    return currentSum


print(sumOfDiagonalCorners(1001))
