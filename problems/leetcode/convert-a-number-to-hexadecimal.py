# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        charset = '0123456789abcdef'
        result = ''
        
        while num != 0 and len(result) < 8:
            result = charset[num & 15] + result            
            num >>= 4
            
        return result
