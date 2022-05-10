class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) is 2: return [1,2]
        temp = numbers
        numbers = sorted(list(set(numbers)))
        
        i = 0
        j = 1
        
        while i < len(numbers):
            while j < len(numbers):
                if numbers[i] + numbers[j] == target: 
                    i = temp.index(numbers[i]) + 1
                    j = temp.index(numbers[j]) + 1
                    return [i, j]
                j += 1
            i += 1
            j = i + 1
                
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) is 2: return [1,2]
        temp = numbers
        if len(numbers) > 100: 
            numbers = sorted(list(set(numbers)))
        
        i = 0
        j = 1
        
        while i < len(numbers):
            while j < len(numbers):
                if numbers[i] + numbers[j] == target: 
                    i = temp.index(numbers[i]) + 1
                    j = temp.index(numbers[j])
                    return [i, j]
                j += 1
            i += 1
            j = i + 1
                
            

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = dict()
        i = 0
        
        for i in range(len(numbers)):
            if (numbers[i] - target) not in m.keys():
                m[numbers[i]] = i
            else: 
                temp = None
                for k,v in m.items():
                    if v == (numbers[i] - target):
                        return [i, k]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, (len(numbers) - 1)
        
        while i < len(numbers): 
            sum = numbers[i] + numbers[j]
            if sum > target: 
                j -= 1
            elif sum < target: 
                i += 1
            else:
                i += 1
                j += 1
                return [i,j]
                
        

