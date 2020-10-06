'''
An irrational decimal fraction is created by concatenating the
positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,
find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
'''


def createChampernowne(max):
    fraction = '0'
    for n in range(1, max + 1):
        fraction = fraction + str(n)
    return fraction


champer = createChampernowne(1000000)
solution = int(champer[1]) * int(champer[10]) * int(champer[100]) * \
    int(champer[1000]) * int(champer[10000]) * int(champer[100000]) * \
    int(champer[1000000])
print(solution)
