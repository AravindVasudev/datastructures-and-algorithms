import java.util.*;

public class NaughtyStudents {
    public Map<String, String> parent;

    public NaughtyStudents() {
        parent = new HashMap<>();
    }

    public void makeSet(String element) {
        if (!parent.containsKey(element)) {
            parent.put(element, element);
        }
    }

    public void makeSet(String[] elements) {
        makeSet(elements[0]);
        for (int i = 1; i < elements.length; i++) {
            if (!parent.containsKey(elements[i])) {
                parent.put(elements[i], elements[0]);
            }
        }
    }

    public String root(String node) {
        String curNode = node;
        while (!curNode.equals(parent.get(curNode))) {
            curNode = parent.get(curNode);
        }

        parent.put(node, curNode);
        return curNode;
    }

    public void union(String nodeA, String nodeB) {
        parent.put(root(nodeA), root(nodeB));
    }

    public boolean find(String nodeA, String nodeB) {
        return root(nodeA).equals(root(nodeB));
    }

    public List<String> getSet(String node) {
        List<String> out = new ArrayList<>();
        String rootNode = root(node);

        Iterator it = parent.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<String, String> cur = (Map.Entry)it.next();

            if (root(cur.getValue()).equals(rootNode)) {
                out.add(cur.getKey());
            }
        }

        return out;
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        NaughtyStudents ds = new NaughtyStudents();

        String[] punishmentList = kb.next().split(",");
        ds.makeSet(punishmentList);

        int iterationCount = kb.nextInt();
        String[] relation;
        for (int i = 0; i < iterationCount; i++) {
            relation = kb.next().split("->");

            ds.makeSet(relation[0]);
            ds.makeSet(relation[1]);

            ds.union(relation[0], relation[1]);
        }

        System.out.println(ds.getSet(punishmentList[0]));
    }
}
