# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findOffset() -> int:
            start, end = 0, len(nums) - 1
            while start < end:
                mid = (start + end) // 2
                if nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid

            return start

        return nums[findOffset()]
