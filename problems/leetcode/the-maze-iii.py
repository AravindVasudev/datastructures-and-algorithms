# https://leetcode.com/problems/the-maze-iii/
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        ball, hole = tuple(ball), tuple(hole)
        M, N = len(maze), len(maze[0])
        directions = [(0, -1, "l"), (-1, 0, "u"), (0, 1, "r"), (1, 0, "d")] # Up, Down, Right, Left.

        # Helpers
        canMove = lambda cell, d: (0 <= cell[0] + d[0] < M and 0 <= cell[1] + d[1] < N and
            maze[cell[0] + d[0]][cell[1] + d[1]] == 0)
        move = lambda cell, d: (cell[0] + d[0], cell[1] + d[1])

        # min-heap of cells to visit.
        # [(dist, path, cell)].
        pq = [(0, "", ball)]

        # Visited Table.
        visited = [[False] * N for _ in range(M)]

        while pq:
            dist, path, cell = heapq.heappop(pq)
            if visited[cell[0]][cell[1]]:
                continue

            if cell == hole:
                return path

            visited[cell[0]][cell[1]] = True
            for d in directions:
                newCell, newDist = cell, dist
                while canMove(newCell, d):
                    newCell = move(newCell, d)
                    newDist += 1

                    if newCell == hole:
                        break

                heapq.heappush(pq, (newDist, path + d[2], newCell))

        # If not path exists, return impossible.
        return "impossible"
