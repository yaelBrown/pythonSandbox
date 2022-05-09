class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for n in range(len(nums)):
            cur = nums.pop(0)
            if len(nums) == 0: return False
            if cur in nums:
                return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        i = 1
        for n in nums:
            s.add(n)
            if s.size() != i:
                return False
        return True
