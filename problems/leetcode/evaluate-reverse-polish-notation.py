# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(x / y)
        }

        for token in tokens:
            if token in operations:
                num2, num1 = stack.pop(), stack.pop()
                stack.append(operations[token](num1, num2))
            else:
                stack.append(int(token))
        
        return stack[-1]
