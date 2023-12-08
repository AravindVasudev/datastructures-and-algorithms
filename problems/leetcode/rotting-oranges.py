# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()
        fresh = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append(([i, j], 0))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0
        while q:
            orange, steps = q.popleft()
            minutes = max(minutes, steps)

            for x, y in directions:
                i, j = orange[0] + x, orange[1] + y
                if (0 <= i < M and 0 <= j < N and
                    grid[i][j] == 1):
                    fresh -= 1
                    grid[i][j] = 2
                    q.append(([i, j], steps + 1))

        return minutes if fresh == 0 else -1
