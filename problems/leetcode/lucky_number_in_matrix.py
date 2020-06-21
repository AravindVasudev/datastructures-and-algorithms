# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        luckies = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.isLucky(matrix, i, j):
                    luckies.append(matrix[i][j])
                    
        return luckies
    
    def isLucky(self, matrix: List[List[int]], i: int, j: int) -> bool:
        for row in range(len(matrix)):
            if matrix[row][j] > matrix[i][j]:
                return False
            
        for col in range(len(matrix[i])):
            if matrix[i][col] < matrix[i][j]:
                return False
            
        return True
