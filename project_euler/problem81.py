''' Project Euler Problem 81

Find the minimal path sum from the top left to the bottom right by only
moving right and down in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing an 80 by 80 matrix.
'''

import os
import heapq

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'p081_matrix.txt')) as matrix_file:
    matrix = [list(map(int, n.split(','))) for n in
              matrix_file.read().splitlines()]


''' Using A Star Pathfinding, with guide from-
https://www.redblobgames.com/pathfinding/a-star/implementation.html '''


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Location: x={self.x} y={self.y}'

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return 0


class Matrix:
    def __init__(self):
        self.data = matrix

    @property
    def width(self):
        return len(self.data[0]) if self.data else 0

    @property
    def height(self):
        return len(self.data)

    def get(self, location):
        return self.data[location.y][location.x]

    def neighbors(self, location):
        neighbors = []

        if location .x < self.width - 1:
            neighbors.append(Location(location.x + 1, location.y))

        if location.y < self.height - 1:
            neighbors.append(Location(location.x, location.y + 1))

        return neighbors

    def find_path(self, start, end):
        frontier = PriorityQueue()
        frontier.put(start, self.get(start))
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = self.get(start)

        while not frontier.empty():
            current = frontier.get()

            if current == end:
                break

            for next in self.neighbors(current):
                new_cost = cost_so_far[current] + self.get(next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put(next, priority)
                    came_from[next] = current

        path = [end]
        while path[-1] != start:
            path.append(came_from[path[-1]])
            path.reverse()

        return path, cost_so_far[end]


path, answer = Matrix.find_path(Matrix(), Location(0, 0), Location(79, 79))
print(answer)
