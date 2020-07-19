'''Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s==s[::-1]:
            return s
        start, maxlength = -1, 0
        for i in range(len(s)):
            odd = s[i - maxlength - 1:i + 1]
            even = s[i - maxlength:i + 1]
            if i - maxlength - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlength - 1
                maxlength += 2
                continue
            if i - maxlength >= 0 and even == even[::-1]:
                start = i - maxlength
                maxlength += 1
        return s[start:start+maxlength]