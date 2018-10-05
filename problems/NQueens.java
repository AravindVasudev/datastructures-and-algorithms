import java.util.Scanner;

public class NQueens {
    private boolean[][] board;
    private int n;

    NQueens(int n) {
        this.n = n;
        board = new boolean[n][n];
    }

    private boolean isSafe(int x, int y) {
        for (int i = 0; i < y; i++) {
            if (board[x][i]) {
                return false;
            }
        }

        for (int i = x, j = y; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j]) {
                return false;
            }
        }

        for (int i = x, j = y; i < n && j >= 0; i++, j--) {
            if (board[i][j]) {
                return false;
            }
        }

        return true;
    }

    boolean solve() {
        return solve(n, 0);
    }

    private boolean solve(int n, int col) {
        if (n == 0) {
            return true;
        }

        for (int i = 0; i < this.n; i++) {
            if (isSafe(i, col)) {
                board[i][col] = true;

                if (solve(n - 1, col + 1)) {
                    return true;
                }

                board[i][col] = false;
            }
        }

        return false;
    }

    String visualizeBoard() {
        StringBuilder visualized = new StringBuilder();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                visualized.append(board[i][j] ? 1 : 0).append(" ");
            }

            visualized.append("\n");
        }

        return visualized.toString();
    }

    public static void main(String[] args) {
        NQueens nQueens = new NQueens(new Scanner(System.in).nextInt());
        if (nQueens.solve()) {
            System.out.println("YES");
            System.out.println(nQueens.visualizeBoard());
        } else {
            System.out.println("NO");
        }
    }
}
