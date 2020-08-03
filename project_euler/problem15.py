'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

def numOfPaths(gridSize):
    c = 1
    for i in range(1, gridSize + 1):
        c = c * (gridSize + i) / i
    return c


print(numOfPaths(20))
