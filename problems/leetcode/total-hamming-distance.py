# https://leetcode.com/problems/total-hamming-distance/
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        for bit in range(32):
            ones = 0
            for num in nums:
                ones += (num >> bit) & 1

            zeros = len(nums) - ones
            total += zeros * ones

        return total
