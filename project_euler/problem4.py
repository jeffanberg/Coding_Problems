'''A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

def palindrome_check(num):
    forwardstring = str(num)
    backwardstring = forwardstring[::-1]
    if forwardstring == backwardstring:
        return True
    else:
        return False

def highest_palindrome():
    palindromes = []
    for num in range(100, 1000):
        for num2 in range(100, 1000):
            if palindrome_check(num * num2):
                palindromes.append(num * num2)
    return max(palindromes)

print(highest_palindrome())