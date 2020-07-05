# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows is 0:
            return []

        return self.pascal(numRows, [[1]])
        
    def pascal(self, numRows, result):
        if numRows == 1:
            return result
        
        curRow = [1]
        prevRow = result[-1]
        for i in range(1, len(prevRow)):
            curRow.append(prevRow[i] + prevRow[i - 1])
            
        curRow.append(1)
        result.append(curRow)
        
        return self.pascal(numRows - 1, result)
