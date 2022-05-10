class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        
        for n in nums: 
            if n not in m.keys():
                m[n] = 1
            else: 
                m[n] += 1
                
        out = []
        temp = []
        for key,v in m.items():
            temp.append((key,v))
        
        temp.sort(key = lambda i: i[1])
        temp.reverse()
        
        if k is 1: 
            return [temp.pop(0)[0]]
        
        cnt = 0
        while cnt != k:
            out.append(temp.pop(0)[0])
            cnt += 1
            
        return out 