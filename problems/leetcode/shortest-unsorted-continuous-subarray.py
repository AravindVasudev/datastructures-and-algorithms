# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        
        start, end = len(nums), 0
        for i, num in enumerate(nums):
            if num != sortedNums[i]:
                start = min(start, i)
                end = max(end, i)
                
        return max(0, end - start + 1)
        
# Efficient Solution
# Solution: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103067/Python-O(N)-with-O(1)-space-complexity.-No-sorting
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        left, right = 0, len(nums) - 1
        
        # Find the first non-ascending index
        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
            left += 1
            
        # Find the first non-descending index from the last
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
            
        if left > right:
            return 0
        
        temp = nums[left:right+1]
        tempMin = min(temp)
        tempMax = max(temp)
        
        # Move left until the minimum finds its position
        while left > 0 and tempMin < nums[left - 1]:
            left -= 1
            
        # Move right until the maximum finds its position
        while right < len(nums) - 1 and tempMax > nums[right + 1]:
            right += 1
            
        return right - left + 1
