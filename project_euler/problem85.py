''' Project Euler Problem 85
By counting carefully it can be seen that a rectangular grid measuring 3 by 2
contains eighteen rectangles.

Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution.
'''


def count_rectangles(x, y):
    return int((x * (x + 1) / 2) * (y * (y + 1) / 2))


closest_to_2mill = 100000000
answer = []

for x in range(1, 2000):
    for y in range(1, 2000):
        current = count_rectangles(x, y)
        if abs(current - 2000000) < closest_to_2mill:
            closest_to_2mill = abs(current - 2000000)
            answer = [x, y]

print(answer)

print(f'Area: {answer[0] * answer[1]}')
