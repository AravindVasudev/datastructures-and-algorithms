# https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/
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

N = 200 # Dimension (N x N)

UNEXPLORED = -1
BLOCKED = -2

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        
        startX = startY = N // 2 - 1 # Start from the middle
        grid = [[UNEXPLORED] * N for _ in range(N)]
        grid[startX][startY] = 0
        
        # Explore the grid
        targetX, targetY = self.explore(grid, master, startX, startY)
        
        # If target is not present
        if targetX == -1:
            return -1
        
        # Find minimum cost
        return self.findMimimumCost(grid, startX, startY, targetX, targetY)
        
    def explore(self, grid: List[List[int]], master: 'GridMaster', X: int, Y: int) -> (int, int):
        """
        Explore the world and fill the grid
        """
        
        if master.isTarget():
            return X, Y
        
        target = -1, -1
        for direction, offset in DIRECTIONS.items():
            nextX, nextY = X + offset[0], Y + offset[1]
            
             # Only work on unexplored cells
            if grid[nextX][nextY] == UNEXPLORED:
                if master.canMove(direction):
                    # Move to the cell
                    grid[nextX][nextY] = master.move(direction)
                    
                    # Explore that cell
                    found = self.explore(grid, master, nextX, nextY)
                    
                    # If found, note it down
                    if found[0] != -1:
                        target = found
                    
                    # Come back
                    master.move(OPPOSITE_DIRECTION[direction])
                else:
                    grid[nextX][nextY] = BLOCKED
                    
        return target
    
    def findMimimumCost(self, grid: List[List[int]], startX: int, startY: int, targetX: int, targetY: int) -> int:
        """
        Find the smallest cost required to go from start to finish.
        """
        
        pqueue = [(0, startX, startY)]
        visited = [[False] * N for _ in range(N)]
        
        while pqueue:
            cost, curX, curY = heapq.heappop(pqueue)
            
            # Stop when target is found
            if curX == targetX and curY == targetY:
                return cost
                
            # Add neighbors to the queue
            for offsetX, offsetY in DIRECTIONS.values():
                nextX, nextY = curX + offsetX, curY  + offsetY
                
                # If next is valid, add to the heap
                if 0 <= nextX < N and 0 < nextY < N and grid[nextX][nextY] > 0 and not visited[nextX][nextY]:
                    visited[nextX][nextY] = True
                    heapq.heappush(pqueue, (cost + grid[nextX][nextY], nextX, nextY))
                    
        return -1
                    
