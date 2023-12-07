# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      vowels = lambda c: c["a"] + c["e"] + c["i"] + c["o"] + c["u"]
      window = Counter(s[:k])
      start, count = 0, vowels(window)

      for end in range(k, len(s)):
        window[s[end]] += 1
        window[s[start]] -= 1
        start += 1
        
        count = max(count, vowels(window))

      return count
