''' By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number? '''

# Generate prime numbers to a given number. 
from random import randrange

def generatePrimes(num):
    list_of_primes = []
    n = 2
    while len(list_of_primes) != num:
        if isPrime(n):
            list_of_primes.append(n)
            n += 1
        else:
            n += 1
    return list_of_primes

def isPrime(n):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    return millerTest(n)

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

print(max(generatePrimes(10001)))

#alternative way to check if prime:
def is_prime(number):
    for i in range(2, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
    return True