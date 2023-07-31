class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        prod = 1
        for i in range(len(nums)): 
            temp = nums[i]
            nums[i] = 1
            for j in nums:
                prod *= j
            out.append(prod)
            prod, nums[i] = 1, temp

        return out

                    
