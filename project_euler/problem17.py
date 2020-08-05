'''If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, then there are 
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.'''

#one two three four five six seven eight nine ten
#eleven6 twelve6 thirteen8 fourteen8 fifteen7 sixteen7 seventeen9 eighteen8 nineteen8 twenty
#twenty thirty forty fifty sixty seventy eighty ninety

def ones(num):
    if num == 1 or num == 2 or num == 6:
        return 3
    if num == 4 or num == 5 or num == 9:
        return 4
    if num == 3 or num == 7 or num == 8:
        return 5
    if num == 0:
        return 0

def tens(num):
    if num == 0:
        return 0
    if num == 2 or num == 3 or num == 8 or num == 9 or num == 11 or num == 12:
        return 6
    if num == 4 or num == 5 or num == 6:
        return 5
    if num == 7 or num == 15 or num == 16:
        return 7
    if num == 13 or num == 14 or num == 18 or num == 19:
        return 8
    if num == 17:
        return 9
    if num == 10:
        return 3

def hundreds(num):
    return ones(num) + 7

def numberToNumberOfLetters(num):
    numstring = str(num)
    if num == 1000:
        return 11
    if num < 10:
        return ones(num)
    if len(numstring) == 2:
        if num >= 10 and num <= 19:
            return tens(num)
        else: return tens(int(numstring[:1])) + ones(int(numstring[1:]))
    if len(numstring) == 3:
        if int(numstring[1:]) == 0:
            return hundreds(int(numstring[:1]))
        elif int(numstring[1:]) >= 10 and int(numstring[1:]) <= 19: 
            return hundreds(int(numstring[:1])) + tens(int(numstring[1:])) + 3
        else:
            return hundreds(int(numstring[:1])) + tens(int(numstring[1:2])) + ones(int(numstring[2:])) + 3

total = 0
for num in range(1,1001):
    total += numberToNumberOfLetters(num)
print(total)