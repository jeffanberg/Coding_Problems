'''
Day 2: Password Philosophy
'''

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'day2_input.txt')) as password_file:
    passwords = [p for p in password_file.read().split('\n') if p.strip()]


# Solution 1

def validPasswords(passwords):
    list_of_passes = passwords
    valid_count = 0
    for entry in list_of_passes:
        # Split the entry into its parts
        i, p = entry.split(': ')[0], entry.split(': ')[-1]
        r, v = i.split(' ')[0], i.split(' ')[-1]
        low, high = r.split('-')[0], r.split('-')[-1]
        occurances = len(list(filter(lambda variable: v in variable, p)))
        if occurances >= int(low) and occurances <= int(high):
            valid_count += 1
    return valid_count

# Solution 2


def passwordPosition(passwords):
    list_of_passes = passwords
    valid_count = 0
    for entry in list_of_passes:
        # Split the entry into its parts
        i, p = entry.split(': ')[0], entry.split(': ')[-1]
        r, v = i.split(' ')[0], i.split(' ')[-1]
        position_one = int(r.split('-')[0])
        position_two = int(r.split('-')[-1])
        if position_one > len(p) or position_two > len(p):
            pass
        elif p[position_one - 1] == v and p[position_two - 1] != v:
            valid_count += 1
        elif p[position_one - 1] != v and p[position_two - 1] == v:
            valid_count += 1
        else:
            pass
    return valid_count


print('Solution 1: ' + str(validPasswords(passwords)))
print('Solution 2: ' + str(passwordPosition(passwords)))
