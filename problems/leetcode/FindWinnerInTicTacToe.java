// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
class Solution {
    int X = 1;
    int Y = -100;
    public String tictactoe(int[][] moves) {
        int[][] board = new int[3][3];

        boolean isX = true;
        for (int i = 0; i < moves.length && i < 9; i++) {
            board[moves[i][0]][moves[i][1]] = isX ? X : Y;

            if (isDone(board)) {
                return isX ? "A" : "B";
            }

            isX = !isX;
        }

        return moves.length == 9 ? "Draw" : "Pending";
    }

    private boolean isDone(int[][] board) {
        int leadingDiagonal = 0;
        int otherDiagonal = 0;

        int xWin = X * board.length;
        int yWin = Y * board.length;

        for (int i = 0; i < board.length; i++) {
            int rowCount = 0;
            int colCount = 0;
            for (int j = 0; j < board.length; j++) {
                rowCount += board[i][j];
                colCount += board[j][i];
            }

            if (rowCount == xWin || rowCount == yWin ||
                colCount == xWin || colCount == yWin) {
                return true;
            }

            leadingDiagonal += board[i][i];
            otherDiagonal += board[board.length - 1 - i][i];
        }

        return leadingDiagonal == xWin || leadingDiagonal == yWin || otherDiagonal == xWin || otherDiagonal == yWin;
    }
}
