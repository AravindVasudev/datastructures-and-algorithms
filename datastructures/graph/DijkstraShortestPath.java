import java.time.temporal.ChronoUnit;
import java.util.*;

public class DijkstraShortestPath {
    private class Node {
        Integer id;
        List<Edge> adjecency = new LinkedList<>();

        Node(Integer id) {
            this.id = id;
        }

        Integer getId() {
            return id;
        }

        List<Edge> getAdjecency() {
            return adjecency;
        }

        @Override
        public String toString() {
            return id.toString();
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }

            return id.equals(((Node) o).id);
        }
    }

    private class Edge implements Comparable<Edge> {
        Node src, dest;
        int weight;

        Edge(Node src, Node dest, int weight) {
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge edge) {
            return weight - edge.weight;
        }

        @Override
        public String toString() {
            return String.format("%s <--| %d |--> %s", src, weight, dest);
        }
    }

    Map<Integer, Node> vertices = new HashMap<>();
    List<Edge> edges = new ArrayList<>();

    DijkstraShortestPath addVertex(Integer id) {
        vertices.put(id, new Node(id));

        return this;
    }

    DijkstraShortestPath addEdge(int source, int dest, int weight) {
        return addEdge(getVertex(source), getVertex(dest), weight);
    }

    DijkstraShortestPath addEdge(Node source, Node dest, int weight) {
        Edge edge = new Edge(source, dest, weight);

        source.getAdjecency().add(edge);
        dest.getAdjecency().add(edge);

        edges.add(edge);

        return this;
    }

    Node getVertex(int id) {
        return vertices.get(id);
    }

    Node getAdjecentVertexForEdge(Edge edge, Node source) {
        return edge.src == source ? edge.dest : edge.src;
    }

    public List<Node> shortestPath(Integer start, Integer end) {
        return shortestPath(getVertex(start), getVertex(end));
    }

    private class DijkstraNode implements Comparable<DijkstraNode> {
        Node node;
        int distance = Integer.MAX_VALUE;

        DijkstraNode(Node node, int distance) {
            this.node = node;
            this.distance = distance;
        }

        public Node getNode() {
            return node;
        }

        public void setNode(Node node) {
            this.node = node;
        }

        public int getDistance() {
            return distance;
        }

        public void setDistance(int distance) {
            this.distance = distance;
        }

        @Override
        public int compareTo(DijkstraNode dijkstraNode) {
            return distance - dijkstraNode.distance;
        }

//        @Override
//        public int hashCode() {
//            return node.hashCode();
//        }
//
//        @Override
//        public boolean equals(Object o) {
//            if (this == o) {
//                return true;
//            }
//
//            return node.equals(((DijkstraNode) o).node);
//        }
    }

    public List<Node> shortestPath(Node start, Node end) {
        Map<Node, Node> prevMap = new HashMap<>();
        Map<Node, Integer> distance = new HashMap<>();
        Map<Node, DijkstraNode> nodeVsDijkstraNode = new HashMap<>();
        Set<Node> visited = new HashSet<>();
        PriorityQueue<DijkstraNode> pq = new PriorityQueue<>();

        DijkstraNode dn = new DijkstraNode(start, 0);
        pq.add(dn);
        nodeVsDijkstraNode.put(start, dn);

        for (Map.Entry<Integer, Node> entry : vertices.entrySet()) {
            if (!entry.getValue().equals(start)) {
                dn = new DijkstraNode(entry.getValue(), Integer.MAX_VALUE);

                pq.add(dn);
                nodeVsDijkstraNode.put(entry.getValue(), dn);
            }
        }

        while (!pq.isEmpty()) {
            DijkstraNode curNode = pq.poll();

            distance.put(curNode.getNode(), curNode.getDistance());

            if (curNode.node == end) {
                break;
            }

            for (Edge curEdge : curNode.getNode().getAdjecency()) {
                Node adjecentNode = getAdjecentVertexForEdge(curEdge, curNode.getNode());
                DijkstraNode adjecentDijkstraNode = nodeVsDijkstraNode.get(adjecentNode);

                if (!pq.contains(adjecentDijkstraNode)) {
                    continue;
                }

                int newDistance = distance.get(curNode.node) + curEdge.weight;

                if (adjecentDijkstraNode.distance > newDistance) {
                        pq.remove(adjecentDijkstraNode);
                        adjecentDijkstraNode.distance = newDistance;
                        pq.add(adjecentDijkstraNode);
                        prevMap.put(adjecentNode, curNode.node);
                }
            }
        }

        List<Node> result = new ArrayList<>(vertices.size());
        Node crawl = end;
        while (crawl != null) {
            result.add(crawl);
            crawl = prevMap.get(crawl);
        }

        Collections.reverse(result);
        return result;
    }

    public static void main(String[] args) {
        DijkstraShortestPath graph = new DijkstraShortestPath();


        graph
                .addVertex(0)
                .addVertex(1)
                .addVertex(2)
                .addVertex(3);

        graph
                .addEdge(0, 1, 10)
                .addEdge(0, 2, 6)
                .addEdge(0, 3, 30)
                .addEdge(1, 3, 15)
                .addEdge(2, 3, 4);

        System.out.println("ShortestPath(1, 2): " + graph.shortestPath(1, 2));
        System.out.println("ShortestPath(0, 3): " + graph.shortestPath(0, 3));
        System.out.println("ShortestPath(0, 2): " + graph.shortestPath(0, 2));
        System.out.println("ShortestPath(0, 0): " + graph.shortestPath(0, 0));
    }
}
