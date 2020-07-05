# https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)
        
        
    def binarySearch(self, nums, left, right, x):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if nums[mid] == x:
            return mid
        
        if nums[mid] > x:
            return self.binarySearch(nums, left, mid - 1, x)
        
        return self.binarySearch(nums, mid + 1, right, x)
