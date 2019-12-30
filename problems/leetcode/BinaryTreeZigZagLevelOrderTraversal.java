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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> output = new ArrayList<>();

        if (root == null) {
            return output;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        boolean isEvenLevel = false;
        while (!q.isEmpty()) {
            int levelSize = q.size();
            List<Integer> level = new ArrayList<>(levelSize);

            while (levelSize-- > 0) {
                TreeNode cur = q.poll();

                if (cur.left != null) q.add(cur.left);
                if (cur.right != null) q.add(cur.right);

                level.add(cur.val);
            }

            if (isEvenLevel) {
                Collections.reverse(level);
            }

            output.add(level);
            isEvenLevel = !isEvenLevel;
        }

        return output;
    }
}
