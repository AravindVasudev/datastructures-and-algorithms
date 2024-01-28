# https://leetcode.com/problems/toeplitz-matrix/
class Solution:
    def isToeplitzMatrix(self, arr: List[List[int]]) -> bool:
        N = len(arr)
        if N == 0:
            return True

        M = len(arr[0])
        if M == 0:
            return True

        for j in range(M):
            row, col = 0, j
            diagonalElement = arr[0][j]
            
            while row < N and col < M:
                if arr[row][col] != diagonalElement:
                    return False
                
                row += 1
                col += 1

        for i in range(1, N):
            row, col = i, 0
            diagonalElement = arr[i][0]
            
            while row < N and col < M:
                if arr[row][col] != diagonalElement:
                    return False
                
                row += 1
                col += 1

        return True

# Cleaner Solution
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i - 1][j - 1] != matrix[i][j]:
                    return False

        return True
