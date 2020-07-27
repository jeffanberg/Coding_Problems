'''Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary
until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign
followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, 
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1].
If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.'''
import re

class Solution:
    def myAtoi(self, str: str) -> int:
        res = str
        num = ''
        negative = False
        if not re.findall('[0-9]', res):
                return 0
        while True:
            if res[0] == ' ':
                res = res[1:]
            elif res[0] == '-' and re.findall('[0-9]', res[1]):
                negative = True
                res = res[1:]
            elif res[0] == '+' and re.findall('[0-9]', res[1]):
                res = res[1:]
            elif re.findall('[0-9]', res[0]):
                num = num + res[0]
                if len(res) > 1 and re.findall('[0-9]', res[1]):
                    res = res[1:]
                else:
                    break
            else:
                break
        if len(num) > 0:
            num = int(num)
        else:
            return 0
        if negative:
            num = num * -1
        if num > pow(2,31) - 1:
            return pow(2,31) - 1
        elif num < pow(2,31) * -1:
            return pow(2,31) * -1
        else:
            return num
    
print(Solution().myAtoi("0-1"))