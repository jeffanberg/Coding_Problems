'''
Advent of Code Day 6
https://adventofcode.com/2020/day/6
'''

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'day6_input.txt')) as customs_file:
    answers = [p for p in customs_file.read().split('\n\n') if p.strip()]
    answers_smushed = [c.replace('\n', '') for c in answers]


def yesSum(answers):
    count = 0
    for a in answers:
        count += len(set(list(a)))
    return count


# Solution 1
print(yesSum(answers_smushed))

answers_grouped = [c.split('\n') for c in answers]
answers_grouped[-1].pop(-1)


def everyoneYesSum(answers):
    count = 0
    for a in answers:
        current = set(list(a[0]))
        if len(a) > 1:
            i = 1
            while i < len(a):
                current = current & set(list(a[i]))
                i += 1
        count += len(current)
    return count


# Solution 2
print(everyoneYesSum(answers_grouped))
