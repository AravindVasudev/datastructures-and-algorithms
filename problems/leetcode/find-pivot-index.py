# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum = 0
        rSum = sum(nums)

        for i, num in enumerate(nums):
            if lSum == (rSum - lSum - num):
                return i

            lSum += num

        return -1
