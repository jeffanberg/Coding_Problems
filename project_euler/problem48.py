'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''


def selfPowers(limit):
    sum = 0
    for n in range(1, limit + 1):
        sum += n ** n
    return sum


ans = str(selfPowers(1000))
print(ans[-10:])
