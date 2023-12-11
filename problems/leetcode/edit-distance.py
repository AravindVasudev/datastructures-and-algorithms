# https://leetcode.com/problems/edit-distance/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def distance (word1Ptr: int = 0, word2Ptr: int = 0):
            if word1Ptr == len(word1) and word2Ptr == len(word2):
                return 0

            if word1Ptr == len(word1):
                return len(word2) - word2Ptr

            if word2Ptr == len(word2):
                return len(word1) - word1Ptr

            if word1[word1Ptr] == word2[word2Ptr]:
                return distance(word1Ptr + 1, word2Ptr + 1)

            insertion = distance(word1Ptr, word2Ptr + 1)
            deletion = distance(word1Ptr + 1, word2Ptr)
            replacement = distance(word1Ptr + 1, word2Ptr + 1)

            return min(insertion, deletion, replacement) + 1
        
        return distance()

# Top-Down
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        memo = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(1, M + 1):
            memo[i][0] = i

        for j in range(1, N + 1):
            memo[0][j] = j

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                    continue

                memo[i][j] = min(
                    memo[i - 1][j - 1],
                    memo[i - 1][j],
                    memo[i][j - 1],
                ) + 1
                
        return memo[M][N]
