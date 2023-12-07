# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
      index = lambda c: ord(c) - ord("a")
      def counter(word):
        count = [0] * 26
        for c in word:
          count[index(c)] += 1

        return count

      charsCount = counter(chars)
      length = 0

      for word in words:
        count = counter(word)
        valid = True
        for i in range(len(count)):
          if charsCount[i] < count[i]:
            valid = False
            break

        if valid:
          length += len(word)

      return length
        
