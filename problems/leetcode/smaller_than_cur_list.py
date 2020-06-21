# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallList = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                count += 1 if nums[j] < nums[i] else 0
                
            smallList.append(count)
            
        return smallList
