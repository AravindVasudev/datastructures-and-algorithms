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
