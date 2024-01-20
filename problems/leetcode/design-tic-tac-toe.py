# https://leetcode.com/problems/design-tic-tac-toe/
class TicTacToe:

    def __init__(self, n: int):
        # Init counters for winning.
        self.rows = [0] * n
        self.cols = [0] * n
        self.leading_diag = 0
        self.anti_diag = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        # +ve direction for player 1 and -ve for player 2.
        move = 1 if player == 1 else -1

        # Add the move to the row, col, and diags.
        self.rows[row] += move
        self.cols[col] += move
        
        if row == col:
            self.leading_diag += move
        
        if row + col == self.n - 1:
            self.anti_diag += move

        # If the current player won, return player.
        if (self.n * move) in (self.rows[row], self.cols[col],
            self.leading_diag, self.anti_diag):
            return player

        # No one won yet.
        return 0
