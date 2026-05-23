# https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def backtrack(i: int, current: list[int]) -> None:    
            if len(current) == k:
                results.append(current[:])
                return

            if i > n:
                return

            current.append(i)
            backtrack(i + 1, current)

            current.pop()
            backtrack(i + 1, current)

        backtrack(1, [])
        return results

# Optimal w/ pruning
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def backtrack(i: int, current: list[int]) -> None:    
            if len(current) == k:
                results.append(current[:])
                return

            remainingNeeded = k - len(current)
            end = n - remainingNeeded + 1

            for num in range(i, end + 1):
                current.append(num)
                backtrack(num + 1, current)
                current.pop()


        backtrack(1, [])
        return results
