# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.getInorderArray(root, [])
        
        
    def getInorderArray(self, root, traversal):
        if root is None:
            return traversal
        
        self.getInorderArray(root.left, traversal)
        traversal.append(root.val)
        self.getInorderArray(root.right, traversal)
        
        return traversal
