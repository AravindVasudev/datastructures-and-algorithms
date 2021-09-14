# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        
        sequence = 1
        maxSequence = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    sequence += 1
                else:
                    maxSequence = max(maxSequence, sequence)
                    sequence = 1
                
        return max(maxSequence, sequence)
      
# Efficient
