# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        maxSum = float('-inf')
        windowSum = 0
        
        for j, num in enumerate(nums):
            windowSum += num
            maxSum = max(maxSum, windowSum)
            
            if windowSum < 0:
                i = j + 1
                windowSum = 0
            
        return maxSum
