# https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []

        for x in nums:
            if nums[abs(x) - 1] < 0:
                result.append(abs(x))
                
            nums[abs(x) - 1] *= -1;
       
        return result
