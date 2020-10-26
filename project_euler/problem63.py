'''
The 5-digit number, 16807=7^5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

powerful_digits = []
power = 1

while power < 100:
    n = 1
    current = 0
    while len(str(current)) <= power:
        current = pow(n, power)
        if len(str(current)) == power:
            powerful_digits.append(current)
        n += 1
    power += 1

print(powerful_digits)
print(len(powerful_digits))
