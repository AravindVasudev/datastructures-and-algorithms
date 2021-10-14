# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        
        start, end = len(nums), 0
        for i, num in enumerate(nums):
            if num != sortedNums[i]:
                start = min(start, i)
                end = max(end, i)
                
        return max(0, end - start + 1)
        
# Efficient Solution
