
def contains_duplicate(nums):
    _ = list(set(nums))
    return len(_) != len(nums)


"""
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

    Input: nums = [1,2,3,1]
    Output: true

Hint: Use sets
"""