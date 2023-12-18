# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        M, N = binaryMatrix.dimensions()
        l, r = 0, N - 1
        
        @cache
        def colContainsOne(col: int) -> bool:
            for i in range(M):
                if binaryMatrix.get(i, col) == 1:
                    return True
                
            return False
        
        while l < r:
            mid = (l + r) // 2
            
            if colContainsOne(mid):
                r = mid
            else:
                l = mid + 1
                
        return l if colContainsOne(l) else -1
