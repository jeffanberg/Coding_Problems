'''Given an input string (s) and a pattern (p), implement regular expression matching
with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.'''

def isMatch(s: str, p: str) -> bool:
    cache = {}
    def bt(x, y):
        if (x, y) not in cache:
            if y == len(p):
                ans = x == len(s)
            else:
                match = x < len(s) and p[y] in {s[x], '.'}
                if y + 1 < len(p) and p[y+1] == '*':
                    ans = bt(x, y + 2) or match and bt(x + 1, y)
                else:
                    ans = match and bt(x + 1, y + 1)
            cache[x, y] = ans
        return cache[x, y]

    return bt(0, 0)


s = 'aab'
p = 'c*a*b'

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

'''
def isMatch(s: str, p: str) -> bool:
    rev_p = p[::-1]
    rev_s = s[::-1]

    expunged = set()

    if set(p) == {'.','*'} and p.count('*') == p.count('.'):
        return True

    if p[:1] != s[:1] and p[1:2] != "*" and p[:1] != ".":
        return False

    while len(rev_p) > 0:
        if rev_p[:1] == "*":
            if rev_p[1:2] == "." and len(rev_s) > 0:
                if rev_p[2:] != '' and rev_p[2] != '.':
                    while rev_p[2] != rev_s[:1]:
                        expunged.add(rev_s[:1])
                        rev_s = rev_s[1:]
                        if len(rev_s) == 0:
                            rev_p = rev_p[2:]
                            break
                    rev_p = rev_p[2:]
                    continue
                else:
                    return True
                    break
            while rev_p[1:2] == rev_s[:1]:
                expunged.add(rev_s[:1])
                rev_s = rev_s[1:]
            rev_p = rev_p[2:]
        elif rev_p[:1] == ".":
            if rev_s == '':
                if len(expunged) > (p.count('.') - p.count('.*')) and len(rev_p) > 0:
                    return True
                return False
                break
            rev_s = rev_s[1:]
            rev_p = rev_p[1:]
        else:
            if rev_p[:1] == rev_s[:1]:
                rev_s = rev_s[1:]
                rev_p = rev_p[1:]
            elif rev_p[0] in expunged:
                rev_p = rev_p[1:]
            elif rev_p in expunged and rev_p > rev_s:
                return True
                break
            else:
                return False
                break
    if rev_s == rev_p:
        return True
    else: return False
    '''