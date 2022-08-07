"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = collections.defaultdict()
        i, j, k = nums[0], nums[1], nums[2]
        
        if i is 0 and j is 0 and k is 0 and length(nums) is 3:
            return [[0,0,0]]
        
        
# ?