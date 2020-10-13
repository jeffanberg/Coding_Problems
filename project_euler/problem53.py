'''
https://projecteuler.net/problem=53
'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def combinatoric(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


values_over_a_million = []
for n in range(1, 101):
    for r in range(1, n + 1):
        current_value = combinatoric(n, r)
        if current_value > 1000000:
            values_over_a_million.append(current_value)

print(len(values_over_a_million))
