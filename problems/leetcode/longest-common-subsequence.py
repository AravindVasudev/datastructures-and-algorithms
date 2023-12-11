# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dfs(t1 = 0, t2 = 0):
            if t1 == len(text1) or t2 == len(text2):
                return 0
            
            if text1[t1] == text2[t2]:
                return 1 + dfs(t1 + 1, t2 + 1)
            
            return max(dfs(t1 + 1, t2), dfs(t1, t2 + 1))
        
        return dfs()

# Bottom-Up
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        memo = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

        return memo[M][N]

# Bottom-Up Space Optimized
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        M, N = len(text1), len(text2)
        prevRow = [0] * (N + 1)
        curRow = [0] * (N + 1)
    
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    curRow[j] = 1 + prevRow[j - 1]
                else:
                    curRow[j] = max(prevRow[j], curRow[j - 1])

            prevRow, curRow = curRow, prevRow

        return prevRow[N]
