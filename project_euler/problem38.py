'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by
1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the
concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''


def isPandigital(num_string):
    if sorted(num_string) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    else:
        return False


def findLargestMultiple(max):
    largestpandigital = 0
    for n in range(max + 1):
        product = 1
        temp = ''
        while len(temp) < 10 and product <= 9:
            temp = temp + str(n * product)
            if isPandigital(temp):
                if int(temp) > largestpandigital:
                    largestpandigital = int(temp)
                break
            product += 1
    return largestpandigital


print(findLargestMultiple(10000))
