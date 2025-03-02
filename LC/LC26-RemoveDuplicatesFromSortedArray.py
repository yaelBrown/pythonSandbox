"""
  Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

  Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

  Return k after placing the final result in the first k slots of nums.

  Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = set()
        idx = 0
        unique = 1
        for n in nums:
            if n not in temp: 
                temp.add(n)
                unique += 1
            else: 
                nums.append(nums[idx])
                del nums[idx]
            idx += 1
        nums = nums[:unique]
        return len(nums)





class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[2] = nums[5]
        return 6
    
    # have to iterate and count the values, then swap them. 


# basically recreating the list by swapping values but you are counting how many times you swapped values
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for s in range(1, len(nums)):
            
            print(s)
            if nums[s] != nums[s-1]:
                print({ "s-1": s-1, "s": s })
                nums[l] = nums[s]
                l += 1
        return l

    # shorthand
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        cur = head
        while cur and cur.next != None:
            if cur.val == cur.next.val: # The duplicates since they are next to each other in a sorted list
                cur.next = cur.next.next
            else: 
                cur = cur.next
        return head