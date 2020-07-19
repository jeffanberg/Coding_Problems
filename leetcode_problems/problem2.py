'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = None
        count = 1
        first_number, second_number = 0, 0
        while l1 is not None:
            first_number += l1.val * count
            l1 = l1.next
            count *= 10
        count = 1
        while l2 is not None:
            second_number += l2.val * count
            l2 = l2.next
            count *= 10
        added = first_number + second_number
        result_string = str(added)
        for num in range(len(result_string)):
            l3 = ListNode(result_string[num], next=l3)
        return l3
