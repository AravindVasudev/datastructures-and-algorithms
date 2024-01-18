# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If the searched node is found, return.
        if root == p or root == q:
            return root

        # Else look in both left and right subtree
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right return a node, it means
        # that both of them have one node, hence root is
        # the parent.
        if left and right:
            return root

        # If only one returned, it should be the LCA
        # of both the nodes. 
        return left or right
