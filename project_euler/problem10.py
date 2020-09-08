'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def is_prime(number):
    for i in range(2, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
    return True

def generatePrimes(num):
    list_of_primes = []
    n = 2
    while n < num + 1:
        if is_prime(n):
            list_of_primes.append(n)
            n += 1
        else:
            n += 1
    return list_of_primes

print(sum(generatePrimes(2000000)))

