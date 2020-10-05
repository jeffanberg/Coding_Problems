'''
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
'''


def palindrome_check(num):
    forwardstring = str(num)
    backwardstring = forwardstring[::-1]
    if forwardstring == backwardstring:
        return True
    else:
        return False


def palindromeTwoBases(max):
    palindromes = []
    for n in range(1, max):
        if palindrome_check(n) and palindrome_check(bin(n)[2:]):
            palindromes.append(n)
    return palindromes


ans = palindromeTwoBases(1000000)
print(ans)
print(sum(ans))
