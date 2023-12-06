# https://leetcode.com/problems/unique-number-of-occurrences/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
      counter = Counter(arr)
      occurences = set()
      for occurence in counter.values():
        if occurence in occurences:
          return False

        occurences.add(occurence)

      return True
