# https://leetcode.com/problems/the-maze-ii/
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Up, Down, Right, Left.

        isValidMove = lambda cell, d: (0 <= cell[0] + d[0] < M and 0 <= cell[1] + d[1] < N and 
            maze[cell[0] + d[0]][cell[1] + d[1]] == 0)
        move = lambda cell, d: [cell[0] + d[0], cell[1] + d[1]]

        pq = [(0, start)]
        visited = [[float("inf")] * N for _ in range(M)]
        visited[start[0]][start[1]] = 0

        while pq:
            dist, cell = heapq.heappop(pq)

            if cell == destination:
                return dist

            for d in directions:
                newCell, newDist = cell, dist
                while isValidMove(newCell, d):
                    newCell = move(newCell, d)
                    newDist += 1

                if visited[newCell[0]][newCell[1]] > newDist:
                    visited[newCell[0]][newCell[1]] = newDist
                    heapq.heappush(pq, (newDist, newCell))

        return -1
