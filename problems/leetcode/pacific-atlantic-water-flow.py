# https://leetcode.com/problems/pacific-atlantic-water-flow/
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N, M = len(heights), len(heights[0])
        
        def dfs(row, col, reachable):
            """
            Returns all cells "reachable" from row, col
            reachable -> The value must be >= row, col
            """
            reachable.add((row, col))
            
            for x, y in directions:
                nextRow, nextCol = row + x, col + y
                if 0 <= nextRow < N and 0 <= nextCol < M and \
                    (nextRow, nextCol) not in reachable and \
                    heights[row][col] <= heights[nextRow][nextCol]:
                    dfs(nextRow, nextCol, reachable)
                    
        # Find cells reachable from Pacific & Atlantic Ocean 
        pacificReachable = set()
        atlanticReachable = set()
        
        for i in range(N):
            dfs(i, 0, pacificReachable)
            dfs(i, M - 1, atlanticReachable)
            
        for j in range(M):
            dfs(0, j, pacificReachable)
            dfs(N - 1, j, atlanticReachable)
            
        # Return intersection
        return list(pacificReachable.intersection(atlanticReachable))
