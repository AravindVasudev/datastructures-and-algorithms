# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        sIndex = 0
        for tIndex, tChar in enumerate(t):
            if s[sIndex] == tChar:
                sIndex += 1
                
            if sIndex == len(s):
                return True
            
        return False
