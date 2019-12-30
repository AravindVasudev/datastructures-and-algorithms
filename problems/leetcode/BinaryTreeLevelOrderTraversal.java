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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> output = new ArrayList<>();

        if (root == null) {
            return output;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int levelSize = q.size();
            List<Integer> level = new ArrayList<>(levelSize);
            while (levelSize-- > 0) {
                TreeNode cur = q.poll();

                if (cur.left != null) q.add(cur.left);
                if (cur.right != null) q.add(cur.right);

                level.add(cur.val);
            }

            output.add(level);
        }

        return output;
    }
}
