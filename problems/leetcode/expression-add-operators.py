# https://leetcode.com/problems/expression-add-operators
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N, result = len(num), []

        def backtrack(index: int, path: str, value: int, prev: int) -> None:
            if index == N:
                if value == target:
                    result.append(path)
                return

            for i in range(index, N):
                if i != index and num[index] == "0":
                    break # Don't process leading zeros.


                curStr = num[index:i+1]
                cur = int(curStr)

                # No symbol before starting
                if index == 0:
                    backtrack(i + 1, curStr, cur, cur)
                else:
                    backtrack(i + 1, f"{path}+{curStr}", value + cur, cur)
                    backtrack(i + 1, f"{path}-{curStr}", value - cur, -cur)
                    backtrack(i + 1, f"{path}*{curStr}", value - prev + prev * cur, prev * cur)

        backtrack(0, "", 0, 0)
        return result
