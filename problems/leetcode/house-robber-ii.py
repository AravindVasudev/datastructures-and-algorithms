# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        return max(self.robRange(nums, 0, len(nums) - 2), self.robRange(nums, 1, len(nums) - 1))

    def robRange(self, nums: List[int], i: int, j: int) -> int:
        prev_two, prev_one = 0, 0
        cur = 0
        for index in range(i, j + 1):
            cur = max(prev_two + nums[index], prev_one)
            prev_two, prev_one = prev_one, cur
            
        return cur
