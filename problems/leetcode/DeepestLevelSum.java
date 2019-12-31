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
    public int deepestLeavesSum(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();

        q.add(root);
        int curLevelSum = 0;
        while (!q.isEmpty()) {
            int levelSize = q.size();
            curLevelSum = 0;

            while (levelSize-- > 0) {
                TreeNode cur = q.poll();

                if (cur.left != null) q.add(cur.left);
                if (cur.right != null) q.add(cur.right);

                curLevelSum += cur.val;
            }
        }

        return curLevelSum;
    }
}
