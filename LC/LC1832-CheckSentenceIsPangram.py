"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        
        t = list(sentence)
        t = set(t)
        t = sorted(t)
        t = "".join(t)
        
        import string
        return t == string.ascii_lowercase
            
