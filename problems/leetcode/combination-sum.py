# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curList = [], curSum = 0, start = 0):
            if curSum == target:
                result.append(list(curList))
                return
            
            if curSum > target:
                return
            
            for i in range(start, len(candidates)):
                curList.append(candidates[i])
                backtrack(curList, curSum + candidates[i], i)
                curList.pop()
        
        result = []
        backtrack()
        
        return result
