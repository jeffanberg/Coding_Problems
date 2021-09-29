''' Project Euler 79
A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order,
analyse the file so as to determine the shortest possible secret passcode
of unknown length.
'''

import os
from functools import reduce

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'p079_keylog.txt')) as keylog_file:
    keylog_text = keylog_file.read().splitlines()

keylog_text = list(set(keylog_text))

graph = {}
for n in keylog_text:
    for i in range(1, len(n)):
        if not n[i] in graph:
            graph[n[i]] = set()
        graph[n[i]].update(n[i-1])


def topological_sort(graph):
    if len(graph) == 0:
        return
    graph = graph.copy()
    for i, j in graph.items():
        j.discard(i)
    root_nodes = reduce(set.union, graph.values()) - set(graph.keys())
    for r in root_nodes:
        graph[r] = set()
    while True:
        sorting = set(key for key, value in graph.items() if len(value) == 0)
        if len(sorting) == 0:
            break
        yield sorting

        graph = {key: value - sorting for key, value in graph.items()
                 if key not in sorting}


print(list(topological_sort(graph)))


''' Show rate of occurance
first, middle, last = {}, {}, {}

for each in keylog_text:
    if each[0] not in first.keys():
        first.update({each[0]: 1})
    else:
        count_first = first.pop(each[0]) + 1
        first.update({each[0]: count_first})
    if each[1] not in middle.keys():
        middle.update({each[1]: 1})
    else:
        count_middle = middle.pop(each[1]) + 1
        middle.update({each[1]: count_middle})
    if each[2] not in last.keys():
        last.update({each[2]: 1})
    else:
        count_last = last.pop(each[2]) + 1
        last.update({each[2]: count_last})
'''
