# https://leetcode.com/problems/maximum-average-subarray-i/
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        maxAvg = window / k
  
        for i in range(k, len(nums)):
          window += nums[i] - nums[i-k]
          maxAvg = max(maxAvg, window / k)

        return maxAvg
