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
