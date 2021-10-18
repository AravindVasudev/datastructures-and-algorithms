# https://leetcode.com/problems/number-of-distinct-islands/
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i, j, currentPath, direction = "0"):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or not grid[i][j]:
                return currentPath
            
            grid[i][j] = 0
            currentPath.append(direction)
            
            dfs(i + 1, j, currentPath, "D")
            dfs(i - 1, j, currentPath, "U")
            dfs(i, j + 1, currentPath, "R")
            dfs(i, j - 1, currentPath, "L")
            
            currentPath.append("0")
            
            return currentPath
        
        uniqueIslands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    uniqueIslands.add(str(dfs(i, j, [])))
                    
        return len(uniqueIslands)
