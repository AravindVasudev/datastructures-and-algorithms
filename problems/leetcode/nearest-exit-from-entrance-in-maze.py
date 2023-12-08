# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        isExit = lambda x: (x[0] == 0 or x[0] == M - 1 or
            x[1] == 0 or x[1] == N - 1)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()
        q.append((entrance, 0))
        maze[entrance[0]][entrance[1]] = "+"

        while q:
            cell, steps = q.popleft()

            if steps != 0 and isExit(cell):
                return steps

            for x, y in directions:
                i, j = cell[0] + x, cell[1] + y
                if (0 <= i < M and 0 <= j < N and
                    maze[i][j] != "+"):
                    maze[i][j] = "+"
                    q.append(([i, j], steps+1))

        return -1
