# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.sumAllPaths(root)
    
    def sumAllPaths(self, root, path=[]):       
        if (root.left is None) and (root.right is None):       
            power = 1
            num = root.val
            for i in range(len(path) - 1, -1, -1):
                num += path[i] * (2 ** power)
                power += 1
                
            return int(num)

        path.append(root.val)
        total = 0
        if root.left is not None:
            total = self.sumAllPaths(root.left, path)
        
        if root.right is not None:
            total += self.sumAllPaths(root.right, path)

        path.pop()
        
        return total
