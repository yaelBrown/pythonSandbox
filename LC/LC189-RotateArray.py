"""
  Given an array, rotate the array to the right by k steps, where k is non-negative.
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def _rotate():
            j = 0
            temp = []
            temp.append(nums[len(nums) - 1])

            for i in nums: 
                if j < len(nums):
                    temp.append(nums[j])
                    j += 1
                else: 
                    continue
                        
            del temp[len(nums)]
            return temp
        
        for z in range(k):
            t2 = _rotate()
            print(t2)
        
        print(t2)
        
        nums = t2
        # ?        
        
            
                
        