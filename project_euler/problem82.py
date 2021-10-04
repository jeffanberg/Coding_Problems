''' Project Euler Problem 82
by starting in any cell in the left column and finishing in any cell
in the right column, and only moving up, down, and right.
'''

import os
import heapq

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'p083_matrix.txt')) as matrix_file:
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

        if location.x < self.width - 1:
            neighbors.append(Location(location.x + 1, location.y))

        if location.y < self.height - 1:
            neighbors.append(Location(location.x, location.y + 1))

        if location.y - 1 > -1:
            neighbors.append(Location(location.x, location.y - 1))

        return neighbors

    def find_path(self):
        minimum_cost = 0
        minimum_path = []
        minimum_start = Location(0, 0)
        min_camefrom = dict()
        for y in range(0, 80):
            start = Location(0, y)
            frontier = PriorityQueue()
            frontier.put(start, self.get(start))
            came_from = dict()
            cost_so_far = dict()
            came_from[start] = None
            cost_so_far[start] = self.get(start)

            while not frontier.empty():
                current = frontier.get()

                if current.x == 79:
                    end = current
                    break

                for next in self.neighbors(current):
                    new_cost = cost_so_far[current] + self.get(next)
                    if next not in cost_so_far or new_cost < cost_so_far[next]:
                        cost_so_far[next] = new_cost
                        priority = new_cost
                        frontier.put(next, priority)
                        came_from[next] = current

            if minimum_cost == 0 or cost_so_far[end] < minimum_cost:
                minimum_cost = cost_so_far[end]
                minimum_path = [end]
                minimum_start = start
                min_camefrom = came_from

        path = minimum_path
        while path[-1] != minimum_start:
            path.append(min_camefrom[path[-1]])
            path.reverse()

        return path, minimum_cost

    def print_path(self, path):
        for y in range(self.height):
            line = ''
            for x in range(self.width):
                location = Location(x, y)
                if location in path:
                    line += 'x'
                else:
                    line += '.'
            print(line)


path, answer = Matrix.find_path(Matrix())
Matrix.print_path(Matrix(), path)
print(answer)
