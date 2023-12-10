# https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])

            transposed.append(row)

        return transposed
