"""
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
"""






class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = "aeiou"
        for v in vowels:
            s = s.replace(v, "")
            
        return s