'''
Magic 5-gon ring
https://projecteuler.net/problem=68

By concatenating each group it is possible to form 9-digit strings;
the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements,
it is possible to form 16- and 17-digit strings.
What is the maximum 16-digit string for a "magic" 5-gon ring?
'''

from itertools import permutations


def create3gon():
    possible = [1, 2, 3, 4, 5, 6]
    solutions = set()
    for p in permutations(possible, 3):
        inner = [p[0], p[1], p[2]]
        outer = [i for i in possible if i not in inner]
        for o in permutations(outer):
            first_group = [o[0], p[0], p[2]]
            second_group = [o[1], p[2], p[1]]
            third_group = [o[2], p[1], p[0]]
            if (sum(first_group) == sum(second_group)
                    and sum(first_group) == sum(third_group)):
                if (first_group[0] < second_group[0]
                        and first_group[0] < third_group[0]):
                    solutions.add(str(first_group + second_group
                                      + third_group))
                elif second_group[0] < third_group[0]:
                    solutions.add(str(second_group + third_group
                                      + first_group))
                else:
                    solutions.add(str(third_group + first_group
                                      + second_group))
    return solutions


# ans = create3gon()
# print(ans)
# print(len(ans))
# print(max(ans))


def create5gon():
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    solutions = set()
    for p in permutations(possible, 5):
        inner = [p[0], p[1], p[2], p[3], p[4]]
        outer = [i for i in possible if i not in inner]
        for o in permutations(outer):
            first_group = [o[0], p[0], p[1]]
            second_group = [o[1], p[1], p[2]]
            third_group = [o[2], p[2], p[3]]
            fourth_group = [o[3], p[3], p[4]]
            fifth_group = [o[4], p[4], p[0]]
            if (sum(first_group) == sum(second_group)
                    and sum(first_group) == sum(third_group)
                    and sum(first_group) == sum(fourth_group)
                    and sum(first_group) == sum(fifth_group)):
                if (first_group[0] < second_group[0]
                        and first_group[0] < third_group[0]
                        and first_group[0] < fourth_group[0]
                        and first_group[0] < fifth_group[0]):
                    solutions.add(str(first_group + second_group + third_group
                                      + fourth_group + fifth_group))
                elif (second_group[0] < third_group[0]
                      and second_group[0] < fourth_group[0]
                      and second_group[0] < fifth_group[0]):
                    solutions.add(str(second_group + third_group + fourth_group
                                      + fifth_group + first_group))
                elif (third_group[0] < fourth_group[0]
                      and third_group[0] < fifth_group[0]):
                    solutions.add(str(third_group + fourth_group + fifth_group
                                      + first_group + second_group))
                elif fourth_group[0] < fifth_group[0]:
                    solutions.add(str(fourth_group + fifth_group + first_group
                                      + second_group + third_group))
                else:
                    solutions.add(str(fifth_group + first_group + second_group
                                      + third_group + fourth_group))
    return solutions


ans = create5gon()
print(ans)
print(len(ans))
print(max(ans))
