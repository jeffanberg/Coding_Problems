'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

def findPyTriplet(num):
    total = 0
    c, m = 0, 2
    while c < num:
        #generate triplets to test
        for n in range(1, m):
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n
            
            if c > num:
                break

            total = a + b + c
            if total == num:
                triplets = sorted([a, b, c])
                print ("Product: " + str(a * b *c))

        m = m + 1

    return triplets

print(findPyTriplet(1000))

###also:

def divisors(n):
    for divisor in range(1, int(n**0.5) + 1):
        if n % divisor == 0:
            yield divisor, n//divisor

def findPyTriplet2(num):

    pn = {}
    for r in range(2, 550, 2):
        st = r*r // 2
        for s, t in divisors(st):
            x = (r+s) + (r+t) + (r+s+t)
            if x == num:
                pn[x] = (r+s) * (r+t) * (r+s+t)
                print(f"a: {r+s} b: {r+t} c: {r+s+t}")

    return pn

print(findPyTriplet2(1000))