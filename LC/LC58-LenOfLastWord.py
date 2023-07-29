class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split(" ")

        t = []

        for w in split:
            if w.isalnum():
                t.append(w)

        return len(t[len(t) - 1])

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])
    

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])