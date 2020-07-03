# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        beforeSet = set(['I', 'X', 'C'])
        
        intVal = 0
        for i, digit in enumerate(s):
            if i + 1 == len(s) or digit not in beforeSet:
                intVal += romanToInt[digit]
                continue
                
            if digit == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                intVal -= 1  
            elif digit == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                intVal -= 10
            elif (s[i + 1] == 'D' or s[i + 1] == 'M'):
                intVal -= 100
            else:
                intVal += romanToInt[digit]
            
        return intVal
