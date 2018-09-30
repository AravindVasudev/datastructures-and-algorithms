import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class EdgeExistence {
    private List<Integer>[] graph;

    public EdgeExistence(int n) {
        graph = new List[n];

        for (int i = 0; i < n; i++) {
            graph[i] = new LinkedList<>();
        }
    }

    public void addEdge(int source, int dest) {
        graph[source].add(dest);
        graph[dest].add(source);
    }

    public boolean doesEdgeExist(int source, int dest) {
        return graph[source].contains(dest);
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        int n = kb.nextInt();
        int m = kb.nextInt();

        EdgeExistence graph = new EdgeExistence(n);
        for (int i = 0; i < m; i++) {
            graph.addEdge(kb.nextInt(), kb.nextInt());
        }

        int q = kb.nextInt();
        for (int i = 0; i < q; i++) {
            System.out.println(graph.doesEdgeExist(kb.nextInt(), kb.nextInt()) ? "YES" : "NO");
        }
    }
}
