/* you only have to complete the function given below.  
Node is defined as  

class Node {
    int data;
    Node left;
    Node right;
}

*/

void preOrder(Node root) {
    if (root == null) return;
    
    System.out.printf("%d ", root.data);
    preOrder(root.left);
    preOrder(root.right);
}
