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