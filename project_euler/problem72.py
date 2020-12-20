# Euler Problem 72: Counting fractions

def toitient(num):
    result = num
    p = 2
    while p * p <= num:
        if num % p == 0:
            while num % p == 0:
                num = num // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
    if num > 1:
        result = result * (1.0 - (1.0 / float(num)))
    return int(result)


def countFoley(limit):
    count = 2
    f = 1
    while limit >= f:
        count = count + toitient(f)
        f += 1
    return count - 1


# Subtract 2 from the foley length to eliminate 0/1 and 1/1
print(countFoley(10 ** 6) - 2)
