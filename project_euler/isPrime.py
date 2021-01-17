from random import randrange

'''Uses the Rabin-Miller algorithm to determine whether a number is
prime.'''


def millerTest(num):
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1

    for _ in range(5):
        a = randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != num - 1:
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = (v ** 2) % num
    return True


def isPrime(number):
    if number <= 1 or number == 4:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    return millerTest(number)
