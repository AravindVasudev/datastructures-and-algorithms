# https://leetcode.com/problems/minesweeper/
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or len(board) == 0 or len(board[0]) == 0 or not click or len(click) != 2:
            return board
        
        # If clicked on mine
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        # If empty
        directions = [[-1, -1], [-1, 0], [-1, 1],
                      [ 0, -1],          [ 0, 1],
                      [ 1, -1], [ 1, 0], [ 1, 1]]
        
        boundryCheck = lambda x, y: 0 <= x < len(board) and 0 <= y < len(board[0])
        
        queue = deque()
        queue.append(click)
        board[click[0]][click[1]] = "B"
        
        while queue:
            x, y = queue.popleft()
            
            neighbors = []
            mineCount = 0
            
            for i, j in directions:
                if boundryCheck(x+i, y+j) and board[x+i][y+j] == "M":
                    mineCount += 1
                    
            if mineCount > 0:
                board[x][y] = str(mineCount)
                continue
                
            for i, j in directions:
                if boundryCheck(x+i, y+j) and board[x+i][y+j] == "E":
                    board[x+i][y+j] = "B"
                    queue.append((x+i, y+j))

        return board    
