# https://leetcode.com/problems/split-array-largest-sum/
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.split(nums, mid) > m:
                left = mid + 1
            else:
                right = mid
                
        
        return left
    
    def split(self, nums: List[int], cap: int) -> int:
        splits = 0
        currentTotal = 0

        for x in nums:
            currentTotal += x
            if currentTotal > cap:
                currentTotal = x
                splits += 1
                
        return splits + 1 # sub array = num of splits + 1
