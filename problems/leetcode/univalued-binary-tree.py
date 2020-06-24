# https://leetcode.com/problems/univalued-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:        
        return (root is None) or self.recurValidate(root, root.val)
    
    def recurValidate(self, root: TreeNode, val: int):
        return (root is None) or \
            ((root.val == val) and \
             self.recurValidate(root.left, val) and \
             self.recurValidate(root.right, val))
