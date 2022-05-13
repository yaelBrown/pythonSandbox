class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) is 1: return 1
        i,j,k = 0,1,0
        temp = []
        out = cnt = 0
        
        for k in range(len(s)):
            if s[k] not in temp:
                temp.append(s[k])
            else: 
                if s[k] != s[k-1]:
                    temp = [s[k-1], s[k]]
                else:
                    temp = [s[k-1]]
            
            cnt = len(temp)
            out = max(cnt, out)
            
        return out


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        c = set()
        c.add(s[start])
        out = 0


        while end < len(s): 
            if s[end] not in c: 
                c.add(s[end])
            else: 
                out = max(out, (end - start))
                start = end
                c = set()
                c.add(s[start])

            end += 1

        return out


    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) is 0 or len(s) is 1: return len(s)
        
        start = end = 0
        c = set()
        out = 0

        while end < len(s): 
            print(s[end])
            if s[end] not in c: 
                c.add(s[end]) 
                end += 1
            else: 
                out = max(out, end - start)
                if start < (len(s) - 1):
                    start += 1

                c.add(s[start])
                c.add(s[end])
            end += 1        
            
        return out