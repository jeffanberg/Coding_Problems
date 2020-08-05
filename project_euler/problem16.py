'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
largenumstring = str(pow(2, 1000))
largenumsum = 0

for char in range(len(largenumstring)):
    largenumsum += int(largenumstring[char])

print (largenumsum)