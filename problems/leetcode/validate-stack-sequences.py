# https://leetcode.com/problems/validate-stack-sequences/
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while pushed or popped:
            if stack and popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
            elif pushed:
                stack.append(pushed.pop(0))
            else:
                return False
        
        return not (pushed and popped)
