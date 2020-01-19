// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class FindElements {
    TreeNode root;
    public FindElements(TreeNode root) {
        this.root = root;
        findElements(root, 0);
    }

    private static void findElements(TreeNode root, int value) {
        if (root == null) {
            return;
        }

        root.val = value;

        if (root.left != null) {
            findElements(root.left, 2 * value + 1);
        }

        if (root.right != null) {
            findElements(root.right, 2 * value + 2);
        }
    }

    public boolean find(int target) {
        return find(root, target);
    }

    private boolean find(TreeNode root, int target) {
        if (root == null) {
            return false;
        }

        if (root.val == target) {
            return true;
        }

        return find(root.left, target) || find(root.right, target);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */
