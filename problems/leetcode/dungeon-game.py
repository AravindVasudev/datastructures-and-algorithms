# https://leetcode.com/problems/dungeon-game/
class Solution:
    def calculateMinimumHP(self, dungeon):
        cache = [[-1 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        return self.solve(dungeon, cache)

    def solve(self, dungeon, cache, row=0, col=0):
        if row >= len(dungeon) or col >= len(dungeon[0]):
            return float('inf')

        if row == len(dungeon) - 1 and col == len(dungeon[0]) - 1:
            return 1 if dungeon[row][col] > 0 else -dungeon[row][col] + 1

        if cache[row][col] != -1:
            return cache[row][col]

        cache[row][col] = max(1, min(self.solve(dungeon, cache, row + 1, col) - dungeon[row][col],
                                self.solve(dungeon, cache, row, col + 1) - dungeon[row][col]))

        return cache[row][col]

#########################
# Top Down
#########################
class Solution:
    def calculateMinimumHP(self, dungeon):
        M, N = len(dungeon), len(dungeon[0])
        cache = [[float('inf') for _ in range(N + 1)] for _ in range(M + 1)]

        cache[M - 1][N], cache[M][N - 1] = 1, 1
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                cache[i][j] = max(1, min(cache[i + 1][j] - dungeon[i][j],
                                         cache[i][j + 1] - dungeon[i][j]))

        return cache[0][0]
