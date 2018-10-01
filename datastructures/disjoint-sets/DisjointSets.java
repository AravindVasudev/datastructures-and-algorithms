public class DisjointSets {
    int[] parent;

    DisjointSets(int size) {
        parent = new int[size];

        for (int i = 0; i < size; i++) {
            parent[i] = i;
        }
    }

    int root(int node) {
        int curNode = node;
        while (parent[node] != node) {
            node = parent[node];
        }

        parent[curNode] = node; // path compression
        return node;
    }

    void union(int nodeA, int nodeB) {
        parent[root(nodeA)] = root(nodeB);
    }

    boolean find(int nodeA, int nodeB) {
        return root(nodeA) == root(nodeB);
    }

    public static void main(String[] args) {
        DisjointSets ds = new DisjointSets(10);

        /*
            0 3 4 8 7 9
            5 6
         */

        ds.union(0, 3);
        ds.union(3, 4);
        ds.union(5, 6);
        ds.union(7, 9);
        ds.union(8, 4);
        ds.union(4, 9);

        System.out.println("find(0, 9): " + ds.find(0, 9));
        System.out.println("find(5, 6): " + ds.find(5, 6));
        System.out.println("find(5, 3): " + ds.find(5, 3));
    }
}
