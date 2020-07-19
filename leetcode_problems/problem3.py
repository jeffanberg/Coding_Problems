# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_dict = {}
        maxlength, start = 0, 0
        for index, value in enumerate(s):
            if value in new_dict:
                total = new_dict[value] + 1
                if total > start:
                    start = total
            num = index - start + 1
            if num > maxlength:
                maxlength = num
            new_dict[value] = index
        return maxlength