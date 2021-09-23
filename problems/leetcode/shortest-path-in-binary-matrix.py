# https://leetcode.com/problems/shortest-path-in-binary-matrix/
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        
        END = len(grid) - 1
        
        queue = deque()
        queue.append((0, 0))
        
        level = 1
        while queue:
            # Level ordered traversal
            levelSize = len(queue)
            
            for _ in range(levelSize):
                x, y = queue.popleft()
                
                if x == END and y == END:
                    return level
                
                for dirX in range(-1, 2):
                    for dirY in range(-1, 2):
                        if not (dirX == 0 and dirY == 0):
                            nextX, nextY = x + dirX, y + dirY
                            if 0 <= nextX <= END and 0 <= nextY <= END and grid[nextX][nextY] == 0:
                                grid[nextX][nextY] = 1
                                queue.append((nextX, nextY))
    
            level += 1
            
        return -1
      
# Efficient Solution (A* algorithm)

# TBD
