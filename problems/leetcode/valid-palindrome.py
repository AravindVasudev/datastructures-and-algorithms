# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        startIndex, endIndex = 0, len(s) - 1
        s = s.lower()
        
        while startIndex <= endIndex:
            # Skip non-alphanumeric
            if not s[startIndex].isalnum():
                startIndex += 1
                continue
                
            if not s[endIndex].isalnum():
                endIndex -= 1
                continue
            
            # Check
            if s[startIndex] != s[endIndex]:
                return False
            
            # Move index
            startIndex += 1
            endIndex -= 1
        
        return True
