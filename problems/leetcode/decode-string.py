# https://leetcode.com/problems/decode-string/
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNumber, curString = 0, ""
        
        for c in s:
            if c == "[":
                stack.append(curString)
                stack.append(curNumber)
                
                curNumber, curString = 0, ""
            elif c == "]":
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                curNumber = curNumber * 10 + int(c)
            else:
                curString += c
                
        return curString
