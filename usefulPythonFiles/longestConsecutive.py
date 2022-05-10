class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) is 0: return 0
        
        nums.sort()
        cnt = out = 0
        
        next = 1
        cur = 0
        while next != len(nums):
            if (nums[cur] + 1) is nums[next]:
                cnt += 1
            else: 
                cnt = 0
            out = max(out, cnt)
            cur += 1 
            next += 1
        
        return out +1
            


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) is 0: return 0
        if len(nums) is 1: return 1
        
        nSet = list(set(nums))
        nSet.sort()
        
        out = i = 0
        cnt = 1
        while (i+1) != len(nSet):
            
            if (nSet[i] + 1) is nSet[i+1]:
                cnt += 1
            elif (nSet[i] + 1) is nSet[i]:    
                cnt += 1
            else: 
                cnt = 1
            i += 1
            out = max(out, cnt)
        
        if len(nums) is 2: 
            if nSet[0] is nSet[1]:
                cnt += 1
            else: 
                return 1
        
        return out
            

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) is 0: return 0
        if len(nums) is 1: return 1
        
        nums = sorted(list(set(nums)))
        out = cnt = 1 
        
        for i in range(1, len(nums)):
            if (nums[i-1]+1) == nums[i]:
                cnt += 1
            else:
                cnt = 1
                
            out = max(cnt, out)
        return out