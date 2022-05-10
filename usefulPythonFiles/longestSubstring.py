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

