import java.util.*;

public class MST {
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

    MST addVertex(int id) {
        vertices.put(id, new Node(id));

        return this;
    }
    
    MST addEdge(int source, int dest, int weight) {
        return addEdge(getVertex(source), getVertex(dest), weight);
    }

    MST addEdge(Node source, Node dest, int weight) {
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

    List<Edge> kruskalMSTUsingSet() {
        List<Edge> result = new ArrayList<>(vertices.size());
        Set<Integer> visited = new HashSet<>(vertices.size());

        Collections.sort(edges);
        for (int i = 0; result.size() < vertices.size() - 1; i++) {
            final Edge curEdge = edges.get(i);

            if (visited.contains(curEdge.source.id) && visited.contains(curEdge.dest.id)) {
                continue;
            }

            result.add(curEdge);

            visited.add(curEdge.source.id);
            visited.add(curEdge.dest.id);
        }

        return result;
    }

    private class PrimNode implements Comparable<PrimNode> {
        Node node;
        int minPathWeight;

        PrimNode(Node node, int weight) {
            this.node = node;
            this.minPathWeight = weight;
        }

        PrimNode(Node node) {
            this(node, Integer.MAX_VALUE);
        }

        void setWeight(int weight) {
            minPathWeight = weight;
        }

        int getWeight() {
            return minPathWeight;
        }

        Node getNode() {
            return node;
        }

        @Override
        public int compareTo(PrimNode o) {
            return minPathWeight - o.minPathWeight;
        }
    }

    List<Edge> primMST() {
        PriorityQueue<PrimNode> pq = new PriorityQueue<>();
        Map<Node, PrimNode> nodeVsPrimNode = new HashMap<>();
        List<Edge> result = new ArrayList<>(vertices.size());
        Map<PrimNode, Edge> vertexToEdge = new HashMap<>();
        Set<PrimNode> visited = new HashSet<>();

        Iterator<Map.Entry<Integer, Node>> it = vertices.entrySet().iterator();

        Node node = it.next().getValue();
        PrimNode primNode = new PrimNode(node, 0);
        pq.add(primNode);
        nodeVsPrimNode.put(node, primNode);

        while (it.hasNext()) {
            node = it.next().getValue();
            primNode = new PrimNode(node);

            pq.add(primNode);
            nodeVsPrimNode.put(node, primNode);
        }

        while (!pq.isEmpty()) {
            PrimNode curNode = pq.poll();

            if (visited.contains(curNode)) {
                continue;
            }

            Edge minEdge = vertexToEdge.get(curNode);
            if (minEdge != null) {
                result.add(minEdge);
                visited.add(curNode);
            }

            for (Edge curEdge : curNode.node.adjacency) {
                Node curEdgeNode = curNode.node == curEdge.source ? curEdge.dest : curEdge.source;
                PrimNode curEdgePrimNode = nodeVsPrimNode.get(curEdgeNode);

                if (curEdgePrimNode != null && curEdgePrimNode.getWeight() > curEdge.weight) {
                    pq.remove(curEdgePrimNode);
                    curEdgePrimNode.setWeight(curEdge.weight);
                    pq.add(curEdgePrimNode);

                    vertexToEdge.put(curEdgePrimNode, curEdge);
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        MST graph = new MST();

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

        System.out.println("Kruskal: " + graph.kruskalMST());
        System.out.println("Kruskal without DisjointSets: " + graph.kruskalMSTUsingSet());
        System.out.println("Prim: " + graph.primMST());
    }
}