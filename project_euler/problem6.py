'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares
of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.'''

def findSumOfSquares(num):
    x = 0
    for i in range(1, num+1):
        x += i ** 2
    return x

def findSquareOfSum(num):
    x = 0
    for i in range(1, num+1):
        x += i
    x = x ** 2
    return x

sum_of_squares = findSumOfSquares(100)
square_of_sum = findSquareOfSum(100)
the_difference = square_of_sum - sum_of_squares

print("The difference between the sum of the squares: "
        "of the first hundred natural numbers and the square of the sum is "
        f"{square_of_sum} - {sum_of_squares} = {the_difference}")

''' The MATH way to do it:
sum = 0
for i in range(1,101):
	for j in range(i+1,101):
		sum += 2*i*j
print(sum) '''