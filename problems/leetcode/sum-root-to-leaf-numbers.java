// https://leetcode.com/problems/sum-root-to-leaf-numbers/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumNumbers(TreeNode root) {
        return sumNumbers(root, 0);
    }
    
    private int sumNumbers(TreeNode root, int currentPath) {
        if (root == null) {
            return 0;
        }
        
        currentPath = (currentPath * 10) + root.val;
        
        if (root.left == null && root.right == null) {
            return currentPath;
        }
        
        return sumNumbers(root.left, currentPath) + sumNumbers(root.right, currentPath);
    }
}
