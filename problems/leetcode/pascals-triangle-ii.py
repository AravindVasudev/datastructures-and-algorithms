# https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.getRowRecur([1], rowIndex)
    
    def getRowRecur(self, prevRow, rowIndex):
        if rowIndex == 0:
            return prevRow
        
        curRow = [prevRow[0]]
        for i in range(1, len(prevRow)):
            curRow.append(prevRow[i - 1] + prevRow[i])
            
        curRow.append(1)
        return self.getRowRecur(curRow, rowIndex - 1)
