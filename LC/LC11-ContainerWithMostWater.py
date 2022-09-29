"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = 1
        out = 0
        length = len(height)
        
        while left <= (length - 1):
            while right <= (length - 1):
                res = min(height[left], height[right]) * (right - left)
                print((height[left], height[right]))
                print(res)
                out = max(out, res) 
                right += 1
            left += 1
            right = left + 1
            
        return out

    # memoized solution, works for small inputs
    class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = 1
        out = 0
        length = len(height)
        mem = {}
        
        while left <= (length - 1):
            while right <= (length - 1):
                # res = min(height[left], height[right]) * (right - left)
                minVal = min(height[left], height[right])
                dist = (right - left)
                # print({"dist": dist, "minVal": minVal})
                if dist in mem.keys():
                    if minVal in mem[dist]:
                        out = max(out, mem[dist][minVal])
                    else:
                        res = minVal * dist
                        mem[dist][minVal] = res
                        out = max(out, res)
                else: 
                    res = minVal * dist
                    mem[dist] = {}
                    mem[dist][minVal] = res
                    out = max(out, res) 
                right += 1
                # print(mem)
            left += 1
            right = left + 1
            
        return out







# o(n) solution
"""https://leetcode.com/problems/container-with-most-water/"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans=0
        while l<r:
            if height[l]<height[r]:
                area=height[l]*(r-l)
                l+=1
            else:
                area=height[r]*(r-l)
                r-=1
            ans=max(ans,area)
        return ans
            
# SUBMISSION REPORT:-
    # Runtime: 748 ms, faster than 96.52% of Python3 online submissions for Container With Most Water.
    # Memory Usage: 27.5 MB, less than 44.36% of Python3 online submissions for Container With Most Water.
    
# EXPLANATION:-
    # We will use two pointer technique to solve this problem
    # We will take left pointer at 0 and right at last index
    # If the element at l index is small, we will store area as distance between r and l multiply by l element
    # Else we will store area as distance between r and l and multiply by r element
    # Lastly, we will store the max element in area and return the answer