'''
Advent of Code Day 5
https://adventofcode.com/2020/day/5
'''

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'day5_input.txt')) as bp_file:
    boardingpasses = [p for p in bp_file.read().split('\n') if p.strip()]


def findSeatID(boardingpass):
    row = list(range(128))
    column = list(range(8))
    for x in boardingpass:
        if x == 'F':
            row = row[:(len(row) // 2)]
        elif x == 'B':
            row = row[(len(row) // 2):]
        elif x == 'L':
            column = column[:(len(column) // 2)]
        elif x == 'R':
            column = column[(len(column) // 2):]
    return row[0] * 8 + column[0]


def findHighestSeatID(list_of_passes):
    maximum = 0
    for p in list_of_passes:
        if findSeatID(p) > maximum:
            maximum = findSeatID(p)
    return maximum


# Solution 1
print(f'Solution 1: The highest seat ID: {findHighestSeatID(boardingpasses)}')


def findMissingSeat(list_of_passes):
    list_of_seats = []
    for b in list_of_passes:
        list_of_seats.append(findSeatID(b))
    list_of_seats = sorted(list_of_seats)
    for i in range(len(list_of_seats)):
        if list_of_seats[i + 1] - 1 != list_of_seats[i]:
            return list_of_seats[i] + 1


# Solution 2
print(f'Solution 2: The missing seat ID: {findMissingSeat(boardingpasses)}')
