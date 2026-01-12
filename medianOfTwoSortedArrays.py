"""Hard task. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums = sorted(nums, reverse=False)
        if len(nums)%2==0:
            a1 = len(nums)//2
            med = round((float(nums[a1-1]) + float(nums[a1])) / 2, 5)
        else: med = round(float(nums[len(nums)//2]), 5)
        return med