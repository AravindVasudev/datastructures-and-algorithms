# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start, count = 0, 0
        zeros = 0

        for end in range(len(nums)):
          if nums[end] == 0:
            zeros += 1

          while zeros > 1:
            if nums[start] == 0:
              zeros -= 1

            start += 1

          count = max(count, end - start)

        return count
