class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        
        buy = i
        sell = j
        while j < (len(prices) - 1):
            if j > i: 
                i = j
                j += 1
                buy = min(prices[i], prices[j])
            else: 
                buy = i
                j += 1
                
        
        return buy - sell

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = min(prices)
        temp = prices[prices.index(buy):]
        if len(temp) is 1: 
            buy = prices[0]
            temp = prices[prices.index(buy):]
        sell = max(temp)
        
        return sell - buy
        


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
                
        