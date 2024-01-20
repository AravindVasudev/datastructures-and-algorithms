# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Helpers.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right.
        move = lambda x, y: (x[0] + y[0], x[1] + y[1])
        M, N = len(grid), len(grid[0])
        end = (M - 1, N - 1)

        # BFS Datastructures.
        q = deque([((0, 0), k, 0)])
        visited = set([((0, 0), k)])

        while q:
            node, eliminations, steps = q.popleft()

            if node == end:
                return steps

            for d in directions:
                nxt = move(node, d)
                if 0 <= nxt[0] < M and 0 <= nxt[1] < N:
                    e = (eliminations
                        if grid[nxt[0]][nxt[1]] == 0 else eliminations - 1)

                    if e < 0 or (nxt, e) in visited:
                        continue

                    visited.add((nxt, e))
                    q.append((nxt, e, steps + 1))

        return -1
