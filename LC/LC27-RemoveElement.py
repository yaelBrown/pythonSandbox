"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""


def removeElement(self, nums: List[int], val: int) -> int:
  swapped = 0
  idx = 0
  for n in nums:
    if idx >= (len(nums) - (1 + swapped)):
      break
  if n is val:
    print("swapping")
    nums[idx] = nums[len(nums) - (1 + swapped)]
    print(nums[len(nums) - (1 + swapped)])
    swapped += 1
    idx += 1
    print("swapped: " + str(swapped))
  return (len(nums) - swapped)


# o(# of dupliates) correct soln
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums: 
            idx = nums.index(val)
            nums.pop(idx)
        return len(nums)