// https://leetcode.com/problems/surrounded-regions
class Solution {
    int[][] dir = new int[][] {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public void solve(char[][] board) {
        if (board == null || board.length == 0) {
            return;
        }

        int N = board.length;
        int M = board[0].length;

        boolean[][] unbounded = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            dfs(board, i, 0, unbounded);
            dfs(board, i, M - 1, unbounded);
        }

        for (int j = 0; j < M; j++) {
            dfs(board, 0, j, unbounded);
            dfs(board, N - 1, j, unbounded);
        }

        for (int i = 1; i < N - 1; i++) {
            for (int j = 1; j < M - 1; j++) {
                if (board[i][j] == 'O' && !unbounded[i][j]) {
                    board[i][j] = 'X';
                }
            }
        }
    }

    private void dfs(char[][] board, int i, int j, boolean[][] unbounded) {
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] == 'X' || unbounded[i][j]) {
            return;
        }

        unbounded[i][j] = true;
        for (int[] d : dir) {
            dfs(board, i + d[0], j + d[1], unbounded);
        }
    }
}
