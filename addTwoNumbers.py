"""Medium Task. Add Two Numbers.
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        i=0
        l1_sum = l1.val
        while l1.next is not None:
            l1 = l1.next
            i = i+1
            l1_sum =  l1.val * (10**i) + l1_sum

        i=0
        l2_sum = l2.val
        while l2.next is not None:
            l2 = l2.next
            i = i+1
            l2_sum =  l2.val * (10**i) + l2_sum

        l_sum = l1_sum + l2_sum
        l_sum_str = str(l_sum)
        a=len(l_sum_str)
        result = ListNode(int(l_sum_str[a-1]))
        res = result
        for j in range(a-2, -1, -1):
            result.next = ListNode(int(l_sum_str[j]))
            if j!=0: result = result.next
        return res