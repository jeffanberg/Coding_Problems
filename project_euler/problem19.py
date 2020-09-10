''' You are given the following information, but you may prefer to do
some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''

firstdays = dict()

# 1 = sunday, 2 = monday, 3 = tuesday, etc.
# Jan. 1901 was a Tuesday
day = 3


def advanceWeek(currentday, num):
    start = currentday
    count = 0
    while count < num:
        if start == 7:
            start = 1
            count += 1
        else:
            start += 1
            count += 1
    return start

# print(advanceWeek(5, 28))


def count(values, item):
    count = 0
    for each in values:
        if each == item:
            count += 1
    return count


for year in range(1901, 2001, 1):
    for month in range(1, 13):
        if month in [4, 6, 9, 11]:
            key_string = str(month) + '-' + str(year)
            firstdays.update({key_string: day})
            day = advanceWeek(day, 30)
        elif month == 2:
            key_string = str(month) + '-' + str(year)
            firstdays.update({key_string: day})
            if year % 400 == 0:
                day = advanceWeek(day, 29)
            elif year % 4 == 0 and not year % 100 == 0:
                day = advanceWeek(day, 29)
            else:
                day = advanceWeek(day, 28)
        else:
            key_string = str(month) + '-' + str(year)
            firstdays.update({key_string: day})
            day = advanceWeek(day, 31)

print(firstdays)
print(count(firstdays.values(), 1))
