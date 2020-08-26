//https://leetcode.com/problems/serialize-and-deserialize-bst/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.Arrays;

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder serialized = new StringBuilder();
        serialize(root, serialized);
        return serialized.toString();
    }
    
    private void serialize(TreeNode root, StringBuilder buffer) {
        if (root == null) {
            buffer.append("#,");
            return;
        }
        
        buffer.append(root.val).append(",");

        serialize(root.left, buffer);
        serialize(root.right, buffer);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Queue<String> q = new LinkedList<>(Arrays.asList(data.split(",")));
        return deserialize(q);
    }
    
    private TreeNode deserialize(Queue<String> q) {
        String current = q.poll();
        if (current.equals("#")) {
            return null;
        }
        
        TreeNode currentNode = new TreeNode(Integer.parseInt(current));
        currentNode.left = deserialize(q);
        currentNode.right = deserialize(q);
        
        return currentNode;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
