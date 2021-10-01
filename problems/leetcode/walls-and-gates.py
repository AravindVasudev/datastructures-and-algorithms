# https://leetcode.com/problems/walls-and-gates/
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2147483647
        
        pqueue = deque()
        
        for i, row in enumerate(rooms):
            for j, cell in enumerate(row):
                if cell == 0: # cell is a gate
                    pqueue.append((i, j))
                    
        while pqueue:
            curX, curY = pqueue.popleft()
            
            for dirX, dirY in directions:
                nextX, nextY = curX + dirX, curY + dirY
                if 0 <= nextX < len(rooms) and 0 <= nextY < len(rooms[0]) and rooms[nextX][nextY] == INF:
                    rooms[nextX][nextY] = rooms[curX][curY] + 1
                    pqueue.append((nextX, nextY))
                
