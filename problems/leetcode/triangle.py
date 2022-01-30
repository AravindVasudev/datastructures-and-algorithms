# https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def minPathSum(row: int = 0, col: int = 0) -> int:
            if row >= len(triangle):
                return 0

            return triangle[row][col] + min(minPathSum(row + 1, col),
                                            minPathSum(row + 1, col + 1))
        
        return minPathSum()
