# https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:    
        return self.getNumWays(s, 0, [-1] * len(s))
    
    def getNumWays(self, s: str, index: int, memo: List[int]) -> int:
        if index == len(s):
            return 1
        
        if s[index] == "0":
            return 0
        
        if memo[index] != -1:
            return memo[index]
        
        ways = self.getNumWays(s, index + 1, memo)
        if index + 1 < len(s) and int(s[index:index + 2]) <= 26:
            ways += self.getNumWays(s, index + 2, memo)
        
        memo[index] = ways
        return memo[index]
