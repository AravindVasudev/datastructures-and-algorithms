# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.calculateEvenGrandChildSum(root)
        
    def calculateEvenGrandChildSum(self, root, parent=None, grandParent=None):
        if not root:
            return 0
        
        curVal = root.val if grandParent and (grandParent.val % 2 == 0) else 0
            
        return curVal + self.calculateEvenGrandChildSum(root.left, root, parent) +\
                self.calculateEvenGrandChildSum(root.right, root, parent)
