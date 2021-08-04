# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        newArrayIndex = 0
        for nextIndex in range(1, len(nums)):
            if nums[newArrayIndex] != nums[nextIndex]:
                newArrayIndex += 1
                nums[newArrayIndex] = nums[nextIndex]
                
        return newArrayIndex + 1
