import java.util.*;

public class UnweightedShortestPath {
    private class Node {
        Integer id;
        List<Integer> adjecency = new LinkedList<>();

        Node(Integer id) {
            this.id = id;
        }
    }

    Map<Integer, Node> vertices = new HashMap<>();

    public UnweightedShortestPath addEdge(Integer src, Integer dest) {
        vertices.get(src).adjecency.add(dest);
        vertices.get(dest).adjecency.add(src);

        return this;
    }

    public UnweightedShortestPath addVertex(Integer id) {
        vertices.put(id, new Node(id));

        return this;
    }

    public List<Integer> shortestPath(Integer src, Integer dest) {
        Queue<Node> q = new LinkedList<>();
        int[] path = new int[vertices.size()];

        int[] distance = new int[vertices.size()];
        Arrays.fill(distance, -1);
        distance[src] = 0;
        q.add(vertices.get(src));

        parent:
        while (!q.isEmpty()) {
            Node curNode = q.poll();
            for (Integer node : curNode.adjecency) {
                if (distance[node] == -1) {
                    q.add(vertices.get(node));
                    distance[node] = distance[curNode.id] + 1;

                    path[node] = curNode.id;

                    if (node.equals(dest)) {
                        break parent;
                    }
                }
            }
        }

        List<Integer> result = new ArrayList<>(vertices.size());
        Integer crawl = dest;
        while (crawl != src) {
            result.add(crawl);
            crawl = path[crawl];
        }

        result.add(src);
        Collections.reverse(result);

        return result;
    }

    public static void main(String[] args) {
        UnweightedShortestPath graph = new UnweightedShortestPath();

        for (int i = 0; i < 8; i++) {
            graph.addVertex(i);
        }

        graph
            .addEdge(0, 1)
            .addEdge(0, 3)
            .addEdge(1, 2)
            .addEdge(3, 4)
            .addEdge(3, 7)
            .addEdge(4, 5)
            .addEdge(4, 6)
            .addEdge(4, 7)
            .addEdge(5, 6)
            .addEdge(6, 7);

        System.out.println("Shortest Path(0, 7): " + graph.shortestPath(0, 7));
        System.out.println("Shortest Path(0, 4): " + graph.shortestPath(0, 4));
        System.out.println("Shortest Path(0, 1): " + graph.shortestPath(0, 1));
        System.out.println("Shortest Path(2, 6): " + graph.shortestPath(2, 6));
    }
}
