# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        return self.maxMoneyRange(1, n)
    
    @cache
    def maxMoneyRange(self, lo: int, hi: int) -> int:
        if lo >= hi:
            return 0
        
        maxMoney = float('inf')
        for i in range(lo, hi + 1):
            maxMoney = min(maxMoney, max(self.maxMoneyRange(lo, i-1) + i, self.maxMoneyRange(i+1, hi) + i))
            
        return maxMoney
