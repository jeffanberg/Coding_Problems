    '''
The nth term of the sequence of triangle numbers is given by,
t_n = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10.
If the word value is a triangle number then we shall call the word
a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
'''

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'p042_words.txt')) as words_file:
    words = words_file.read().replace('"', '').split(',')


def convertCharToInt(char):
    stringtoint = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
                   'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
                   'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                   'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
                   }
    return stringtoint.get(char)


def wordSum(word):
    totalsum = 0
    for i in word:
        for x in i:
            totalsum += convertCharToInt(x)
    return totalsum


def generateTriangleNumbers(max):
    triangle_list = []
    for n in range(1, max + 1):
        triangle_list.append(int((0.5 * n) * (n + 1)))
    return triangle_list


triangle_numbers = generateTriangleNumbers(100)
triangle_words = []
for w in words:
    if wordSum(w) in triangle_numbers:
        triangle_words.append(w)
print(len(triangle_words))
