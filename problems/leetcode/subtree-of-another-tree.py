# https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.compare(s, t):
            return True
        
        if not s:
            return False
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
        
    def compare(self, s, t):
        if not (s or t):
            return True
        
        if not (s and t):
            return False
        
        return s.val == t.val and \
            self.compare(s.left, t.left) and \
            self.compare(s.right, t.right)
