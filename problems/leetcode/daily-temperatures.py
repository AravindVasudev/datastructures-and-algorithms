# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        stack = []
        result = [0] * N
        for i in reversed(range(N)):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                result[i] = (stack[-1] - i)

            stack.append(i)

        return result
