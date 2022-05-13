class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return tokens[0]
        op = []
        nums = []
            
        for t in tokens: 
            if not t.isnumeric(): 
                op.append(t)
            else: 
                nums.append(t)
                
        
        sum = nums[0]
        nums.pop(0)
        
        for o in ops: 
            sum = 
        
        