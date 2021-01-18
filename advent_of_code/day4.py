'''
Advent of Code Day 4
https://adventofcode.com/2020/day/4
'''

import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'day4_input.txt')) as passport_file:
    passports = [p for p in passport_file.read().split('\n\n') if p.strip()]


def sanitizePassports(list_of_passports):
    sanitized_passports = dict()
    for i in range(len(list_of_passports)):
        current = [p for p in
                   list_of_passports[i].replace('\n', ' ').split(' ')
                   if p.strip()]
        passport = dict()
        for field in current:
            key = field.split(':')[0]
            value = field.split(':')[-1]
            passport.update({str(f'{key}'): value})
        sanitized_passports.update({str(f'passport{i}'): passport})
    return sanitized_passports

# Solution 1


def validPassports1(dict_of_passports):
    valid_passport_count = 0
    for p in dict_of_passports.values():
        keys = p.keys()
        if len(keys) == 8:
            valid_passport_count += 1
        elif len(keys) == 7 and 'cid' not in keys:
            valid_passport_count += 1
    return valid_passport_count


print((validPassports1(sanitizePassports(passports))))


# Solution 2

def checkBirth(value):
    if value >= 1920 and value <= 2002:
        return True
    else:
        return False


def checkIssue(value):
    if value >= 2010 and value <= 2020:
        return True
    else:
        return False


def checkExpiration(value):
    if value >= 2020 and value <= 2030:
        return True
    else:
        return False


def checkHeight(value):
    if re.search(r'cm', value):
        if int(value.strip('cm')) >= 150 and int(value.strip('cm')) <= 193:
            return True
        else:
            return False
    elif re.search(r'in', value):
        if int(value.strip('in')) >= 59 and int(value.strip('in')) <= 76:
            return True
        else:
            return False
    else:
        return False


def checkHair(value):
    if re.search(r'^#([a-f]|[0-9]){6}', value):
        return True
    else:
        return False


def checkEye(value):
    eyecolor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value in eyecolor:
        return True
    else:
        return False


def checkPassID(value):
    if re.search(r'^[0-9]{9}$', value):
        return True
    else:
        return False


def areAllFieldsValid(passport):
    # fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if (checkBirth(int(passport.get('byr')))
            and checkIssue(int(passport.get('iyr')))
            and checkExpiration(int(passport.get('eyr')))
            and checkHeight(passport.get('hgt'))
            and checkHair(passport.get('hcl'))
            and checkEye(passport.get('ecl'))
            and checkPassID(passport.get('pid'))):
        return True
    else:
        return False


def validPassports2(dict_of_passports):
    valid_passport_count = 0
    for p in dict_of_passports.values():
        keys = p.keys()
        if (len(keys) == 8) or (len(keys) == 7 and 'cid' not in keys):
            if areAllFieldsValid(p):
                valid_passport_count += 1
    return valid_passport_count


print(validPassports2(sanitizePassports(passports)))
