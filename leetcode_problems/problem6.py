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
        #create a matrix of numrows
        stringmatrix = [0] * (len(s) // 2)
        for x in range((len(s) // 2)):
            stringmatrix[x] = [0] * numRows
        
        print(stringmatrix)


Solution().convert('PAYPALISHIRING', 4)