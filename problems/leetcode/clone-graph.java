// https://leetcode.com/problems/clone-graph/
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        return cloneGraph(node, new HashMap<Node, Node>());
    }
    
    private Node cloneGraph(Node node, Map<Node, Node> visited) {
        if (node == null) {
            return null;
        }

        if (visited.containsKey(node)) {
            return visited.get(node);
        }
        
        Node newNode = new Node(node.val);
        visited.put(node, newNode);
        
        for (Node connected : node.neighbors) {
            newNode.neighbors.add(cloneGraph(connected, visited));
        }
        
        return newNode;
    }
}

// Python
from typing import Optional, Mapping
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.clone(node, {})

    def clone(self, node: Optional['Node'], visited: Mapping[int, 'Node']) -> Optional['Node']:
        if not node:
            return None

        if node.val in visited:
            return visited[node.val]

        copy = visited[node.val] = Node(node.val)
        for neighbor in node.neighbors:
            copy.neighbors.append(self.clone(neighbor, visited))

        return copy
