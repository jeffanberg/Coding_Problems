# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

def palindrome_check(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

print(palindrome_check(121))