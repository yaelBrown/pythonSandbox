"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1) + len(nums2)

        joined = (nums1 + nums2)
        joined.sort()

        if totalLen % 2 == 1:
            return joined[int(totalLen / 2)]
        else:
            mid = int(totalLen // 2)
            return (joined[mid] + joined[~mid]) / 2
