'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence
to contain 1000 digits?
'''


def fibonacciseq():
    twoagonum = 1
    prevnum = 2
    newnum = 0
    fib_list = [1, twoagonum, prevnum]
    while True:
        newnum = twoagonum + prevnum
        if len(str(newnum)) < 1000:
            fib_list.append(newnum)
        else:
            fib_list.append(newnum)
            return fib_list.index(newnum, -1) + 1
        twoagonum = prevnum
        prevnum = newnum


print(fibonacciseq())
