/*
class Node 
   int data;
   Node left;
   Node right;
*/
void topView(Node root) {
    topView(root.left, true);
    System.out.printf("%d ", root.data);
    topView(root.right, false);
}

void topView(Node root, boolean isLeft) {
    if (root == null) return;
    
    if (isLeft) {
        topView(root.left, isLeft);
        System.out.printf("%d ", root.data);
    } else {
        System.out.printf("%d ", root.data);
        topView(root.right, isLeft);
    }
}
