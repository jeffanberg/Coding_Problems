'''
Advent of Code Day 7
https://adventofcode.com/2020/day/7
'''

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'day7_input.txt')) as bags_file:
    bag_rules = [p for p in bags_file.read().split('\n') if p.strip()]


print(bag_rules)
