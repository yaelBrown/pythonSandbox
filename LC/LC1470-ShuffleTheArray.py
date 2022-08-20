"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = abs(len(nums) / 2)
        i = 0
        j = int(mid)
        out = []
        
        while i < int(mid):
            out.append(nums[i])
            out.append(nums[j])
            i += 1
            j += 1
            
        return out