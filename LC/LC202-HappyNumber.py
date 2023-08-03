class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: True
        if n == 2: False
        mem = dict()

        while n > 3: 
            div = (n // 10)
            ddd = int(str(n)[-1]) # error here

            n = (div ** div) + (ddd * ddd)

            if n == 1: return True

            # endless loop

        return False





# simplest solution ? 
class Solution:
    def isHappy(self, n: int) -> bool:
        used = []

        while(n>0):
            tmp = 0
            while(n>0):
                i = n%10

                tmp += i*i
                n = n//10

            if(tmp in used):
                return False
            else:
                used.append(tmp)

            if(tmp==1):
                return True
            
            n = tmp

        return False