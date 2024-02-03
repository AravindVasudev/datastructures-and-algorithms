# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_index = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[new_index] = nums[i]
                new_index += 1

        return new_index
