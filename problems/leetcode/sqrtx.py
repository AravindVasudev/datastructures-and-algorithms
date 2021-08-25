# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
    
        left = 1
        right = x - 1
        
        while left < right:
            mid = ceil((left + right) / 2)
            midSquared = mid * mid
            
            if midSquared == x:
                return mid
            elif midSquared < x:
                left = mid
            else:
                right = mid - 1
        
        return left
