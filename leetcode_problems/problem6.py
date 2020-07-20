'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #if number of rows is 1 or greater than string length
        if numRows == 1 or numRows > len(s):
            return s
        #create a string of numrows
        step = 0
        i = 0
        stringline = ['' for rows in range(numRows)]
        #zigzag
        for char in s:
            stringline[i] += char
            if i == 0:
                step = 1
            if i == numRows - 1:
                step = -1
            i += step
        return ''.join(stringline)


Solution().convert('PAYPALISHIRING', 4)