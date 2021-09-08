''' Problem 74: Digit Factorial Chains '''

import math


def factorize(n):
    number = list(str(n))
    result = 0
    for each in number:
        result += math.factorial(int(each))
    return result


def factorialChain(n):
    terms = set()
    while True:
        if n not in terms:
            terms.add(n)
            n = factorize(n)
        else:
            break
    return len(terms)


def exactlySixty(limit):
    i = 0
    count = 0
    while i < limit:
        if factorialChain(i) == 60:
            count += 1
            i += 1
        else:
            i += 1
    return count


print(exactlySixty(1000000))
