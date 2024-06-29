class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        max_value = 0 
        while right < len(prices):
            if prices[left] < prices[right]:
                result = prices[right] - prices[left]
                max_value = max(max_value, result)
            else:
                left = right
            right += 1
        
        return max_value

                
        
