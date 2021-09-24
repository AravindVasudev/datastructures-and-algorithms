# https://leetcode.com/problems/inorder-successor-in-bst/
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            # Smallest in right
            smallest = p.right
            while smallest.left:
                smallest = smallest.left
                
            return smallest
        else:
            leftParent = self.getLeftParent(root, p)
            return leftParent if leftParent != p else None
        
    def getLeftParent(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        if root == p:
            return p
        
        if root.val > p.val:
            left = self.getLeftParent(root.left, p)
            if left:
                return root if left == p else left
        
        return self.getLeftParent(root.right, p)

        
