'''Given an input string (s) and a pattern (p), implement regular expression matching
with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.'''


def isMatch(s: str, p: str) -> bool:
    stillMatches = True
    s_index = 0
    for char in range(len(p)):
        if char < len(p) - 1:
            if p[char + 1] == "*":
                continue

        if p[char] == ".":
            s_index += 1
            continue
        elif p[char] == "*":
            if s[s_index] == p[char - 1]:
                s_index += 1
                continue
        else:
            if s[s_index] != p[char]:
                stillMatches = False
            else:
                s_index += 1
    if s_index != len(s) - 1:
        stillMatches = False      
    return stillMatches

s = "aaaaaa"
p = "a*"

print(isMatch(s,p))