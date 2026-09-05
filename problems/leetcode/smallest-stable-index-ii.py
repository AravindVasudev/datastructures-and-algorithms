# https://leetcode.com/problems/smallest-stable-index-ii/
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        leftMax = [nums[0]]
        for i in range(1, len(nums)):
            leftMax.append(max(leftMax[-1], nums[i]))

        rightMin = [0] * len(nums)
        rightMin[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            rightMin[i] = min(rightMin[i + 1], nums[i])

        for i in range(len(nums)):
            if leftMax[i] - rightMin[i] <= k:
                return i

        return -1
