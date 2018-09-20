import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode<T> {
    T data;
    TreeNode<T> left;
    TreeNode<T> right;

    public TreeNode(T data) {
        this.data = data;
    }

    public int getHeight() {
        return getHeight(this);
    }

    private int getHeight(TreeNode<T> tree) {
        return tree == null ? 0 : Math.max(getHeight(tree.left), getHeight(tree.right)) + 1;
    }

    public T getDeepestNode() {
        Queue<TreeNode> q = new LinkedList<>();
        TreeNode<T> cur = null;

        q.add(this);
        while (!q.isEmpty()) {
            cur = q.poll();

            if (cur.left != null) {
                q.add(cur.left);
            }

            if (cur.right != null) {
                q.add(cur.right);
            }
        }

        return cur.data;
    }

    public int numLeaves() {
        return numLeaves(this);
    }

    private int numLeaves(TreeNode<T> tree) {
        if (tree == null) {
            return 0;
        }

        if (tree.left == null && tree.right == null) {
            return 1;
        }

        return numLeaves(tree.left) + numLeaves(tree.right);
    }

    @Override
    public boolean equals(Object obj) {
        return equals(this, (TreeNode<T>) obj);
    }

    private boolean equals(TreeNode<T> tree1, TreeNode<T> tree2) {
        if (tree1 == null && tree2 == null) {
            return true;
        }

        if (tree1 == null || tree2 == null) {
            return false;
        }

        return tree1.data == tree2.data && equals(tree1.left, tree2.left) && equals(tree1.right, tree2.right);
    }

    @Override
    public String toString() {
        StringBuilder out = new StringBuilder();

        toString(this, out);
        return out.toString();
    }

    private void toString(TreeNode<T> tree, StringBuilder out) {
        if (tree == null) {
            out.append("NULL ");
            return;
        }

        out.append(tree.data).append(" ");

        toString(tree.left, out);
        toString(tree.right, out);
    }

    public int getDiameter() {
        return getDiameter(this, Integer.MIN_VALUE);
    }

    private int getDiameter(TreeNode<T> tree, int curDiameter) {
        if (tree == null) {
            return 0;
        }

        int leftDiameter = getDiameter(tree.left, curDiameter);
        int rightDiameter = getDiameter(tree.right, curDiameter);

        curDiameter = Math.max(curDiameter, leftDiameter + rightDiameter);

        return Math.max(leftDiameter, rightDiameter) + 1;
    }

    public List<String> rootToLeaves() {
        return rootToLeaves(this, new ArrayList<>(), new ArrayList<>());
    }

    private List<String> rootToLeaves(TreeNode<T> tree, List<String> cur, List<String> list) {
        if (tree == null) {
            return null;
        }

        cur.add(tree.data.toString());
        if (tree.left == null && tree.right == null) {
            list.add(cur.toString());
        }

        rootToLeaves(tree.left, cur, list);
        rootToLeaves(tree.right, cur, list);

        cur.remove(cur.size() - 1);

        return list;
    }

    public void reflect() {
        reflect(this);
    }

    private void reflect(TreeNode<T> tree) {
        if (tree == null) {
            return;
        }

        TreeNode<T> temp = tree.left;
        tree.left = tree.right;
        tree.right = temp;

        reflect(tree.left);
        reflect(tree.right);
    }

    public boolean isMirror(TreeNode<T> tree) {
        return isMirror(this, tree);
    }

    private boolean isMirror(TreeNode<T> tree1, TreeNode<T> tree2) {
        if (tree1 == null && tree2 == null) {
            return true;
        }

        if ((tree1 == null || tree2 == null) || !tree1.data.equals(tree2.data)) {
            return false;
        }

        return isMirror(tree1.left, tree2.right) && isMirror(tree1.right, tree2.left);
    }
}

public class BinaryTree {
    public static int maxLevelSum(TreeNode<Integer> tree) {
        if (tree == null) {
            return 0;
        }

        Queue<TreeNode<Integer>> q = new LinkedList<>();
        int curSum = 0, maxSum = 0;

        q.add(tree);
        while (!q.isEmpty()) {
            int levelSize = q.size();
            while (levelSize-- > 0) {
                TreeNode<Integer> node = q.poll();

                curSum += node.data;

                if (node.left != null) {
                    q.add(node.left);
                }

                if (node.right != null) {
                    q.add(node.right);
                }
            }

            maxSum = Math.max(maxSum, curSum);
            curSum = 0;
        }

        return maxSum;
    }

    public static boolean hasPathSum(TreeNode<Integer> tree, int sum) {
        if (tree == null) {
            return sum == 0;
        }

        final Integer remainingSum = sum - tree.data;
        return hasPathSum(tree.left, remainingSum) || hasPathSum(tree.right, remainingSum);
    }

    public static Integer treeSum(TreeNode<Integer> tree) {
        return tree == null ? 0 : treeSum(tree.left) + treeSum(tree.right) + tree.data;
    }

    public static void main(String[] args) {
        /*
                     1
                    / \
                   2   6
                  / \ /
                 3  4 7
                /
               5
         */
        TreeNode<Integer> tree = new TreeNode<>(1);

        tree.left = new TreeNode<>(2);
        tree.left.left = new TreeNode<>(3);
        tree.left.right = new TreeNode<>(4);
        tree.left.left.left = new TreeNode<>(5);

        tree.right = new TreeNode<>(6);
        tree.right.left = new TreeNode<>(7);

        System.out.println("Preorder: " + tree);
        System.out.println("Height: " + tree.getHeight());
        System.out.println("Deepest Node: " + tree.getDeepestNode());
        System.out.println("Number of Leaves: " + tree.numLeaves());

        // Duplicate Tree
        TreeNode<Integer> duplicateTree = new TreeNode<>(1);

        duplicateTree.left = new TreeNode<>(2);
        duplicateTree.left.left = new TreeNode<>(3);
        duplicateTree.left.right = new TreeNode<>(4);
        duplicateTree.left.left.left = new TreeNode<>(5);

        duplicateTree.right = new TreeNode<>(6);
        duplicateTree.right.left = new TreeNode<>(7);

        // Different Tree
        TreeNode<Integer> differentTree = new TreeNode<>(1);

        differentTree.left = new TreeNode<>(2);
        differentTree.left.left = new TreeNode<>(3);
        differentTree.left.right = new TreeNode<>(4);
        differentTree.left.left.left = new TreeNode<>(5);

        differentTree.right = new TreeNode<>(6);


        System.out.println("DuplicateTree: " + duplicateTree);
        System.out.println("DifferentTree: " + differentTree);

        System.out.println("Tree && DuplicateTree: " + tree.equals(duplicateTree));
        System.out.println("Tree && DifferentTree: " + tree.equals(differentTree));

        System.out.println("Diameter: " + tree.getDiameter());

        System.out.println("Tree's max level sum: " + maxLevelSum(tree));

        System.out.println("rootToLeaves: " + tree.rootToLeaves());

        System.out.println("hasPathSum(14): " + hasPathSum(tree, 14));
        System.out.println("hasPathSum(6): " + hasPathSum(tree, 6));
        System.out.println("hasPathSum(15): " + hasPathSum(tree, 15));

        System.out.println("TreeSum: " + treeSum(tree));

        duplicateTree.reflect();
        System.out.printf("Tree: %s | Mirror: %s\n", tree, duplicateTree);

        System.out.println("isMirror(tree, tree): " + tree.isMirror(tree));
        System.out.println("isMirror(tree, duplicate): " + tree.isMirror(duplicateTree));
    }
}
