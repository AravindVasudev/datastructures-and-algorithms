import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Trie {
    class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>(26);
        boolean isCompleteWord;
    }

    private TrieNode root = new TrieNode();

    void insert(String[] keys) {
        for (String key : keys) {
            this.insert(key);
        }
    }

    void insert(String key) {
        TrieNode cur = root;
        for (int i = 0; i < key.length(); i++) {
            if (cur.children.get(key.charAt(i)) == null) {
                cur.children.put(key.charAt(i), new TrieNode());
            }

            cur = cur.children.get(key.charAt(i));
        }

        cur.isCompleteWord = true;
    }

    boolean contains(String key) {
        TrieNode cur = root;
        for (int i = 0; i < key.length(); i++) {
            if (cur.children.get(key.charAt(i)) == null) {
                return false;
            }

            cur = cur.children.get(key.charAt(i));
        }

        return cur.isCompleteWord;
    }

    List<String> autocomplete(String query) {
        TrieNode cur = root;
        for (int i = 0; i < query.length(); i++) {
            if (cur.children.get(query.charAt(i)) == null) {
                return null;
            }

            cur = cur.children.get(query.charAt(i));
        }

        return getCompletions(cur, query, new ArrayList<String>());
    }

    List<String> getCompletions(TrieNode node, String curString ,List<String> output) {
        if (node.isCompleteWord) {
            output.add(curString);
        }

        for (Map.Entry<Character, TrieNode> child : node.children.entrySet()) {
            if (child.getValue() == null) {
                continue;
            }

            getCompletions(child.getValue(), curString + child.getKey(), output);
        }

        return output;
    }
}

class Main {
    public static void main(String[] args) {
        Trie t = new Trie();

        t.insert(new String[]{"app", "apple", "application", "appreciate", "approval", "bat", "ball", "bang", "bad"});

        System.out.printf("application : %b\n", t.contains("application"));
        System.out.printf("bang : %b\n", t.contains("bang"));
        System.out.printf("ba : %b\n", t.contains("ba"));
        System.out.printf("appd : %b\n", t.contains("appd"));
        System.out.printf("cat : %b\n", t.contains("cat"));

        System.out.println(t.autocomplete("ap"));
        System.out.println(t.autocomplete("b"));
        System.out.println(t.autocomplete("c"));
    }
}