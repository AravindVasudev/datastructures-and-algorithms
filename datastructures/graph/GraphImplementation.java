import java.util.*;

public class GraphImplementation {
    List<Integer>[] graph;

    public GraphImplementation(int v) {
        graph = new List[v];

        for (int i = 0; i < v; i++) {
            graph[i] = new LinkedList<>();
        }
    }

    public void addEdge(int src, int dest) {
        graph[src].add(dest);
        graph[dest].add(src); 
    }

    @Override
    public String toString() {
        StringBuilder out = new StringBuilder();

        for (List<Integer> node : graph) {
            out.append("HEAD ");
            for (Integer adjecencyElement : node) {
                out.append(" -> ").append(adjecencyElement);
            }
            out.append("\n");
        }

        return out.toString();
    }

    public static void main(String[] args) {
        GraphImplementation graph = new GraphImplementation(5);

        graph.addEdge(2, 3);
        graph.addEdge(2, 1);
        graph.addEdge(3, 4);
        graph.addEdge(4, 0);

        System.out.println(graph);
    }
}