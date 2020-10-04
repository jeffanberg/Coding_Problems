'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is
1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way
so be sure to only include it once in your sum.
'''


def isPandigital(multiplicand, multiplier):
    product = multiplicand * multiplier
    identity = str(product) + str(multiplicand) + str(multiplier)
    if sorted(identity) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return product
    else:
        return 0


def findPandigitals():
    pandigital_set = set()
    for x in range(1, 100):
        for y in range(100, 10000):
            pandigital_set.add(isPandigital(x, y))
    return pandigital_set


pandigitals = findPandigitals()
print(pandigitals)
print(sum(pandigitals))
