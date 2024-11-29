# https://leetcode.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total

                if abs(target - total) < abs(target - closest):
                    closest = total

                if target > total:
                    left += 1
                else:
                    right -= 1

        return closest
