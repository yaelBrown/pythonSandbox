"""
We create a dictionary, which will be responsible for storing the numbers in the array as keys, so we can quickly check to see if we have encountered any number before, and we store the indexes/positions of each of these numbers as values, so we can track where the number is located in the array, for our final answer.

We traverse the array left to right, while recording the elements we come across with the number as the key and the index as the value in our dictionary. This occurs at the 'else' portion.

While traversing, at each number, we are calculating the other number we need to complete the sum. This second number that we need is the difference, which is 'target - value', which we look for in our keys of our dictionary.

If we found that we have already passed over the number we need to complete the sum, we return the position or index of the past number which we have been tracking with our dictionary seen_values[target - value] and the index of the current number.
"""

# Dictionary Solution
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen_values = {}
    
    for index, value in enumerate(nums):
        if target - value in seen_values:
            return seen_values[target - value], index
        
        else:
            seen_values[value] = index
            
    return -1



def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
  
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")