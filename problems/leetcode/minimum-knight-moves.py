# https://leetcode.com/problems/minimum-knight-moves/
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(2, 1), (-2, 1),
                      (1, 2), (-1, 2),
                      (2, -1), (-2, -1),
                      (1, -2), (-1, -2)]
        
        visited = set()
        queue = deque()
        queue.append((0, 0))
        
        moves = 0

        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                i, j = queue.popleft()
                
                if i == x and j == y:
                    return moves
                
                for dirI, dirJ in directions:
                    nextI, nextJ = i + dirI, j + dirJ
                    if (nextI, nextJ) not in visited:
                        visited.add((nextI, nextJ))
                        queue.append((nextI, nextJ))
                    
            moves += 1
            
        return -1
