'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''


def factorial(num):
    if num == 0:
        return 1
    total = num
    for x in range(num - 1, 0, -1):
        total = x * total
    return total


fact_dict = dict()
for n in range(0, 10):
    fact_dict.update({n: factorial(n)})


def isSumOfDigits(num):
    num_str = str(num)
    sum = 0
    for i in num_str:
        sum += fact_dict.get(int(i))
    if sum == num:
        return True
    else:
        return False


def digitFactorial(max):
    curiousnumbers = []
    for x in range(3, max):
        if isSumOfDigits(x):
            curiousnumbers.append(x)
    return curiousnumbers


print(sum(digitFactorial(fact_dict.get(9) * 7)))
