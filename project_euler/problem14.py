'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

mem = dict()

def collatz(num):
    global mem
    length = 0
    while num != 1:
        if num in mem:
            return mem[num] + length
        length += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
    return length + 1

def longest_collatz(num):
    longest = 0
    ans = 0
    for each in range(1,num):
        x = collatz(each)
        mem[each] = x
        if x > longest:
            ans = each
            longest = x
    return ans

print(longest_collatz(1000000))