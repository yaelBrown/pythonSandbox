class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    j, k = 0, 1

    while j != (len(nums) - 1):
      while k != len(nums):
        if nums[j] + nums[k] == target:
          return [j, k]
        k += 1
      j += 1
      k = j+1


  def twoSum(self, nums: List[int], target: int) -> List[int]:
    m, j = dict(), 0
    
    while j < len(nums): 
        k = target - nums[j]
        if k in m.keys():
            return [j, m[k]]
        else: 
            m[nums[j]] = j
            j = j + 1
            