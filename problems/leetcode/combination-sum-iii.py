# https://leetcode.com/problems/combination-sum-iii/
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def dfs(i, path, total):
            if len(path) == k:
                if total == n:
                    result.append(path)

                return

            if i == 10 or total + i > n:
                return

            dfs(i + 1, path + [i], total + i)
            dfs(i + 1, path, total)

        dfs(1, [], 0)
        return result
