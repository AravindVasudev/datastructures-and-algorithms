# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openingIndex, closingIndex = [], []
        
        for index, char in enumerate(s):
            if char == "(":
                openingIndex.append(index)
            elif char == ")":
                if len(openingIndex) > 0:
                    openingIndex.pop()
                else:
                    closingIndex.append(index)
            
        
        invalidIndex = set(openingIndex + closingIndex)
        result = ""
        for index, char in enumerate(s):
            if index not in invalidIndex:
                result += char
                
        return result
