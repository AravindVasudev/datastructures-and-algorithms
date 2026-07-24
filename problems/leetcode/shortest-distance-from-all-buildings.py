# Mirror of https://leetcode.com/problems/shortest-distance-from-all-buildings/
# Solved in https://algo.monster/liteproblems/317
from collections import deque

def shortest_distance_from_all_buildings(grid: list[list[int]]) -> int:
    M, N = len(grid), len(grid[0])
    dist = [[0] * N for _ in range(M)]
    buildingCount = [[0] * N for _ in range(M)]
    buildings = 0

    # BFS from building -> empty cell
    def bfs(i, j):
        queue = deque([(i, j)])
        visited = [[False] * N for _ in range(M)]
        visited[i][j] = True

        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dirX, dirY in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nxtX, nxtY = x + dirX, y + dirY
                    if 0 <= nxtX < M and 0 <= nxtY < N and grid[nxtX][nxtY] == 0 and not visited[nxtX][nxtY]:
                        visited[nxtX][nxtY] = True
                        dist[nxtX][nxtY] += level + 1
                        buildingCount[nxtX][nxtY] += 1

                        queue.append((nxtX, nxtY))

            level += 1
            

    # BFS from every building
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                buildings += 1
                bfs(i, j)

    # Find the smallest empty cell
    smallest = float("inf")
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0 and buildingCount[i][j] == buildings and smallest > dist[i][j]:
                smallest = dist[i][j]

    return smallest if smallest != float("inf") else -1
