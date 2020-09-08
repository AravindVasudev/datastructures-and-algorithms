// https://leetcode.com/problems/count-univalue-subtrees/
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
    class UnivalueNode {
        boolean isUnivalue;
        int univalueCount;
        
        UnivalueNode(boolean isUnivalue, int univalueCount) {
            this.isUnivalue = isUnivalue;
            this.univalueCount = univalueCount;
        }
    }
    
    public int countUnivalSubtrees(TreeNode root) {
        return computeUnivalueTrees(root).univalueCount;
    }
    
    private UnivalueNode computeUnivalueTrees(TreeNode root) {
        if (root == null) {
            return new UnivalueNode(true, 0);
        }       
        
        UnivalueNode left = computeUnivalueTrees(root.left);
        UnivalueNode right = computeUnivalueTrees(root.right);
        
        int count = left.univalueCount + right.univalueCount;
        boolean isCurrentUnivalue = true;
        if (root.left != null) {
            isCurrentUnivalue = left.isUnivalue && root.left.val == root.val;
        }
        
        if (root.right != null) {
            isCurrentUnivalue = isCurrentUnivalue && right.isUnivalue && root.right.val == root.val;
        }
        
        return new UnivalueNode(isCurrentUnivalue, count + (isCurrentUnivalue ? 1 : 0));
    }
}
