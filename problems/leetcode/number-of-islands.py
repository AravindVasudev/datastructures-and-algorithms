# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        M, N = len(grid), len(grid[0])
        visited = [[-1] * N for _ in range(M)]

        total = 0
        for i in range(M):
            for j in range(N):
                if visited[i][j] == 1 or grid[i][j] == '0':
                    continue
                    
                self.visit(grid, visited, i, j)
                total += 1
                
        return total
    
    def visit(self, grid, visited, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or \
            visited[i][j] == 1 or grid[i][j] != '1':
            return

        visited[i][j] = 1
        
        self.visit(grid, visited, i + 1, j)
        self.visit(grid, visited, i - 1, j)
        self.visit(grid, visited, i, j + 1)
        self.visit(grid, visited, i, j - 1)
