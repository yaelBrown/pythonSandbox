"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

# not dp
class Solution:
    def countBits(self, n: int) -> List[int]:
        def _cnt(s):
            print(s)
            cnt = 0
            for l in s: 
                cnt += int(l)
            return cnt
        out = []
        t = 0
        while t <= n: 
            out.append(_cnt(bin(t).replace("0b", "")))
            t += 1
        
        return out

#dp 
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        if n == 1:
            return [0,1]
        
        # Bottom Up approach
        res = [0,1]
        for i in range(2,n+1):
            res.append((res[i//2] + res[i%2]))
        return res 