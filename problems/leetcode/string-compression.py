# https://leetcode.com/problems/string-compression/
class Solution:
    def compress(self, chars: List[str]) -> int:
      newIndex = 0
      char, count = "", 0

      for c in chars:
        if c == char:
          count += 1
          continue

        if count > 0:
          chars[newIndex] = char
          newIndex += 1

        if count > 1:
          for i in str(count):
            chars[newIndex] = i
            newIndex += 1

        count = 1
        char = c

      return newIndex
        
