// https://leetcode.com/problems/merge-two-binary-trees/
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
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) {
            return null;
        }

        TreeNode node = new TreeNode();
        
        if (t1 != null && t2 == null) {
            node.val = t1.val;
            node.left = mergeTrees(t1.left, null);
            node.right = mergeTrees(t1.right, null);
        } else if (t1 == null && t2 != null) {
            node.val = t2.val;
            node.left = mergeTrees(null, t2.left);
            node.right = mergeTrees(null, t2.right);
        } else {
            node.val = t1.val + t2.val;
            node.left = mergeTrees(t1.left, t2.left);
            node.right = mergeTrees(t1.right, t2.right); 
        }

        return node;
    }
}
