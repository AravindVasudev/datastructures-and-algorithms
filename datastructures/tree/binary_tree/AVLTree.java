class AVLTree<T extends Comparable<T>> {
    public class AVLTreeNode<T> {
        T data;
        int height;
        AVLTreeNode<T> left, right;

        AVLTreeNode() {}

        AVLTreeNode(T data) {
            this.data = data;
        }

        @Override
        public String toString() {
            StringBuilder out = new StringBuilder();

            toString(this, out);
            return out.toString();
        }

        private void toString(AVLTreeNode<T> node, StringBuilder out) {
            if (node == null) {
                return;
            }

            toString(node.left, out);
            out.append(node.data).append(" ");
            toString(node.right, out);
        }
    }

    private AVLTreeNode<T> root;

    public AVLTreeNode<T> getRoot() {
        return root;
    }

    public int getHeight(AVLTreeNode<T> node) {
        return node == null ? -1 : node.height;
    }

    private AVLTreeNode<T> rightRotate(AVLTreeNode<T> node) {
        AVLTreeNode<T> left = node.left;
        AVLTreeNode<T> leftRight = left.right;

        left.right = node;
        node.left = leftRight;

        node.height = Math.max(getHeight(node.left), getHeight(node.right)) + 1;
        left.height = Math.max(getHeight(left.left), getHeight(left.right)) + 1;

        return left;
    }

    private AVLTreeNode<T> leftRotate(AVLTreeNode<T> node) {
        AVLTreeNode<T> right = node.right;
        AVLTreeNode<T> rightLeft = right.left;

        right.left = node;
        node.right = rightLeft;

        node.height = Math.max(getHeight(node.left), getHeight(node.right)) + 1;
        right.height = Math.max(getHeight(right.left), getHeight(right.right)) + 1;

        return right;
    }

    private int getBalanceFactor(AVLTreeNode<T> node) {
        return node == null ? -1 : (getHeight(node.left) - getHeight(node.right));
    }

    public void insert(T data) {
        root = insert(root, data);
    }

    private AVLTreeNode<T> insert(AVLTreeNode<T> node, T data) {
        if (node == null) {
            return new AVLTreeNode<T>(data);
        }

        if (data.compareTo(node.data) < 0) {
            node.left = insert(node.left, data);
        } else if (data.compareTo(node.data) > 0) {
            node.right = insert(node.right, data);
        } else return node;

        node.height = Math.max(getHeight(node.left), getHeight(node.right)) + 1;

        int balance = getBalanceFactor(node);

        // LL
        if (balance > 1 && data.compareTo(node.left.data) < 0) {
            return rightRotate(node);
        }

        // RR
        if (balance < -1 && data.compareTo(node.right.data) > 0) {
            return leftRotate(node);
        }

        // LR
        if (balance > 1 && data.compareTo(node.left.data) > 0) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        // RL
        if (balance < -1 && data.compareTo(node.right.data) < 0) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        return node;
    }

    @Override
    public String toString() {
        return root.toString();
    }
}

class Main {
    public static void main(String[] args) {
        AVLTree<Integer> tree = new AVLTree<>();

        tree.insert(1);
        tree.insert(2);
        tree.insert(3);
        tree.insert(4);
        tree.insert(5);
        tree.insert(6);
        tree.insert(7);
        tree.insert(8);
        tree.insert(9);
        tree.insert(10);

        System.out.println(tree);
    }
}