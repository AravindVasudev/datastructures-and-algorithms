# https://leetcode.com/problems/sum-root-to-leaf-numbers/
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def total(root, path):
            if not root:
                return 0
            
            if not (root.left or root.right):
                path += str(root.val)
                return int(path)

            path += str(root.val)
            return total(root.left, path) + total(root.right, path)

        return total(root, "")
