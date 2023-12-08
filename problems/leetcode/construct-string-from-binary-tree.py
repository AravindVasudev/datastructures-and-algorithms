# https://leetcode.com/problems/construct-string-from-binary-tree/
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
      if not root:
        return ""

      tree = str(root.val)
      if root.left or root.right:
        tree += f"({self.tree2str(root.left)})"

      if root.right:
        tree += f"({self.tree2str(root.right)})"

      return tree
