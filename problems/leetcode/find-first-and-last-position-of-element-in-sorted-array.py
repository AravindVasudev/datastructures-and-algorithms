# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def boundedBinarySearch(forward: bool) -> int:
            left, right = 0, len(nums) - 1
            while left < right:
                if forward:
                    mid = (left + right + 1) // 2
                    
                    if nums[mid] <= target:
                        left = mid
                    else:
                        right = mid - 1
                else:
                    mid = (left + right) // 2
                    
                    if nums[mid] >= target:
                        right = mid
                    else:
                        left = mid + 1
                        
            return left if 0 <= left < len(nums) and nums[left] == target else -1
        
        leftBound = boundedBinarySearch(False)
        if leftBound == -1:
            return [-1, -1]
        
        return [leftBound, boundedBinarySearch(True)]
