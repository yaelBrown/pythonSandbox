"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
"""



class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for i in arr: 
            if i not in map: 
                map[i] = 1
            else: 
                map[i] += 1
                
        return len(set(list(dict.values(map)))) == len(dict.values(map))


