"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p is ".":
            return True
        if "*" in p: 
            p.split()
            
        # ?


"""
Runtime: 182 ms, faster than 26.52% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 14.1 MB, less than 38.52% of Python3 online submissions for Regular Expression Matching.
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        res = re.findall(p, s)
        return True if s in res else False