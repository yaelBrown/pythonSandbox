"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""







class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        map = {}
        out = -1
        
        for i in nums:
            if i not in map: 
                map[i] = 1
            else: 
                map[i] += 1
        
        out = list(dict.items(map))
        out.sort(key=lambda x: x[1], reverse=True)
        
        return out[0][0]
        
        

