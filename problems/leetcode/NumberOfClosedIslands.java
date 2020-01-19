// https://leetcode.com/problems/number-of-closed-islands
class Solution {
    public int closedIsland(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }

        int N = grid.length;
        int M = grid[0].length;

        int islands = 0;
        boolean[][] visited = new boolean[N][M];

        for (int i = 1; i < N - 1; i++) {
            for (int j = 1; j < M - 1; j++) {
                if (grid[i][j] == 1 || visited[i][j]) {
                    continue;
                }

                boolean[][] curVisited = new boolean[N][M];
                islands += dfs(grid, i, j, curVisited, visited) ? 1 : 0;
            }
        }

        return islands;
    }

    private boolean dfs(int[][] grid, int i, int j, boolean[][] curVisited, boolean[][] visited) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) {
            return false;
        }

        if (curVisited[i][j] || grid[i][j] == 1) {
            return true;
        }

        visited[i][j] = true;
        curVisited[i][j] = true;

        return dfs(grid, i + 1, j, curVisited, visited) &&
            dfs(grid, i - 1, j, curVisited, visited) &&
            dfs(grid, i, j + 1, curVisited, visited) &&
            dfs(grid, i, j - 1, curVisited, visited);
    }
}
