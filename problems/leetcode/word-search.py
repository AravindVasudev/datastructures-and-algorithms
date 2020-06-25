# https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == word[0] and self.lookup(board, word, set(), i, j):
                    return True
                
        return False
    
    def lookup(self, board, word, seen, row, col, wordPos=0):
        if wordPos >= len(word):
            return True

        if row < 0 or row >= len(board) or \
            col < 0 or col >= len(board[0]) or \
            (row, col) in seen:
            return False
        
        if board[row][col] != word[wordPos]:
            return False
        
        seen.add((row, col))
        for dir in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if self.lookup(board, word, seen, row + dir[0], col + dir[1], wordPos + 1):
                return True
            
        seen.remove((row, col))
        return False
