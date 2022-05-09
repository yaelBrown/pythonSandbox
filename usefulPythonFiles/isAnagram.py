class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for l in s: 
            if l not in t:
                return False
            else: 
                t = t.replace(l, "", 1)
        return len(t) == 0