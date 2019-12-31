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
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Queue<TreeNode> q = new LinkedList<>();

        if (root1 != null) q.add(root1);
        if (root2 != null) q.add(root2);
        while (!q.isEmpty()) {
            TreeNode cur = q.poll();

            if (cur.left != null) {
                q.add(cur.left);
            }

            if (cur.right != null) {
                q.add(cur.right);
            }

            pq.add(cur.val);
        }

        List<Integer> list = new ArrayList<>(pq.size());
        while (!pq.isEmpty()) {
            list.add(pq.poll());
        }

        return list;
    }
}
