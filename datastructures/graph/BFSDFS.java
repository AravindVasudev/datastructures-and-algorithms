import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BFSDFS {
    private List<Integer>[] graph;

    public BFSDFS(int v) {
        graph = new List[v];

        for (int i = 0; i < v; i++) {
            graph[i] = new LinkedList<>();
        }
    }

    public BFSDFS addEdge(int source, int dest) {
        graph[source].add(dest);
        return this;
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

    public String BFS() {
        boolean[] visited = new boolean[graph.length];
        Queue<Integer> q = new LinkedList<>();
        StringBuilder out = new StringBuilder();

        q.add(0);
        visited[0] = true;

        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int curNode : graph[cur]) {
                if (!visited[curNode]) {
                    q.add(curNode);
                    visited[curNode] = true;
                }
            }

            out.append(cur).append(" ");
        }

        return out.toString();
    }

    public void DFS(int node, boolean[] visited, StringBuilder out) {
        visited[node] = true;
        out.append(node).append(" ");

        for (int adjNode : graph[node]) {
            if (!visited[adjNode]) {
                DFS(adjNode, visited, out);
            }
        }
    }

    public String DFS() {
        boolean[] visited = new boolean[graph.length];
        StringBuilder out = new StringBuilder();
        DFS(0, visited, out);

        return out.toString();
    }

    public static void main(String[] args) {
        BFSDFS graph = new BFSDFS(5);

        graph
                .addEdge(0, 1)
                .addEdge(1, 4)
                .addEdge(1, 2)
                .addEdge(2, 3)
                .addEdge(3, 4)
                .addEdge(1, 3)
                .addEdge(4, 1);

        System.out.println(graph);
        System.out.println("BFS: " + graph.BFS());
        System.out.println("DFS: " + graph.DFS());
    }
}
