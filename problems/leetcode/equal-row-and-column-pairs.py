# https://leetcode.com/problems/equal-row-and-column-pairs/
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs, N = 0, len(grid)
        hashes = Counter(tuple(row) for row in grid)

        for j in range(N):
          col = [grid[i][j] for i in range(N)]
          pairs += hashes[tuple(col)]

        return pairs
