# https://leetcode.com/problems/max-consecutive-ones-iii/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
      start, count = 0, 0
      window = [0, 0]

      for end in range(len(nums)):
        window[nums[end]] += 1

        while window[0] > k:
          window[nums[start]] -= 1
          start += 1

        count = max(count, end - start + 1)

      return count
