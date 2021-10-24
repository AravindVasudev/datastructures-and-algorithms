# https://leetcode.com/problems/combination-sum-iv/
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def combinations(path=0):
            if path > target:
                return 0
    
            if path == target:
                return 1

            ways = 0
            for num in nums:
                ways += combinations(path + num)
                
            return ways
                
        return combinations()
