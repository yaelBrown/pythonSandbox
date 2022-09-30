"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

# times out on larget inputs
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == [] or target not in nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        out = []
        
        while nums[l] != target or nums[r] != target: 
            print(r)
            l = nums.index(target)
            if nums[r] != target:
                r -= 1
                if r < l:
                    r = 0
                    break
                
            print({"left": l, "right": r})
            
        return [l,r]
        
        