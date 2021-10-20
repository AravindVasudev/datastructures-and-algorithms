# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def getLongestPath(X, Y):
            if not (0 <= X < len(matrix) and 0 <= Y < len(matrix[0])):
                return 0
            
            if memo[X][Y] == -1:
                memo[X][Y] = 1
                for offsetX, offsetY in directions:
                    nextX, nextY = X + offsetX, Y + offsetY
                    if 0 <= nextX < len(matrix) and 0 <= nextY < len(matrix[0]) and \
                        matrix[nextX][nextY] > matrix[X][Y]:
                        memo[X][Y] = max(memo[X][Y], getLongestPath(nextX, nextY) + 1)
                    
            return memo[X][Y]
        
        
        memo = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        maxPath = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxPath = max(maxPath, getLongestPath(i, j))
                
        return maxPath
