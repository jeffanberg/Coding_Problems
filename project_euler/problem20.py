'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def factorial(num):
    total = num
    for x in range(num - 1, 0, -1):
        total = x * total
    return total

def sumofdigits(fact):
    sum = 0
    string = str(fact)
    for s in string:
        sum = sum + int(s)
    return sum

print(sumofdigits(factorial(100)))