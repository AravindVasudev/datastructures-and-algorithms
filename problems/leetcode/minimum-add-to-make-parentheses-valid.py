# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openBraces, neededBraces = 0, 0
        for x in s:
            if x == "(":
                openBraces += 1
            elif x == ")":
                if openBraces == 0:
                    neededBraces += 1
                else:
                    openBraces -= 1

        return neededBraces + openBraces
