# https://leetcode.com/problems/shortest-path-in-a-hidden-grid/
# States
UNEXPLORED = 0
EXPLORED = 1
BLOCKED = 2
START = 3
TARGET = 4

# Directions
DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

OPPOSITE_DIRECTION = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L"
}
    
class Solution(object):    
    def findShortestPath(self, master: 'GridMaster') -> int:
        N = 1000 # Dimension (N x N)
        grid = [[0] * N for _ in range(N)]
        grid[N // 2][N // 2] = START # Start from the middle
        
        # Explore the grid
        self.explore(grid, master, N // 2, N // 2)
        
        # Find the shortest path
        return self.getDistance(grid, N // 2, N // 2)
    
    
    def explore(self, grid, master, X, Y):
        """
        Explore the world and fill the grid
        """
        
        # Stop exploring when target is found
        if master.isTarget():
            grid[X][Y] = TARGET
            return
        
        for direction, offset in DIRECTIONS.items():
            nextX, nextY = X + offset[0], Y + offset[1]
            
            # Only work on unexplored cells
            if grid[nextX][nextY] == UNEXPLORED:
                if master.canMove(direction):
                    # Move to the cell
                    master.move(direction)
                    grid[nextX][nextY] = EXPLORED
                    
                    # Explore that cell
                    self.explore(grid, master, nextX, nextY)
                    
                    # Come back to the current cell
                    master.move(OPPOSITE_DIRECTION[direction])
                else:
                    grid[nextX][nextY] = BLOCKED
                    
                    

    def getDistance(self, grid, startX, startY):
        """
        Returns the shortest distance to the TARGET cell.
        """
        
        queue = deque()
        queue.append((startX, startY))
        
        level = 0
        while queue:
            levelSize = len(queue)
            
            for _ in range(levelSize):
                curX, curY = queue.popleft()
                
                for offsetX, offsetY in DIRECTIONS.values():
                    nextX, nextY = curX + offsetX, curY + offsetY
                    
                    # If next is a valid cell
                    if 0 <= nextX < len(grid) and 0 <= nextY < len(grid):
                        # Return current level if found
                        if grid[nextX][nextY] == TARGET:
                            return level + 1
                        
                        # Explore next unblocked cell
                        if grid[nextX][nextY] != BLOCKED:
                            grid[nextX][nextY] = BLOCKED
                            queue.append((nextX, nextY))
            
            level += 1
            
        # If not found
        return -1
