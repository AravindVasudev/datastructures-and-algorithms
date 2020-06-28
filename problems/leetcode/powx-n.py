# https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.myPowRecur(x, n)
        
    def myPowRecur(self, x: float, n: int, cache=dict()) -> float:
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n == -1:
            return 1 / x
        
        if (x, n) in cache:
            return cache[(x, n)]
        
        leftPow = n // 2
        rightPow = n - leftPow
        
        cache[(x, n)] = self.myPow(x, leftPow) * self.myPow(x, rightPow)
        return cache[(x, n)]
