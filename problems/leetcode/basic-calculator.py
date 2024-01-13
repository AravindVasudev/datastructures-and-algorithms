# https://leetcode.com/problems/basic-calculator/
# https://leetcode.com/problems/basic-calculator-ii/
# https://leetcode.com/problems/basic-calculator-iii/
class Solution:
    def calculate(self, s: str) -> int:
        def update(op, v):
            if op == "+": stack.append(v)
            elif op == "-": stack.append(-v)
            elif op == "*": stack.append(stack.pop() * v)
            else: stack.append(int(stack.pop() / v))

        stack = []
        num, op = 0, "+"
        for c in s:
            if c.isdigit():
                num = (num * 10) + int(c)
            if c in "+-/*":
                # When c hits a operator, process the previous
                # op first.
                update(op, num)
                num, op = 0, c
            elif c == "(":
                stack.append(op)
                op = "+"
            elif c == ")":
                update(op, num)
                num, op = 0, c

                while type(stack[-1]) == int:
                    num += stack.pop()
                op = stack.pop()

        update(op, num)
        return sum(stack)
                
