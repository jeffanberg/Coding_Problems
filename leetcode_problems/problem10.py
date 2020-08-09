'''Given an input string (s) and a pattern (p), implement regular expression matching
with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.'''


def isMatch(s: str, p: str) -> bool:
    rev_p = p[::-1]
    rev_s = s[::-1]

    while len(rev_p) > 0:
        if rev_p[:1] == "*":
            if rev_p[1:2] == ".":
                return True
                break
            while rev_p[1:2] == rev_s[:1]:
                rev_s = rev_s[1:]
            rev_p = rev_p[2:]
        elif rev_p[:1] == ".":
            rev_s = rev_s[1:]
            rev_p = rev_p[1:]
        else:
            if rev_p[:1] == rev_s[:1]:
                rev_s = rev_s[1:]
                rev_p = rev_p[1:]
            else:
                return False
                break

    if rev_s == rev_p:
        return True
    else: return False


s = "aaa"
p = "ab*a*c*a"


print(isMatch(s,p))


'''
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''