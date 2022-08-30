# https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def pathSum(i: int = 0, j: int = 0) -> int:
            if i >= len(grid) or j >= len(grid[0]):
                return float('inf')
            
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            
            return grid[i][j] + min(pathSum(i + 1, j), pathSum(i, j + 1))
        
        return pathSum()
