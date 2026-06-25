# https://leetcode.com/problems/swim-in-rising-water/
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        queue = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        while queue:
            elevation, x, y = heapq.heappop(queue)
            if x == N - 1 and y == M - 1:
                return elevation

            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nextX, nextY = x + i, y + j
                if 0 <= nextX < N and 0 <= nextY < M and (nextX, nextY) not in visited:
                    visited.add((nextX, nextY))
                    heapq.heappush(queue, (max(elevation, grid[nextX][nextY]), nextX, nextY))

        return -1
