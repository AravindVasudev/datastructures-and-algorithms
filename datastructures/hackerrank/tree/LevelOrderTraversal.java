/*
class Node 
   int data;
   Node left;
   Node right;
*/
void levelOrder(Node root) {
    Queue<Node> q = new LinkedList();
    
    q.add(root);
    while (!q.isEmpty()) {
        Node cur = q.remove();
        System.out.printf("%d ", cur.data);
        
        if (cur.left != null)  q.add(cur.left);
        if (cur.right != null) q.add(cur.right);
    }
}
