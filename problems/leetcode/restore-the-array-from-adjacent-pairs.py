"""
Prereq:
=======
- Given adjacentPairs list.
- elements are unique.
- adjacentPairs is valid.
- Return original array.

Brute Force (Intuition):
========================
adjacentPairs = [[2,1],[3,4],[3,2]]

2 -- 1
|       ==> [1, 2, 3, 4] or [4, 3, 2, 1]
3 -- 4

1. Find the node with one connected edge.
    1.1. Iterate through edges in adjacentPairs & construct a graph. O(E)
    1.2. Iterate through the adjecency list and find the first node with one edge. O(V)
2. DFS from that node. O(V+E)
    2.1. DFS while writing to a result array.

2 -- 1
|
3 -- 4

1. Find node [1].
2. [1] -> [2] -> [3] -> [4].

TC: O(V+E) ~= O(V), since E = V - 1 for this case.
SC: O(V), V = len(result) | number of nodes.
"""

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Construct a graph.
        graph = defaultdict(list)
        for edge in adjacentPairs:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # Find a root node.
        root = None
        for node, edges in graph.items():
            if len(edges) == 1:
                root = node
                break
        
        # DFS.
        # Given we know that our graph is a doubly-linked list,
        # we can simply check if neighbor != prev instead of
        # using a general-purposed visited set.
        restored = []
        def dfs(node, prev):
            restored.append(node)
            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, node)

        dfs(root, None)
        return restored
