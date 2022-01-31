# Kadanes Algorithm
def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) is 1:          # Edge case
        return nums[0]

    cur = 0                     # init vars
    m = nums[0]
    
    for i in nums:              # iterate
        if cur < 0: cur = 0     # init cur to 0 if less than 0    
        cur += i                # add idx to cur
        m = max(cur, m)         # find max between cur and max
        
    return m                    # return 