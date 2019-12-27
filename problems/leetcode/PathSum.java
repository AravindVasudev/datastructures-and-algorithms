/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        return root == null ? false : hasPathSum(root, sum, 0);
    }
    
    public boolean hasPathSum(TreeNode root, int sum, int curSum) {
        curSum += root.val;
        if (root.left == null && root.right == null) {
            return  (curSum == sum);
        }
        
        boolean left = root.left != null ? hasPathSum(root.left, sum, curSum) : false;
        boolean right = root.right != null ? hasPathSum(root.right, sum, curSum) : false;
        
        return left || right;
    }
}