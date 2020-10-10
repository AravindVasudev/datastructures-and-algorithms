// https://leetcode.com/problems/maximum-average-subtree/
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
    public double maximumAverageSubtree(TreeNode root) {
      double[] result = new double[1];
      maximumAverageSubtree(root, result);
      
      return result[0];
    }
  
    private double[] maximumAverageSubtree(TreeNode root, double[] result) {
      if (root == null) {
        return new double[] {0, 0};
      }
      
      if (root.left == null && root.right == null) {
        result[0] = Math.max(result[0], root.val);        
        return new double[] {root.val, 1};
      }
      
      double[] left = maximumAverageSubtree(root.left, result);
      double[] right = maximumAverageSubtree(root.right, result);
      
      left[0] += right[0] + root.val;
      left[1] += right[1] + 1;
      
      result[0] = Math.max(result[0], left[0] / left[1]);
      return left;
    }
}
