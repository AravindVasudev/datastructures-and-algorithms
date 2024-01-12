# https://leetcode.com/problems/max-area-of-island/
class Solution:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    move = lambda x, y: (x[0] + y[0], x[1] + y[1])

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxArea = max(maxArea, self.computeArea(grid, (i, j)))

        return maxArea

    def computeArea(self, grid: List[List[int]], start: tuple[int, int]) -> int:
        if grid[start[0]][start[1]] == 0:
            return 0

        grid[start[0]][start[1]] = 0
        area = 1

        for d in self.directions:
            nxt = Solution.move(start, d)
            if 0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0]):
                area += self.computeArea(grid, nxt)

        return area
