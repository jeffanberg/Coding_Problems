'''
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''


def findSolutions(value):
    max_solutions = 0
    max_value = 0
    for p in range(1, value + 1):
        num_of_solutions = len(findPyTriplet(p))
        if num_of_solutions > max_solutions:
            max_solutions = num_of_solutions
            max_value = p
    return max_value


def divisors(n):
    for divisor in range(1, int(n**0.5) + 1):
        if n % divisor == 0:
            yield divisor, n//divisor


def findPyTriplet(num):
    pn = {}
    i = 0
    for r in range(2, 550, 2):
        st = r*r // 2
        for s, t in divisors(st):
            x = (r+s) + (r+t) + (r+s+t)
            if x == num:
                a = (r+s)
                b = (r+t)
                c = (r+s+t)
                pn[i] = [a, b, c]
                i += 1
    return pn


print(findSolutions(1000))
