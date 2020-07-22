# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        inorder = self.inOrderNodes(root)
        dummy = curNode = TreeNode()

        for node in inorder:
            curNode.right = node
            curNode.left = None
            curNode = curNode.right
            
        return dummy.right
        
    def inOrderNodes(self, root, traversal=[]):
        if not root:
            return traversal
        
        traversal.append(root)
        self.inOrderNodes(root.left, traversal)
        self.inOrderNodes(root.right, traversal)
        
        return traversal
