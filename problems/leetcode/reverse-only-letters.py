 # https://leetcode.com/problems/reverse-only-letters/
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        sArr = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalpha():
                i += 1
                continue
                
            if not s[j].isalpha():
                j -= 1
                continue
                
            sArr[i], sArr[j] = sArr[j], sArr[i]
            i += 1
            j -= 1
            
        return "".join(sArr)
