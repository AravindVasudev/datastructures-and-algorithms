# https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        total = 0
        for num in nums:
            total += num
            runningSum.append(total)
            
        return runningSum
