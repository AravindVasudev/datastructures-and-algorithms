# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '1':
                    continue
                    
                self.visit(grid, i, j)
                total += 1
                
        return total
    
    def visit(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '0'
        
        self.visit(grid, i + 1, j)
        self.visit(grid, i - 1, j)
        self.visit(grid, i, j + 1)
        self.visit(grid, i, j - 1)
