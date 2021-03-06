'''
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100,
what is the maximum digital sum?
'''


def maximumDigitalSum(a, b):
    return sum([int(n) for n in str(pow(a, b))])


maximum = 0
for a in range(1, 100):
    for b in range(1, 100):
        if maximumDigitalSum(a, b) > maximum:
            maximum = maximumDigitalSum(a, b)
print(maximum)
