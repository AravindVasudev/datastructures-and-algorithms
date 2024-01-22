# https://leetcode.com/problems/nested-list-weight-sum/
class Solution:
    def depthSum(self, nestedList: List[NestedInteger], depth=1) -> int:
        if not nestedList:
            return 0

        total = 0
        for el in nestedList:
            if el.isInteger():
                total += el.getInteger() * depth
            else:
                total += self.depthSum(el.getList(), depth + 1)

        return total
