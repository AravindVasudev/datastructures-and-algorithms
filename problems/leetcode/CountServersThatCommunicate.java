// https://leetcode.com/problems/count-servers-that-communicate
class Solution {
    public int countServers(int[][] grid) {
        if (grid == null || grid[0].length == 0 || grid[0].length == 0) {
            return 0;
        }

        int N = grid.length;
        int M = grid[0].length;

        int[] rowCount = new int[N];
        int[] colCount = new int[M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == 1) {
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }

        int communicatable = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == 1 && (rowCount[i] > 1 || colCount[j] > 1)) {
                    communicatable++;
                }
            }
        }

        return communicatable;
    }
}
