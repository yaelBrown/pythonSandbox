
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        s1, s2 = 0, 1
        for i in range(n):
            temp = s1 + s2
            s1 = s2
            s2 = temp
            
        


        return s2


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        s1, s2 = 0, 1
        for i in range(n):
            s1, s2 = s2, s1+s2

        return s2