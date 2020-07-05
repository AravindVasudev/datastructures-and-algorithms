# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.generateTree(nums, 0, len(nums) - 1)
        
    def generateTree(self, nums, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        curNode = TreeNode(nums[mid])
        curNode.left = self.generateTree(nums, left, mid - 1)
        curNode.right = self.generateTree(nums, mid + 1, right)
        
        return curNode
