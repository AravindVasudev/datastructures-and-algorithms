# https://leetcode.com/problems/the-maze/
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Helpers
        M, N = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # down, up, left, right.
        
        isDestination = lambda cell: cell[0] == destination[0] and cell[1] == destination[1]
        move = lambda cell, dir: [cell[0] + dir[0], cell[1] + dir[1]]
        isValid = lambda cell: 0 <= cell[0] < M and 0 <= cell[1] < N and maze[cell[0]][cell[1]] == 0

        # BFS Datastructures
        q = deque()
        visited = [[False] * N for _ in range(M)]

        # BFS
        q.append(start)
        visited[start[0]][start[1]] = True

        while q:
            cell = q.popleft()
            if isDestination(cell):
                return True

            for d in directions:
                cur = cell

                # While valid, keep moving in the same direction.
                toMove = move(cur, d)
                while isValid(toMove):
                    cur = toMove
                    toMove = move(cur, d)

                # Add the new cell to the queue.
                if not visited[cur[0]][cur[1]]:
                    q.append(cur)
                    visited[cur[0]][cur[1]] = True

        return False
