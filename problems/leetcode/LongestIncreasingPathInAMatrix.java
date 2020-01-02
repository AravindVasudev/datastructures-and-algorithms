// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
class Solution {
    int[][] dir = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int M = matrix.length;
        int N = matrix[0].length;

        int[][] memo = new int[M][N];
        int longest = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                longest = Math.max(dfs(matrix, i, j, memo), longest);
            }
        }

        return longest;
    }

    private int dfs(int[][] matrix, int i, int j, int[][] memo) {
        if (memo[i][j] > 0) {
            return memo[i][j];
        }

        for (int[] curDir : dir) {
            int curI = i + curDir[0];
            int curJ = j + curDir[1];

            if (curI < 0 || curI >= matrix.length ||
                curJ < 0 || curJ >= matrix[0].length ||
                matrix[i][j] >= matrix[curI][curJ]) {
                continue;
            }

            memo[i][j] = Math.max(memo[i][j], dfs(matrix, curI, curJ, memo));
        }

        return ++memo[i][j];
    }
}
