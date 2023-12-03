class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined = ""
        for a, b in zip(word1, word2):
            combined += a + b

        if len(word2) > len(word1):
            word1, word2 = word2, word1

        return combined + word1[len(word2):]
