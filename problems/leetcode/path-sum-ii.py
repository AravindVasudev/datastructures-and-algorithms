# https://leetcode.com/problems/path-sum-ii/
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        if (not (root.left or root.right)) and (targetSum == root.val):
            return [[root.val]]

        result = self.pathSum(root.left, targetSum - root.val) + \
            self.pathSum(root.right, targetSum - root.val)

        return [[root.val] + r for r in result]
