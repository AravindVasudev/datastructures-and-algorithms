# https://leetcode.com/problems/shortest-path-to-get-food/
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        move = lambda x, y: (x[0] + y[0], x[1] + y[1])
        foodCells = self.getFoodCells(grid)

        q = deque()
        q.append(self.getStart(grid))

        level = 0
        while q:
            levelSize = len(q)
            for _ in range(levelSize):
                cur = q.popleft()
                if cur in foodCells:
                    return level

                for d in directions:
                    nxt = move(cur, d)
                    if (0 <= nxt[0] < len(grid) and
                        0 <= nxt[1] < len(grid[0]) and
                        grid[nxt[0]][nxt[1]] != "X"):
                        grid[nxt[0]][nxt[1]] = "X"
                        q.append(nxt)

            level += 1

        return -1

    def getFoodCells(self, grid: List[List[str]]) -> Set[tuple[int, int]]:
        food = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "#":
                    food.add((i, j))

        return food

    def getStart(self, grid: List[List[str]]) -> tuple[int, int]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "*":
                    return (i, j)

        return None
