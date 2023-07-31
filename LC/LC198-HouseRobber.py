class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return nums[0] + nums[1]

        mid = len(nums) / 2 == 0 if len(nums) / 2 == 0 else int(((len(nums) / 2) -.5) + 1)
        idx = 0
        while idx <= mid:
            try:
                nums[idx] = max(nums[idx], nums[idx+2])
            except: 
                continue
            finally: 
                idx += 1           

        return max(nums[:mid])
