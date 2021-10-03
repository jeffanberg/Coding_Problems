''' Project Euler Problem 81

Find the minimal path sum from the top left to the bottom right by only
moving right and down in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing an 80 by 80 matrix.
'''

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'p081_matrix.txt')) as matrix_file:
    matrix = [list(map(int, n.split(','))) for n in
              matrix_file.read().splitlines()]

n, m = len(matrix), len(matrix[0])

for i in range(n):
    for j in range(m):
        matrix[i][j] += (min(matrix[i-1][j], matrix[i][j-1]) if i * j > 0 else
                         (matrix[i - 1][j] if i else (matrix[i][j - 1] if j
                                                      else 0)))

print(matrix[-1][-1])


''' Below is a non-working attempt to use A Star Pathfinding to find
the solution.

class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = int(matrix[position[0]][position[1]])
        self.h = 0
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.position == other.position


def min_sum(matrix):  # Using the A Star Algorithm
    start, end = (0, 0), (79, 79)
    start_node = Node(None, start)
    start_node.g = int(matrix[start_node.position[0]][start_node.position[1]])
    start_node.h = 0
    start_node.f = start_node.g + start_node.h
    end_node = Node(None, end)
    end_node.g = int(matrix[end_node.position[0]][end_node.position[1]])
    end_node.h = 0
    end_node.f = end_node.g + end_node.h

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_position in [(0, 1), (1, 0)]:  # Can only move down or right.

            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])

            if (node_position[0] > (len(matrix) - 1) or node_position[0] < 0 or
                    node_position[1] > (len(matrix[len(matrix) - 1]) - 1) or
                    node_position[1] < 0):
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

        child.g = current_node.g + int(matrix[child.position[0]]
                                             [child.position[1]])
        child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                   ((child.position[1] - end_node.position[1] ** 2)))
        child.f = child.g + child.h

        for open_node in open_list:
            if child == open_node and child.g > open_node.g:
                continue

        open_list.append(child)


path = min_sum(matrix)
print(path)
'''
