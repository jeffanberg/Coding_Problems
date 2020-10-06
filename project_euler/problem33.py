'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''


def digitCancelling():
    curiousfractions = []
    for x in range(10, 99):
        for y in range(x + 1, 100):
            num1 = int(str(x)[0])
            num2 = int(str(x)[1])
            den1 = int(str(y)[0])
            den2 = int(str(y)[1])
            if x % 10 == 0 and y % 10 == 0:
                continue
            elif den1 != 0 and (x / y) == (num1 / den1):
                if num2 == den2:
                    curiousfractions.append(x / y)
                    print(f'{x}/{y} - {num1}/{den1}')
            elif den1 != 0 and (x / y) == (num2 / den1):
                if num1 == den2:
                    curiousfractions.append(x / y)
                    print(f'{x}/{y} - {num2}/{den1}')
            elif den2 != 0 and (x / y) == (num1 / den2):
                if num2 == den1:
                    curiousfractions.append(x / y)
                    print(f'{x}/{y} - {num1}/{den2}')
            elif den2 != 0 and (x / y) == (num2 / den2):
                if num1 == den1:
                    curiousfractions.append(x / y)
                    print(f'{x}/{y} - {num2}/{den2}')
            else:
                continue
    return curiousfractions


ans = 1
for i in digitCancelling():
    ans = ans * i
print(ans)
