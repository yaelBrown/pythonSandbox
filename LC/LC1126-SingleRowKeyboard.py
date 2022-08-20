"""
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25). Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.
"""



class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        idx = 0
        out = 0
        
        for l in list(word):
            prev = idx
            idx = keyboard.index(l)
            out += abs(prev - idx)
            
        return out

