# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rightMax = [0] * len(prices)
        rightMax[-1] = prices[-1]
        
        for i in range(len(prices) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], prices[i])
            
        maxProfit = 0
        for i, price in enumerate(prices):
            maxProfit = max(0, rightMax[i] - price, maxProfit)
            
        return maxProfit
