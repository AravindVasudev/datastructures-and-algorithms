# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate(n, "", 0, 0, [])
    
    def generate(self, n: int, string: str, opening: int, closing: int, result: List[str]) -> List[str]:
        if len(string) == n * 2:
            result.append(string)
            return
        
        if opening < n:
            self.generate(n, string + "(", opening + 1, closing, result)
            
        if closing < opening:
            self.generate(n, string + ")", opening, closing + 1, result)
            
        return result
