// https://www.hackerrank.com/contests/quora-haqathon/challenges/ontology
import java.util.*;

public class Ontology {
    static class Topic {
        String topic;
        List<Topic> desendents = new ArrayList<>();
        List<String> questions = new ArrayList<>();

        Topic(String topic) {
            this.topic = topic;
        }
    }

    private static Topic generateTree(Stack<String> treeNodes, Map<String, Topic> topicMap) {
        Topic newNode = new Topic(treeNodes.pop());
        topicMap.put(newNode.topic, newNode);

        if (!treeNodes.empty() && treeNodes.peek().equals("(")) {
            treeNodes.pop(); // remove (

            while (!treeNodes.peek().equals(")")) {
                newNode.desendents.add(generateTree(treeNodes, topicMap));
            }

            treeNodes.pop(); // remove )
        }

        return newNode;
    }

    private static int searchCount(Topic topic, String query) {
        int curCount = 0;
        for (int i = 0; i < topic.questions.size(); i++) {
            if (topic.questions.get(i).startsWith(query)) {
                curCount++;
            }
        }

        for (int i = 0; i < topic.desendents.size(); i++) {
            curCount += searchCount(topic.desendents.get(i), query);
        }

        return curCount;
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        // Tree
        int N = kb.nextInt(); kb.nextLine();
        String treeString = kb.nextLine();

        Stack<String> nodeStack = new Stack<>();
        String[] nodesStr = treeString.split(" ");

        for (int i = nodesStr.length - 1; i >= 0; i--) {
            nodeStack.push(nodesStr[i]);
        }

        Map<String, Topic> topicMap = new HashMap<>();
        Topic tree = generateTree(nodeStack, topicMap);

        // Questions
        int M = kb.nextInt(); kb.nextLine();
        for (int i = 0; i < M; i++) {
            String[] questionArr = kb.nextLine().split(":", 2);
            topicMap.get(questionArr[0]).questions.add(questionArr[1].trim());
        }

        // Queries
        int K = kb.nextInt(); kb.nextLine();
        while (K-- > 0) {
            String[] queryArr = kb.nextLine().split(" ", 2);
            Topic topic = topicMap.get(queryArr[0]);

            System.out.println(searchCount(topic, queryArr[1]));
        }
    }
}
