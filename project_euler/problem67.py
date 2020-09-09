import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'p067_triangle.txt')) as triangle_file:
    triangle_raw = triangle_file.read()
    triangle_raw = triangle_raw.strip().split('\n')
    for i in range(1, len(triangle_raw)):
        triangle_raw[i] = triangle_raw[i].strip().split(' ')
        triangle_raw[i] = [int(x) for x in triangle_raw[i]]
triangle = triangle_raw
triangle[0] = [59]

print(triangle)

# Dynamic method

def maxSum(triangle_array):
    while True:
        lastLine = triangle_array[-1]
        tempValue = 0
        for i in range(len(lastLine) - 1):
            tempValue = lastLine[i] if lastLine[i] > lastLine[i + 1] else lastLine[i + 1]
            triangle_array[-2][i] += tempValue
        triangle_array.pop()

        if len(triangle_array) == 1:
            return triangle_array[0][0]

print(maxSum(triangle))

