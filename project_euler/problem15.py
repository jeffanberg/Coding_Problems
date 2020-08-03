'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

def numOfPaths(gridSize):
    i = 1
    c = 1
    while i <= gridSize:
        c = c * (gridSize + i) / i
        i += 1
    return c


print(numOfPaths(20))
