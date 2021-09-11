# https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1
        
        a = 0
        b = 1
        c = 1
        
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
            
        return c
