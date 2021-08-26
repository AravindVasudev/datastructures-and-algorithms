# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        N = len(grid)
        rowMax = [0] * N
        colMax = [0] * N
        
        for i in range(N):
            for j in range(N):
                rowMax[i] = max(rowMax[i], grid[i][j])
                colMax[i] = max(colMax[i], grid[j][i])
                
        maxIncrease = 0
        for i in range(N):
            for j in range(N):
                maxIncrease += min(rowMax[i], colMax[j]) - grid[i][j]
        
        return maxIncrease
