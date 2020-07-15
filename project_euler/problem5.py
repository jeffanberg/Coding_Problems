'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

def smallestmultiple():
    n = 20
    counter = 0
    while counter < 20:
        for i in range(1, 21):
            if n % i == 0:
                counter += 1
            else:
                n += 1
                counter = 0
    return n

#print(smallestmultiple())

""" This one is better/faster
n = 2*3*5*7*11*13*17
while all(n % i == 0 for i in range(1, 21)) is False:
    n = n + 2*3*5*7*11*13*17
print(n) 
"""