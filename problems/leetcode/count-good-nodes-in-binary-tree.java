// https://leetcode.com/problems/count-good-nodes-in-binary-tree/
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
    public int goodNodes(TreeNode root) {
        return goodNodes(root, Integer.MIN_VALUE);
    }
    
    private int goodNodes(TreeNode root, int max) {
        if (root == null) {
            return 0;
        }
        
        int count = (root.val >= max) ? 1 : 0;
        count += goodNodes(root.left, Math.max(root.val, max));
        count += goodNodes(root.right, Math.max(root.val, max));
        
        return count;
    }
}
