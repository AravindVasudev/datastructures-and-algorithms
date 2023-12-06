# https://leetcode.com/problems/determine-if-two-strings-are-close/
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
      if len(word1) != len(word2):
        return False

      count1, count2 = Counter(word1), Counter(word2)
      if set(count1.keys()) != set(count2.keys()):
        return False

      return sorted(count1.values()) == sorted(count2.values())
