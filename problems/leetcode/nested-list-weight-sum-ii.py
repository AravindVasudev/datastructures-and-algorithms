# https://leetcode.com/problems/nested-list-weight-sum-ii/
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        levelSum = defaultdict(int)
        maxDepth = self.dfs(nestedList, 1, levelSum)
        
        weightedSum = 0
        for level, total in levelSum.items():
            weightedSum += total * (maxDepth - level + 1)

        return weightedSum


    def dfs(self, nestedList: List[NestedInteger], level: int, levelSum: Dict[int, int]) -> int:
        maxDepth = 1
        for element in nestedList:
            if element.isInteger():
                levelSum[level] += element.getInteger()
            else:
                maxDepth = max(maxDepth, self.dfs(element.getList(), level + 1, levelSum) + 1)

        return maxDepth
