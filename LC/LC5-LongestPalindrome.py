"""
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.
"""





class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        
        def _checkPalin(sub: str):
            return sub == sub[::-1]
        
        maxPalin = 0
        temp = ""
        out = ""
        for i in range(len(s)):
            temp += s[i]
            if _checkPalin(temp):
                maxPalin = max(len(temp), maxPalin)
                print(temp)
            else: 
                temp = ""
        return out


# Manacher's algo ? https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm