# https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowSet, colSet = set(), set()
            
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rowSet:
                        return False
                    
                    rowSet.add(board[i][j])
                    
                if board[j][i] != '.':
                    if board[j][i] in colSet:
                        return False
                    
                    colSet.add(board[j][i])
                    
        for gridI in range(3):
            for gridJ in range(3):
                offsetI = gridI * 3
                offsetJ = gridJ * 3
                gridSet = set()

                for i in range(offsetI, offsetI + 3):
                    for j in range(offsetJ, offsetJ + 3):
                        if board[i][j] != '.':
                            if board[i][j] in gridSet:
                                return False
                            
                            gridSet.add(board[i][j])
                            
        return True
