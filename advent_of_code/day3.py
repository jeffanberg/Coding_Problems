'''
Day 3 Advent of Code
https://adventofcode.com/2020/day/3
'''

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'day3_input.txt')) as slope_file:
    slope = [lines for lines in slope_file.read().split('\n') if lines.strip()]

# Solution 1


def findTrees(down, right):
    position = [0, 0]
    treecount = 0
    while position[0] < len(slope):
        # Check if there's a tree
        if slope[position[0]][position[1]] == '#':
            treecount += 1
        # Go to next position
        position[0] += down
        position[1] += right
        if position[1] > len(slope[0][0]):
            position[1] = position[1] - 31
    return treecount


print(f'Number of trees encountered: {findTrees(1, 3)}')

# Solution 2

multipleslopes = (findTrees(1, 1) * findTrees(1, 3) * findTrees(1, 5)
                  * findTrees(1, 7) * findTrees(2, 1))

print(f'Number of trees encountered on multiple slopes: {multipleslopes}')
