'''
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''


def properDivisor(x):
    tempList = []
    for num in range(1, x):
        if (x / num) % 1 == 0:
            tempList.append(num)
    return sum(tempList)


def findAmicableNums(limit):
    amicableNums = set()
    checked = set()
    for x in range(limit, 1, -1):
        if x not in checked:
            print('Checking: ' + str(x))
            possibleami = properDivisor(x)
            possibleami2 = properDivisor(possibleami)
            checked.add(possibleami2)
            checked.add(possibleami)
            if possibleami2 == possibleami:
                amicableNums.add(possibleami)
                amicableNums.add(possibleami2)
    return amicableNums


print(properDivisor(220))
print(properDivisor(properDivisor(220)))

# print(findAmicableNums(1000))
# print(sum(findAmicableNums(10000)))
