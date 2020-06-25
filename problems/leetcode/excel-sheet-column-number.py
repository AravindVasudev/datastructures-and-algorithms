# https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, s: str) -> int:
        power = 0
        val = 0
        for i in range(len(s) - 1, -1, -1):
            val += (ord(s[i]) - 64) * (26 ** power)
            power += 1
            
        return val
