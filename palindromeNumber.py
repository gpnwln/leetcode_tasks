"""Easy task. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints: -2**(31) <= x <= 2**(31) - 1
 
Follow up: Could you solve it without converting the integer to a string?
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: return False
        p=x
        n=0
        while p != 0:
            n = n + 1
            p = p // 10
        k=0
        n1 = (n // 2) + 1
        for i in range(n1):
            a1 = (x // 10**i) % 10
            a2 = (x // 10**(n-i-1)) % 10
            if a1==a2: k=k+1
        if k == n1: return True
        else: return False
        