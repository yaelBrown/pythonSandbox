class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = ""
        for n in digits: 
            t += str(n)
        
        t = int(t)
        t += 1 
        t = str(t)

        t2 = []
        for n in t: 
            t2.append(int(n))
        
        return t2


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in (str(int(str(''.join(str(n) for n in digits))) + 1))]