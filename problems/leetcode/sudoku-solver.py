# https://leetcode.com/problems/sudoku-solver/
import math

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)

    def isValid(self, board: List[List[str]], row: int, col: int, val: str) -> bool:
            # Row & Col Check
            for i in range(9):
                if (board[row][i] == val) or (board[i][col] == val):
                    return False

            # Grid Check
            offsetI = math.floor(row / 3) * 3
            offsetJ = math.floor(col / 3) * 3

            for i in range(3):
                for j in range(3):
                    if board[offsetI + i][offsetJ + j] == val:
                        return False

            return True

    def getNextEmpty(self, board: List[List[str]]) -> (int, int):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j

        return -1, -1

    def solve(self, board: List[List[str]], row=0, col=0) -> bool:
        i, j = self.getNextEmpty(board)

        if i == -1: # Done State
            return True

        for val in range(1, 10):
            if self.isValid(board, i, j, str(val)):
                board[i][j] = str(val)

                if self.solve(board, i, j):
                    return True

        board[i][j] = '.' # Backtrack
        return False
