import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class KruskalMST {
    final int V, E;
    Edge[] edges;

    private class Edge implements Comparable<Edge> {
        int src, dest, weight;

        @Override
        public int compareTo(Edge edge) {
            return weight - edge.weight;
        }

        @Override
        public String toString() {
            return String.format("%d <--| %d |--> %d", src, weight, dest);
        }
    }

    private class DisjointSets {
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
    }

    public KruskalMST(int V, int E) {
        this.V = V;
        this.E = E;

        edges = new Edge[E];
        for (int i = 0; i < E; i++) {
            edges[i] = new Edge();
        }
    }

    public List<Edge> kruskalMST() {
        List<Edge> result = new ArrayList<>(V);
        DisjointSets ds = new DisjointSets(V);

        Arrays.sort(edges);
        for (int i = 0; result.size() < V - 1; i++) {
            final Edge curEdge = edges[i];

            if (!ds.find(curEdge.src, curEdge.dest)) {
                result.add(curEdge);

                ds.union(curEdge.src, curEdge.dest);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        KruskalMST graph = new KruskalMST(4, 5);

        graph.edges[0].src = 0;
        graph.edges[0].dest = 1;
        graph.edges[0].weight = 10;

        graph.edges[1].src = 0;
        graph.edges[1].dest = 2;
        graph.edges[1].weight = 6;

        graph.edges[2].src = 0;
        graph.edges[2].dest = 3;
        graph.edges[2].weight = 5;

        graph.edges[3].src = 1;
        graph.edges[3].dest = 3;
        graph.edges[3].weight = 15;

        graph.edges[4].src = 2;
        graph.edges[4].dest = 3;
        graph.edges[4].weight = 4;

        System.out.println(graph.kruskalMST());
    }
}
