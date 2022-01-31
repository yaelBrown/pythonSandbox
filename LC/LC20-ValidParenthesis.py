# Slow solution
# Runtime: 56 ms, faster than 8.54% of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) is 1:
            return False
        
        map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        seen = []
        
        for c in s: 
            if c in map: 
                seen.append(map[c])
            else: 
                try: 
                    temp = seen.pop()
                except: 
                    return False
                
                if temp is c:
                    continue
                else: 
                    return False
        return (len(seen) is 0)


    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")": "(", "]": "[", "}": "{" }

        for c in s: 
            if c in closeToOpen: 
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(c)

        return True if not stack else False