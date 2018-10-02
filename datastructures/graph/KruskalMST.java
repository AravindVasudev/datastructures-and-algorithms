import java.util.*;

public class KruskalMST {
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

    private class Node {
        Integer id;
        List<Edge> adjacency = new LinkedList<>();

        Node(Integer id) {
            this.id = id;
        }

        @Override
        public String toString() {
            return id.toString();
        }
    }

    private class Edge implements Comparable<Edge> {
        Node source, dest;
        int weight;

        Edge(Node source, Node dest, int weight) {
            this.source = source;
            this.dest = dest;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge edge) {
            return weight - edge.weight;
        }

        @Override
        public String toString() {
            return String.format("%s <--| %d |--> %s", source, weight, dest);
        }
    }

    Map<Integer, Node> vertices = new HashMap<>();
    List<Edge> edges = new ArrayList<>();

    KruskalMST addVertex(int id) {
        vertices.put(id, new Node(id));

        return this;
    }
    
    KruskalMST addEdge(int source, int dest, int weight) {
        return addEdge(getVertex(source), getVertex(dest), weight);
    }

    KruskalMST addEdge(Node source, Node dest, int weight) {
        Edge edge = new Edge(source, dest, weight);

        source.adjacency.add(edge);
        dest.adjacency.add(edge);

        edges.add(edge);

        return this;
    }

    Node getVertex(int id) {
        return vertices.get(id);
    }

    List<Edge> kruskalMST() {
        List<Edge> result = new ArrayList<>(vertices.size());
        DisjointSets ds = new DisjointSets(vertices.size());

        Collections.sort(edges);
        for (int i = 0; result.size() < vertices.size() - 1; i++) {
            final Edge curEdge = edges.get(i);

            if (!ds.find(curEdge.source.id, curEdge.dest.id)) {
                result.add(curEdge);

                ds.union(curEdge.source.id, curEdge.dest.id);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        KruskalMST graph = new KruskalMST();

        graph
            .addVertex(0)
            .addVertex(1)
            .addVertex(2)
            .addVertex(3);

        graph
            .addEdge(0, 1, 10)
            .addEdge(0, 2, 6)
            .addEdge(0, 3, 5)
            .addEdge(1, 3, 15)
            .addEdge(2, 3, 4);

            System.out.println(graph.kruskalMST());
    }
}