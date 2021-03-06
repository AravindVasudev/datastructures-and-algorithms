https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        modifiedIndex = 0
        for num in nums:
            if num != 0:
                nums[modifiedIndex] = num
                modifiedIndex += 1
                
        size = len(nums)
        while modifiedIndex < size:
            nums[modifiedIndex] = 0
            modifiedIndex += 1
 
############# ALTERNATE OPTIMAL SOLUTION #############

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        modifiedIndex = 0
        
        for i, cur in enumerate(nums):
            if cur != 0:
                nums[modifiedIndex], nums[i] = cur, nums[modifiedIndex]
                modifiedIndex += 1
